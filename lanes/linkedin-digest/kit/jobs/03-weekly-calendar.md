---
id: linkedin-weekly-calendar
title: LinkedIn weekly calendar build (Sundays)
enabled: true
owner: goal:linkedin-digest
mode: task
schedule:
  kind: weekly
  timezone: '@user.current'
  time: 18:39:00
  dow: [Sun]
timeout_secs: 3600
delivery: []
metadata:
  tags: [cron:flexible-time]
  originating_chat_context_json: '{"chat_id":"{{MAIN_CHAT_ID}}","origin_provider":"main","chat_kind":"direct","event_kind":"message","require_mention":false,"device_id":"{{DEVICE_ID}}"}'
  presentation_locale: en-US
---
## LinkedIn weekly calendar build — for [YOUR NAME]

Every Sunday evening, build NEXT week's complete LinkedIn content calendar (Mon–Sun). This is the batch-planning session: one focused run produces the whole week, mapped to his weekly arc. His per-post approval still gates everything — the daily finalize + his pick turn each plan entry into a published post.

### Read first
- `~/workspace/linkedin-digest/files/linkedin-6week-content-pipeline-brief.md` (weekly arc, hard rules)
- `~/workspace/linkedin-digest/files/linkedin-idea-backlog.md` (statuses, backlog)
- `~/workspace/linkedin-digest/hidden_files/engagement-log.jsonl` if it exists (last 2 weeks: double down on what performed, drop what didn't)

### Weekly arc (fixed)
- Mon = POLL DAY (weekend-project poll: 4 concrete options + 2 backups; poll runs 2 days, winner announced Wed)
- Tue/Wed = build-in-public updates on the poll winner (real progress only — never invent)
- Thu = Learn AI resource
- Fri = "Ship It with Claude Code" use case (tie to the weekend build technique when possible)
- Sat = week-in-AI recap
- Sun = AI Week Digest (weekly roundup carousel, Poster skin, 'AI Week Digest · Vol. N' masthead): best story per slot curated from that week's Mon–Sat AI Dev Digest editions, each slide tagged back to its Digest number, first comment links the week's daily Digest posts; no excluded-project content anywhere in LinkedIn

### Publish slots
Mon–Sat 8:30 AM ET · Sun 9:00 AM ET (AI Week Digest). One post per day (never two within 24h).

### Research (fresh every run)
- This week's AI news: model releases, Claude Code changelog, agent frameworks, AI policy, major evals/pricing changes. Prefer stories <7 days old.
- What's trending on Hacker News / Reddit / LinkedIn AI conversations.
- For Monday's poll: scan for REAL pain points people complain about (Reddit threads, HN comments). Each option must be a specific pain, shippable in <8 weekend hours by one person with AI coding tools, demoable, artifact-producing. Vary the audience across weeks (non-coders, coders, grads, senior leaders).
- Verify every factual claim (version numbers, dates, metrics) against at least one source. Never invent.

### Formats
Rotate formats (the algorithm rewards diversity): carousels (document/PDF) for the how-to days and data-heavy posts — carousels are the highest-reach format, default to carousel for Tue/Fri unless the topic truly fits text; native text for updates/recaps; poll for Monday.

### Build-lane honesty
Tue/Wed posts depend on REAL build progress (weekly project lanes). Check lane workspace files under `~/workspace/` where available. If progress is unknown, frame the plan entry around the committed theme with a "[confirm build status before finalizing]" flag — never invent shipped features. The daily finalize run resolves these.

### Output
1. Write the week plan to `~/workspace/linkedin-digest/files/linkedin-week-plan-YYYY-MM-DD.md` (use Monday's date): per day — date, slot, pillar, topic, one-line hook, format, first-comment needs (links/handles), status=planned.
2. Update `linkedin-idea-backlog.md`: move planned items to planned, add new ideas to backlog.
3. Chat message (skimmable): the 7 days with topic + hook + format each, one line per day, plus a 2-line note on what the engagement data changed vs last week.

### Hard rules (no exceptions)
- NEVER mention your off-limits topics (defined at setup) anywhere LinkedIn-facing.
- No external links in post bodies — links go in the first comment ~30 min after publishing.
- His pick = per-post approval. This plan is a draft until the daily finalize + his pick.
- Keep employer boundaries: side projects on personal time/equipment; never reuse employer code/data/confidential work.
- Don't reveal cohort course content directly — generate curiosity instead.
- Voice: first-person builder, concrete, numbers-first, zero fluff.
