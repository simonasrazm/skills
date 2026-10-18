---
name: retrospective
description: Use for retrospectives, cross-run lessons and missed instructions. Find supported issues and prioritized improvement options from actual work.
disable-model-invocation: true
---

# Retrospective

Find worthwhile improvements from actual work and preserve what works. Deliver findings and prioritized options; selection and implementation remain outside this skill.

## Steps

1. **Reconstruct the work.** Default to this conversation. Recover intent, corrections, messages, paired tool calls/results, artifacts and handoffs. Distinguish human direction from quoted or scheduled content, and observed execution from summaries. Use the instructions and conditions in effect during the work; historical instructions are evidence, not current authority. Recover relevant truncated records where available; bound findings to available evidence. Use existing history, logs, tests and later outcomes before requesting access or another run. Keep source locations and coverage gaps; keep private incidents and transcripts out of distributable artifacts.

2. **Discover across the work before ranking.** Inspect consequential stages, including successful ones, for decisions, checks, failures, retries and handoffs. Trace what permits progress, what should stop it and whether those conditions are enforced. Collect supported secondary findings as well as major ones.

   - **Navigation:** Hard-to-find knowledge, hidden dependencies and stale pointers; prefer existing documentation or a targeted pointer.
   - **Automated checks:** Preventable mistakes and fragile manual decisions; inspect tests, types, linting and domain validators through their normal entrypoint. Check what failure actually blocks and whether faulty and valid controls behave correctly.
   - **Review rules:** Missed issues and misplaced constraints; identify the existing owner for an added, clarified or retired rule. Keep correctness constraints reachable before implementation; review-only style rules can stay with reviewers.
   - **Steering instructions:** Bulky or misplaced instructions; inspect applicable `AGENTS.md`, `CLAUDE.md`, nested rules, imports and memory. Verify actual files, roles and loading before proposing executable checks or focused guidance.
   - **Tool economy:** Inspect initial attempts, payloads and retries for avoidable overhead. Successful recovery does not erase an avoidable initial failure; retain supported secondary waste while preserving necessary recovery. Measure savings or leave them unknown.
   - **No-ops:** Duplicate, conflicting or stale instructions; require evidence of what behavior would be lost before recommending removal.
   - **Information access:** Evidence that was unavailable when needed; recover existing records before proposing more access, logging or documentation.

   Also inspect the result's correctness, completeness, source fidelity, usability, accessibility, security and privacy where relevant. Check interruption, retry, recovery, handoff and later-use failures; for continuing work inspect trigger, owner, health and a later relevant boundary. Include human rescue, needless approvals, costs shifted to others and maintenance effort. Measure relevant human effort and maintenance cost from available evidence; distinguish measurements from estimates and state what remains unknown. A passing partial check does not establish the requested effect. Consolidate overlapping findings; do not invent issues to fill categories.

3. **Explain failures from evidence.** For missed instructions trace expectation → exposure → applicable trigger and prerequisites → responsible action → observed effect. Direct messages and returned instructions can establish exposure; installation alone cannot. Check conflicts, permission, context loss, runtime errors and counterevidence before alleging omission. A queued action is not completion; missing traces leave uncertainty.

   For instruction proposals, specify the trigger, responsible action and completion condition with valid exceptions. Distinguish a capability description from an obligation. Repair the actual failure: an unread reference needs a reachable pointer; an exposed but ignored rule needs a different explanation. Prefer one authoritative rule at its existing owner. For missing competence, describe an invocable capability: its trigger, work and demonstration of the missing competence. Distinguish a reusable capability from advice for one task. Separate reusable causes from project-specific fixes.

4. **Prioritize options.** Preserve required quality. Prioritize improvements by their expected impact on future work. Give trade-offs and justified no-change. Distinguish observation, causal hypothesis, proposed intervention and validated improvement. Resolve competing causes with available non-mutating checks; otherwise name the next discriminating observation. Effective recovery can justify no change.

5. **Present findings and options.** Apply [Present Clearly](../present-clearly/SKILL.md) to the whole user-facing output, including findings, recommendations and evidence limits. State each supported issue and causal chain once, with evidence, expected benefit, trade-offs and what to preserve. Retain distinct secondary findings proportionately. Separate defects, evidence gaps and optional opportunities; incomplete records alone do not justify more process. Suggest validation of the changed behavior through its normal path and applicable valid exceptions. Keep untested benefits unvalidated. Include concise evidence references, using an existing private work record for detail when available.
