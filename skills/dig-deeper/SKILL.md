---
name: dig-deeper
description: Evidence-first, non-mutating troubleshooting for difficult problems. Use when the user asks for a deep diagnosis, root-cause investigation, or challenge to assumptions without changing the target system.
---

# Dig Deeper

Run `dig-deeper-core` with:

```markdown
profile: GENTLE
allow: read-only/supplied evidence; disposable probes iff no target/durable effect
deny: target/durable change; install; submit; config; restart
escalate: stop -> suggest dig-deeper-probe; never auto
remediate: no
```

Pass problem + profile. Core owns loop/report. Preserve independent roles.
