# Skills

[![Skills](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsimonasrazm%2Fskills%2Fmain%2Fskills.catalog.json&query=%24.skills.length&label=skills&color=blue)](skills.catalog.json) [![Validate skills](https://github.com/simonasrazm/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/simonasrazm/skills/actions/workflows/validate.yml)

Skills for Software (or any work) Factory, deep diagnosis, hard decisions and verified outcomes. Built for Codex, Claude Code and other compatible agents.

## Skills

| Skill | Use it for | Version |
|---|---|---|
| [SFLO Waydriver](skills/sflo-waydriver/) | Best of SFLO and Wayfinder (from Matt Pocock). Throw at any problem, not just software development or quick fixes | `1.0.1-rc.2` |
| [Smart Shot](skills/smart-shot/) | Read between the lines: discover hidden intents. Identify domains touched and discover unknown unknowns. Assemble ad hoc expert agents | `2.0.0` |
| [Dig Deeper](skills/dig-deeper/) | Diagnose nasty, deep bugs using logs, system state and other read-only evidence. Do not allow AI to present assumptions as facts or conclusions | `2.0.1` |
| [Dig Deeper Probe](skills/dig-deeper-probe/) | Reproduce failures and run controlled experiments when observation is not enough. Install tools with consent or within your established execution boundary | `2.0.1` |
| [Fast Shot](skills/fast-shot/) | Get a moderately better result from a weak prompt through a lighter, much faster Smart Shot | `0.1.0` |
| [Retrospective](skills/retrospective/) | Find why skills and workflows fell short. Suggest evidence-backed improvements for future work. | `0.1.0` |
| [Slop Sweep](skills/slop-sweep/) | Remove unjustified filler and complexity from prose, plans, interfaces or code; repair presentation when authorized. | `1.0.1-rc.2` |
| [Security Check](skills/security-check/) | First line for the security risks. Use linters, scanners and other means for any professional delivery. | `1.0.1-rc.2` |

[Skill Compressor](skills/skill-compressor/) is my own utility for optimizing my skills. It saves tokens and improves speed without breaking it. You can find many other variants of the same problem on the wild internet.

See [release notes](CHANGELOG.md).

### SFLO Waydriver components

These also work independently, but are meant for the factory

| Skill | Use independently for | Version |
|---|---|---|
| [S Waydriver](skills/s-waydriver/) | Map decisions, coordinate dependencies and resume work. Supply the project's execution and acceptance policy. | `1.0.1-rc.2` |
| [S Domain Modeling](skills/s-domain-modeling/) | Sharpen domain language and rules; reconcile glossaries, behavior and decisions. | `1.0.1-rc.2` |
| [S Dev](skills/s-dev/) | Implement or repair a scoped change and return builder checks. Independent acceptance follows through S QA. | `1.0.1-rc.2` |
| [S QA](skills/s-qa/) | Verify an increment candidate against acceptance criteria with fast, slice or final coverage. | `1.0.1-rc.2` |
| [S UI Check](skills/s-ui-check/) | Verify visual presentation and interaction in the delivered medium. | `1.0.1-rc.2` |
| [Present Clearly](skills/present-clearly/) | Select useful content and clear views for explanations, decisions and handovers. | `1.0.1-rc.2` |

### Dependencies

Retrospective uses Present Clearly for its findings and recommendations. Both are included in the bundle.

The complete bundle includes SFLO Waydriver and its execution, review and discovery skills; no separate Matt Pocock installation is required.

## Install

Install the complete bundle for Codex and other compatible agents:

```shell
npx skills@latest add simonasrazm/skills --skill '*'
```

Claude Code: the marketplace package includes the same complete bundle.

```shell
claude plugin marketplace add simonasrazm/skills
claude plugin install simon-skills@simonasrazm
```

## Try them

```text
Use retrospective: what should we improve from this session?
```

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
Use sflo-waydriver: prepare the presentation for tomorrow's product review.
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

## Upstream license

Retrospective includes adaptations from [Matt Pocock’s skills](https://github.com/mattpocock/skills). His MIT notice is reproduced below. The repository’s own license remains in [LICENSE](LICENSE).

MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
