# Market-Monitoring Desk — Replication Kit

A personal stock-portfolio research desk: an agent analyzes your real
portfolio daily, maintains an evidence-based investing playbook, suggests
adjustments for your main account (you execute those yourself), and — only
if your broker supports an agent account and you grant it — manages a
small dedicated pilot account where **every order still pends your in-app
approval**.

Layout:

- `00`–`11` setup + operating docs (read in order)
- `SETUP-KICKOFF-PROMPT.txt` — paste into a fresh agent account to start
  the interview-driven rebuild
- `jobs/` — the six scheduled jobs, full saved bodies (chat IDs are
  placeholders you substitute)
- `scripts/` — connector pattern + Scanner/Time Machine tools + tests
- `playbooks/` — PLAYBOOK.md (the standing rulebook, as a template you
  adapt), the Scanner/Time Machine skill, a blank trade-log template, and
  a blank holdings-analysis template
- `brand/` — no visual brand; voice/standards live in doc 08

Honest limits: no credentials transfer (OAuth is re-done by you, in your
own hands); portfolio state starts from your fresh account's live reads,
not from any snapshot; your broker's MCP/API terms and toolset may drift —
doc 04 carries a worked example and the re-verification steps.

> This kit is a personal research workflow, not financial advice. See the
> lane README (`../README.md`) for the full disclaimer.
