# Temporal, Action-Order, and Causality Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

A list of desired actions is not an executable event graph. As dependency depth rises, generators may merge, omit, repeat, reverse, or make events simultaneous; effects can then detach from causes or attach to the wrong actor or location.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| E | Temporal order and action-graph collapse | 6 | beats + actions + editing + verification | metric_action_graph_agreement, metric_temporal_event_error, metric_action_omission_rate, metric_recovery_presence |
| F | Causality and reaction | 6 | actions + interactions + effects + verification | metric_causal_edge_agreement, metric_effect_origin_error, metric_reaction_latency, metric_target_assignment_accuracy |

## Canonical contract implications

Represent each event with initiator, target, action, onset, apex, consequence, reaction delay, recovery, and secondary effects. Use hard dependency edges for `before`, `only_after`, `causes`, `prevents`, `while`, and `terminates`. Compile a topological order, preserve setup/recovery windows, and split when the provider/task-specific capacity staircase fails.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### E.25 — Primary action omission

**Failure ID:** `failure://e/action_omission/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B017], [B027], [B029], [B033], [B039], [B043]

**Trigger.** The clip contains many requested events or dependent beats.

**Observable symptom.** One or more required actions never occur.

**Likely cause.** Finite temporal/attention capacity causes lower-priority actions to be dropped. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Reduce to one primary event chain per shot, preserve hard events, and generate separate clips when a provider-specific density staircase fails.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_action_graph_agreement` is the primary metric; companion checks: `metric_action_omission_rate`, `metric_recovery_presence`, `metric_temporal_event_error`.

**Compiler/score impact.** `beats`, `actions`, `editing`, `continuity.event_state`, `verification_requirements`.

**Prompt risks.** packs many dependent verbs into one sentence; omits terminal hold and recovery; assumes textual order is an executable timeline.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### E.26 — Sequential actions merged into one gesture

**Failure ID:** `failure://e/action_merge/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B017], [B027], [B029], [B033], [B039]

**Trigger.** Two or more similar actions occur close together or share actors/effect language.

**Observable symptom.** Setup, action, consequence, or recovery collapse into a single ambiguous movement.

**Likely cause.** The generator compresses semantically related tokens into one visual event. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Use explicit event nodes with non-overlapping intervals and prerequisite edges; include visible setup and settle beats.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_action_graph_agreement` is the primary metric; companion checks: `metric_action_omission_rate`, `metric_recovery_presence`, `metric_temporal_event_error`.

**Compiler/score impact.** `beats`, `actions`, `editing`, `continuity.event_state`, `verification_requirements`.

**Prompt risks.** packs many dependent verbs into one sentence; omits terminal hold and recovery; assumes textual order is an executable timeline.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### E.27 — Unrequested action repetition

**Failure ID:** `failure://e/action_repeat/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B017], [B027], [B029], [B033], [B039]

**Trigger.** Unused duration remains after the main action or a cyclic motion prior is strong.

**Observable symptom.** A strike, gesture, step, or camera move repeats.

**Likely cause.** The model fills time with locally plausible motion and lacks an explicit terminal hold/state. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L1 (structured prompt repair).** Specify the end state and hold duration positively; shorten the generation or freeze the terminal interval in editing.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_action_graph_agreement` is the primary metric; companion checks: `metric_action_omission_rate`, `metric_primary_action_completion`, `metric_recovery_presence`, `metric_temporal_event_error`.

**Compiler/score impact.** `beats`, `actions`, `editing`, `continuity.event_state`, `verification_requirements`.

**Prompt risks.** packs many dependent verbs into one sentence; omits terminal hold and recovery; assumes textual order is an executable timeline.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### E.28 — Event-order reversal

