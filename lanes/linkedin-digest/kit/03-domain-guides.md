# 03 — Domain Guides (LinkedIn Pipeline)

Three formats run on one weekly rhythm. All formats share the hard rules
in doc 08; this doc is the per-format field guide.

## A. AI Dev Digest (daily)

- **What:** 5 technical stories for builders as an 8-slide carousel.
  Slots: (1) PRODUCT [default lead], (2) FRAMEWORKS, (3) REPO (repo of
  the day — mandatory), (4) RESEARCH, (5) ECOSYSTEM.
- **Structure (locked "Front Page" system):** cover = masthead + lead
  headline (≤8 words) + "ALSO IN TODAY'S DIGEST" contents of the other
  four + date/edition line + swipe cue → slides 2–6 one story each
  (uniform title size, 3 bullets: what / why it matters / key detail) →
  slide 7 RECAP "Today in one screen" (5 headlines + verdicts + one
  quotable take — never skip) → slide 8 person-led CTA (avatar,
  "[YOUR NAME]", exactly one CTA). Author lockup + "0X / 08" page
  numbers on every slide.
- **Skin:** POSTER is the standing default (the owner's standing pick
  in the original lane — pick yours the same way: samples, one default,
  alternates only on request). `frontpage` is the alternate light skin
  for a deliberate variety edition. Dark skins (terminal, neon-grid,
  aurora) are special-occasion only. `statdeck` is REJECTED — never use.
  `signal` is retired. Full record: `hidden_files/digest-samples/
  SELECTED.txt` (snapshot in `playbooks/` era files; recreate on setup).
- **Research:** technical signal for builders, NOT the AI-news virality
  sweep. GitHub Trending (daily), Hacker News, signed-in Medium, Product
  Hunt AI/dev-tools, Hugging Face trending, arXiv cs.AI/cs.CL/cs.LG,
  framework release feeds, + the voices layer
  (`playbooks/ai-linkedin-voices.md`). Every story real, primary-source
  linked. Thin day (<4 solid) → present honestly, no padding.
- **Publish model (2026-10-21, current):** build job fires 07:00 ET →
  draft presented → on his approval, publish LIVE immediately from the
  warm LinkedIn Fresh session → first comment ~10 min later in the SAME
  session. Unapproved by ~7:45 → fallback: native-schedule for 8:00 AM +
  his manual first-comment paste (paste-ready text delivered in chat).
  The old 11:00 AM target, 10:45 fallback, and evening 6 PM slot are
  retired.
- **Numbering:** edition N read from `hidden_files/digest-edition.txt`;
  kicker `AI DEV DIGEST #<N> · <MON D>`; write N+1 back after a
  successful build.

## B. Concept posts (Tue/Thu/Sat 07:40 ET)

- One AI concept in plain English, first-person builder voice, 150–250
  words, hook first line, one genuine closing question, 3–5 Title Case
  hashtags, NO links in the body (sources + channel block go in the
  first comment).
- Formats: carousel (spec JSON → `scripts/linkedin_carousel.py`), single
  sketchnote infographic, text, or native poll (question + 4 options ≤30
  chars each).
- Flow: week plan picks the topic → prior-evening finalize job does
  FRESH research (every claim verified against a source), writes copy,
  builds + visually QAs the asset, delivers the package
  (`hidden_files/daily-packages/<date>/package.json`) → owner replies
  **schedule** (load into LinkedIn's native scheduler for Tue/Thu/Sat
  07:40) / **edit:** / **skip**.
- Topic taste (owner-steered 2026-10-19): hot/current topics, simple
  presentation, learning-focused, intriguing — topics he picks outrank
  the backlog. The workslop explainer was dropped by him after the final
  draft — do not revive dropped topics; the backlog records them.

## C. AI Week Digest (Sundays ~18:00 ET)

- Weekly best-of: one story per slot from the week's AI Dev Digests,
  Poster skin, native-scheduled for 6 PM Sunday; first comment via the
  Sunday 09:40 job pattern / same-session where possible. Volumes are
  numbered Vol. 1, 2, 3… from your first Sunday edition.

## The weekly rhythm (all times ET)

| When | What |
|---|---|
| Sun 18:39 | Weekly calendar job builds next week's plan |
| Sun ~18:00 | AI Week Digest publishes (native-scheduled) |
| Daily 07:00 | Digest build job → draft for approval → live ~08:00 |
| Mon/Wed/Fri/Sat 19:39 | Finalize job builds the next morning concept post |
| Tue/Thu/Sat 07:40 | Concept post publishes (native scheduler) |
| Tue/Thu/Sat 07:50 + Sun 09:40 | First-comment jobs |
| Daily 19:39 | Topic-options job (see doc 10 — largely superseded by finalize) |
| Daily 20:39 | Engagement monitor (metrics + draft replies for approval) |

## Scheduling mechanics (proven patterns)

- Native scheduler via browser task: spawn with a minimal placeholder,
  then STEER with the files (the spawn `files` param fails — steer-with-
  files is the proven pattern). Attach the carousel PDF as a document.
- Record every scheduled post in `hidden_files/linkedin-queue.json`.
- If LinkedIn walls the session (verification/passkey): close the task,
  start fresh ONCE; if still walled, hand the owner the copy to schedule
  manually. Never hammer retries — human pacing, always.
