# Gate 2: Build

**Owner:** Developer  
**Input:** Current `SCOPE.md`; current failure artifact on retries  
**Output:** Product deliverables and `BUILD-STATUS.md`

## Work

1. Read `SCOPE.md` directly and verify its revision against `RUN.md`.
2. On retry, read current `QA-REPORT.md` or `PM-VERIFY.md`; address every actionable item.
3. Build only the scoped increment at the declared paths.
4. Use real external data when scope requires it. Do not substitute mock/sample data.
5. Run the product, build checks, and project-relevant self-checks.
6. Confirm every declared deliverable exists and every acceptance criterion is addressed.

## BUILD-STATUS.md template

```markdown
Artifact: BUILD-STATUS.md
Run: <run-slug>
Revision: <N>
Updated: <ISO-8601 timestamp>
Owner: <developer agent>
Status: PASS | FAIL | BLOCKED
Inputs:
- SCOPE.md: revision <N>
- <QA-REPORT.md or PM-VERIFY.md>: revision <N, on retry>

## Build evidence
- Start/run command: `<command>`
- Result: <exit status and observed behavior>
- Build/check commands: `<commands and results>`
- External data: <source and observed record/result, or not required>

## Deliverable manifest
| Path from SCOPE.md | Exists | Evidence |
|---|---|---|
| `<path>` | yes/no | <check> |

## Acceptance-criteria coverage
| Criterion | Addressed | Evidence |
|---|---|---|
| AC1 | yes/no | <path/output> |

## Self-check
- [ ] Product starts and core journey runs.
- [ ] Build completes with zero errors.
- [ ] Error states are handled.
- [ ] Required real data loads.
- [ ] Every failure finding is addressed.
```

## Pass check

Require status `PASS`, zero build errors, a runnable core journey, complete deliverable manifest, current input revisions, and all self-checks marked. Otherwise remain in Build.

