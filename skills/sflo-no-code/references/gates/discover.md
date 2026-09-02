# Gate 1: Discover

**Owner:** Product manager  
**Input:** Exact user request  
**Output:** `SCOPE.md`

## Work

1. Identify the human problem and smallest useful product increment.
2. Declare whether external data is required.
3. When required, probe real endpoints or sources and record exact results. Assumptions or documentation alone do not verify availability.
4. List every product deliverable using an exact project-relative path.
5. Define prioritized features and specific, testable acceptance criteria.
6. Optionally record a timebox. Never weaken gate criteria to fit it.

## SCOPE.md template

```markdown
Artifact: SCOPE.md
Run: <run-slug>
Revision: <N>
Updated: <ISO-8601 timestamp>
Owner: <PM agent>
Status: PASS | BLOCKED
Inputs:
- user request

## Problem and user
<one concise paragraph>

## External data
- Required: yes | no
- Source: <URL, API, dataset, or none>
- Probe: <command or method>
- Result: <timestamped real result or reason none is needed>

## Deliverables
- `<exact/project-relative/path>` — <purpose>

## Features
1. Must: ...
2. Must: ...
3. Optional: ...

## Acceptance criteria
- [ ] AC1: <observable, testable condition>
- [ ] AC2: <observable, testable condition>

## Optional timebox
<duration or omitted>
```

## Pass check

- `SCOPE.md` exists with current run metadata.
- Problem, user, exact deliverables, features, and testable criteria are present.
- External data says `no` with rationale, or required sources have real probe evidence.

Missing item → `BLOCKED`. Do not start Build.
