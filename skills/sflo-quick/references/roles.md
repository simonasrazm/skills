# Agent Roles

## Orchestrator (Team Lead)

The agent running the pipeline. Usually the main/primary agent in a conversation.

**Responsibilities:**

- Own the project end-to-end
- Spawn specialist agents for each gate
- Verify gate artifacts before proceeding
- Track iteration count and post status
- Escalate after 10 failed cycles

**Does NOT:** Write code, test features, or verify specs --- delegates to specialists.

## Product Manager (PM)

Runs Gate 1 (Discovery) and Gate 4 (Verification).

**Responsibilities:**

- Find and verify data sources
- Define scope and acceptance criteria
- Verify built product matches spec

**Selection:** Use a PM-flavored agent if available. Otherwise, any capable agent with explicit PM instructions.

## Developer

Runs Gate 2 (Build).

**Responsibilities:**

- Implement requirements from SCOPE.md using vertical slices
- Connect to real data sources
- Run self-checks before handoff
- Fix issues from QA feedback loops

**Selection:** Use a coding agent (Codex, Claude Code, etc.) with access to the project directory.

## QA Tester

Runs Gate 3 (Test).

**Responsibilities:**

- Test with real data, not mocks
- Grade the product honestly
- Report bugs to the developer
- Provide evidence for every finding

**Selection:** Use any capable agent. QA agents should NOT be the same instance that built the feature
