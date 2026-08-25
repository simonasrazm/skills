# Gate 1: PM Discovery

**Agent:** Product Manager
**Produces:** `SCOPE.md`

## What the PM Does

1. **Discover data sources** - find APIs, datasets, assess availability
2. **Verify endpoints work** - actual curl/fetch, not assumptions
3. **Define scope** - what can we build with available data?
4. **Set acceptance criteria** - specific, testable conditions

## SCOPE.md Template

```markdown
## Data Sources
- Endpoint: [URL] - Verified (tested with curl, returned [N] records)
- Endpoint: [URL] - Verified

## What We're Building
[One paragraph - what problem this solves for a real human]

## Features
1. [Feature description and details] ...
2. [Feature description and details] ...

## Acceptance Criteria
- [ ] AC1: [specific, testable]
- [ ] AC2: [specific, testable]
- [ ] AC3: [specific, testable]
```

## Gate Check (Orchestrator verifies)

- [ ] SCOPE.md exists
- [ ] At least 1 data endpoint verified with real curl output
- [ ] Acceptance criteria are specific and testable

**If anything missing → BLOCKED. Do not proceed to Gate 2.**
