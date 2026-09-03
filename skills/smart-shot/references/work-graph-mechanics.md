# Generic work-graph kernel

Use this kernel only when the request contains multiple consequential decisions,
specialists, artifacts, evidence regimes, or validation duties. A simple request
whose intent and acceptance are already clear exits without constructing visible
graph ceremony or spawning unnecessary specialists.

## Typed runtime graph

Represent the work internally with stable, versioned nodes: `INTENT`, `CONCERN`,
`DECISION`, `SPECIALIST`, `ARTIFACT`, `EVIDENCE`, `GATE`, `VERDICT`, and `EXCEPTION`.
Use typed edges: `OWNS`, `REQUIRES`, `PRODUCES`, `IMPORTS`, `VALIDATES`, `CONFLICTS`,
and `INVALIDATES`. Give each active node an owner, state, required inputs, output or
terminal disposition, and local exit condition. Preserve one canonical ledger;
user-facing artifacts omit graph bookkeeping unless it aids operation or audit.

Within an execution epoch, `REQUIRES` and `IMPORTS` form an acyclic artifact DAG.
Consultation and conflict are not scheduling edges. Feedback occurs across versions:
a failed gate, changed input, activated condition, or new evidence creates a new
epoch, increments the affected version, and reopens only causal descendants.

## Admission, split, and merge

Admit a concern only when it can change a decision, criterion, dependency, evidence
need, risk, artifact, or escalation. Express it as a domain-native tuple:
`state/mechanism → invariant → failure mode → affected decision → observable check`.
Run a uniqueness pass for concerns generic axes missed, then disposition every
candidate concern rather than silently pruning it.

Split nodes when failure, verdict, rollback, authority, evidence permission,
competence, artifact, or one-way dependency can vary independently. Separate creator
and validator. Merge only when one owner, inseparable artifact, evidence/authority
regime, and verdict survive the merge. Sharing discovery never implies shared
execution. Stop recursion when a proposed split changes none of those properties or
adds no independently testable interface.

## Evidence identity and scope

Preserve each supplied or acquired material claim as an immutable `EVIDENCE` node
with a stable ID and the smallest applicable scope key: subject, component or actor,
event or state, time window, source, revision, and evidence status. Derived claims
must cite their source IDs and may narrow but never silently broaden or move their
scope. Use stable event/state IDs in conclusions; avoid relative aliases such as
“former”, “third”, or “latest” when multiple orderings could resolve differently.

Before acceptance, compare every derived claim with its cited nodes and with other
claims sharing a scope key. A changed subject, component, event, time, authority,
polarity, quantity, or maturity is a contradiction unless an explicit transformation
or reconciliation explains it. Route the mismatch to the earliest source,
transformation, integration, or prose-reference seam; never let later fluent prose
override the canonical evidence ledger.

## Closure before execution

Run four closures to a fixed point before dispatch and after every change:

1. **Coverage:** every accepted prompt clause maps to an intent, constraint, fact,
   component, uncertainty, or non-goal; every material concern reaches an owned
   decision/artifact and acceptance effect.
2. **Interface:** every import names a passing producer artifact and version; every
   export names its consumers or an explicit terminal sink; authority and uncertainty
   cross only declared interfaces.
3. **Acceptance:** every criterion names admissible evidence, maturity
   (`DESIGN`, `IMPLEMENTATION`, `OPERATION`, or `OUTCOME`), evaluator, and verdict.
4. **Invalidation:** changes traverse typed causal edges; affected descendants become
   `STALE` until regenerated or revalidated, while unrelated passing nodes remain closed.

## Nested convergence loops

- **Node loop:** contract → produce → deterministic check → semantic check when
  needed → `PASS`, `BLOCKED`, or one bounded repair.
- **Intent loop:** continue while required nodes become ready, interfaces remain
  open, conditions activate, or a verdict makes a descendant stale.
- **Orchestration loop:** integrate terminal intent artifacts and repeat only affected
  subgraphs until every accepted intent has a terminal verdict and no required node
  is unresolved or stale.

Each iteration must close an obligation, change a version, consume repair reserve,
or record a blocker. An unchanged state cannot repeat. Budget exhaustion yields
`PARTIAL` or `BLOCKED`, never `PASS`.

## Delivery contract gate

Compile the user's measurable delivery constraints into deterministic checks before
drafting: required and forbidden content, output-only boundaries, schema, section or
item counts, ordering, units, and minimum/maximum length. Apply the checks to the
exact final artifact after all synthesis and formatting. Count with the user's stated
method when supplied; otherwise record the method used. Any failure reopens only the
smallest responsible artifact or presentation seam for one bounded repair, followed
by complete rechecking. Never declare completion while a mechanically decidable
constraint fails, and never add execution commentary outside an output-only artifact.

## Causal failure routing

Map a failed criterion to the earliest false or unevidenced contract on its ancestry:

- missing or wrong outcome/constraint → intent resolution;
- missing mechanism, lifecycle state, actor, or failure mode → domain discovery;
- wrong grouping, authority isolation, or dependency → topology;
- wrong competence, owner, boundary, or output contract → charter;
- incorrect artifact content or scope-key reference → executing specialist;
- mismatched imports, conflict, or stale consumer → integration;
- invalid criterion, assurance method, independence, or verdict scope → verification;
- genuinely absent external fact or approval → evidence acquisition or explicit block.

Return stable exception IDs, failed criteria, evidence gaps, allowed repair surface,
and affected descendants to the owning seam. Never repair an upstream defect by
polishing final prose.

For nontrivial assurance, compile an executable method: population or frame, stable
item IDs, admissible evidence, exhaustive or sampling rule, independent
transformation/recomputation, tolerances, version/hash/diff scope, discrepancy classes,
exception owner, repair, rerun, and escalation. Include only fields relevant to the
claim; a named activity such as “sample” or “recompute” without a method is incomplete.
