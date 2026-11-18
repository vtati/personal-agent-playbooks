# Flight Finder — Playbook v2

**Version:** 2.0 · **Date:** 2026-11-16 · **Supersedes:** v1 (2026-11-15)
**Purpose:** Given only a route, dates, and who's traveling, research the market properly and return the best flight options with an honest, *computed* verdict. No prompt-crafting needed from the traveler — this playbook IS the prompt, permanently.
**Evidence base:** `RESEARCH.md` (same folder). Every technique here is Grade A or B there; Grade C myths are banned in §2. **Engine spec:** `ENGINE.md`. **Change list:** `UPGRADE-PLAN.md`.

**Standing rule:** Research-only by default. Nothing is ever booked without the traveler's explicit "book it" plus passport-exact names and dates of birth for every traveler.

---

## 1. Input contract

Required (all the traveler has to give):
- **From** — city or airport
- **To** — city or airport
- **Dates** — departure and return (or one-way)
- **Adults** — count
- **Kids** — count + each child's age (age on the *final* travel date — that's what fares price on)

Read the traveler profile before searching: `PROFILE.md` in this folder (your saved preferences: home airports, party defaults, points balances and status, bag habits, value-of-time, flexibility windows). What the traveler says in this request overrides the profile; name the profile facts you used so they can correct one.

Assumed unless stated otherwise:
- Economy cabin, cheapest *sensible* option wins
- Home airports from your profile
- Checked bags: a family trip of 4+ nights needs them; always price both ways (§6)
- Flexibility: ±1 day is fair game; ±3 when the trip is far out or dates are called soft

Ask only when a missing detail would change the route, the price, or the traveler (e.g., lap vs. seat for a child under 2 — always ask, never infer).

## 2. Search protocol (run in this order, every time)

1. **Expand the map.** Search the city code (all airports at once) plus any airport within ~150 miles that could plausibly win after ground transport. Note drive time and parking/transfer cost per alternate — an alternate only counts if it's *net*-profitable after ground costs and time.
2. **Run the direct inventory search** across every airport pair, the exact dates, the full passenger mix (adults + one child-age per kid). Limit 300, requested cabin.
3. **Run the browser cross-check** (metasearch) for the carriers the direct search can't sell or prices above their own sites (United, Southwest-class, budget carriers). Read the 3 cheapest complete trips + the fastest from the first results page. When the direct search and the metasearch disagree, the airline's own site is the tiebreaker — verify there before presenting.
4. **Flex the dates.** Scan ±1–3 days (same trip length) via the date grid; report the 3 cheapest day-pairs and flag spike days. Weight *departure-day* shifts first — the day you fly moves price ~14–20%; the day you book moves it ~1–3% and is ignored.
5. **Establish the baseline.** Record the route's typical range (metasearch price insight: low / typical / high, or our own watch history in `DEAL-LOG.md`). No deal score without a baseline.
6. **Check the structural tricks** (§4) — split tickets, one-way combos, self-transfers, positioning where relevant.
7. **Price the points side** (§7) when the profile shows a relevant balance.
8. **Normalize every candidate to true total cost** (§6) before ranking anything.
9. **Score** (§8), give the **verdict** (§8.3), present in the standard format (§10).
10. **Log the run** in `DEAL-LOG.md`: baseline, best true total, score given, verdict. This is what calibrates future scores.

### Myth ban (standing)
Never spend steps on: incognito/cookie clearing to change prices, VPN point-of-sale arbitrage as a tactic, "book at 2–3 AM", "book on Tuesday", or any social-media tip that hasn't been graded in `RESEARCH.md`. Airlines price on inventory and demand, not browsing history.

## 3. Timing model (when to search, when to book)

Booking windows are **zones** (Google 5-year data; CheapAir and Expedia 2026 broadly agree on zones, not days):

| Trip | Low-price zone | Cheapest point (avg) | Danger zones |
|---|---|---|---|
| US domestic | ~3–10 weeks out (22–57 days) | ≈39 days | 6+ months out (early premium); inside 21 days (spike); inside ~7–13 days (~+26%) |
| International | ~7–19 weeks out (50–133 days) | ≈89 days | Same shape, wider zone |

Rules:
- State which zone today's search sits in, in every report. A WAIT verdict is only honest inside or before the low-price zone; inside 21 days, WAIT needs a specific reason.
- Far out (>zone): present prices as *early readings*, recommend a watch (§5), don't push booking unless the fare already scores 8+.
- Peak dates (Christmas, spring break, Thanksgiving) compress the zones — book at the early edge; the "wait for the dip" logic does not apply to immovable peak family trips.

## 4. The techniques

