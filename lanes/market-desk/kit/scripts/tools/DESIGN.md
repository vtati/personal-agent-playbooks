# Scanner + Time Machine — Design

Origin: two ideas from third-party "trader skill" packs, **rebuilt natively**
on the broker's own data rather than installed — never install unknown code
next to a live trading account. Scope: the pilot (agent) account ONLY. The
main account stays read-and-suggest. Nothing here places orders.

## Data source

Your broker's trading MCP (or API) should expose everything needed — no
external feed required:

- A native screener (e.g. `preview_scan`) + its filter specs
- Equity historicals (OHLCV, split-adjusted) — Time Machine price history
- Fundamentals / financials / analyst ratings — R7 enrichment
- Technical indicators (RSI, SMA, ATR…) — trend checks
- Earnings results/calendar — R8 earnings-window check

## Scanner (scanner.py)

Stage 1 — broker native screen (hard filters, playbook-bound):
STOCK only; market cap ≥ $10B; EPS > 0; forward P/E 5–35; RSI(14,1d) 40–70
(R12: no falling knives, no chasing); price ≥ $10 (no penny noise).

Stage 2 — the desk re-ranks (R7 five checks, scored 0–100):
Valuation (forward P/E vs the regime anchor in your playbook §0),
Profitability (net margin, ROE), Growth (revenue + net income trend, last
4 quarters vs prior 4), Analyst tone (buy/hold/sell mix), Trend (price vs
SMA50, RSI mid-range bonus). Missing data scores 0 for that leg and is
NAMED in the output — never silently passed.

Output: ranked top 15 with per-leg scores; the R7 legs still needing human
evidence (free cash flow after capex, balance sheet) flagged OPEN.
Markdown + JSON in `runs/`. A scanner hit is a CANDIDATE for the weekly
idea slot, not a buy signal (R14 still applies).

## Time Machine (time_machine.py)

Input: symbol, entry, stop, target, horizon (trading days, default 20),
and YOUR pilot account value (`--pilot`, required — used only for sizing).

Engine A — Historical analogs: every trading day in ~2 years of daily bars
is a hypothetical entry at that close, with the SAME % stop/target
distances; walk forward to the horizon; record first passage
(target / stop / timeout at close). Real paths, no model assumption.

Engine B — Monte Carlo: 10,000 paths, 5-day block bootstrap of the stock's
own daily log returns (preserves volatility clustering), first passage
within the horizon.

Outputs (both engines + blended): P(target), P(stop), P(timeout),
expectancy in R and in currency at the sized position, median outcome,
5th-percentile outcome, worst drawdown proxy.

Gate (Playbook R18):
- PASS — blended expectancy ≥ +0.20R AND P(stop) ≤ 45%
- WATCH — expectancy 0 to +0.20R, or earnings inside the horizon (R8)
- VETO — expectancy < 0 or P(stop) > 45% → binding on the Skeptic (R14);
  no pilot order may proceed at those levels

Sizing (R10/R16): risk budget = 1% of the pilot; shares = risk budget /
(entry − stop); position capped at 10% of the pilot (single-name cap);
size 0 if the stop distance is 0 or the cap binds below 1 share.

Earnings: a next earnings date inside the horizon forces at best WATCH,
flagged EVENT RISK.

## What this deliberately is NOT

- No day-trading entry timing (no opening-range breakouts) — conflicts
  with R11/R12/R15.
- No auto-trading. Output feeds Scout → News → Chart → Skeptic → Sizer;
  execution stays in the interactive flow, with human trade approvals ON
  where the pilot account is used at all.
- Backtest statistics are base rates from past paths, not predictions.
  Every report says so.
