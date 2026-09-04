---
name: dig-deeper-probe
description: High-trust active evidence-first troubleshooting for difficult problems. Use when the agent should employ whatever evidence-gathering methods the objective requires, including using or installing tools and interacting with targets, while avoiding damage. Diagnosis only, never remediation.
disable-model-invocation: true
---

# Dig Deeper Probe

Run `dig-deeper-core` with:

```markdown
profile: HIGH_TRUST_ACTIVE
objective: gather evidence needed for diagnosis
allow: any useful method; acquire missing capabilities; reproduce/simulate/experiment; controlled target interaction
choose: rank available methods by expected discrimination and effect; run best permitted first; if blocked, unblock/acquire within boundary; weaker fallback only if best remains unavailable or insufficient
computer: first only when rendered/manual state is itself evidence
damage: avoid destructive, irreversible, security/privacy-compromising, or recklessly high-blast-radius action; isolate risk when practical; stop if meaningful damage cannot be avoided
authorization: installs allowed; ask only if runtime requires or damage boundary crossed
remediate: no; evidence collection != disguised fix
```

Pass problem + profile. Core owns loop/report. Preserve independent roles.