1. **Flexible date matrix** — cheapest date combinations in the window from the date grid; spike days named and avoided.
2. **Radius & alternate routes** — all commercial airports within ~150 miles on both ends, priced *with* ground transport and time; verdict on net profitability. Positioning to a cheaper origin is the same technique at premium-cabin scale (worth steps only for long-haul premium or very large gaps).
3. **Split tickets & one-way combos** — two one-ways (same or different carriers) priced against the round trip. Label the risk: a delay or change on one ticket is not protected by the other. Bonus, stated when relevant: two one-ways can each be repriced independently if fares drop after booking (§9).
4. **Self-transfer / layover arbitrage** — only with a stated safety buffer (≥3h same-airport), baggage re-check rules, transit-visa check, and the failure cost in dollars. A guaranteed virtual-interline product (seller covers the misconnect) is a different, safer product than a naked self-transfer — never present them as equivalent.
5. **Hidden-city ticketing** — mention only when the saving is large, always with the full risk card: violates airline terms, checked bags go to the ticketed final city (carry-on only), skipping a segment cancels the rest of the itinerary, frequent-flyer credit/status can be forfeited. Never for family trips with checked bags; never on a carrier where the traveler holds status they value.
6. **Error fares** — not searchable on demand; they arrive via the alert intake (§5.3) and run the fast lane there.
7. **All-inclusive fee scanner** — seat selection (carrier-aware, §6), baggage, carrier surcharges; on the hotel side: resort fees, local tourist taxes, parking, transfers. The fare is never the price.
8. **Destination flex** — when the destination is softer than the dates, run an Explore/Everywhere pass and present the cheapest appealing destinations as a PIVOT option.

## 5. Watching & intake (deals come from movement)

### 5.1 Price watch
Every presented trip that isn't booked gets a watch entry: route, dates, party, baseline, best true total seen, and a **book-trigger** (a target price or score ≥8). Re-check cadence: weekly when >8 weeks out; twice weekly inside the low-price zone; daily inside 21 days. A drop of **≥5% or ≥$25/person** vs the last report is worth a message; smaller moves are logged silently.

### 5.2 After-booking watch
Booked trips stay on watch until departure (§9): fare drops on changeable fares, schedule changes (which can create refund rights), and equipment/nonstop changes are all reportable.

