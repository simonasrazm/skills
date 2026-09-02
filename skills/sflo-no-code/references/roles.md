# Roles

Read this file at run start. Give each gate owner only relevant gate instructions and direct artifact paths.

## Orchestrator

Own the run, not specialist work.

- Create the run directory and `RUN.md`.
- Select capable PM, developer, and fresh QA agents.
- Verify artifact existence, revisions, evidence, grade, and freshness before transitions.
- Maintain attempt counters and archive superseded artifacts.
- Own `SHIP-DECISION.md` and the final `RUN.md` outcome.
- Escalate after ten failed Build→Test attempts.

Do not build, perform QA, or conduct PM verification. Do not certify missing evidence from chat memory.

## Product manager

Own Discover and Verify. The same PM may perform both, but must be distinct from builder and QA.

- Discover external-data needs and verify sources when required.
- Define exact deliverables and testable acceptance criteria.
- During Verify, compare current delivery evidence against original scope.
- Record deviations rather than repairing the product.

## Developer

Own Build and every Build retry.

- Read current `SCOPE.md` directly.
- On retries, also read current `QA-REPORT.md` or `PM-VERIFY.md` directly.
- Build product deliverables, connect required real data, run self-checks, and record evidence.
- Never approve own work or write QA/PM grades.

## QA tester

Own Test. Use a fresh agent instance that did not build the product.

- Exercise real product outcomes and required external data.
- Test every acceptance criterion, core journey, error state, relevant edge case, and performance.
- Record exact evidence and actionable findings.
- Do not change product deliverables. Return findings to Build.
- Grade honestly; only A advances.

## Availability stop

If role separation or a fresh QA context is unavailable, mark run blocked and ask the human. Never collapse builder, QA, and verifier into self-approval.

