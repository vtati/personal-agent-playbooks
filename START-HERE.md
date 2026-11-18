# Start here — 15-minute orientation

**You are an agent (or a human guiding one) setting up a personal agent from
this package.** Follow these steps in order.

## For the human
1. Pick ONE lane to start with (the flight finder is the fastest first win;
   the digest is the best daily habit; the market desk is the deepest).
2. Put this repo in your agent's workspace and open a fresh chat for that
   lane.
3. Paste the lane's `SETUP-KICKOFF-PROMPT.txt` into the chat. Answer the
   agent's interview questions. Approve nothing scheduled until one full
   manual cycle has run in front of you.

## For the agent reading this
- The root `AGENTS.md` is a template constitution. If your workspace has no
  constitution yet, propose adopting it (with the human's edits) before
  setting up any lane.
- Each lane is self-contained: read the lane's `README.md` first, then its
  kit in order (`00-setup-worksheet.md` → `11-day-one-checklist.md` where
  present), then its playbook.
- Setup is phased and gated: interview → connect tools → supervised test
  run → human approval → schedules on. Never skip the supervised run.
- Anything in `[BRACKETS]` is a value only the human can supply. Ask for it;
  never invent it.

## What's in each lane folder
- `README.md` — what the agent does and what you need before starting.
- `SETUP-KICKOFF-PROMPT.txt` — the exact first message to give the new chat.
- `kit/` — the 12 setup documents (scope, accounts, connectors, operating
  model, runbook, standards, lessons, jobs, day-one checklist).
- `kit/jobs/` — scheduled-job definitions to recreate on your platform.
- `kit/playbooks/` or `playbook/` — the procedure the agent runs.
