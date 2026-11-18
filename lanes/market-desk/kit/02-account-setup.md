# 02 — Account Setup (broker side)

Written generically for [YOUR BROKER]. The worked example behind this kit
is a broker that offers an official trading MCP with a dedicated agent
account and in-app trade approvals; adapt the names and steps to your
broker. If your broker offers neither, skip to read-only mode: the desk
works from the account data you provide, and steps 2, 4, and 6 don't
apply.

1. Sign in to your broker yourself (your own credentials, your own hands —
   the agent never receives the password).
2. Open the agent/MCP trading account from the broker's agent flow if it
   does not exist yet (typically a separate, limited-margin account; no
   options level). Fund it at pilot scale — [YOUR PILOT SIZE], an amount
   you can afford to experiment with.
3. Connect the trading MCP/API via doc 04 (OAuth). Verify with the
   account read: identify the main (default individual), any joint/other,
   and the pilot (agent-trading allowed) accounts; record the identifiers
   in worksheet rows 5–7.
4. **SAFETY GATE — Trade approvals.** For EXTERNAL agents, at least one
   major broker's default has trade approvals OFF — meaning agent orders
   would execute with no human tap. Read the trade-approval setting for
   the pilot account. If "human must approve trades" is false, STOP: turn
   Trade approvals ON in the broker's app (pilot account → agent settings
   → safety controls) — only you can change it; no tool exists. Re-read
   and confirm `true` before any order capability is enabled in the
   client.
5. Sanity reads: portfolio + positions for each account; pending trade
   approvals (expect empty); save the baseline snapshots in the working
   directory.
6. Only after steps 1–5: enable the order place/cancel tools in the local
   client allowlist (doc 04) and run the small test-trade protocol
   (doc 07) to prove the place → approve → fill loop end to end.