**Failure ID:** `failure://e/event_order_reversal/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B017], [B027], [B029], [B033], [B039]

**Trigger.** The prompt uses compressed clauses or several dependent events.

**Observable symptom.** Reaction precedes cause, impact precedes approach, or recovery precedes landing.

**Likely cause.** Text order is not a guaranteed executable temporal graph and evaluator models may also miss the reversal. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Topologically sort an explicit event graph and compile causal phrases; verify event timestamps with human calibration for fast actions.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_action_graph_agreement` is the primary metric; companion checks: `metric_action_omission_rate`, `metric_recovery_presence`, `metric_temporal_event_error`.

**Compiler/score impact.** `beats`, `actions`, `editing`, `continuity.event_state`, `verification_requirements`.

**Prompt risks.** packs many dependent verbs into one sentence; omits terminal hold and recovery; assumes textual order is an executable timeline.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### E.29 — Recovery or settle omission

**Failure ID:** `failure://e/recovery_omission/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B003], [B004], [B017], [B027], [B029], [B032], [B033], [B039]

**Trigger.** A dynamic action consumes most clip duration.

**Observable symptom.** The actor never lands, regains balance, lowers the arm, or reaches the requested end state.

**Likely cause.** The model allocates duration to salient apex motion and truncates low-salience recovery. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Reserve an explicit recovery interval or separate recovery shot; use first/last frames only when the path remains plausible.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_action_graph_agreement` is the primary metric; companion checks: `metric_action_omission_rate`, `metric_recovery_presence`, `metric_temporal_event_error`.

**Compiler/score impact.** `beats`, `actions`, `editing`, `continuity.event_state`, `verification_requirements`.

**Prompt risks.** packs many dependent verbs into one sentence; omits terminal hold and recovery; assumes textual order is an executable timeline.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### E.30 — Sequential events become simultaneous

**Failure ID:** `failure://e/simultaneity_collapse/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B017], [B027], [B029], [B033], [B039], [B043]

**Trigger.** Multiple actors act concurrently with causal dependencies.

**Observable symptom.** Mutually dependent actions happen at once or turn order disappears.

**Likely cause.** The generation conditions do not enforce partial order under dense multi-actor motion. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Serialize actor turns into separate beats or shots; keep only genuinely simultaneous actions in one interval.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_action_graph_agreement` is the primary metric; companion checks: `metric_action_omission_rate`, `metric_recovery_presence`, `metric_temporal_event_error`.

**Compiler/score impact.** `beats`, `actions`, `editing`, `continuity.event_state`, `verification_requirements`.

**Prompt risks.** packs many dependent verbs into one sentence; omits terminal hold and recovery; assumes textual order is an executable timeline.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### F.31 — Effect occurs before cause

**Failure ID:** `failure://f/effect_before_cause/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B027], [B033], [B038], [B044], [B045]

**Trigger.** A splash, recoil, debris burst, sound, or camera shake accompanies a fast action.

**Observable symptom.** The effect begins before contact or near-contact.

**Likely cause.** The effect token is strongly associated with the action but not anchored to its causal frame. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Declare cause, contact/near-contact frame, effect onset, reaction delay, and recovery as separate event nodes.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_causal_edge_agreement` is the primary metric; companion checks: `metric_effect_origin_error`, `metric_reaction_latency`, `metric_target_assignment_accuracy`.

**Compiler/score impact.** `actions`, `interactions`, `motion`, `audio`, `verification_requirements`.

**Prompt risks.** compresses cause and consequence into a noun list; names an effect without its origin and preconditions; does not identify the reactor.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### F.32 — Effect without a valid cause

**Failure ID:** `failure://f/effect_without_cause/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B027], [B038], [B044], [B045]

**Trigger.** The prompt contains effect imagery but omits the generating interaction or permits filler.

**Observable symptom.** Debris, water, recoil, shake, or damage appears spontaneously.

**Likely cause.** The model satisfies salient effect semantics independently of physical preconditions. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Gate every effect by a named causal event and reject effects whose preconditions are absent; move ornamental effects to post.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_causal_edge_agreement` is the primary metric; companion checks: `metric_effect_origin_error`, `metric_reaction_latency`, `metric_target_assignment_accuracy`.

