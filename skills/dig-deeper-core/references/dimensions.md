# Dig Deeper Dimensions

Pass threshold: all dimensions >= 0.7. Impact may pass at 0.6 only when all other dimensions are >= 0.8 and the Interrogator justifies the exception. An authority violation always prevents PASS.

## Evidence (0.30)

Every claim is backed by collected, verifiable data.

- 0.0-0.3: Most claims unsupported.
- 0.4-0.6: Mix of evidence-backed and assumed claims.
- 0.7-0.8: All major claims have evidence; minor gaps remain.
- 0.9-1.0: Every claim has numbered, sourced, timestamped evidence.

## Root Cause (0.25)

The report identifies actual cause, not symptoms.

- 0.0-0.3: Symptoms only.
- 0.4-0.6: Plausible hypothesis; alternatives not ruled out.
- 0.7-0.8: Strong hypothesis with evidence chain; major alternatives ruled out.
- 0.9-1.0: Confirmed causal path with alternatives disproven.

## Reproducibility / Verifiability (0.20)

The report explains when and why the problem occurs from evidence collected within the supplied authority profile.

- 0.0-0.3: No condition understanding.
- 0.4-0.6: Some conditions identified, incomplete.
- 0.7-0.8: Conditions well-characterized from evidence.
- 0.9-1.0: Triggers, frequency, conditions, and stopping conditions are fully characterized from evidence.

## Impact (0.10)

Blast radius is understood.

- 0.0-0.3: Unknown or vague.
- 0.4-0.6: Incomplete frequency, affected population, or severity.
- 0.7-0.8: Clear scope, frequency, severity, and workarounds.
- 0.9-1.0: Full user/system impact, degradation/outage distinction, and workaround status.

## Resolution (0.15)

Fix guidance states the evidence-backed change required at the root cause and how to verify it.

- 0.0-0.3: Missing or vague fix.
- 0.4-0.6: Targets a symptom, or is not evidence-backed.
- 0.7-0.8: States the required root-cause change and verification.
- 0.9-1.0: Also identifies material constraints and unresolved implementation choices.

If evidence is insufficient for an evidence-backed fix, score Resolution conservatively and require an unresolved finding with next probes.
