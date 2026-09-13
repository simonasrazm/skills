# Skill lifecycle

Every skill has a permanent source path at `skills/<name>/`. Maturity is recorded in `skills.catalog.json` as `arena`, `stable`, or `deprecated`. Promotion changes metadata and installation catalog membership, never paths or names.

## Versions and releases

All skills share one repository SemVer version. The catalog and plugin manifest carry the same version. Waydriver's seven components are released and installed together; they have no independent version counters.

Use patch releases for compatible corrections, minor releases for added capabilities, and major releases for incompatible names, contracts, or installation changes. Before 1.0, incompatible changes increment the minor version and are called out explicitly. Preview releases append `-rc.N`, starting with `v0.3.0-rc.1`. Preview status does not demote existing stable skills, and a stable repository release does not automatically promote arena skills.

Tags identify immutable commits: never move a published tag. CHANGELOG.md records changed skills, compatibility, and verification. A release's GitHub source archive is the versioned artifact. Maturity metadata is descriptive; the plugin's explicit skill list controls its stable selection. Other installers may discover every skill, so select arena skills explicitly.

## Install a fixed Waydriver family

Clone a release into a retained, version-specific directory:

```sh
git clone --branch v0.3.0-rc.1 --depth 1 https://github.com/simonasrazm/skills.git skills-v0.3.0-rc.1
```

Install these sibling directories from that checkout into your harness skill directory: `sflo-waydriver`, `s-waydriver`, `s-dev`, `s-qa`, `security-check`, `slop-sweep`, and `s-ui-check`. Preserve all references and the bundled license. For Codex the destination is `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`. Back up existing copies before replacing them. Record the tag and commit SHA with the installation.

Updates are explicit: install the complete family from another tagged checkout. Retain earlier copies and their revision receipts; rollback restores the whole previous family. Do not mix component revisions or link an installation to a mutable development checkout. Existing pinned installations remain unchanged when source files move or new releases appear.

## Promotion

Promote a skill after real-project evidence supports its acceptance behavior and cost. Record relevant limitations, change its maturity, include it in the stable plugin list if appropriate, and publish a new release with matching catalog and plugin versions. A correction after publication always receives a new version.

There is no automatic updater. Releases and retained snapshots provide explicit installation, comparison, and rollback.
