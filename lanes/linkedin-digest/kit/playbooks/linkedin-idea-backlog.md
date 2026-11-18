# LinkedIn Idea Backlog — TEMPLATE
*Living doc for the LinkedIn content-pipeline unit. Statuses: backlog → planned → drafted → approved → posted. Dropped topics stay recorded as dropped — never revive them.*
*This is the scrubbed template edition: the original was one owner's live backlog across a 6-week sprint. Its standing rules, structure, digest design notes, and generic starter ideas are kept; the dated week-by-week history is replaced by a blank week table for you to fill.*

## Standing rules (from the brief)
- NEVER mention your off-limits topics (defined at setup) anywhere LinkedIn-facing.
- Your pick = per-post approval. Never publish or schedule without your explicit pick for that post.
- No external links in post bodies. Handles are text; full URLs go in the first comment ~30 min after publishing.
- Keep employer boundaries: side projects on personal time/equipment; never reuse employer code/data/confidential work.
- Don't reveal course/cohort content directly — generate curiosity instead.
- Post at [YOUR MORNING SLOT] on concept-post days; the Sunday digest goes out Sunday evening. Polls (if you run them): early week, close before the weekend build.

## Current week — [WEEK OF YYYY-MM-DD] (plan: files/linkedin-week-plan-<monday>.md)

| Day | Date | Slot | Status | Post |
|---|---|---|---|---|
| Mon |  |  |  |  |
| Tue |  |  |  |  |
| Wed |  |  |  |  |
| Thu |  |  |  |  |
| Fri |  |  |  |  |
| Sat |  |  |  |  |
| Sun |  |  |  | AI Week Digest · Vol. [N] — best story per slot from this week's daily digests |

**Engagement note:** check `hidden_files/engagement-log.jsonl` before planning — if no measured data exists yet, say so in the plan and make no engagement-driven pivots. Changes come from locked decisions + fresh research, not vibes.

## Backlog (unassigned) — starter ideas carried over from the original lane
- "It Acted. You Own It." — agent accountability / containment explainer (emergency brake, tamper-proof logs, never let a model grade its own work). Anchor it to fresh eval/incident news at build time.
- "Stop picking a model. Start picking per task." — the model-picker finding (a per-task picker can beat the single best model at lower cost) as a concepts-made-simple post for leaders. Verify the current numbers at build time.
- "The 3 ways to teach an AI your business" (prompt context vs RAG vs fine-tuning) — concepts-made-simple for non-coders; curiosity, never course content.
- Weekend-project poll candidates — each must be a real pain, shippable in <8 weekend hours by one person with AI coding tools, demoable, artifact-producing:
  1. Action-item amnesia fixer — transcript → owner-assigned, due-dated action tracker with weekly follow-up.
  2. Silent-capture watchdog — a meeting notetaker that alerts the moment capture dies mid-call.
  3. Never-lose-a-quote recorder — transcript where every line links back to its audio.
  4. Inbox second pair of eyes — morning brief of buried invites, wrong-inbox mail, moved sessions.
  5. *(backup)* Relative-date resolver — "next Thursday" said on a Wednesday; non-calendar fiscal "end of quarter".
  6. *(backup)* Hallucination guardrail — action items verified against the source transcript before they ship.
- A "how I built it" carousel for your own automation pipeline, using the reusable structure: cover → problem → machine → autonomous steps → human-in-the-loop → guardrails → improvement loop → proof → steal-this → CTA.
- Concepts-made-simple series anchors: one plain-English AI concept per post, mapped to techniques from your own recent builds.
- Role-curated explainers: the same concept reframed for non-coders vs coders (audience rotation per the brief).
- [ADD YOUR OWN: one line per idea, with the date added. Move items to the week table when planned; mark dropped items DROPPED with the date and never revive them.]

## Input feeds
- `linkedin-weekly-calendar` job (Sun evening): full week plan → `files/linkedin-week-plan-<Monday-date>.md`.
- `linkedin-daily-finalize` job (evenings): fresh research + full copy + carousel PDF for tomorrow's post → your "schedule" reply = approval → loaded into LinkedIn's native scheduler.
- `linkedin-first-comment` / `-sunday` jobs: first comment shortly after publish.
- `linkedin-engagement-monitor` job (evenings): metrics + drafted replies (replies never posted without your explicit approval of the exact text).
- Build milestones from your own project work (Tue/Wed updates depend on real build status — never invent progress).
- Your picks and overrides (your pick overrides any poll or plan).

## AI Dev Digest — design notes (the method behind doc 03A)
- Concept: a daily carousel for a technical AI audience. Cover (dated) + 5 stories + recap + CTA, 8 slides.
- Fixed slots: (1) Product launches [PRODUCT], (2) Frameworks & tools [FRAMEWORKS], (3) Repo of the day [REPO — mandatory], (4) Research [RESEARCH], (5) Ecosystem [ECOSYSTEM].
- Pipeline: the daily build job sweeps the sources below, builds carousel + copy + first comment (5 primary-source links), stages the draft package, and presents it for your review. NEVER auto-schedules — you approve per post, then it publishes live (current model, doc 03A) or is native-scheduled.
- Research design: digest research is SEPARATE from any virality sweep you may run elsewhere. A virality sweep optimizes for reach; the digest optimizes for technical signal for builders. The same story can lead one and have no place in the other.
  - Primary sources: GitHub Trending (repo of the day, mandatory), Hacker News front page, signed-in Medium ("For you" feed + the artificial-intelligence tag), Product Hunt AI/dev-tools, Hugging Face trending, arXiv cs.AI/cs.CL/cs.LG, framework release feeds (e.g. LangChain, LlamaIndex, Vercel AI SDK, PyTorch via GitHub releases), tech-press momentum + dev social signals as a proxy for "hot in tech circles" (LinkedIn has no automatable trending feed — be honest about this).
  - A general AI-news research feed is a SECONDARY input only (big technical stories that happen to be viral), re-ranked through the technical lens.
  - Prefer primary sources (official release notes, repos, papers) over press rewrites. Every story real and verifiable; thin day (<4 solid stories) → present honestly, no padding.
- Edition numbering: `hidden_files/digest-edition.txt` counter; kicker "AI DEV DIGEST #<N> · <MON D>"; write N+1 back after a successful build.
- Copy formula (SCAN format — full spec in `jobs/01`): bold opener with edition + date, a "Today in 10 seconds" one-liner of all 5 stories, per-story blocks with only load-bearing keywords bolded, a genuine closing question, the follow line, 3–4 Title Case hashtags. Reading ONLY the bold text must convey the whole day.
- Skin: pick your digest skin deliberately (samples → your pick → record it in `hidden_files/digest-samples/SELECTED.txt`; the build job reads it). In the original lane the standing default became the light POSTER skin; a dark skin reads well for evening editions but a light skin won on clarity. Whatever you pick: one default, alternates only on request, and never resurrect a skin you rejected.
- Timing lesson from the original lane: the digest's slot moved (evening → morning) as the lane learned that freshness is the product and the publish+comment must happen in ONE warm browser session. Expect to move yours once; log the decision here when you do.
