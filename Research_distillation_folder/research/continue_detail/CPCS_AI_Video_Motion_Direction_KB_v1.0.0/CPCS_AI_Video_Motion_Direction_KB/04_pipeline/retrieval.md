# Retrieval Design

## Indexes

1. **Source/claim index:** authoritative evidence and locators.
2. **Concept index:** canonical entities, synonyms, and distinctions.
3. **Example index:** canonical scenes and prompt compilations.
4. **Experiment index:** immutable summaries filtered by model/adapter/version.
5. **Failure index:** diagnosed failure patterns and fixes.

## Query plan

- Parse user intent, action, actors, style, camera, target model, and constraints.
- Retrieve definitions and constraints from Curated.
- Retrieve comparable examples and experiments filtered to current adapter/model.
- Expand through graph relations such as intent→realization, primitive→phase, predicate→contact, and adapter→capability.
- Rerank for task match, evidence quality, freshness, and constraint compatibility.
- Return compact evidence bundles to the planner/compiler.

## Tier isolation

Curated facts and Derived recommendations must be distinguishable in retrieval. An experiment-derived prompt phrase cannot appear as a source-defined Laban term. Result objects carry tier, source IDs, version, and confidence.

## Suggested local implementation

Qdrant stores embeddings of parent summaries/claims/examples/experiment summaries; MongoDB hydrates full records and exact fields; Neo4j traverses ontology, evidence, interaction, and lineage. Filter by `tier`, `cpcs_version`, `model_id`, `adapter_version`, `verified_at`, and rights.
