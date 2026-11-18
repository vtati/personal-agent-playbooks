#!/usr/bin/env python3
"""Scanner — universe screen for the MCP pilot idea pipeline (Playbook R17).

Stage 1: your broker's native screener (preview_scan or equivalent) with hard filters (read-only, saves nothing):
  STOCK, market cap >= $10B, EPS > 0, forward P/E 5–35, RSI(14,1d) 40–70, price >= $10.
Stage 2: the desk re-ranks, R7 five-checks scored 0–100 (see score_candidate).
  Legs still needing human evidence (FCF after capex, balance sheet) are reported
  OPEN on every candidate — a scanner hit is a candidate, never a buy signal.

CLI: python3 scanner.py [--top 15] [--enrich 30]
Outputs runs/scan-<date>.md + .json
"""
import argparse, datetime as dt, json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from broker_client import call_tool, batches

RUNS = pathlib.Path(__file__).resolve().parent / "runs"
REGIME_FWD_PE = 18.7  # EXAMPLE anchor only — replace with YOUR market's current forward P/E from your playbook regime snapshot (§0)

# ---------------- pure scoring (unit-tested) ----------------

def score_candidate(forward_pe, net_margin, roe, revenue_growth_pct, income_growth_pct,
                    buy, hold, sell, price, sma50, rsi):
    """R7-scored 0–100. Every missing input scores 0 for its leg and is NAMED in 'missing'."""
    missing = []
    legs = {}

    # Valuation (25) — forward P/E vs the regime anchor
    if forward_pe is None or forward_pe <= 0:
        legs["valuation"] = 0; missing.append("forward_pe")
    elif forward_pe <= 15: legs["valuation"] = 25
    elif forward_pe <= 20: legs["valuation"] = 20
    elif forward_pe <= 25: legs["valuation"] = 15
    elif forward_pe <= 30: legs["valuation"] = 10
    elif forward_pe <= 35: legs["valuation"] = 5
    else: legs["valuation"] = 0

    # Profitability (25) — net margin (15) + ROE (10)
    prof = 0
    if net_margin is None:
        missing.append("net_margin")
    elif net_margin >= 20: prof += 15
    elif net_margin >= 10: prof += 11
    elif net_margin >= 5: prof += 7
    elif net_margin >= 0: prof += 3
    if roe is None:
        missing.append("roe")
    elif roe >= 20: prof += 10
    elif roe >= 10: prof += 7
    elif roe >= 5: prof += 4
    elif roe >= 0: prof += 2
    legs["profitability"] = prof

    # Growth (20) — revenue (10) + net income (10), last 4Q vs prior 4Q
    growth = 0
    for label, val in (("revenue_growth", revenue_growth_pct), ("income_growth", income_growth_pct)):
        if val is None:
            missing.append(label)
        elif val >= 15: growth += 10
        elif val >= 5: growth += 7
        elif val >= 0: growth += 4
    legs["growth"] = growth

    # Analyst tone (15) — buy share of ratings
    if buy is None or hold is None or sell is None or (buy + hold + sell) < 5:
        legs["analyst"] = 0; missing.append("analyst_ratings")
    else:
        ratio = buy / (buy + hold + sell)
        legs["analyst"] = round(15 * max(0.0, (ratio - 0.2) / 0.8))

    # Trend (15) — price vs SMA50 (8) + RSI zone (7); R12: no chasing >70, no knives <30
    trend = 0
    if price is None or sma50 is None:
        missing.append("sma50_trend")
    elif price > sma50:
        trend += 8
    if rsi is None:
        missing.append("rsi")
    elif 45 <= rsi <= 65: trend += 7
    elif 40 <= rsi < 45 or 65 < rsi <= 70: trend += 4
    elif 30 <= rsi < 40: trend += 2
    legs["trend"] = trend

    return {"total": int(round(sum(legs.values()))), "legs": legs, "missing": missing}

# ---------------- live data helpers ----------------

def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _pct(v):
    """Scanner margin/ROE columns arrive as fractions (0.2923 = 29.23%).
    Normalize to percent units for scoring; values already >1 are left alone."""
    if v is None:
        return None
    return v * 100 if abs(v) <= 1.0 else v


