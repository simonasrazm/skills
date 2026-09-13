---
name: s-qa
description: Independently verify a frozen candidate through fast, vertical-slice, or final QA and return evidence, defects, boundaries, and useful feedback. Use for QA after product changes, final simulations, or a standalone quality check.
---

# S QA

Protect the product and improve the next decision. Inspect a frozen candidate without modifying maintained product or maintained tests. Temporary probes and evidence may live outside maintained output for the check. Bind every observation to the exact candidate; a product mutation invalidates affected evidence.

Independent acceptance starts in a fresh context with the accepted contract, candidate identity, and relevant project constraints, without inherited builder conversation or rationale. A review performed in the builder's context remains self-verification.

## Select the evidence depth

- **Fast:** focused feedback near a mutation unit. Check the changed behavior, core journey, applicable acceptance, boundaries, and silent wrong output. Exclude simulations and known long-running checks. Fast QA cannot claim final acceptance.
- **Slice:** exercise a meaningful vertical slice across its real layers and interfaces. Use rendered interaction or simulation when that is where the failure can exist.
- **Final:** exercise accumulated acceptance, cross-slice behavior, regressions, integration, and the destination as a whole. This mode owns justified end-to-end simulations and reuses current unaffected evidence.

The project's testing pyramid and defined checks remain authoritative. These modes describe feedback placement and cost, not code-versus-no-code techniques.

## Produce actionable evidence

For every applicable acceptance condition, record the action or command, observed result, evidence location, and pass/fail/blocked verdict. Add a verifier-chosen probe against the riskiest plausible false pass.

A probe's exit status must match its stated expectation: required rejection is a passing outcome, not a failed test. For a new defect probe, demonstrate that the same assertion passes a contract-conforming control and fails the suspected behavior, using isolated fixtures when necessary. If a control cannot be established, report that limitation and keep the probe's verdict provisional.

Report supported observations as defects, observed boundaries or undecided policy, coverage gaps, user/operator friction, maintainability signals, or actionable opportunities. Include UI/design issues when observed, but use a rendered-interface verifier for an interface verdict. Avoid quotas and tracker pollution; connect related symptoms to the smallest evidenced cause.

After repair, independently recheck the finding and relevant regressions against the new candidate. A checker that does not return identifiable, retrievable evidence is unavailable, not passed and not pending forever.

Return the report in-channel; create no report or run-state artifact unless requested.

For a small clean candidate, use one coverage table and normally about 200 words of prose, excluding hashes and executable evidence. Cover identity, checks, observed outcomes, coverage, gaps, and verdict without repeating the table in narrative sections. Preserve each verifier-chosen probe as a complete executable command or link its saved file with the invocation and result. Expand for material findings or limitations. If a report file is requested, create its parent directory and write the complete report in one invocation; after a successful write, return its exact path and verdict without routinely rereading it. Reinspect when the write failed or its contents are uncertain.
