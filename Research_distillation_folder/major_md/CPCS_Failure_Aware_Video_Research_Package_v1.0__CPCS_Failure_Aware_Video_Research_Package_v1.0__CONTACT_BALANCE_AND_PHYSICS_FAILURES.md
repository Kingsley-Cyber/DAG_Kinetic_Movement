# Contact, Balance, Support, and Physics Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Visual overlap is not physical contact, and cinematic plausibility is not a conservation or support solver. Prompt-only generation should not promise exact grip, collision-free geometry, support, momentum, landing, or reaction latency without appropriate control and measurement.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| G | Contact, penetration, and interaction geometry | 6 | interactions + motion + camera + verification | metric_contact_distance_error, metric_penetration_duration, metric_contact_target_accuracy, metric_limb_separability |
| H | Balance, support, weight, and momentum | 6 | motion + interactions + verification | metric_foot_slip_distance, metric_support_state_consistency, metric_momentum_discontinuity, metric_landing_stability |

## Canonical contract implications

Extend existing `interactions` and `motion` fields with contact type, target region, interval, minimum separation, allowed screen-space cheat, support state, base of support, takeoff/flight/landing, momentum/recoil/recovery, and verification lanes. Distinguish physical contact, staged near-contact, camera-cheated contact, effect-obscured contact, grasp/support, and surface contact.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### G.37 — False contact

**Failure ID:** `failure://g/false_contact/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B016], [B025], [B032], [B038], [B043]

**Trigger.** Two actors approach rapidly or projected silhouettes overlap.

**Observable symptom.** A hit or grasp is implied although world-space separation remains large.

**Likely cause.** Screen overlap is mistaken for physical contact and perspective masks depth. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Specify near-contact versus contact, target region, minimum/maximum distance, and camera-cheated overlap; use pose/depth controls for exact interaction.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_contact_distance_error` is the primary metric; companion checks: `metric_contact_target_accuracy`, `metric_limb_separability`, `metric_penetration_duration`.

**Compiler/score impact.** `interactions`, `motion`, `camera`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** uses hit or grab without distinguishing contact from near-contact; omits target body region and contact interval; combines close contact with heavy blur or occlusion.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### G.38 — Missing required contact

**Failure ID:** `failure://g/missing_contact/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B025], [B032], [B036], [B038], [B043]

**Trigger.** A handoff, grasp, support, strike, or landing is partly occluded or fast.

**Observable symptom.** Bodies or objects stop short, float apart, or pass without touching.

**Likely cause.** Contact is a short low-duration constraint with weak frame-level supervision. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Provide a contact keyframe/pose, reserve readable approach and consequence frames, and verify the target region at the declared contact interval.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_contact_distance_error` is the primary metric; companion checks: `metric_contact_target_accuracy`, `metric_limb_separability`, `metric_penetration_duration`.

**Compiler/score impact.** `interactions`, `motion`, `camera`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** uses hit or grab without distinguishing contact from near-contact; omits target body region and contact interval; combines close contact with heavy blur or occlusion.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### G.39 — Body or limb penetration

**Failure ID:** `failure://g/body_penetration/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B016], [B018], [B019], [B025], [B032], [B038], [B043]

**Trigger.** Close combat, grapples, crossed limbs, or rapid camera motion reduce silhouette separation.

**Observable symptom.** Limbs pass through torsos, actors interpenetrate, or body ownership becomes ambiguous.

**Likely cause.** The 2D generator lacks hard 3D collision constraints and instance boundaries overlap. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use pose/depth/mask controls, maintain silhouette readability, or stage camera-cheated near-contact and add impact effects in post.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_contact_distance_error` is the primary metric; companion checks: `metric_contact_target_accuracy`, `metric_limb_separability`, `metric_penetration_duration`.

**Compiler/score impact.** `interactions`, `motion`, `camera`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** uses hit or grab without distinguishing contact from near-contact; omits target body region and contact interval; combines close contact with heavy blur or occlusion.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### G.40 — Grip and support drift

