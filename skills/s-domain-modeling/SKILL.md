---
name: s-domain-modeling
description: Build and sharpen a project's domain model. Use when domain terminology, relationships or rules change, when writing or editing a GLOSSARY.md, or when recording or editing an ADR.
---

# S Domain Modeling

Actively build and sharpen the project's domain model as you design. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing the glossary and decisions down the moment they crystallise. (Merely *reading* `GLOSSARY.md` for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

Resolve apparent conflicts against accepted decisions and available evidence. Ask the person when consequential interpretations remain unresolved; keep pending interpretations out of accepted definitions. Use the project’s existing glossary and decision-record conventions; the formats below are defaults when none exist.

When legacy `CONTEXT.md` or `CONTEXT-MAP.md` files exist, read [glossary migration](GLOSSARY-MIGRATION.md) before creating or moving a glossary. The names below are defaults, not an instruction to replace an established project convention.

## File structure

Most repos have a single context:

```
/
├── GLOSSARY.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `GLOSSARY-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── GLOSSARY-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── GLOSSARY.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── GLOSSARY.md
│       └── docs/adr/
```

Create files lazily: only when you have something to write. If no `GLOSSARY.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `GLOSSARY.md`, surface the discrepancy and reconcile it against accepted decisions. If the intended meaning remains unresolved, ask: "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and establish precise boundaries between concepts. Ask the person when the remaining boundary depends on their unresolved intent.

### Cross-reference with behavior

When the user states how something works, check whether the code or operational evidence agrees. If you find a contradiction, surface it and reconcile it against accepted decisions; ask when the intended rule remains unresolved: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

### Update GLOSSARY.md inline

When a term is resolved, update `GLOSSARY.md` right there. Don't batch these up: capture them as they happen. Use the format in [GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md).

`GLOSSARY.md` should be totally devoid of implementation details. Do not treat `GLOSSARY.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).

Link each lasting decision to its originating unit or task slug and link the changed records from that task. For an accepted change, update the existing decision record at its stable path and align affected documentation, current requirements and glossary. Record current accepted direction separately from implementation still pending; verify that the prior accepted state is recoverable in version history before replacing it, recording any history gap before proceeding. Preserve the reason, decision owner and supporting evidence; distinguish agent assumptions from human decisions.

Adapted from Matt Pocock’s domain-modeling skill. The bundled MIT license and repository maintenance metadata preserve attribution and pinned upstream provenance.
