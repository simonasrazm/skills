# Generic work-graph kernel

Use only for multiple consequential decisions, specialists, artifacts, evidence
regimes, or validation duties. Clear simple requests exit without visible graph
ceremony or unnecessary specialists.

## Typed runtime graph

Maintain stable, versioned `INTENT`, `CONCERN`, `DECISION`, `SPECIALIST`, `ARTIFACT`,
`ACTION`, `OPERATION`, `EVIDENCE`, `GATE`, `VERDICT`, and `EXCEPTION` nodes with `OWNS`,
`REQUIRES`, `RUNS`, `CHANGES`, `PRODUCES`, `MEASURES`, `IMPORTS`, `VALIDATES`, `CONFLICTS`, and
`INVALIDATES` edges. Every active
node has an owner, state, required inputs, output or terminal disposition, and local
exit condition. Keep one canonical ledger; expose bookkeeping only when operationally
or auditably useful.

Within an epoch, `REQUIRES` and `IMPORTS` form an acyclic artifact DAG; consultation
and conflict are not scheduling edges. Feedback creates a new epoch: increment the
affected version and reopen only causal descendants.

## Runtime type extension

Experts may introduce domain-native objects needed to model or execute their work.
First decompose the candidate across the kernel lifecycle and use a named subtype or
composition when this preserves meaning. For example, “test” commonly decomposes
into a specification or test code (`ARTIFACT`), execution (`OPERATION`), result
(`EVIDENCE`), acceptance condition (`GATE`), decision (`VERDICT`), and corrective
change (`ACTION`); one undifferentiated `TEST` node would hide those boundaries.

Admit a new primitive type only when it has irreducible identity and lifecycle;
distinct owner or authority; inputs, outputs, and dependency edges; failure,
rollback, acceptance, or invalidation behavior; and composition from existing types
would lose a decision-changing invariant. Define those semantics and affected
interfaces before use. The expert proposes the extension; orchestration compiles it
against the shared graph and resolves collisions before dispatch or integration.
Otherwise instantiate a domain-labeled kernel subtype rather than expanding the
schema. Type creation never grants competence, authority, evidence, or acceptance.

## Admission, split, and merge

Admit a concern only if it can change a decision, criterion, dependency, evidence,
risk, artifact, or escalation. Express it as `state/mechanism → invariant → failure
mode → affected decision → observable check`; run a domain-uniqueness pass and
disposition every candidate concern.

Split when failure, verdict, rollback, authority, evidence permission, competence,
artifact, or one-way dependency can vary independently; keep creator and validator
separate. Merge only when one owner, inseparable artifact, evidence/authority regime,
and verdict survive. Shared discovery does not imply shared execution. Stop splitting
when no such property or independently testable interface changes.

## Evidence identity and scope

Preserve supplied or acquired claims as immutable `EVIDENCE` nodes with stable IDs
and the smallest scope key: subject, component/actor, event/state, time window, source,
revision, and evidence status. Derived claims cite source IDs and may narrow but never
silently broaden or move scope. Use stable event/state IDs instead of relative aliases
when orderings could differ.

Before acceptance, compare derivations with cited nodes and claims sharing a scope
key. A changed subject, component, event, time, authority, polarity, quantity, or
maturity requires an explicit transformation or reconciliation; otherwise route the
contradiction to the earliest source, transformation, integration, or prose-reference
seam. Fluent prose cannot override the ledger.

## Closure before execution

Run to fixed point before dispatch and after change:

1. **Coverage:** every accepted clause is classified; every material concern reaches
   an owned decision/artifact and acceptance effect.
2. **Interface:** each import names a passing producer artifact/version; each export
   names consumers or a terminal sink; authority and uncertainty cross only declared
   interfaces.
3. **Acceptance:** every criterion names admissible evidence, maturity (`DESIGN`,
   `IMPLEMENTATION`, `OPERATION`, or `OUTCOME`), evaluator, and verdict.
4. **Invalidation:** typed causal changes make descendants `STALE` until regenerated
   or revalidated while unrelated passed nodes remain closed.

## Convergence and failure routing

- **Node:** contract → produce → deterministic check → semantic check when needed →
  `PASS`, `BLOCKED`, or one bounded repair.
- **Intent:** continue while required nodes become ready, interfaces stay open,
  conditions activate, or a verdict stales a descendant.
- **Orchestration:** integrate terminal intent artifacts and repeat affected subgraphs
  until all accepted intents are terminal and no required node is unresolved/stale.

Every iteration must close an obligation, change a version, spend repair reserve, or
record a blocker; unchanged state cannot repeat. Exhaustion yields `PARTIAL` or
`BLOCKED`, never `PASS`.

Route a failure to its earliest false or unevidenced ancestor: outcome/constraint →
intent; mechanism/state/actor/failure → domain; grouping/authority/dependency →
topology; competence/owner/boundary/contract → charter; artifact content/scope →
specialist; missing observation/protocol/operator/control → operation;
missing target-state transition/precondition/authority/read-back → action;
import/conflict/staleness → integration; criterion/method/independence/
verdict → verification; absent external fact/approval → acquisition or explicit block.
Return stable exception IDs, failed criteria, gaps, allowed repair surface, and
affected descendants. Never polish final prose to mask an upstream defect.

## Delivery and assurance gates

Before drafting, compile measurable delivery constraints into deterministic checks:
required/forbidden content, output-only boundary, schema, counts, order, units, and
length. Apply them to the exact final artifact after synthesis/formatting using the
user's counting method or a recorded default. Failure reopens the smallest responsible
artifact or presentation seam for one bounded repair followed by complete recheck;
mechanically failed output cannot complete, and output-only artifacts admit no extra
commentary.

For nontrivial assurance, specify applicable population/frame, stable item IDs,
admissible evidence, exhaustive or sampling rule, independent recomputation,
tolerances, version/hash/diff scope, discrepancy classes, exception owner, repair,
rerun, and escalation. Naming an activity without its method is insufficient.
