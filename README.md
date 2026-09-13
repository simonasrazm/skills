# Skills

[skills.sh directory](https://skills.sh/simonasrazm/skills)
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
| [SFLO Waydriver](skills/sflo-waydriver/) | Carry a problem from intent through discovery, action, independent checks and repair to an evidenced outcome. Composes the capabilities below as the work requires; preview |
| [Point the Way](skills/point-the-way/) | When you want AI to consider more options and probe which one is unblocked. When you just need a problem to go away rather than a perfect solution |

### Waydriver components

SFLO Waydriver is the full delivery workflow. Its six supporting skills also work independently; invoking one does not start the full workflow.

| Skill | Use independently for | Relationship to SFLO Waydriver |
|---|---|---|
| [S Waydriver](skills/s-waydriver/) | Map a complex effort, resolve decisions, coordinate dependencies and resume work. Supply the execution and acceptance policy for the project. | Maintains decisions and work state when durable coordination is needed. |
| [S Dev](skills/s-dev/) | Implement or repair a scoped change and return the candidate with builder checks. | Software implementation and repair; independent acceptance follows through S QA. |
| [S QA](skills/s-qa/) | Check an existing candidate against acceptance criteria and return evidence and defects. | Independent QA after S Dev; fast, slice or final coverage. |
| [S UI Check](skills/s-ui-check/) | Inspect a running interface for visual, interaction, accessibility and responsive defects. | Required when delivered or changed behavior has a user interface. |
| [Security Check](skills/security-check/) | Assess a candidate's security and privacy risks. | Used when the destination or changed surface warrants security review. |
| [Slop Sweep](skills/slop-sweep/) | Review prose, plans, interfaces or code for unjustified filler and complexity; make bounded presentation repairs when authorized. | An applicable quality lens, not a mandatory separate stage. |

Independent checks need a fresh context, the candidate and its acceptance criteria. Standalone components do not require the conductor. S Waydriver creates durable work state; the other components return results without creating workflow state unless requested.

### Dependencies and installation

Install SFLO Waydriver with all six components above so its delegated paths are available. It loads only the capabilities needed for the current work. [Smart Shot](skills/smart-shot/) supplies discovery and specialist judgment; [Dig Deeper](skills/dig-deeper/) and [Dig Deeper Probe](skills/dig-deeper-probe/) supply diagnosis. These are optional competence providers: when unavailable, the conductor uses available tools to obtain the required evidence. The code-based `sflo` runner is separate and is not a dependency.

Both Dig Deeper entry points require [Dig Deeper Core](skills/dig-deeper-core/), their shared internal engine. The core is not a standalone user entry point. [Skill Compressor](skills/skill-compressor/) is a standalone utility for reducing a skill's token cost while testing that its routing and behavior survive.

The [catalog](skills.catalog.json) lists 15 definitions: seven main entry points, six Waydriver components, the Dig Deeper core and Skill Compressor. The skills.sh directory may list fewer; its badge is not the repository inventory.

Waydriver and Point the Way remain previews with `arena` maturity in the catalog. Their source paths stay under `skills/`. The Claude marketplace package currently selects the seven stable definitions, including Dig Deeper Core; it does not install the preview family. Use the `npx skills@latest add simonasrazm/skills` installer above and select the Waydriver family to try it. Main-table placement does not change maturity or package selection. See [release notes](CHANGELOG.md) and the [Waydriver guide](skills/sflo-waydriver/).

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
