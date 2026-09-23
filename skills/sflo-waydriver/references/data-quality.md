# Data-quality expertise

Apply DAMA-DMBOK to the fitness of data for its intended use. Establish the decisions, critical data, quality requirements and assessment scope from project evidence and discovery.

## Data fitness

Use DAMA’s nine dimensions below to identify applicable quality requirements. Define each consequential check against the intended use: population or sample, rule, denominator, threshold and evidence source. Mark unmeasured dimensions unknown and explain inapplicability.

| Dimension | Observable question |
|---|---|
| Accuracy | Do values agree with independent truth or an agreed authoritative source? |
| Completeness | Are the expected population, records and required fields present? |
| Consistency | Do representations agree across records, systems and time under the same definitions? |
| Integrity | Do relationships, keys and cardinalities hold, including orphan references? |
| Timeliness | Is data available by the decision or processing deadline? |
| Currency | Does data represent the latest relevant state at its required effective time? |
| Reasonableness | Do values and distributions fit evidence-backed expectations for this use? |
| Uniqueness | Is each intended entity or event represented once at the declared grain? |
| Validity | Do values satisfy their domains, formats and business rules? |

Extend these with use-specific requirements such as measurement precision, accessibility or privacy when they affect fitness. Keep precision and rounding tolerances explicit where decisions depend on them. Separate relationship integrity from protection against unauthorized changes. Dimensions overlap: give each defect one identity, map its affected dimensions and count its impact once. Passing validity checks establishes rule compliance; accuracy still needs truth evidence.

Profile accessible data and reconcile consequential transformations with their sources. Report observed scope and uncertainty alongside results.

## Management capabilities

Assess practices separately from measured data fitness: a mature process can produce bad data, and a good sample can come from fragile practices. For a current-state assessment, examine every knowledge area below. Record each area's applicability, observed practices, operating level, supporting evidence and effect on data quality. A missing document leaves a question; establish absence through evidence. Distinguish a declared policy or installed tool from a practice demonstrated in operation. Explain any area judged inapplicable.

| Knowledge area | Evidence to examine for the quality assessment |
|---|---|
| Data governance | Who defines quality, resolves disputed meanings and owns remediation; decisions actually carried out |
| Data architecture | Critical source-to-consumer paths, dependencies and quality boundaries |
| Data modeling and design | Entity meaning, grain, keys, units, relationships and temporal rules |
| Data storage and operations | Availability, recoverability, retention and operational incident evidence |
| Data security | Integrity protections, change authority and traceability of data modifications |
| Data integration and interoperability | Reconciliation, loss or duplication, schema changes and delivery timing |
| Document and content management | Quality of unstructured inputs, extraction, versioning and provenance |
| Reference and master data | Shared identifiers, authoritative values, matching and conflict resolution |
| Data warehousing and business intelligence | Published metric definitions, transformations and consumer-visible consistency |
| Metadata management | Definitions, ownership and lineage that can actually be followed |
| Data quality management | Measured defects, coverage, thresholds, alerts, root-cause repair and recurrence |

Use the project's established maturity rubric. Where none exists, describe whether practice is ad hoc, documented, repeatable or measured, and cite the observation supporting that description. These are descriptive states, not an official DAMA maturity score. Keep unknowns separate from weak or absent capabilities.

Deliver an evidence-backed assessment across the areas, the measured quality status and a prioritized improvement path. Connect each priority to its business effect, responsible owner and observable acceptance. For a bounded quality repair, investigate the areas that explain its cause and verify the affected quality outcome; a full organizational assessment belongs to a current-state assessment request.

Framework: [DAMA-DMBOK knowledge areas](https://www.damadmbok.org/copy-of-about-dama-dmbok). The evidence prompts and descriptive operating states above are this skill's assessment guidance, not a certification rubric.

Dimensions: [DAMA-DMBOK2 revision](https://www.damadmbok.org/dmbok2-revisions). The checks above operationalize the dimensions; they are not an exhaustive or mutually exclusive taxonomy.
