# Previous SFLO Project Migration

When durable project knowledge from an earlier SFLO structure exists, migrate it before producing parallel documentation.

Inventory the durable material and its current readers. Move knowledge into the project's established documentation convention when one exists. Otherwise use one coherent `docs/` tree: product and operational knowledge remain ordinary project documentation; lasting decisions are classified as product or architecture records.

A product decision governs behavior, features, content, UX, or business rules. An architecture decision governs technical structure, platform, data, integration, security boundary, scalability, or operational qualities. A decision lives in one record and maps or issues point to it rather than restating it.

Preserve meaningful hierarchy, provenance, and links. Confirm the destination covers the source and update known pointers before retiring migrated material. Ambiguous or still-consumed material remains with a migration note rather than being silently lost. Existing operational run state remains in place; new Waydriver effort state uses the configured tracker or `.scratch/<effort>/` fallback.
