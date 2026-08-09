# Derived Weights and Learning

## Eligible derived artifacts

- model-specific canonical-to-prose phrase weights;
- native/reference/prompt control success estimates;
- failure probabilities by action, contact density, duration, camera, and style;
- calibration models for automatic metrics versus human judgments;
- retrieval/reranking models over examples;
- adapter loss estimates;
- recommended repetition/seed budgets.

## Lineage

Every artifact stores:

```json
{
  "derived_id": "dw_runway_gen45_contact_v3",
  "input_experiment_query": "...",
  "input_manifest_sha256": "...",
  "code_git_commit": "...",
  "environment_lock_sha256": "...",
  "training_parameters": {},
  "metrics": {},
  "created_at": "...",
  "supersedes": "..."
}
```

## Guardrails

Derived weights cannot rename an AU, redefine an LMA factor, or alter a source claim. They influence candidate selection and compilation. Negative or surprising results remain in the training set unless a documented data-quality rule excludes them.

## Promotion

A learned pattern becomes a curated convention only after held-out replication, effect-size/confidence reporting, and review. The promoted rule cites the derived artifact and experiment set.
