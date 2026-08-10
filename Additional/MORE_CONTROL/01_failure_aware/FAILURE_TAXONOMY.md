# Failure Taxonomy

## Taxonomy design

The taxonomy is organized by the **first violated production contract**, not by surface artifact alone. The same visible symptom can have different causes: a teleport may come from an undefined hidden trajectory, an actor-tracker swap, a camera-coordinate error, or a genuine provider failure despite a complete score. Classification should therefore retain symptom, suspected mechanism, evidence lane, and first-divergence interval.

This package defines **96 versioned failure records** in `FAILURE_RECORDS.jsonl`. Each record is schema-valid and contains a provider-neutral failure ID, triggers, symptoms, likely cause, evidence status, canonical paths, prompt risks, mitigations, metrics, regression fixture, owner, confidence, and unresolved questions.

## Families

| ID | Family | Records | Existing owner | Default evidence |
| --- | --- | --- | --- | --- |
| A | Occlusion and hidden-state continuity | 6 | continuity + actions + verification | [B012], [B013], [B014], [B017], [B027], [B028] |
| B | Object permanence and state persistence | 6 | entities + continuity + verification | [B011], [B012], [B015], [B027], [B028], [B042] |
| C | Identity, role, and actor assignment | 6 | entities + interactions + continuity + verification | [B002], [B015], [B027], [B028], [B041], [B042] |
| D | Spatial reasoning and screen geography | 6 | scenes + shots + actions + camera + verification | [B002], [B031], [B035], [B036], [B037], [B040] |
| E | Temporal order and action-graph collapse | 6 | beats + actions + editing + verification | [B003], [B017], [B027], [B029], [B033], [B039] |
| F | Causality and reaction | 6 | actions + interactions + effects + verification | [B004], [B005], [B025], [B027], [B038], [B044] |
| G | Contact, penetration, and interaction geometry | 6 | interactions + motion + camera + verification | [B002], [B004], [B025], [B032], [B038], [B043] |
| H | Balance, support, weight, and momentum | 6 | motion + interactions + verification | [B004], [B005], [B025], [B032], [B044], [B045] |
| I | Fluid, cloth, hair, debris, and material interaction | 6 | interactions + style + continuity + verification | [B004], [B005], [B010], [B025], [B027], [B045] |
| J | Camera and actor-motion entanglement | 6 | camera + motion + shots + verification | [B031], [B035], [B037], [B040] |
| K | Cuts, flashes, smears, and scene reset | 6 | editing + continuity + style + verification | [B003], [B010], [B015], [B027], [B033] |
| L | Anatomy and stylization recovery | 6 | motion + style + performance + verification | [B001], [B016], [B032], [B042] |
| M | Prompt and serialization | 6 | compiler + provider adapter + experiment registry | [R005], [M001], [M002], [M007], [M023], [M025] |
| N | Constraint overload and under-specification | 6 | compiler + loss report + shot planner | [B002], [B003], [B039], [B040], [B043] |
| O | Audio and cross-modal synchronization | 6 | audio + actions + verification | [B022], [B023], [B024], [B046], [M004], [M019] |
| P | Verification and evaluator failure | 6 | verification + immutable evidence + human calibration | [B007], [B008], [B017], [B025], [B029], [B030], [B031], [B033], [B034] |

## Taxonomy invariants

- A failure ID names one stable failure concept; provider/model/version observations attach to it rather than replacing it.
- A visible symptom does not establish a hidden internal cause.
- Official provider capability is not empirical reliability.
- Prompt, canonical contract, visual control, shot decomposition, postproduction, localized regeneration, and provider substitution remain distinct mitigation levels.
- Evaluator failure is a first-class family, not noise to be averaged away.
- No record authorizes a production schema change or curated promotion.

## Complete record index

