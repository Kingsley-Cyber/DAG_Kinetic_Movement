# CPCS Directory Map (LIVE)

> **MANDATORY FILE.** This document is the live index of every route in the
> `cpcs/` tree. It MUST be regenerated whenever a route is added, removed,
> or renamed:
>
> ```pwsh
> pwsh -NoProfile -File .\update_directory_md.ps1
> ```
>
> Do not hand-edit the tree below; it is generated from the filesystem.

| Property | Value |
| --- | --- |
| Last updated | 2026-08-09 15:35:05 UTC |
| Root | `cpcs/` |
| Total routes | 1124 |
| Leaf routes | 1011 |

## Route Tree

```text
cpcs/
├── 00_governance/
│   ├── agent_logs/
│   ├── authority/
│   ├── change_control/
│   ├── contracts/
│   ├── deprecation_policy/
│   ├── epistemic_policy/
│   ├── naming/
│   ├── policies/
│   ├── release_policy/
│   └── versioning/
├── archive/
│   ├── deprecated_profiles/
│   ├── deprecated_providers/
│   ├── deprecated_taxonomy/
│   ├── frozen_releases/
│   ├── historical_experiments/
│   ├── migrations/
│   ├── previous_compilers/
│   ├── previous_graph_builds/
│   ├── previous_world_models/
│   └── superseded_research/
├── evaluation/
│   ├── ablations/
│   ├── benchmark_runs/
│   ├── calibration/
│   ├── carrier_equivalence/
│   ├── compiler/
│   ├── complexity/
│   ├── continuity/
│   ├── experiments/
│   ├── golden_cases/
│   ├── human_ratings/
│   ├── provider/
│   ├── reference_video/
│   ├── retrieval/
│   ├── synthesis/
│   ├── taxonomy/
│   └── world_model/
├── examples/
│   ├── action/
│   ├── anime/
│   ├── commercial/
│   ├── compiled_packages/
│   ├── dialogue/
│   ├── directing_strategies/
│   ├── documentary/
│   ├── multi_actor/
│   ├── product/
│   ├── reference_video/
│   ├── story_direction/
│   ├── ugc/
│   └── world_models/
├── generated/
│   ├── maintenance/
│   │   └── health_snapshots/
│   ├── provider/
│   │   └── capability_snapshots/
│   ├── reflections/
│   ├── repository_map/
│   ├── research/
│   │   ├── distillation_coverage/
│   │   ├── gap_matrix/
│   │   ├── numeric_coverage/
│   │   ├── source_coverage/
│   │   └── source_to_taxonomy/
│   ├── retrieval/
│   │   ├── aliases/
│   │   ├── context_indexes/
│   │   ├── query_roots/
│   │   └── retrieval_manifest/
│   └── taxonomy/
│       ├── branch_concept_index/
│       ├── concept_routes/
│       ├── director_tree/
│       └── interface_index/
├── knowledge/
│   ├── 00_foundations/
│   │   ├── architecture/
│   │   ├── causality/
│   │   ├── confidence/
│   │   ├── constraints/
│   │   ├── coordinate_systems/
│   │   │   ├── actor_local/
│   │   │   ├── camera/
│   │   │   ├── normalized/
│   │   │   ├── screen/
│   │   │   └── world/
│   │   ├── epistemic_classes/
│   │   │   ├── authored/
│   │   │   ├── creative_choice/
│   │   │   ├── detected/
│   │   │   ├── inferred/
│   │   │   ├── interpreted/
│   │   │   ├── measured/
│   │   │   └── observed/
│   │   ├── epistemic_policy/
│   │   ├── epistemology/
│   │   ├── invariants/
│   │   ├── measurement_principles/
│   │   ├── numerical_representation/
│   │   ├── salience/
│   │   ├── semantic_types/
│   │   ├── terminology/
│   │   ├── time/
│   │   │   ├── beats/
│   │   │   ├── frames/
│   │   │   ├── phrases/
│   │   │   ├── seconds/
│   │   │   └── synchronization/
│   │   ├── uncertainty/
│   │   └── units/
│   ├── 01_story_direction/
│   │   ├── anticipation_payoff/
│   │   ├── beats/
│   │   │   ├── action/
│   │   │   ├── climax/
│   │   │   ├── decision/
│   │   │   ├── discovery/
│   │   │   ├── escalation/
│   │   │   ├── inciting_change/
│   │   │   ├── payoff/
│   │   │   ├── reaction/
│   │   │   ├── reveal/
│   │   │   ├── reversal/
│   │   │   └── setup/
│   │   ├── conflict/
│   │   ├── information_strategy/
│   │   │   ├── confirm/
│   │   │   ├── establish/
│   │   │   ├── foreshadow/
│   │   │   ├── misdirect/
│   │   │   ├── payoff/
│   │   │   ├── reveal/
│   │   │   └── withhold/
│   │   ├── motivation/
│   │   ├── narrative_causality/
│   │   ├── narrative_perspective/
│   │   │   ├── alignment/
│   │   │   ├── focal_character/
│   │   │   ├── information_access/
│   │   │   ├── narrative_distance/
│   │   │   ├── objectivity/
│   │   │   ├── perspective_shift/
│   │   │   ├── point_of_view/
│   │   │   ├── reliability/
│   │   │   └── subjectivity/
│   │   ├── objectives/
│   │   │   ├── character/
│   │   │   ├── communication/
│   │   │   ├── dramatic/
│   │   │   └── scene/
│   │   ├── obstacle/
│   │   ├── pacing/
│   │   ├── premise/
│   │   │   ├── central_situation/
│   │   │   ├── dramatic_question/
│   │   │   ├── narrative_promise/
│   │   │   └── subject/
│   │   ├── setup_payoff/
│   │   ├── stakes/
│   │   ├── story_angle/
│   │   │   ├── contrast/
│   │   │   ├── discovery_lens/
│   │   │   ├── emotional_lens/
│   │   │   ├── framing/
│   │   │   ├── identity_lens/
│   │   │   ├── informational_lens/
│   │   │   ├── interpretation/
│   │   │   ├── novelty/
│   │   │   ├── social_lens/
│   │   │   ├── stakes_lens/
│   │   │   ├── thesis/
│   │   │   └── transformation_lens/
│   │   ├── subtext/
│   │   ├── tactic/
│   │   ├── tension/
│   │   ├── theme/
│   │   │   ├── motif/
│   │   │   ├── progression/
│   │   │   ├── thematic_argument/
│   │   │   ├── thematic_question/
│   │   │   └── value_conflict/
│   │   └── transformation/
│   │       ├── decision/
│   │       ├── pressure/
│   │       ├── realization/
│   │       ├── state_after/
│   │       └── state_before/
│   ├── 02_audience/
│   │   ├── anticipation/
│   │   ├── attention/
│   │   │   ├── auditory_guidance/
│   │   │   ├── focus_guidance/
│   │   │   ├── gaze_guidance/
│   │   │   ├── motion_salience/
│   │   │   ├── primary/
│   │   │   ├── secondary/
│   │   │   └── visual_salience/
│   │   ├── cognitive_load/
│   │   ├── comprehension/
│   │   ├── dramatic_irony/
│   │   ├── emotional_curve/
│   │   ├── information_state/
│   │   │   ├── concealed/
│   │   │   ├── false_belief/
│   │   │   ├── known/
│   │   │   ├── suspected/
│   │   │   └── unknown/
│   │   ├── misdirection/
│   │   ├── payoff/
│   │   ├── readability/
│   │   ├── reveal/
│   │   ├── surprise/
│   │   └── withholding/
│   ├── 03_world_scene/
│   │   ├── atmosphere/
│   │   ├── environment/
│   │   │   ├── architecture/
│   │   │   ├── atmosphere/
│   │   │   ├── environmental_motion/
│   │   │   ├── terrain/
│   │   │   └── weather/
│   │   ├── environmental_state/
│   │   ├── persistent_damage/
│   │   ├── scene_state/
│   │   ├── spatial_geometry/
│   │   │   ├── background/
│   │   │   ├── boundaries/
│   │   │   ├── depth_order/
│   │   │   ├── foreground/
│   │   │   ├── midground/
│   │   │   ├── traversal_space/
│   │   │   ├── vertical_levels/
│   │   │   └── world_coordinates/
│   │   ├── topology/
│   │   └── world_rules/
│   ├── 04_character_performance/
│   │   ├── affect/
│   │   │   ├── arousal/
│   │   │   ├── dominance/
│   │   │   ├── experienced_vs_displayed/
│   │   │   ├── trajectory/
│   │   │   └── valence/
│   │   ├── anatomy/
│   │   ├── appearance/
│   │   ├── breath/
│   │   ├── capabilities/
│   │   ├── costume/
│   │   ├── facs/
│   │   │   ├── action_units/
│   │   │   ├── asymmetry/
│   │   │   ├── combinations/
│   │   │   ├── intensity/
│   │   │   └── timing/
│   │   ├── gaze/
│   │   │   ├── eyes_head_lead/
│   │   │   ├── head_torso_lead/
│   │   │   ├── shift/
│   │   │   └── target/
│   │   ├── gesture/
│   │   ├── identity/
│   │   ├── knowledge_belief/
│   │   │   ├── belief/
│   │   │   ├── knowledge/
│   │   │   ├── knowledge_change/
│   │   │   └── uncertainty/
│   │   ├── mannerism/
│   │   ├── performance_readability/
│   │   ├── performance_scale/
│   │   ├── physical_state/
│   │   │   ├── breath_state/
│   │   │   ├── cleanliness/
│   │   │   ├── fatigue/
│   │   │   ├── injury/
│   │   │   ├── tension/
│   │   │   └── wetness/
│   │   ├── posture/
│   │   └── props/
│   ├── 05_action/
│   │   └── combat/
│   ├── 05_speech_social_interaction/
│   │   ├── affiliation/
│   │   ├── backchannel/
│   │   ├── dominance_submission/
│   │   ├── gaze_avoidance/
│   │   ├── group_formations/
│   │   ├── interpersonal_synchrony/
│   │   ├── interruption/
│   │   ├── joint_attention/
│   │   ├── leader_follower/
│   │   ├── mirroring/
│   │   ├── multi_party_attention/
│   │   ├── mutual_gaze/
│   │   ├── orientation/
│   │   ├── overlap/
│   │   ├── proxemics/
│   │   ├── relationship_state/
│   │   ├── speech/
│   │   │   ├── dialogue/
│   │   │   ├── emphasis/
│   │   │   ├── pause/
│   │   │   ├── phoneme/
│   │   │   ├── prosody/
│   │   │   ├── speech_act/
│   │   │   ├── timing/
│   │   │   └── viseme/
│   │   └── turn_taking/
│   ├── 06_body_motion/
│   │   ├── action_primitives/
│   │   ├── anticipatory_adjustment/
│   │   ├── bartenieff/
│   │   │   ├── basic_six/
│   │   │   ├── connectivity/
│   │   │   ├── initiation/
│   │   │   └── support/
│   │   ├── biomechanics/
│   │   │   ├── balance/
│   │   │   ├── center_of_mass/
│   │   │   ├── counter_rotation/
│   │   │   ├── joint_kinematics/
│   │   │   ├── proximal_distal/
│   │   │   ├── support/
│   │   │   └── weight_transfer/
│   │   ├── choreography/
│   │   ├── coarticulation/
│   │   ├── kinematics/
│   │   ├── kinetic_phrases/
│   │   ├── laban_bess/
│   │   │   ├── body/
│   │   │   ├── effort/
│   │   │   │   ├── flow/
│   │   │   │   ├── space/
│   │   │   │   ├── time/
│   │   │   │   └── weight/
│   │   │   ├── shape/
│   │   │   └── space/
│   │   ├── locomotion/
│   │   │   ├── climb/
│   │   │   ├── crawl/
│   │   │   ├── gait/
│   │   │   ├── jump/
│   │   │   ├── run/
│   │   │   └── walk/
│   │   ├── phase_grammar/
│   │   │   ├── acceleration/
│   │   │   ├── contact/
│   │   │   ├── follow_through/
│   │   │   ├── initiation/
│   │   │   ├── interruption/
│   │   │   ├── preparation/
│   │   │   └── recovery/
│   │   ├── phase_overlap/
│   │   ├── reaction/
│   │   ├── root_motion/
│   │   └── trajectories/
│   ├── 07_interaction_contact/
│   │   ├── actor_actor/
│   │   ├── actor_environment/
│   │   ├── actor_object/
│   │   ├── constraint_graphs/
│   │   ├── contact_topology/
│   │   ├── cooperative_contact/
│   │   ├── grasp/
│   │   ├── grip/
│   │   ├── impact/
│   │   ├── maintained_contact/
│   │   ├── near_contact/
│   │   ├── reaction/
│   │   ├── redirection/
│   │   ├── release/
│   │   ├── rolling/
│   │   ├── sliding/
│   │   └── support/
│   ├── 08_objects_affordances/
│   │   ├── affordances/
│   │   │   ├── carry/
│   │   │   ├── grasp/
│   │   │   ├── manipulate/
│   │   │   ├── open_close/
│   │   │   ├── pull/
│   │   │   ├── push/
│   │   │   ├── support/
│   │   │   └── traverse/
│   │   ├── articulated_parts/
│   │   ├── cooperative_manipulation/
│   │   ├── identity/
│   │   ├── materials/
│   │   ├── object_state/
│   │   ├── occupancy/
│   │   └── ownership/
│   ├── 09_evaluation/
│   ├── 09_force_physics/
│   │   ├── balance/
│   │   ├── cloth/
│   │   ├── collision/
│   │   ├── damping/
│   │   ├── debris/
│   │   ├── deformation/
│   │   ├── elasticity/
│   │   ├── fluid/
│   │   ├── follow_through/
│   │   ├── force_chain/
│   │   ├── friction/
│   │   ├── gravity/
│   │   ├── hair/
│   │   ├── impulse/
│   │   ├── inertia/
│   │   ├── mass/
│   │   ├── momentum/
│   │   ├── perceived_weight/
│   │   ├── recoil/
│   │   ├── torque/
│   │   └── virtual_physics/
│   ├── 10_time_rhythm/
│   │   ├── accents/
│   │   ├── anticipation/
│   │   ├── asynchrony/
│   │   ├── beats/
│   │   ├── cadence/
│   │   ├── clocks/
│   │   ├── compression/
│   │   ├── expansion/
│   │   ├── holds/
│   │   ├── overlap/
│   │   ├── pause/
│   │   ├── phrases/
│   │   ├── rhythm/
│   │   ├── synchronization/
│   │   ├── tempo/
│   │   ├── tempo_curve/
│   │   ├── temporal_density/
│   │   └── temporal_hierarchy/
│   ├── 11_blocking_screen_space/
│   │   ├── action_axis/
│   │   ├── axis_crossing/
│   │   ├── blocking/
│   │   │   ├── group/
│   │   │   ├── single_actor/
│   │   │   ├── tactical/
│   │   │   └── two_actor/
│   │   ├── combat_topology/
│   │   │   ├── attack_defense_geometry/
│   │   │   ├── depth_exchange/
│   │   │   ├── dynamic_topology/
│   │   │   ├── spatial_power_transfer/
│   │   │   └── tactical_reblocking/
│   │   ├── depth/
│   │   ├── entrances_exits/
│   │   ├── frame_dominance/
│   │   ├── occlusion/
│   │   ├── power_relationships/
│   │   ├── reveal_geometry/
│   │   ├── screen_direction/
│   │   ├── screen_position/
│   │   └── spatial_progression/
│   ├── 12_camera_image_formation/
│   │   ├── action_camera/
│   │   ├── camera_actor_choreography/
│   │   ├── camera_geometry/
│   │   │   ├── height/
│   │   │   ├── orientation/
│   │   │   ├── pitch/
│   │   │   ├── position/
│   │   │   ├── roll/
│   │   │   └── yaw/
│   │   ├── camera_subject_distance/
│   │   ├── composition/
│   │   ├── compression_noise/
│   │   ├── dialogue_camera/
│   │   ├── dynamic_range/
│   │   ├── exposure_behavior/
│   │   ├── focus/
│   │   │   ├── depth_of_field/
│   │   │   ├── focus_plane/
│   │   │   └── rack_focus/
│   │   ├── framing/
│   │   ├── lens/
│   │   │   ├── aberration/
│   │   │   ├── distortion/
│   │   │   ├── field_of_view/
│   │   │   ├── focal_length/
│   │   │   └── perspective_compression/
│   │   ├── motivated_camera/
│   │   ├── movement/
│   │   │   ├── compound/
│   │   │   ├── crane/
│   │   │   ├── dolly/
│   │   │   ├── handheld/
│   │   │   ├── orbit/
│   │   │   ├── pan/
│   │   │   ├── pedestal/
│   │   │   ├── tilt/
│   │   │   └── truck/
│   │   ├── observational_camera/
│   │   ├── perspective/
│   │   ├── reveal_camera/
│   │   ├── sensor_device_character/
│   │   ├── shutter_motion_blur/
│   │   ├── stabilization/
│   │   └── white_balance/
│   ├── 13_lighting_color/
│   │   ├── atmosphere/
│   │   ├── color_contrast/
│   │   ├── color_temperature/
│   │   ├── continuity/
│   │   ├── contrast/
│   │   ├── direction/
│   │   ├── exposure/
│   │   ├── falloff/
│   │   ├── grading/
│   │   ├── intensity/
│   │   ├── key_fill_rim/
│   │   ├── motivated_lighting/
│   │   ├── moving_light/
│   │   ├── palette/
│   │   ├── practicals/
│   │   ├── softness/
│   │   ├── source_geometry/
│   │   ├── source_size/
│   │   └── sources/
│   ├── 14_editing/
│   │   ├── continuity/
│   │   ├── coverage/
│   │   ├── cut_motivation/
│   │   │   ├── action/
│   │   │   ├── attention_transfer/
│   │   │   ├── information_change/
│   │   │   ├── reaction/
│   │   │   ├── reveal/
│   │   │   └── sound_motivation/
│   │   ├── cut_on_motion/
│   │   ├── cut_on_sound/
│   │   ├── cutaway/
│   │   ├── discontinuity/
│   │   ├── editorial_rhythm/
│   │   ├── ellipsis/
│   │   ├── eyeline/
│   │   ├── insert/
│   │   ├── match_on_action/
│   │   ├── montage/
│   │   ├── parallel_action/
│   │   ├── reaction/
│   │   ├── reveal_cut/
│   │   ├── shot_information_contract/
│   │   ├── shot_reverse_shot/
│   │   ├── shot_sequence/
│   │   └── transition_causality/
│   ├── 15_audio/
│   │   ├── ambience/
│   │   ├── audiovisual_causality/
│   │   ├── dialogue/
│   │   │   ├── emphasis/
│   │   │   ├── pause/
│   │   │   ├── prosody/
│   │   │   ├── syllable_rate/
│   │   │   ├── timing/
│   │   │   ├── word_timestamps/
│   │   │   └── wpm/
│   │   ├── diegetic/
│   │   ├── foley/
│   │   ├── footsteps/
│   │   ├── impacts/
│   │   ├── j_cuts/
│   │   ├── l_cuts/
│   │   ├── music/
│   │   │   ├── emotion/
│   │   │   ├── hit_points/
│   │   │   ├── motif/
│   │   │   ├── rhythm/
│   │   │   └── tension_release/
│   │   ├── nondiegetic/
│   │   ├── occlusion/
│   │   ├── offscreen_sound/
│   │   ├── reverb/
│   │   ├── room_acoustics/
│   │   ├── silence/
│   │   ├── sound_bridges/
│   │   ├── sound_perspective/
│   │   ├── spatial_sources/
│   │   ├── synchronization/
│   │   └── voice/
│   ├── 16_style_visual_language/
│   │   ├── 3d_animation/
│   │   ├── allowed_variation/
│   │   ├── anime/
│   │   │   ├── background_motion/
│   │   │   ├── deliberate_discontinuity/
│   │   │   ├── exposure_density/
│   │   │   ├── held_drawings/
│   │   │   ├── impact_frames/
│   │   │   ├── key_pose_hierarchy/
│   │   │   ├── limited_animation/
│   │   │   ├── sakuga/
│   │   │   └── smears/
│   │   ├── audio_style/
│   │   ├── camera_style/
│   │   ├── cartoon/
│   │   ├── cinematic/
│   │   ├── comedy/
│   │   ├── commercial/
│   │   ├── documentary/
│   │   ├── editing_style/
│   │   ├── fashion/
│   │   ├── forbidden_drift/
│   │   ├── horror/
│   │   ├── illustration/
│   │   ├── invariants/
│   │   ├── motion_style/
│   │   ├── narrative_style/
│   │   ├── noir/
│   │   ├── performance_style/
│   │   ├── realism/
│   │   ├── stop_motion/
│   │   ├── surreal/
│   │   ├── ugc/
│   │   └── visual_style/
│   ├── 17_vfx_secondary_motion/
│   │   ├── accessories/
│   │   ├── cloth/
│   │   ├── debris/
│   │   ├── destruction/
│   │   ├── dust/
│   │   ├── energy/
│   │   ├── fire/
│   │   ├── hair/
│   │   ├── impact_frames/
│   │   ├── motion_blur/
│   │   ├── particles/
│   │   ├── smears/
│   │   ├── smoke/
│   │   ├── soft_tissue/
│   │   ├── trails/
│   │   ├── vfx_causality/
│   │   └── water/
│   ├── 18_sequence_continuity/
│   │   ├── affect_state/
│   │   ├── audience_information_state/
│   │   ├── audio_state/
│   │   ├── character_state/
│   │   ├── continuity_hashes/
│   │   ├── costume_state/
│   │   ├── dramatic_obligations/
│   │   ├── environment_state/
│   │   ├── fatigue_state/
│   │   ├── gaze_state/
│   │   ├── identity_state/
│   │   ├── injury_state/
│   │   ├── knowledge_state/
│   │   ├── lighting_state/
│   │   ├── object_state/
│   │   ├── occluded_hidden_state/
│   │   ├── orientation_state/
│   │   ├── prop_state/
│   │   ├── reentry_state/
│   │   ├── relationship_state/
│   │   ├── spatial_state/
│   │   └── unresolved_actions/
│   ├── 19_generation_complexity/
│   │   ├── action_density/
│   │   ├── actor_burden/
│   │   ├── camera_complexity/
│   │   ├── contact_density/
│   │   ├── dialogue_density/
│   │   ├── identity_burden/
│   │   ├── interaction_density/
│   │   ├── partitioning/
│   │   ├── physics_complexity/
│   │   ├── provider_risk/
│   │   ├── simplification/
│   │   ├── simultaneous_actions/
│   │   ├── style_complexity/
│   │   ├── temporal_density/
│   │   └── vfx_complexity/
│   └── 20_interfaces/
│       ├── actor_x_scene/
│       ├── audience_x_audio/
│       ├── audience_x_camera/
│       ├── audience_x_editing/
│       ├── audience_x_lighting/
│       ├── audience_x_performance/
│       ├── audio_x_editing/
│       ├── blocking_x_camera/
│       │   ├── action_axis/
│       │   ├── actor_camera_coupling/
│       │   ├── camera_countermotion/
│       │   ├── depth_reframing/
│       │   ├── occlusion_management/
│       │   └── reveal_geometry/
│       ├── blocking_x_editing/
│       ├── blocking_x_lighting/
│       ├── camera_x_audio/
│       ├── camera_x_editing/
│       ├── camera_x_lighting/
│       ├── causality_x_editing/
│       ├── lighting_x_editing/
│       ├── motion_x_audio/
│       ├── motion_x_camera/
│       ├── motion_x_contact/
│       ├── motion_x_physics/
│       ├── object_x_affordance/
│       ├── object_x_physics/
│       ├── performance_x_camera/
│       ├── performance_x_editing/
│       ├── performance_x_lighting/
│       ├── performance_x_speech/
│       ├── shot_x_shot/
│       ├── state_x_continuity/
│       ├── story_x_audience/
│       ├── story_x_camera/
│       ├── story_x_editing/
│       ├── story_x_performance/
│       ├── style_x_camera/
│       ├── style_x_editing/
│       └── style_x_motion/
├── maintenance/
│   ├── archive_rotation/
│   ├── compiler_health/
│   │   ├── carrier_parity/
│   │   ├── duration_partitioning/
│   │   ├── loss_accounting/
│   │   ├── numerical_fidelity/
│   │   ├── regression/
│   │   └── semantic_equivalence/
│   ├── data_migrations/
│   ├── dependency_health/
│   ├── deprecations/
│   ├── health_reports/
│   ├── maintenance_history/
│   ├── provider_health/
│   │   ├── capability_refresh/
│   │   ├── deprecated_capabilities/
│   │   ├── documentation_drift/
│   │   ├── experiment_refresh/
│   │   └── version_drift/
│   ├── provider_migrations/
│   ├── release_checks/
│   ├── research_health/
│   │   ├── contradiction_review/
│   │   ├── distillation_coverage/
│   │   ├── duplicate_detection/
│   │   ├── novelty_detection/
│   │   ├── numerical_audit/
│   │   ├── stale_evidence/
│   │   └── unresolved_research/
│   ├── retrieval_health/
│   │   ├── context_budget/
│   │   ├── forbidden_leakage/
│   │   ├── required_recall/
│   │   ├── reranking/
│   │   ├── retrieval_regression/
│   │   └── stale_indexes/
│   ├── schema_migrations/
│   ├── source_health/
│   │   ├── hash_integrity/
│   │   ├── inventory/
│   │   ├── missing_sources/
│   │   ├── parse_failures/
│   │   ├── quarantine/
│   │   └── source_closure/
│   ├── taxonomy_health/
│   │   ├── alias_conflicts/
│   │   ├── broken_routes/
│   │   ├── cycles/
│   │   ├── edge_validation/
│   │   ├── interface_coverage/
│   │   ├── orphan_nodes/
│   │   └── route_coverage/
│   ├── taxonomy_migrations/
│   ├── verification_health/
│   │   ├── failure_taxonomy/
│   │   ├── golden_case_drift/
│   │   ├── human_review_calibration/
│   │   └── metric_coverage/
│   └── world_model_health/
│       ├── causal_consistency/
│       ├── distiller_calibration/
│       ├── salience_quality/
│       ├── schema_coverage/
│       └── state_persistence/
├── observation/
│   ├── actor_tracking/
│   ├── audio/
│   ├── camera/
│   ├── concept_bridges/
│   ├── contact/
│   ├── editing/
│   ├── face/
│   ├── gaze/
│   ├── lighting/
│   ├── local_measurements/
│   ├── motion/
│   ├── pegasus/
│   ├── pose/
│   ├── reference_video/
│   ├── research_gap_discovery/
│   ├── reverse_compiler/
│   ├── scene_detection/
│   ├── shot_detection/
│   ├── style/
│   └── video_observation_graph/
├── profiles/
│   ├── audience/
│   ├── audio/
│   ├── camera/
│   ├── capture/
│   ├── composite/
│   ├── domain/
│   │   ├── action/
│   │   ├── anime/
│   │   ├── cinematic/
│   │   ├── commercial/
│   │   ├── dialogue/
│   │   ├── documentary/
│   │   ├── educational/
│   │   ├── music_video/
│   │   ├── product/
│   │   └── ugc/
│   ├── editing/
│   ├── generation/
│   ├── interaction/
│   ├── lighting/
│   ├── motion/
│   ├── performance/
│   ├── screen_action/
│   ├── speech_social/
│   ├── story/
│   └── style/
├── providers/
│   ├── capabilities/
│   ├── kling/
│   ├── ltx/
│   ├── luma/
│   ├── other/
│   ├── registry/
│   ├── runway/
│   ├── seedance/
│   ├── sora/
│   ├── veo/
│   └── versions/
├── research/
│   ├── contradictions/
│   ├── coverage/
│   │   ├── by_interface/
│   │   ├── by_numeric_domain/
│   │   ├── by_provider/
│   │   ├── by_source/
│   │   ├── by_taxonomy/
│   │   └── reverse_audit/
│   ├── curation/
│   │   ├── merge/
│   │   ├── promotion/
│   │   ├── proposals/
│   │   ├── rejected/
│   │   ├── review/
│   │   └── superseded/
│   ├── distillation/
│   │   ├── contradiction_sweep/
│   │   ├── coverage/
│   │   ├── deduplication/
│   │   ├── interface_sweep/
│   │   ├── ledger/
│   │   ├── novelty_detection/
│   │   ├── numerical_sweep/
│   │   ├── representation_sweep/
│   │   ├── source_forward/
│   │   ├── structured_sweep/
│   │   └── taxonomy_reverse/
│   ├── evidence/
│   │   ├── claims/
│   │   ├── counterexamples/
│   │   ├── doctrines/
│   │   ├── equations/
│   │   ├── examples/
│   │   ├── failure_modes/
│   │   ├── measurements/
│   │   ├── mechanisms/
│   │   ├── methods/
│   │   └── principles/
│   ├── gaps/
│   ├── numerical/
│   │   ├── calibration/
│   │   ├── categorical_codes/
│   │   ├── equations/
│   │   ├── normalization/
│   │   ├── ordinal_scales/
│   │   ├── physical_measurements/
│   │   ├── project_derived_scales/
│   │   ├── ranges/
│   │   ├── scientific_scales/
│   │   ├── thresholds/
│   │   ├── timing_relations/
│   │   ├── tolerances/
│   │   └── units/
│   ├── representation/
│   │   ├── hybrids/
│   │   ├── json/
│   │   ├── jsonl/
│   │   ├── natural_language/
│   │   ├── nesting_effects/
│   │   ├── ordering_effects/
│   │   ├── prompt_budget/
│   │   ├── semantic_equivalence/
│   │   ├── xml/
│   │   └── yaml/
│   ├── source_registry/
│   │   ├── hashes/
│   │   ├── identities/
│   │   ├── lineage/
│   │   ├── source_closure/
│   │   └── source_units/
│   └── sources/
│       ├── experiments/
│       ├── manifests/
│       ├── preserved/
│       ├── provider_research/
│       ├── quarantine/
│       ├── rag/
│       │   ├── chunks/
│       │   ├── extracted_objects/
│       │   ├── graph_exports/
│       │   ├── hierarchical_summaries/
│       │   └── parent_summaries/
│       ├── raw/
│       ├── reference_video_research/
│       └── structured/
│           ├── csv/
│           ├── json/
│           ├── jsonl/
│           ├── tables/
│           ├── xml/
│           └── yaml/
├── runtime/
│   ├── 00_request/
│   │   ├── ambiguity/
│   │   ├── constraints/
│   │   ├── exactness/
│   │   ├── intent/
│   │   ├── normalization/
│   │   └── story_angle_resolution/
│   ├── 01_world_model/
│   │   ├── audience/
│   │   ├── audio_state/
│   │   ├── camera_state/
│   │   ├── causal_events/
│   │   ├── character_state/
│   │   ├── complexity/
│   │   ├── continuity/
│   │   ├── distiller/
│   │   ├── editing_state/
│   │   ├── entities/
│   │   ├── intent/
│   │   ├── knowledge_state/
│   │   ├── lighting_state/
│   │   ├── motion_state/
│   │   ├── performance_state/
│   │   ├── relationships/
│   │   ├── salience/
│   │   ├── spatial_state/
│   │   ├── state_transitions/
│   │   ├── style_state/
│   │   ├── temporal_state/
│   │   └── world/
│   ├── 02_routing/
│   │   ├── branch_activation/
│   │   ├── budgets/
│   │   ├── edge_policy/
│   │   ├── interface_activation/
│   │   ├── profile_activation/
│   │   ├── query_decomposition/
│   │   └── taxonomy/
│   ├── 03_retrieval/
│   │   ├── aliases/
│   │   ├── context_packing/
│   │   ├── coverage_check/
│   │   ├── interface_retrieval/
│   │   ├── lexical/
│   │   ├── reranking/
│   │   ├── source_hydration/
│   │   ├── tree/
│   │   ├── typed_graph/
│   │   └── vector/
│   ├── 04_synthesis/
│   │   ├── audience/
│   │   ├── audio/
│   │   ├── blocking/
│   │   ├── camera/
│   │   ├── contradiction_resolution/
│   │   ├── coverage/
│   │   ├── cross_department/
│   │   ├── decision_validation/
│   │   ├── editing/
│   │   ├── interaction/
│   │   ├── lighting/
│   │   ├── motion/
│   │   ├── performance/
│   │   ├── story/
│   │   └── style/
│   ├── 05_strategy/
│   │   ├── compiled_directing_strategy/
│   │   ├── compromises/
│   │   ├── constraints/
│   │   ├── controlled_degrees_of_freedom/
│   │   ├── decision_ledger/
│   │   ├── locks/
│   │   └── verification_targets/
│   ├── 06_canonical/
│   │   ├── control_registry/
│   │   ├── duration/
│   │   ├── field_policies/
│   │   ├── normalization/
│   │   ├── numerical_resolution/
│   │   ├── precedence/
│   │   ├── sequence_partitioning/
│   │   ├── temporal_tracks/
│   │   └── universal_score/
│   ├── 07_compiler/
│   │   ├── approximation/
│   │   ├── carrier_planner/
│   │   ├── compression/
│   │   ├── hybrid/
│   │   ├── json/
│   │   ├── loss_ledger/
│   │   ├── merge_precedence/
│   │   ├── natural_language/
│   │   ├── salience_budgeting/
│   │   ├── semantic_mapping/
│   │   ├── xml/
│   │   └── yaml/
│   ├── 08_provider_negotiation/
│   │   ├── capability_matching/
│   │   ├── continuity_handoff/
│   │   ├── native_controls/
│   │   ├── reference_baking/
│   │   ├── segmentation/
│   │   ├── text_fallback/
│   │   └── unsupported_controls/
│   └── 09_execution/
│       ├── build/
│       ├── lineage/
│       ├── receipt/
│       ├── render/
│       └── request_package/
├── schemas/
│   ├── canonical_score/
│   ├── carrier/
│   ├── evaluation/
│   ├── governance/
│   ├── maintenance/
│   ├── numerical/
│   ├── observation/
│   ├── profiles/
│   ├── providers/
│   ├── research/
│   ├── retrieval/
│   ├── routing/
│   ├── sources/
│   ├── strategy/
│   ├── taxonomy/
│   ├── verification/
│   └── world_model/
├── tests/
│   ├── canaries/
│   ├── carrier/
│   ├── compiler/
│   ├── distillation/
│   ├── fixtures/
│   ├── integration/
│   ├── maintenance/
│   ├── numerical/
│   ├── provider/
│   ├── regression/
│   ├── retrieval/
│   ├── scale/
│   ├── semantic/
│   ├── source_closure/
│   ├── synthesis/
│   ├── taxonomy/
│   ├── unit/
│   ├── verification/
│   └── world_model/
└── verification/
    ├── action_order/
    ├── actor_count/
    ├── audience_information/
    ├── audio/
    ├── blocking/
    ├── camera/
    ├── causality/
    ├── contact/
    ├── continuity/
    ├── editing/
    ├── facs/
    ├── failures/
    │   ├── causal_diagnosis/
    │   ├── classification/
    │   ├── detection/
    │   └── failure_cards/
    ├── foot_slip/
    ├── gaze/
    ├── human_director/
    ├── identity/
    ├── lighting/
    ├── motion/
    ├── performance/
    ├── persistent_state/
    ├── phase/
    ├── physics/
    ├── provider_loss/
    ├── readability/
    ├── repair/
    │   ├── control_adjustment/
    │   ├── minimal_repair/
    │   ├── regeneration/
    │   ├── repartition/
    │   └── stopping_rules/
    ├── screen_direction/
    ├── semantic/
    ├── story/
    ├── style/
    ├── timing/
    ├── trajectory/
    └── world_state/
```

---
_Generated by `update_directory_md.ps1`. Never edit this file manually._
