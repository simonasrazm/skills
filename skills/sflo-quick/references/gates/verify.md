# Gate 4: PM Verification

**Agent:** Product Manager (same or different from Gate 1)
**Input:** QA-REPORT.md (grade A) + original SCOPE.md
**Produces:** `PM-VERIFY.md`

## What the PM Does

Compare what was built against what was scoped. Not re-testing - verifying spec match.

## PM-VERIFY.md Template

```markdown
## PM Verification: [Project Name]

### Acceptance Criteria Check
- [ ] AC1: MET / NOT MET - [evidence]
- [ ] AC2: MET / NOT MET - [evidence]
- [ ] AC3: MET / NOT MET - [evidence]

### Scope Alignment
- Original scope: [summary from SCOPE.md]
- What was built: [summary from BUILD-STATUS.md]
- Alignment: MATCHES / MINOR DEVIATIONS / OFF TRACK

### Deviations
- [Any scope creep, missing features, or unexpected additions]

### Grade: [A / B+ / B / C / D / F]

### Verdict: APPROVED (A) / NEEDS CHANGES (below A)

### If NEEDS CHANGES:
1. [Specific change needed, concise reasoning]
2. [Specific change needed, concise reasoning]
```

## Gate Check (Orchestrator verifies)

- [ ] PM-VERIFY.md exists
- [ ] Verdict is APPROVED
- [ ] All acceptance criteria marked MET

**If NEEDS CHANGES → BACK TO GATE 2 with PM's change list.**
