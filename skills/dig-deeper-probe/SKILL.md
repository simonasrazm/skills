---
name: dig-deeper-probe
description: Diagnose nasty, deep bugs when observation is not enough. Use when tools, safe reproduction and controlled experiments are needed to find the cause. Tool installation follows the user's consent or established execution boundary. Diagnosis only, never remediation.
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
authorization: acquire or install tools within the user's explicit consent or established execution boundary; when neither covers the proposed installation, explain the tool, purpose and scope of changes and obtain consent first; honor runtime approval requirements
remediate: no; evidence collection != disguised fix
```

Pass problem + profile. Core owns loop/report. Preserve independent roles.
