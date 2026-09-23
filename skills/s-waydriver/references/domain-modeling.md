# Domain modeling

Resolve the concepts the work depends on against the project’s glossary, actual behavior and accepted requirements. Follow existing context boundaries; use CONTEXT-MAP.md to locate scoped glossaries when present. An overloaded term needs a precise context-specific meaning, not a forced global definition.

Test proposed meanings and relationships with concrete boundary and counterexample scenarios. Compare stated rules with the implementation or operational evidence. Resolve contradictions from authoritative decisions and evidence; when consequential interpretations remain possible, ask the person before committing dependent changes. Keep pending interpretations out of accepted definitions.

Capture resolved terms as they crystallize in the existing glossary. If none exists, create CONTEXT.md when the first term is resolved: context name, short purpose, then a Language section with concise definitions and misleading synonyms to avoid. Keep the glossary about domain meaning; put implementation choices and current requirements in their respective records. Preserve existing multiple contexts and their relationships.

Record lasting choices under the project’s decision convention. Create a new architecture record when the choice has meaningful reversal cost, would surprise a future reader without context, and resolves a real trade-off. Keep the reason and consequence explicit; corrections to existing records retain their history. A short paragraph is sufficient. Respect existing docs/adr/ paths and numbering; otherwise follow S Waydriver’s decision-record convention. Link the originating unit, evidence and affected requirements. In standalone work, use the existing task identity or a stable task slug tied to the accepted request; this requires no execution-run artifact. Accepted replacements update current requirements and mark older decision records superseded with a replacement link.

Adapted from Matt Pocock’s domain-modeling skill; upstream provenance and adaptation boundaries are recorded in the repository’s maintenance metadata.
