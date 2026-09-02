# Gate 3: Test

**Owner:** Fresh QA tester who did not build the product  
**Input:** Current `SCOPE.md`, `BUILD-STATUS.md`, and runnable product  
**Output:** `QA-REPORT.md`

Quality means useful to a human, not merely compiling.

## Mandatory tests

1. Run the product using the documented command.
2. Exercise the main user journey from start to finish.
3. Test every acceptance criterion separately with observed evidence.
4. Recheck every exact deliverable path.
5. When external data is required, use real current data and verify completeness/freshness relevant to scope.
6. Test relevant boundaries, unexpected input, error states, performance, crashes, hangs, and confusing behavior.
7. Perform the stranger test: could a new user understand and benefit from the product?

Do not edit product deliverables. Findings return to Build so role ownership and evidence remain clear.

## QA-REPORT.md template

```markdown
Artifact: QA-REPORT.md
Run: <run-slug>
Revision: <N>
Updated: <ISO-8601 timestamp>
Owner: <fresh QA agent>
Status: PASS | FAIL | BLOCKED
Inputs:
- SCOPE.md: revision <N>
- BUILD-STATUS.md: revision <N>

## Execution evidence
- Start/run command: `<command>`
- Environment: <relevant details>
- Evidence: <outputs, screenshots, logs, or exact reproduction steps>

## Results
| Test | Result | Evidence |
|---|---|---|
| Core journey | PASS/FAIL | ... |
| Acceptance criteria | PASS/FAIL | ... |
| Deliverable manifest | PASS/FAIL | ... |
| Real external data, when required | PASS/FAIL/N/A | ... |
| Edge cases | PASS/FAIL | ... |
| Performance | PASS/FAIL | ... |
| Error states | PASS/FAIL | ... |
| Stranger test | YES/NO | ... |

## Findings
1. CRITICAL | MAJOR | MINOR — <problem> — <evidence> — <required fix>

## Grade
A | B+ | B | C | D | F

## Verdict
PASS TO VERIFY | RETURN TO BUILD | BLOCKED
```

## Grading

- **A:** Every mandatory test passes, required real data works, no unresolved finding remains, UX is polished enough for scope, and value is clear.
- **B+:** Useful with minor unresolved issues.
- **B:** Works but needs polish.
- **C:** Mediocre, confusing, slow, or incomplete.
- **D:** Major breakage or weak usefulness.
- **F:** Product does not run, core journey fails, purpose is unclear, or required real data was replaced by mock/sample data.

## Pass check

Only grade **A** with `PASS TO VERIFY` advances. Any lower grade returns the report to Build. Increment Build→Test attempt; after attempt 10 fails, set `RUN.md` to `ESCALATED` and ask the human.

