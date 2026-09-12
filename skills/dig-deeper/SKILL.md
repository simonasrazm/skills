---
name: dig-deeper
description: Diagnose nasty, deep bugs and failures using logs, system state, documentation, code and other read-only evidence. Use when the obvious explanation is weak, several causes fit, or earlier fixes treated symptoms. Does not change the target.
---

# Dig Deeper

Run `dig-deeper-core` with:

```markdown
profile: GENTLE
objective: gather evidence needed for diagnosis without changing the target
allow: any useful method within boundary; incidental logging/caching allowed
deny: harmful/irreversible/security/privacy-compromising action; target mutation; persistent config; restart
choose: rank available methods by expected discrimination and effect; run best permitted first; if blocked, unblock/acquire within boundary; weaker fallback only if best remains unavailable or insufficient
computer: first only when rendered/manual state is itself evidence
escalate: continue permitted probes; if blocked by boundary, suggest dig-deeper-probe; never auto
remediate: no
```

Pass problem + profile. Core owns loop/report. Preserve independent roles.
