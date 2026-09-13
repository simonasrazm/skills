# Contributing

Focused improvements and reproducible defects are welcome.

Before opening a pull request:

- Explain the user situation the skill should handle.
- Show the current behaviour and the proposed change.
- Preserve explicit authority, safety and verification boundaries.
- Include evidence that the new wording improves routing or runtime behaviour when behaviour changes.
- Run the checks listed in [utilities/validation/](utilities/validation/).

Keep pull requests small enough to review. A shorter prompt, a stronger claim or a model's approval is not evidence by itself.

The catalog owns release-unit versions; coupled skills version together. Use patches for compatible fixes, minors for compatible additions, and majors for incompatible contracts. Keep unsettled contracts below 1.0. Record changes and evidence in CHANGELOG.md. Tag the collection as `v<version>` and changed units as `<unit>/v<version>`; reserve GitHub Releases for milestones.
