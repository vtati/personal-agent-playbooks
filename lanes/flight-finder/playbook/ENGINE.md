# Flight Finder — Run-Agent Engine Spec

**Version:** 1.0 · **Date:** 2026-11-16 · **Companion to:** `PLAYBOOK.md` v2 (the protocol) and `RESEARCH.md` (the evidence).
**Purpose:** make the playbook executable by *any* agent, on any account, with the same quality bar. The protocol is the product; the tools underneath are swappable.

## 1. Design principles

1. **State machine, not vibes.** Every trip is a record moving through named states with gates. An agent that can't name its state isn't running the system.
2. **Snapshots or it didn't happen.** Every price presented comes from a saved, timestamped search snapshot. Summaries and memory are never price sources.
3. **Coverage is declared.** Each state records what was searched and what failed. Silent gaps are the #1 failure mode of agent travel research.
4. **The human decides money.** The engine researches, scores, recommends, and — only on an explicit "book it" with passport-exact names/DOBs — books. Approval is per-booking, never standing.
5. **Portability.** Nothing in the protocol depends on a specific vendor. Data sources are tiers (§3); any implementation that satisfies a tier works.

## 2. State machine

```
INTAKE → SEARCH → SCORE → PRESENT → DECISION ──(book it)──→ BOOK → WATCH → POST-TRIP
                                  │                              │
                                  └──(wait / pivot)──→ WATCH ────┘ (re-enters SEARCH on trigger)
```

| State | Entry gate | Exit gate |
|---|---|---|
| INTAKE | Route, dates, party with kid ages on final travel date | Profile read; missing detail asked only if it changes route/price/traveler |
| SEARCH | Intake complete | All §2 protocol steps run or explicitly marked not-run with reason; snapshots saved |
| SCORE | ≥1 verified complete trip | Baseline recorded; true totals computed; score arithmetic written |
| PRESENT | Score done | Output matches §10 format incl. coverage note + timing zone |
| DECISION | Presented | Traveler's pick, "book it", WAIT (with trigger), or PIVOT recorded |
| BOOK | Explicit go + passport-exact names/DOBs | Confirmation verified in system of record (reference read back) |
| WATCH | Booked, or WAIT verdict with trigger | Cadence checks logged; drop ≥ threshold or schedule change surfaced within one check cycle |
| POST-TRIP | Travel completed | Outcome (final price paid, drops harvested, score accuracy) written to `DEAL-LOG.md` |

Failure handling: a failed source never advances the state silently — SEARCH records the failure and either substitutes the next tier or exits with a coverage note naming the gap.

## 3. Data source tiers (swap implementations freely)

| Tier | Job | Reference implementation here | Portable alternatives |
|---|---|---|---|
| 1 — Bookable inventory | Structured search across airports/dates/party; fare brands, bags, change terms; booking | Duffel connector (search, limit 300) | Amadeus Flight Offers API, SerpApi Google Flights (search-only), airline NDC APIs |
| 2 — Metasearch cross-check | Carriers Tier 1 can't sell or misprices; price insights (low/typical/high baseline); date grid | Browser read of Google Flights (3 cheapest + fastest, first page) | SerpApi / DataForSEO travel endpoints, Skyscanner/Momondo/Kayak reads |
| 3 — Airline direct | Tiebreak verification; fares Tier 1–2 can't see; award verification; booking for handoff carriers (e.g. United) | Airline sites via browser / handoff link with exact pick list | Airline apps/APIs where offered |
| 4 — Award availability | Points pricing beside cash | Airline award search (manual) | seats.aero Partner API (27 programs) |
| 5 — Deal intake | Error fares and route deals | Mailbox subscriptions: Going, Secret Flying, Jack's Flight Club | RSS/API feeds, community alerts |
| 6 — Context | Conflicts, flexibility windows, confirmations | Calendar app, email inbox | Any calendar/mail the host agent can read |

Rules: Tier 1 and Tier 2 run in parallel on every search. A Tier 2 trip that beats Tier 1 is routed (bookable? handoff? airline-direct?) before presenting. Tier 3 verification is mandatory before calling any Tier 2-only price "the price" in a booking recommendation.

## 4. Scoring module (deterministic)

Inputs: candidate true total (§6 of playbook), route baseline (typical low / typical / typical high for the season), flags, fare changeability, days-to-departure.
Output: score 1–10 with one-line arithmetic, per playbook §8.1. The module is pure math on recorded inputs — two agents given the same snapshot must produce the same score. Disagreement means an input wasn't recorded; fix the record, not the score.

Value-of-time default: $25/hr/person, stored in the profile, overridable per trip. Nonstop premium is always expressed as $/hr/person saved.

## 5. Watch engine

- A watch is a scheduled job owned by the trip record: `{route, dates, party, baseline, last_best_true_total, book_trigger, cadence, state}`.
- Cadence by distance: >8 weeks weekly · inside low-price zone 2×/week · inside 21 days daily · booked trips 2×/week until departure (drop harvest + schedule changes).
- Notify threshold: ≥5% or ≥$25/person improvement, any error-fare hit on watched airports, any schedule change on a booked trip. Everything else logs silently to the trip record.
- Watches expire at departure or on the traveler's word. A watch never books anything by itself.

## 6. Records

- **Trip record** — one file or row per trip: inputs, snapshots (paths), baseline, shortlist, score math, verdict, decision, booking reference (if any), watch state, outcome.
- **Deal log** (`DEAL-LOG.md`) — the calibration ledger: date, route, baseline, best true total, score, verdict, outcome. Reviewed quarterly; scoring bands change only from log evidence.
- **Profile** (`PROFILE.md` in this folder) — durable traveler facts. The engine reads it every run and writes back only traveler-confirmed changes.

## 7. Porting checklist (new agent / new account)

1. Copy `PLAYBOOK.md`, `RESEARCH.md`, `ENGINE.md`, `DEAL-LOG.md` template into the new workspace.
2. Create the traveler's profile from the template (`PROFILE.template.md`).
3. Bind the tiers: at minimum a Tier 1 or Tier 2 search source and a browser. The engine degrades honestly — with only Tier 2 it still runs, with wider coverage notes.
4. Subscribe the deal-intake mailbox (Tier 5).
5. Run one calibration trip end-to-end (a real upcoming trip) and log it before trusting scores.

## 8. Known limits (state them, don't hide them)

- Browser metasearch reads are one route at a time and can be bot-walled; API tiers remove this limit (Phase 3 in `UPGRADE-PLAN.md`).
- Award pricing without an award-availability API is manual and slow; the points lane is best-effort until Tier 4 is bound.
- Baselines for thin routes (few weekly flights) are unreliable — widen the score's uncertainty language instead of faking precision.
- Error-fare intake depends on third-party alert latency; the engine can miss a fare that dies in under an hour. That's inherent, not a bug to promise away.
