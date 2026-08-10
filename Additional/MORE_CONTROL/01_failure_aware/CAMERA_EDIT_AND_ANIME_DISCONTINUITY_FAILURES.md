# Camera, Edit, Graphic Discontinuity, and Anime-Recovery Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Camera motion, full-frame effects, cuts, smears, and stylized deformation are ambiguous unless CPCS distinguishes screen projection from world motion and graphic discontinuity from world-state change. Anime accents require explicit anatomy recovery rather than continuous realism.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| J | Camera and actor-motion entanglement | 6 | camera + motion + shots + verification | metric_camera_motion_agreement, metric_actor_world_trajectory, metric_zoom_translation_disambiguation, metric_screen_direction_consistency |
| K | Cuts, flashes, smears, and scene reset | 6 | editing + continuity + style + verification | metric_cut_flash_classification, metric_post_cut_state_consistency, metric_shot_boundary_error, metric_graphic_discontinuity_recovery |
| L | Anatomy and stylization recovery | 6 | motion + style + performance + verification | metric_anatomical_validity, metric_deformation_duration, metric_recovery_frame_accuracy, metric_silhouette_readability |

## Canonical contract implications

Separate camera translation, rotation, lens/zoom, actor world motion, actor screen motion, background motion, edit boundary, and impact impulse. Type every discontinuity as cut, flash, hold, smear, blur, wipe, occlusion, or world reset. For stylized deformation, encode affected region, onset, source/destination poses, maximum deformation, exposure duration, silhouette anchors, and required recovery frame.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### J.55 — Camera pan becomes actor translation

**Failure ID:** `failure://j/pan_becomes_actor_motion/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B031], [B035], [B037], [B040]

**Trigger.** The prompt combines a pan with actor locomotion or static blocking.

**Observable symptom.** The actor slides across the world or background instead of the camera rotating.

**Likely cause.** Camera and object motion are entangled in the learned representation. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Represent camera pose and actor world trajectory separately; use camera-control media or source-video motion.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_world_trajectory` is the primary metric; companion checks: `metric_camera_motion_agreement`, `metric_screen_direction_consistency`, `metric_zoom_translation_disambiguation`.

**Compiler/score impact.** `camera`, `motion`, `shots`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** mixes camera and actor motion in one undifferentiated sentence; combines orbit, impact shake, blur, and choreography; uses zoom and dolly interchangeably.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### J.56 — Tracking shot freezes actor locomotion

**Failure ID:** `failure://j/tracking_freezes_locomotion/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B021], [B031], [B035], [B037], [B040]

**Trigger.** A camera should follow a moving actor at stable framing.

**Observable symptom.** The actor appears stationary while the background moves, or gait collapses.

**Likely cause.** Screen-space constancy is mistaken for world-space immobility. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Encode world locomotion and camera follow as separate tracks; verify foot motion and background parallax.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_world_trajectory` is the primary metric; companion checks: `metric_camera_motion_agreement`, `metric_screen_direction_consistency`, `metric_zoom_translation_disambiguation`.

**Compiler/score impact.** `camera`, `motion`, `shots`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** mixes camera and actor motion in one undifferentiated sentence; combines orbit, impact shake, blur, and choreography; uses zoom and dolly interchangeably.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### J.57 — Orbit reverses screen direction

**Failure ID:** `failure://j/orbit_reverses_screen_direction/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B031], [B035], [B037], [B040]

**Trigger.** The camera orbits around two actors during directional action.

**Observable symptom.** Left-to-right action flips or roles swap.

**Likely cause.** Camera-side crossing changes projection while the canonical action axis is not preserved. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Do not combine an orbit with exact two-actor choreography unless camera-pose control is available; split or re-establish the axis.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_world_trajectory` is the primary metric; companion checks: `metric_camera_motion_agreement`, `metric_screen_direction_consistency`, `metric_zoom_translation_disambiguation`.

**Compiler/score impact.** `camera`, `motion`, `shots`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** mixes camera and actor motion in one undifferentiated sentence; combines orbit, impact shake, blur, and choreography; uses zoom and dolly interchangeably.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### J.58 — Zoom and dolly confusion

**Failure ID:** `failure://j/zoom_dolly_confusion/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B031], [B035], [B037], [B040]

**Trigger.** The prompt asks for zoom, push-in, dolly, or Hitchcock-style motion.

**Observable symptom.** Perspective/parallax and subject scale change incorrectly.

**Likely cause.** Intrinsic lens change and extrinsic camera translation are visually confusable and evaluators also have blind spots. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use explicit camera intrinsics/extrinsics or a source/control video; validate parallax, subject scale, and background expansion separately.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_world_trajectory` is the primary metric; companion checks: `metric_camera_motion_agreement`, `metric_screen_direction_consistency`, `metric_zoom_translation_disambiguation`.

