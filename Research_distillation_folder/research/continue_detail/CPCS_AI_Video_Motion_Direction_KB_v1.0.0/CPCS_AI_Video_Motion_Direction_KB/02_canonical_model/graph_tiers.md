# Three-Tier Knowledge Graph

## Curated

Git-versioned definitions, source claims, schemas, controlled vocabulary, mappings, adapter contracts, and reviewed examples. Curated records can change only through a reviewable commit with provenance and migration notes.

## Immutable

Append-only experiment records. Each experiment captures exact model/endpoint, adapter version, prompt/request, references, seed when provided, output hashes, evaluator annotations, costs/latency, and environment. Corrections create a new record linked with `supersedes`; they do not overwrite history.

## Derived

Learned weights and statistics computed from immutable experiments: model-specific prompt weights, failure likelihoods, preferred phrase mappings, control-loss estimates, and calibration models. Every derived artifact stores the input experiment query/hash, code version, parameters, and metrics.

## Promotion

A derived pattern may be proposed as a curated convention only after reproducibility across held-out experiments and human review. Promotion copies a reviewed proposition into Curated with links to evidence; it never moves or edits the immutable observations.

## Example graph path

`CreativeIntent(protect) → candidate MotionPrimitive(shield) → HAS_PHASE → ContactEvent → CameraShot → COMPILED_FOR Adapter(runway_act_two_vX) → EVALUATED_IN Experiment(exp_...) → DERIVED_FROM Weight(weight_...)`
