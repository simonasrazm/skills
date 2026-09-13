---
name: s-waydriver
description: Reusable control plane for discovering, mapping, coordinating, and resuming a foggy or context-spanning effort. Use when the route itself needs durable decisions, dependencies, frontier state, or Wayfinder-compatible continuation; callers supply domain-specific delivery and verification policy.
---

# S Waydriver

A destination has arrived but the route is not fully visible. Chart only what can be seen, resolve the decisions that clear the fog, then drive acceptance-bearing work until the destination is reached or no safe route remains.

Waydriver ports Wayfinder's map, decision-ticket, fog, frontier, tracker, and resumption semantics. It adds autonomous uncertainty resolution, a separate delivery graph, evidence invalidation, and safe continuation beyond planning. Read [the port notes](references/wayfinder-port.md) when maintaining or synchronizing it.

## Preserve the decision map

The decision map is a canonical index, not a store. A decision lives in exactly one ticket or lasting decision record; the map gists and links it. Refer to maps and units by their human-readable names, with ids carried inside links.

Keep the upstream-compatible decision surface:

```markdown
## Destination

<the accepted end state>

## Notes

<domain, standing preferences, compatibility base, and capabilities to consult>

## Decisions so far

- [<resolved decision name>](link): <one-line consequence>

## Not yet specified

<in-scope fog not yet sharp enough to ask as a precise question>

## Out of scope

<conscious boundaries held outside the frontier>
```

Use the configured issue tracker. If none exists, use `.scratch/<effort>/map.md` with decision tickets under `.scratch/<effort>/issues/`. Read [tracker operations](references/tracker.md) when creating or adapting the carrier.

## Clear fog proportionally

A decision ticket is a precise question whose answer changes the safe route. It is not an implementation slice. Preserve Wayfinder's four types:

- **Grilling:** preference, intent, or domain choices. Apply [autonomous discovery](references/discovery.md); involve the person only when the consequential answer remains theirs.
- **Research:** facts outside the working context. Use `smart-shot` when available, or the same primary-source, multi-domain evidence outcome with available tools.
- **Prototype:** a concrete experiment can answer what discussion cannot. Apply [prototype guidance](references/prototype.md).
- **Task:** action or access needed before a decision can be made. Complete it when authorized; otherwise persist and communicate the blocker while independent work continues.

Fog becomes a ticket when its question can be stated precisely. Resolving a ticket graduates newly visible questions and removes that patch from **Not yet specified**. Out-of-scope work is closed as a boundary, not carried as fog.

Classify lasting records as **product** (behavior, feature, content, UX, business rule) or **architecture** (technical structure, platform, data, integration, security boundary, scalability, operations). Follow the project's decision-record location; otherwise place them under `docs/decisions/product/` or `docs/decisions/architecture/`. The ticket records evidence and links the record.

## Drive delivery separately

When enough decisions are clear to build, create or resume a linked delivery map; keep implementation units separate from Wayfinder decision tickets. Locally use `.scratch/<effort>/delivery.md`. In an issue tracker, use a linked delivery-map issue with its own acceptance-bearing child units.

Delivery units are coherent vertical changes with observable acceptance, real dependencies, candidate identity, and current evidence. The frontier is the open, unblocked, unclaimed set. Keep one maintained-product mutation unit active unless isolation and merge/revalidation are demonstrated. Non-mutating research and checks may overlap when their inputs are frozen and their outputs retrievable.

A caller may supply implementation and verification capabilities. Waydriver records their units, candidate identities, evidence, and blockers without imposing a domain-specific delivery or verification policy. A repair creates a new candidate and reopens affected evidence.

## Continue safely

Each context begins from the destination, frontier, active candidate, decisions, fog, blockers, and evidence, not replayed conversation. Claim before mutating and persist resolution before taking another unit.

One mutation-bearing unit at a time is the focus invariant, not a forced session ending. A session may continue into the next safe frontier unit while context remains reliable. At a context boundary, leave enough state for a fresh executor to continue without guessing.

Drive until the destination has current acceptance evidence, every remaining route is blocked, or a consequential preference or authority decision cannot be derived safely. Ask a person only for that irreducible input; resume independent frontier work before and after the request when possible.
