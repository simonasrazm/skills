---
name: dig-deeper
description: Evidence-first, gentle troubleshooting for difficult problems. Use when the user asks for a deep diagnosis, root-cause investigation, or challenge to assumptions without harmful or durable effects.
---

# Dig Deeper

Run `dig-deeper-core` with:

```markdown
profile: GENTLE
objective: gather evidence needed for diagnosis without harmful or durable effect
allow: any useful method within the effect boundary; acquire missing capability only without harmful or durable effect
deny: harmful/irreversible/security/privacy-compromising action; target/system durable change; submit; persistent config; restart
choose: rank available methods by expected discrimination and effect; run best permitted first; if blocked, unblock/acquire within boundary; weaker fallback only if best remains unavailable or insufficient
computer: first only when rendered/manual state is itself evidence
escalate: stop -> suggest dig-deeper-probe; never auto
remediate: no
```

Pass problem + profile. Core owns loop/report. Preserve independent roles.
