# Experiment and Ablation Plan

## Status

The experiment program is **designed but not run**. No authorized provider credentials, generation budget, local model weights, or human rating panel were supplied in this session. The package therefore reports no provider-specific success distributions and invents no universal capacity limits.

## Campaign sequence

1. **Evaluator calibration first.** Build a small human-adjudicated set containing the exact failure families. Do not allow an uncalibrated VLM to decide the later experiments.
2. **Low-cost provider/interface qualification.** Capture exact model IDs, endpoint schemas, prompt/rewrite settings, durations, resolutions, references, seeds, audio, outputs, and costs.
3. **Occlusion and state campaign.** Run the water-splash fixture and a non-fluid opaque-control fixture to distinguish hidden-state failure from material complexity.
4. **Serialization campaign.** Hold canonical meaning constant and compare formats, including duplicated hybrids.
5. **Capacity staircases.** Estimate provider/task-specific action/dependency/camera/effect thresholds.
6. **Control and decomposition.** Compare wording, state contracts, visual controls, source/video edit, shot splits, and postproduction.
7. **Repair campaign.** Use retained failed artifacts and isolate one repair intervention at a time.
8. **Immutable recording and reflection.** Admit only lineage-complete runs, then derive provider/model-conditioned mitigation rankings.

## Fixtures

| File | Experiment | Primary independent variable | Primary outcome |
| --- | --- | --- | --- |
| experiments/01_occlusion_continuity.yaml | Occlusion continuity and water-splash hidden state | no occlusion; partial occlusion; complete opaque occlusion; visibility bridge; structured state and path; pose/point/depth path; decomposition/post | metric_hidden_path_consistency, metric_occlusion_reappearance_region_error, metric_actor_count_consistency |
| experiments/02_format_semantic_equivalence.yaml | Prompt serialization semantic-equivalence ablation | serialization only; serialization only; serialization only; serialization only; duplicate representation; triple duplication; adapter-specific compression | metric_prompt_semantic_equivalence, metric_field_projection_coverage, metric_hard_lock_retention |
| experiments/03_action_density.yaml | Provider-specific action-density staircase | action count=1; action count=3; action count=5; maximum planned sequence; shot decomposition | metric_action_graph_agreement, metric_action_omission_rate, metric_primary_action_completion |
| experiments/04_spatial_control.yaml | Spatial control and coordinate-frame ablation | unqualified spatial prose; screen-relative state; numeric screen regions; visual layout; time-varying spatial control; decomposition | metric_screen_direction_consistency, metric_depth_order_accuracy, metric_trajectory_target_error |
| experiments/05_causality.yaml | Causal-event representation ablation | compressed semantics; explicit order; explicit cause/dependency/reaction; visual cause/effect anchors; postproduction consequence | metric_causal_edge_agreement, metric_effect_origin_error, metric_reaction_latency |
| experiments/06_repair_strategy.yaml | Full regeneration versus localized repair | regenerate entire artifact; text-only interval repair; first/last accepted frames; decomposition; deterministic finishing; model/provider | metric_state_transition_accuracy, metric_identity_continuity, metric_environment_layout_consistency |
| experiments/07_identity_state.yaml | Identity, role, object permanence, and state-ledger ablation | no persistent ledger; identity/role contract; count/possession/state transitions; visual identity anchors; time-varying possession; decomposition | metric_identity_continuity, metric_role_assignment_accuracy, metric_object_count_consistency |
| experiments/08_evaluator_calibration.yaml | Failure-aware evaluator calibration | aggregate semantic evaluator; scene-graph assertions; numeric evidence; semantic + measured + human conflict policy; reference authority | metric_evaluator_calibration, metric_human_agreement, metric_false_positive_rate |

## Required repeated-seed design

- Initial screen: at least 20 completed outputs per arm/provider; 30+ for local/open workflows when affordable.
- Use paired seeds where supported and retain provider sample/retry identifiers everywhere.
- Randomize arm order; do not run one arm only during a different service/version window.
- Record provider/model/version/interface, region, request, prompt, prompt rewrite, seed, references, masks/control assets, duration, aspect ratio, resolution, FPS, cost, latency, safety/filter status, and output hash.
- Retain all outputs. The primary analysis may not choose the best candidate from a larger private pool.
- Human raters are blind to arm and provider where practical.
- Pre-register critical assertions; aggregate aesthetic quality is secondary.

## Outcomes

Binary critical success requires every critical assertion to pass. Continuous error metrics remain visible even when the binary verdict fails. Report:

```text
per-seed verdicts
success proportion and Wilson interval
continuous error distributions and bootstrap intervals
first-divergence frames/intervals
evaluator-human confusion and disagreement
cost and latency distributions
collateral failure rates
provider/model/version and date
```

## Promotion rule

A mitigation may become a derived recommendation only from evidence-complete isolated comparisons. A provider capability profile may change only from reviewed official documentation and live qualification. No experiment automatically promotes curated concepts, changes the canonical score, or grants production authority.
