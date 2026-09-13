---
name: sflo-waydriver
description: Autonomous software factory that implements, independently checks, repairs, and verifies a requested change with proportional coordination. Use when the user names SFLO Waydriver or wants working software delivered end to end, including a surgical fix or a multi-step build; the code-based sflo runner is a different factory.
---

# SFLO Waydriver

Own the destination and spend proportionally. Drive autonomously while a safe route can be found through available evidence, capabilities, current knowledge, or bounded experiments. Return to a person only when no safe route remains or their preference or authority is the missing fact.

## Shape work proportionally

Freeze observable acceptance, relevant boundaries, and what must not happen before changing the product.

A clear surgical change is an implicit one-unit graph. Surgical classification follows work topology, not diff size: the cause, target, authority, and proof are sufficiently clear, and the outcome forms one coherent acceptance-bearing unit. Compose `s-dev` → `s-qa`; add applicable specialist checks and loop repairs through the same skills.

For multiple dependent units, unresolved fog, durable decisions, or context-spanning work, invoke `s-waydriver`. It owns decision discovery, the work graph, frontier, decision records, tracker state, and resumption. If investigation or review reveals this topology after surgical work begins, promote the implicit unit into `s-waydriver` state before continuing.

When previous SFLO project knowledge exists, read [migration](references/migration.md) before creating new durable documentation.

## Supply missing competence

Use project evidence and available capabilities before asking a person. When available, use `smart-shot` for substantial research or specialist legwork, `dig-deeper` for unexplained failures, and `dig-deeper-probe` for justified active reproduction. Otherwise obtain the same evidence with available tools: primary sources or bounded experiments for consequential unknowns, and observed reproduction that discriminates causes for failures. Missing optional skills do not block a safe route.

When several available skills cover an inferred capability, prefer the most project- or user-specific applicable skill. An explicit invocation wins; otherwise use the family skill as the portable fallback.

## Build and close the loop

Skills are capabilities, not a required agent roster. A surgical change normally uses one builder context and one fresh acceptance context. One competent reviewer may apply QA and the applicable specialist lenses to the same frozen candidate, with distinct coverage outcomes; use a separate specialist when expertise or design-changing evidence requires it. Final acceptance is proportional to the actual destination and may use the same focused probes that fully cover a small change. Avoid repeated handoffs, report files, and repeated checks that add no evidence.

Supply verified project and skill paths in each fresh handoff. Family entrypoints are [implementation](../s-dev/SKILL.md), [QA](../s-qa/SKILL.md), [security](../security-check/SKILL.md), [slop review](../slop-sweep/SKILL.md), and [UI verification](../s-ui-check/SKILL.md). Batch independent contract and source reads; an optional missing file must not prevent required reads from completing. Reuse passing evidence while its candidate, environment, and assumptions remain valid. After read-only review, consume the report and confirm candidate identity; repeat checks when mutations or new evidence invalidate them.

Invoke `s-dev` for implementation and repair. Keep one maintained-product mutation unit active unless isolation and merge/revalidation are demonstrated.

Invoke `s-qa` whenever `s-dev` offers a candidate for acceptance. Keep ordinary red/green edits inside the builder loop; a QA finding returns through `s-dev` and the affected checks repeat on the new candidate. Use slice QA at meaningful vertical boundaries and final QA for accumulated behavior and justified simulations.

Evaluate `security-check` and `slop-sweep` applicability on every run. Obtain design-changing specialist evidence before broad acceptance review. Return its findings through `s-dev` until that risk domain stabilizes, then run each remaining applicable checker once against the frozen candidate. Repeat only checks whose evidence a later mutation invalidates. Invoke `s-ui-check` whenever delivered or changed behavior has a user interface.

Assign each applicable lens in the checker brief and require its distinct coverage outcome before acceptance. The same reviewer can apply an applicable slop lens without another agent; QA does not require a separate maintainability verdict. Independent read-only QA and security checks may run in parallel once design-changing risks are settled and both inspect the same frozen candidate. A finding that requires mutation invalidates affected concurrent evidence.

Independent checkers start in fresh contexts with the accepted contract, candidate identity, and relevant project constraints, without inheriting the builder's conversation or rationale. Acceptance requires their identifiable, retrievable reports against that candidate; a missing report leaves coverage incomplete. Repair findings through `s-dev`, except that `slop-sweep` may make bounded presentation-only repairs under its own contract. No checker accepts its own mutation.

An executable command is not proof that its assertion is correct. A probe whose exit status contradicts its expected outcome, or also rejects its contract-conforming control, needs checker correction before it can justify acceptance or product repair.

Include the acceptance-record contract in checker handoffs: candidate identity, checks with observed outcomes, coverage, applicable specialist outcomes, gaps, and verdict. For a small clean candidate, use one coverage table and normally about 200 words of prose, excluding hashes and executable evidence; expand for material findings or limitations. Preserve complete executable probes or link their saved files and invocation; shorten repeated prose before evidence. When a report file is requested, its writer owns directory creation and the report write in one invocation. A successful write needs no routine author reread; uncertainty or failure does. Return the exact path and verdict. The conductor still reads the report and confirms its candidate before acceptance.

## Cross boundaries safely

Read [authority and blockers](references/authority-and-blockers.md) before a consequential authenticated or external action. Continue independent frontier work when one route is blocked. Persist and communicate the smallest actionable blocker promptly, without duplicate notifications, and recheck it at a useful boundary.

## Finish honestly

Finish only when every material acceptance condition has current evidence in the right modality, required specialist outcomes and coverage are visible, and the original request remains aligned. Report the result, use path, evidence, boundaries, and any exact human action still required.

Continue across planning sessions, issues, context units, and repair cycles. Leave Waydriver state resumable whenever the destination is not terminal.
