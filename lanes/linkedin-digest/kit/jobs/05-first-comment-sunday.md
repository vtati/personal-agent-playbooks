---
id: linkedin-first-comment-sunday
title: LinkedIn first comment (Sunday mornings)
enabled: true
owner: goal:linkedin-digest
mode: task
schedule:
  kind: weekly
  timezone: '@user.current'
  time: 09:40:00
  dow: [Sun]
timeout_secs: 1800
delivery:
  - chat_id: {{UNIT_CHAT_ID}}
metadata:
  originating_chat_context_json: '{"chat_id":"{{UNIT_CHAT_ID}}","origin_provider":"main","chat_kind":"direct","event_kind":"message","require_mention":false,"device_id":"{{DEVICE_ID}}"}'
  presentation_locale: en-US
---
## LinkedIn first comment (Sunday) — for [YOUR NAME]

About 40 minutes after the Sunday ship post goes live (9:00 AM slot), add the first comment (handles + links) to that post. Runs Sundays at 9:40 AM ET.

### Do
1. Read `~/workspace/linkedin-digest/hidden_files/linkedin-queue.json`. Find entries with status="scheduled", today's date, and slot="09:00". If the file is missing or no entry matches: end quietly with no chat message.
2. If found: use a browser task to open the owner's LinkedIn profile → recent activity → find today's post → confirm it is live → post the first comment using the EXACT text from the queue entry's first_comment field. Do not edit, rephrase, or add to it.
3. Update the queue entry: status="commented", post_url=<the live post URL>.
4. Report in chat: "First comment posted on this morning's LinkedIn ship post: <post_url>".

### Browser rules
- Spawn the browser task with a minimal placeholder task first, then steer it WITH the text it needs (the `files` param on spawn fails — steer-with-text is the working pattern).
- the owner authorized LinkedIn publishing via the browser (2026-10-04). If LinkedIn shows a login or verification wall ("Verify it's you", passkey prompt): close the task completely and start a fresh one (fresh sessions have cleared this before). If the fresh session is still walled: STOP, do not attempt any bypass, and report in chat: "LinkedIn asked for verification — please post this first comment manually:" followed by the exact comment text.
- Never like, share, reply to, or otherwise interact with anything beyond posting the one comment.
