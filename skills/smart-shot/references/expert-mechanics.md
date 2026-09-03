# Expert mechanics

Use after intents are resolved, partitioned, and supplied with a Domain Brief.
Instantiate specialists dynamically; never select a fixed or generic roster.

## Runtime contract

Give each specialist only its intent or valid group; objective and success conditions;
relevant Domain Brief facts, assumptions, concerns, evidence needs, failures,
interfaces, and materiality states; owned decision, dependencies, exclusions, output
contract; tools, authority, and resource limits. The Brief is evidence, not a script:
challenge consequential contradictions or omissions without repeating discovery.

Compile expertise from the assignment, not a biography. It must make these properties
operational:

- contextual fit: subspecialty, setting, lifecycle, jurisdiction/market, and stakes;
- exact decision ownership and a professional artifact usable downstream;
- domain mechanisms, states, invariants, terms, measurements, standards, methods,
  tools, tolerances, workflows, and conventions;
- evidence judgment over authority, freshness, applicability, uncertainty, practice,
  expert judgment, assumptions, and missing evidence;
- practitioner judgment over alternatives, trade-offs, reversibility, burden, warning
  signs, edge cases, ordinary failure, and catastrophic omission;
- boundaries over recommendation, approval, blocking, delegation, escalation,
  adjacent specialists, interfaces, and conflicts;
- adaptive, dependency-ordered inquiry that updates the design tree;
- observable domain-native probes, negative/boundary checks, rollback/stop conditions,
  recommendation rationale, consequences, change triggers, gaps, and handoff.

## Charter compiler

Compile the narrowest charter that owns the work. Always include:

1. **Identity:** profession, subspecialty, setting, jurisdiction/market when relevant,
   lifecycle, and stakes.
2. **Responsibility:** exact questions/decisions, returned professional artifact, and
   real-work standard.
3. **Competence rationale:** decision-changing knowledge or judgment and why an
   adjacent generalist is insufficient.
4. **Inputs/interfaces:** binding artifacts, unresolved dependencies, consultations,
   consumers, and handoffs.
5. **Authority boundary:** what it may recommend, approve, block, must escalate, or
   cannot decide alone.
6. **Verification boundary:** criteria, evidence, and pass, repair, safe-stop, and
   escalation conditions.

Add a module only when triggered:

| Trigger | Module |
|---|---|
| regulation, safety, money, privacy, external claims | authority hierarchy, jurisdiction, freshness, confirmation |
| evolving system/artifact | states, migration/reversal, monitoring, recovery, ownership |
| specialized craft | native method, tools, tolerances, artifact conventions |
| potentially harmed/excluded stakeholders | duties, affected groups, accessibility/ethics, disagreement route |
| expert/interface conflict | decision owner, precedence, reconciliation evidence, safe interim state |
| material uncertainty | discovery, value-of-information, defaults, confidence/change triggers |

Omit fields that change no decision, test, dependency, or artifact. One person may
cover specialties, but materially different competence and approvals remain visible.

## Practitioner loop

1. **Frame:** express the choice, constraints, stakeholders, and high-cost or
   irreversible outcomes in domain-native terms.
2. **Ground:** separate supplied facts, binding authority needing confirmation,
   established practice, credible judgment, assumptions, and unresolved evidence;
   never fabricate authority or treat popularity as proof.
3. **Model:** identify mechanisms, states, invariants, measurements, edges, warning
   signs, generalist traps, and the most damaging plausible omission.
4. **Compare:** evaluate viable alternatives by evidence, trade-offs, reversibility,
   burden, and failure behavior.
5. **Recommend:** answer each material question with preferred answer, rationale,
   uncertainty, and change evidence/trigger.
6. **Craft:** produce the actionable domain-native artifact.
7. **Self-check:** define observable probes, negative and boundary checks, stop or
   rollback conditions, and evidence for independent acceptance; confidence is not
   a verdict.
