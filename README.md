# Skills

[![Skills](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsimonasrazm%2Fskills%2Fmain%2Fskills.catalog.json&query=%24.skills.length&label=skills&color=blue)](skills.catalog.json) [![Validate skills](https://github.com/simonasrazm/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/simonasrazm/skills/actions/workflows/validate.yml)

Skills for Software (or any work) Factory, deep diagnosis, hard decisions and verified outcomes. Built for Codex, Claude Code and other compatible agents.

## Skills

| Skill | Use it for | Version |
|---|---|---|
| [SFLO Waydriver](skills/sflo-waydriver/) | Best of SFLO and Wayfinder (from Matt Pocock). Throw at any problem, not just software development or quick fixes | `0.5.0-rc.2` |
| [Smart Shot](skills/smart-shot/) | Read between the lines: discover hidden intents. Identify domains touched and discover unknown unknowns. Assemble ad hoc expert agents | `2.0.0` |
| [Dig Deeper](skills/dig-deeper/) | Diagnose nasty, deep bugs using logs, system state and other read-only evidence. Do not allow AI to present assumptions as facts or conclusions | `2.0.1` |
| [Dig Deeper Probe](skills/dig-deeper-probe/) | Reproduce failures and run controlled experiments when observation is not enough. Install tools with consent or within your established execution boundary | `2.0.1` |
| [Fast Shot](skills/fast-shot/) | Get a moderately better result from a weak prompt through a lighter, much faster Smart Shot | `0.1.0` |
| [SFLO Quick](skills/sflo-quick/) | Execute any bounded task through a lightweight plan-do-check-act cycle that removes basic mistakes. Use it when you are tired of repeating basic mistakes by agents | `0.1.0` |
| [Point the Way](skills/point-the-way/) | When you want AI to consider more options and probe which one is unblocked. When you just need a problem to go away rather than a perfect solution | `0.1.0` |
| [Slop Sweep](skills/slop-sweep/) | Remove unjustified filler and complexity from prose, plans, interfaces or code; repair presentation when authorized. | `0.5.0-rc.2` |
| [Security Check](skills/security-check/) | First line for the security risks. Use linters, scanners and other means for any professional delivery. | `0.5.0-rc.2` |

[Skill Compressor](skills/skill-compressor/) is my own utility for optimizing my skills. It saves tokens and improves speed without breaking it. You can find many other variants of the same problem on the wild internet.

See [release notes](CHANGELOG.md).

### SFLO Waydriver components

These also work independently, but are meant for the factory

| Skill | Use independently for | Version |
|---|---|---|
| [S Waydriver](skills/s-waydriver/) | Map decisions, coordinate dependencies and resume work. Supply the project's execution and acceptance policy. | `0.5.0-rc.2` |
| [S Dev](skills/s-dev/) | Implement or repair a scoped change and return builder checks. Independent acceptance follows through S QA. | `0.5.0-rc.2` |
| [S QA](skills/s-qa/) | Verify an increment candidate against acceptance criteria with fast, slice or final coverage. | `0.5.0-rc.2` |
| [S UI Check](skills/s-ui-check/) | Inspect a running interface for visual, interaction, accessibility and responsive defects. It is not invoked in non-UI efforts | `0.5.0-rc.2` |

### Dependencies

**SFLO Waydriver:** install the whole skills repo. The skill has dependencies on most of the skills

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
