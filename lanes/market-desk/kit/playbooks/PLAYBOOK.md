# Investing Playbook — Template v1.0

Owner: [YOUR NAME]. Operator: your market-desk agent. Accounts: your main
individual account at [YOUR BROKER] (manual execution by you), a pilot
agent account ([YOUR PILOT SIZE], agent autonomy under your grant, human
trade approvals ON — if your broker offers one), other accounts
(read-only / parked).

Build your own evidence base first: research your market regime and the
studies behind each rule, save the sources, and adapt the thresholds.
This playbook is a living document: daily logs feed it, Friday close
wraps propose changes, the interactive advisory flow applies them, and
the regime snapshot refreshes monthly.

## 0. Regime snapshot — TEMPLATE (write yours; refresh monthly)

Do not trade on a stale snapshot. Fill each line from dated sources at
setup and at every monthly review:

- Policy rates: current central-bank rate, last move, market-implied path
  (cuts/hikes priced), next decision date.
- Inflation: latest headline/core prints and trend.
- Earnings & valuation: index EPS growth (latest season), forward P/E vs
  its 5-yr and 10-yr averages, trailing P/E / CAPE, equity risk premium.
- Concentration: top-10 share of the index; what theme dominates it.
- Credit & growth: IG/HY spreads, GDP trend, unemployment, recession
  signals you track (e.g. Sahm rule).
- Factors: value vs growth and domestic vs international performance YTD;
  published long-horizon outlooks you trust.
- Rates & cash: 10-yr yield, real yield, T-bill yield (is cash a real
  asset right now?), stock–bond correlation.
- Next tests: the dated events that could change this snapshot (major
  earnings, central-bank meetings, data prints).

## 1. Account architecture

- **Main account = the compounding core.** Long-term holdings, ETF
  skeleton plus deliberate single-name tilts. You execute all trades
  manually from the desk's written recommendations. No margin use, ever,
  without a separate explicit decision.
- **Pilot account = the experiment.** The agent places orders
  autonomously under your autonomy grant; every order is logged in
  TRADE-LOG.md and reported the same day. Trade approvals stay ON: your
  in-app tap is the execution gate. Benchmark: a broad index ETF
  buy-and-hold. If the pilot cannot beat or match it with less drama over
  a quarter, the strategy gets rebuilt, not scaled.
- **Other accounts = parked.** No role until you assign one.

## 2. The rules

**R1 — Allocation anchor.** The portfolio is judged against a written
structure, not headlines: an ETF core (e.g. US total/SPX, developed
international, emerging markets, small/mid, REIT, intermediate bonds,
gold) carries the base; single names are a satellite with a job each. Any
trade that cannot name which bucket it serves does not happen.

**R2 — Concentration caps.** Default single-stock cap 5% of equity value;
10% is a hard ceiling requiring a written reduction plan. Index
look-through counts: aggregate an index fund's top holdings with your
direct exposure to the same names before judging sector/theme weight.
(Evidence: Bessembinder — ~4% of stocks created all net wealth above
T-bills; most single stocks underperform cash over their lives.)

**R3 — Rebalancing.** Semi-annual check plus 5-percentage-point bands
(5/25 for small sleeves). Rebalance with cash flows first; sell in
taxable only on a material breach. Rebalancing is risk control, not a
return trick.

**R4 — Recovery math gate.** Before averaging down, state the math out
loud: −20% needs +25%, −30% needs +43%, −50% needs +100%, −60% needs
+150%. Adding to a loser requires the fresh-money thesis (R7) to pass at
the new price AND the post-add weight to respect R2. Otherwise the
position is an exit candidate, not a bargain.

**R5 — Tax-loss harvesting (main account, taxable; adapt to your
jurisdiction).** Harvest losers against realized gains first, then up to
the annual ordinary-income limit (US: $3,000/yr); carry the rest forward.
Wash-sale discipline: no repurchase of a substantially identical security
within 30 days either side, in any household account including retirement
accounts (a retirement-account repurchase can kill the loss permanently,
under US rules). Stay invested via a different-index replacement when
exposure is still wanted. Best window: late in the tax year, paired with
any planned winner-trims so gains are sheltered. Skip harvesting when the
loss is trivial or nothing can absorb it.

**R6 — Cash deployment.** Lump sum is the default (it beat 12-month
dollar-cost averaging ~68% of the time by ~2.3pp in Vanguard's 1976–2022
study). DCA is allowed only as a written, dated schedule of ≤3 tranches
when a known binary event (central-bank decision, a portfolio-moving
earnings print) sits inside the window — and the schedule is kept even if
the event resolves calmly. Set a strategic cash target appropriate to
what cash currently yields in your market.

**R7 — The five checks before any buy or add.** (1) Earnings revisions
rising or stable, dispersion noted. (2) Cash conversion: free cash flow
vs earnings over 3–5 years. (3) Balance sheet: net debt/EBITDA, coverage,
share-count trend. (4) Valuation vs its own 5–10-yr history and true
peers. (5) Bull/base/bear scenarios in writing. Addendum for
theme-linked names (e.g. AI capex names): free cash flow after capex —
who funds the capex, and does the market currently reward or punish this
name's spending?

**R8 — Earnings-event rule.** No new buys or adds in a name within 5
trading days before its earnings unless the position is explicitly a
small, pre-sized event trade. Every holding gets a thesis check at its
print: beat/miss matters less than guidance and estimate revisions after.

