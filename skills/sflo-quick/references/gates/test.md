# Gate 3: QA Testing

**Agent:** QA Tester
**Input:** Testable implementation from Gate 2
**Produces:** `QA-REPORT.md` with grade

## Core Principle

**Quality means "useful to a human", not "code compiles".**

Every test MUST use REAL production data, not samples.

## Mandatory Tests

### 1. Real Data Test

- Does the product use REAL data, not mock/sample?
- Is the data complete and current?

### 2. Core Journey Test

- Can a new user accomplish the main task from SCOPE.md?
- Is it obvious what to do and how to do it?

### 3. Acceptance Criteria Test

- Test each AC from SCOPE.md individually
- Evidence required for each (output, screenshot, log - whatever applies)

### 4. Edge Cases

- Test boundary conditions relevant to the product type
- Unexpected input handled gracefully?
- Error states produce clear feedback?

### 5. Performance

- Core operations respond within acceptable time?
- No hanging/freezing/crashes?

## QA-REPORT.md Template

```markdown
## QA Report: [Project Name]

**Date:** [YYYY-MM-DD]
**Tester:** [Agent name]

### Data Verification
- Records loaded: [N] from [source]
- Data freshness: [current/stale]

### Test Results
| Test | Result | Notes |
|------|--------|-------|
| Real data loads | PASS/FAIL | |
| Core journey works | PASS/FAIL | |
| Acceptance criteria | PASS/FAIL | Tested each AC from SCOPE.md |
| Edge cases | PASS/FAIL | |
| Performance | PASS/FAIL | |
| Error states | PASS/FAIL | |

### Issues Found
1. [CRITICAL/MAJOR/MINOR] - [description] → [suggested fix]
2. ...

### Grade: [A / B+ / B / C / D / F]

### Stranger Test
Would a random person find this useful? [Yes/No/Maybe - why]
```

## Grading Scale

| Grade | Meaning | Criteria |
|-------|---------|----------|
| **A** | Ship it | Real data works, UX polished, clear value |
| **B+** | Almost | Minor issues, still useful |
| **B** | Decent | Works but needs polish |
| **C** | Mediocre | Works but ugly/confusing/slow |
| **D** | Broken | Major issues, not useful |
| **F** | Fail | Doesn't work or no real data |

## Minimum to proceed to Gate 4: A

## Auto-Fail Triggers

These automatically score F regardless of other results:

- Mock/sample data instead of real data
- Product does not start or run
- Purpose is unclear ("what is this for?")
- Core use case from SCOPE.md does not work

## Gate Check (Orchestrator verifies)

- [ ] QA-REPORT.md exists
- [ ] Grade is A
- [ ] No auto-fail triggers present

**If grade < A → BACK TO GATE 2 with QA findings. Max 10 cycles, then escalate.**

## QA Agent Rules

1. **REPORT issues** - don't fix them directly
2. **Evidence required** - screenshots, logs, exact repro steps
3. **Be honest** - "it compiles" ≠ "it works"
4. **Priority order** - report critical before nitpicking