**Compiler/score impact.** `camera`, `motion`, `shots`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** mixes camera and actor motion in one undifferentiated sentence; combines orbit, impact shake, blur, and choreography; uses zoom and dolly interchangeably.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### J.59 — Impact shake deforms or teleports subjects

**Failure ID:** `failure://j/impact_shake_deforms_subject/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B016], [B031], [B032], [B035], [B037], [B040]

**Trigger.** Handheld shake or impact impulse coincides with contact/effect.

**Observable symptom.** Bodies warp, location jumps, or motion blur rewrites identity.

**Likely cause.** Global frame perturbation is entangled with object deformation and the contact interval is already ambiguous. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L6 (postproduction/compositing).** Generate a stable plate and add camera shake in post, or apply controlled V2V to the final shot.

**Fallback — L8 (provider/model substitution).** Use a provider/model with an officially documented control input matching the missing constraint and rerun qualification.

**Verification.** `metric_actor_world_trajectory` is the primary metric; companion checks: `metric_camera_motion_agreement`, `metric_identity_continuity`, `metric_screen_direction_consistency`, `metric_zoom_translation_disambiguation`.

**Compiler/score impact.** `camera`, `motion`, `shots`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** mixes camera and actor motion in one undifferentiated sentence; combines orbit, impact shake, blur, and choreography; uses zoom and dolly interchangeably.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### J.60 — Motion blur destroys identity and geometry

**Failure ID:** `failure://j/motion_blur_identity_loss/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B016], [B019], [B031], [B032], [B035], [B037], [B040]

**Trigger.** Whip pans, fast limbs, smears, or low shutter cues cover key frames.

**Observable symptom.** Faces/limbs melt, duplicate, or reconnect incorrectly.

**Likely cause.** Blur removes high-frequency identity and boundary cues during high motion. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Keep the decisive contact/recovery readable, shorten blur intervals, add authored blur/smears in post, or provide source motion.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_world_trajectory` is the primary metric; companion checks: `metric_camera_motion_agreement`, `metric_identity_continuity`, `metric_screen_direction_consistency`, `metric_zoom_translation_disambiguation`.

**Compiler/score impact.** `camera`, `motion`, `shots`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** mixes camera and actor motion in one undifferentiated sentence; combines orbit, impact shake, blur, and choreography; uses zoom and dolly interchangeably.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### K.61 — Impact flash misread as a camera cut

**Failure ID:** `failure://k/flash_misread_as_cut/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B010], [B015], [B027], [B033]

**Trigger.** A full-frame white/black/monochrome flash interrupts action.

**Observable symptom.** The model resets scene, identity, pose, or location after the flash.

**Likely cause.** A graphic discontinuity resembles a shot boundary in training data. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L6 (postproduction/compositing).** Generate continuous action without the flash and insert a one-frame graphic flash in post; verify pre/post state identity.

**Fallback — L8 (provider/model substitution).** Use a provider/model with an officially documented control input matching the missing constraint and rerun qualification.

**Verification.** `metric_cut_flash_classification` is the primary metric; companion checks: `metric_graphic_discontinuity_recovery`, `metric_post_cut_state_consistency`, `metric_shot_boundary_error`.

**Compiler/score impact.** `editing`, `continuity`, `style`, `shots`, `verification_requirements`.

**Prompt risks.** uses full-frame flash or wipe without declaring continuity semantics; describes multi-shot events without state handoffs; uses transformation language without allowed-state deltas.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### K.62 — Effect wipe causes scene reset

**Failure ID:** `failure://k/smoke_splash_wipe_scene_reset/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B010], [B012], [B015], [B027], [B033]

**Trigger.** Smoke, splash, speed lines, or transformation effects cover the whole frame.

**Observable symptom.** A new background, costume, pose, or actor arrangement appears.

**Likely cause.** Opaque effect interval is interpreted as permission for a new scene sample. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Treat the wipe as an edit boundary with explicit outgoing/incoming state or composite it between separately verified plates.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_cut_flash_classification` is the primary metric; companion checks: `metric_graphic_discontinuity_recovery`, `metric_post_cut_state_consistency`, `metric_shot_boundary_error`.

**Compiler/score impact.** `editing`, `continuity`, `style`, `shots`, `verification_requirements`.

**Prompt risks.** uses full-frame flash or wipe without declaring continuity semantics; describes multi-shot events without state handoffs; uses transformation language without allowed-state deltas.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### K.63 — Hard cut resets world state

