# 10 — Scheduled Jobs (create ONLY after the day-one manual test cycle)

| Job id | Schedule (market time, e.g. America/New_York) | Purpose |
|---|---|---|
| market-desk-premarket-brief | Mon–Fri 08:30 | Pre-market brief (doc 03) |
| market-desk-intraday-watch-1030 | Mon–Fri 10:30 | Trigger watch |
| market-desk-intraday-watch-1330 | Mon–Fri 13:30 | Trigger watch (central-bank pre-decision) |
| market-desk-intraday-watch-1530 | Mon–Fri 15:30 | Trigger watch (central-bank reaction) |
| market-desk-close-wrap | Mon–Fri 16:15 | Close wrap + Friday refinement/idea section |
| market-desk-monthly-playbook-review | Monthly, day 1, 17:00 | Regime refresh + scorecard + proposals |

Full saved bodies: `jobs/<job-id>.md` (frontmatter + body). On a fresh
account: substitute {{UNIT_CHAT_ID}} with the new unit chat ID everywhere
(including frontmatter delivery), set your own timezone, create via your
platform's scheduling tools, then read each back and compare against the
kit copy before enabling. All six are read-only for orders by design
(doc 06).