**R9 — Exit on thesis break, never on cost basis.** Exit triggers: (a)
the written kill criteria occur; (b) two straight quarters of estimate
cuts plus deteriorating FCF or balance sheet; (c) R2 breach (trim, not
necessarily exit); (d) clearly better after-tax use of capital. A price
fall on an intact thesis is a hold/add review (R4), not a sell. Your
purchase price is not information.

**R10 — No mechanical stop-losses on core holdings.** Evidence says tight
stops reduce expected return for long-term holders and whipsaw in normal
−14% years; position size (R2/R4) is the risk control. Stops are allowed
only inside the pilot for event trades, set at placement, sized so the
stop-out costs ≤1% of the pilot.

**R11 — Drawdown pre-commitment.** A −10 to −15% intra-year index fall
is the average year (J.P. Morgan: average intra-year decline −14.2%
since 1980, yet most years finished positive). In a drawdown the default
action is the pre-committed plan (rebalance bands, staged deployment),
not a decision made under stress. Panic is a data point about position
sizing, not about the market.

**R12 — No performance chasing.** Nothing gets bought because it topped
a 1-year leaderboard or sold because it lagged one without passing
R1/R7. Investor timing costs ~1.2pp/yr (Morningstar "Mind the Gap");
this desk's job is to be on the right side of that gap.

**R13 — Position-count hygiene.** Target ≤25 lines in the main account.
Positions under 0.5% of equity value must justify existing (real thesis,
real weight path) or be folded into the core — micro-lines add monitoring
cost and decision noise, not diversification.

**R14 — Decision workflow.** Every discretionary call runs Scout (what
moved) → News (why, sourced) → Chart (levels, trend vs SMA50, RSI) →
Skeptic (argue the other side; can veto) → Sizer (R2/R4/R6 math) →
Execute or Recommend. The skeptic's veto is binding unless new evidence
answers its objection.

**R15 — Cadence.** Daily pre-market brief and close wrap are monitoring,
not trading triggers. Decisions cluster at: earnings prints (R8), the
weekly Friday review, band breaches (R3), and regime changes (Section 0
refresh). Between those, doing nothing is the default and is a decision.
**Intraday watch:** checkpoints at 10:30, 13:30, and 15:30 ET on trading
days scan for decision-grade events only — a holding moving ≥3%
intraday, breaking news on a held name (guidance, downgrades, lawsuits,
M&A), an earnings print due that day (pre-print posture / post-print
first read), central-bank decisions (14:00 ET; the 13:30 checkpoint is
the pre-decision posture, 15:30 the reaction), broad-index moves ≥1.5%,
and pilot fills or R16 limit approaches. No trigger = one line, "all
quiet." A trigger produces a prepared decision with rule citation — it
does not authorize the scheduled run itself to trade; pilot execution
still happens in the interactive flow with the owner informed the same
day.

**R16 — Pilot rules.** Max 5 positions until the process has a track
record; single-name cap 10% of the pilot; core ETFs first; no options, no
margin, no shorts, no leveraged ETFs; every order pre-logged with thesis
+ kill criteria; pilot drawdown of −15% from its starting value pauses
all new orders pending a review with the owner; results reported against
the benchmark monthly.

**R17 — Scanner.** The idea pipeline is systematic, not headline-driven:
`tools/scanner.py` runs your broker's native screen (stocks, market cap
≥ $10B, EPS > 0, forward P/E 5–35, RSI(14) 40–70, price ≥ $10) and
re-ranks survivors with the R7 score (valuation / profitability / growth
/ analyst tone / trend, 0–100, missing data named and scored 0). A
scanner hit is a candidate for the Friday idea slot only — it still
needs the open R7 legs (FCF after capex, balance sheet) evidenced and the
full R14 workflow before it is a buy case.

**R18 — Time Machine gate.** No pilot order proceeds without a
`tools/time_machine.py` run at its actual entry/stop/target/horizon:
historical-analog first-passage stats (~2y of the stock's own daily bars)
blended with a 10,000-path block-bootstrap Monte Carlo. PASS = blended
expectancy ≥ +0.20R and P(stop) ≤ 45%. VETO = expectancy < 0 or P(stop)
> 45% — binding on the Skeptic (R14). Earnings inside the horizon caps
the verdict at WATCH (R8). Sizing inside the tool follows R10/R16 (1%
pilot risk budget, 10%-of-pilot position cap). Statistics are base
rates, never predictions, and every report says so. Record your first
runs in the trade log — they become your calibration examples.

## 3. Refinement loop (standing directive: "be a continuously improving machine")

- Daily: briefs log suggestions, triggers hit/missed, and rule weaknesses
  to the daily log. Knowledge stays current — regime-moving news is
  checked every brief, not monthly.
- Weekly (Friday close wrap): which rules fired, which would have helped
  or hurt, concrete change proposals, PLUS one new idea candidate run
  through R7 and the skeptic — or an explicit "no idea cleared the bar."
- Monthly (job `market-desk-monthly-playbook-review`, 1st of month):
  full regime refresh against Section 0, a graded scorecard of every
  desk call including the value of doing nothing, pilot vs benchmark,
  and numbered playbook change proposals.
- Ideas are a standing output, not an event: whenever research surfaces a
  candidate that passes R7 + skeptic, it is brought to the owner with
  thesis, sizing, and kill criteria — in briefs, wraps, or directly in
  chat.
- Versioning: every applied change bumps the version with a dated line
  below.

## Version history

- v1.0 — template: adapt the thresholds, write your Section 0 regime
  snapshot from your own sourced research, and start your history here.
