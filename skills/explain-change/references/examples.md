# Examples, not templates

## Bounded verification repair

**Fixed the verifier: one failed check no longer hides later results.**

Media library → local command verification → evidence for repair/review

```diff
   Setup + import succeed; checks run in sequence
-  List fails → stop → search/export never checked
+  List fails → record failure → check search/export
   Any failed check → whole run FAILS
```

This explains a representative control-flow repair, not a product fix. No decision or action section is needed if none exists.

## Process change with a recorded decision

**Routine requests no longer wait for the monthly meeting.**

Requester → operations intake → approval

```diff
-  Every request waits for the monthly meeting
+  Routine requests use delegated approval
   Exceptions still require the meeting
```

Decision: the recorded delegation policy replaces the previous all-requests policy; link the real records and explain the scope. Do not invent a threshold or authorization from this example.

## An action that matters

“Owner decision needed: this change removes the old recovery route. Confirm the replacement recovery procedure before proceeding.” Include the actual affected scope and decisive evidence. Reversibility labels alone would not explain the action; a costly but reversible operation can also need attention.

## Research correction

**The apparent rise came from broader reporting coverage.**

Reader → trend report → interpretation of change

```diff
- Compare totals from different reporting populations → apparent rise
+ Compare the same reporting population → no rise observed
  The broader population remains outside this conclusion.
```

Illustrative only: the actual evidence must support both the correction and its scope.

## Presentation restructuring

**The audience sees the decision before the supporting detail.**

Leadership audience → proposal presentation → funding decision

```diff
- Background → methods → findings → requested decision
+ Requested decision → options and trade-offs → supporting findings
  The underlying findings and requested funding are unchanged.
```

This reports a change in explanation order, not proof of improved audience understanding.
