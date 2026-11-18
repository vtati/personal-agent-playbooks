#!/usr/bin/env python3
"""Time Machine — pre-trade simulation gate for the MCP pilot (Playbook R18).

Two engines over the stock's OWN daily history (your broker's
get_equity_historicals or equivalent, split-adjusted):
  A) Historical analogs — every past day as a hypothetical entry with the same
     % stop/target distances; first passage within the horizon.
  B) Monte Carlo — 10,000 paths, 5-day block bootstrap of daily log returns;
     first passage within the horizon.
Blended expectancy feeds the R18 gate: PASS >= +0.20R and P(stop) <= 45%;
VETO on negative expectancy or P(stop) > 45% (binding on the Skeptic, R14);
earnings inside the horizon caps the verdict at WATCH (R8 event risk).
Sizing follows R10/R16: 1% pilot risk budget, single-name cap of 10% of the pilot.

These are base rates from past paths, NOT predictions. Every report says so.

CLI:
  python3 time_machine.py <SYMBOL> --entry 100 --stop 95 --target 110 --horizon 20
  (entry defaults to the latest close; stop/target default to -5% / +10% and are labelled as defaults)
"""
import argparse, datetime as dt, json, math, pathlib, random, statistics, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from broker_client import call_tool

RUNS = pathlib.Path(__file__).resolve().parent / "runs"

# ---------------- pure functions (unit-tested) ----------------

def classify_path(closes, stop, target, horizon, lows=None, highs=None):
    """First passage for a long position. closes[0] is the entry price.
    Returns (outcome, exit_price, days) with outcome in target|stop|timeout.
    When both barriers are crossed in the same bar, the stop wins (conservative)."""
    n = min(horizon, len(closes) - 1)
    for i in range(1, n + 1):
        if lows is not None and highs is not None:
            hit_stop = lows[i] <= stop
            hit_target = highs[i] >= target
            if hit_stop and hit_target:
                return "stop", stop, i
            if hit_stop:
                return "stop", stop, i
            if hit_target:
                return "target", target, i
        c = closes[i]
        if c <= stop:
            return "stop", stop, i
        if c >= target:
            return "target", target, i
    return "timeout", closes[n], n


def _summarize(pairs):
    """pairs: list of (outcome, R). Returns probability + expectancy stats."""
    total = len(pairs)
    if total == 0:
        return {"n": 0, "p_target": 0.0, "p_stop": 0.0, "p_timeout": 0.0,
                "expectancy_r": 0.0, "median_r": 0.0, "p05_r": 0.0}
    counts = {"target": 0, "stop": 0, "timeout": 0}
    all_r = []
    for outcome, r in pairs:
        counts[outcome] += 1
        all_r.append(r)
    srt = sorted(all_r)
    return {
        "n": total,
        "p_target": counts["target"] / total,
        "p_stop": counts["stop"] / total,
        "p_timeout": counts["timeout"] / total,
        "expectancy_r": sum(all_r) / total,
        "median_r": statistics.median(all_r),
        "p05_r": srt[max(0, int(0.05 * total) - 1)],
    }


def analog_stats(closes, stop_pct, target_pct, horizon):
    """Every day with a full horizon of forward history is a hypothetical entry."""
    pairs = []
    for s in range(0, len(closes) - horizon):
        entry = closes[s]
        if entry <= 0:
            continue
        stop = entry * (1 - stop_pct)
        target = entry * (1 + target_pct)
        outcome, exit_price, _ = classify_path(closes[s : s + horizon + 1], stop, target, horizon)
        pairs.append((outcome, (exit_price - entry) / (entry - stop)))
    return _summarize(pairs)


def monte_carlo(log_returns, start, stop, target, horizon, n_paths=10000, seed=42, block=5):
    """Block-bootstrap Monte Carlo. log_returns: the stock's daily log returns."""
    rng = random.Random(seed)
    risk = start - stop
    if risk <= 0 or not log_returns:
        return _summarize([])
    max_start = max(0, len(log_returns) - block)
    pairs = []
    for _ in range(n_paths):
        seq = []
        while len(seq) < horizon:
            j = rng.randint(0, max_start) if max_start > 0 else 0
            seq.extend(log_returns[j : j + block])
        price = start
        outcome, exit_price = "timeout", start
        for r in seq[:horizon]:
            price *= math.exp(r)
            if price <= stop:
                outcome, exit_price = "stop", stop
                break
            if price >= target:
                outcome, exit_price = "target", target
                break
        else:
            exit_price = price
        pairs.append((outcome, (exit_price - start) / risk))
    return _summarize(pairs)


