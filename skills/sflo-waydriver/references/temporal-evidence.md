---
name: temporal-evidence
description: Interpret and present metrics whose windows, observation times, revisions or accumulation rules differ.
---

# Temporal evidence

Use when a decision combines snapshots, rolling windows, cumulative totals, late-arriving data or revised periods.

Establish each consequential measure's temporal contract: the interval when the represented activity occurred, when the value was observed, whether it may revise, whether it is cumulative or rolling, and whether separate values can be added. Keep event/effective time separate from observation or processing time.

Admit a comparison only when its populations, interval grain, finality and update rules support the claimed operation. Derive interval increments from cumulative snapshots before describing pace. Do not add overlapping rolling windows. For a revised period, use the latest compatible version for a current comparison and show that the revision changed knowledge about the old period rather than creating new activity. Preserve unavailable finality instead of treating a provisional value as fixed.

Build the representation around the operator's time question. Make compatible values directly comparable and visually separate values that answer another time question. Label effective interval and as-of/finality close to the marks or values they qualify. Show revision history when it changes the decision. Retain exact supporting values without forcing the reader to reconcile clocks across distant panels or recommendation prose.

Test the rendered artifact by asking the intended reader to distinguish new activity, accumulation, rolling-window movement and retrospective revision; identify the comparison that can trigger action; and recover its arithmetic. If the distinction exists only in a caveat, revise the representation. Do not add time machinery when every measure already shares one fixed, final interval.

Return causal questions unresolved unless the evidence establishes them.
