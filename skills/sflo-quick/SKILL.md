---
name: sflo-quick
description: Run a five-gate Markdown workflow for quick software development on small personal projects and simple problems where speed matters most. Use when the user says `SFLO-QUICK:` or directly asks to run `sflo-quick`.
---

# Core Pipeline

**Trigger:** User says `SFLO-QUICK:` or directly asks to run `sflo-quick`.

## Pipeline Overview

```mermaid
flowchart LR
    G1["Gate 1\nDISCOVER\n\nPM Agent\nSCOPE.md"] --> DEV_QA

    subgraph DEV_QA ["Inner Loop - max 10 rounds"]
        G2["Gate 2\nBUILD\n\nDev Agent\nBUILD-STATUS.md"] --> G3["Gate 3\nTEST\n\nQA Agent\nQA-REPORT.md"]
        G3 -- "grade < A" --> G2
    end

    DEV_QA -- "grade A" --> G4["Gate 4\nVERIFY\n\nPM Agent\nPM-VERIFY.md"]
    G4 -- "not A" --> DEV_QA
    G4 -- "A" --> G5["Gate 5\nSHIP\n\nOrchestrator\nSHIP-DECISION.md"]
```

**Two loops, not one:**

1. **Inner loop (Dev↔QA):** Dev builds, QA tests. If QA grade < A, back to Dev. Max 10 rounds.
2. **Outer loop (PM):** Once QA passes (A), PM verifies against spec. If PM doesn't grade A - back to the Dev↔QA loop with PM's deviation list.

## Gate Rules

1. **Gate 2 CANNOT start** without Gate 1's SCOPE.md existing and having verified data endpoints
2. **Gate 3 CANNOT start** without a successful build (zero errors)
3. **Gate 4 CANNOT start** without QA grade of A
4. **Gate 5 CANNOT start** without PM Verification verdict: APPROVED
5. **Each gate produces a file** - no file = gate not passed

Gate references:

- [Discover](references/gates/discovery.md)
- [Build](references/gates/build.md)
- [Test](references/gates/test.md)
- [Verify](references/gates/verify.md)
- [Ship](references/gates/ship.md)
- [Roles](references/roles.md)

## Fail Loops

- **QA fails (grade < A):** Loop back to Dev. Max 10 Dev↔QA cycles.
- **PM rejects (not A):** Loop back to Dev↔QA with PM's deviation list. The inner loop counter resets.
- **After 10 failed inner cycles:** Escalate to human. Something is fundamentally wrong.

## Orchestrator Responsibilities

The orchestrating agent MUST:

1. **Never skip gates** - even if "it looks fine"
2. **Verify artifact files exist** before proceeding
3. **Track iteration count** - post status after each gate
4. **Keep all evidence** in the project directory
5. **Reference predecessor artifacts** - don't summarize, point to files
6. **Each agent reads its gate doc** - no relying on the orchestrator's summary
7. **Artifacts are the truth** - if it's not in a file, it didn't happen
8. **Fresh agents for QA** - don't let the builder test their own work

## Status Format

After each gate, post:

```
Pipeline: [Project Name]

Gate 1 (Discover): DONE - SCOPE.md verified
Gate 2 (Build):    DONE - build passes
Gate 3 (Test):     IN PROGRESS - Round 2/10 (grade C, fixing issues)
Gate 4 (Verify):   WAITING
Gate 5 (Ship):     WAITING

Current: QA found 3 issues, Dev fixing
```

## Emergency Override

Only the human owner can override this pipeline. If they say "ship it anyway" - ship it. But log the override in SHIP-DECISION.md with reason.

No agent can self-override. No "it's good enough" shortcuts.

## Retrospective

After every project completes (ship or kill), write:

```markdown
## Retrospective: [Project]

Iterations: PM [N] → Dev [N] → QA [N] → Verify [N]
Total time: [X hours]
Final grade: [A]

What worked:
- [specific]

What broke:
- [specific] → [prevention]
```
