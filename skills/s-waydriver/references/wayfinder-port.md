# Wayfinder Port Notes

Compatibility base: `mattpocock/skills` commit `3cca18b368ae95cdbdebbff572ccafa662551015` (2026-09-04, package version 1.2.3).

Derived Wayfinder material retains the upstream [MIT copyright and permission notice](../LICENSE.wayfinder).

This port intentionally retains Wayfinder's vocabulary and boundaries in parallel sections: destination, map-as-index, named decision tickets, four ticket types, tracker-native blocking, frontier, fog of war, out of scope, resolution pointers, and resumability. Preserve upstream wording where the behavior is unchanged so a manual comparison remains legible.

## Dependency inventory

The upstream skill directly depends on or schedules these capabilities:

- `setup-matt-pocock-skills` plus tracker-specific Wayfinding operations, with local Markdown as the fallback;
- grilling and domain modeling for intent and decision discovery;
- prototype for questions requiring a concrete artifact;
- research subagents for facts outside the working directory, with findings carried on throwaway research branches and linked from the ticket.

Waydriver carries tracker setup/fallback, discovery, domain-modeling outcomes, prototype, research-carrier, and continuation behavior in its own skill and references. It uses this repository's `smart-shot` for substantial research when installed and has an evidence-equivalent fallback. Software implementation and quality policy after the map clears belong to the embedding workflow rather than this control-plane skill.

## Deliberate divergences

- The agent drives high-confidence discovery and bounded experiments before asking a person. Human grilling remains for irreducible preferences or authority.
- Research uses the best available evidence carrier and a retrievable pointer; it does not require a subagent or throwaway branch when the harness or task does not justify one.
- Planning still precedes implementation when needed, but clearing the decision map does not force the factory to stop.
- Delivery units live in a separate linked map, preserving the meaning of Wayfinder decision tickets and allowing either skill to resume the decision map.
- Focus is one active mutation-bearing unit, not an unconditional one-ticket session.
- Product and architecture decision records are distinct classifications under one protocol.
- Quality, security, slop, UI, repair, blocker notification, and terminal-state behavior extend the map into an autonomous factory.

## Manual upstream review

Compare the upstream `skills/engineering/wayfinder/SKILL.md`, its documentation, and tracker templates against this file and `SKILL.md`. Record the reviewed upstream commit here. Port semantic changes section by section; retain deliberate divergences rather than overwriting them. Re-run Waydriver compatibility and factory forward tests after every accepted update.
