# Changelog

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
