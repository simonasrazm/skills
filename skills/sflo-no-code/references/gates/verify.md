# Gate 4: Verify

**Owner:** Product manager distinct from builder and QA  
**Input:** Current `SCOPE.md`, `BUILD-STATUS.md`, and grade-A `QA-REPORT.md`  
**Output:** `PM-VERIFY.md`

Verify scope match; do not repeat QA or repair product files.

## Work

1. Confirm every input revision is current in `RUN.md`.
2. Compare each original acceptance criterion against current Build and QA evidence.
3. Compare exact scoped deliverables against the current manifest.
4. Identify missing work, scope creep, or unexpected additions.
5. Assign grade A only when every acceptance criterion is met and alignment matches.

## PM-VERIFY.md template

```markdown
Artifact: PM-VERIFY.md
Run: <run-slug>
Revision: <N>
Updated: <ISO-8601 timestamp>
Owner: <PM agent>
Status: PASS | FAIL | BLOCKED
Inputs:
- SCOPE.md: revision <N>
- BUILD-STATUS.md: revision <N>
- QA-REPORT.md: revision <N>

## Acceptance criteria
| Criterion | MET/NOT MET | Evidence |
|---|---|---|
| AC1 | ... | <direct artifact reference> |

## Scope alignment
- Original scope: <direct SCOPE.md reference>
- Current deliverables: <direct BUILD-STATUS.md reference>
- Alignment: MATCHES | MINOR DEVIATIONS | OFF TRACK

## Deviations
1. <missing, extra, or changed behavior and required correction>

## Grade
A | B+ | B | C | D | F

## Verdict
APPROVED | NEEDS CHANGES | BLOCKED
```

## Pass check

Require grade **A**, `APPROVED`, and every criterion `MET`. Otherwise return `PM-VERIFY.md` to Build, increment the PM verification cycle, reset Build→Test attempt to zero, and rerun Build→Test→Verify.

