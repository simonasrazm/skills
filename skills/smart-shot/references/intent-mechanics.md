# Intent mechanics

## Resolve clauses into an intent graph

Classify each consequential clause as one of:

- **end intent:** a user-valued state change;
- **instrumental intent:** an outcome required to reach an end intent;
- **validation intent:** independent evidence or approval about another result;
- **requirement or constraint:** a condition on an intent;
- **deliverable component:** part of an output, not a separate outcome;
- **context or uncertainty:** supplied state or a gap needing resolution.

Only end, instrumental, and validation intents receive execution loops. Attach
requirements and deliverable components to their owning intent instead of
inflating them into experts or workstreams.

For each intent record: beneficiary, desired state, consequential decision,
decision owner, output contract, acceptance checks, evidence regime, deadline or
reversibility, failure envelope, and escalation condition. Preserve a global
ledger of verbatim constraints, facts, assumptions, sources, and unresolved gaps.

Use causal questioning only while it changes this graph. Do not mechanically run
five whys after the objective is already evidenced; do not invent hidden motives.

## Choose the coupling mode

An intent gets an isolated commitment and validation run when any applies:

- it creates while another audits, approves, challenges, or evaluates;
- success criteria, objectives, or legitimate alternatives conflict;
- authority, duty holder, evidence permission, or epistemic regime differs;
- confidentiality, safety, security, or protected-context boundaries differ;
- it owns a separate irreversible decision, rollback, or explicitly independent output;
- it can fail independently and does not share an inseparable decision or artifact;
- it depends one-way on another intent.

One-way dependency means sequence, not grouping. Pass only the validated upstream
artifact, stable identifiers, declared uncertainty, and allowed interface.

If no isolation rule fires, share discovery only when it materially reduces
duplicate investigation and at least one coupling fact holds:

- the intents inform the same consequential decision;
- one artifact cannot pass acceptance unless both intents pass;
- the intents have a genuinely bidirectional dependency.

The shared pass must preserve each intent's authority, permitted evidence,
acceptance, and failure boundary. If it cannot, isolate.

Choose the least-coupled safe runtime mode:

1. **Isolated:** separate discovery and execution when evidence access, safety,
   confidentiality, adversarial independence, or epistemic regime differs.
2. **Hybrid:** share a discovery pass and source register, then run separate intent
   commitments, artifacts, validators, and repair states. This is the default for
   related consequential intents.
3. **Fully grouped:** share execution only when there is one decision owner, one
   inseparable artifact, one evidence/authority regime, and one acceptance verdict;
   all intents must fail or pass together. If any of those tests fails, use hybrid.

The intent compiler alone sets intent cardinality. Domain discovery may propose
concerns, competencies, or work packages, but cannot promote them into new user
intents without re-running this classification. Split a group immediately if later
evidence reveals an isolation condition.

## Execute and converge per intent

For each dependency-ready intent:

1. compile its contract and relevant Domain Brief;
2. obtain the owned professional artifact from the responsible specialist(s);
3. run its acceptance ledger independently;
4. preserve passed commitments and repair failed criteria once;
5. mark `PASS`, `PARTIAL`, or `BLOCKED`, with evidence.

Run independent, dependency-ready intents concurrently within the active-agent
limit. Maintain a contradiction ledger across intent artifacts. Integrate only
after prerequisite intents pass or explicitly expose their uncertainty.

Resolve factual conflicts by the applicable evidence hierarchy; objective
conflicts by the named decision owner; interface conflicts by reopening affected
contracts; authority conflicts by escalation. Integration cannot invent a domain
commitment or convert uncertainty into agreement.

For every irreversible or dependency-releasing gate record: stable ID, owned
decision, accountable owner, required evidence and upstream artifact versions,
latest safe point, pass condition, failure action, restart condition, and downstream
consumers. A downstream artifact must reference the stable IDs it actually imports.

When an accepted fact, permission, assumption, scope, or artifact changes, run an
impact-propagation check across dependent artifacts, decisions, cost, schedule,
risk, and acceptance evidence. Version affected outputs and re-run their gates;
never treat file replacement alone as completed propagation.
