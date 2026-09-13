# Skills

[skills.sh directory](https://skills.sh/simonasrazm/skills) · [![Validate skills](https://github.com/simonasrazm/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/simonasrazm/skills/actions/workflows/validate.yml)

Skills for deep diagnosis, hard decisions and verified outcomes. Built for Codex, Claude Code and other compatible agents.

## Skills

| Skill | Use it for | Version |
|---|---|---|
| [SFLO Waydriver](skills/sflo-waydriver/) | Carry a problem through discovery, action, independent checks and repair to the intended outcome. | `0.4.0-rc.2` |
| [Smart Shot](skills/smart-shot/) | Discover hidden intent and unknowns; assemble specialists to resolve them. | `2.0.0` |
| [Dig Deeper](skills/dig-deeper/) | Diagnose difficult failures through read-only evidence. | `2.0.0` |
| [Dig Deeper Probe](skills/dig-deeper-probe/) | Reproduce failures and run controlled experiments when observation is insufficient. | `2.0.0` |
| [Fast Shot](skills/fast-shot/) | Improve a bounded request with a few focused checks. | `0.1.0` |
| [SFLO Quick](skills/sflo-quick/) | Execute a small task through a lightweight plan, act, check and repair loop. | `0.1.0` |
| [Point the Way](skills/point-the-way/) | Find and test a workable route around constraints. | `0.1.0` |
| [Slop Sweep](skills/slop-sweep/) | Remove unjustified filler and complexity from prose, plans, interfaces or code; repair presentation when authorized. | `0.4.0-rc.2` |
| [Security Check](skills/security-check/) | Independently assess realistic security and privacy risks. | `0.4.0-rc.2` |
| [Skill Compressor](skills/skill-compressor/) | Reduce skill token cost while testing that routing and behavior survive. | `0.1.0` |

Versions come from the [catalog](skills.catalog.json). `0.x` denotes initial development; `rc` denotes a release candidate. See [release notes](CHANGELOG.md) for changes and verification limits.

### Waydriver components

These also work independently. Slop Sweep and Security Check, listed above, bring the supporting component count to six.

| Skill | Use independently for | Version |
|---|---|---|
| [S Waydriver](skills/s-waydriver/) | Map decisions, coordinate dependencies and resume work. Supply the project's execution and acceptance policy. | `0.4.0-rc.2` |
| [S Dev](skills/s-dev/) | Implement or repair a scoped change and return builder checks. Independent acceptance follows through S QA. | `0.4.0-rc.2` |
| [S QA](skills/s-qa/) | Verify a candidate against acceptance criteria with fast, slice or final coverage. | `0.4.0-rc.2` |
| [S UI Check](skills/s-ui-check/) | Inspect a running interface for visual, interaction, accessibility and responsive defects. | `0.4.0-rc.2` |

### Dependencies

- **SFLO Waydriver:** install all six components. It invokes them as needed; UI changes require S UI Check. Smart Shot and the Dig Deeper skills are optional discovery and diagnosis providers. The code-based `sflo` runner is separate.
- **Dig Deeper and Dig Deeper Probe:** require [Dig Deeper Core](skills/dig-deeper-core/), a shared engine rather than a standalone entry point.
- **Standalone components:** do not require SFLO Waydriver. Independent checks need a fresh context, the candidate and acceptance criteria.

## Install

Codex and other compatible agents; select the skills you need:

```shell
npx skills@latest add simonasrazm/skills
```

Claude Code's marketplace package includes Dig Deeper, Dig Deeper Probe, their core, Smart Shot, Fast Shot, SFLO Quick and Skill Compressor. Use the installer above for the other skills.

```shell
claude plugin marketplace add simonasrazm/skills
claude plugin install simon-skills@simonasrazm
```

## Try them

```text
Use sflo-waydriver: develop a convincing offer for this product.
```

```text
Use dig-deeper: why is my computer slow today?
```

```text
Use dig-deeper-probe: why does the payment workflow fail end-to-end?
```

```text
Use smart-shot: analyze incident.io.
```

```text
SFLO-QUICK: prepare the presentation for tomorrow's product review.
```

```text
Use slop-sweep: review this strategy for filler and unnecessary complexity.
```

See the [Waydriver guide](skills/sflo-waydriver/) for composition and standalone use.

## Why I build these

I want agents to investigate thoroughly, challenge assumptions and catch their own mistakes. I keep instructions broad enough for frontier models to apply their capabilities, then test them in personal and professional work. Delegating legwork doesn't mean cognitive surrender.

My approach combines software development, product, privacy, security and work management.

## Project

MIT licensed. [Report an issue](https://github.com/simonasrazm/skills/issues) or read [contribution guidance](CONTRIBUTING.md). Browse the [public catalogue](https://finallydone.ai/skills/) for HTML descriptions.
