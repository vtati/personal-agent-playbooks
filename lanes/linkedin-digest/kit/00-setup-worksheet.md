# 00 — Setup Worksheet (LinkedIn Pipeline)

Fill/confirm every row during the setup interview. TEMPLATE kit: the
bracketed values are yours to fill in — the cadences and slots shown are
the original lane's proven defaults; keep or adjust them with the agent.

## Placeholders (must be replaced at setup)

| Placeholder | What it is | Where it appears |
|---|---|---|
| `{{UNIT_CHAT_ID}}` | The new LinkedIn unit side chat's ID | `jobs/*.md` (delivery + origin context) |
| `{{MAIN_CHAT_ID}}` | The owner's main chat ID on the new account | `jobs/01`, `jobs/02` (delivery — reports go to both chats where the original did) |
| `{{DEVICE_ID}}` | The owner's paired device ID on the new account | `jobs/*.md` (originating context JSON) |
| `{{ORIGIN_MESSAGE_ID}}` | The message that originally triggered the job's creation — provenance only; set to the setup conversation's first message ID, or leave the placeholder (the job body does not depend on it) | `jobs/04-first-comment-tue-thu-sat.md` (originating context JSON) |

## Operational values (confirm, already live)

| Item | Value |
|---|---|
| Profile | [YOUR NAME] — [YOUR LINKEDIN URL] |
| Headline | [YOUR HEADLINE] |
| Login email | [YOUR EMAIL] (native LinkedIn form + Secure Vault password — owner's updated vault entry is the working path; do NOT attempt the login autonomously during setup) |
| Browser profile | **"LinkedIn Fresh"** (old profile id `[OLD PROFILE ID]` — informational only; create a NEW fresh profile on the new account, test the composer BEFORE composing) |
| Entity name | [YOUR COMPANY LLC, if any] — use one name consistently, never an old company name |
| Portfolio | [YOUR PORTFOLIO URL] |
| Contact email (profile) | [YOUR EMAIL] |
| Off-limits topics | [TOPICS THE AGENT MUST NEVER MENTION — e.g. a past venture; referenced by the hard rules in docs 06/08 and the job bodies] |
| Excluded project | [ONE PROJECT/TOPIC DELIBERATELY OUT OF THIS LANE — see doc 01] |
| Digest | AI Dev Digest — daily (Mon–Sat), build job 07:00 ET, publish LIVE ~08:00 ET on approval, POSTER skin, 8 slides; edition counter file `hidden_files/digest-edition.txt` — seed it at **1** on a fresh setup (each build reads N from the file) |
| Concept posts | Tue/Thu/Sat 07:40 ET; finalized Mon/Wed/Fri/Sat 19:39 ET; your reply `schedule` / `edit:` / `skip` gates each one |
| AI Week Digest | Sundays ~18:00 ET (native-scheduled 6 PM pattern), best-per-slot from the week's digests; volume counter starts at Vol. 1 on a fresh setup |
| First comments | Tue/Thu/Sat 07:50 ET job + Sunday 09:40 ET job; sources/handles text comes from the post package |
| Weekly calendar | Sundays 18:39 ET → week plan file `files/linkedin-week-plan-<monday>.md` |
| Engagement monitor | Daily 20:39 ET — metrics + drafted replies; replies NEVER posted without his approval of the exact text |
| Avatar (slides) | `brand/avatar.jpg` ONLY (your own headshot, added at setup) — never any other photo file |
| Channels (first-comment block) | YouTube @[YOUR YOUTUBE HANDLE] · YouTube @[YOUR NEWS CHANNEL] · Instagram @[YOUR INSTAGRAM] · Instagram @[your-news-channel] |
| Workspace paths (recreate) | `~/workspace/linkedin-digest/` (goal home: `files/`, `tools/`, `hidden_files/daily-packages/`, `hidden_files/digest-samples/`) |
| Carousel bullet cap | ≤ ~125 characters per bullet — longer bullets silently lose their tail in the PIL builder |

## Interview questions the agent must ask

1. Has the owner re-saved the LinkedIn password in THIS account's vault?
   (Never test it autonomously — ask, don't try.)
2. Fresh browser profile created and composer tested with a throwaway
   draft? (Mandatory before the first publish attempt.)
3. Does the owner want the digest to resume at the next edition number,
   and does the Tue/Thu/Sat + Sunday cadence still stand post-cohort?
4. Medium session: does the owner want the signed-in Medium sweep
   restored (owner signs in on the shared browser profile)?
