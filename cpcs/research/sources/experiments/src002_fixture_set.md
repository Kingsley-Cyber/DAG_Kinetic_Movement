---
id: cpcs.verification.src002_fixture_set
kind: fixture_set
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 §25, L2.§53, L2.§35]
primary_route: cpcs/research/sources/experiments/
secondary_routes:
  - cpcs/verification/facs/
  - cpcs/verification/performance/
---

# SRC-002 Fixture & Minimal-Pair Corpus

## Layer-1 fixtures (SRC-002 §25)

```text
facs/
  au12_bilateral_b · au12_left_c_right_b · au7_vs_au6_confusion ·
  au23_vs_au24_confusion · au12_temporal_overlap_au6 ·
  legacy_41_version_rejection · legacy_44_version_rejection ·
  occluded_left_eye · missing_timestamp · detector_presence_intensity_disagreement
laban/
  effort_strong_sudden_direct_free · effort_light_sustained_indirect_bound ·
  shape_spread_rise_advance · phrasing_beginning · phrasing_middle · phrasing_end ·
  directness_proxy_uncalibrated · cross_subject_normalization_required
bartenieff/
  breath_inhale · breath_exhale · core_distal_expand · core_distal_condense ·
  head_tail · upper_lower · body_half_left · body_half_right · cross_lateral ·
  connectivity_unknown
integration/
  restrained_dialogue · explosive_action · stylized_anime ·
  unsupported_facs_provider · semantic_only_provider · bilateral_loss
```

## Layer-2 fixtures (SRC-002 L2.§53)

```text
facs_laterality_minimal_pair · facs_intensity_minimal_pair · facs_temporal ·
laban_effort_minimal_pair · laban_shape_minimal_pair · laban_phrase ·
bartenieff_connectivity · body_topology · cross_framework_timing ·
causal_performance · occlusion_continuity · multi_actor_response ·
provider_fallback · attention_budget · observability
```

## Fixture invariant (L2.§53)

Every fixture must identify: canonical target · source/evidence basis ·
expected realization · forbidden realization · provider projection ·
verification metric · expected failure class.

## Minimal-pair requirement (L2.§35)

`same action/actor/camera/scene · one semantic variable changed · expected
visible difference`. Examples: AU12 lower-vs-higher ordinal; bilateral vs
left-dominant; Strong vs Light; Cross-Lateral vs Body-Half. Measures action
identity preserved · trajectory preserved · timing preserved · visible
quality difference.
