# Flight Finder — Research & Evidence Base

**Compiled:** 2026-11-16. **Purpose:** every rule in `PLAYBOOK.md` v2 traces to a source here. Claims are graded: **A** = data-backed (adopt), **B** = plausible/conditional (use, label), **C** = myth (banned from the engine).

## 1. When to book (Grade A)

- Google's analysis of five years of Google Flights data (holiday travel trends, Oct 5, 2026): domestic fares bottom out ≈**39 days** before departure, low range **22–57 days**; international ≈**89 days**, low range **50–133 days**.
- CheapAir's annual study (hundreds of millions of fares): prime domestic window **21–74 days**, best single day ≈42 — consistent zone, different point estimate.
- Expedia's 2026 Air Hacks (its own booking data, Dec 2024–Nov 2025) runs closer-in: domestic sweet spot **15–30 days** (averaged $130 less than booking 6+ months out); international cheapest at 8–15 days in its data but 31–45 days still saved ~$190 — treat Expedia's late window as high-variance, not a plan.
- **Consensus the engine uses:** book inside the zone, not on a magic day; fares bought 6+ months out often carry an early premium; prices spike inside **21 days** (many lowest fare buckets require 21-day advance purchase) and hard inside **7–13 days** (CheapAir: ~26% above the cheapest window).
- Sources: factaxy.com summary of Google/CheapAir data; thepointsking.com 2026 airfare analysis (cites Google Oct 2026 report directly); Expedia 2026 Air Hacks via travel.galantmedia.com.ng; matthandzel.com Cheap Flights System (aggregates Expedia 2025/2026, Google, Going, CheapAir, Dollar Flight Club, NerdWallet).

## 2. Which day (Grade A)

- Day you **fly** moves price: leaving Monday and returning Tue/Wed saves ~14% vs weekend patterns, up to ~20% vs Sunday-out/Sunday-back (Google). Expedia 2026: Tuesday departure ~14% below Sunday; international Thursday ~17% below Sunday.
- Day you **book** is noise: Google puts the best booking day ~1.3–1.4% below the worst; Expedia ~3%. Studies disagree on *which* day because there is effectively no effect. **"Book on Tuesday" is Grade C as a tactic.**

## 3. Search mechanics that work (Grade A)

- **Date grid / price graph** (Google Flights): 49 departure×return combos at ±3 days; a one-day shift can cut a fare by a third on some routes. Price insights label a fare low / typical / high vs the route's history — the engine's baseline for deal scoring.
- **Track Prices**: alerts on exact dates or "any dates" for a route; watching beats repeated manual searching.
- **Cheapest tab**: surfaces lower fares that may involve longer layovers, a different airport in the same city, separate tickets, or third-party sellers — read the fine print before presenting (Google, Oct 2024 feature notes).
- **Nonstop premium**: ~+20% on average vs connecting (Google 2026 data) — the anchor for the $/hour nonstop test.
- **Three-source rule** (2026 consensus across guides): metasearch for the landscape (Google Flights), a second aggregator that indexes smaller OTAs (Momondo/Skyscanner/Kayak — Kayak also labels split-carrier "hacker fares"), then the airline's own site to verify and book. Book direct where prices tie: easier changes, refunds, and the 24-hour rule is cleanest.
- **Explore / Everywhere search** (Google Explore map, Skyscanner Everywhere): the right tool when the destination, not the route, is flexible.

## 4. Family seating — the rule that changed our math (Grade A)

- The proposed DOT rule (Aug 2024 NPRM: seat children ≤13 next to an accompanying adult free, within 48h of booking) **stalled in Jan 2025 and is not final**. What exists is the DOT **Family Seating Dashboard** of voluntary guarantees.
- As of Sep 2026, five large US carriers **guarantee** fee-free adjacent seating for a child 13 or under on every fare type: **Alaska, American, Frontier, Hawaiian, JetBlue**. Four do **not**: **Allegiant, Delta, Southwest, United**.
- Conditions: child and adult on the **same reservation**; adjacent seats confirmed no later than the day before the flight.
- Engine consequence: seat-selection fees are a real true-total cost only on non-guarantee carriers (or when the party wants specific seats beyond adjacency). On guarantee carriers, price $0 and say why. United — our most-used carrier — is a non-guarantor, so seat pricing stays in its totals.
- Note: Southwest's move to assigned seating (early 2026) ended the old open-seating family pre-board strategy.
- Sources: DOT Family Seating Dashboard summaries (Sep 2026), travel.tudiencau.com seat-fee comparison, FAA Reauthorization Act 2024 (PL 118-63) analyses.

## 5. Refunds & rights (Grade A)

- **24-hour rule** (14 CFR 259.5): booking made 7+ days before departure can be cancelled for a full refund to original payment within 24 hours (airline may instead offer a free 24h hold). Cleanest when booked direct with the airline.
- **DOT refund rule** (14 CFR Part 260, effective Oct 28, 2024): airline cancellation or significant change — **3h domestic / 6h international** thresholds — entitles the traveler to an **automatic cash refund** if they decline rebooking; fees for ancillary services not received are refundable too. Credits are the traveler's choice, never the forced default.
- Sources: DOT rule summaries via Going, tripmemos, travelstacks FAA Act analysis.

## 6. After-booking price drops (Grade A)

