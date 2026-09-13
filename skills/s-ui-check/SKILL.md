---
name: s-ui-check
description: Independently verify a rendered web, mobile, or desktop interface against product intent, its design system, accessibility, themes, states, responsiveness, and localization resilience. Use for UI changes or explicit interface review.
---

# S UI Check

Inspect the running interface in the modality where users experience it. Source alone cannot prove appearance, interaction, responsiveness, accessibility, or platform fit. Use the project's real browser, simulator, device, or native harness and retain rendered evidence.

Independent verification starts in a fresh context with the accepted contract, candidate identity, and relevant project constraints, without inherited builder conversation or rationale. A review performed in the builder's context remains self-verification.

Treat the project's design system as the source of truth. When none exists, verify that the surface establishes a proportional, coherent token/component system rather than isolated styling decisions.

Exercise the relevant combinations of:

- light, dark, and system appearance;
- representative wide and narrow layouts, orientation, zoom, and content density;
- keyboard, focus, pointer, touch, assistive names, contrast, and reduced motion;
- loading, empty, validation, saving, success, failure, offline, permission, and destructive-confirmation states that can occur;
- long translated text, dynamic values, overflow, and RTL when localization is applicable or future support is an accepted design constraint;
- platform navigation and interaction conventions, hierarchy, continuity, and recovery from errors.

Derive relevant platforms, sizes, states, and standards from the product and changed surface, using native conventions rather than a fixed viewport grid. Use current market practice when project rules leave a consequential point open.

Bind findings and screenshots to the frozen candidate. Report defects, evidence boundaries, and coverage separately. Leave maintained product unchanged, return repairs to the implementation owner, and recheck affected states against the new candidate. When an issue is unjustified residue, coordinate with the applicable artifact-quality capability; report the concrete UI effect without making an aesthetic resemblance the verdict.

Document-level fit does not prove component text is visible. Inspect pixels and local bounds for clipping or stale layouts. Return evidence in-channel; create no report or run-state artifact unless requested.
