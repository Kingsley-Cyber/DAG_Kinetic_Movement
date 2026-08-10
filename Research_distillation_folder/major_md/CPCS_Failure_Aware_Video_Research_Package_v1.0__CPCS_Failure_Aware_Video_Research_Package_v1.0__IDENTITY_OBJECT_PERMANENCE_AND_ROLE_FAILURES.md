# Identity, Object Permanence, and Role Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Identity and persistence failures are binding failures across time: the system must keep stable entities, attributes, roles, counts, possession, and irreversible state deltas even when appearance, screen side, visibility, or shot context changes.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| B | Object permanence and state persistence | 6 | entities + continuity + verification | metric_object_count_consistency, metric_state_transition_accuracy, metric_material_attribute_stability, metric_environment_layout_consistency |
| C | Identity, role, and actor assignment | 6 | entities + interactions + continuity + verification | metric_identity_continuity, metric_role_assignment_accuracy, metric_screen_side_consistency, metric_voice_identity_consistency |

## Canonical contract implications

Use a State Ledger and identity/role ledger under existing `entities`, `interactions`, and `continuity` owners. Bind every action to persistent initiator and target IDs; keep screen lanes and world identity distinct; represent object possession as release/acquire transitions; treat reflections and duplicates as typed entities, not appearance variants.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### B.07 — Persistent object disappearance

**Failure ID:** `failure://b/object_disappearance/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B002], [B011], [B012], [B015], [B027], [B028], [B042]

**Trigger.** A prop becomes small, briefly hidden, passed between hands, or de-emphasized by the camera.

**Observable symptom.** The prop vanishes before the canonical removal event.

**Likely cause.** Object memory and salience fall below competing scene content. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Use a dedicated reference/asset binding, state-ledger presence invariant, and object-specific verification track.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_environment_layout_consistency` is the primary metric; companion checks: `metric_material_attribute_stability`, `metric_object_count_consistency`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `entities`, `continuity.state_ledger`, `assets`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** omits the complete initial inventory; describes an irreversible state change without a persistent end-state lock; expects exact product geometry from text alone.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### B.08 — Spontaneous object creation

**Failure ID:** `failure://b/spontaneous_object_creation/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B011], [B012], [B015], [B027], [B028], [B041], [B042]

**Trigger.** The prompt implies an interaction but omits the required prop's introduction or exact count.

**Observable symptom.** A new prop, weapon, product, or environmental element appears without an event.

**Likely cause.** The model fills causal or semantic gaps with statistically likely objects. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Declare the complete initial inventory and event-scoped creation/destruction permissions; reject undeclared count increases.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_environment_layout_consistency` is the primary metric; companion checks: `metric_material_attribute_stability`, `metric_object_count_consistency`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `entities`, `continuity.state_ledger`, `assets`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** omits the complete initial inventory; describes an irreversible state change without a persistent end-state lock; expects exact product geometry from text alone.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### B.09 — Object-state reset

**Failure ID:** `failure://b/state_reset/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B011], [B012], [B014], [B015], [B027], [B028], [B042]

**Trigger.** An object changes state, then is occluded, cut away from, or revisited.

**Observable symptom.** Open becomes closed, broken becomes intact, wet becomes dry, or consumed material returns.

**Likely cause.** The generator re-samples a prototypical object rather than preserving an irreversible state delta. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Represent state transitions as irreversible ledger deltas with validity intervals and post-transition reference frames.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_environment_layout_consistency` is the primary metric; companion checks: `metric_material_attribute_stability`, `metric_object_count_consistency`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `entities`, `continuity.state_ledger`, `assets`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** omits the complete initial inventory; describes an irreversible state change without a persistent end-state lock; expects exact product geometry from text alone.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### B.10 — Size, color, or material drift

