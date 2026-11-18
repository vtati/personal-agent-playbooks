# Personal Agent Playbooks — Show & Tell

Three working **personal agents**, packaged so anyone can set them up on their
own AI agent account and run them. A personal agent is not a chatbot you
prompt once — it is a standing worker with **memory, tools, a schedule, and a
playbook**, operating under one set of standing rules (a *constitution*) and
asking a human before anything irreversible.

Built as the companion package to the slide deck
**"From Chatbots to Personal Agents — Show & Tell."**

## The three agents

| Lane | What it does | Folder |
|---|---|---|
| **LinkedIn AI News Digest** | Researches AI news every day, selects and verifies stories, and produces a ready-to-post LinkedIn digest (plus a weekly Sunday edition) in a fixed scan-friendly format. | [`lanes/linkedin-digest/`](lanes/linkedin-digest/) |
| **Market-Monitoring Desk** | Watches your portfolio on a schedule — pre-market brief, intraday trigger checks, a close wrap that grades its own calls, and a monthly playbook review. Research and recommendations only; a human makes every trade decision. | [`lanes/market-desk/`](lanes/market-desk/) |
| **Flight Finder** | Takes just a route, dates, and who's traveling — then searches like a professional: alternate airports, date flexing, true-total pricing (fare + bags + seats) — and returns 3–5 options with a computed deal score and a BOOK NOW / WAIT / PIVOT verdict. | [`lanes/flight-finder/`](lanes/flight-finder/) |

## How to set one up (self-guided)

You need an AI agent that can keep memory, follow standing instructions, use
tools/connectors, and run scheduled jobs (this package was built with Muse,
but the playbooks are platform-portable markdown).

1. **Copy this repo into your agent's workspace** (clone it, or upload the
   lane folder you want).
2. **Adopt the constitution.** Start from [`AGENTS.md`](AGENTS.md) in this
   repo — a template for the standing rules every agent works under. Edit the
   bracketed parts; keep the precedence rule.
3. **Open one new chat per agent** and paste that lane's
   `SETUP-KICKOFF-PROMPT.txt` as the first message. The agent will interview
   you phase by phase — profile, accounts, tools, a supervised test run —
   and will **not** switch on any schedule until you approve a manual test
   cycle.
4. **Run it supervised for the first cycle**, correct it, and let it learn.
   Then enable the schedule.

Each lane folder contains everything the agent needs: the playbook (the
step-by-step procedure), the setup worksheet and phase guides, the scheduled
job definitions as templates, and a day-one checklist.

## The model in one picture

- **Constitution** (`AGENTS.md`) — one file of standing rules at the top.
  Always on, applies to everything, changes rarely and deliberately.
- **Lane packet** — each agent is a self-contained packet with its own small
  rules file, its own memory, and its own workflow. Local law under global
  law: it can add detail, never override the constitution.
- **Playbook → Skill** — a procedure starts as a playbook written for one
  lane. When it proves reusable, it is generalized into a *skill* any agent
  can load. These lanes are playbooks; promote from them freely.

## Safety defaults baked into every lane

- A human approves anything irreversible (publishing, booking, trading).
- Every claim is verified against a live source before it is presented.
- Each lane logs what it did, so its own accuracy can be graded over time.

## Notes

- All personal data has been scrubbed; anything in `[BRACKETS]` is yours to
  fill in during setup.
- The market-desk lane is a personal research workflow, **not financial
  advice**.
- License: MIT — copy, adapt, and share. Attribution appreciated.
