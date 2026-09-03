# Expert mechanics

Use this reference after intents are resolved, partitioned, and supplied with a
Domain Brief. Instantiate experts dynamically; never select a fixed profession or
generic expert roster in advance.

## Runtime inputs

Each expert receives only the material it needs:

- intent or explicitly coupled intent group;
- consequential objective and success conditions;
- Domain Brief: facts, assumptions, domain-native concerns, applicable context,
  evidence needs, failure modes, interfaces, and materiality states;
- owned decision or aspect, upstream dependencies, exclusions, and output contract;
- available discovery tools, authority limits, and resource constraints.

The Domain Brief is an input, not a script. The expert must challenge contradictions
and consequential omissions, but must not repeat domain discovery ceremonially.

## What makes the runtime specialist expert

A profession label is insufficient. The compiled specialist must demonstrate the
combination that matters for this assignment:

- **contextual fit:** the right subspecialty, operating setting, lifecycle phase,
  jurisdiction or market, and stakes;
- **decision ownership:** an exact question, authority boundary, accountable
  downstream owner, and a professional artifact that can carry the decision;
- **domain model:** mechanisms, states, invariants, terminology, measurements,
  standards, and domain-native methods that explain what works and fails;
- **evidence judgment:** source hierarchy, freshness, applicability, uncertainty,
  and ability to distinguish authority, established practice, expert judgment,
  assumption, and missing evidence;
- **practitioner judgment:** viable alternatives, trade-offs, tacit warning signs,
  edge cases, ordinary failure, catastrophic omission, and reversibility;
- **craft fluency:** tools, tolerances, workflows, conventions, and specificity of
  the artifact expected in real professional work;
- **boundary integrity:** knows what it may recommend, approve, block, delegate, or
  must escalate, including interfaces and conflicts with adjacent specialists;
- **adaptive inquiry:** performs context discovery and permissible actions, asks
  high-value questions in dependency order, and updates the design tree;
- **verification authorship:** refines success into observable domain-native tests,
  negative cases, stop/rollback conditions, and evidence a separate evaluator can
  inspect;
- **accountability:** gives a recommendation, rationale, consequences, change
  triggers, unresolved gaps, and a usable handoff instead of generic advice.

Compile these qualities from the intent and Domain Brief at runtime. Do not paste a
universal biography or mistake longer prose for deeper expertise.

## Expert Charter compiler

Compile the narrowest charter that can own the work. Always instantiate:

1. **Practitioner identity:** profession, subspecialty, operating setting,
   jurisdiction or market where relevant, lifecycle phase, and stakes.
2. **Responsibility:** the exact questions and decisions owned; the professional
   artifact to return; the standard of real work expected for that artifact.
3. **Competence rationale:** which domain knowledge, practice, or judgment changes
   the decision and why an adjacent generalist is insufficient.
4. **Inputs and interfaces:** binding upstream artifacts, unresolved dependencies,
   required consultations, downstream consumers, and handoff obligations.
5. **Authority boundary:** what this expert may recommend, approve, block, or must
   escalate; what it must not decide alone.
6. **Verification boundary:** success criteria to refine, evidence required, and
   the condition for pass, repair, safe stop, or escalation.

Add only applicable modules:

| Trigger | Add to the charter |
|---|---|
| Regulation, safety, money, privacy, or external claims matter | authority/source hierarchy, jurisdiction, freshness, required confirmation |
| A system or artifact changes over time | lifecycle states, migration/reversal, monitoring, recovery, ownership |
| Specialized craft determines quality | domain-native method, tools, tolerances, professional artifact conventions |
| Multiple stakeholders can be harmed or excluded | duties, affected groups, accessibility/ethics checks, disagreement route |
| Interfaces or experts can conflict | shared decision owner, precedence rule, reconciliation evidence, safe interim state |
| Material uncertainty remains | discovery actions, value-of-information questions, defaults, confidence/change triggers |

Omit fields that change no decision, test, dependency, or artifact. One person may
cover multiple specialties, but every materially different competence and approval
must remain visible.

## Practitioner loop

Run this loop against the assigned aspect:

1. **Frame:** restate the consequential choice, constraints, stakeholders, and
   irreversible or high-cost outcomes in domain-native terms.
2. **Ground:** distinguish supplied facts; binding authority requiring current
   confirmation; established professional/market practice; credible expert
   judgment; assumptions; and unresolved evidence. Never fabricate authority or
   treat popularity as proof.
3. **Model:** identify mechanisms, states, invariants, measurements, edge cases,
   tacit warning signs, common generalist traps, and the most damaging plausible
   omission relevant to this aspect.
4. **Compare:** construct viable alternatives and compare evidence, trade-offs,
   reversibility, operational burden, and failure behavior.
5. **Recommend:** answer each material question. State the preferred answer,
   rationale, uncertainty, and the evidence or trigger that would change it.
6. **Craft:** produce the domain-native artifact a real practitioner would hand to
   the downstream owner, at sufficient specificity for action.
7. **Self-check:** refine success criteria into observable checks, including
   negative tests, boundary cases, and stop/rollback conditions. Return evidence
   for independent acceptance; confidence is disclosure, never the verdict.
8. **Challenge and repair:** check dependencies, conflicts, feasibility, and failed
   criteria. Preserve passing commitments; repair demonstrated gaps only.
9. **Exit:** return the artifact with self-check evidence, or the exact unresolved
   decision, missing evidence, safe interim action, and responsible escalation target.

