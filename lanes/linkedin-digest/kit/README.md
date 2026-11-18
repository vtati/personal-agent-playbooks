# LinkedIn Pipeline — Replication Kit

This kit rebuilds a LinkedIn lane like the original owner's: a profile
overhaul (positioning for [YOUR TARGET ROLES]) plus the two content
systems that run on it — the daily **AI Dev Digest** carousel and the
Tue/Thu/Sat **concept-post** rhythm with its Sunday **AI Week Digest** —
including the weekly calendar build, the evening finalize step, first
comments, and the engagement monitor. Seven recurring scheduled jobs,
three carousel builder scripts, and every standing rule.

**Mode: TEMPLATE.** This is the public, scrubbed edition of a private
replication kit: the full method is intact (cadences, formats, quality
gates, job bodies), but every personal value — name, handles, URLs,
profile copy, edition state — is a bracketed placeholder like
`[YOUR NAME]`. You fill them in during the setup interview; each maps to
a row in `00-setup-worksheet.md`. Credentials are named, never valued,
here or anywhere.

**The one rule that outranks everything in this kit:** nothing is ever
published, scheduled, or commented on LinkedIn without the owner's
explicit per-post approval. The jobs build drafts and packages; the human
fires every shot.

## How to use this kit

1. Paste `SETUP-KICKOFF-PROMPT.txt` into a fresh chat on the new account.
2. The agent reads the docs in order (00 → 11), interviews the owner, and
   drives setup in phases: worksheet → profile/account → browser profile
   → workspace install → ONE manual test cycle (a digest draft + a
   finalize package, both unpublished) → owner approval → scheduled jobs.
3. All LinkedIn browser work uses a fresh dedicated browser profile
   ("LinkedIn Fresh") — see doc 02 and lesson 1 in doc 09 before touching
   the composer.

## What's inside

| File | What it is |
|---|---|
| `SETUP-KICKOFF-PROMPT.txt` | Paste-in prompt that drives the whole rebuild |
| `00-setup-worksheet.md` | Every placeholder + every operational value, one table |
| `01-scope.md` | What this kit rebuilds — and what it deliberately doesn't |
| `02-account-setup.md` | LinkedIn account, vault login, the LinkedIn Fresh browser profile, Medium session |
| `03-domain-guides.md` | The three formats: AI Dev Digest, concept posts, AI Week Digest + the weekly rhythm |
| `04-connectors.md` | Browser profiles, vault, image search, research sources — how each is wired |
| `05-secrets-inventory.md` | Every secret by NAME + handling rules. No values, ever |
| `06-operating-model.md` | Charter: per-post approval, autonomy bounds, escalation, reporting |
| `07-pipeline-runbook.md` | End-to-end weekly cycle, job by job |
| `08-brand-and-standards.md` | Voice, post formulas, Front Page structure, skins, hashtags, link blocks |
| `09-hard-won-lessons.md` | Standing rules bought with real failures (Fresh profile, warm-session comments, palette…) |
| `10-scheduled-jobs.md` | Catalog of all 7 recurring jobs + recreation guide |
| `11-day-one-checklist.md` | Go-live gate — every box must pass before jobs are created |
| `jobs/` | Full bodies of the 7 recurring jobs, chat IDs placeholdered |
| `scripts/` | `carousel_digest_themes.py` (digest skins), `linkedin_carousel.py` (concept carousels), `carousel_theme_d.py` (legacy theme) |
| `playbooks/` | Overhaul playbook (profile-copy template), 6-week pipeline brief, idea-backlog template, voices list, week-plan template, one worked example brief |
| `brand/` | `avatar.jpg` — the ONLY avatar allowed on digest slides — + brand notes |

## Honest limits

- No credentials transfer; the LinkedIn login is re-entered by the owner
  through the vault, and a fresh browser profile must be created and its
  composer tested before any publish attempt.
- LinkedIn's UI drifts and its session behavior is the lane's #1
  operational risk — the lessons doc exists because of it.
- Engagement history and the post queue are your own live state on the
  new account; the live profile is always the source of truth.
- Run the digest as a trial first (the original ran a 2-week trial,
  then reviewed): cadence after the trial is the owner's call.
