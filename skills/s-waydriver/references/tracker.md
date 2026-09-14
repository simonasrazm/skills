# Tracker Operations

Prefer the project's configured issue tracker and its native child, dependency, assignment, label, notification, and query primitives. The tracker should make the frontier visible without reconstructing it from prose.

Bind tracker operations to the intended account/tenant, project or repository, and visibility using project configuration and existing work. A connected tracker or source repository is not itself the destination: a public skill repository need not host a person’s private execution tickets. If the binding remains ambiguous, keep work local until the destination is resolved; do not create external tickets to discover it. Verify native IDs and actual states rather than treating a local label mapping as a tracker mutation.

Maintain two linked carriers:

- a Wayfinder-compatible **decision map** with decision-ticket children;
- a **delivery map** with acceptance-bearing implementation children.

Create all units before wiring dependency edges when the tracker needs stable ids. Claim a unit before work. Resolve it with the answer or artifact, evidence pointer, newly exposed fog/frontier, and a concise pointer from its parent map. Keep detail in one authoritative location.

Without configured tracker operations, use:

```text
.scratch/<effort>/
├── map.md
├── delivery.md
├── issues/
│   └── NN-<decision-name>.md
└── delivery/
    └── NN-<unit-name>.md
```

Decision files carry `Type`, `Status`, and `Blocked by`. Delivery files carry `Status`, `Blocked by`, acceptance, candidate, and evidence pointers. The frontier is the open, unblocked, unclaimed set in the relevant carrier.

An executing delivery file also links its [execution run](execution-runs.md) at `.sflo/NN-<slug>/run.md`. These are project-root paths, independent of the local or external tracker carrier.

External trackers may express the two maps and their children differently; preserve the semantics rather than inventing provider commands. If native blocking is absent, record explicit dependencies in the unit and derive the frontier from them.

Carry each unit’s applicable source commitments, interfaces and acceptance evidence into its handoff, with a retrievable source. Reconcile existing work before creating duplicates. New in-scope findings remain linked to the map; superseded decisions retain a pointer to their replacement and invalidate affected work. Distinguish waiting from active claims, and verify claim ownership before releasing or taking over unfinished work.
