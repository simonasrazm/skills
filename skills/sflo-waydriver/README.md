# SFLO Waydriver

SFLO Waydriver is a Markdown outcome driver for frontier models, shaped by real work and experiments with Sol and Astra. Compared with earlier SFLO variants, its agent capabilities are reusable skills: invoke the full factory or only the capability you need, whenever you need it. The experimental package has been tested with Sol and Astra; verification limits are recorded in the release notes.

It aims to drive safely from intent to verified acceptance and return to a person only when evidence, collective knowledge, and bounded experiments cannot find a safe route.

## Skill family

| Skill | Purpose |
| --- | --- |
| `sflo-waydriver` | Default entry point: discovery, action, independent checks, acceptance |
| `s-waydriver` | Advanced control plane only: discovery, decisions, graph, frontier, resumption |
| `s-dev` | Product implementation and repair |
| `s-qa` | Fast, slice, and final functional QA |
| `security-check` | Independent security outcome and coverage |
| `slop-sweep` | Intent-based slop/bloat review and bounded presentation repair |
| `s-ui-check` | Rendered web, mobile, or desktop interface verification |

The family is deliberately compound. The conductor activates only the skills justified by the current work and changed surface, keeping unrelated specialist instructions unloaded.

Smart Shot and the Dig Deeper skills are optional competence providers. When absent, the family uses available primary sources, bounded experiments, and evidence-first diagnosis. Independent acceptance requires fresh reviewer contexts and retrievable reports bound to the candidate.

## Which driver to call

Call `sflo-waydriver` when a problem needs discovery, authorized action, and independent acceptance. The destination can be a strategy, research result, practical project, or software change. It chooses a bounded composition or invokes `s-waydriver` when durable coordination becomes useful.

The code-based `sflo` runner is a separate factory. An explicit `sflo-waydriver` invocation selects this Markdown family.

For a surgical software fix, it stays with the smallest verified composition: a clarity check, one mutation unit, `s-dev`, `s-qa`, and only applicable specialist checks. It creates no durable map and avoids loading unrelated capabilities.

These are capabilities rather than a required agent roster. A small change normally uses one builder context and one fresh acceptance context; a competent reviewer can cover multiple applicable lenses while reporting their coverage separately. Extra specialists remain available when the risk or expertise requires them.

Handoffs carry verified file paths. Independent reads are batched, current evidence is reused, and compact acceptance records retain executable probes. Requested report files belong to the checker that writes them; the conductor consumes the report and confirms candidate identity before accepting it.

Call `s-waydriver` directly when the requested outcome is the route itself: map a foggy effort, resolve decisions, coordinate or resume work, or embed a durable work graph in another workflow. It supplies control state, not SFLO's implementation and quality policy.

If unsure, call `sflo-waydriver`; it delegates navigation without forcing a durable map onto a surgical change.

## Component output

Standalone component skills return their result through the invoking harness. The developer and bounded slop repair may modify the requested artifact; independent checkers remain read-only. They create no factory state or report file unless asked. `s-waydriver` is the exception because durable work state is its product.

## Using surgical mode

Invoke the conductor explicitly:

> Use `sflo-waydriver` in surgical mode to fix the duplicate submission bug.

Surgical mode is not another skill. It is the smallest acceptance-bearing composition. For software, that means a clarity assessment, `s-dev`, independent `s-qa`, applicable specialist checks, and the repair loop. You can also invoke `s-dev` and `s-qa` directly when you want to compose that route yourself.

## Arena status

This family has permanent paths under `skills/` and `arena` maturity in the repository catalog. It is available for explicit installation but remains outside the stable plugin catalog. Promotion changes maturity and catalog inclusion without moving files.

Existing SFLO project knowledge will be migrated into a durable documentation and decision-record structure compatible with current and future Wayfinder work; active legacy run state is left in place.

## Credits and compatibility

`s-waydriver` ports and extends Matt Pocock's excellent [Wayfinder](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder) model. The current compatibility base is upstream commit `3cca18b` (2026-09-04). Wayfinder and Waydriver can coexist: Waydriver preserves Wayfinder decision maps and keeps delivery units in a separate linked carrier. The deliberate changes are documented next to the port for manual upstream review.

The upstream MIT copyright and permission notice is retained in [the Wayfinder license](../s-waydriver/LICENSE.wayfinder).