**Failure ID:** `failure://g/grip_drift/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B019], [B020], [B025], [B032], [B038], [B043]

**Trigger.** A hand carries, turns, or supports a prop across motion.

**Observable symptom.** Grip point slides, fingers detach, or the object changes orientation independently.

**Likely cause.** Grasp/contact is not modeled as a persistent constraint across frames. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Track grip anchor and object transform, use source-video/pose guidance, and isolate the manipulation shot.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_contact_distance_error` is the primary metric; companion checks: `metric_contact_target_accuracy`, `metric_limb_separability`, `metric_penetration_duration`.

**Compiler/score impact.** `interactions`, `motion`, `camera`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** uses hit or grab without distinguishing contact from near-contact; omits target body region and contact interval; combines close contact with heavy blur or occlusion.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### G.41 — Incorrect contact body part or region

**Failure ID:** `failure://g/wrong_contact_target/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B025], [B032], [B033], [B038], [B043]

**Trigger.** A prompt states a general hit/grab without a spatial target.

**Observable symptom.** Contact lands on the wrong limb, side, or object region.

**Likely cause.** Language describes event category but not target geometry. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Encode target_region in actor-local coordinates plus allowed screen tolerance; use a contact keyframe for precise choreography.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_contact_distance_error` is the primary metric; companion checks: `metric_contact_target_accuracy`, `metric_limb_separability`, `metric_penetration_duration`.

**Compiler/score impact.** `interactions`, `motion`, `camera`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** uses hit or grab without distinguishing contact from near-contact; omits target body region and contact interval; combines close contact with heavy blur or occlusion.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### G.42 — Interaction-distance drift

**Failure ID:** `failure://g/interaction_distance_drift/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B025], [B031], [B032], [B035], [B037], [B038], [B043]

**Trigger.** Dialogue, handoffs, dances, or combat continue during dolly/zoom/orbit motion.

**Observable symptom.** Actors become too close/far or collision distance changes without locomotion.

**Likely cause.** Camera-scale changes are entangled with inferred world-space spacing. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Separate world distance from screen size, constrain actor trajectories, and verify with depth/pose estimates plus human review.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_contact_distance_error` is the primary metric; companion checks: `metric_contact_target_accuracy`, `metric_limb_separability`, `metric_penetration_duration`.

**Compiler/score impact.** `interactions`, `motion`, `camera`, `constraints.hard`, `verification_requirements`.

**Prompt risks.** uses hit or grab without distinguishing contact from near-contact; omits target body region and contact interval; combines close contact with heavy blur or occlusion.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### H.43 — Foot skating

**Failure ID:** `failure://h/foot_skating/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B021], [B025], [B032], [B044], [B045]

**Trigger.** Walking, pivots, landings, or stance holds occur while the camera or background moves.

**Observable symptom.** A planted foot slides relative to the surface.

**Likely cause.** Generated limb motion and global translation are not constrained by a persistent contact point. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use pose/source-video guidance, encode planted-foot intervals, and measure foot-to-ground optical-flow residual.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_foot_slip_distance` is the primary metric; companion checks: `metric_landing_stability`, `metric_momentum_discontinuity`, `metric_support_state_consistency`.

**Compiler/score impact.** `motion`, `interactions`, `actions`, `verification_requirements`.

**Prompt risks.** specifies only motion endpoints; omits support contacts and recovery; demands instant stylized direction changes without a causal skeleton.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### H.44 — Missing support foot or base of support

**Failure ID:** `failure://h/missing_support/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B032], [B044], [B045]

**Trigger.** A body leans, kicks, carries weight, or changes direction.

**Observable symptom.** The body floats or remains stable without a supporting foot/hand/contact.

**Likely cause.** Support state and center-of-mass relation are absent from the condition. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Encode support contacts and transfer order; require a readable base of support or use source-motion control.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_foot_slip_distance` is the primary metric; companion checks: `metric_landing_stability`, `metric_momentum_discontinuity`, `metric_support_state_consistency`.

