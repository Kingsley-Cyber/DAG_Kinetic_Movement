# CPCS JSON Schemas

Schemas use JSON Schema Draft 2020-12. Relative references in `canonical_scene.schema.json` resolve within this directory. Validation is structural; semantic validators additionally check temporal order, phase coverage, contact causality, unit completeness, adapter freshness, and graph provenance.

Do not weaken `unevaluatedProperties: false` to accommodate an undocumented model response. Save provider response separately, update the adapter snapshot, and explicitly map new fields.
