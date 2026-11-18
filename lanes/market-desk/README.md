# Market-Monitoring Desk — a personal agent system for your portfolio

A personal agent system that watches a stock portfolio for you: it reads
your accounts, follows a written investing playbook, and produces a
**pre-market brief**, **intraday trigger watches**, a **close wrap**, and a
**monthly playbook review**. It is a research and recommendations desk —
**a human makes every final trade decision.**

## What it does

- **Pre-market brief** (weekday mornings): market setup, what touches
  your holdings today (earnings, events, analyst actions, big movers with
  sourced reasons), and at most 3 suggested actions — each with the
  playbook rule behind it and the risk if wrong. "No action today" is a
  common, valid answer.
- **Intraday watches** (3 checkpoints a day): trigger-only. A holding
  moving ±3%, breaking news on a held name, an earnings print due today,
  a central-bank decision, a broad-market move — or silence ("all
  quiet"). Scheduled runs never trade.
- **Close wrap** (after the close): the day's result, a thesis check with
  a **skeptic pass** (argue against the day's most tempting trade first),
  tomorrow's queued actions, and a running scoreboard. Fridays add a
  weekly idea candidate and playbook-refinement proposals.
- **Monthly playbook review**: a refreshed market-regime snapshot, a
  **graded scorecard of every call the desk made** (including the value of
  doing nothing), and numbered playbook change proposals.
- **Decision discipline built in**: a five-check gate before any buy
  (earnings revisions, cash conversion, balance sheet, valuation,
  scenarios), a Scout → News → Chart → **Skeptic** → Sizer workflow with
  a binding skeptic veto, a base-rate "Time Machine" simulation gate
  before any pilot trade, concentration caps, and recovery-math checks
  before averaging down.

## The pilot account (optional)

If your broker offers a dedicated agent account, the desk can also run a
small self-funded **pilot**: the agent places orders only there, only
under your standing grant, and **every order pends your in-app approval**
— with strict sizing (single-name cap 10% of the pilot, ≤1% of the pilot
at risk per trade, a −15% drawdown pause) and every order pre-logged.
If your broker has no agent account, skip the pilot: read + recommend is
a complete configuration.

## What you need

- A brokerage account **you** control, at [YOUR BROKER].
- Market-data access: ideally your broker's official MCP/API connection
  (the kit documents the pattern, with one broker's MCP as a worked
  example); otherwise exported statements/positions you provide.
- An agent platform with scheduling (to run the six jobs), a secure
  credential vault, and chat delivery.
- A playbook: the kit's `playbooks/PLAYBOOK.md` is a template — you adapt
  the thresholds and write your own regime snapshot from your own
  research.

## How setup works

1. Copy this lane into your agent's workspace.
2. Feed `kit/SETUP-KICKOFF-PROMPT.txt` to your new agent. It reads the
   whole kit first, then **interviews you phase by phase** (risk basics,
   accounts, pilot size), requests each access grant with exact
   instructions, and waits for your confirmation at every step.
3. Setup runs in phases: interview → broker connection (reads +
   review tools only) → account verification incl. the **trade-approvals
   safety gate** → workspace install → a manual test cycle (one hand-run
   brief, tool tests green, one small supervised test trade if the pilot
   is used) → your go-live → only then are the six scheduled jobs
   created.

## The cadence (generic)

| When | What |
|---|---|
| Mon–Fri 08:30 (market time) | Pre-market brief |
| Mon–Fri 10:30 / 13:30 / 15:30 | Intraday trigger watches |
| Mon–Fri 16:15 | Close wrap (Fridays: + refinement & idea) |
| Monthly, day 1, 17:00 | Playbook review: regime refresh + scorecard |

Full job bodies live in `kit/jobs/` — substitute your chat ID and
timezone when you create them.

## Disclaimer

This is a personal research workflow shared for educational purposes. It
is **not financial advice**, not a recommendation to buy or sell any
security, and not a substitute for a licensed financial adviser. Markets
carry risk, including loss of principal. Any agent-assisted trading
features are optional, off by default, and gated behind your own
broker's human-approval controls; you are responsible for every decision
on your accounts.
