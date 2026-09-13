---
name: security-check
description: Independently assess a change, product, workflow, or deployment for realistic security and privacy risk, reporting outcome separately from coverage. Use for trust-boundary or exposure changes and explicit security review.
---

# Security Check

Use the strongest available security specialist.

Independent assessment starts in a fresh context with the accepted contract, candidate identity, and relevant project constraints, without inherited builder conversation or rationale. A review performed in the builder's context remains self-verification.

Derive the threat model from the actual candidate, changed surface, assets, actors, trust boundaries, data paths, deployment, and project requirements. Prefer realistic abuse and reproducible evidence over a universal checklist or speculative severity.

Inspect the frozen candidate without modifying maintained product or tests. Safe temporary probes may live outside maintained output when authorized. Report each finding with affected candidate, evidence, plausible impact, confidence, and the smallest useful repair direction. Return repair to the implementation owner, then renew affected security evidence against the new candidate.

Report **outcome** and **coverage** separately. Required checks that are unavailable, incomplete, unsafe, or erroneous keep the coverage verdict incomplete. Scope probes and external mutations to the authorization granted for the review.

Return the report in-channel; create no report or run-state artifact unless requested.