def stage1_filters():
    return [
        {"filter_type": "FILTER_TYPE_INSTRUMENT_TYPE", "predicate": "=", "values": ["STOCK"]},
        {"filter_type": "FILTER_TYPE_MARKET_CAP", "predicate": ">", "values": ["10000000000"]},
        {"filter_type": "FILTER_TYPE_EPS", "predicate": ">", "values": ["0"]},
        {"filter_type": "FILTER_TYPE_FORWARD_PE", "predicate": "BETWEEN", "values": ["5", "35"]},
        {"filter_type": "FILTER_TYPE_RSI", "predicate": "BETWEEN", "values": ["40", "70"], "interval": "1d", "length": 14},
        {"filter_type": "FILTER_TYPE_LAST", "predicate": ">", "values": ["10"]},
    ]


SCAN_COLUMNS = [
    {"display_name": "Forward P/E"},
    {"display_name": "Net profit margin"},
    {"display_name": "Return on equity"},
    {"display_name": "Gross margin"},
    {"display_name": "Market cap"},
]


def run_stage1():
    try:
        data = call_tool("preview_scan", {"filters": stage1_filters(), "columns": SCAN_COLUMNS})
    except Exception:
        data = call_tool("preview_scan", {"filters": stage1_filters()})
    result = data.get("result", data)
    rows = []
    for r in result.get("results", []):
        cols = r.get("columns", {})
        rows.append({
            "symbol": r.get("ticker") or cols.get("Symbol"),
            "name": cols.get("Name"),
            "price": _f(cols.get("Last")),
            "forward_pe": _f(cols.get("Forward P/E")),
            "net_margin": _pct(_f(cols.get("Net profit margin"))),
            "roe": _pct(_f(cols.get("Return on equity"))),
            "market_cap": _f(cols.get("Market cap")),
            "rsi": _f(cols.get("RSI (14, 1D)") or cols.get("RSI")),
            "columns": cols,
        })
    return result.get("total_items", len(rows)), [r for r in rows if r["symbol"]]


def growth_from_financials(symbol):
    """Revenue / net-income growth: sum of last 4 quarters vs prior 4. Defensive parser
    over get_financials — returns (rev_growth_pct, income_growth_pct, gap_note)."""
    try:
        data = call_tool("get_financials", {"symbols": [symbol], "period": "quarterly", "limit": 8})
    except Exception as e:
        return None, None, f"financials unavailable ({e})"
    series = {"revenue": [], "income": []}

    def walk(obj):
        if isinstance(obj, dict):
            keys = {k.lower(): k for k in obj}
            for want, bucket in (("revenue", "revenue"), ("net_income", "income"), ("net income", "income")):
                for lk, orig in keys.items():
                    if want.replace("_", " ") in lk.replace("_", " ") and isinstance(obj[orig], (int, float, str)):
                        v = _f(obj[orig])
                        if v is not None:
                            series[bucket].append(v)
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)

    results = [r for r in data.get("results", []) if isinstance(r, dict)]
    mine = next((r for r in results if r.get("symbol") == symbol), None) or data
    walk(mine)

    def growth(vals):
        if len(vals) < 8:
            return None
        recent, prior = sum(vals[:4]), sum(vals[4:8])
        if prior == 0:
            return None
        return (recent - prior) / abs(prior) * 100

    rg, ig = growth(series["revenue"]), growth(series["income"])
    note = None if (rg is not None and ig is not None) else "fewer than 8 quarters parsed — growth leg partial"
    return rg, ig, note


