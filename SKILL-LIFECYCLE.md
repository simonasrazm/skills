# Skill lifecycle

Every skill has a permanent source path at `skills/<name>/`. Maturity is recorded in `skills.catalog.json` as `arena`, `stable`, or `deprecated`. Promotion changes metadata and installation catalog membership, never paths or names. Maturity and version are separate: an established skill can retain stable discovery while its new version contract starts below 1.0.

## Versions and releases

The catalog is the version source of truth. Each skill identifies a release unit and its version; related skills with coupled references share one unit. Other skills advance independently. The collection version matches the plugin manifest and identifies the complete installation catalog. Updating one skill does not advance unrelated skill versions.

Use patch releases for compatible corrections, minor releases for added capabilities, and major releases for incompatible names, contracts, or installation changes. Before 1.0, incompatible changes increment the minor version and are called out explicitly. Preview releases append `-rc.N`. A collection release does not automatically promote arena skills.

Tags identify immutable repository commits:

- `v<version>` identifies a collection snapshot.
- `<release-unit>/v<version>` identifies a component release, for example `smart-shot/v2.0.0`.

A component tag still points to a complete Git commit. Its promise covers only the catalog members of that release unit. Never move a published tag. If any member's contract changes, increment the unit version and publish a new tag. A catalog-only collection release can reference unchanged component versions. `CHANGELOG.md` records changes and verification; [VERSIONING.md](VERSIONING.md) records the initial history-based version decisions.

GitHub Releases are curated milestone notes attached to tags. Create them for major changes or another explicitly selected milestone; routine fixes and minor updates need only version tags and changelog entries. A major change can be worth a Release even when it is a SemVer minor increment. No uploaded archives are required; GitHub generates source zip/tar downloads automatically. No release resolver or automatic updater is installed.

## Live development and pinned use

For immediate testing, symlink each selected skill directory from a development checkout into the harness skill directory. For Codex that directory is `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`. Back up existing copies before replacing them. Editing the source updates what the symlink resolves to immediately; a task that already loaded instructions may need to reload them or start fresh. A dirty development checkout is ahead of its catalog version: record its commit and diff when comparing experiments.

For reproducible use, clone a tag into a retained directory and link the selected release unit's members from there:

```sh
git clone --branch smart-shot/v2.0.0 --depth 1 https://github.com/simonasrazm/skills.git skills-smart-shot-v2.0.0
```

Select members from `releaseUnits` in that checkout's catalog. For a coupled unit, update or roll back every member together, preserving references and bundled licenses. Record the tag and commit SHA. Retain the old checkout; rollback repoints the links to it. Do not update a pinned checkout in place.

The plugin's explicit skill list controls its stable selection. Other installers may discover every skill, so select arena skills explicitly.

## Publishing and promotion

Before publishing, update changed unit versions and matching skill entries, advance the collection/plugin version, update release notes, and run the checks in `utilities/validation/`. Tag the verified commit with the new collection tag and only the component tags whose versions are new. Preserve existing component tags for unchanged units.

Promote a skill after real-project evidence supports its acceptance behavior and cost. Record limitations, change maturity, and include it in the stable plugin list if appropriate. Promotion is a separate decision from version numbering.
