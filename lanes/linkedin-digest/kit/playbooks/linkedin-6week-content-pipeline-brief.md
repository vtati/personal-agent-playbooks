# LinkedIn Content Pipeline — 6-Week Build-in-Public Sprint
*Brief for the pipeline side chat. Created 2026-10-05.*

## Mission
6-week build-in-public sprint. (The original ran alongside an AI certification course — if you're taking a course or cohort, name it here: **[YOUR COURSE / COHORT, PROVIDER, DATES]**; otherwise delete this clause.) Every week: design, build, and ship a real AI project live — full journey shared across channels. Position yourself as a top-tier **[YOUR TARGET ROLE]** candidate.

## Positioning
- Headline: **[YOUR HEADLINE]**
- Legal entity (if you use one in formal contexts): **[YOUR COMPANY LLC]** — use this name consistently, never an old company name.
- Framing: "[YOUR BRAND] is an AI lab exploring AI applications across industries — building, showcasing, and problem-solving." Lead with learning + building, not the corporate entity.
- Motto for video content: "make AI learning easy and understandable."

## Week 1 builds (Oct 5–11) — already committed publicly
1. **AI Note Taker** — AI Interviewer that transforms notes/documents into structured output.
2. **[YOUR PROJECT 2]** — a second small product with a clear user pain point (in the original sprint this slot held an estate-planning tool: a painful, expensive process made easy with AI). Pick something demoable with artifacts.

## Weekly operating rhythm
- **Monday:** poll with 4 concrete weekend-project ideas (real pains, shippable by one person in a weekend, demoable, artifact-producing). His pick overrides the poll if he wants; default = poll winner.
- **Tue/Wed:** build progress, blockers, decisions, winner updates.
- **Thursday:** AI learning resource post.
- **Friday:** "Ship It with Claude Code" — real use case, real setup + artifacts (synergy: technique used in the weekend build).
- **Saturday:** week-in-AI recap.
- **Sunday night:** ship post — demo + artifacts + lessons, or an honest post-mortem. Never silence, never vaporware.

## Daily system (fully automated, 2026-10-06 — his pick still gates every post)
- **Sunday ~6:39 PM ET** — `linkedin-weekly-calendar`: batch-builds the full week's calendar (topics, hooks, formats, carousel outlines) from fresh research + engagement data → week plan file + chat summary.
- **Daily ~7:39 PM ET** — `linkedin-daily-finalize`: fresh research on tomorrow's planned topic, full copy written, carousel PDF built → ready-to-publish package delivered in this chat (copy + carousel preview + first-comment text).
- **His approval** — he replies **schedule** (or **edit:** / **skip**). On "schedule", the pipeline agent loads the post into LinkedIn's native scheduler via a browser task: spawn with a minimal placeholder first, then steer WITH the files (the `files` param on spawn fails — steer-with-files is the proven pattern); composer → paste copy → attach the PDF as a document for carousels (native poll for Monday) → clock icon → schedule for Mon–Sat 8:30 AM ET, Sun 6:00 PM ET. Record the entry in `hidden_files/linkedin-queue.json` (status=scheduled). Confirm in chat: "Scheduled for [slot]." If LinkedIn walls the session (verification/passkey): close the task, start fresh once; if still walled, hand him the copy and ask him to schedule manually.
- **Mon–Sat 9:10 AM / Sun 6:40 PM** — first-comment crons post the links/handles comment ~40 min after publish, exact text from the queue. If walled, they hand him the exact text to post manually.
- **Daily ~8:39 PM ET** — `linkedin-engagement-monitor`: metrics + drafted reply suggestions. Replies are NEVER posted without his explicit approval of the exact reply text. The morning 10-min reply block (60–90 min after publish) stays his — strongest algorithm signal, can't be automated.
- Monday's deliverable = the weekend-project poll. Never publish or schedule without his explicit pick for that post.
- Superseded 2026-10-06: the old `linkedin-daily-topic-options` cron (3 options, delivered to the profile chat) is disabled; the finalize cron replaces it and delivers here, fixing the misroute.

## Content pillars & audiences
- Pillars: build-in-public (weekly project), AI concepts made simple, Claude Code mastery, AI news & updates.
- Audiences: non-coders, coders, every role, college graduates, experienced PMs/devs/designers, senior leaders. Role-curated videos: easy to understand whether you write code or not.
- Playlists (YouTube @[YOUR YOUTUBE HANDLE]): Claude Code Mastery, AI Concepts Made Simple, AI News & Updates, Build in Public.

## Channels (handles are text in posts; full URLs go in the first comment)
- YouTube: @[YOUR YOUTUBE HANDLE] (builds & deep-dives) — https://www.youtube.com/@[YOUR YOUTUBE HANDLE]
- YouTube: @[YOUR NEWS CHANNEL] (daily AI news) — https://www.youtube.com/@[YOUR NEWS CHANNEL]
- Instagram: @[YOUR INSTAGRAM] — https://www.instagram.com/[YOUR INSTAGRAM]
- Instagram: @[your-news-channel] — https://www.instagram.com/[your-news-channel]
- Portfolio: [YOUR PORTFOLIO URL]
- Profile: [YOUR LINKEDIN URL]

## Hard rules
- **NEVER mention your off-limits topics** (define them at setup — e.g. a past venture you never discuss publicly) anywhere LinkedIn-facing (profile, posts, comments, banner). Non-negotiable.
- No external links in post bodies (LinkedIn penalizes reach) — links go in the first comment, posted ~30 min after publishing.
- His pick = per-post approval. Never publish, schedule, or auto-post without his explicit pick/approval for that post.
- Keep employer boundaries: side projects on personal time/equipment; never reuse employer code/data/confidential work; outside-activity disclosure updated with the new company name.
- Don't reveal cohort course content directly — generate curiosity instead.

## Pipeline (live, 2026-10-06)
Stages: **idea backlog → weekly plan (Sun) → daily finalize → his approval → native-scheduler queue → first comment → engagement digest**. State lives in `hidden_files/linkedin-queue.json` (entry statuses: scheduled → commented → measured) and `hidden_files/engagement-log.jsonl`. Carousel builder: `tools/linkedin_carousel.py` (spec JSON → 1080×1350 PDF document post). All five crons are goal-owned and deliver to this chat.