def enrich(candidates):
    symbols = [c["symbol"] for c in candidates]
    ratings, sma = {}, {}
    for batch in batches(symbols, 16):
        try:
            data = call_tool("get_equity_analyst_ratings", {"symbols": batch})
            for r in data.get("results", []):
                ratings[r["symbol"]] = r.get("ratings", {})
        except Exception:
            pass
    start = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=400)).strftime("%Y-%m-%dT%H:%M:%SZ")
    for batch in batches(symbols, 10):
        try:
            data = call_tool("get_equity_technical_indicators", {
                "symbols": batch, "type": "sma", "interval": "day",
                "start_time": start, "period": 50, "output": "latest",
            })
            for r in data.get("results", []):
                # shape: results[].indicators[0].series[-1].value (verified live 2026-11-06)
                v = None
                for ind in r.get("indicators", []):
                    series = ind.get("series", [])
                    if series:
                        v = _f(series[-1].get("value"))
                if r.get("symbol") and v:
                    sma[r["symbol"]] = v
        except Exception:
            pass
    for c in candidates:
        rt = ratings.get(c["symbol"], {})
        c["buy"], c["hold"], c["sell"] = rt.get("num_buy_ratings"), rt.get("num_hold_ratings"), rt.get("num_sell_ratings")
        c["sma50"] = sma.get(c["symbol"])
        rg, ig, note = growth_from_financials(c["symbol"])
        c["revenue_growth_pct"], c["income_growth_pct"], c["growth_note"] = rg, ig, note
        scored = score_candidate(c["forward_pe"], c["net_margin"], c["roe"], rg, ig,
                                 c["buy"], c["hold"], c["sell"], c["price"], c["sma50"], c["rsi"])
        c["score"] = scored
    return candidates


def held_symbols():
    held = set()
    try:
        accounts = json.loads((pathlib.Path(__file__).resolve().parents[1] / "accounts.json").read_text())
        text = accounts["content"][0]["text"] if "content" in accounts else json.dumps(accounts)
        data = json.loads(text).get("data", {})
        for acct in data.get("accounts", []):
            num = acct.get("account_number")
            if not num:
                continue
            try:
                pos = call_tool("get_equity_positions", {"account_number": num})
                for p in pos.get("positions", pos.get("results", [])):
                    if p.get("symbol"):
                        held.add(p["symbol"])
            except Exception:
                pass
    except Exception:
        pass
    return held


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--enrich", type=int, default=30)
    a = ap.parse_args()

    total, rows = run_stage1()
    held = held_symbols()
    for r in rows:
        r["held"] = r["symbol"] in held
    candidates = enrich(rows[: a.enrich])
    candidates.sort(key=lambda c: c["score"]["total"], reverse=True)
    top = candidates[: a.top]

    stamp = dt.date.today().isoformat()
    RUNS.mkdir(parents=True, exist_ok=True)
    payload = {"run_at": dt.datetime.now().isoformat(timespec="seconds"),
               "stage1_total": total, "enriched": len(candidates), "candidates": top}
    (RUNS / f"scan-{stamp}.json").write_text(json.dumps(payload, indent=1))

    lines = [
        f"# Scanner — MCP pilot idea pipeline ({stamp})",
        "",
        f"Stage 1 (broker screen): {total} names passed the hard filters "
        "(stock, mkt cap ≥ $10B, EPS > 0, fwd P/E 5–35, RSI 40–70, price ≥ $10).",
        f"Stage 2: top {len(candidates)} enriched and R7-scored; best {len(top)} below.",
        "Every candidate still has OPEN R7 legs: FCF after capex + balance sheet need evidence before any buy case (R7/R14).",
        "A scanner hit is a candidate for the Friday idea slot — not a buy signal.",
        "",
        "| # | Symbol | Score | Val | Prof | Growth | Analyst | Trend | Price | Fwd P/E | Margin | RSI | Held | Missing data |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, c in enumerate(top, 1):
        s = c["score"]; L = s["legs"]
        lines.append(
            f"| {i} | {c['symbol']} | **{s['total']}** | {L['valuation']} | {L['profitability']} | {L['growth']} | {L['analyst']} | {L['trend']} "
            f"| ${c['price']:.2f} | {c['forward_pe'] if c['forward_pe'] else '—'} | {c['net_margin'] if c['net_margin'] is not None else '—'} "
            f"| {c['rsi'] if c['rsi'] else '—'} | {'yes' if c['held'] else ''} | {', '.join(s['missing']) or '—'} |"
        )
    md = "\n".join(lines) + "\n"
    (RUNS / f"scan-{stamp}.md").write_text(md)
    print(md)


if __name__ == "__main__":
    main()
