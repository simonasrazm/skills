# Agent Skills

Agent skills I use in day-to-day work: building SFLO, working on my private
dark factory, and investigating complex systems by hand.

## Skills

| Skill | Purpose |
|---|---|
| [Dig Deeper](#dig-deeper) | Evidence-first troubleshooting with gentle and active modes |
| [Smart Shot](#smart-shot) | Intent-based prompt enhancement when multiple domain experts are needed |
| [SFLO Quick](#sflo-quick) | Light version of dark factory. Good for demos and small projects |
| [SFLO No Code](#sflo-no-code) | Markdown-only SFLO with durable evidence gates |

### Dig Deeper

#### Motivation

I have run into this pattern too many times: an LLM confidently claims it found the real problem, but it was just an assumption. Dig Deeper exists to make that failure mode harder. Claims need evidence; weak hypotheses get challenged.

It has two entry points:

- [`dig-deeper`](skills/dig-deeper/) for non-mutating investigation.
- [`dig-deeper-probe`](skills/dig-deeper-probe/) for active evidence collection using tools, installations, reproductions, and controlled experiments while avoiding damage.

Dig Deeper separates investigation from challenge. The Troubleshooter collects facts, builds hypotheses, and traces possible causes. The Interrogator attacks weak evidence, bias, premature closure, and unsupported fixes.

Use Dig Deeper when you need to hunt down nasty issues in complex systems, especially when the cost of guessing is high. Use available tools to collect evidence and take authorized corrective actions when needed.

Default run budget: up to five Troubleshooter/Interrogator rounds. The loop stops immediately on PASS.

The original [`str`](skills/deprecated/str/) implementation is preserved under `deprecated` with a migration notice.

#### Outcomes

- Deep diagnosis with an explicit evidence-collection boundary.
- Clear evidence tables instead of persuasive narratives.
- Bias checks against anchoring, premature closure, and guessed causes.
- Fix recommendations only when the root cause is evidence-backed.

### Smart Shot

Zero-shot enhancement for people in a hurry, from text improvement to micro
software delivery.

Use Smart Shot when a prompt is short, when the user may be speaking in a
solution rather than the underlying intent, or when the task needs fast intent
recovery before planning and execution.

Path: [skills/smart-shot](skills/smart-shot/)

#### Outcomes

- Hidden intents, consequential objectives, requirements, and success criteria recovered before planning.
- Expert subagents for inferred domains, roles, and LLM judge responsibilities.

### SFLO Quick

Five-gate Markdown workflow for quick software development.

Invoke it explicitly:

> SFLO-QUICK: build a small personal expense tracker

You can also directly ask to run `sflo-quick`.

Path: [skills/sflo-quick](skills/sflo-quick/)

Run evidence stays under `.sflo-quick/<feature-or-scope-slug>/`; product files stay at scoped project paths.

### SFLO No Code

Markdown-only SFLO for building software through five evidence gates:
Discover, Build, Test, Verify, and Ship. Each gate writes a durable artifact,
fresh QA and PM reviewers must both award grade A, and repeated failures loop
back to Build or escalate to the human.

Invoke it explicitly:

> SFLO-NO-CODE: build a small personal expense tracker

You can also directly ask to run or use `sflo-no-code`. Ordinary software
requests do not activate it, and `SFLO:` remains reserved for Python-backed
SFLO. Its personal, non-commercial, speed-first positioning is descriptive;
explicit commercial use remains allowed.

Path: [skills/sflo-no-code](skills/sflo-no-code/)

Derived from [SFLO v1 at commit `7c53dba`](https://github.com/simonasrazm/simon-factory-lights-out/commit/7c53dba87045d3ae80b4b01bb23d4cbf09941b84).

#### Outcomes

- Exact scope, deliverables, and acceptance criteria before building.
- Runnable product evidence instead of compilation-only completion claims.
- Fresh QA and independent PM verification with grade-A thresholds.
- Durable Markdown handoffs, bounded retries, and terminal SHIP/HOLD/KILL evidence.

## Recommendation

Use [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) to gain speed in any agent. Terse communication reduces turn latency, especially in long loops.