8. **Repair:** challenge dependencies, conflicts, feasibility, and failed criteria;
   preserve passing commitments and repair demonstrated gaps only.
9. **Exit:** return artifact plus evidence, or the exact unresolved decision, missing
   evidence, safe interim action, and escalation owner.

Use the highest defensible real-work standard that fits context; highest does not mean
maximum scope. When source access is unavailable, mark claims needing confirmation.

## Authority and inquiry

An expert conclusion binds orchestration only inside declared responsibility and
competence, with required evidence and approvals, passed checks, and no conflict with
higher authority or another legitimate boundary. Otherwise it is a recommendation,
veto request, or escalation. The named shared decision owner resolves cross-aspect
conflicts from evidence and consequences; orchestration cannot average them.

Ask only when the answer can change a decision, criterion, dependency, risk, or
artifact. For each question give the controlled branch, recommended defensible
default, evidence/uncertainty, consequential alternatives, resolver, and latest safe
point. Ask the smallest dependency-ordered batch; group only when one respondent or
evidence source resolves answers that cannot redirect work independently. Stop when
high-impact branches are resolved, conditional, or blocked; retain lower-impact
uncertainty as `CONDITIONAL(trigger)`.

## Artifact, acceptance, and disclosure

Return one bounded professional artifact containing owned recommendation and boundary;
driving facts, assumptions, authorities/practices, and evidence gaps; alternatives,
trade-offs, chosen and failure behavior, residual risk; sequence, ownership,
dependencies, interfaces, handoffs; native probes and evidence; applicable safe-stop,
rollback, escalation, and completion conditions. Headings are optional.

Deterministic checks cover structure, references, dependency consistency, counts, and
termination; independent qualified evaluation covers domain correctness and semantic
satisfaction. The creator cannot judge final acceptance. On failure, return the
original charter, artifact, and failed criteria for one bounded repair that preserves
passing commitments; then escalate remaining material failures.

## Compiler prompt blocks

Fill braces and include only triggered blocks; stable labels support ablation.

```text
[X0 CORE] Act as {qualified specialty/context} for {intent}. Own {decisions}; return
{artifact} to {consumer} at its real-work standard. Use {inputs}; exclude {limits}.
You may {authority}; consult/escalate {boundary}.

[X1 BRIEF] Treat the Domain Brief as evidence. Challenge consequential contradictions
or omissions; apply native mechanisms, states, measures, failures, warnings, and
constraints that change the decision.

[X2 GROUND — evidence/authority trigger] Separate fact, authority needing current
confirmation, established practice, judgment, assumption, and missing evidence.
Never fabricate citations, approvals, measurements, or mandates.

[X3 DECIDE] Compare viable alternatives by evidence, trade-offs, reversibility,
burden, and failure. Answer every material question with rationale, uncertainty, and
the evidence or trigger that changes it.

[X4 VOI — material unknown trigger] Ask only decision-changing questions. State the
safe default, controlled branch, evidence, resolver, and latest safe point; use the
smallest dependency-ordered batch or escalate.

[X5 SELF-CHECK] Define native probes, negative/boundary tests, stop/rollback conditions,
sequence, ownership, dependencies, handoffs, risks, and evidence. Challenge damaging
omission and ordinary failure. One returned repair may change failed criteria only;
self-check and confidence are not acceptance.

[X6 BIND] Bind only inside competence with required evidence/approvals and passed
checks. Expose boundary conflicts to {decision owner}; do not decide for another role.

[X7 EXIT] Return artifact plus evidence, or blocked decision, missing evidence, safe
interim action, and escalation target. Omit biography, empty headings, assurances,
and repeated rationale.
```

Keep this reference available to the compiler; do not paste it wholesale into every
prompt. Always load the six-field core and compact loop, add triggered modules only,
attach detailed standards as domain context, and checkpoint charter, decisions,
evidence, and passed criteria before replacing a context-limited expert.
