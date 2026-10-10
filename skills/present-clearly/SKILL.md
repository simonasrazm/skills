---
name: present-clearly
description: Make explanations, decisions and work results easy to understand in replies, documents and reviews. Use for substantive explanations, architecture decisions, comparisons and handovers, including when nothing changed. Select useful content and its clearest form while preserving requested depth and format.
---

# Present Clearly

Present the meaning the person needs, with enough detail to understand it correctly. Apply this to substantive explanations and artifacts; a simple answer can stay a sentence.

Use the request and existing context to infer what the person needs to understand or do. Apply this directly, without an audience questionnaire or a separate planning artifact. Ask only when an unresolved difference would materially change the answer. Respect explicit depth, format and audience expertise.

## Select before drafting

Privately identify the question this artifact must answer, then build its outline from that question rather than from the source notes. Select content for that outline; do not summarize every supplied fact. Keep decisions, relationships, consequences and uncertainty that change its interpretation. Place investigation history, test logs and tuning details in their existing evidence or operational home, linking when useful. Keep a warning beside an action when omitting it could lead someone to act incorrectly. Omit irrelevant evidence silently; do not fill the deliverable with explanations of what belongs elsewhere.

For architecture and decision documents, describe the intended arrangement and its trade-offs. Include operational settings or implementation status only when they affect the decision; these documents are not progress reports. A fact can matter to the project without belonging in this artifact.

Preserve constraints, exceptions, numbers and qualifications needed for correctness. Concision removes duplication and irrelevant material, not requested detail or inconvenient uncertainty. Do not manufacture a baseline, causal connection or completion claim. Check that the source supports the connections between facts, not only the facts individually. When a connection depends on an unstated assumption, state that condition where the claim first appears. Later caveats do not repair an overconfident opening.

Choose and build the main view before supporting prose. For relationship-heavy explanations, show the relevant paths and boundaries in a flow or sequence; an inventory of owners alone does not show how they connect. Use a comparison for alternatives, a before/after view for change, or plain text when that is clearer. A requested format takes precedence. After building the view, compare each supporting sentence with it and delete repeated information. Keep prose for reasons, exceptions or consequences the view does not convey. Keep essential meaning visible without interaction. Use the medium's appropriate authoring and rendering tools.

## Revise as a whole

When adding findings or responding to a correction, reassess the whole affected artifact against its purpose. Replace superseded content and remove duplication instead of appending another explanation. Apply relevant corrections throughout the current task without turning situational preferences into universal rules.

Keep evidence and status distinct: proposed is not implemented, a passing deployment is not runtime proof, and a repaired check is not a repaired product. Retain the evidence in the work record; include it in the deliverable when requested or needed to judge or act on the result.

For a requested deep catch-up, a baseline that needs reconstruction, or interacting changes that cannot be explained faithfully in a compact view, use [catch-up](references/catch-up.md). [Examples](references/examples.md) illustrate choices, not required templates.

## Acceptance

Review the actual reply or whole affected artifact against the original request:

- **Fidelity:** Essential facts, exceptions, uncertainty and actions survive. Check against source evidence, not just the previous draft.
- **Necessity:** Each part answers the request or prevents a consequential misunderstanding. Remove material whose absence changes neither understanding nor action.
- **Representation:** Relationships are clear in the main view, with each point stated once unless repetition serves the requested use.
- **Readability:** Inspect visuals where delivered, at normal viewing size. Essential labels must be legible beside surrounding text in the intended initial view; check all changed diagrams, not just the page header or source. A compact container does not establish readable content.

Repair failed qualities before delivery. Word count, successful tool calls and having loaded this skill are not acceptance evidence. If rendering cannot be verified, state that limit rather than claiming visual completion.
