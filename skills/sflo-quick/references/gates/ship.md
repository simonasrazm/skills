# Gate 5: Ship Decision

**Agent:** Orchestrator (the coordinating agent)
**Input:** All gate artifacts
**Produces:** `SHIP-DECISION.md`

## SHIP-DECISION.md Template

```markdown
## Ship Decision: [Project Name]

**Date:** [YYYY-MM-DD]

### Pipeline Evidence
- SCOPE.md: exists, data verified
- BUILD-STATUS.md: build passes, real data
- QA-REPORT.md: grade [X], [N] issues resolved
- PM-VERIFY.md: all ACs met, approved

### Iterations
- Discovery: [N] rounds
- Dev↔QA cycles: [N] rounds
- PM verification: [N] rounds
- Total time: [X hours]

### Decision: SHIP / HOLD / KILL

### Deploy Target
[URL, platform, or "local only"]

### Override (if applicable)
[Human override reason, if pipeline was bypassed]
```

## Decision Criteria

**SHIP** - All gates passed with evidence. Product is useful.

**HOLD** - Gates passed but external blocker (deployment issue, dependency, timing).

**KILL** - After multiple failed cycles, product isn't viable. Document why and move on.
