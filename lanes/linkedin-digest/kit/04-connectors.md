# 04 — Connectors (LinkedIn Pipeline)

This lane has no API path for publishing — LinkedIn's API does not allow
auto-publishing to personal profiles, and tools claiming otherwise risk
the account. Everything runs through the browser + owner approvals.

## 1. Browser — LinkedIn Fresh profile (primary)

- A dedicated fresh browser profile named "LinkedIn Fresh" holds the
  LinkedIn session. Composer tested before first use (doc 02).
- Human pacing is mandatory: paced, sequential actions with natural
  pauses. Rapid-fire behavior triggers bot checks. If stuck: HOLD —
  close all sessions, pause, reopen fresh. Never hammer.
- Medium's signed-in session rides the shared browser profile for the
  digest research sweep.

## 2. Secure Vault — LinkedIn password

- The LinkedIn password (native form, [YOUR EMAIL]) is
  stored by the OWNER in the vault. The agent references it only through
  the platform's credential flow during an owner-approved sign-in.
- If a saved login is rejected: report it and stop. Never guess, never
  loop retries, never ask for the password in chat.

## 3. Research sources (no credentials beyond Medium)

- GitHub Trending, Hacker News, Product Hunt, Hugging Face, arXiv,
  framework GitHub releases, tech press — public.
- A separate AI-news research feed, if you run one
  (`~/workspace/[your-news-research]/`), is a SECONDARY input only, for
  big technical stories that are also viral. If you run a news lane on
  the same account, share the folder; otherwise recreate a research
  inbox.

## 4. Image search (special editions only)

- Daily poster editions skip b-roll entirely. Dark-skin specials may use
  `[image-search tool]`; verify image bytes before use; never
  block a digest on images.
