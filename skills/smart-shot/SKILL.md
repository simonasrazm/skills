---
name: smart-shot
description: Resolve ambiguous requests into expert-executed outcomes. Use when invoked or uncertainty could change the result, authority, dependency, acceptance, or irreversible risk.
---

# Smart Shot

Treat the prompt as evidence, not automatically the task. Resolve intent before
committing. Preserve user wording, constraints, outputs, and superlative comparisons.

## Control loop

1. **Resolve:** classify clauses into an intent graph. Infer only supported outcomes;
   label consequential uncertainty.
2. **Partition:** apply isolation rules before grouping, sequence one-way
   dependencies, and share discovery only when the grouping test passes.
3. **Discover:** compile a Domain Brief per isolated intent or valid group. Retain
   material concerns as `ACTIVE`, `CONDITIONAL(trigger)`, or `UNRESOLVED`; status
   routes work but never prunes scope. Before dispatch, deterministically validate
   IDs, ownership/check mappings, boundaries, and graph acyclicity; evaluate semantic
   coverage separately. Structural failure blocks dispatch.
4. **Charter:** compile the smallest context-qualified specialist set owning every
   material concern, interface, and independent validation duty. Each specialist is
   a runtime contract, not a profession label.
5. **Execute:** spawn required charters; record each returned agent ID before waiting.
   Run ready work concurrently and import only validated upstream artifacts. Each
   consequential intent keeps its own decision artifact, acceptance ledger, verdict,
   and repair state. If delegation is unavailable, label local execution; never claim
   an expert ran.
6. **Integrate:** admit passed artifacts only. Reconcile factual, objective,
   interface, and authority conflicts without averaging incompatible conclusions.
   Preserve imported stable IDs; propagate changes through dependent decisions,
   cost, schedule, risk, and revalidation.
7. **Verify:** run deterministic checks first and qualified semantic evaluation only
   for judgment. Classify checks as design, implementation, or outcome; unexecuted
   checks are `NOT_TESTABLE`, never `PASS`. The creator cannot give final acceptance.
8. **Repair or exit:** repair failed semantic criteria once without weakening passed
   ones, then rerun critical, regression, and renewed independent checks. Compiler
   and boundary failures fail closed outside this repair budget. Deliver, narrow
   scope, or escalate the exact blocker.

After a failed check or material change, restart at the earliest affected stage:
intent/constraint → Resolve; grouping/dependency → Partition; missing concern →
Discover; ownership/contract → Charter; artifact defect → Execute; conflict/stale
import/interface → Integrate; verdict defect → Verify. Increment changed node
versions, invalidate causal descendants, preserve unaffected passed nodes, and
resume forward. Exit only when every accepted intent has a terminal verdict and no
required node is unresolved or stale.

Load references progressively:

- [intent mechanics](references/intent-mechanics.md): resolution, topology, integration;
- [domain mechanics](references/domain-mechanics.md): briefs and specialist routing;
- [expert mechanics](references/expert-mechanics.md): charters and execution;
- [work-graph mechanics](references/work-graph-mechanics.md): consequential multi-node work;
- [verification mechanics](references/verification-mechanics.md): acceptance and repair;
- [delivery-constraint mechanics](references/delivery-constraint-mechanics.md): measurable output gates.

## Resource and stopping rules

- Respect concurrency; spend calls on distinct competence, evaluation, or ready work.
- Before dispatch, cap successful inference calls and reserve named slots backward
  from acceptance: independent verdict, one creator repair when needed, and renewed
  verdict after repair. Failed dispatches do not consume successful-call slots.
  Release a slot only when its triggering state becomes impossible. Without a
  renewed-verdict slot after repair, report `PARTIAL`.
- Set each artifact's output ceiling from its use case. Keep one canonical ledger
  and reference stable IDs. Exceed a ceiling only for a named acceptance check, and
  report the overage with criterion-level justification.
- Give every call a contract, ceiling, and observable stop event. Let executor
  deadlines govern elapsed time; never estimate wall time. On completion or external
  timeout, persist usable evidence before retry or reassignment.
- Never call `wait` without a successfully spawned unfinished agent.
- Ask only when an answer can change an outcome, decision, criterion, dependency,
  risk, or artifact and no safe default exists.
- Checkpoint contracts, evidence, decisions, and passed criteria before replacing an
  expert whose context may truncate.
- Stop expanding when every material concern has a decision, falsifiable check,
  condition, or escalation. Deliver every accepted intent or mark it `PARTIAL`,
  `BLOCKED`, or out of scope.
