---
name: s-dev
description: Implement or repair one coherent product change with behavior-first evidence, useful seams, and proportional architecture. Use for a scoped change or when another workflow delegates a mutation unit.
---

# S Dev

Own maintained-product mutation. Work from the accepted behavior, boundaries, current candidate, and relevant reviewer findings; hold the accepted destination.

For code, establish a meaningful failing behavior at the narrowest useful public boundary before the production change when the failure can be represented. Make the smallest coherent change that passes, then refactor only while behavior stays proven. When a rule is demonstrably repeated or already varies, place it behind one local seam that improves locality and leverage; avoid speculative layers and generic abstractions.

For non-code artifacts, establish the cheapest meaningful falsifier before settling the final change. Follow the medium's acceptance conditions rather than translating code rituals mechanically.

UI work follows the project's design system. If none exists, establish a proportional system of reusable tokens and components. Treat light/dark/system appearance, accessibility, responsive and complete states, logical layout, and longer-text tolerance as acceptance, not later polish.

Preserve project conventions and previously proven behavior. Return the candidate identity, changed paths, intended delta, and builder checks to the caller. Builder checks establish readiness; they are not independent acceptance. Standalone use creates no run-state artifact.

For repair, reproduce or validate the finding against its candidate, fix the smallest coherent cause, and issue a new candidate identity. Route unexplained failures to an evidence-first diagnostic capability, including active reproduction when justified. Return the candidate to the checker that owns the invalidated evidence.
