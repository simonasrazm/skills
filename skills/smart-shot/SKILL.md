---
name: smart-shot
description: Resolve ambiguous or consequential requests through runtime specialists, authorized action, and independent acceptance. Use when invoked or uncertainty could change outcomes, authority, dependencies, or irreversible risk; costs more than Fast Shot.
---

# Smart Shot

Treat the prompt as evidence, not automatically the task. Before committing, resolve
intent and operationalize consequential qualifiers while preserving user wording,
constraints, outputs, and relative or aspirational targets.

## Control loop

1. **Resolve:** classify clauses into an intent graph. Infer only supported outcomes;
   label consequential uncertainty.
2. **Partition:** apply isolation rules before grouping, sequence one-way
   dependencies, and share discovery only when the grouping test passes.
3. **Discover:** recursively compile a domain graph per isolated intent/group. Stop
   at competence leaves whose methods, evidence, failures, and professional artifact
   form one practice. Brief every material leaf; retain concerns as `ACTIVE`,
   `CONDITIONAL(trigger)`, or `UNRESOLVED`. Status routes work, never scope. Admit
   domain-native objects through the work-graph extension test.
4. **Charter:** cover competence leaves before optimizing specialist count. Assign
   every material leaf, interface, and independent validation duty to a
   context-qualified runtime contract. Merge only with positive proof; shared topic
   or intent is insufficient. Preserve independently failing leaf questions, checks,
   and verdicts; use another agent only when competence, authority, conflict, or
   artifact ownership requires it. Structural or semantic topology failure blocks
   dispatch.
5. **Execute:** dispatch required charters; only agent IDs returned by successful
   tool calls count as delegation. If unavailable, execute locally with reduced
   assurance or expose the blocker. Experts perform the authorized work their intent
   requires, not default research or advice when an executable target-state change is
   required. Run ready work concurrently and import validated upstream artifacts.
   Each consequential intent retains its decision artifact, acceptance ledger,
   verdict, and repair state. Tool results outrank narration.
6. **Act:** an `ACTION` changes target state; an `OPERATION` creates a missing
   observation that can change or validate a decision. Run ready nodes in dependency
   order within authority; preserve receipts/read-back and update affected work. A
   plan, recommendation, or attempted call is not execution.
7. **Integrate:** admit passed artifacts only. Reconcile factual, objective,
   interface, and authority conflicts without averaging incompatible conclusions.
   Preserve imported stable IDs; propagate changes through dependent decisions,
   cost, schedule, risk, and revalidation.
8. **Verify:** run deterministic checks first and qualified semantic evaluation for
   judgment. Classify checks as design, implementation, operation, or outcome;
   unexecuted checks are `NOT_TESTABLE`. Require independent semantic acceptance when
   material judgment, authority, conflict, or risk demands it; low-risk deterministic
   acceptance may close locally.
9. **Repair or exit:** repair failed semantic criteria once without weakening passed
   ones, then rerun critical, regression, and renewed independent checks. Compiler
   and boundary failures fail closed outside this repair budget. Deliver, narrow
   scope, or escalate the exact blocker.

After a failed check or material change, restart at the earliest affected stage:
intent/constraint → Resolve; grouping/dependency → Partition; missing concern →
Discover; ownership/contract → Charter; artifact defect → Execute; conflict/stale
import/interface → Integrate; missing action, observation, protocol, precondition,
operator, authority, or control → Act; verdict defect → Verify. Increment changed
node versions, invalidate causal descendants, preserve unaffected passed nodes, and
resume forward. Exit only when every accepted intent is terminal and no required
node is unresolved or stale.

Load references progressively:

- [intent mechanics](references/intent-mechanics.md): resolution, topology, integration;
- [domain mechanics](references/domain-mechanics.md): briefs and specialist routing;
- [expert mechanics](references/expert-mechanics.md): charters and execution;
- [action mechanics](references/action-mechanics.md): outcome-producing state changes;
- [operation mechanics](references/operation-mechanics.md): empirical evidence production;
- [work-graph mechanics](references/work-graph-mechanics.md): consequential multi-node work;
- [verification mechanics](references/verification-mechanics.md): acceptance and repair;
- [delivery-constraint mechanics](references/delivery-constraint-mechanics.md): measurable output gates.

## Resource and stopping rules

- Respect concurrency. Budget successful calls before dispatch and reserve named
  slots backward from acceptance: independent verdict, one creator repair when
  needed, and renewed verdict. Failed dispatches consume no successful-call slot;
  release reserves only when their trigger becomes impossible. Without renewed
  review after repair, report `PARTIAL`.
- Set each artifact's output ceiling from its use case. Keep one canonical ledger
  and reference stable IDs. Exceed a ceiling only for a named acceptance check, and
  report the overage with criterion-level justification.
- Give every call a contract, ceiling, and observable stop event. Use executor
  deadlines, not wall-time estimates; persist usable evidence before retry/reassignment.
- Ask only when an answer can change an outcome, decision, criterion, dependency,
  risk, or artifact and no safe default exists.
- Checkpoint contracts, evidence, decisions, and passed criteria before replacing an
  expert whose context may truncate.
- Stop expanding when every material concern has a decision, falsifiable check,
  condition, or escalation. Deliver every accepted intent or mark it `PARTIAL`,
  `BLOCKED`, or out of scope.