**Failure ID:** `failure://b/size_material_drift/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B002], [B011], [B012], [B015], [B016], [B027], [B028], [B042]

**Trigger.** A product or prop rotates, changes depth, becomes partially hidden, or crosses shots.

**Observable symptom.** Dimensions, logo placement, color, or material changes.

**Likely cause.** Appearance features are not bound to a stable entity representation across viewpoints. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Use orthographic/reference views or a product sheet, freeze non-negotiable attributes, and use video-to-video or compositing for exact product geometry.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_environment_layout_consistency` is the primary metric; companion checks: `metric_material_attribute_stability`, `metric_object_count_consistency`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `entities`, `continuity.state_ledger`, `assets`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** omits the complete initial inventory; describes an irreversible state change without a persistent end-state lock; expects exact product geometry from text alone.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### B.11 — Hand-object detachment

**Failure ID:** `failure://b/hand_object_detachment/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B011], [B012], [B015], [B027], [B028], [B032], [B038], [B042]

**Trigger.** A hand manipulates, rotates, passes, or rapidly moves a held item.

**Observable symptom.** The object floats, penetrates the hand, changes hands without a pass, or lags behind the grip.

**Likely cause.** Grasp state and contact point are not explicitly represented and fast interaction exceeds local binding stability. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Provide pose/trajectory or source-video motion; encode hand, grip region, contact interval, and transfer event; isolate product close-ups.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_contact_distance_error` is the primary metric; companion checks: `metric_environment_layout_consistency`, `metric_material_attribute_stability`, `metric_object_count_consistency`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `entities`, `continuity.state_ledger`, `assets`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** omits the complete initial inventory; describes an irreversible state change without a persistent end-state lock; expects exact product geometry from text alone.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### B.12 — Environmental layout drift

**Failure ID:** `failure://b/environment_layout_drift/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B011], [B012], [B015], [B027], [B028], [B031], [B040], [B042]

**Trigger.** A camera move, cut, or multi-shot sequence revisits the same room or terrain.

**Observable symptom.** Doors, cliffs, furniture, waterline, or background geometry move or change count.

**Likely cause.** No explicit persistent scene map anchors layout across view changes. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Use a scene reference board, depth/layout map, or source-video transform; maintain a scene-state ledger and camera/world transform.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_environment_layout_consistency` is the primary metric; companion checks: `metric_material_attribute_stability`, `metric_object_count_consistency`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `entities`, `continuity.state_ledger`, `assets`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** omits the complete initial inventory; describes an irreversible state change without a persistent end-state lock; expects exact product geometry from text alone.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### C.13 — Face and costume drift

**Failure ID:** `failure://c/face_costume_drift/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B002], [B015], [B027], [B028], [B041], [B042]

**Trigger.** A character turns away, is blurred, changes shot scale, or crosses an edit.

**Observable symptom.** Facial structure, hair, costume elements, or accessories change.

**Likely cause.** Identity features are weakly persistent relative to pose, lighting, and style changes. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Use separate character references, stable identity IDs, attribute locks, and post-shot identity checkpoints.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_identity_continuity` is the primary metric; companion checks: `metric_role_assignment_accuracy`, `metric_screen_side_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `entities`, `interactions`, `actions`, `continuity.identity_ledger`, `constraints.continuity_locks`.

**Prompt risks.** uses only relative labels such as the left fighter; gives similar actors indistinguishable appearance cues; omits persistent actor IDs from events.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### C.14 — Actor duplication or fusion

**Failure ID:** `failure://c/actor_duplication_fusion/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B015], [B018], [B019], [B027], [B028], [B041], [B042], [B043]

**Trigger.** Two similar actors overlap, grapple, cross, or enter a high-effect interval.

**Observable symptom.** Two actors become one, one becomes two, or limbs are assigned to the wrong body.

**Likely cause.** Instance binding collapses when silhouettes and appearance cues overlap. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use distinct wardrobe/color/depth lanes, avoid crossings, supply separate masks or pose tracks, and split grapples into readable contact beats.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_identity_continuity`, `metric_role_assignment_accuracy`, `metric_screen_side_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `entities`, `interactions`, `actions`, `continuity.identity_ledger`, `constraints.continuity_locks`.

