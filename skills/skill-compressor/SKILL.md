---
name: skill-compressor
description: Reduce a skill's expected token load without losing routing or runtime behavior. Use for measured skill compression, debloating, progressive disclosure, or prompt-cost optimization; not for untested shortening.
---

# Skill Compressor

Optimize behavior per loaded token, not file length. A smaller candidate wins only
when it preserves or improves every required quality cell. Treat plausible wording
changes as hypotheses until execution evidence supports them.

## Compression loop

1. **Freeze:** preserve the exact baseline, promotion bank, graders, settings,
   thresholds, staged evidence budget, and stop rules. Include real failures.
2. **Measure:** inventory description, always-loaded body, each routed reference,
   full surface, and expected loaded tokens. Use `scripts/measure_skill.py`; provide
   observed route frequencies when available.
3. **Map:** create a behavioral ledger: stable rule ID, decision changed, activation
   condition, owning file, dependent rules, positive case, and failure if lost.
   Separate catalog routing from post-load execution behavior.
4. **Hypothesize:** consider unchanged control, removal, and the shortest replacement
   per seam. Prefer one independent variable. Reject noncompetitive variants by
   inspection; generating hypotheses does not require executing them.
5. **Screen:** run deterministic checks, then one observation per live variant on the
   most discriminating known failure. Reuse a condition-identical control observation.
   One hard regression may reject; one clean screen cannot promote.
6. **Falsify:** before replication, challenge survivors on a different failure
   mechanism, archetype, or grader. Run another trial only when its result can change
   the decision. Localize failures by restoring or splitting the changed seam.
7. **Transfer:** replicate survivors on the frozen required cells, including fresh
   held-out and compounded cases. Promote only when every cell passes and no material
   NFR regresses. Otherwise keep the baseline and report the smallest failing seam.
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
