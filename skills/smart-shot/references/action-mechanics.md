# Outcome-action mechanics

Use an `ACTION` when an accepted intent requires a target-state change beyond a
conclusion or the requested artifact itself. Examples include creating, modifying,
configuring, migrating, deploying, communicating, purchasing, or operating, but the
actual form is derived at runtime. Do not turn an action request into a research
report or implementation plan when the action is authorized and executable.

## Admission and ownership

Admit an action only when it is causally necessary for the accepted outcome, within
scope, and assigned to a competent operator. Resolve required inputs, dependencies,
authority, and latest safe decision point before crossing an irreversible or
externally consequential boundary. Approval to analyze, recommend, or design does
not authorize mutation.

The responsible expert may design and perform the action when competence and
authority fit. Separate designer, operator, approver, and outcome validator when
their competence, permissions, conflicts, rollback duties, or acceptance can differ.
An artifact is the outcome when the user requested that artifact; do not invent an
additional action merely to populate the graph.

## Action contract

Compile only fields that change execution, safety, or acceptance:

- owning intent and criterion; before-state, target state, subject/scope, and
  observable completion evidence;
- operator, tools, permissions, dependencies, sequence, invariants, and handoffs;
- expected effects, affected parties/systems, maximum downside, reversibility,
  checkpoint, stop, rollback, retry/idempotency, and escalation when material;
- read-back method, validator, outcome threshold, residual state, and invalidating
  changes.

## Outcome-production loop

`Accepted intent/decision → smallest sufficient action → preflight/authorize → perform →
read back target state → validate outcome → update dependents`

Repeat only while another action is required by the accepted outcome. Every pass
must create a verified state transition, complete a dependency, or expose an exact
blocker. Preserve partial effects and rollback status. A proposed, queued, attempted,
or narrated action is not completed execution; tool success without outcome read-back
proves at most implementation or operation, not the target outcome.
