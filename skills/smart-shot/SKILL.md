---
name: smart-shot
description: Resolve ambiguous requests into expert-executed outcomes. Use when invoked or uncertainty could change the result, authority, dependency, acceptance, or irreversible risk.
---

# Smart Shot

Treat the prompt as evidence about the task, not automatically as the task.
Do not commit to a deliverable until intent resolution completes. Preserve the
user's wording, constraints, requested outputs, and comparison set for superlatives.

## Control loop

1. **Resolve:** classify prompt clauses and compile an intent graph. Infer only
   outcomes supported by prompt/context; label uncertain consequential intent.
2. **Partition:** apply hard isolation rules before grouping. Sequence one-way
   dependencies. Share discovery only where the grouping test passes.
3. **Discover:** compile a Domain Brief for each isolated intent or valid discovery
   group. Retain every material concern and mark it `ACTIVE`, `CONDITIONAL(trigger)`,
   or `UNRESOLVED`; a label may route work but never erase scope. Before dispatch,
   deterministically validate IDs, concern-to-owner/check mappings, boundaries,
   and an acyclic specialist graph. Evaluate semantic coverage independently. Do
   not dispatch a structurally invalid plan.
4. **Charter:** compile the smallest set of context-qualified specialists that owns
   every material concern, interface, and independent validation duty. A specialist
   is a runtime contract, not merely a profession label.
5. **Execute:** spawn each required specialist with its compiled charter; record
   the returned agent identifier before waiting. Each consequential intent keeps
   its own decision artifact, acceptance ledger, validation verdict, and repair
   state. Run dependency-ready work concurrently; import only validated upstream
   artifacts. If delegation is unavailable, execute locally and label that fallback
   instead of claiming an expert ran.
6. **Integrate:** reconcile factual, objective, interface, and authority conflicts.
   Integrate passed artifacts only; preserve imported stable IDs and propagate
   changes through dependent decisions, cost, schedule, risk, and revalidation.
   Never average incompatible expert conclusions.
7. **Verify:** run deterministic checks first and qualified semantic evaluation only
   where judgment is required. Classify checks as design, implementation, or outcome;
   unexecuted checks are `NOT_TESTABLE`, never `PASS`. The creator never supplies
   final acceptance.
8. **Repair or exit:** for a semantic artifact failure, repair the failed criteria
   once without weakening passed ones. Re-run critical and regression checks. Then
   deliver, explicitly narrow scope, or escalate the exact blocker. Compiler and
   boundary invariant failures fail closed rather than consuming this repair budget.

Load references progressively:

- [intent mechanics](references/intent-mechanics.md) for resolution, topology, and integration;
- [domain mechanics](references/domain-mechanics.md) for briefs and specialist routing;
- [expert mechanics](references/expert-mechanics.md) for charters and execution;
- [work-graph mechanics](references/work-graph-mechanics.md) for consequential multi-node work;
- [verification mechanics](references/verification-mechanics.md) for acceptance and repair;
- [delivery-constraint mechanics](references/delivery-constraint-mechanics.md) for measurable final-output gates.

## Resource and stopping rules

- Respect the runtime's concurrency cap and never exceed five active subagents.
  Spend calls on distinct competence, evaluation, or dependency-ready work.
- Before dispatch, declare a total call/time/output budget and reserve capacity in
  reverse from the acceptance gate: independent verdict, creator-owned targeted
  repair, and renewed verdict after repair. Release unused reserve only after a
  pass; if the runtime cannot fund a renewed verdict, label a repaired result
  `PARTIAL` rather than treating repair as acceptance.
- Set a per-artifact output ceiling from the user's use case before dispatch. Keep
  one canonical ledger and reference stable IDs instead of repeating full records.
  Exceed the ceiling only when a named acceptance check requires the added content;
  report the overage and its criterion-level justification.
- Distinguish successful inference calls, failed dispatches, and simultaneously
  active agents. Timebox each call from task stakes and runtime limits; checkpoint
  its contract and usable evidence before interruption or reassignment.
- Never call `wait` without at least one successfully spawned unfinished agent.
- Ask the user only when the answer can materially change an outcome, decision,
  criterion, dependency, risk, or artifact and no safe default is defensible.
- Checkpoint contracts, evidence, decisions, and passed criteria before replacing
  an expert whose context may truncate the work.
- Stop expanding when each material concern has a decision, falsifiable check,
  explicit condition, or named escalation. Completeness means every accepted
  intent is delivered or explicitly reported as partial, blocked, or out of scope.
