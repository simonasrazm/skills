---
name: s-dev
description: Implement or repair one coherent product change with behavior-first evidence, useful seams, and proportional architecture. Use for a scoped change or when another workflow delegates a mutation unit.
---

# S Dev

Own maintained-product mutation. Work from the accepted behavior, boundaries, current candidate, and relevant reviewer findings; hold the accepted destination.

Load [data-quality guidance](../sflo-waydriver/references/data-quality.md) when data quality is an objective or acceptance criterion. Carry the relevant quality rules and evidence into implementation and builder checks.

When implementation changes domain concepts, language, relationships or rules, apply [domain modeling](../s-waydriver/references/domain-modeling.md) and carry resolved meanings into behavior checks.

Build in vertical slices. For code, repeat this cycle:

1. Add one behavior test at a public seam and run it to establish the failure.
2. Implement that behavior through its required layers and run the check to establish the pass.
3. Use that working slice to choose the next behavior test.

Pair each edit with its check in one tool invocation when sequential execution is supported; inspect the result before the next cycle.

When a failure cannot be represented in an executable test, establish the corresponding observable falsifier. Refactor only while established behavior stays proven. When a rule is demonstrably repeated or already varies, place it behind one local seam that improves locality and leverage; avoid speculative layers and generic abstractions.

For non-code artifacts, establish the cheapest meaningful falsifier before settling the final change. Follow the medium's acceptance conditions rather than translating code rituals mechanically.

UI work follows the project's design system. If none exists, establish a proportional system of reusable tokens and components. Treat light/dark/system appearance, accessibility, responsive and complete states, logical layout, and longer-text tolerance as acceptance, not later polish.

Preserve project conventions and previously proven behavior. Return the candidate identity, changed paths, intended delta, and builder checks to the caller. Builder checks establish readiness; they are not independent acceptance. Standalone use creates no run-state artifact.

For repair, reproduce or validate the finding against its candidate, fix the smallest coherent cause, and issue a new candidate identity. Route unexplained failures to an evidence-first diagnostic capability, including active reproduction when justified. Return the candidate to the checker that owns the invalidated evidence.
