# 07 — Pipeline Runbook (LinkedIn Pipeline)

State lives in the goal workspace: `files/` (backlog, week plans),
`hidden_files/linkedin-queue.json` (scheduled → commented → measured),
`hidden_files/engagement-log.jsonl`, `hidden_files/daily-packages/`,
`hidden_files/digest-edition.txt`.

## Sunday — set the week

1. **18:39 — weekly calendar job** (`jobs/03`): fresh research +
   engagement data → next week's plan file (`files/linkedin-week-plan-
   <monday>.md`) + chat summary: topics, hooks, formats, carousel
   outlines for Tue/Thu/Sat + the Sunday ship slot.
2. **~18:00 — AI Week Digest** (`jobs/05` pattern + digest build):
   best-per-slot from the week's digests, Poster skin, native-scheduled
   6 PM, first comment with sources.

## Daily — the digest

3. **07:00 — digest build job** (`jobs/01`): sweep the technical sources
   (doc 03A), pick the 5-slot slate, write the spec JSON, render with
   `scripts/carousel_digest_themes.py poster <spec> <pkgdir>/
   carousel.pdf`, verify 8 pages, render EVERY slide to PNG and LOOK at
   each one (cover contents + recap included), write the package
   (`daily-packages/<date>-digest/package.json`), bump the edition
   counter, present copy + first comment + PDF for approval.
4. **On approval:** publish LIVE from the warm LinkedIn Fresh session;
   ~10 min later post the first comment in the same session; verify both
   on the public profile; report the live URL.
   **Unapproved by ~7:45:** native-schedule for 8:00 + deliver the
   paste-ready first-comment text for his manual paste.

## Mon/Wed/Fri/Sat evening — finalize the next concept post

5. **19:39 — finalize job** (`jobs/02`): take the next entry from the
   week plan; fresh research, verify every claim; write full copy
   (150–250 words, hook first, one genuine question, 3–5 hashtags);
   build the asset (carousel via `scripts/linkedin_carousel.py`, or
   infographic/poll/text per the plan); write the first-comment text;
   save `daily-packages/<date>/package.json`; deliver copy + asset +
   first comment + the exact closing line asking for
   `schedule` / `edit:` / `skip`.
6. **On `schedule`:** browser task on LinkedIn Fresh — spawn minimal,
   steer with files; paste copy; attach the PDF as a document (or build
   the native poll); clock icon → schedule Tue/Thu/Sat 07:40 (Sunday
   ship posts 09:00/18:00 per plan); record in `linkedin-queue.json`;
   confirm in chat.

## Publish mornings — first comments

7. **Tue/Thu/Sat 07:50 job** (`jobs/04`) and **Sunday 09:40 job**
   (`jobs/05`): post the package's first-comment text (sources + channel
   block). Standing tweak (2026-10-20): for Thu/Sat posts, prefer
   posting the sources comment in a fresh morning session right after
   the post fires and VERIFY it landed, rather than trusting the
   standalone step — standalone scheduled comments keep missing.
   If walled: hand him the exact text to paste manually.

## Evenings — engagement

8. **19:39 — topic options job** (`jobs/07`): three topic candidates
   for tomorrow where the plan has gaps. (Largely superseded by the
   finalize flow — see doc 10.)
9. **20:39 — engagement monitor** (`jobs/06`): metrics sweep + drafted
   reply suggestions. Replies go out only with his approval of the exact
   text. The owner's own first-hour reply block stays his — it's the
   strongest reach lever and can't be automated.

## Failure handling (all steps)

- Session walled/dead → close, ONE fresh attempt, then hand the owner
  the manual path (copy/text). Never hammer.
- Builder error → report it; never ship a broken PDF.
- Thin research day → present honestly; a skipped day beats a filler
  post.
