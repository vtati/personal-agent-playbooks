# 11 — Day-One Checklist (manual test cycle BEFORE any job is created)

- [ ] Kickoff interview done; worksheet (doc 00) filled except secrets
- [ ] Broker accounts identified via the account read; pilot account
      exists and is funded at your chosen pilot size (or the lane is
      declared read-only — a valid end state)
- [ ] Trade approvals read on the pilot account: human must approve
      trades = true (owner toggles in-app if not; re-read to confirm)
- [ ] Connector client installed; allowlist = reads + review tools only
- [ ] Baseline snapshots saved (portfolio + positions, all accounts)
- [ ] Playbook read end to end; Section 0 regime snapshot written fresh
      for your market (refresh via web/finance search — the template
      ships blank on purpose)
- [ ] Holdings analysis run once by hand (runbook protocol) and compared
      against playbooks/holdings-analysis-template.md format
- [ ] One manual pre-market brief produced in chat and reviewed by owner
- [ ] Scanner test run: `python3 tools/tests/run_tests.py` green (20/20),
      then one scanner.py run completes and writes tools/runs/
- [ ] Time Machine sanity: a broad index ETF run at −5%/+10%/20d returns
      a verdict with the base-rates caveat
- [ ] Test trade (owner-approved, pilot only): a small market buy of a
      broad index ETF (≈5% of the pilot) → owner approves in app → fill
      verified from the orders read → fill recorded in a new
      TRADE-LOG.md. Only now add place/cancel to the client allowlist
      (they were enabled for this test under owner supervision) — if the
      test cannot run, the lane stays read-only
- [ ] Owner approves go-live → create the six jobs from jobs/ → read each
      back → confirm first fire times