**Failure ID:** `failure://k/hard_cut_state_reset/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B010], [B015], [B027], [B028], [B033], [B040]

**Trigger.** A multi-shot prompt revisits actors/objects after a cut.

**Observable symptom.** Object, injury, wardrobe, direction, or environment state regresses.

**Likely cause.** Shots are generated with insufficient shared entity/world memory. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Use shot-level state snapshots, shared references, and explicit continuity inheritance; generate shots separately when provider multi-shot control is weak.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_cut_flash_classification` is the primary metric; companion checks: `metric_graphic_discontinuity_recovery`, `metric_post_cut_state_consistency`, `metric_shot_boundary_error`.

**Compiler/score impact.** `editing`, `continuity`, `style`, `shots`, `verification_requirements`.

**Prompt risks.** uses full-frame flash or wipe without declaring continuity semantics; describes multi-shot events without state handoffs; uses transformation language without allowed-state deltas.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### K.64 — Whip-pan teleport

**Failure ID:** `failure://k/whip_pan_teleport/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B010], [B012], [B015], [B027], [B031], [B033]

**Trigger.** A whip pan bridges positions or shots.

**Observable symptom.** Actors teleport, swap sides, or disappear during the blur.

**Likely cause.** The hidden interval combines camera ambiguity and subject occlusion. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L6 (postproduction/compositing).** Create outgoing and incoming plates with matched motion direction, then add the whip blur/edit in post.

**Fallback — L8 (provider/model substitution).** Use a provider/model with an officially documented control input matching the missing constraint and rerun qualification.

**Verification.** `metric_cut_flash_classification` is the primary metric; companion checks: `metric_graphic_discontinuity_recovery`, `metric_post_cut_state_consistency`, `metric_screen_direction_consistency`, `metric_shot_boundary_error`.

**Compiler/score impact.** `editing`, `continuity`, `style`, `shots`, `verification_requirements`.

**Prompt risks.** uses full-frame flash or wipe without declaring continuity semantics; describes multi-shot events without state handoffs; uses transformation language without allowed-state deltas.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### K.65 — Transformation burst redesigns forbidden attributes

**Failure ID:** `failure://k/transformation_burst_unintended_redesign/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B010], [B015], [B027], [B033]

**Trigger.** A transformation or energy burst permits only a specific state change.

**Observable symptom.** Identity, costume, body, or environment changes beyond the authorized delta.

**Likely cause.** The effect activates broad transformation priors without a constrained change set. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Declare allowed and forbidden state deltas and provide the required post-transform reference frame; verify every locked attribute.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_cut_flash_classification` is the primary metric; companion checks: `metric_graphic_discontinuity_recovery`, `metric_post_cut_state_consistency`, `metric_shot_boundary_error`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `editing`, `continuity`, `style`, `shots`, `verification_requirements`.

**Prompt risks.** uses full-frame flash or wipe without declaring continuity semantics; describes multi-shot events without state handoffs; uses transformation language without allowed-state deltas.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### K.66 — Multi-shot temporal jump or duplicate beat

**Failure ID:** `failure://k/multi_shot_temporal_jump/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B010], [B015], [B027], [B033], [B040]

**Trigger.** A model generates several shots inside one clip.

**Observable symptom.** Events repeat, time skips, or a shot shows a contradictory phase.

**Likely cause.** Shot segmentation and event graph are not explicitly aligned. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Assign each shot a closed event interval and handoff state; compile/generate separately if the provider cannot expose shot-level control.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_action_graph_agreement` is the primary metric; companion checks: `metric_cut_flash_classification`, `metric_graphic_discontinuity_recovery`, `metric_post_cut_state_consistency`, `metric_shot_boundary_error`.

**Compiler/score impact.** `editing`, `continuity`, `style`, `shots`, `verification_requirements`.

**Prompt risks.** uses full-frame flash or wipe without declaring continuity semantics; describes multi-shot events without state handoffs; uses transformation language without allowed-state deltas.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### L.67 — Extra or missing limbs

**Failure ID:** `failure://l/extra_missing_limbs/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B016], [B018], [B032], [B042]

**Trigger.** Fast action, overlap, blur, cloth, hair, or foreshortening hides joints.

**Observable symptom.** An extra limb appears, a limb disappears, or ownership changes.

**Likely cause.** Ambiguous silhouettes and compressed spatiotemporal representation weaken anatomical correspondence. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use pose/source-video guidance, maintain limb separability, and reserve anatomy recovery checkpoints.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_anatomical_validity` is the primary metric; companion checks: `metric_deformation_duration`, `metric_recovery_frame_accuracy`, `metric_silhouette_readability`.

**Compiler/score impact.** `motion`, `style`, `performance`, `continuity.anatomy_state`, `verification_requirements`.

**Prompt risks.** requests prolonged smear anatomy without a recovery frame; stacks blur, cloth, overlap, and extreme foreshortening; does not distinguish intentional deformation from invalid anatomy.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### L.68 — Joint inversion or impossible articulation

**Failure ID:** `failure://l/joint_inversion/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B016], [B032], [B042]

