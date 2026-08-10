# Prompt Format, Serialization, and Attention-Budget Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Serialization helps CPCS validate and prioritize meaning; it does not automatically create provider-side structure. Duplicate representations, contradictions, prompt rewriting, and too many simultaneous requirements can dilute or erase hard controls, while under-specification invites filler.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| M | Prompt and serialization | 6 | compiler + provider adapter + experiment registry | metric_field_projection_coverage, metric_prompt_semantic_equivalence, metric_hard_lock_retention, metric_prompt_truncation_loss |
| N | Constraint overload and under-specification | 6 | compiler + loss report + shot planner | metric_instruction_coverage, metric_hallucinated_action_rate, metric_constraint_conflict_count, metric_primary_action_completion |

## Canonical contract implications

Keep canonical JSON authority, compile one provider-native representation, rank information by hard-control value, fail on unresolved conflict or hard-lock overflow, record prompt rewriting, and learn provider/task-specific capacity from repeated-seed staircases. End state, allowed variation, and forbidden new primary actions are mandatory when duration would otherwise be unassigned.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### M.73 — Structured serialization treated as ordinary text

**Failure ID:** `failure://m/structured_format_not_parsed/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [M001], [M002], [M007], [M023], [M025], [R005]

**Trigger.** XML, YAML, or JSON is submitted to an endpoint that documents only a prompt string.

**Observable symptom.** Field boundaries, nesting, keys, or numeric values are ignored inconsistently.

**Likely cause.** The provider has no documented schema parser; structure only changes token sequence and semantic emphasis. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L1 (structured prompt repair).** Keep JSON as CPCS authority, compile one concise provider-native prose prompt, and treat structured serialization as an experiment unless officially supported.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_field_projection_coverage` is the primary metric; companion checks: `metric_hard_lock_retention`, `metric_prompt_semantic_equivalence`, `metric_prompt_truncation_loss`.

**Compiler/score impact.** `provider_neutral_controls`, `provider_realization`, `constraints`, `warnings`, `provenance`.

**Prompt risks.** submits multiple duplicate serializations; assumes a prompt-string endpoint parses XML/YAML/JSON as a schema; places hard locks after low-priority decorative text.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### M.74 — Duplicate-format attention collision

**Failure ID:** `failure://m/duplicate_representation_attention_collision/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B039], [M001], [M002], [M007], [M023], [M025], [R005]

**Trigger.** The same semantics are repeated in prose, XML, JSON, and YAML.

**Observable symptom.** Instructions conflict, fields are omitted, or motion becomes stiff/averaged.

**Likely cause.** Redundant tokens consume prompt budget and introduce slight semantic differences and priority competition. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L1 (structured prompt repair).** Compile exactly one provider-facing representation plus non-submitted verification metadata; A/B-test hybrids instead of assuming benefit.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_field_projection_coverage` is the primary metric; companion checks: `metric_hard_lock_retention`, `metric_instruction_coverage`, `metric_prompt_semantic_equivalence`, `metric_prompt_truncation_loss`.

**Compiler/score impact.** `provider_neutral_controls`, `provider_realization`, `constraints`, `warnings`, `provenance`.

**Prompt risks.** submits multiple duplicate serializations; assumes a prompt-string endpoint parses XML/YAML/JSON as a schema; places hard locks after low-priority decorative text.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### M.75 — Exact numeric values ignored or approximated

**Failure ID:** `failure://m/numeric_control_ignored/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B035], [B037], [M001], [M002], [M007], [M023], [M025], [R004], [R005], [R006]

**Trigger.** Timestamps, angles, speeds, coordinates, or distances are placed only in text.

**Observable symptom.** The output follows qualitative intent but not the requested numbers.

**Likely cause.** Prompt-string conditioning is semantic, not an executable trajectory or simulation constraint. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Project numbers to provider controls when documented; otherwise retain them for verification and use control media or postproduction.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_field_projection_coverage` is the primary metric; companion checks: `metric_hard_lock_retention`, `metric_prompt_semantic_equivalence`, `metric_prompt_truncation_loss`.

**Compiler/score impact.** `provider_neutral_controls`, `provider_realization`, `constraints`, `warnings`, `provenance`.

**Prompt risks.** submits multiple duplicate serializations; assumes a prompt-string endpoint parses XML/YAML/JSON as a schema; places hard locks after low-priority decorative text.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### M.76 — Negative instruction introduces or preserves forbidden content