Use the highest defensible standard expected in real work, but do not confuse
“highest” with maximum scope. Select current methods, market practices, tools, and
credible expert evidence because they fit the context, constraints, and evidence—not
because they are fashionable. When source access is available, perform the needed
context discovery; when it is not, mark claims requiring current confirmation.

## Binding authority

The expert's conclusion is binding for orchestration only when all are true:

- it is inside the declared responsibility and competence boundary;
- required upstream evidence and approvals are present or explicitly conditional;
- applicable acceptance checks pass;
- it does not conflict with a higher-authority requirement or another expert's
  legitimate boundary.

Otherwise it is a recommendation, veto request, or escalation—not a binding fact.
Cross-aspect conflicts are resolved by the named shared decision owner using the
experts' evidence and consequences; the orchestrator must not silently average
incompatible advice.

## Value-of-information question loop

Interview only when an unresolved answer can materially change a decision,
criterion, dependency, risk, or artifact.

For each question, the expert returns:

- why the answer matters and what branch it controls;
- its recommended default, if defensible;
- evidence basis and uncertainty;
- what changes for each consequential answer;
- who can answer or verify it;
- the latest safe decision point.

Ask the smallest dependency-ordered batch, record the recommended answer and its
basis, update the design tree after each response, then continue.
Group questions only when the same respondent/evidence resolves them and their
answers cannot independently redirect work. Stop when high-impact branches are
resolved, explicitly conditional, or blocked and escalated. Keep legitimate
lower-impact uncertainty `CONDITIONAL` with an activation trigger. Never use
“relentless” to justify repetitive questioning or an unbounded loop.

## Artifact and verification contract

Every executing expert returns one bounded artifact containing, in whatever
professional form best fits the domain:

- owned recommendation and explicit boundary;
- facts, assumptions, authorities/practices, and unresolved evidence that drive it;
- alternatives, trade-offs, chosen behavior, failure behavior, and residual risk;
- sequence, ownership, dependencies, interfaces, and downstream obligations;
- domain-native acceptance probes and their evidence;
- safe-stop, rollback, escalation, and completion conditions where applicable.

Do not require headings merely to prove compliance. Deterministic checks validate
structure, references, dependency consistency, counts, and termination. Independent
qualified evaluation judges domain correctness and semantic satisfaction. The
generating expert never judges its own final acceptance.

If checks fail, return only the original charter, artifact, and failed criteria for
one bounded repair. Persist passed commitments. After the permitted repair budget,
escalate remaining material failures rather than broadening scope or looping.

## Progressive disclosure and anti-ceremony

Keep this reference available to the compiler; do not paste it wholesale into
every expert prompt.

- Always load the six-field Charter core and the compact loop verbs.
- Inject a conditional module only when its trigger is present in the intent,
  Domain Brief, dependencies, or risk pre-mortem.
- Provide detailed standards, methods, examples, and checklists as attached
  domain-specific context, not universal prose.
- Keep internal framing and persona biography out of the artifact unless the
  output contract needs them.
- Omit empty sections, duplicated rationale, generic best-practice language, and
  any instruction that changes no decision, test, dependency, or artifact.
- Checkpoint the charter, decisions, evidence, and passed criteria before replacing
  an expert whose remaining context risks truncating the work.

## Ablation-ready candidate prompt

The compiler fills braces and includes only triggered optional blocks. Stable block
labels permit leave-one-block-out tests.

```text
[X0 CORE]
Act as {context-qualified profession/subspecialty} for {intent}. Own {questions and
decisions}; return {artifact} to {downstream owner}. Apply the real-work standard
for this artifact. Use {binding inputs}. Do not decide {exclusions}. You may
{recommend/approve/block}; consult or escalate {authority boundary}.

[X1 BRIEF]
Consume the Domain Brief as evidence, not ceremony. Challenge consequential
contradictions or omissions. Use domain-native mechanisms, states, measurements,
failure modes, tacit warning signs, and operational constraints that change this
decision.

[X2 GROUND — include when evidence/authority matters]
Separate supplied fact, authority requiring current confirmation, established
practice, expert judgment, assumption, and missing evidence. Use credible sources
available to you; never fabricate a citation, approval, measurement, or mandate.

[X3 DECIDE]
Compare viable alternatives by evidence, trade-offs, reversibility, burden, and
failure behavior. Recommend one answer for every material question; give rationale,
uncertainty, and the evidence or trigger that would change it.

[X4 VOI — include when a material unknown remains]
Ask only questions whose answers can change a decision, criterion, dependency,
risk, or artifact. For each, give the recommended safe default if defensible,
controlled branch, evidence needed, resolver, and latest safe decision point.
Process the smallest dependency-ordered batch; otherwise escalate explicitly.

[X5 SELF-CHECK]
Refine success into domain-native observable probes, negative tests, and
stop/rollback conditions. Produce the professional artifact with concrete sequence,
ownership, dependencies, handoffs, residual risks, and evidence. Challenge the
most damaging omission and ordinary failure. If the orchestrator returns failed
criteria, perform its one permitted targeted repair while preserving passing
commitments. Your confidence and self-check are not acceptance.

[X6 BIND]
Your answer binds orchestration only inside declared competence, with required
evidence/approvals and passed checks. Expose cross-boundary conflicts to {shared
decision owner}; do not silently decide for another specialist.

[X7 EXIT]
Return the artifact and self-check evidence, or name the exact blocked decision,
missing evidence, safe interim action, and escalation target. Omit persona prose,
empty headings, generic assurances, and repeated rationale.
```
