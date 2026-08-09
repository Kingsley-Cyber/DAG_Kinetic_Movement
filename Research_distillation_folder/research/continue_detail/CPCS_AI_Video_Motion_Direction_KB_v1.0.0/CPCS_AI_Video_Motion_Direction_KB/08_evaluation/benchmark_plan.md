# CPCS Benchmark Plan

## Goal

Measure whether CPCS improves controllability and auditability over unstructured prompts across scene families and model surfaces.

## Conditions

1. **Baseline prose:** competent natural-language prompt with no CPCS compilation.
2. **CPCS prose-only:** canonical planning compiled to text.
3. **CPCS native/reference:** uses documented controls and references.
4. **Ablations:** remove BESS/body, phases, contact topology, camera, style invariants, or derived weights.

## Scene families

- single-actor gesture/emotion;
- everyday person-object interaction;
- two-person social interaction;
- staged combat exchange;
- dance/music alignment;
- UGC product interaction;
- stylized/anime action;
- camera-dominant action;
- long multi-beat sequence.

## Sampling

Use at least five canonical scenes per family, multiple seeds/repetitions per condition, and model-specific feasible durations. Hold canonical content constant across model/condition where possible. Randomize and blind evaluator presentation.

## Primary outcomes

Predicate/action correctness and contact causality are co-primary. Identity, intent, timing, camera, style-invariant preservation, and production usefulness are secondary. Report per-model and pooled effects; do not hide model × scene interactions.

## Statistical/reporting policy

Report sample counts, missing/failed requests, confidence intervals, inter-rater reliability, effect sizes, and all predeclared exclusions. Treat outputs from changed model versions as a new stratum.
