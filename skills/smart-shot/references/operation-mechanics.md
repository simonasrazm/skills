# Empirical operation mechanics

Use an empirical operation when fulfilling or validating an accepted intent requires
a new observation, not merely more expert judgment. It differs from an `ACTION`: an
operation reduces uncertainty; an action changes the target state. Examples include inspection,
measurement, paired benchmarking, diagnostic probing, experimentation, simulation,
prototyping, representative-task trials, and controlled real-world execution. These
are forms discovered at runtime, not a required catalog.

## Admission and ownership

Admit an `OPERATION` only when all are true:

1. an accepted criterion or decision has a named evidence gap;
2. existing admissible evidence cannot close it;
3. an observable result could change the verdict, ranking, condition, confidence,
   risk, or next action;
4. the operation is authorized, feasible, and proportionate to its decision value;
5. its subject, result, and failure remain distinguishable from expert judgment.

Do not substitute advice for a requested demonstration or evidence-based comparison:
run the operation, narrow the claim, or expose the blocker. Do not run an operation
whose possible results leave the decision unchanged.

The owning specialist states the evidence gap and interpretation rules. Assign
design, operation, evidence validation, and decision ownership separately whenever
competence, authority, conflict, acceptance independence, or rollback differs. An
operation produces evidence; only the owning decision and its validator can turn
that evidence into an accepted conclusion.

Split operations when subject/version, authority, operator competence, control,
risk/rollback, evidence maturity, or verdict can vary independently. Merge only when
one protocol, population, authority regime, evidence contract, and failure behavior
survive.

## Operation contract

Compile only fields that can affect validity, safety, or interpretation:

- question, owning criterion/decision, hypothesis, result branches including
  inconclusive, and downstream consumers;
- subject/population, stable identifiers, version/configuration, environment, scope,
  and invalidating changes;
- procedure, operator, tools, permissions, dependencies, instrumentation, comparator
  or control, sampling/repeats, and order or blinding when material;
- evidence, units, provenance, maturity, integrity checks, thresholds, and the exact
  decision update for each result branch;
- maximum downside, exposure/resource cap, stop condition, rollback/latest safe
  point, retention, handoff, and independent acceptance.

For relative claims such as “which is better,” first resolve better for whom, for
which job and inputs, under which versions and constraints, across which scoring
dimensions or unresolved tradeoffs, and what constitutes superiority or a severe
failure. Run equivalent representative cases. Reputation, documentation, and expert
opinion may select candidates or criteria; they do not replace observed comparative
performance when that is the requested basis.

## Evidence-production loop

`Gap → design smallest discriminating operation → authorize → run exact protocol →
validate evidence → update owning decision → invalidate affected descendants`

Repeat only while another operation has positive decision value. Every pass must
create inspectable evidence, close an obligation, change a decision/version, or
record an exact blocker. Preserve negative and inconclusive results. Stop a larger
operation when a cheaper safe operation rejects its enabling mechanism. Distinguish
an implemented procedure from an executed operation, and an executed operation from
a demonstrated outcome. Route target-state work through action mechanics instead.
