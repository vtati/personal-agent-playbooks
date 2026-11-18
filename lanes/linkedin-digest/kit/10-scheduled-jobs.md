# 10 — Scheduled Jobs (LinkedIn Pipeline)

## Catalog — 7 recurring jobs

| # | Job id | Schedule (ET) | Delivers to | Body |
|---|---|---|---|---|
| 1 | `linkedin-ai-dev-digest-daily` | Mon–Sat 07:00 (America/New_York) | Unit chat + main chat | `jobs/01-ai-dev-digest-build.md` |
| 2 | `linkedin-daily-finalize` | Mon/Wed/Fri/Sat 19:39 | Unit chat + main chat | `jobs/02-daily-finalize.md` |
| 3 | `linkedin-weekly-calendar` | Sun 18:39 | Unit chat | `jobs/03-weekly-calendar.md` |
| 4 | `linkedin-first-comment` | Tue/Thu/Sat 07:50 | Unit chat | `jobs/04-first-comment-tue-thu-sat.md` |
| 5 | `linkedin-first-comment-sunday` | Sun 09:40 | Unit chat | `jobs/05-first-comment-sunday.md` |
| 6 | `linkedin-engagement-monitor` | Daily 20:39 | Unit chat | `jobs/06-engagement-monitor.md` |
| 7 | `linkedin-daily-topic-options` | Daily 19:39 | Unit chat | `jobs/07-daily-topic-options.md` |

**Status note on #7:** the pipeline brief records the topic-options job
as superseded by the finalize flow (2026-10-06) — its file remained in
the goal's crons/ folder at sync time. On rebuild, confirm with the
owner whether to recreate it; the finalize job covers its purpose.

**Historical one-offs (not recreated):** a dozen `runonce` first-comment
jobs from Oct 8–18 (per-edition comment runs under the old session
model). They are spent; the recurring first-comment jobs + the
warm-session pattern replaced them. Their existence explains gaps in
older publish logs — nothing to rebuild.

## Recreating the jobs

1. Create each job from its `jobs/` file verbatim after replacing
   `{{UNIT_CHAT_ID}}`, `{{MAIN_CHAT_ID}}`, `{{DEVICE_ID}}` (worksheet
   doc 00). Job bodies reference workspace paths under
   `~/workspace/linkedin-digest/`
   — recreate that tree first (doc 11).
2. Keep frontmatter semantics: mode `task`, goal-owned, delivery as
   tabled (the digest and finalize jobs report to BOTH chats per the
   standing side-chat reporting rule).
3. Seed state files before enabling: `digest-edition.txt` seeded at 1
   on a fresh setup, empty `linkedin-queue.json`,
   `engagement-log.jsonl`, `daily-packages/` folder.
4. Do NOT enable any job until `11-day-one-checklist.md` passes,
   including one manual digest build + one manual finalize package,
   both left unpublished for the owner's review.