**Failure ID:** `failure://m/negative_prompt_concept_priming/1`  
**Empirical confidence:** low  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [M001], [M002], [M007], [M023], [M025], [R005]

**Trigger.** The prompt repeatedly names forbidden objects/actions/effects.

**Observable symptom.** The forbidden concept appears or attention is diverted from positive target behavior.

**Likely cause.** Negation handling is provider-specific and the named concept remains present in the condition. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L0 (wording repair).** Prefer a positive replacement state and provider-specific negative field only when documented; do not generalize deprecated-model guidance.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_field_projection_coverage` is the primary metric; companion checks: `metric_hard_lock_retention`, `metric_prompt_semantic_equivalence`, `metric_prompt_truncation_loss`.

**Compiler/score impact.** `provider_neutral_controls`, `provider_realization`, `constraints`, `warnings`, `provenance`.

**Prompt risks.** submits multiple duplicate serializations; assumes a prompt-string endpoint parses XML/YAML/JSON as a schema; places hard locks after low-priority decorative text.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### M.77 — Provider prompt rewriting changes canonical intent

**Failure ID:** `failure://m/prompt_rewrite_semantic_loss/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [M001], [M002], [M007], [M023], [M025], [R005], [R006], [R007]

**Trigger.** The endpoint silently enhances or rewrites a short prompt.

**Observable symptom.** New actions/details appear, priorities shift, or hard locks weaken.

**Likely cause.** An opaque secondary model transforms the submitted semantics before generation. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L1 (structured prompt repair).** Disable rewriting where possible, record the setting, hash the exact request, and reject providers that cannot preserve hard-lock meaning for critical shots.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_field_projection_coverage` is the primary metric; companion checks: `metric_hard_lock_retention`, `metric_prompt_semantic_equivalence`, `metric_prompt_truncation_loss`.

**Compiler/score impact.** `provider_neutral_controls`, `provider_realization`, `constraints`, `warnings`, `provenance`.

**Prompt risks.** submits multiple duplicate serializations; assumes a prompt-string endpoint parses XML/YAML/JSON as a schema; places hard locks after low-priority decorative text.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### M.78 — Prompt-budget overflow or truncation

**Failure ID:** `failure://m/prompt_budget_truncation/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [M001], [M002], [M007], [M023], [M025], [R005], [R006], [R008]

**Trigger.** Long nested prompts exceed provider or aggregator limits.

**Observable symptom.** Late constraints, end state, or forbidden variation disappear.

**Likely cause.** Transport or adapter truncation loses low-position fields and no canonical loss report is enforced. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L1 (structured prompt repair).** Compile by priority, never drop hard locks, emit an explicit loss report, and split the shot when minimum sufficient semantics do not fit.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_field_projection_coverage` is the primary metric; companion checks: `metric_hard_lock_retention`, `metric_prompt_semantic_equivalence`, `metric_prompt_truncation_loss`.

**Compiler/score impact.** `provider_neutral_controls`, `provider_realization`, `constraints`, `warnings`, `provenance`.

**Prompt risks.** submits multiple duplicate serializations; assumes a prompt-string endpoint parses XML/YAML/JSON as a schema; places hard locks after low-priority decorative text.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### N.79 — Overconstraint and priority dilution

**Failure ID:** `failure://n/overconstraint_priority_dilution/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B039], [B040], [B043]

**Trigger.** Too many exact actions, camera moves, effects, spatial locks, and negatives share one clip.

**Observable symptom.** Motion stiffens, instructions are randomly ignored, or the scene fails to complete.

**Likely cause.** Competing conditions exceed practical attention and temporal capacity. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Classify hard/soft/evaluation-only controls, remove duplicated semantics, and decompose the shot when calibrated complexity limits are exceeded.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_constraint_conflict_count` is the primary metric; companion checks: `metric_hallucinated_action_rate`, `metric_instruction_coverage`, `metric_primary_action_completion`.

**Compiler/score impact.** `constraints`, `warnings`, `unresolved`, `provider_realization`, `verification_requirements`.

**Prompt risks.** treats all instructions as equally hard; leaves unused time and allowed variation undefined; combines too many high-variance control dimensions.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### N.80 — Under-specified filler action

**Failure ID:** `failure://n/under_specified_filler/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B027], [B033], [B039], [B040], [B043]

**Trigger.** The prompt defines a start and one action but leaves duration/end state open.

**Observable symptom.** The model adds gestures, attacks, dialogue, effects, or scene changes.

