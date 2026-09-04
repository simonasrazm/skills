# Evaluation protocol

Use this reference when creating a compression benchmark.

## Freeze before generation

Record hashes, model/settings, corpus, promotion replicates, graders, thresholds,
randomization, timeout, and rerun policy. Freeze separate screening and promotion
samples, an evidence ceiling, and decision-changing escalation. Never selectively
replace failures; rerun infrastructure failures only under a symmetric rule.

## Preflight

Before generation, verify hashes, isolation, fixtures, oracles, graders, and telemetry
against a reference case and deliberate mutant. Harness failures are invalid; fix
symmetrically and rerun preflight.
Inspect effective instructions and traces; invalidate runs loading another variant.
Record the compressor model and target executor separately. Planning tests cannot
establish execution savings or target-skill non-regression.

## Evidence ladder

1. Check exact invariants and token eligibility deterministically.
2. Screen each variant once on the strongest historical failure; reuse a
   condition-identical control. Hard regression rejects; clean advances only.
3. Falsify survivors through a different failure mechanism, archetype, or grader.
4. Run more trials only when their outcome can change the decision.
5. Promotion requires the full bank: every distinct required failure mode plus fresh
   held-out and compounded cases. One clean observation never promotes.

## Corpus layers

- **Positive:** the removed instruction should activate and change the result.
- **Negative:** it is irrelevant and must not add work or prose.
- **Distractor:** its concrete examples or named tools are plausible but wrong.
- **Boundary:** permission, scope, format, output, or irreversible-risk constraints.
- **Compounded:** several decisions accumulate across turns, intents, or dependencies.
- **Held-out:** fresh domains and wording unavailable during candidate design.

Screen with the most discriminating case. Promotion covers each distinct failure mode
and at least three task archetypes, including unseen wording or archetype. Replicate
non-deterministic cells. Hide historical failure solutions from the executor.
Correlated checks are not independent trials.

## Grading

Run deterministic checks first: parseability, exact constraints, stable identifiers,
required/forbidden actions, tool calls, graph validity, and size limits. Semantic
judges receive anonymous artifacts, no variant descriptions, and position-swapped
order. Calibrate model judges against deterministic or human-labeled examples when
possible. A creator cannot provide final acceptance.

Predeclare per-cell pass thresholds and catastrophe conditions. Promotion requires
every candidate cell to pass, zero catastrophes, and control-relative non-regression.
Report effect sizes and raw denominators; statistical uncertainty remains explicit.

## Stop and account

Stop on hard regression, futility, sub-threshold savings, exhausted budget, or repeated
same-mechanism failure. Change mechanisms, not synonyms. Report actual and avoided
trials, calls, tokens, latency, invalid runs, missing telemetry, and escalation causes.
Budget exhaustion with missing required evidence is inconclusive; retain the baseline.

## NFR accounting

Report catalog, always-loaded, expected-route, and full-surface tokens separately.
Inventory routed Markdown outside `references/` too; legacy skills often name files
beside `SKILL.md`. The measurement script discovers existing linked or backticked
local Markdown paths as well as the conventional directory.
The script reports unknown expected cost without route data. Declare mandatory loads
with repeatable `--required` paths. `--routes` lists complete, mutually exclusive load
scenarios, including nested files; probabilities must sum to one. Use the same
validated `--encoding` for both variants; `--require-tokenizer` forbids fallback
estimates. Character estimates support screening, not small token-win claims.
For executions report input/output tokens, successful and failed calls, median and
p95 executor latency, artifact bytes/words, and route frequencies. Cache effects and
post-hoc grading cost stay separate from workflow cost.
