# CPCS Pipeline Architecture

## Objective

Convert creative intent into a canonical scene, validate it, downcast it to one or more AI-video model surfaces, generate outputs, evaluate them, and feed immutable observations into derived model-specific weights without mutating curated knowledge.

```text
Research sources / expert notes / model documentation
                │
                ▼
      Curated knowledge ingestion
                │
      claims + entities + relations
                │
                ▼
        CPCS planning/compiler
Intent → beats → affect → BESS/body → primitives/phases
      → kinematics/contact/force → rhythm/camera/style
                │
                ▼
      Canonical scene JSON + YAML/XML views
                │
        schema + semantic validation
                │
                ▼
 Capability-aware model adapter(s)
 native controls + references + prose + loss report
                │
                ▼
      Provider generation endpoint/UI
                │
                ▼
 outputs + logs + human/automatic evaluation
                │
                ▼
       Immutable experiment ledger
                │
                ▼
 Derived weights/calibration/failure models
                └──────────────► compiler reranking
```

## Storage lanes

### Curated lane

Git repository: source registry, claims, schemas, ontology, vocabularies, prompt templates, adapters, reviewed examples, and migrations. Every change is human-reviewable.

### Immutable lane

Append-only experiment metadata in a transactional store; video/image/reference assets in content-addressed object storage. Records use hashes, exact model IDs, adapter versions, request payloads, and evaluation data. Corrections append a successor record.

### Derived lane

Versioned tables/models generated from immutable query snapshots: phrase weights, control success rates, calibration curves, retrieval indexes, and model-specific failure predictors. Each artifact records code/environment/input hashes.

## Suggested implementation mapping

The architecture maps cleanly to a local-first stack:

- **Git:** curated Markdown/JSON/YAML/XML and schemas.
- **MongoDB:** hydrated source/claim/experiment documents and raw provider responses.
- **Neo4j:** ontology, claim-source graph, intent-to-realization graph, interaction/contact semantics, and experiment lineage.
- **Qdrant:** source-note, claim, example, and experiment-summary embeddings, filtered by tier/version/model.
- **Object storage:** generated video, references, keyframes, pose tracks, audio, and checksums.
- **Redis/queue:** extraction, compilation, generation, and evaluation jobs.

No database is the sole source of truth. Git controls curated definitions; object hashes and append-only experiment records control observations.

## Control-plane invariants

1. Every generated request points to a canonical-scene hash and adapter version.
2. Every adapter is provider/model/surface/date specific.
3. Every derived weight points to the immutable experiment query used to train it.
4. Unsupported canonical fields remain visible in a loss report.
5. Model output never overwrites canonical intent or source claims.
6. A failed validation blocks generation unless the failure is explicitly waived and recorded.