def gate_verdict(expectancy_r, p_stop, earnings_in_horizon):
    """Playbook R18 gate."""
    if expectancy_r < 0:
        return "VETO"
    if p_stop > 0.45:
        return "VETO"
    if earnings_in_horizon:
        return "WATCH"
    if expectancy_r >= 0.20:
        return "PASS"
    return "WATCH"


def size_position(pilot_value, entry, stop, risk_pct=0.01, cap_dollars=None):
    """R10/R16 sizing: risk budget 1% of pilot; single-name position cap defaults
    to 10% of the pilot (pass cap_dollars to override)."""
    if cap_dollars is None:
        cap_dollars = pilot_value * 0.10
    risk_per_share = entry - stop
    if risk_per_share <= 0 or entry <= 0:
        return {"shares": 0, "position_dollars": 0, "risk_dollars": 0}
    budget = pilot_value * risk_pct
    shares = min(budget / risk_per_share, cap_dollars / entry)
    shares = round(shares, 4)
    return {
        "shares": shares,
        "position_dollars": round(shares * entry, 2),
        "risk_dollars": round(shares * risk_per_share, 2),
    }

# ---------------- live runner ----------------

def fetch_closes(symbol, years=2):
    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(days=365 * years + 10)
    data = call_tool("get_equity_historicals", {
        "symbols": [symbol],
        "start_time": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end_time": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "interval": "day", "bounds": "regular", "adjustment_type": "split",
    })
    results = data.get("results") or data.get("historicals") or []
    bars = []
    if results and isinstance(results[0], dict):
        bars = results[0].get("historicals") or results[0].get("bars") or []
    closes = []
    for b in bars:
        c = b.get("close_price") or b.get("close")
        if c:
            closes.append(float(c))
    return closes


