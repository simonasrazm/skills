# SFLO Waydriver

Use `sflo-waydriver` to carry a problem from discovery through execution, independent checks and repair. It uses a durable work map when decisions or dependencies require one; a clear surgical fix stays small.

```text
Use sflo-waydriver to fix the duplicate submission bug.
```

## Skills

| Skill | Use independently for |
| --- | --- |
| `sflo-waydriver` | Delivering an outcome with discovery and independent acceptance |
| `s-waydriver` | Mapping decisions, coordinating dependencies and resuming work; supply execution and verification capabilities |
| `s-dev` | Implementing or repairing a scoped change |
| `s-qa` | Independently checking an increment or accumulated behavior |
| `security-check` | Assessing security risks and review coverage |
| `slop-sweep` | Removing unjustified filler and complexity |
| `s-ui-check` | Verifying a rendered interface |

The conductor selects applicable skills. Smart Shot and Dig Deeper provide optional discovery and diagnosis; available evidence and tools provide the fallback. A small change normally needs one builder and one fresh reviewer.

Components return results in-channel unless an artifact is requested. Independent checks are read-only; implementation and authorized slop repairs may modify artifacts. `s-waydriver` maintains durable work records. The code-based `sflo` runner is a separate execution option, selected explicitly.

## Credits

S Waydriver adapts Matt Pocock's [Wayfinder](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder) and [domain-modeling](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling). It preserves decision maps and adds a separate delivery map. The [upstream MIT notice](../s-waydriver/LICENSE.wayfinder) is retained.