- US majors have eliminated change fees on **standard economy and above** (US-originating). If the fare drops: change/rebook the same itinerary and bank the difference — as **travel credit** on United/Delta/American/JetBlue (typically 1 year), **original payment or credit** on Alaska reprice, **unlimited rebooks** on Southwest with points bookings refunded in points.
- **Basic Economy breaks the strategy**: mostly unchangeable after 24h (American: AAdvantage members may cancel for credit minus a $99 fee). This is a quantifiable cost of Basic on far-out bookings.
- Within the first 24 hours, a drop is cash: **book the new ticket before cancelling the old one** so the seat is never unheld.
- Two one-way tickets (when priced equal to the round trip) let each direction be repriced independently.
- Services exist that monitor this (Going's Price Drop feature, Jetback-style confirmation forwarding) — the engine replicates the check itself on a schedule instead of depending on them.
- Sources: going.com fare-drop guide; withautopilot.com rebooking guide (carrier tables, Sep 2026); ottotheagent.com price-tracking guide.

## 7. Points & awards (Grade A/B)

- **Value formula:** cents-per-point = (cash fare − award taxes & fees) ÷ points × 100. Always compute; never eyeball.
- United MileagePlus is **dynamic** (no chart since 2019): median realized value measured ≈0.66¢ across a 10-trip sample (Sep 2026, seats.aero cached data via gregoiremaillard.com comparator) — but **saver** space, when it appears, prices far better (worked example: 55k miles vs a $967 cash fare ≈ 1.7¢/mile). United's miles+cash floor is 1.0¢/mile. Engine bar: redeem United miles at **≥1.5¢** on verified saver space; below that, cash usually wins. Cardholders/Premier members see extra saver inventory and 10–15% award discounts (Apr 2026 program changes).
- **seats.aero** searches cached + live award space across 27 programs and has a Partner API — the scalable way to add award search to the engine (Phase 3, only if balances justify it). Its default filters hide overpriced dynamic awards.
- **Iron rule:** verify the award on the airline's own site *before* transferring bank points — transfers are one-way.
- Positioning/ex-EU fares (Grade B): premium-cabin prices vary hugely by origin country; a cheap positioning flight to a cheaper origin can save four figures on long-haul business. Real, but only worth engine steps for premium cabins or very long hauls.
- Fifth-freedom routes (Grade B): foreign carriers flying between two other countries sometimes price premium cabins aggressively. Opportunistic, not systematic.

## 8. Error fares (Grade A mechanics, unpredictable supply)

- Mistake fares appear a few times a month, live **1–3 hours**, and are surfaced by alert services — **Going, Secret Flying, Jack's Flight Club, Airfarewatchdog** — not by searching. Most are honored; the safe play is book direct, don't call the airline to ask about the price, and don't book non-refundable hotels/car until the ticket is confirmed/issued.
- Sources: Secret Flying / Jack's Flight Club descriptions across guides; grabflightsnow flight-hacking survey.

## 9. Structural tricks — graded

- **Split tickets / two one-ways** (A): routinely ±20–40% vs round trip on some markets; also buys per-leg repricing flexibility. Risk: no protection across tickets — always labelled.
- **Virtual interlining** (B): Kiwi-style combinations of non-codeshare carriers can price 30–50% under standard results; with the seller's guarantee product the misconnect risk is covered, without it it's a naked self-transfer. Engine presents both states distinctly.
- **Self-transfer** (B): fine with a real buffer (≥3h, same airport, carry-on or re-check time priced in) and a stated failure cost.
- **Hidden city** (B, restricted): real savings exist (Skiplagged indexes them) but it violates carrier terms, checked bags go to the ticketed destination, skipping a segment cancels the rest of the itinerary, and frequent-flyer credit/status can be clawed back. Engine: risk-card only, never for family trips with checked bags, never where the traveler values status on that carrier.
- **Fuel dumping** (C for this engine): real historically, now fragile, ToS-risky, and not systematizable. Excluded.

## 10. Myths — Grade C, banned

From the Instagram audit (Nov 16, 2026 — 50 posts skimmed across flight-hack queries) cross-checked against the data sources above:

- **"Search incognito / clear cookies or airlines raise your price"** — no evidence; Going, Skyscanner and Google's own product leadership attribute changes to inventory/demand. Repeated in multiple high-engagement reels (e.g. @gisselle.travelhacks, 230K followers) — engagement is not evidence.
- **"Use a VPN set to a poorer country"** — point-of-sale differences exist occasionally but are inconsistent, can break payment/refund rules, and can violate site terms. Not a tactic; at most a single labelled check.
- **"Book at 2–3 AM"** — no supporting data anywhere in the booking-window studies.
- **"Book on Tuesday"** — see §2: ~1–3% noise, studies disagree on the day.
- **"Search from a library computer"** — tested by creators themselves, debunked; same dynamic-pricing explanation.
- What Instagram *did* surface that's real: deal-alert subscriptions (Going), price-drop monitoring after booking, Expedia's booking-window data, and the window+aisle pair trick for couples (irrelevant for families who must sit together, useful for 2-adult trips — noted in the playbook as a minor tactic).

## 11. What this means for "anyone using this playbook"

The transferable assets are the **protocol, the grading discipline, and the logs** — not any single trick. Tricks decay (fuel dumping died, the family-seating rule stalled, Southwest changed its seating); a system that (a) anchors prices to a route baseline, (b) watches instead of one-shot searching, (c) prices the *whole* trip including post-booking optionality, and (d) grades new claims before adopting them keeps working when individual hacks die. `ENGINE.md` specifies that system so another agent or account can run it.
