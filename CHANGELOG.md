# Changelog

## 0.4.0-rc.3

- Deliver code behaviors in working vertical slices, preserving shared seams and proven behavior. Pair edits with their checks when the tool supports sequential execution.
- Recheck the evidence behind a suspected QA defect before requesting repair.

## 0.4.0-rc.2

- Keep live linked skill names unprefixed in Codex by defining the Claude plugin in its marketplace entry with strict:false. Preserve the simon-skills package identity and existing marketplace skill selection. Standalone --plugin-dir loading of this repository no longer has a plugin.json definition; use marketplace installation for Claude Code.
- Resolve discovery depth from consequential unknowns, preserve the requested destination through intermediate deliverables, and obtain a human decision before committing to material outcome reductions.
- Ground quality criteria in demonstrated leading practice and remove the remaining routine maintainability signal from QA.

## 0.4.0-rc.1

- Extend Waydriver discovery and acceptance to non-software outcomes, retaining software implementation capabilities. Resolve consequential intent before choosing surgical execution.
- Preserve outcome and comparative-quality requirements, distinguish evidence from hypotheses, and investigate delivery capabilities before accepting material concessions.
- Bind tracker destinations and visibility; preserve source commitments, existing work and superseded decisions.
- Add explicit display names for the Waydriver family. Plugin identity remains simon-skills; no installation namespace migration.

## 0.3.0-rc.3

- Recognize Smart Shot’s second-generation orchestration and Dig Deeper’s STR lineage with component version 2.0.0. Earlier tags remain unchanged; this corrects version baselines without changing skill instructions.
- Reserve GitHub Releases for major changes and selected milestones. Routine updates use tags and changelog entries.

## 0.3.0-rc.2

- Introduce independent component versions and immutable component tag names in the schema-v2 catalog. Coupled skills share a release unit; collection and plugin versions still match.
- Establish initial component versions. No skill instructions change in this release.
- Move repository checks to utilities/validation/ and validate every cataloged skill without a fixed family name or member count.
- Document both live symlink testing and pinned installation/rollback.

Catalog consumers: schema 2 uses `releaseUnit` and `releaseUnits` instead of `family`.

## 0.3.0-rc.1

First versioned preview of the Markdown SFLO Waydriver family.

- Add the conductor and six reusable capabilities: discovery, implementation, QA, security, slop review, and rendered-interface checking.
- Use permanent skills/<name> paths and a maturity catalog. Point the Way retains its original source path and is classified as arena, outside the stable plugin list.
- Require fresh independent acceptance, complete executable evidence, and explicit coverage. Allow independent QA/security to run in parallel against a frozen candidate.
- Remove the mandatory maintainability verdict. Keep proportional architecture guidance in the builder.
- Correct QA probe expectations for required rejection and require control evidence; contradictory assertions cannot justify acceptance or repair.

Compatibility: existing installed snapshots remain unchanged. The new family is experimental and explicitly installed; existing stable plugin skills remain selected. No automatic update or per-skill release resolver is introduced.
