# Verification mechanics

Compile acceptance before final judgment from the intent contract, Domain Brief,
expert-refined criteria, output contract, and downstream interfaces.

## Evaluator contract

An evaluator is a specialized assurance role, not another creator or generic critic.
Require independence/conflict disclosure; exact artifact version, atomic criteria,
authority, and audit boundary; direct admissible evidence; domain competence;
deterministic recomputation or explicit sampling; stable exception IDs mapped to
claim, decision, owner, and repair; and a scoped verdict with invalidating evidence.

Classify every criterion `DESIGN`, `IMPLEMENTATION`, `OPERATION`, or `OUTCOME`, then return `PASS`,
`FAIL`, or `NOT_TESTABLE` with evidence. A promised procedure can pass design only;
unexecuted implementation, operation, or outcome work and missing evidence are `NOT_TESTABLE`.
Separate deterministic exceptions, judgment disagreement, and evidence gaps.

Deterministically reject verdicts missing version, criterion status, inspectable
evidence, exception mapping, or marking unexecuted work `PASS`. Report template
readiness separately from intent acceptance.

## Layered checks

1. **Deterministic:** outputs, schema, IDs, counts, references, dependency order,
   tool/test results, limits, and explicit constraints.
2. **Domain:** facts, mechanisms, standards, edges/failures, executability, usability.
3. **Integration:** contradiction, interfaces, authority, shared assumptions, and
   semantic conservation of every accepted intent and consequential qualifier.
4. **NFR:** child calls, tokens, executor latency, output size, redundant questions,
   unnecessary specialists, failed tools, and unresolved state.

Use tools for deterministic truth and an independent context-qualified evaluator for
judgment. Give it the intent, relevant Brief, artifact, and atomic criteria—not the
creator's private reasoning or confidence. Require criterion-level evidence and
severity, not a holistic score. Catastrophic or authority failures cannot be averaged
away.

On failure, return the original artifact and failed criteria for one targeted repair;
rerun all critical checks and regression-check passed ones. Repair itself never
passes: only a reserved renewed independent verdict can accept the revision. Without
that slot, or with remaining material failure, mark `PARTIAL`/`BLOCKED` and name the
gap, safe interim action, owner, and escalation.

The final response maps every accepted intent to its artifact or explicit status and
reports material uncertainty and limitations; omit internal mechanics unless asked.
