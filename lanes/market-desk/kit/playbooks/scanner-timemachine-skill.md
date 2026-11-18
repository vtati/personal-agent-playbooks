---
name: market-desk-scanner-timemachine
description: Run the Scanner (R17 idea pipeline) and Time Machine (R18 pre-trade simulation gate) for the market desk's pilot account. Use for idea candidates, Friday idea slot prep, and before ANY proposed pilot order.
---

# Scanner + Time Machine

Native tools in `~/workspace/market-desk/tools/` on your broker's MCP/API
data (read tools only — neither tool can place orders). Playbook:
`~/workspace/market-desk/PLAYBOOK.md` rules R17 (Scanner) and R18 (Time
Machine gate). Design: `tools/DESIGN.md`.

## Scanner — idea pipeline (R17)

- Run: `cd ~/workspace/market-desk/tools && python3 scanner.py --top 15 --enrich 30`
  (~2 min; per-symbol financials calls dominate).
- Stage 1 hard filters live server-side (your broker's screener): STOCK,
  cap ≥ $10B, EPS > 0, fwd P/E 5–35, RSI(14,1d) 40–70, price ≥ $10.
  Expect a few hundred survivors.
- Stage 2 re-ranks by the R7 score (0–100). Read `runs/scan-<date>.md`
  for the table; check the "Missing data" column — a missing leg scored 0
  and is named, never passed silently.
- A hit is a CANDIDATE for the Friday idea slot, not a buy. Open R7 legs
  on every candidate: FCF after capex + balance sheet still need
  evidence; then full R14 (News → Chart → Skeptic → Sizer).

## Time Machine — pre-trade gate (R18, mandatory before any pilot order)

- Run: `python3 time_machine.py <SYMBOL> --pilot <YOUR PILOT VALUE> --entry <px> --stop <px> --target <px> --horizon <trading days, default 20>`
- Omit entry to use the latest close; omitted stop/target default to
  −5%/+10% and are labelled as defaults in the report — prefer explicit
  levels from the Chart step.
- Verdicts: PASS (blended expectancy ≥ +0.20R and P(stop) ≤ 45%), WATCH
  (0 to +0.20R, or earnings inside horizon — R8), VETO (expectancy < 0 or
  P(stop) > 45%). VETO is binding on the Skeptic: the order does not
  proceed at those levels; re-level (wider stop for volatile names) and
  re-run, or drop the idea.
- Sizing printed by the tool already applies R10/R16: 1% pilot risk
  budget, 10%-of-pilot single-name cap.
- Always quote the report's own caveat: base rates from past paths, not
  predictions.

## Tests

- `python3 ~/workspace/market-desk/tools/tests/run_tests.py` — 20
  pure-function tests (first passage, expectancy, gate thresholds,
  sizing caps, scoring). Must be green before relying on a code change
  to either tool.

## Data quirks (from the reference build — re-verify on your broker)

- Scanner margin/ROE columns may arrive as fractions (0.2923 = 29.23%) —
  scanner.py normalizes via `_pct`.
- SMA indicator shape: `results[].indicators[0].series[-1].value`.
- Financials results can contain null entries and fewer than 8 parseable
  quarters — the growth leg goes partial and is named in the output.
- Screener predicates may use symbols (">", "BETWEEN", "="), not enum
  names.
