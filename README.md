# Skills

[![skills.sh](https://skills.sh/b/simonasrazm/skills)](https://skills.sh/simonasrazm/skills)
[![Validate skills](https://github.com/simonasrazm/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/simonasrazm/skills/actions/workflows/validate.yml)

Professional skills for nasty bugs, hard decisions and work that needs to be right. Built for Codex, Claude Code and other compatible agents.

## Install

Codex and other compatible agents:

```shell
npx skills@latest add simonasrazm/skills
```

Claude Code:

```shell
claude plugin marketplace add simonasrazm/skills
claude plugin install simon-skills@simonasrazm
```

## Why I build these

Most public skills give up too early, do little legwork, and use overly large, too specific (narrow) instructions that limit frontier models' capabilities and waste tokens. My skills are polished and battle-tested in personal and professional work.

Dark (Software) Factories - delegate as much as it makes sense. Delegating legwork doesn't mean cognitive surrender. Use AI to sharpen your mind. Agents can do so much more based on known best practices, collecting routine evidence, or catching their own mistakes that they make constantly. I question pre-AI software development habits. I keep the principles, but dive back to the purpose and rebuild the workflow around how AI does the work.

My approach is holistic. I combine experience in software development, product, privacy, security and work organization/management.

## Skills

| Skill | Use it for |
|---|---|
| [Dig Deeper](skills/dig-deeper/) | Diagnose nasty, deep bugs using logs, system state and other read-only evidence. Do not allow AI to present assumptions as facts or conclusions |
| [Dig Deeper Probe](skills/dig-deeper-probe/) | Reproduce failures and run controlled experiments when observation is not enough. Install tools if that would help |
| [Smart Shot](skills/smart-shot/) | Read between the lines: discover hidden intents. Identify domains touched and discover unknown unknowns. Assemble ad hoc expert agents  |
| [Fast Shot](skills/fast-shot/) | Get a moderately better result from a weak prompt through a lighter, much faster Smart Shot |
| [SFLO Quick](skills/sflo-quick/) | Execute any bounded task through a lightweight plan-do-check-act cycle that removes basic mistakes. Use it when you are tired of repeating basic mistakes by agents |
| [Point the Way](skills/point-the-way/) | When you want AI to consider more options and probe which one is unblocked. When you just need a problem to go away rather than a perfect solution |

[Skill Compressor](skills/skill-compressor/) is my own utility for optimizing my skills. It saves tokens and improves speed without breaking it. You can find many other variants of the same problem on the wild internet.

[Dig Deeper core](skills/dig-deeper-core/) is an internal engine used by the two Dig Deeper wrappers. It is not a user entry point.

## Try them

```text
Use dig-deeper with up to 10 rounds: why is my computer slow today?
```

```text
Use dig-deeper-probe: why does the payment workflow fail end-to-end?
```

```text
Use dig-deeper-probe: why does my computer restart often?
```

Smart Shot can start from two words:

```text
Analyze incident.io
```

```text
What are the best options for preserving useful website analytics?
```

```text
Use fast-shot: what does GitLeaks do?
```

```text
SFLO-QUICK: prepare the presentation for tomorrow's product review.
```

```text
SFLO-QUICK: make the presentation about European AI security companies/.  Use smart-shot to shortlist the best ones.
```

## Project

The collection is MIT licensed. [Issues](https://github.com/simonasrazm/skills/issues) are open for reproducible defects and improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change.

The [public catalogue](https://finallydone.ai/skills/) provides the HTML variant of skills' descriptions.

## SFLO Waydriver preview

[SFLO Waydriver](skills/sflo-waydriver/) is a Markdown software factory for implementation, independent checks, repair, and acceptance. Its seven capabilities can be used together or independently.

The family and Point the Way have `arena` maturity in [skills.catalog.json](skills.catalog.json); all source paths remain under `skills/`. Arena skills require explicit installation and are excluded from the stable plugin list. Other installers may still discover them.

Invoke: `Use sflo-waydriver in surgical mode to fix …`

See [release notes](CHANGELOG.md) and [versions, installation and rollback](SKILL-LIFECYCLE.md). The first preview is `v0.3.0-rc.1`.