| Ordinal | Failure ID | Family | Failure | Primary mitigation | Primary metric | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | failure://a/hidden_state_reconstruction/1 | A | Hidden-state reconstruction hallucination | L4 | metric_actor_count_consistency | high |
| 2 | failure://a/duplicate_after_occlusion/1 | A | Subject duplication after opaque occlusion | L4 | metric_actor_count_consistency | moderate |
| 3 | failure://a/identity_rewrite_under_effect/1 | A | Identity rewrite under effect cover | L3 | metric_actor_count_consistency | moderate |
| 4 | failure://a/reappearance_region_error/1 | A | Incorrect reappearance region | L2 | metric_actor_count_consistency | high |
| 5 | failure://a/occluder_subject_fusion/1 | A | Occluder-subject fusion | L4 | metric_actor_count_consistency | moderate |
| 6 | failure://a/frame_exit_reentry_reset/1 | A | Frame-exit and re-entry state reset | L5 | metric_actor_count_consistency | moderate |
| 7 | failure://b/object_disappearance/1 | B | Persistent object disappearance | L3 | metric_environment_layout_consistency | high |
| 8 | failure://b/spontaneous_object_creation/1 | B | Spontaneous object creation | L2 | metric_environment_layout_consistency | high |
| 9 | failure://b/state_reset/1 | B | Object-state reset | L2 | metric_environment_layout_consistency | high |
| 10 | failure://b/size_material_drift/1 | B | Size, color, or material drift | L3 | metric_environment_layout_consistency | moderate |
| 11 | failure://b/hand_object_detachment/1 | B | Hand-object detachment | L4 | metric_contact_distance_error | high |
| 12 | failure://b/environment_layout_drift/1 | B | Environmental layout drift | L3 | metric_environment_layout_consistency | moderate |
| 13 | failure://c/face_costume_drift/1 | C | Face and costume drift | L3 | metric_identity_continuity | high |
| 14 | failure://c/actor_duplication_fusion/1 | C | Actor duplication or fusion | L4 | metric_actor_count_consistency | high |
| 15 | failure://c/role_swap/1 | C | Attacker-defender or speaker-role swap | L2 | metric_identity_continuity | high |
| 16 | failure://c/screen_side_identity_swap/1 | C | Screen-side identity swap | L5 | metric_identity_continuity | high |
| 17 | failure://c/target_confusion/1 | C | Action target confusion | L2 | metric_identity_continuity | high |
| 18 | failure://c/voice_identity_drift/1 | C | Voice identity drift | L3 | metric_identity_continuity | moderate |
| 19 | failure://d/left_right_frame_confusion/1 | D | Viewer-, actor-, and world-left confusion | L2 | metric_depth_order_accuracy | high |
| 20 | failure://d/axis_reversal_after_cut/1 | D | Axis reversal after cut | L5 | metric_depth_order_accuracy | high |
| 21 | failure://d/depth_order_inversion/1 | D | Depth-order inversion | L4 | metric_depth_order_accuracy | moderate |
| 22 | failure://d/trajectory_target_miss/1 | D | Trajectory misses target region | L4 | metric_depth_order_accuracy | high |
| 23 | failure://d/entrance_exit_mismatch/1 | D | Entrance and exit mismatch | L2 | metric_depth_order_accuracy | moderate |
| 24 | failure://d/eyeline_mismatch/1 | D | Eyeline and gaze-target mismatch | L3 | metric_depth_order_accuracy | moderate |
| 25 | failure://e/action_omission/1 | E | Primary action omission | L5 | metric_action_graph_agreement | high |
| 26 | failure://e/action_merge/1 | E | Sequential actions merged into one gesture | L2 | metric_action_graph_agreement | high |
| 27 | failure://e/action_repeat/1 | E | Unrequested action repetition | L1 | metric_action_graph_agreement | moderate |
| 28 | failure://e/event_order_reversal/1 | E | Event-order reversal | L2 | metric_action_graph_agreement | high |
| 29 | failure://e/recovery_omission/1 | E | Recovery or settle omission | L5 | metric_action_graph_agreement | high |
| 30 | failure://e/simultaneity_collapse/1 | E | Sequential events become simultaneous | L5 | metric_action_graph_agreement | high |
| 31 | failure://f/effect_before_cause/1 | F | Effect occurs before cause | L2 | metric_causal_edge_agreement | high |
| 32 | failure://f/effect_without_cause/1 | F | Effect without a valid cause | L2 | metric_causal_edge_agreement | high |
| 33 | failure://f/wrong_effect_origin/1 | F | Effect originates at the wrong location | L4 | metric_causal_edge_agreement | high |
| 34 | failure://f/wrong_reactor/1 | F | Wrong actor reacts | L2 | metric_causal_edge_agreement | high |
| 35 | failure://f/reaction_latency_error/1 | F | Reaction latency error | L2 | metric_causal_edge_agreement | moderate |
| 36 | failure://f/secondary_effect_chain_break/1 | F | Secondary-effect chain break | L5 | metric_causal_edge_agreement | high |
| 37 | failure://g/false_contact/1 | G | False contact | L4 | metric_contact_distance_error | high |
| 38 | failure://g/missing_contact/1 | G | Missing required contact | L4 | metric_contact_distance_error | high |
| 39 | failure://g/body_penetration/1 | G | Body or limb penetration | L4 | metric_contact_distance_error | high |
| 40 | failure://g/grip_drift/1 | G | Grip and support drift | L4 | metric_contact_distance_error | high |
| 41 | failure://g/wrong_contact_target/1 | G | Incorrect contact body part or region | L2 | metric_contact_distance_error | moderate |
| 42 | failure://g/interaction_distance_drift/1 | G | Interaction-distance drift | L4 | metric_contact_distance_error | moderate |
| 43 | failure://h/foot_skating/1 | H | Foot skating | L4 | metric_foot_slip_distance | high |
| 44 | failure://h/missing_support/1 | H | Missing support foot or base of support | L2 | metric_foot_slip_distance | high |
| 45 | failure://h/weightless_takeoff_landing/1 | H | Weightless takeoff or landing | L5 | metric_foot_slip_distance | high |
| 46 | failure://h/momentum_discontinuity/1 | H | Momentum disappearance or reversal | L4 | metric_foot_slip_distance | high |
| 47 | failure://h/constant_speed_motion/1 | H | Constant-speed motion without acceleration profile | L2 | metric_foot_slip_distance | moderate |
| 48 | failure://h/impossible_recovery/1 | H | Impossible recovery or balance regain | L5 | metric_foot_slip_distance | high |
| 49 | failure://i/solid_fluid_boundary_error/1 | I | Solid-fluid boundary error | L5 | metric_effect_origin_error | high |
| 50 | failure://i/splash_before_displacement/1 | I | Splash before displacement | L2 | metric_effect_origin_error | high |
| 51 | failure://i/splash_origin_drift/1 | I | Splash or water column follows the actor | L4 | metric_effect_origin_error | high |
| 52 | failure://i/submerged_subject_disappearance/1 | I | Submerged subject disappearance | L4 | metric_effect_origin_error | high |
| 53 | failure://i/material_effect_anatomy_spawn/1 | I | Material effect spawns anatomy or duplicate faces | L6 | metric_actor_count_consistency | moderate |
| 54 | failure://i/environment_material_state_drift/1 | I | Material topology or persistence drift | L3 | metric_effect_origin_error | moderate |
| 55 | failure://j/pan_becomes_actor_motion/1 | J | Camera pan becomes actor translation | L4 | metric_actor_world_trajectory | high |
| 56 | failure://j/tracking_freezes_locomotion/1 | J | Tracking shot freezes actor locomotion | L4 | metric_actor_world_trajectory | high |
| 57 | failure://j/orbit_reverses_screen_direction/1 | J | Orbit reverses screen direction | L5 | metric_actor_world_trajectory | high |
| 58 | failure://j/zoom_dolly_confusion/1 | J | Zoom and dolly confusion | L4 | metric_actor_world_trajectory | high |
| 59 | failure://j/impact_shake_deforms_subject/1 | J | Impact shake deforms or teleports subjects | L6 | metric_actor_world_trajectory | high |
| 60 | failure://j/motion_blur_identity_loss/1 | J | Motion blur destroys identity and geometry | L5 | metric_actor_world_trajectory | high |
| 61 | failure://k/flash_misread_as_cut/1 | K | Impact flash misread as a camera cut | L6 | metric_cut_flash_classification | high |
| 62 | failure://k/smoke_splash_wipe_scene_reset/1 | K | Effect wipe causes scene reset | L5 | metric_cut_flash_classification | high |
| 63 | failure://k/hard_cut_state_reset/1 | K | Hard cut resets world state | L3 | metric_cut_flash_classification | high |
| 64 | failure://k/whip_pan_teleport/1 | K | Whip-pan teleport | L6 | metric_cut_flash_classification | high |
| 65 | failure://k/transformation_burst_unintended_redesign/1 | K | Transformation burst redesigns forbidden attributes | L2 | metric_cut_flash_classification | moderate |
| 66 | failure://k/multi_shot_temporal_jump/1 | K | Multi-shot temporal jump or duplicate beat | L5 | metric_action_graph_agreement | high |
| 67 | failure://l/extra_missing_limbs/1 | L | Extra or missing limbs | L4 | metric_anatomical_validity | high |
| 68 | failure://l/joint_inversion/1 | L | Joint inversion or impossible articulation | L4 | metric_anatomical_validity | high |
| 69 | failure://l/persistent_smear_anatomy/1 | L | Smear deformation persists beyond the accent | L3 | metric_anatomical_validity | moderate |
| 70 | failure://l/perspective_deformation_persists/1 | L | Perspective enlargement persists | L3 | metric_anatomical_validity | moderate |
| 71 | failure://l/failed_anatomy_reconnection/1 | L | Failed anatomy reconnection after occlusion | L4 | metric_anatomical_validity | high |
| 72 | failure://l/stylization_readability_loss/1 | L | Stylization destroys action readability | L5 | metric_anatomical_validity | moderate |
| 73 | failure://m/structured_format_not_parsed/1 | M | Structured serialization treated as ordinary text | L1 | metric_field_projection_coverage | high |
| 74 | failure://m/duplicate_representation_attention_collision/1 | M | Duplicate-format attention collision | L1 | metric_field_projection_coverage | moderate |
| 75 | failure://m/numeric_control_ignored/1 | M | Exact numeric values ignored or approximated | L4 | metric_field_projection_coverage | high |
| 76 | failure://m/negative_prompt_concept_priming/1 | M | Negative instruction introduces or preserves forbidden content | L0 | metric_field_projection_coverage | low |
| 77 | failure://m/prompt_rewrite_semantic_loss/1 | M | Provider prompt rewriting changes canonical intent | L1 | metric_field_projection_coverage | moderate |
| 78 | failure://m/prompt_budget_truncation/1 | M | Prompt-budget overflow or truncation | L1 | metric_field_projection_coverage | high |
| 79 | failure://n/overconstraint_priority_dilution/1 | N | Overconstraint and priority dilution | L5 | metric_constraint_conflict_count | high |
| 80 | failure://n/under_specified_filler/1 | N | Under-specified filler action | L1 | metric_constraint_conflict_count | high |
| 81 | failure://n/contradictory_constraints/1 | N | Contradictory canonical constraints | L2 | metric_constraint_conflict_count | high |
| 82 | failure://n/action_density_overflow/1 | N | Action-density overflow | L5 | metric_constraint_conflict_count | high |
| 83 | failure://n/multi_actor_complexity_overflow/1 | N | Multi-actor interaction overload | L5 | metric_constraint_conflict_count | high |
| 84 | failure://n/camera_effect_choreography_overflow/1 | N | Camera, VFX, and choreography overload | L6 | metric_constraint_conflict_count | high |
| 85 | failure://o/impact_sound_offset/1 | O | Impact sound temporal offset | L2 | metric_audio_visual_semantic_match | high |
| 86 | failure://o/lip_speech_mismatch/1 | O | Lip-speech mismatch | L4 | metric_audio_visual_semantic_match | high |
| 87 | failure://o/sound_without_visual_cause/1 | O | Sound without visual cause | L2 | metric_audio_visual_semantic_match | high |
| 88 | failure://o/visual_event_without_sound/1 | O | Visual event lacks required sound | L6 | metric_audio_visual_semantic_match | moderate |
| 89 | failure://o/speaker_voice_drift/1 | O | Speaker or voice drift | L3 | metric_audio_visual_semantic_match | moderate |
| 90 | failure://o/music_action_accent_misalignment/1 | O | Music or beat accent misalignment | L4 | metric_audio_visual_semantic_match | high |
| 91 | failure://p/vlm_misses_fast_action/1 | P | VLM misses or reorders fast action | L2 | metric_evaluator_calibration | high |
| 92 | failure://p/vlm_invents_contact/1 | P | VLM invents contact from screen overlap | L4 | metric_evaluator_calibration | high |
| 93 | failure://p/tracker_identity_swap/1 | P | Tracker or segmenter swaps actor identity | L2 | metric_evaluator_calibration | high |
| 94 | failure://p/shot_detector_flash_false_positive/1 | P | Shot detector mistakes flash or smear for cut | L2 | metric_cut_flash_classification | moderate |
| 95 | failure://p/pose_metric_stylization_failure/1 | P | Pose/anatomy metric fails on anime or stylization | L2 | metric_evaluator_calibration | high |
| 96 | failure://p/aggregate_metric_hides_local_failure/1 | P | Aggregate score hides a decisive localized failure | L2 | metric_evaluator_calibration | high |

## Machine-readable authority

The Markdown index is for navigation. `FAILURE_RECORDS.jsonl` plus `FAILURE_RECORD.schema.json` is the machine-readable research authority for this package. The records are candidate evidence only; CPCS repository promotion still requires the existing second-brain distillation and human-curation path.
