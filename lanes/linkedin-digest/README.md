# Lane: LinkedIn AI News Digest

A personal agent that researches AI news every day and produces a
LinkedIn digest — a daily carousel/post in a locked "Front Page" format,
plus a weekly Sunday best-of edition. It also runs the surrounding
pipeline: a weekly content calendar, evening post-finalize packages,
first comments, and an engagement monitor. **Nothing ever publishes
without your explicit per-post approval** — the agent builds drafts and
packages; you fire every shot.

This is a self-guided package: you don't set it up by hand. You hand the
kit to your AI agent, and the agent interviews you and drives the whole
setup in phases.

## What the agent does (the method)

- **Daily digest (Mon–Sat):** sweeps technical sources — GitHub Trending,
  Hacker News, signed-in Medium, Product Hunt, Hugging Face, arXiv,
  framework release feeds, plus a watchlist of AI voices — and picks a
  5-story slate in fixed slots (PRODUCT / FRAMEWORKS / REPO OF THE DAY /
  RESEARCH / ECOSYSTEM). It builds an 8-slide carousel (cover, 5 story
  slides, a one-screen recap, a closing CTA) and a post written in the
  **SCAN format** (formatted so reading only the bold text conveys the
  whole day), then presents the draft for your approval before anything
  publishes.
- **Concept posts (Tue/Thu/Sat):** one AI concept in plain English,
  finalized the evening before with fresh research, full copy, and a
  visually QA'd carousel/infographic. You reply `schedule` / `edit:` /
  `skip` — that reply is the publish gate.
- **AI Week Digest (Sunday):** the week's best story per slot, curated
  from the daily editions.
- **Supporting jobs:** a Sunday weekly-calendar build, first-comment
  jobs (sources and links live in the first comment, never the post
  body), and an evening engagement monitor that drafts replies — which
  are never posted without your approval of the exact text.

## What you need before starting

1. **A LinkedIn account** — yours, with a profile you're willing to
   overhaul (the kit includes a section-by-section overhaul playbook
   with fill-in templates for headline, About, banner, and settings).
2. **An AI agent platform** that gives your agent: chat/side-chat
   conversations, **scheduled jobs**, **web research and browsing**,
   a browser it can drive at human pace (LinkedIn has no API for
   auto-publishing to personal profiles — publishing runs through the
   browser, with your approval), a **secure vault** for your LinkedIn
   password (the agent never holds it in chat or files), and file
   storage for the carousel builders (the kit's Python/PIL scripts) and
   state files.
3. **A square headshot of yourself** for the carousel slides
   (`brand/avatar.jpg` — you add it during setup; no photo ships in
   this public kit).
4. **Optionally:** a Medium account (for the signed-in research pass)
   and LinkedIn Premium (for InMail and profile-view depth — it does
   not change the profile scores).

## How setup works

1. Copy this lane folder into your agent's workspace.
2. Paste the contents of **`kit/SETUP-KICKOFF-PROMPT.txt`** into a fresh
   chat with your agent.
3. The agent reads the kit in order (docs 00 → 11, then `jobs/`,
   `scripts/`, `playbooks/`, `brand/`) and **interviews you a few
   questions at a time** to fill the setup worksheet: your name,
   headline, LinkedIn URL, channels, off-limits topics, chat IDs, and
   cadence choices. Every personal value in the kit is a bracketed
   placeholder like `[YOUR NAME]` until you fill it.
4. Setup runs in phases and never skips: interview → account + a fresh
   dedicated browser profile (composer tested with a throwaway draft
   before anything real) → workspace install → **one manual test cycle**
   (a digest draft + a finalize package, both left unpublished) → your
   approval → only then are the 7 scheduled jobs created from `kit/jobs/`.
5. The day-one checklist (`kit/11-day-one-checklist.md`) is the go-live
   gate: every box must pass before any job is enabled.

## Cadence at a glance (defaults — adjust in the worksheet)

| When | What |
|---|---|
| Mon–Sat, morning | Digest build job → draft presented → publish live on your approval |
| Tue/Thu/Sat, morning | Concept post publishes (native scheduler); first comment follows |
| Mon/Wed/Fri/Sat, evening | Finalize job builds tomorrow's post package for your pick |
| Sunday, evening | Weekly calendar job builds next week's plan; AI Week Digest publishes |
| Daily, evening | Engagement monitor: metrics + drafted replies for your approval |

## What's in this lane

- `kit/` — the full replication kit: 12 numbered docs (worksheet,
  scope, account setup, domain guides, connectors, secrets inventory,
  operating model, runbook, brand standards, hard-won lessons, job
  catalog, day-one checklist), the kickoff prompt, 7 job bodies in
  `kit/jobs/`, the 3 carousel builder scripts in `kit/scripts/`,
  playbooks and templates in `kit/playbooks/`, and brand notes in
  `kit/brand/`.

Everything personal from the original lane — name, handles, profile
copy, post history, metrics — has been scrubbed to placeholders. The
method, cadences, formats, quality gates, and lessons are intact and
unchanged.
