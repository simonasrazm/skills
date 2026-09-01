---
name: dig-deeper-probe
description: High-trust active evidence-first troubleshooting for difficult problems. Use when the agent should employ whatever evidence-gathering methods the objective requires, including using or installing tools and interacting with targets, while avoiding damage. Diagnosis only, never remediation.
---

# Dig Deeper Probe

Run `dig-deeper-core` with:

```markdown
profile: HIGH_TRUST_ACTIVE
objective: gather evidence needed for diagnosis
allow: any useful method; tools/CLIs/DevTools/Playwright; download/install; reproduce/simulate/experiment; controlled target interaction
choose: diagnostic value
damage: avoid destructive, irreversible, security/privacy-compromising, or recklessly high-blast-radius action; isolate risk when practical; stop if meaningful damage cannot be avoided
authorization: installs allowed; ask only if runtime requires or damage boundary crossed
remediate: no; evidence collection != disguised fix
```

Pass problem + profile and, when tool choice needs context,
`references/probe-selection.md`. Core owns loop/report. Preserve independent roles.