def next_earnings_within(symbol, calendar_days):
    """Best-effort R8 check; returns (bool, date_str_or_None). Failure = (False, None) + gap noted by caller."""
    data = call_tool("get_earnings_results", {"symbol": symbol})
    today = dt.date.today()
    horizon_date = today + dt.timedelta(days=calendar_days)
    dates = []

    def walk(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if "date" in k.lower() and isinstance(v, str) and len(v) >= 10:
                    try:
                        dates.append(dt.date.fromisoformat(v[:10]))
                    except ValueError:
                        pass
                else:
                    walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)

    walk(data)
    future = sorted(d for d in dates if today <= d <= horizon_date)
    return (bool(future), future[0].isoformat() if future else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("symbol")
    ap.add_argument("--entry", type=float)
    ap.add_argument("--stop", type=float)
    ap.add_argument("--target", type=float)
    ap.add_argument("--horizon", type=int, default=20)
    ap.add_argument("--pilot", type=float, required=True, help="YOUR pilot account value, in your currency — used only for position sizing")
    ap.add_argument("--paths", type=int, default=10000)
    a = ap.parse_args()
    symbol = a.symbol.upper()

    closes = fetch_closes(symbol)
    if len(closes) < 60:
        print(f"ERROR: only {len(closes)} daily bars for {symbol} — not enough history to simulate.")
        sys.exit(2)
    entry = a.entry or closes[-1]
    defaults = []
    stop = a.stop
    if stop is None:
        stop = round(entry * 0.95, 2); defaults.append("stop = entry -5% (default)")
    target = a.target
    if target is None:
        target = round(entry * 1.10, 2); defaults.append("target = entry +10% (default)")
    if not (stop < entry < target):
        print("ERROR: need stop < entry < target for a long simulation.")
        sys.exit(2)

    stop_pct = (entry - stop) / entry
    target_pct = (target - entry) / entry
    analog = analog_stats(closes, stop_pct, target_pct, a.horizon)
    log_returns = [math.log(closes[i] / closes[i - 1]) for i in range(1, len(closes)) if closes[i - 1] > 0]
    mc = monte_carlo(log_returns, entry, stop, target, a.horizon, n_paths=a.paths, seed=42)

    blend = {
        k: (analog[k] + mc[k]) / 2 for k in ("p_target", "p_stop", "p_timeout", "expectancy_r", "median_r", "p05_r")
    }
    try:
        earn_flag, earn_date = next_earnings_within(symbol, int(a.horizon * 1.45) + 2)
        earn_note = f"next earnings {earn_date} — INSIDE horizon" if earn_flag else "no earnings date found inside horizon"
    except Exception as e:
        earn_flag, earn_date, earn_note = False, None, f"earnings check failed ({e}) — treat R8 as UNVERIFIED"
    verdict = gate_verdict(blend["expectancy_r"], blend["p_stop"], earn_flag)
    sizing = size_position(a.pilot, entry, stop)
    exp_dollars = round(blend["expectancy_r"] * sizing["risk_dollars"], 2) if sizing["shares"] else 0.0

    report = {
        "symbol": symbol, "entry": entry, "stop": stop, "target": target,
        "horizon_days": a.horizon, "history_bars": len(closes),
        "defaults_used": defaults, "analog": analog, "monte_carlo": mc, "blended": blend,
        "earnings_in_horizon": earn_flag, "earnings_note": earn_note,
        "sizing": sizing, "expectancy_dollars_at_size": exp_dollars, "verdict": verdict,
        "run_at": dt.datetime.now().isoformat(timespec="seconds"),
    }
    RUNS.mkdir(parents=True, exist_ok=True)
    stamp = dt.date.today().isoformat()
    (RUNS / f"timemachine-{symbol}-{stamp}.json").write_text(json.dumps(report, indent=1))

    def pct(x): return f"{x*100:.1f}%"
    lines = [
        f"# Time Machine — {symbol} ({stamp})",
        "",
        f"Entry ${entry:.2f} · Stop ${stop:.2f} (-{stop_pct*100:.1f}%) · Target ${target:.2f} (+{target_pct*100:.1f}%) · Horizon {a.horizon} trading days",
        ("Defaults used: " + "; ".join(defaults)) if defaults else "Levels supplied explicitly.",
        f"History: {len(closes)} daily bars. Earnings: {earn_note}.",
        "",
        "| Engine | P(target) | P(stop) | P(timeout) | Expectancy | Median | 5th pct |",
        "|---|---|---|---|---|---|---|",
        f"| Historical analogs (n={analog['n']}) | {pct(analog['p_target'])} | {pct(analog['p_stop'])} | {pct(analog['p_timeout'])} | {analog['expectancy_r']:+.2f}R | {analog['median_r']:+.2f}R | {analog['p05_r']:+.2f}R |",
        f"| Monte Carlo (n={mc['n']}) | {pct(mc['p_target'])} | {pct(mc['p_stop'])} | {pct(mc['p_timeout'])} | {mc['expectancy_r']:+.2f}R | {mc['median_r']:+.2f}R | {mc['p05_r']:+.2f}R |",
        f"| **Blended** | **{pct(blend['p_target'])}** | **{pct(blend['p_stop'])}** | **{pct(blend['p_timeout'])}** | **{blend['expectancy_r']:+.2f}R** | **{blend['median_r']:+.2f}R** | **{blend['p05_r']:+.2f}R** |",
        "",
        f"Sizing (R10/R16): {sizing['shares']} shares ≈ ${sizing['position_dollars']} position, ${sizing['risk_dollars']} at risk (1% pilot budget, 10%-of-pilot cap).",
        f"Expectancy at that size: ${exp_dollars:+.2f} per trade, before costs.",
        "",
        f"## R18 GATE VERDICT: {verdict}",
        "",
        "Base rates from this stock's own past paths — not a prediction. A PASS still needs the full R14 workflow (News, Chart, Skeptic, Sizer) before any MCP order.",
    ]
    md = "\n".join(lines) + "\n"
    (RUNS / f"timemachine-{symbol}-{stamp}.md").write_text(md)
    print(md)


if __name__ == "__main__":
    main()
