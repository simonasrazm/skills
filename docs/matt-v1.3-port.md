# Matt v1.3 glossary port

The public port covers glossary naming and compatible migration only. It compares the previous upstream pin `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` with v1.3.1, `24fe0ef7737efae15c87225755e9f6f5965e4888`. [Maintenance provenance](../utilities/upstream/mattpocock.json) records the source hashes and retained local adaptations.

## Changes

- New projects use `GLOSSARY.md` and `GLOSSARY-MAP.md` instead of the old context names.
- Existing project glossary and decision-record conventions remain authoritative.
- The old `CONTEXT-FORMAT.md` reference remains a compatibility pointer.
- ADRs remain separate; their existing local rules are preserved.

## Migration loading

The detailed [migration reference](../skills/s-domain-modeling/GLOSSARY-MIGRATION.md) is a separate file, loaded when legacy `CONTEXT.md` or `CONTEXT-MAP.md` exists and a glossary is about to be created or moved. Its text is not embedded in the factory entrypoint. The general SFLO migration reference links it conditionally for legacy glossaries.

The reference covers mixed-content preservation, competing vocabulary authority, context boundaries, current readers and historical evidence. Existing application repositories are not bulk-renamed by installing this port. Only the short conditional pointer is part of the domain-modeling entrypoint; actual model loading remains observable runtime behavior, not a zero-token guarantee.

## Evidence and boundary

Fresh isolated skill executions covered new and custom glossary paths, multi-context migration with operations and decision content, genuinely conflicting definitions, and accepted versus implemented ADR state. Independent inspection verified resulting files, links, anchors and preserved content. These bounded cases do not establish universal reliability.

No PR presentation, handover-policy expansion, new assurance dependency or retrospective capability is included in this public port. Local testing tools are not shipped features. Publication remains a separate action.

Primary sources: [pinned domain-modeling skill](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/skills/engineering/domain-modeling/SKILL.md) and [baseline comparison](https://github.com/mattpocock/skills/compare/c55ee46073ed923f86ce59a5eb3b6d895095d1b7...v1.3.1).
