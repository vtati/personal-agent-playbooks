---
id: linkedin-daily-finalize
title: LinkedIn post finalize (Mon/Wed/Fri/Sat evenings)
enabled: true
owner: goal:linkedin-digest
mode: task
schedule:
  kind: weekly
  timezone: '@user.current'
  time: 19:39:00
  dow: [Mon, Wed, Fri, Sat]
timeout_secs: 3600
delivery:
  - chat_id: {{UNIT_CHAT_ID}}
  - chat_id: {{MAIN_CHAT_ID}}
metadata:
  tags: [cron:flexible-time]
  originating_chat_context_json: '{"chat_id":"{{UNIT_CHAT_ID}}","origin_provider":"main","chat_kind":"direct","event_kind":"message","require_mention":false,"device_id":"{{DEVICE_ID}}"}'
  presentation_locale: en-US
---
## LinkedIn post finalize — for [YOUR NAME]

On Mon/Wed/Fri/Sat evenings, finalize the NEXT post from the weekly plan. Fresh research, full copy, carousel built — delivered ready for his pick. His reply "schedule" in chat = approval to load it into LinkedIn's native scheduler.

Morning posts run 3x/week (Tue/Thu/Sat ~7:40 AM) + Sunday 9:00 AM ship post. So: Monday evening → Tuesday's post, Wednesday evening → Thursday's post, Friday evening → Saturday's post, Saturday evening → Sunday's 9:00 AM ship post.

CADENCE (2026-11-15, the owner): the daily AI Dev Digest runs Mon–Sat only; SUNDAY IS WEEKLY-ONLY. The Saturday-evening run builds the Sunday AI Week Digest, and its curation window extends through SUNDAY MORNING — if a major story breaks Sunday morning, it may displace a weaker slot winner (note the swap in the research note). Sunday's published daily editions list in the weekly's first comment covers Mon–Sat editions only.

### Read first
- This week's plan: the latest `~/workspace/linkedin-digest/files/linkedin-week-plan-*.md` → take the next post entry. If no week-plan file exists yet, fall back to the current week table in `files/linkedin-idea-backlog.md`.
- The pipeline brief + playbook in the same `files/` folder for voice and hard rules.
- Check the idea backlog statuses and recent chat history for what actually published — never assume a planned post went live.

### Do
1. **Fresh research** on the planned topic: today's AI news, verify every factual claim (versions, dates, metrics) against at least one source. If the plan entry has a "[confirm build status]" flag, resolve it from lane workspace files or frame honestly around what's real. Never invent progress or numbers.
2. **Write the full post copy**: 150–250 words, first-person builder, concrete, numbers-first, zero fluff. Open with the hook (first line must earn the "...see more" click). One genuine question at the end — never engagement bait. 3–5 hashtags max. NO external links in post body, handles as plain text only.
   - DIGEST EXCEPTION (SCAN FORMAT, adopted 2026-11-15 per the owner — replaces the 2026-11-11 block format): when the next post is the Sunday AI Week Digest, format for the scanner with Unicode bold characters (LinkedIn has no native bold and its app collapses blank lines into a wall of text): bold opener "𝗔𝗜 𝗪𝗲𝗲𝗸 𝗗𝗶𝗴𝗲𝘀𝘁 · 𝗩𝗼𝗹. <N> — <theme line>", a bold "𝗧𝗵𝗶𝘀 𝘄𝗲𝗲𝗸 𝗶𝗻 𝟭𝟬 𝘀𝗲𝗰𝗼𝗻𝗱𝘀:" line with the 5 micro-headlines separated by " · ", then one block per story: bold category chip "<n> · <SLOT IN CAPS>", bold headline, one plain sub-line (with the source edition noted), up to 3 "→" detail lines with ONLY the load-bearing keywords/metrics bolded; "· · ·" separator lines between stories; the week's thread as its own line; bold question line; follow CTA; hashtags plain. Reading ONLY the bold text must convey the whole week. Never a wall of paragraph text.
3. **Build the asset**:
   - format=carousel → write a spec JSON and run `python3 ~/workspace/linkedin-digest/tools/linkedin_carousel.py spec.json ~/workspace/linkedin-digest/hidden_files/daily-packages/YYYY-MM-DD/carousel.pdf`. Verify the PDF exists and has the expected page count. Spec: kicker (pillar tag), title (the hook), 3–5 content slides (heading + up to 5 short bullets each), cta (2 lines), handle "[YOUR NAME]".
   - format=poll → write the poll question + 4 options (each 30 characters or fewer) + the post copy framing it.
   - format=text → copy only.
4. **Write the first-comment text**: handles as text + full URLs (YouTube @[YOUR YOUTUBE HANDLE] "builds & deep-dives", @[YOUR NEWS CHANNEL] "daily AI news"; IG @[YOUR INSTAGRAM], @[your-news-channel]; portfolio [YOUR PORTFOLIO URL]) — include only what's relevant to the post.
5. **Save the package** to `~/workspace/linkedin-digest/hidden_files/daily-packages/YYYY-MM-DD/package.json`: {publish_date, slot ("07:40" Tue/Thu/Sat / "09:00" Sun), format, copy, carousel_pdf path or null, poll or null, first_comment}.
6. **Deliver to chat**: the full post copy, the carousel PDF attached as a preview (or poll question + options), the first-comment text, and end with exactly: "Reply **schedule** and I'll load this into LinkedIn's native scheduler for [Weekday, Date at slot ET]. Reply **edit:** followed by changes, or **skip** to drop this post."

### Hard rules (no exceptions)
- NEVER mention your off-limits topics (defined at setup). No external links in post body. Employer boundaries apply. No cohort content reveals. Never invent facts, metrics, or build progress.
- Nothing is published or scheduled until he replies "schedule" (or equivalent explicit approval) in the chat.
