---
id: cpcs.research.benchmark_harness_contract
kind: experiment_design
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007 G016, G017]
primary_route: cpcs/research/sources/experiments/
secondary_routes:
  - cpcs/verification/
  - cpcs/research/gaps/
interfaces:
  - cpcs.adrg.experiments
  - cpcs.experiment.carrier_effect_design
  - cpcs.verification.measurement_record_form
---

# Benchmark and Experiment Harness Contract

> **Source:** SRC-007 G016/G017 — "Benchmark and experiment harness"

## Principle

Benchmarks are construction projects, not afterthoughts. Every gold fixture
must link: canonical target → provider request → output artifact →
observations → metrics → human judgments → failure labels.

## Harness specification

- evaluation unit (explicitly defined);
- split policy (development vs held-out certification);
- annotation schema;
- annotator agreement;
- provider/version snapshot per fixture;
- seed/repeat policy;
- leakage controls;
- negative-result retention (never delete failed runs).

## Minimal falsifying slice

Provide a minimal benchmark slice that can falsify at least one claim from
each of: ScenePlan, temporal, state, contact, compiler-loss, and evaluator.
State which result **blocks implementation** versus which only
**recalibrates a threshold**.

## Required benchmark elements

gold scenes · temporal annotations · state annotations · contacts · causal
graphs · provider outputs · human ratings · repeated A/B · confidence
intervals · effect sizes.

## Verification

`test_gold_fixture_links_complete`,
`test_split_policy_prevents_leakage`,
`test_negative_results_retained`,
`test_falsification_slice_covers_six_claim_classes`,
`test_blocks_versus_recalibrates_classification`.
