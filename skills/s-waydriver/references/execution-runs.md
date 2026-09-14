# Execution runs

Each executing delivery unit links a project-local `.sflo/NN-<slug>/run.md`; the run links back to its authoritative unit. For a numbered unit, retain its NN- prefix in the new run name. Preserve existing unit IDs and run paths. Choose a project-wide unique slug, including an effort name when numbering repeats. Decision-only exploration stays in its decision ticket; a clear surgical change keeps its implicit unit unless durable coordination is already needed.

The unit owns acceptance, dependencies and lasting-decision links. The run owns execution progress, candidate identity, check results and repair history. Link the accepted contract revision instead of copying its requirements. Identify the contract by an immutable revision or a hashed acceptance snapshot linked from the run. The snapshot contains the accepted requirements and boundaries; status, evidence and pending-input updates stay outside it, so progress does not change contract identity.

Reserve a new directory exclusively before writing it. An existing path belongs to its existing run: inspect its binding and resume the matching run or choose another slug. Matching numbers alone do not establish identity.

```markdown
# <unit name>

Executor: markdown
Unit: <project-relative unit path or canonical tracker URL>
Contract: <accepted revision or sha256>

## Execution

Status: active | waiting | accepted | blocked
Owner: <execution context, or none while waiting>
Candidate: <immutable identity or not yet produced>
Next: <next action, or exact input and who supplies it>

## Checks and repairs

<candidate → observed check/evidence → repair → new candidate>
```

At claim and closure, follow the stored unit → run → unit links and verify the accepted contract identity. On continuation, resolve the current owner, candidate and evidence before claiming work. Keep a pending question linked from the unit and run; when its answer arrives, reconcile the answer with acceptance and decisions, resolve the waiting item and resume the newly unblocked frontier. A changed contract starts a new run linked to its predecessor; retain previous evidence with its original scope. Final acceptance links the accepted candidate and independent verdicts back from the unit.

## Persist the repair loop

The conductor owns the run record. For each cross-context handoff, assign a candidate-specific evidence path beside the run and require the executor or checker to save its receipt there before returning. Link that receipt rather than copying its report into the run. Before dispatch, persist the current candidate, unresolved findings and next action. Give each repair finding a stable identifier, candidate, reproduction or evidence pointer, and status. Hand the executor the accepted contract and unresolved findings; after repair, record the new candidate and obtain an independent recheck before resolving each finding.

Replace the run record through a temporary sibling file and rename after the write succeeds. Persist referenced evidence before linking it. On continuation, load the unit and run from disk, verify the actual candidate and evidence, and reconcile unfinished actions before repeating them. An interrupted or missing review remains incomplete. If a write fails, retain the previous record and report the persistence blocker before handing off dependent work.

This is a Markdown execution loop; `.sflo/` is its artifact location. Preserve existing run paths and evidence. When historical runner state exists, link it as source evidence and create a separately bound Markdown run for new execution.
