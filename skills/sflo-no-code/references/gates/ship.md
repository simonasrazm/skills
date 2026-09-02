# Gate 5: Ship

**Owner:** Orchestrator  
**Input:** Complete current artifact chain, or an escalated run requiring a terminal decision  
**Output:** `SHIP-DECISION.md` and final `RUN.md`

## Work

1. Read every current artifact directly.
2. For a normal Ship path, verify run slugs, revisions, predecessor revisions, statuses, grade-A QA, grade-A PM approval, exact deliverable existence, and no stale evidence or unresolved finding.
3. For an escalated path, preserve failed and missing evidence exactly. Do not present an incomplete chain as passed.
4. Choose one terminal decision:
   - **SHIP:** every gate passed and product is useful, unless the human explicitly overrides named failures.
   - **HOLD:** an external blocker prevents release or the human pauses an escalated run.
   - **KILL:** repeated failure or invalid scope makes continuation unjustified.
5. If the human overrode a failed or blocked gate, quote or closely record their instruction, reason, and waived evidence. No agent may create an override or infer permission to ship.
6. Add a concise retrospective to the decision artifact.

## SHIP-DECISION.md template

```markdown
Artifact: SHIP-DECISION.md
Run: <run-slug>
Revision: <N>
Updated: <ISO-8601 timestamp>
Owner: <orchestrator>
Status: SHIP | HOLD | KILL
Inputs:
- SCOPE.md: revision <N>
- BUILD-STATUS.md: revision <N>
- QA-REPORT.md: revision <N>
- PM-VERIFY.md: revision <N>

## Evidence chain
- Scope and deliverables: <direct reference>
- Build and run proof: <direct reference>
- QA: <grade/status and direct reference, or missing with reason>
- PM verification: <grade/status and direct reference, or missing with reason>
- Deliverable recheck: <paths and result>

## Iterations
- Discovery revisions: <N>
- Build→Test attempts: <N>
- PM verification cycles: <N>

## Decision
SHIP | HOLD | KILL

## Target or blocker
<deployment/use target, external blocker, or kill rationale>

## Human override
None | <human instruction, reason, affected gate, and waived evidence>

## Retrospective
- Worked: ...
- Broke: ...
- Prevent next time: ...
```

## Finish

Update `RUN.md` to `COMPLETE`, record one terminal outcome (`SHIP`, `HOLD`, or `KILL`), retain any override in its separate Overrides section, record artifact revision, and set next action. Chat status may summarize the result, but never replaces `SHIP-DECISION.md`.
