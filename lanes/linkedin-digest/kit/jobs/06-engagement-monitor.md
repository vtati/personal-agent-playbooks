---
id: linkedin-engagement-monitor
title: LinkedIn engagement monitor (evenings)
enabled: true
owner: goal:linkedin-digest
mode: task
schedule:
  kind: daily
  timezone: '@user.current'
  time: 20:39:00
timeout_secs: 3600
delivery: []
metadata:
  tags: [cron:flexible-time]
  presentation_locale: en-US
---
## LinkedIn engagement monitor — for [YOUR NAME]

Every evening, pull today's LinkedIn post performance and draft reply suggestions. Surface the digest; NEVER post replies without his explicit approval of the exact reply text.

### Do
1. Read `~/workspace/linkedin-digest/hidden_files/linkedin-queue.json`. Find entries with today's date and status="commented" (or "scheduled" with the slot already passed). If the file is missing or nothing matches: end quietly with no chat message.
2. Via a browser task (spawn with a minimal placeholder first, then steer — the `files` param on spawn fails): open each post URL, record impressions, reactions, reposts, comment count, and the text + author of substantive comments. Skip "Great post!"-level noise except as a count.
3. Append to `~/workspace/linkedin-digest/hidden_files/engagement-log.jsonl`: one JSON line per post {date, post_url, format, impressions, reactions, reposts, comments, top_commenters}.
4. Update the queue entry status to "measured".
5. Deliver the digest to chat: metrics vs the week's running average, notable comments worth replying to, and 2–4 drafted replies in his voice (first-person builder, concrete, zero fluff — never argue, never engage hate, never promise future content, never share personal info). End with: "Reply **post replies** to publish these as-is, or edit any first."

### Rules
- NEVER post a comment reply without his explicit approval of that exact reply text in chat.
- If LinkedIn shows a verification wall: close the task, start fresh once; if still walled, report the digest as "metrics unavailable tonight — verification wall" and retry tomorrow. Never attempt a bypass.
- Note: the morning reply block stays his. The playbook's daily 10-minute engagement block (reply within 60–90 minutes of publish) is the algorithm's strongest signal and can't be automated from here — this monitor covers the evening digest and drafts only.
