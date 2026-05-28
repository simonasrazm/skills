# Agent Skills

Agent skills I use in day-to-day work: building SFLO, working on my private
dark factory, and investigating complex systems by hand.

## Skills

### STR: Simon Troubleshoot

#### Motivation

I have run into this pattern too many times: an LLM confidently claims it found the real problem, but it was just an assumption.
STR exists to make that failure mode harder. Claims need evidence; weak hypotheses get challenged.

Evidence-first troubleshooting for problems where a quick fix is risky.

STR separates investigation from challenge. The Troubleshooter collects facts, builds hypotheses, and traces possible causes. The Interrogator attacks weak evidence, bias, premature closure, and unsupported fixes.

Use STR when you need to hunt down nasty issues in complex systems, especially when the cost of guessing is high.

Path: [skills/str](skills/str/)

Default run budget: up to 3 Troubleshooter/Interrogator rounds. Ask for more
rounds when the issue is high-stakes, evidence is sparse, or the first pass
still leaves important uncertainty.

#### Outcomes

- Slower, safer diagnosis before changing production systems.
- Clear evidence tables instead of persuasive narratives.
- Bias checks against anchoring, premature closure, and guessed causes.
- Fix recommendations only when the root cause is backed by evidence.

### More skills!

Stay tuned.

## Recommendation

Use [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) to gain speed in any agent. Terse communication reduces turn latency, especially in long loops.