**Prompt risks.** uses only relative labels such as the left fighter; gives similar actors indistinguishable appearance cues; omits persistent actor IDs from events.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### C.15 — Attacker-defender or speaker-role swap

**Failure ID:** `failure://c/role_swap/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B015], [B017], [B027], [B028], [B033], [B041], [B042], [B043]

**Trigger.** Actors have similar appearance or cross screen positions during a dependent action.

**Observable symptom.** The wrong actor attacks, reacts, speaks, holds the prop, or receives the effect.

**Likely cause.** Role semantics are not anchored to persistent actor IDs and action bindings compete. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Bind every event to initiator_id and target_id, preserve role labels through the event graph, and verify action-to-actor assignment.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_identity_continuity` is the primary metric; companion checks: `metric_role_assignment_accuracy`, `metric_screen_side_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `entities`, `interactions`, `actions`, `continuity.identity_ledger`, `constraints.continuity_locks`.

**Prompt risks.** uses only relative labels such as the left fighter; gives similar actors indistinguishable appearance cues; omits persistent actor IDs from events.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### C.16 — Screen-side identity swap

**Failure ID:** `failure://c/screen_side_identity_swap/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B015], [B027], [B028], [B031], [B035], [B040], [B041], [B042]

**Trigger.** Actors cross, camera orbits, reverse angles are used, or a shot cuts across the axis.

**Observable symptom.** The left actor becomes the right actor without a declared crossing, or identities swap at the cut.

**Likely cause.** Screen-side labels are confused with world identity and camera transform. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Declare world IDs separately from screen lanes, preserve the action axis, and insert a neutral/re-establishing shot before a side reversal.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_identity_continuity` is the primary metric; companion checks: `metric_role_assignment_accuracy`, `metric_screen_side_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `entities`, `interactions`, `actions`, `continuity.identity_ledger`, `constraints.continuity_locks`.

**Prompt risks.** uses only relative labels such as the left fighter; gives similar actors indistinguishable appearance cues; omits persistent actor IDs from events.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### C.17 — Action target confusion

**Failure ID:** `failure://c/target_confusion/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B015], [B027], [B028], [B033], [B038], [B041], [B042], [B043]

**Trigger.** More than one plausible target is visible or interaction lines cross.

**Observable symptom.** An attack, gaze, handoff, effect, or dialogue response lands on the wrong target.

**Likely cause.** Attention binding does not uniquely resolve the event participant graph. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Declare target_id, target region, exclusion targets, and temporal isolation; use bounding/layout controls when multiple candidates remain close.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_identity_continuity` is the primary metric; companion checks: `metric_role_assignment_accuracy`, `metric_screen_side_consistency`, `metric_target_assignment_accuracy`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `entities`, `interactions`, `actions`, `continuity.identity_ledger`, `constraints.continuity_locks`.

**Prompt risks.** uses only relative labels such as the left fighter; gives similar actors indistinguishable appearance cues; omits persistent actor IDs from events.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### C.18 — Voice identity drift

**Failure ID:** `failure://c/voice_identity_drift/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B015], [B022], [B023], [B027], [B028], [B041], [B042], [B046], [M004], [M019]

**Trigger.** Multi-character dialogue spans shots or overlaps with off-screen speech.

**Observable symptom.** Voice timbre, language, accent, or speaker assignment changes.

**Likely cause.** Audio identity is not persistently linked to the visual entity and turn order. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Bind voice references and speaker IDs, encode turn order, and separate speech generation/dubbing when exact identity is required.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_identity_continuity` is the primary metric; companion checks: `metric_role_assignment_accuracy`, `metric_screen_side_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `entities`, `interactions`, `actions`, `continuity.identity_ledger`, `constraints.continuity_locks`.

**Prompt risks.** uses only relative labels such as the left fighter; gives similar actors indistinguishable appearance cues; omits persistent actor IDs from events.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
