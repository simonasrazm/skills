# Repository validation

Run from the repository root:

```sh
bun utilities/validation/skill-definitions.ts
bun utilities/validation/release-catalog.ts
bun test ./utilities/validation/release-catalog.test.ts
```

`skill-definitions.ts` checks discovery frontmatter and unique names.
`release-catalog.ts` checks collection/plugin versions, independent release-unit membership and versions, stable plugin selection, catalog coverage, and local Markdown links throughout every cataloged skill.
`release-catalog.test.ts` exercises valid arbitrary units and rejects inconsistent catalogs and broken links.

These are structural publication checks. They do not establish skill outcome quality or replace behavioral experiments.
