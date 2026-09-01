---
name: dig-deeper-core
description: Internal evidence-first troubleshooting engine used by dig-deeper wrappers. Requires a wrapper-supplied authority profile and independent Troubleshooter and Interrogator contexts.
---

# Dig Deeper Core

## Contract

Dig Deeper Core is a three-role troubleshooting loop:

- Lead: coordinates the run and protects role isolation and supplied authority.
- Troubleshooter: collects evidence, builds hypotheses, and writes diagnosis artifacts.
- Interrogator: audits evidence, attacks assumptions, scores quality, and returns PASS or REVISE.

A wrapper must supply the authority profile. Never infer or expand it inside
the core.

Run only when the agent runtime can create independent role contexts for
Troubleshooter and Interrogator. If not, stop and say Dig Deeper requires
independent role contexts. Do not role-play both roles in one shared context.

## Instructions

The active agent is Lead. Coordinate the run without doing the Troubleshooter
or Interrogator work yourself.

1. Receive the human problem, wrapper-supplied authority profile, optional operating guidance, and run budget. Default: up to 5 rounds unless the user asks for a different budget. The budget is a ceiling, not a target.
2. Start or select a Troubleshooter context. Send the problem, authority profile, applicable operating guidance, and only `references/troubleshooter.md`.
3. Start or select an Interrogator context. Send the problem, diagnosis artifact, authority profile, applicable operating guidance, and only `references/interrogator.md`.
4. Use `references/dimensions.md` when interpreting Interrogator scores.
5. On PASS, return the final report to the user.
6. On REVISE, send only the Interrogator feedback artifact back to the same Troubleshooter role context.
7. Continue only while evidence progress is real and run budget remains.
8. If a role reports `context_used_pct >= 80`, require that role to compact before another round.

Stop immediately on PASS. Do not spend remaining rounds after diagnostic closure.

## Final Report

Return:

- Root cause OR unresolved finding.
- Evidence table with sources, observations, and collection method.
- Hypothesis ledger with supporting evidence, contradicting evidence, and status.
- Confidence grounded in evidence quality.
- Known gaps and why they matter.
- Next probes likely to improve clarity within the supplied profile.
- Recommended fix only if the root cause is evidence-backed and the fix clearly targets it.

## Non-Negotiables

- Every claim must trace to numbered evidence.
- No evidence for a hypothesis means UNTESTED, not LIKELY.
- Role memory must stay isolated; exchange artifacts, not hidden shared context.
- Role context quality must be protected; compact before degradation, not after.
- The supplied authority profile governs evidence collection; the core adds no blanket method prohibition.
- Dig Deeper Core diagnoses and may recommend an evidence-backed fix. It never
  implements or executes remediation without a separate explicit user request.
