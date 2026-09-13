# Skills

[skills.sh directory](https://skills.sh/simonasrazm/skills) · [![Validate skills](https://github.com/simonasrazm/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/simonasrazm/skills/actions/workflows/validate.yml)

Skills for deep diagnosis, hard decisions and verified outcomes. Built for Codex, Claude Code and other compatible agents.

## Skills

| Skill | Use it for | Maturity |
|---|---|---|
| [SFLO Waydriver](skills/sflo-waydriver/) | Carry a problem through discovery, action, independent checks and repair to the intended outcome. | Arena · RC |
| [Smart Shot](skills/smart-shot/) | Discover hidden intent and unknowns; assemble specialists to resolve them. | Stable |
| [Dig Deeper](skills/dig-deeper/) | Diagnose difficult failures through read-only evidence. | Stable |
| [Dig Deeper Probe](skills/dig-deeper-probe/) | Reproduce failures and run controlled experiments when observation is insufficient. | Stable |
| [Fast Shot](skills/fast-shot/) | Improve a bounded request with a few focused checks. | Stable |
| [SFLO Quick](skills/sflo-quick/) | Execute a small task through a lightweight plan, act, check and repair loop. | Stable |
| [Point the Way](skills/point-the-way/) | Find and test a workable route around constraints. | Arena |
| [Slop Sweep](skills/slop-sweep/) | Remove unjustified filler and complexity from prose, plans, interfaces or code; repair presentation when authorized. | Arena · RC |
| [Security Check](skills/security-check/) | Independently assess realistic security and privacy risks. | Arena · RC |
| [Skill Compressor](skills/skill-compressor/) | Reduce skill token cost while testing that routing and behavior survive. | Stable |

Maturity follows the [catalog](skills.catalog.json): **Stable** is the established collection; **Arena** is experimental. **RC** marks a release candidate. Stable skills can still have pre-1.0 versions; see [release notes](CHANGELOG.md) for versions and verification limits.

### Waydriver components

These also work independently. Slop Sweep and Security Check, listed above, bring the supporting component count to six.

| Skill | Use independently for | Maturity |
|---|---|---|
| [S Waydriver](skills/s-waydriver/) | Map decisions, coordinate dependencies and resume work. Supply the project's execution and acceptance policy. | Arena · RC |
| [S Dev](skills/s-dev/) | Implement or repair a scoped change and return builder checks. Independent acceptance follows through S QA. | Arena · RC |
| [S QA](skills/s-qa/) | Verify a candidate against acceptance criteria with fast, slice or final coverage. | Arena · RC |
| [S UI Check](skills/s-ui-check/) | Inspect a running interface for visual, interaction, accessibility and responsive defects. | Arena · RC |

### Dependencies

- **SFLO Waydriver:** install all six components. It invokes them as needed; UI changes require S UI Check. Smart Shot and the Dig Deeper skills are optional discovery and diagnosis providers. The code-based `sflo` runner is separate.
- **Dig Deeper and Dig Deeper Probe:** require [Dig Deeper Core](skills/dig-deeper-core/), a shared engine rather than a standalone entry point.
- **Standalone components:** do not require SFLO Waydriver. Independent checks need a fresh context, the candidate and acceptance criteria.

## Install

Codex and other compatible agents; select the skills you need:

```shell
npx skills@latest add simonasrazm/skills
```

Claude Code's marketplace package includes only stable skills. Use the installer above for Arena skills.

```shell
claude plugin marketplace add simonasrazm/skills
claude plugin install simon-skills@simonasrazm
```

## Try them

```text
Use sflo-waydriver: develop a convincing offer for this product.
Use dig-deeper: why is my computer slow today?
Use dig-deeper-probe: why does the payment workflow fail end-to-end?
Use smart-shot: analyze incident.io.
SFLO-QUICK: prepare the presentation for tomorrow's product review.
Use slop-sweep: review this strategy for filler and unnecessary complexity.
```

See the [Waydriver guide](skills/sflo-waydriver/) for composition and standalone use.

## Why I build these

I want agents to investigate thoroughly, challenge assumptions and catch their own mistakes. I keep instructions broad enough for frontier models to apply their capabilities, then test them in personal and professional work. Delegating legwork doesn't mean cognitive surrender.

My approach combines software development, product, privacy, security and work management.

## Project

MIT licensed. [Report an issue](https://github.com/simonasrazm/skills/issues) or read [contribution guidance](CONTRIBUTING.md). Browse the [public catalogue](https://finallydone.ai/skills/) for HTML descriptions.
