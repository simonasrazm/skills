# Evaluation protocol

Use this reference when creating a compression benchmark.

## Freeze before generation

Record baseline and candidate hashes; model and reasoning settings; prompt corpus;
replicates; graders; thresholds; randomization; executor timeout; and rerun policy.
Never replace a failed run selectively. Infrastructure failures may be rerun only
under a recorded, condition-symmetric rule.

## Corpus layers

- **Positive:** the removed instruction should activate and change the result.
- **Negative:** it is irrelevant and must not add work or prose.
- **Distractor:** its concrete examples or named tools are plausible but wrong.
- **Boundary:** permission, scope, format, output, or irreversible-risk constraints.
- **Compounded:** several decisions accumulate across turns, intents, or dependencies.
- **Held-out:** fresh domains and wording unavailable during candidate design.

Use at least two task archetypes for a local seam and three for a promotion claim.
Replicate non-deterministic cells. Add known historical failures without revealing
their expected solution to the executor.

## Grading

Run deterministic checks first: parseability, exact constraints, stable identifiers,
required/forbidden actions, tool calls, graph validity, and size limits. Semantic
judges receive anonymous artifacts, no variant descriptions, and position-swapped
order. Calibrate model judges against deterministic or human-labeled examples when
possible. A creator cannot provide final acceptance.

Predeclare per-cell pass thresholds and catastrophe conditions. Promotion requires
every candidate cell to pass, zero catastrophes, and control-relative non-regression.
Report effect sizes and raw denominators; statistical uncertainty remains explicit.

## NFR accounting

Report catalog, always-loaded, expected-route, and full-surface tokens separately.
Inventory routed Markdown outside `references/` too; legacy skills often name files
beside `SKILL.md`. The measurement script discovers existing linked or backticked
local Markdown paths as well as the conventional directory.
For executions report input/output tokens, successful and failed calls, median and
p95 executor latency, artifact bytes/words, and route frequencies. Cache effects and
post-hoc grading cost stay separate from workflow cost.