**Trigger.** Extreme pose, rapid rotation, or stylized perspective challenges joint geometry.

**Observable symptom.** Elbows, knees, wrists, or spine bend incorrectly.

**Likely cause.** The generator prioritizes local appearance and motion over biomechanical constraints. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use pose constraints or source motion and verify joint-angle plausibility; simplify the pose when detectors and humans disagree.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_anatomical_validity` is the primary metric; companion checks: `metric_deformation_duration`, `metric_recovery_frame_accuracy`, `metric_silhouette_readability`.

**Compiler/score impact.** `motion`, `style`, `performance`, `continuity.anatomy_state`, `verification_requirements`.

**Prompt risks.** requests prolonged smear anatomy without a recovery frame; stacks blur, cloth, overlap, and extreme foreshortening; does not distinguish intentional deformation from invalid anatomy.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### L.69 — Smear deformation persists beyond the accent

**Failure ID:** `failure://l/persistent_smear_anatomy/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B010], [B016], [B032], [B042]

**Trigger.** Anime smear frames or motion trails are requested.

**Observable symptom.** Elongated limbs, duplicated features, or distorted body shapes remain after the intended smear.

**Likely cause.** The model lacks an explicit recovery frame and treats stylization as a continuing state. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Define deformation onset/end and a required anatomy recovery keyframe; add one-frame smears in post when exact duration is required.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_anatomical_validity` is the primary metric; companion checks: `metric_deformation_duration`, `metric_recovery_frame_accuracy`, `metric_silhouette_readability`.

**Compiler/score impact.** `motion`, `style`, `performance`, `continuity.anatomy_state`, `verification_requirements`.

**Prompt risks.** requests prolonged smear anatomy without a recovery frame; stacks blur, cloth, overlap, and extreme foreshortening; does not distinguish intentional deformation from invalid anatomy.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### L.70 — Perspective enlargement persists

**Failure ID:** `failure://l/perspective_deformation_persists/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B016], [B031], [B032], [B042]

**Trigger.** A fist, foot, or face moves close to lens for a stylized accent.

**Observable symptom.** The enlarged body part stays disproportionate after moving away.

**Likely cause.** Perspective effect is absorbed into entity appearance rather than a transient camera-relative deformation. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Bind deformation to camera distance and interval, then require a normal-proportion recovery state.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_anatomical_validity` is the primary metric; companion checks: `metric_deformation_duration`, `metric_recovery_frame_accuracy`, `metric_silhouette_readability`.

**Compiler/score impact.** `motion`, `style`, `performance`, `continuity.anatomy_state`, `verification_requirements`.

**Prompt risks.** requests prolonged smear anatomy without a recovery frame; stacks blur, cloth, overlap, and extreme foreshortening; does not distinguish intentional deformation from invalid anatomy.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### L.71 — Failed anatomy reconnection after occlusion

**Failure ID:** `failure://l/failed_anatomy_reconnection/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B013], [B016], [B019], [B032], [B042]

**Trigger.** Limbs cross behind body/cloth/effects and re-emerge.

**Observable symptom.** A limb reconnects to the wrong side or body.

**Likely cause.** Occluded joints lose persistent identity and local correspondence. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use joint/pose tracks, partial visibility anchors, and a post-occlusion anatomy checkpoint.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_anatomical_validity` is the primary metric; companion checks: `metric_deformation_duration`, `metric_recovery_frame_accuracy`, `metric_silhouette_readability`.

**Compiler/score impact.** `motion`, `style`, `performance`, `continuity.anatomy_state`, `verification_requirements`.

**Prompt risks.** requests prolonged smear anatomy without a recovery frame; stacks blur, cloth, overlap, and extreme foreshortening; does not distinguish intentional deformation from invalid anatomy.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### L.72 — Stylization destroys action readability

**Failure ID:** `failure://l/stylization_readability_loss/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B010], [B016], [B032], [B042]

**Trigger.** Smears, holds, speed lines, flashes, and deformation stack in the same interval.

**Observable symptom.** The primary pose, target, direction, or contact cannot be read.

**Likely cause.** Multiple graphic accents compete with the causal skeleton and silhouette. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Retain one readable setup, contact/apex, and recovery pose; distribute accents across shots or post layers.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_anatomical_validity` is the primary metric; companion checks: `metric_deformation_duration`, `metric_recovery_frame_accuracy`, `metric_silhouette_readability`.

**Compiler/score impact.** `motion`, `style`, `performance`, `continuity.anatomy_state`, `verification_requirements`.

**Prompt risks.** requests prolonged smear anatomy without a recovery frame; stacks blur, cloth, overlap, and extreme foreshortening; does not distinguish intentional deformation from invalid anatomy.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
