# Tracker Operations

Prefer the project's configured issue tracker and its native child, dependency, assignment, label, notification, and query primitives. The tracker should make the frontier visible without reconstructing it from prose.

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

External trackers may express the two maps and their children differently; preserve the semantics rather than inventing provider commands. If native blocking is absent, record explicit dependencies in the unit and derive the frontier from them.
