# Previous SFLO Project Migration

When durable project knowledge from an earlier SFLO structure exists, migrate it before producing parallel documentation.

Inventory the durable material and its current readers. Move knowledge into the project's established documentation convention when one exists. Otherwise use one coherent `docs/` tree: product and operational knowledge remain ordinary project documentation; lasting decisions are classified as product or architecture records.

A product decision governs behavior, features, content, UX, or business rules. An architecture decision governs technical structure, platform, data, integration, security boundary, scalability, or operational qualities. A decision lives in one record and maps or issues point to it rather than restating it.

Preserve meaningful hierarchy, provenance, and links. Confirm the destination covers the source and update known pointers before retiring migrated material. Ambiguous or still-consumed material remains with a migration note rather than being silently lost. Preserve earlier runner state and gate artifacts as immutable evidence. Link the originating run identifier and relevant artifact paths from current decision or delivery units, keeping each artifact at its authoritative location. Record ongoing Waydriver state in the configured tracker or `.scratch/<effort>/` fallback. Updating a previous runner is a separate execution path, selected explicitly and performed through that runner.
