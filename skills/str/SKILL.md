---
name: str
description: Evidence-first STR (Simon Troubleshoot) diagnostic workflow for human-triggered troubleshooting. Use when the user says "STR:" or asks to diagnose what is wrong, find a root cause, challenge assumptions, or produce a data-driven troubleshooting report using isolated Troubleshooter and Interrogator roles. Requires two independent role contexts; refuse rather than simulate both roles in one shared context.
---

# STR

## Contract

STR is a three-role troubleshooting loop:

- Lead: coordinates the run and protects role isolation.
- Troubleshooter: collects evidence, builds hypotheses, and writes diagnosis artifacts.
- Interrogator: audits evidence, attacks assumptions, scores quality, and returns PASS or REVISE.

Run STR only when the agent runtime can create independent role contexts for
Troubleshooter and Interrogator. If not, stop and say STR requires independent
role contexts. Do not role-play both roles in one shared context.

## Instructions

The active agent is Lead. Coordinate the STR run without doing the
Troubleshooter or Interrogator work yourself.

1. Receive the human problem and set the run budget. Default: up to 3 rounds unless the user asks for a different budget.
2. Start or select a Troubleshooter context. Send the problem plus only `references/troubleshooter.md`.
3. Start or select an Interrogator context. Send the diagnosis artifact plus only `references/interrogator.md`.
4. Use `references/dimensions.md` when interpreting Interrogator scores.
5. On PASS, return the final report to the user.
6. On REVISE, send only the Interrogator feedback artifact back to the same Troubleshooter role context.
7. Continue only while evidence progress is real and run budget remains.
8. If a role reports `context_used_pct >= 80`, require that role to compact before another round.

## Final Report

Return:

- Root cause OR unresolved finding.
- Evidence table with sources, observations, and collection method.
- Hypothesis ledger with supporting evidence, contradicting evidence, and status.
- Confidence grounded in evidence quality.
- Known gaps and why they matter.
- Next safe probes likely to improve clarity.
- Recommended fix only if the root cause is evidence-backed and the fix clearly targets it.

## Non-Negotiables

- Every claim must trace to numbered evidence.
- No evidence for a hypothesis means UNTESTED, not LIKELY.
- Role memory must stay isolated; exchange artifacts, not hidden shared context.
- Role context quality must be protected; compact before degradation, not after.
- Full reproduction is outside v1 STR.
- STR is a clarity tool, not a fixer.
