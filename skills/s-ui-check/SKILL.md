---
name: s-ui-check
description: Independently verify visual presentation and interaction in the form people experience them. Use when creating, changing or reviewing human-facing visual output, including configured surfaces and static artifacts.
---

# S UI Check

Review how the output communicates and supports its intended use. Judge hierarchy, legibility, labels, visual relationships and navigation or interaction where present. Apply the relevant design system, template or host-product conventions.

Inspect the output in its delivered medium and viewing conditions. Source alone cannot prove appearance, interaction, accessibility or medium fit. Use a renderer or viewer appropriate to that medium and retain rendered evidence; exercise interaction where the output supports it.

Independent verification starts in a fresh context with the accepted contract, candidate identity, and relevant project constraints, without inherited builder conversation or rationale. A review performed in the builder's context remains self-verification.

Treat the project's design system as the source of truth. When none exists, verify coherent reusable visual conventions appropriate to the surface.

Exercise the relevant combinations of:

- light, dark, and system appearance;
- representative wide and narrow layouts, orientation, zoom, and content density;
- keyboard, focus, pointer, touch, assistive names, contrast, and reduced motion;
- loading, empty, validation, saving, success, failure, offline, permission, and destructive-confirmation states that can occur;
- long translated text, dynamic values, overflow, and RTL when localization is applicable or future support is an accepted design constraint;
- platform navigation and interaction conventions, hierarchy, continuity, and recovery from errors.

Derive relevant sizes, pages, states and standards from the artifact, medium and intended use. For interfaces, include the relevant platform conventions and interaction states. Use current market practice when project rules leave a consequential point open.

Bind findings and screenshots to the frozen candidate. Report defects, evidence boundaries, and coverage separately. Leave maintained product unchanged, return repairs to the implementation owner, and recheck affected states against the new candidate. When an issue is unjustified residue, coordinate with the applicable artifact-quality capability; report the concrete presentation effect without making an aesthetic resemblance the verdict.

Document-level fit does not prove component text is visible. Inspect pixels and local bounds for clipping or stale layouts. Return evidence in-channel; create no report or run-state artifact unless requested.
