---
name: explain-change
description: Explain material changes so a person can quickly understand what was solved, where it fits and what needs their attention. Use for a work handover, logical diff, decision update or catch-up across many changes. Supports any domain, with a compact default and deeper reconstruction when needed.
---

# Explain Change

Make the material change understandable without requiring the person to reconstruct it from implementation details. Outcome quality comes before brevity or presentation cost. Respect the requested deliverable and format.

## Meaning before presentation

Reuse the current requirements, baseline, result, decisions and assessment records. Establish what was wrong or needed, what logically changed, where it fits, and why that matters. Distinguish the changed work from its verification or presentation: repairing a check does not establish a repaired product. Keep local, proposed and delivered states distinct.

Give enough context to locate the change: the affected participant, purpose, responsibility or flow. Mention particular artifacts, structures or tools only when their identity helps understanding. Missing material context requires discovery or an explicit unresolved boundary, not an invented baseline.

Select representation from that meaning. Every alternative must communicate the same essential change before comparing style. Choose complementary views for different questions; a map, behavioral comparison and decision lineage are options, not required panels. Motion or effects must clarify a relationship and follow the reading path; essential meaning remains visible without interaction or animation. Use the available rendering skill when a richer visual materially helps.

## Compact handover: default

Use existing knowledge and the smallest sufficient presentation:

- A factual change title or caption that identifies what was solved.
- Enough context to locate it, often a short path or embedded labels.
- A compact logical diff: removed behavior, added behavior and any unchanged constraint needed to understand the result.
- Consequential recorded decisions, material conflicts and supersessions, when present. Include the reason or consequence and a source reference when needed; preserve proposed versus accepted status. An inferred rationale is not a recorded decision.
- Remaining calls to action, when present: who needs to do or decide what, why, and the affected scope.

These are content obligations, not fixed headings. For a state comparison, visibly mark removed and added behavior with minus/plus or equivalent diff encoding; make the diff carry the explanation rather than following it with the same story in prose. An explicit requested format takes precedence. Omit absent items and duplicate summary prose. Plain text or Markdown is sufficient; no bespoke canvas, variants or animation by default. A surgical result may fit in one sentence.

Use actual verification, assurance and authority findings rather than reassessing risk for presentation. Surface unresolved limits that affect the person's next action. Omit routine safe/reversible labels, pass totals and no-action notices. Do not turn an action the agent can resolve within its authority into a human task.

Retain verification and provenance in the work record. When evidence is neither requested nor needed for an action, leave out historical test results, verification narratives and source-link lists. Show a deliverable link when needed to locate or use the result. Quiet presentation never relaxes verification or conceals a material uncertainty.

## Select effort by meaning

An explicit preference wins. Otherwise select effort by the amount of meaning the person must absorb: distinct outcomes, affected participants and activities, dependencies, consequential decisions and supersessions, and distance from their last understood state. Change volume is one signal, not a threshold. Many repetitive changes can fit one compact explanation; several independent changes can use compact explanations each. Interacting changes or a missing baseline can justify deeper reconstruction even for a small change.

When only the presentation choice is unclear, start compact and expand where essential meaning would otherwise be lost. When what changed is unclear, investigate or disclose the unresolved boundary; compact presentation must not hide missing knowledge.

## Deep catch-up: selected by need

Load [catch-up](references/catch-up.md) when requested, when the baseline must be reconstructed, or when interacting changes cannot be explained faithfully in a compact handover. A single complex change can qualify. Keep the compact overview; expand only where it improves understanding. Do not trade away essential meaning to stay in the cheaper mode.

## Check the explanation

Can someone identify the problem, changed behavior, context, consequence and any required action from the delivered output itself? Check this against the source records, not only the appearance. A rendered or model review does not establish human comprehension speed. Keep all alternatives above this semantic bar before comparing taste or cost.

For example shapes, load [examples](references/examples.md). Store temporary presentation files outside the deliverable project or in its ignored scratch area unless the person requests them as project artifacts.
