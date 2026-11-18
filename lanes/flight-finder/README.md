# Flight Finder — a personal flight-research agent

Flight Finder is a personal agent that does the tedious part of flight
shopping for you. You give it four things — where from, where to, dates, and
who is traveling — and it researches the market properly and comes back with
a short, honest answer: 3–5 complete options, one recommendation, a computed
1–10 deal score, and a clear **BOOK NOW / WAIT / PIVOT** verdict.

It is a *research* agent, not a booking bot. It ranks options on **true total
cost** (fare + checked bags + seat selection + ground-transport differences,
for every traveler, both directions) instead of the headline fare, checks
more than one source before trusting a price, flexes your dates, and keeps
watching after the verdict — so a fare drop or a schedule change never slips
past you.

## What you need

- **An AI agent with web/browser access.** The agent needs to read live
  flight-search pages (a metasearch site such as Google Flights, plus
  airline sites) to cross-check prices. That alone is enough to run it.
- **Optionally, a flight-search API** for faster, structured inventory
  search. Any of these classes of service works — the engine treats data
  sources as swappable tiers (see `playbook/ENGINE.md` §3):
  - a bookable-inventory API (e.g. Duffel, Amadeus Flight Offers),
  - a search-results API (e.g. SerpApi's Google Flights endpoint),
  - an award-availability tool if you want the points lane priced beside
    cash.
- **A place to keep three small files:** your traveler profile, the deal
  log, and this playbook folder. Plain markdown is fine.

## How setup works

Setup is guided. Paste the contents of `SETUP-KICKOFF-PROMPT.txt` into a
fresh chat with your agent, and it will interview you phase by phase:

1. **Traveler profile** — it walks you through `PROFILE.template.md`
   (home airports, party, bag habits, points balances, value of time,
   flexibility) and saves your answers as `PROFILE.md`.
2. **Data sources** — it binds whatever search tiers you have (API and/or
   browser metasearch) and tells you honestly what coverage you get.
3. **Calibration trip** — it runs one real upcoming trip end-to-end so you
   can see the output format and it can start your deal log.
4. **Watch preferences** — you agree alert thresholds and cadence.
5. **Watches on** — only after the first four phases check out does it
   enable any scheduled price watches.

Nothing is booked during setup, and the agent confirms each phase with you
before moving to the next.

## The input contract

Every search needs only:

- **From** — city or airport
- **To** — city or airport
- **Dates** — departure and return (or one-way)
- **Adults** — count
- **Kids** — count + each child's age (age on the *final* travel date —
  that is what fares price on)

Everything else — home airports, bags, points, flexibility windows — comes
from your saved profile. What you say in a request overrides the profile.

## The safety rule

**Research-only by default.** The agent never books anything without your
explicit "book it" **plus** passport-exact names and dates of birth for
every traveler, supplied for that booking. Approval is per-booking, never
standing. A booking only counts as booked when the confirmation is verified
in the system of record (the booking reference read back) — never from a
checkout screen alone.

## What's in this package

- `SETUP-KICKOFF-PROMPT.txt` — paste into a fresh agent chat to set up.
- `playbook/PLAYBOOK.md` — the full operating protocol: input contract,
  search protocol, money rules, scoring, verdicts, watch rules, hard rules.
- `playbook/ENGINE.md` — the run-agent spec: state machine, data-source
  tiers, watch engine, records, and the porting checklist.
- `playbook/RESEARCH.md` — the evidence base. Every technique in the
  playbook is graded here (A = data-backed, B = conditional, C = myth —
  and Grade C myths like "book on Tuesday" are banned from the engine).
- `playbook/DEAL-LOG.md` — a blank calibration ledger. One row per scored
  run; this history is what keeps future deal scores honest.
- `playbook/templates/PROFILE.template.md` — the traveler-profile template
  the setup interview fills in.

## How a run works, in one paragraph

The agent reads your profile, expands the search to every airport within
~150 miles on both ends (priced net of ground transport), searches the full
party across sources, flexes dates ±1–3 days, records the route's typical
price as a baseline, normalizes every candidate to true total cost, scores
it 1–10 against the baseline with the arithmetic shown, and presents 3–5
options with one recommendation and a BOOK NOW / WAIT / PIVOT verdict —
including a coverage note stating exactly what was searched and what, if
anything, failed. Unbooked trips go on a price watch; booked trips stay on
watch for fare drops and schedule changes until departure.
