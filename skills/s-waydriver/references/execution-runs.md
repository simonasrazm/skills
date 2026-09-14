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

## Native SFLO

Select the executor explicitly. A native run uses `Executor: sflo` and links its `state.json` and gate artifacts from `run.md`; the native runner owns runtime state and locks. Waydriver owns the unit and its acceptance decision. Read native state rather than maintaining a second status or repair log in Markdown.

Use the native runner's reservation or attachment operation to bind the unit and contract. Resume requires the same binding. Attach existing native state only when its identity matches the intended unit; preserve its files. A Markdown-owned directory is not native state and remains with its executor. When changing executors, create a new linked run and preserve the previous run's evidence.

Check that the installed runner supports these operations before selecting native execution. Older runners can reuse unregistered directories: keep them out of Markdown-owned run directories. The portable Markdown execution loop remains available independently of native SFLO.
