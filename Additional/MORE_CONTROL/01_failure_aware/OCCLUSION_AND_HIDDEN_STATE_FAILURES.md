# Occlusion and Hidden-State Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Complete occlusion converts visible continuity into latent-state reconstruction. Prompt-only mitigation can remove lexical ambiguity, but precise identity, count, path, or reappearance obligations require a state contract plus visual control, decomposition, or postproduction.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| A | Occlusion and hidden-state continuity | 6 | continuity + actions + verification | metric_occlusion_reappearance_region_error, metric_actor_count_consistency, metric_identity_continuity, metric_hidden_path_consistency |

## Canonical contract implications

Use the candidate `Occlusion Continuity Contract`: persistent subject ID, pre-occlusion state, occluder, interval, visibility state, hidden path in a declared coordinate frame, expected reappearance region, identity/count locks, allowed/forbidden state changes, visibility bridge, and interval-level verification assertions. Visibility and existence must be separate fields.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### A.01 — Hidden-state reconstruction hallucination

**Failure ID:** `failure://a/hidden_state_reconstruction/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B012], [B013], [B014], [B017], [B027], [B028]

**Trigger.** A subject becomes completely hidden by splash, smoke, debris, darkness, blur, or a foreground object.

**Observable symptom.** The subject returns with an invented pose, action, identity detail, or location.

**Likely cause.** The hidden interval is underdetermined and the generator samples a plausible continuation without an explicit persistent state or trajectory constraint. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Keep a visibility bridge or supply a tracked mask, silhouette, pose path, depth path, or control video; otherwise split before and after the opaque interval.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_hidden_path_consistency`, `metric_identity_continuity`, `metric_occlusion_reappearance_region_error`.

**Compiler/score impact.** `continuity.visibility_intervals`, `continuity.state_ledger`, `actions`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** describes disappearance and reappearance but omits the hidden path; uses a full-frame opaque effect while demanding exact continuity; relies only on negative phrases such as no teleporting.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### A.02 — Subject duplication after opaque occlusion

**Failure ID:** `failure://a/duplicate_after_occlusion/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B002], [B012], [B013], [B014], [B017], [B027], [B028]

**Trigger.** A full-frame effect hides one actor while a second actor or reflection remains visible.

**Observable symptom.** The returning actor coexists with an unintended duplicate or the occluder spawns a face or limb.

**Likely cause.** Entity binding is re-solved from visible evidence after the occlusion and count constraints are weak. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Lock actor count in the canonical state, retain distinct visibility anchors, and verify instance tracks through the effect; move the effect to post when count must be exact.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_hidden_path_consistency`, `metric_identity_continuity`, `metric_occlusion_reappearance_region_error`.

**Compiler/score impact.** `continuity.visibility_intervals`, `continuity.state_ledger`, `actions`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** describes disappearance and reappearance but omits the hidden path; uses a full-frame opaque effect while demanding exact continuity; relies only on negative phrases such as no teleporting.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### A.03 — Identity rewrite under effect cover

**Failure ID:** `failure://a/identity_rewrite_under_effect/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B012], [B013], [B014], [B015], [B016], [B017], [B027], [B028]

**Trigger.** The face, costume, or body is fully hidden by an effect or fast blur.

**Observable symptom.** Hair, face, costume, or body proportions change on reappearance.

**Likely cause.** Reference appearance competes with newly sampled local detail when no visible identity evidence survives. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Use reference-conditioned generation plus a partially visible identity anchor; require an identity checkpoint immediately before and after the cover.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_hidden_path_consistency`, `metric_identity_continuity`, `metric_occlusion_reappearance_region_error`.

**Compiler/score impact.** `continuity.visibility_intervals`, `continuity.state_ledger`, `actions`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** describes disappearance and reappearance but omits the hidden path; uses a full-frame opaque effect while demanding exact continuity; relies only on negative phrases such as no teleporting.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### A.04 — Incorrect reappearance region

**Failure ID:** `failure://a/reappearance_region_error/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B012], [B013], [B014], [B017], [B019], [B020], [B027], [B028]

**Trigger.** A moving subject is fully occluded while continuing to translate or dive.

**Observable symptom.** The subject reappears too early, too late, or in the wrong screen/depth region.

**Likely cause.** The prompt states disappearance and reappearance but not the latent path in a declared coordinate frame. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Encode occlusion start/end, hidden trajectory, expected screen/depth region, and velocity continuity; escalate to trajectory control when tolerance is small.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_hidden_path_consistency`, `metric_identity_continuity`, `metric_occlusion_reappearance_region_error`.

**Compiler/score impact.** `continuity.visibility_intervals`, `continuity.state_ledger`, `actions`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** describes disappearance and reappearance but omits the hidden path; uses a full-frame opaque effect while demanding exact continuity; relies only on negative phrases such as no teleporting.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### A.05 — Occluder-subject fusion

**Failure ID:** `failure://a/occluder_subject_fusion/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B012], [B013], [B014], [B016], [B017], [B018], [B019], [B027], [B028], [B032]

**Trigger.** Hair, cloth, water, smoke, another body, or a foreground prop overlaps the subject for multiple frames.

**Observable symptom.** Materials merge with anatomy, clothing becomes fluid, or two bodies fuse.

**Likely cause.** The model lacks stable layer ownership and boundary evidence during prolonged overlap. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Provide masks or layered control media and preserve a readable silhouette; use compositing for dense particulate or fluid covers.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_hidden_path_consistency`, `metric_identity_continuity`, `metric_limb_separability`, `metric_occlusion_reappearance_region_error`.

**Compiler/score impact.** `continuity.visibility_intervals`, `continuity.state_ledger`, `actions`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** describes disappearance and reappearance but omits the hidden path; uses a full-frame opaque effect while demanding exact continuity; relies only on negative phrases such as no teleporting.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### A.06 — Frame-exit and re-entry state reset

**Failure ID:** `failure://a/frame_exit_reentry_reset/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B012], [B013], [B014], [B015], [B017], [B027], [B028]

**Trigger.** An actor exits the frame or is hidden by a camera whip and returns later.

**Observable symptom.** The actor returns with reset state, wrong prop, changed injury, or reversed role.

**Likely cause.** Off-screen state is not directly observed and recurrence distance weakens entity memory. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Terminate the shot at exit, create an explicit handoff state, and generate re-entry as a new shot from a state/reference keyframe when continuity is hard.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_actor_count_consistency` is the primary metric; companion checks: `metric_hidden_path_consistency`, `metric_identity_continuity`, `metric_occlusion_reappearance_region_error`, `metric_state_transition_accuracy`.

**Compiler/score impact.** `continuity.visibility_intervals`, `continuity.state_ledger`, `actions`, `constraints.continuity_locks`, `verification_requirements`.

**Prompt risks.** describes disappearance and reappearance but omits the hidden path; uses a full-frame opaque effect while demanding exact continuity; relies only on negative phrases such as no teleporting.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
