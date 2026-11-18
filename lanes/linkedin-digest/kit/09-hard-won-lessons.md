# 09 — Hard-Won Lessons (LinkedIn Pipeline)

Standing rules bought with real failures. Read before the first publish.

## 1. The default browser profile's editor is corrupted — LinkedIn Fresh or nothing

The default profile fails deterministically on the composer, repost,
and comment boxes ("There was a problem loading the content") while the
feed reads fine. It is profile-level asset corruption — NOT a CAPTCHA,
NOT an account/IP block (a bot-check check confirmed no challenge
exists). The fix that worked: a FRESH named profile ("LinkedIn Fresh"),
signed in via the native form, composer TESTED before composing. All
LinkedIn browser work uses the Fresh profile until the default is
repaired or replaced. Related: sessions that sit at "working" with zero
page actions for minutes are dead — stop, close, check the window state;
don't spawn more sessions on top.

## 2. Sessions die between runs — publish + comment in ONE warm session

The old pattern (native-schedule now, separate comment run later)
failed 3 straight times: the session alive at build time was dead by
the comment run, and first comments silently never landed (two early
digest editions and two concept posts in the original lane).
Current model: publish LIVE on approval while the session is warm,
first comment ~10 min later in the SAME session, verified on the public
post. When a comment can't land, deliver paste-ready text immediately —
never let it ride to the next run. For scheduled (native) posts, post
the sources comment in a fresh morning session right after the post
fires and verify it.

## 3. Never touch the password after a rejection

The saved LinkedIn login was rejected ("wrong email or password") more
than once; re-saves didn't stick, and the agent-side rule became: after
a rejection, STOP — hand the owner the paste-ready text and let him
re-save the credential himself. The owner's most recent vault update
is the working entry; a saved entry is trusted on the owner's word and
must never be "tested" autonomously.

## 4. His pick is per-post, and dropped means dropped

- The workslop explainer was LOCKED on Oct 16, finalized Oct 20 — and
  dropped by him on sight ("didn't understand it, not interested").
  Dropped topics are never revived; the slot reopens and candidates are
  presented as a pick.
- An excluded project was removed from the lane mid-flight: a finalized,
  presented ship post was dropped the same evening and marked skipped
  so nothing downstream picked it up. When he drops something, mark it
  in the backlog/queue immediately.
- A finalized post he set aside is not "pending approval" — it's dead
  unless he resurrects it by name.

## 5. Design taste is a gate, not a garnish

- POSTER skin won because he liked the light background + per-slot
  colored bars; statdeck was rejected on sight ("Stat is not good") and
  is banned even though it renders fine.
- Pink-dominant palettes read wrong to him (a v3 sketchnote rejected);
  orange/blue/ink is the safe system.
- Pale emoji as icons rendered near-invisible once — drawn SVG icons in
  solid chips only.
- Carousel bullets over ~125 chars silently lose their tail in the PIL
  builder (bit twice) — visually QA every slide's last bullet.

## 6. Bot posture

Human pacing, always: paced sequential actions, natural pauses, never
rapid-fire. When stuck on LinkedIn, HOLD — close all sessions, pause,
reopen fresh. Bot-like speed is what triggers their checks, and a locked
account costs more than a late post.