**Compiler/score impact.** `motion`, `interactions`, `actions`, `verification_requirements`.

**Prompt risks.** specifies only motion endpoints; omits support contacts and recovery; demands instant stylized direction changes without a causal skeleton.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### H.45 — Weightless takeoff or landing

**Failure ID:** `failure://h/weightless_takeoff_landing/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B032], [B044], [B045]

**Trigger.** Jumping, diving, falling, or anime launches involve large vertical motion.

**Observable symptom.** No compression/push-off, acceleration, impact, deceleration, or settle is visible.

**Likely cause.** The model prioritizes trajectory appearance over force-bearing phases. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Separate anticipation, takeoff, flight, contact, deceleration, and settle; retain a causal skeleton even under stylization.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_foot_slip_distance` is the primary metric; companion checks: `metric_landing_stability`, `metric_momentum_discontinuity`, `metric_support_state_consistency`.

**Compiler/score impact.** `motion`, `interactions`, `actions`, `verification_requirements`.

**Prompt risks.** specifies only motion endpoints; omits support contacts and recovery; demands instant stylized direction changes without a causal skeleton.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### H.46 — Momentum disappearance or reversal

**Failure ID:** `failure://h/momentum_discontinuity/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B032], [B044], [B045]

**Trigger.** A fast actor/object changes direction, collides, or crosses an edit.

**Observable symptom.** Velocity changes instantly or momentum vanishes between frames.

**Likely cause.** No explicit velocity/impulse state persists across the event or cut. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use trajectory/control video and encode pre/post velocity plus impulse event; split at impact for compositing when needed.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_foot_slip_distance` is the primary metric; companion checks: `metric_landing_stability`, `metric_momentum_discontinuity`, `metric_support_state_consistency`.

**Compiler/score impact.** `motion`, `interactions`, `actions`, `verification_requirements`.

**Prompt risks.** specifies only motion endpoints; omits support contacts and recovery; demands instant stylized direction changes without a causal skeleton.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### H.47 — Constant-speed motion without acceleration profile

**Failure ID:** `failure://h/constant_speed_motion/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B004], [B005], [B025], [B032], [B044], [B045]

**Trigger.** A fall, swing, throw, or recoil is described only by endpoints.

**Observable symptom.** Motion traverses the path at visually uniform speed.

**Likely cause.** Endpoint or semantic conditioning lacks an authored timing/easing profile. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Encode anticipation, acceleration, apex, deceleration, overshoot, and settle timing; verify phase durations.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_foot_slip_distance` is the primary metric; companion checks: `metric_landing_stability`, `metric_momentum_discontinuity`, `metric_support_state_consistency`.

**Compiler/score impact.** `motion`, `interactions`, `actions`, `verification_requirements`.

**Prompt risks.** specifies only motion endpoints; omits support contacts and recovery; demands instant stylized direction changes without a causal skeleton.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### H.48 — Impossible recovery or balance regain

**Failure ID:** `failure://h/impossible_recovery/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B032], [B044], [B045]

**Trigger.** An actor lands off-center, is struck, or changes direction sharply.

**Observable symptom.** The actor instantly returns to a stable pose without corrective steps or support transfer.

**Likely cause.** Recovery is low-salience and the model samples a canonical stable pose. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Reserve recovery time, specify corrective support steps, or end the shot at impact and generate recovery separately.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_foot_slip_distance` is the primary metric; companion checks: `metric_landing_stability`, `metric_momentum_discontinuity`, `metric_support_state_consistency`.

**Compiler/score impact.** `motion`, `interactions`, `actions`, `verification_requirements`.

**Prompt risks.** specifies only motion endpoints; omits support contacts and recovery; demands instant stylized direction changes without a causal skeleton.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