**Compiler/score impact.** `actions`, `interactions`, `motion`, `audio`, `verification_requirements`.

**Prompt risks.** compresses cause and consequence into a noun list; names an effect without its origin and preconditions; does not identify the reactor.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### F.33 — Effect originates at the wrong location

**Failure ID:** `failure://f/wrong_effect_origin/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B019], [B020], [B025], [B027], [B038], [B044]

**Trigger.** The cause and effect are spatially separated or one actor is occluded.

**Observable symptom.** Splash, dust, sparks, or debris emit from the actor instead of the impact point.

**Likely cause.** The event graph lacks a persistent origin anchor or the model binds effect to the salient subject. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Bind effect_origin to a world/screen region or mask; composite the effect at a tracked point when exact origin matters.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_causal_edge_agreement` is the primary metric; companion checks: `metric_effect_origin_error`, `metric_reaction_latency`, `metric_target_assignment_accuracy`.

**Compiler/score impact.** `actions`, `interactions`, `motion`, `audio`, `verification_requirements`.

**Prompt risks.** compresses cause and consequence into a noun list; names an effect without its origin and preconditions; does not identify the reactor.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### F.34 — Wrong actor reacts

**Failure ID:** `failure://f/wrong_reactor/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B004], [B005], [B025], [B027], [B033], [B038], [B044]

**Trigger.** Several actors are nearby, roles cross, or impact is partly hidden.

**Observable symptom.** A non-target recoils, falls, or speaks.

**Likely cause.** Target binding is ambiguous and reaction semantics are generated independently. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Bind initiator, target, reaction actor, and excluded reactors in the causal graph; isolate the reaction shot if needed.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_causal_edge_agreement` is the primary metric; companion checks: `metric_effect_origin_error`, `metric_reaction_latency`, `metric_target_assignment_accuracy`.

**Compiler/score impact.** `actions`, `interactions`, `motion`, `audio`, `verification_requirements`.

**Prompt risks.** compresses cause and consequence into a noun list; names an effect without its origin and preconditions; does not identify the reactor.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### F.35 — Reaction latency error

**Failure ID:** `failure://f/reaction_latency_error/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B027], [B029], [B032], [B038], [B044], [B046]

**Trigger.** Contact is fast, stylized, obscured, or audio-linked.

**Observable symptom.** Reaction is anticipatory, excessively delayed, or temporally disconnected.

**Likely cause.** No explicit causal latency interval constrains the generated motion. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Encode onset, apex, consequence onset, acceptable latency range, and recovery; verify at frame level.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_causal_edge_agreement` is the primary metric; companion checks: `metric_effect_origin_error`, `metric_reaction_latency`, `metric_target_assignment_accuracy`.

**Compiler/score impact.** `actions`, `interactions`, `motion`, `audio`, `verification_requirements`.

**Prompt risks.** compresses cause and consequence into a noun list; names an effect without its origin and preconditions; does not identify the reactor.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### F.36 — Secondary-effect chain break

**Failure ID:** `failure://f/secondary_effect_chain_break/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B004], [B005], [B025], [B027], [B038], [B044], [B045]

**Trigger.** One impact should create several ordered consequences.

**Observable symptom.** Primary contact occurs but fluid, debris, sound, camera impulse, or environmental response is missing or unordered.

**Likely cause.** Long causal chains exceed reliable event binding and secondary effects compete for attention. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Split the primary interaction from secondary VFX/audio or composite them from tracked anchors; verify each causal edge independently.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_causal_edge_agreement` is the primary metric; companion checks: `metric_effect_origin_error`, `metric_reaction_latency`, `metric_target_assignment_accuracy`.

**Compiler/score impact.** `actions`, `interactions`, `motion`, `audio`, `verification_requirements`.

**Prompt risks.** compresses cause and consequence into a noun list; names an effect without its origin and preconditions; does not identify the reactor.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
