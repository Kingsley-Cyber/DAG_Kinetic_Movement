# Graph Seed Ingestion

## Neo4j shape

Create unique constraints on `Entity.entity_id` and `Relation.relation_id`. Load all entities first, then relations. Convert selected types to labels (`Topic`, `Source`, `Claim`, `CreativeIntent`, `InteractionPredicate`, `ModelAdapter`) after ingestion if desired.

```cypher
CREATE CONSTRAINT entity_id IF NOT EXISTS FOR (n:Entity) REQUIRE n.entity_id IS UNIQUE;
```

Each JSONL relation is reified during import or converted to a typed edge. Reification is recommended when relation attributes/provenance are important.

## Tier

This seed is Curated. Experiments and derived weights belong in separate labels/partitions with immutable lineage. Do not merge a Derived recommendation into a source claim because their text is similar.
