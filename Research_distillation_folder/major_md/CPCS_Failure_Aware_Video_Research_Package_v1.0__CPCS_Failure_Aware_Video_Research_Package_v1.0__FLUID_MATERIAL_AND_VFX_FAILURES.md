# Fluid, Material, Cloth, Hair, Debris, and VFX Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Solid-fluid and other material transitions combine hidden state, effect generation, topology, causality, and persistence. A model can create a visually plausible splash while placing it before contact, centering it on the wrong subject, changing the water plane, or using the effect to reconstruct anatomy.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| I | Fluid, cloth, hair, debris, and material interaction | 6 | interactions + style + continuity + verification | metric_material_response_consistency, metric_effect_origin_error, metric_surface_topology_stability, metric_effect_persistence_error |

## Canonical contract implications

Represent material class, source entity, impact point, onset/apex/decay, displacement region, topology invariants, allowed secondary particles, visibility effects, and terminal state. When exact effect origin/topology is hard, generate a clean interaction plate and composite the effect deterministically.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### I.49 — Solid-fluid boundary error

**Failure ID:** `failure://i/solid_fluid_boundary_error/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B010], [B025], [B027], [B045]

**Trigger.** An actor enters, strikes, stands on, or emerges from water/mud/snow.

**Observable symptom.** Fluid behaves as a rigid plane or fails to admit/displace the body.

**Likely cause.** The model lacks explicit material-state and boundary-condition constraints. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Separate pre-contact, contact/effect, and submerged/post-contact shots; use source/control media or composite the fluid interaction.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_effect_origin_error` is the primary metric; companion checks: `metric_effect_persistence_error`, `metric_material_response_consistency`, `metric_surface_topology_stability`.

**Compiler/score impact.** `interactions`, `style`, `continuity.material_state`, `actions`, `verification_requirements`.

**Prompt risks.** treats material effects as decorations rather than causal responses; omits surface contact and displacement order; requires opaque fluid effects and exact hidden identity in one pass.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### I.50 — Splash before displacement

**Failure ID:** `failure://i/splash_before_displacement/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B010], [B025], [B027], [B045]

**Trigger.** A fast body or object approaches water and the splash is salient in the prompt.

**Observable symptom.** The splash begins before surface contact.

**Likely cause.** Effect semantics are associated with entry but not tied to a contact frame. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Bind surface contact, displacement onset, splash onset, and ripple onset to ordered causal events.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_effect_origin_error` is the primary metric; companion checks: `metric_effect_persistence_error`, `metric_material_response_consistency`, `metric_reaction_latency`, `metric_surface_topology_stability`.

**Compiler/score impact.** `interactions`, `style`, `continuity.material_state`, `actions`, `verification_requirements`.

**Prompt risks.** treats material effects as decorations rather than causal responses; omits surface contact and displacement order; requires opaque fluid effects and exact hidden identity in one pass.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### I.51 — Splash or water column follows the actor

**Failure ID:** `failure://i/splash_origin_drift/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B010], [B019], [B020], [B025], [B027], [B038], [B045]

**Trigger.** An actor dives away while another impact creates a water column.

**Observable symptom.** The effect follows the hidden actor or originates from the wrong point.

**Likely cause.** The effect is bound to the most salient subject rather than the causal impact anchor. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Track the impact point with a mask/point and composite or regenerate the localized effect independently.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_effect_origin_error` is the primary metric; companion checks: `metric_effect_persistence_error`, `metric_material_response_consistency`, `metric_surface_topology_stability`.

**Compiler/score impact.** `interactions`, `style`, `continuity.material_state`, `actions`, `verification_requirements`.

**Prompt risks.** treats material effects as decorations rather than causal responses; omits surface contact and displacement order; requires opaque fluid effects and exact hidden identity in one pass.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### I.52 — Submerged subject disappearance

**Failure ID:** `failure://i/submerged_subject_disappearance/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B010], [B013], [B014], [B017], [B025], [B027], [B045]

**Trigger.** A character passes below an opaque or reflective surface.

**Observable symptom.** The subject vanishes permanently, duplicates, or returns without a continuous path.

**Likely cause.** Complete occlusion removes all identity and trajectory evidence. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Keep bubbles, silhouette, refraction cue, mask, or trajectory control; otherwise cut on entry and establish the underwater shot from a reference state.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_effect_origin_error` is the primary metric; companion checks: `metric_effect_persistence_error`, `metric_hidden_path_consistency`, `metric_material_response_consistency`, `metric_surface_topology_stability`.

**Compiler/score impact.** `interactions`, `style`, `continuity.material_state`, `actions`, `verification_requirements`.

**Prompt risks.** treats material effects as decorations rather than causal responses; omits surface contact and displacement order; requires opaque fluid effects and exact hidden identity in one pass.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### I.53 — Material effect spawns anatomy or duplicate faces

**Failure ID:** `failure://i/material_effect_anatomy_spawn/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B010], [B016], [B018], [B025], [B027], [B032], [B045]

**Trigger.** Dense splash, smoke, cloth, hair, or debris overlaps a face/body.

**Observable symptom.** Faces, hands, limbs, or bodies appear inside the effect.

**Likely cause.** Texture and anatomy priors become entangled in ambiguous high-frequency regions. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L6 (postproduction/compositing).** Render the effect as a separate layer or add it in post; preserve actor masks and verify actor count before compositing.

**Fallback — L8 (provider/model substitution).** Use a provider/model with an officially documented control input matching the missing constraint and rerun qualification.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_effect_origin_error`, `metric_effect_persistence_error`, `metric_material_response_consistency`, `metric_surface_topology_stability`.

**Compiler/score impact.** `interactions`, `style`, `continuity.material_state`, `actions`, `verification_requirements`.

**Prompt risks.** treats material effects as decorations rather than causal responses; omits surface contact and displacement order; requires opaque fluid effects and exact hidden identity in one pass.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### I.54 — Material topology or persistence drift

**Failure ID:** `failure://i/environment_material_state_drift/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B004], [B005], [B010], [B025], [B027], [B028], [B045]

**Trigger.** Waterline, mud, snow, debris, cloth damage, or wetness persists across time/cuts.

**Observable symptom.** Surface height, ripple center, wetness, tear, or debris state resets or moves.

**Likely cause.** Material state is not carried in a persistent ledger and effects outlive or detach from causes. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Record material state deltas, anchor effect regions, and use continuity plates or postproduction for persistent damage/wetness.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_effect_origin_error` is the primary metric; companion checks: `metric_effect_persistence_error`, `metric_material_response_consistency`, `metric_surface_topology_stability`.

**Compiler/score impact.** `interactions`, `style`, `continuity.material_state`, `actions`, `verification_requirements`.

**Prompt risks.** treats material effects as decorations rather than causal responses; omits surface contact and displacement order; requires opaque fluid effects and exact hidden identity in one pass.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