**Likely cause.** Stochastic generation fills unassigned time with likely motion. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L1 (structured prompt repair).** Declare terminal state, hold behavior, allowed variation, and forbidden new primary actions; shorten duration.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_constraint_conflict_count` is the primary metric; companion checks: `metric_hallucinated_action_rate`, `metric_instruction_coverage`, `metric_primary_action_completion`.

**Compiler/score impact.** `constraints`, `warnings`, `unresolved`, `provider_realization`, `verification_requirements`.

**Prompt risks.** treats all instructions as equally hard; leaves unused time and allowed variation undefined; combines too many high-variance control dimensions.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### N.81 — Contradictory canonical constraints

**Failure ID:** `failure://n/contradictory_constraints/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B039], [B040], [B043], [R006], [R007]

**Trigger.** Two profiles or representations demand incompatible positions, motion, camera, or timing.

**Observable symptom.** The model averages, selects randomly, or produces broken geometry.

**Likely cause.** Conflict is passed to the provider instead of resolved by the compiler. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Fail closed at compile time, expose the conflict, and require one explicit resolution before provider submission.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_constraint_conflict_count` is the primary metric; companion checks: `metric_hallucinated_action_rate`, `metric_instruction_coverage`, `metric_primary_action_completion`.

**Compiler/score impact.** `constraints`, `warnings`, `unresolved`, `provider_realization`, `verification_requirements`.

**Prompt risks.** treats all instructions as equally hard; leaves unused time and allowed variation undefined; combines too many high-variance control dimensions.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### N.82 — Action-density overflow

**Failure ID:** `failure://n/action_density_overflow/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B027], [B039], [B040], [B043]

**Trigger.** Many dependent events are packed into a short clip.

**Observable symptom.** Actions merge, omit, reverse, or lose recovery.

**Likely cause.** Required event duration exceeds provider/task capacity. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Run a provider-specific staircase to estimate capacity; split before the first statistically reliable failure point instead of using a universal actions-per-second rule.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_constraint_conflict_count` is the primary metric; companion checks: `metric_hallucinated_action_rate`, `metric_instruction_coverage`, `metric_primary_action_completion`.

**Compiler/score impact.** `constraints`, `warnings`, `unresolved`, `provider_realization`, `verification_requirements`.

**Prompt risks.** treats all instructions as equally hard; leaves unused time and allowed variation undefined; combines too many high-variance control dimensions.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### N.83 — Multi-actor interaction overload

**Failure ID:** `failure://n/multi_actor_complexity_overflow/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B039], [B040], [B041], [B043]

**Trigger.** Several actors have simultaneous, crossing, or contact-heavy actions.

**Observable symptom.** Role swaps, count drift, fusion, and target confusion increase together.

**Likely cause.** Entity, role, spatial, and temporal bindings compete in the same interval. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L5 (shot decomposition).** Reduce simultaneous actors/actions, enforce lanes, and use separate shots or source/control video for dense choreography.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_constraint_conflict_count` is the primary metric; companion checks: `metric_hallucinated_action_rate`, `metric_instruction_coverage`, `metric_primary_action_completion`, `metric_role_assignment_accuracy`.

**Compiler/score impact.** `constraints`, `warnings`, `unresolved`, `provider_realization`, `verification_requirements`.

**Prompt risks.** treats all instructions as equally hard; leaves unused time and allowed variation undefined; combines too many high-variance control dimensions.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### N.84 — Camera, VFX, and choreography overload

**Failure ID:** `failure://n/camera_effect_choreography_overflow/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B002], [B003], [B031], [B035], [B037], [B038], [B039], [B040], [B043]

**Trigger.** Complex camera motion, actor interaction, material effects, and edits coincide.

**Observable symptom.** The system sacrifices motion, identity, geography, or effect causality.

**Likely cause.** Multiple high-variance generators are entangled without independent control channels. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L6 (postproduction/compositing).** Generate stable choreography first, then apply camera/VFX/edit layers through controlled V2V or postproduction.

**Fallback — L8 (provider/model substitution).** Use a provider/model with an officially documented control input matching the missing constraint and rerun qualification.

**Verification.** `metric_constraint_conflict_count` is the primary metric; companion checks: `metric_hallucinated_action_rate`, `metric_instruction_coverage`, `metric_primary_action_completion`.

**Compiler/score impact.** `constraints`, `warnings`, `unresolved`, `provider_realization`, `verification_requirements`.

**Prompt risks.** treats all instructions as equally hard; leaves unused time and allowed variation undefined; combines too many high-variance control dimensions.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
