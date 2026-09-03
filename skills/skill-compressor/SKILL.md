---
name: skill-compressor
description: Reduce a skill's expected token load without losing routing or runtime behavior. Use for measured skill compression, debloating, progressive disclosure, or prompt-cost optimization; not for untested shortening.
---

# Skill Compressor

Optimize behavior per loaded token, not file length. A smaller candidate wins only
when it preserves or improves every required quality cell. Treat plausible wording
changes as hypotheses until execution evidence supports them.

## Compression loop

1. **Freeze:** preserve the exact baseline, test bank, graders, model settings, and
   decision thresholds before editing. Include real failures when available.
2. **Measure:** inventory description, always-loaded body, each routed reference,
   full surface, and expected loaded tokens. Use `scripts/measure_skill.py`; provide
   observed route frequencies when available.
3. **Map:** create a behavioral ledger: stable rule ID, decision changed, activation
   condition, owning file, dependent rules, positive case, and failure if lost.
   Separate catalog routing from post-load execution behavior.
4. **Hypothesize:** generate at least three candidates per seam: unchanged control,
   removal, and the shortest replacement that preserves the decision. Prefer one
   independent variable per comparison.
5. **Test:** run identical randomized trials on control and candidates. Use
   deterministic graders for exact invariants and independent blinded judgment only
   for semantic quality. Measure task-cell pass rate, catastrophes, routing, tokens,
   output size, calls, and executor-measured latency.
6. **Localize:** if a candidate fails, restore the changed seam or split it into
   smaller chunks and repeat from Hypothesize. If variants tie on every quality gate,
   retain the lower expected-load variant.
7. **Transfer:** run fresh held-out and compounded cases. Promote only after every
   required cell passes and no material NFR regresses. Otherwise keep the baseline
   and report the smallest failing seam.
8. **Apply:** update the source, validate it, and prove it is byte-identical to the
   accepted candidate. Rerun the bank only if application transformed the bytes;
   report baseline, candidate, and installed hashes plus measured deltas.

Read [evaluation protocol](references/evaluation-protocol.md) before designing the
test bank. Read [transformation mechanics](references/transformation-mechanics.md)
when classifying or rewriting seams.

## Optimization rules

- Optimize `catalog + always-loaded + routed-on-demand` expected cost. Moving text
  to a reference is not compression when that reference always loads.
- Preserve behavioral atoms, not necessarily their original sentences. A redundant,
  obsolete, default, contradictory, or harmful atom may be removed only by ablation.
- Test both activation and restraint: cases where guidance is needed, irrelevant,
  misleading, and accumulated across multiple turns or deliverables.
- Do not tune to evaluator nouns, fixtures, exact phrases, or one domain. Each retained
  mechanism must generalize to multiple archetypes or an explicit invariant.
- Do not accept aggregate wins that hide a failed task cell or catastrophe.
- Model-authored time estimates are not NFR evidence; use executor timestamps.
- Keep raw prompts, outputs, traces, grades, invalid runs, and protocol deviations.
- Stop when remaining candidates either fail quality gates or save less than the
  preregistered minimum practical token delta.
