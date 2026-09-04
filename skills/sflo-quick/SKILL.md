---
name: sflo-quick
description: Autonomously turn a small request into a verified, runnable result through a lightweight five-gate delivery loop. Use for trusted personal software, multi-iteration demos, scripts, SQL, data work, and other bounded builds when speed and useful quality matter. Triggered by `SFLO-QUICK:` or a direct request to run `sflo-quick`.
---

# SFLO Quick

Deliver the result. Keep the factory dark: expose concise outcomes, not routine process narration.

## Operating policy

- Resolve routine ambiguity with the smallest reasonable reversible assumption, record consequential assumptions in `FRAME.md`, and continue.
- Treat consequential, irreversible, or external actions as requiring explicit authority; preserve the best safe local result and name the exact blocker when authority is absent.
- Match rigor to the stated environment, reversibility, and consequence.
- Build the smallest usable end-to-end slice first and preserve the last proven slice before each repair.
- Choose for each criterion the cheapest direct proof capable of falsifying it.

## Run workspace

Create or resume `<project>/.sflo-quick/<scope-slug>/`. Keep five Markdown artifacts there. Each fact has one authoritative home; later artifacts point backward instead of copying detail.

## Five gates

1. **FRAME** — Freeze the outcome, boundaries, criteria, planned proofs, and work-product paths in `FRAME.md`. Read [FRAME](references/gates/frame.md).
2. **MAKE** — Build candidate `M1` and record candidate identity, artifact deltas, repair history, current candidate, and last proven candidate in `MAKE.md`. Read [MAKE](references/gates/make.md).
3. **CHECK** — Run objective proofs in clean processes and give judgment-dependent criteria a fresh non-builder evaluator; record provenance, results, and targeted falsification in `CHECK.md`. Read [CHECK](references/gates/check.md).
4. **ALIGN** — Compare that candidate with `FRAME.md` using CHECK evidence; record deviations, provenance, and verdict in `ALIGN.md`. Read [ALIGN](references/gates/align.md).
5. **DELIVER** — Select a candidate with passing CHECK evidence and an aligned ALIGN record; record the decision, recovery reference, usage, evidence references, limitations, and blockers in `DELIVER.md`. Read [DELIVER](references/gates/deliver.md).

## Repair loop

When CHECK or ALIGN finds a material failure:

1. Keep the last proven candidate available.
2. Fix the smallest coherent cause.
3. Record the next candidate in `MAKE.md` and increment its ID.
4. After a product change, re-run the affected proof plus the launch or core-use probe. After a probe-only correction, re-run the corrected proof.

Use at most three focused repair cycles by default. Finish earlier when all material criteria pass, a repair leaves the failing proof unchanged, or only disclosed non-material limitations remain. At the limit, select the best proven local result and make its limitations explicit.

## Completion contract

All five same-named Markdown artifacts agree on the selected candidate. Every FRAME criterion has independent CHECK evidence; ALIGN evaluates that candidate without unresolved material blockers; DELIVER names the decision and shortest usage path. Keep factory artifacts under `.sflo-quick`, work products at declared project paths, and lead the final response with the result and usage.

Read [Perspectives](references/roles.md) only when assigning or separating build and verification perspectives.
