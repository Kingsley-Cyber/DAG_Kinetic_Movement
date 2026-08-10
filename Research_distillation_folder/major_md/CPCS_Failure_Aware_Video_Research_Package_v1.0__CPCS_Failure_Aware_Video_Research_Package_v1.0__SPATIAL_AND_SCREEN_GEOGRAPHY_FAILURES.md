# Spatial and Screen-Geography Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Unqualified left/right and position descriptions collapse actor-relative, viewer-relative, camera-relative, and world-relative coordinates. A shot can satisfy a screen-space phrase while violating world geometry or the action axis.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| D | Spatial reasoning and screen geography | 6 | scenes + shots + actions + camera + verification | metric_screen_direction_consistency, metric_depth_order_accuracy, metric_trajectory_target_error, metric_eyeline_consistency |

## Canonical contract implications

Use the Spatial State Transition Contract: coordinate frame, camera state, before/after world and screen relations, trajectories, screen/depth lanes, target regions, axis and eyeline invariants, and explicit transforms across pans, orbits, reverse angles, and cuts.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### D.19 — Viewer-, actor-, and world-left confusion

**Failure ID:** `failure://d/left_right_frame_confusion/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B031], [B035], [B036], [B037], [B040]

**Trigger.** A prompt uses left/right without naming the coordinate frame.

**Observable symptom.** Motion or placement occurs in the opposite direction.

**Likely cause.** Natural language under-specifies whether direction is viewer-, camera-, actor-, or world-relative. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Normalize every direction to an explicit coordinate frame and compile provider prose from canonical screen/world coordinates.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_depth_order_accuracy` is the primary metric; companion checks: `metric_eyeline_consistency`, `metric_screen_direction_consistency`, `metric_trajectory_target_error`.

**Compiler/score impact.** `scenes`, `shots`, `actions`, `camera`, `continuity.spatial_state`, `verification_requirements`.

**Prompt risks.** uses left or right without a coordinate frame; combines camera-side crossing with directional action; specifies endpoints without depth or path.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### D.20 — Axis reversal after cut

**Failure ID:** `failure://d/axis_reversal_after_cut/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B031], [B035], [B036], [B037], [B040]

**Trigger.** A reverse angle, orbit, or cut changes camera side during two-actor action.

**Observable symptom.** Attack direction, gaze, or travel reverses without an authored crossing.

**Likely cause.** The 180-degree action axis is not represented as persistent world geometry. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Lock the action axis, prohibit unmotivated camera-side crossing, or insert a neutral bridge shot that re-establishes geography.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_depth_order_accuracy` is the primary metric; companion checks: `metric_eyeline_consistency`, `metric_screen_direction_consistency`, `metric_trajectory_target_error`.

**Compiler/score impact.** `scenes`, `shots`, `actions`, `camera`, `continuity.spatial_state`, `verification_requirements`.

**Prompt risks.** uses left or right without a coordinate frame; combines camera-side crossing with directional action; specifies endpoints without depth or path.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### D.21 — Depth-order inversion

**Failure ID:** `failure://d/depth_order_inversion/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B016], [B018], [B031], [B035], [B036], [B037], [B040]

**Trigger.** Actors or props overlap, camera parallax is weak, or effects obscure boundaries.

**Observable symptom.** Foreground/background ordering flips or an actor passes through another layer.

**Likely cause.** Depth is inferred ambiguously from 2D appearance without an explicit depth map or lane. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use depth lanes, masks, depth maps, and minimum-separation constraints; verify ordering at overlap frames.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_depth_order_accuracy` is the primary metric; companion checks: `metric_eyeline_consistency`, `metric_screen_direction_consistency`, `metric_trajectory_target_error`.

**Compiler/score impact.** `scenes`, `shots`, `actions`, `camera`, `continuity.spatial_state`, `verification_requirements`.

**Prompt risks.** uses left or right without a coordinate frame; combines camera-side crossing with directional action; specifies endpoints without depth or path.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### D.22 — Trajectory misses target region

**Failure ID:** `failure://d/trajectory_target_miss/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B019], [B020], [B031], [B035], [B036], [B037], [B038], [B040]

**Trigger.** A fast actor/object follows a curved, airborne, or partially hidden path.

**Observable symptom.** The subject lands, strikes, or exits at the wrong region.

**Likely cause.** Text describes intent but not a measurable spatiotemporal path. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Provide point/pose trajectory or storyboard keyframes with time-indexed target regions; fail to shot decomposition when tolerance is tight.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_depth_order_accuracy` is the primary metric; companion checks: `metric_eyeline_consistency`, `metric_screen_direction_consistency`, `metric_trajectory_target_error`.

**Compiler/score impact.** `scenes`, `shots`, `actions`, `camera`, `continuity.spatial_state`, `verification_requirements`.

**Prompt risks.** uses left or right without a coordinate frame; combines camera-side crossing with directional action; specifies endpoints without depth or path.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### D.23 — Entrance and exit mismatch

**Failure ID:** `failure://d/entrance_exit_mismatch/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B015], [B031], [B035], [B036], [B037], [B040]

**Trigger.** A subject leaves one shot and enters another after a camera change.

**Observable symptom.** Entry side, direction, scale, or depth lane conflicts with the previous exit.

**Likely cause.** Shot-local coordinates are not transformed through a shared world state. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Record exit world state and compile the next shot's entrance through the camera transform; verify directional continuity.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_depth_order_accuracy` is the primary metric; companion checks: `metric_eyeline_consistency`, `metric_screen_direction_consistency`, `metric_trajectory_target_error`.

**Compiler/score impact.** `scenes`, `shots`, `actions`, `camera`, `continuity.spatial_state`, `verification_requirements`.

**Prompt risks.** uses left or right without a coordinate frame; combines camera-side crossing with directional action; specifies endpoints without depth or path.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### D.24 — Eyeline and gaze-target mismatch

**Failure ID:** `failure://d/eyeline_mismatch/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B031], [B033], [B035], [B036], [B037], [B040]

**Trigger.** Dialogue or reaction shots isolate actors in close-up.

**Observable symptom.** Actors look to the wrong side or at the wrong height/depth.

**Likely cause.** Gaze target is omitted or screen geometry is reconstructed independently per shot. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Bind gaze_target_id and screen target, use matching reference frames, and verify gaze ray/target intersection with human calibration.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_depth_order_accuracy` is the primary metric; companion checks: `metric_eyeline_consistency`, `metric_screen_direction_consistency`, `metric_trajectory_target_error`.

**Compiler/score impact.** `scenes`, `shots`, `actions`, `camera`, `continuity.spatial_state`, `verification_requirements`.

**Prompt risks.** uses left or right without a coordinate frame; combines camera-side crossing with directional action; specifies endpoints without depth or path.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
