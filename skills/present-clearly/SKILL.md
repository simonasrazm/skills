---
name: present-clearly
description: Make explanations, decisions and work results easy to understand in replies, documents and reviews. Use for substantive explanations, architecture decisions, comparisons and handovers, including when nothing changed. Select useful content and its clearest form while preserving requested depth and format.
---

# Present Clearly

Present the meaning the person needs, with enough detail to understand it correctly. Apply this to substantive explanations and artifacts; a simple answer can stay a sentence.

Use the request and existing context to infer what the person needs to understand or do. Apply this directly, without an audience questionnaire or a separate planning artifact. Ask only when an unresolved difference would materially change the answer. Respect explicit depth, format and audience expertise.

## Select before drafting

Privately identify the question this artifact must answer, then build its outline from that question rather than from the source notes. Select content for that outline; do not summarize every supplied fact. Keep decisions, relationships, consequences and uncertainty that change its interpretation. Place investigation history, test logs and tuning details in their existing evidence or operational home, linking when useful. Keep a warning beside an action when omitting it could lead someone to act incorrectly. Omit irrelevant evidence silently; do not fill the deliverable with explanations of what belongs elsewhere.

For comparisons and borrowing recommendations, establish the difference at the same level: an existing requirement, its implemented mechanism, and a proposed addition are different claims. Show what the addition supplies beyond the established baseline, or say that no addition is supported. A concrete example of an existing responsibility is not evidence of a missing capability.

For architecture and decision documents, describe the intended arrangement and its trade-offs. Include operational settings or implementation status only when they affect the decision; these documents are not progress reports. A fact can matter to the project without belonging in this artifact.

Preserve constraints, exceptions, numbers and qualifications needed for correctness. Concision removes duplication and irrelevant material, not requested detail or inconvenient uncertainty. Do not manufacture a baseline, causal connection or completion claim. Check that the source supports the connections between facts, not only the facts individually. When a connection depends on an unstated assumption, state that condition where the claim first appears. Later caveats do not repair an overconfident opening.

Make the main view carry the explanation so the reader can grasp the material meaning without reading a prose version first. For a change with a known baseline, default to a compact logical diff in a fenced `diff` block: minus lines show what stops or changes, plus lines show its replacement, and context lines retain consequential conditions. Explain behavior or meaning rather than listing edited files. For flows, ownership, dependencies or boundaries, use a compact diagram with meaningful connections: who acts, on what, and under which condition. For alternatives, align the consequential differences in a comparison. Choose the smallest set of views that answers the question.

Write supporting prose only for reasons, qualifications or actions the views cannot convey clearly. A heading can locate a view; an introduction, bullet list or conclusion that retells it is duplication. Keep essential meaning visible without interaction. Preserve requested depth and format, use the actual media when appearance or motion is the subject, and keep genuinely simple answers as sentences. Without an established baseline, show the current relationship or conclusion rather than inventing a change. Use the medium's appropriate authoring and rendering tools.

## Revise as a whole

When adding findings or responding to a correction, reassess the whole affected artifact against its purpose. Replace superseded content and remove duplication instead of appending another explanation. Apply relevant corrections throughout the current task without turning situational preferences into universal rules.

Keep evidence and status distinct: proposed is not implemented, a passing deployment is not runtime proof, and a repaired check is not a repaired product. Retain the evidence in the work record; include it in the deliverable when requested or needed to judge or act on the result.

For a requested deep catch-up, a baseline that needs reconstruction, or interacting changes that cannot be explained faithfully in a compact view, use [catch-up](references/catch-up.md). [Examples](references/examples.md) illustrate choices, not required templates.

## Acceptance

Review the actual reply or whole affected artifact against the original request:

- **Fidelity:** Essential facts, exceptions, uncertainty and actions survive. Check against source evidence, not just the previous draft.
- **Necessity:** Each part answers the request or prevents a consequential misunderstanding. Remove material whose absence changes neither understanding nor action.
- **Representation:** The main view carries the material change or relationship; accurate prose alone does not substitute for an applicable view. Check supporting sentences against it and remove repeated meaning. Exceptions follow the requested format, medium or genuinely simple answer, not convenience.
- **Readability:** Inspect visuals where delivered, at normal viewing size. Essential labels must be legible beside surrounding text in the intended initial view; check all changed diagrams, not just the page header or source. A compact container does not establish readable content.

Repair failed qualities before delivery. Word count, successful tool calls and having loaded this skill are not acceptance evidence. If rendering cannot be verified, state that limit rather than claiming visual completion.
