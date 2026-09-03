# Verification mechanics

Compile acceptance checks from the intent contract, Domain Brief, expert-refined
success criteria, output contract, and downstream interfaces before final judgment.

## Evaluator contract

An evaluator is a specialized assurance role, not a second creator or a generic
critic. Compile its charter from the decision and evidence regime. Require:

- independence and conflict disclosure, including prior authorship or advocacy;
- the exact artifact version, atomic criteria, authority, and audit boundary;
- direct access to admissible evidence needed to reproduce each material claim;
- domain competence for the mechanisms and professional artifact being judged;
- deterministic recomputation where possible and explicit sampling where exhaustive
  checking is impossible;
- stable exception IDs mapped to the affected claim, decision, owner, and repair;
- a scoped verdict and the evidence that would invalidate it.

Classify each criterion as `DESIGN`, `IMPLEMENTATION`, or `OUTCOME`, then return
`PASS`, `FAIL`, or `NOT_TESTABLE` with evidence. A promised procedure may pass a
design criterion; it cannot pass implementation or outcome criteria that were not
executed. Missing evidence is `NOT_TESTABLE`, never a semantic pass. Distinguish
deterministic exceptions, judgment disagreements, and missing evidence.

Validate the verdict schema deterministically. Reject a verdict that lacks version,
criterion status, inspectable evidence, exception mapping, or that marks an
unexecuted implementation/outcome check `PASS`. State separately whether the
artifact is ready as a template and whether the consequential intent is accepted;
a usable blocked template does not make the blocked outcome pass.

## Check in layers

1. Deterministic checks: required outputs, schema, identifiers, counts, references,
   dependency order, tool/test results, limits, and explicit constraints.
2. Domain checks: factual correctness, mechanism validity, standards fit, edge and
   failure behavior, artifact executability, and downstream usability.
3. Integration checks: contradiction, interface compatibility, authority, shared
   assumptions, and preservation of every accepted intent.
4. NFR checks: child calls, tokens, latency, output size, redundant questions,
   unnecessary specialists, failed tools, and unresolved state.

Use code or tools for deterministic truth. Use an independent, context-qualified
evaluator only for semantic judgments. Supply the evaluator the intent, relevant
Domain Brief, artifact, and atomic criteria—not the creator's private reasoning or
self-confidence. The evaluator returns criterion-level evidence and failure
severity, not a vague holistic score.

Catastrophic or authority failures cannot be averaged away by high total scores.
When a check fails, return the original artifact plus failed criteria for one
targeted repair. Re-run all critical checks and regression-check previously passed
ones. A repair is not a pass: only the renewed independent verdict can accept the
revised version. Reserve that verdict before execution or mark the repaired intent
`PARTIAL`. If material failure remains, mark the intent partial/blocked and name
the missing evidence, safe interim action, owner, and escalation path.

The final response must map every accepted intent to its delivered artifact or
explicit status. Report material uncertainty and limitations; omit internal
ceremony and mechanics unless the user asks for them.