### 5.3 Error-fare fast lane
Alert sources (subscribed once, monitored in the traveler's mailbox): Going, Secret Flying, Jack's Flight Club, route-specific alerts. On a plausible hit for the traveler's airports/flexibility:
1. Verify the fare is live (direct inventory + airline site) — most die within 1–3 hours.
2. Present immediately with the typical price beside it and the score; verdict is BOOK NOW by construction.
3. Book **direct with the airline**; never call the airline about the price; don't attach non-refundable hotels/car until the ticket shows as issued/confirmed.

## 6. Money rules (the math that decides)

- **True total = fare + checked bags + seat selection (where actually chargeable, below) + ground-transport deltas**, for *all* travelers, both directions. Rank on this, never the headline fare.
- **Family seating is carrier-aware.** Carriers that *guarantee* a child ≤13 sits next to an accompanying adult free on every fare (DOT Family Seating Dashboard, Sep 2026): **Alaska, American, Frontier, Hawaiian, JetBlue** — price seat selection at $0 for adjacency on these (same reservation required). Carriers with **no guarantee — Allegiant, Delta, Southwest, United** — price seat selection in, or state plainly that adjacency isn't assured on the cheap fare. Re-check the dashboard each run; the list can change and the proposed federal rule is not final.
- **The bag step-up test:** the fare one class up (bags included) is often cheaper than Basic + paid bags — always price it. On non-guarantee carriers run the same test for the fare that includes seat selection. Note what the step-up buys beyond bags (usually free changes — which powers §9).
- **Basic Economy discount-rate:** when departure is far out and the fare is likely to move, Basic's unchangeability has a real expected cost (it kills the price-drop harvest, §9). Say so in the red flags; don't pretend Basic and Standard differ only by bags.
- **The 24-hour rule (US DOT):** flights booked 7+ days before departure can be cancelled for a full refund within 24 hours. This makes BOOK NOW the right call on a great fare — lock it, verify calmly, cancel free if it's wrong. Say this out loud whenever the verdict is BOOK NOW.
- **Kids price by age on the final travel date.** A child searched as an adult is priced and ticketed wrong.
- **Nonstop premium test:** price the nonstop in **$/hour saved per person** against the traveler's value-of-time (profile; default $25/hr/person, and weight it up for late-night arrivals or travel days with young kids). Nonstops average ~+20%; below the value-of-time line it's a buy, above it it's a luxury — say which.

## 7. Points lane (when the profile holds a relevant balance)

- Price the award for the same trip and compute **cents-per-point = (cash true total − award taxes/fees) ÷ points**. Show cash and points side by side with the cpp.
- **Saver vs dynamic, always stated.** Saver/partner space is where points win; dynamic prices track cash and usually lose. Program bars (verify per run): United MileagePlus — miles+cash floor ≈1.0¢, redeem at **≥1.5¢** on verified saver space, otherwise pay cash. Re-derive bars for other programs from current data, don't reuse United's.
- Award availability tools (seats.aero-class) may be used when connected; whatever the tool says, **verify the award on the airline's own site before any points transfer** — transfers are irreversible.
- Points totals are for the whole party: 4 award seats on one flight is a different availability problem than 1 — search the real party size.

## 8. Deal scoring & verdict

### 8.1 Score (1–10), computed
Start from price vs baseline (route's typical range for the season):
- ≥25% below typical low → 9–10 (error-fare territory — §5.3 behavior)
- 10–25% below typical → 7–8
- Within typical range → 5–6
- 10–25% above typical → 3–4
- >25% above / peak pricing → 1–2

Adjust: −1 for an overnight layover disguised as "1 stop", airport change mid-itinerary, or a naked self-transfer on a family trip; −1 if the cheapest fare is Basic *and* departure is >60 days out (optionality cost, §6); +1 if the fare is changeable at no fee and priced at/below typical (the drop-harvest option has value). Show the arithmetic in one line: `Score 7 = 14% below typical (−0 flags)`.

### 8.2 Calibration
Scores are checked against `DEAL-LOG.md` outcomes quarterly: did 7+ fares actually get booked or drop further? Adjust the bands, not individual memories.

### 8.3 Verdict — one of three, with reasoning
- **BOOK NOW** — score ≥7 with firm dates, or any score inside 21 days of departure on an immovable trip, or an error fare. State the expected swing if he waits, and invoke the 24-hour rule.
- **WAIT** — score ≤6 and outside the 21-day spike, with a named book-trigger price and the watch cadence that will catch it (§5.1). "Wait" without a trigger and a watch is not a verdict.
- **PIVOT** — change dates, airports, or destination shape. Give the specific pivot and what it saves, in dollars.

## 9. After booking (the deal isn't over)

1. **Price-drop harvest** (changeable fares): re-price the booked itinerary on the watch cadence. On a drop: change/rebook the same flights and bank the difference (credit on most majors; Southwest returns points on points bookings). Inside 24 hours of the original booking the difference is cash — and **book the new ticket before cancelling the old one**.
2. **Schedule-change rights:** if the airline cancels or significantly changes the trip (≥3h domestic / ≥6h international), the traveler is owed a **cash refund to original payment** if they decline rebooking (DOT, 14 CFR Part 260) — surface this the moment a change notice arrives; never let a credit be the default.
3. **Ancillary refunds:** fees for services not received (bags/seats on a cancelled flight) are refundable — claim them.
4. A booking is only reported as booked when the confirmation is verified in the system of record (airline/booking reference read back), never from a checkout screen alone.

## 10. Output format

One message, this shape:
1. **The shortlist** — 3–5 complete trips (round trips as one total). Each: airline + flight numbers, local times, stops/layovers, duration, fare brand, bags included, **true total** for all travelers. Points options shown beside cash when §7 ran.
2. **Recommendation** — one pick, why it fits *this* party (kids' ages, arrival time, bags, seating guarantee), and the tradeoff of the runner-up in one clause.
3. **Deal score + red flags** for the recommended option, with the score arithmetic shown.
4. **Verdict** — BOOK NOW / WAIT / PIVOT, the book-trigger or expected swing, and the timing zone the search sits in (§3).
5. **Coverage note** — what was actually searched (airports, dates, sources, points checked or not) and anything that failed or wasn't covered. Prices are live snapshots with a timestamp, never guarantees.

## 11. Companions (run when he asks for the full trip, not just flights)

- **Neighborhood & Location Matcher** — 3 best areas for the trip style and nightly budget: safety, transit, walkable amenities, pros/cons.
- **Accommodation ROI Breakdown** — hotels vs. Airbnb vs. serviced apartments on total out-of-pocket: cleaning fees, taxes, kitchen savings. Price hotel points (profile) beside cash with a cents-per-point, same discipline as §7.
- **Total Expense Optimization** — audit the full itinerary for 3 concrete cuts of ≥20% that don't sacrifice safety or comfort.
- **All-In Travel Snapshot** — one page: best flight, hotel pick, day-by-day plan, transport tips, emergency numbers, currency advice, must-know local rules.

## 12. Hard rules

- Never invent a price, a schedule, or a fare rule — every number comes from a live search in this run.
- A listing is not availability; a search snippet is not a price. Verify on the actual inventory before presenting.
- Distinguish starting prices from totals, and one-way prices from round-trip totals, every time.
- If a search source fails or is blocked, say what remains unverified instead of filling the gap.
- Booking happens only on the traveler's explicit go, with passport-exact names/DOBs, and the confirmation gets verified in the system of record before it's reported as booked.
- New techniques enter this playbook only through `RESEARCH.md` grading. A viral reel is a lead, never a source.
