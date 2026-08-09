# Audio-Video Synchronization Failures

**Research date:** 2026-08-05  
**Repository revision inspected:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.

## Decision finding

Semantic audio relevance and temporal synchronization are separate requirements. A plausible impact sound can still occur before contact; a correct voice can still belong to the wrong speaker; music can be semantically appropriate but phase-misaligned.

## Covered families

| ID | Family | Records | Existing owner | Core metrics |
| --- | --- | --- | --- | --- |
| O | Audio and cross-modal synchronization | 6 | audio + actions + verification | metric_audio_visual_temporal_offset, metric_audio_visual_semantic_match, metric_lip_speech_consistency, metric_voice_identity_consistency |

## Canonical contract implications

Bind every foreground audio event to a visual event ID or explicitly classify it as ambient/off-screen. Record speaker/voice identity, onset window, semantic cause, permitted offset, and recovery/tail. Separate generated-audio failure from visual failure and replace deterministic foreground audio in post when frame-level timing is critical.

The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.

## Failure records

### O.85 — Impact sound temporal offset

**Failure ID:** `failure://o/impact_sound_offset/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B022], [B023], [B024], [B046], [M004], [M019]

**Trigger.** A fast contact or near-contact should trigger a sound.

**Observable symptom.** Sound precedes or lags the visual event beyond tolerance.

**Likely cause.** Joint generation or later audio synthesis lacks a shared event anchor. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Use canonical audio event anchors tied to visual event IDs and verify onset offset; replace sound in post when timing is critical.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_audio_visual_semantic_match` is the primary metric; companion checks: `metric_audio_visual_temporal_offset`, `metric_lip_speech_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `audio`, `actions`, `beats`, `continuity.voice_state`, `verification_requirements`.

**Prompt risks.** does not bind sound events to visual event IDs; asks a joint model to preserve multiple voices without speaker references; uses BPM numerals without a shared timecode.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### O.86 — Lip-speech mismatch

**Failure ID:** `failure://o/lip_speech_mismatch/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B022], [B023], [B024], [B046], [M004], [M019]

**Trigger.** Dialogue contains phonetic complexity, profile view, fast cuts, or multiple speakers.

**Observable symptom.** Mouth motion does not match speech timing/content.

**Likely cause.** Audio and facial motion are weakly aligned or speaker assignment changes. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use a driving performance/dedicated lip-sync system or generate clean visuals and dub; measure temporal and phonetic agreement separately.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_audio_visual_semantic_match` is the primary metric; companion checks: `metric_audio_visual_temporal_offset`, `metric_lip_speech_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `audio`, `actions`, `beats`, `continuity.voice_state`, `verification_requirements`.

**Prompt risks.** does not bind sound events to visual event IDs; asks a joint model to preserve multiple voices without speaker references; uses BPM numerals without a shared timecode.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### O.87 — Sound without visual cause

**Failure ID:** `failure://o/sound_without_visual_cause/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B022], [B023], [B024], [B046], [M004], [M019]

**Trigger.** Joint generation is asked for ambience/effects while actions are ambiguous.

**Observable symptom.** An impact, splash, step, or mechanical sound occurs without the event.

**Likely cause.** Audio semantics are generated independently from visual causal satisfaction. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Bind every foreground sound to a visual event or explicitly classify it as off-screen/ambient.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_audio_visual_semantic_match` is the primary metric; companion checks: `metric_audio_visual_temporal_offset`, `metric_lip_speech_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `audio`, `actions`, `beats`, `continuity.voice_state`, `verification_requirements`.

**Prompt risks.** does not bind sound events to visual event IDs; asks a joint model to preserve multiple voices without speaker references; uses BPM numerals without a shared timecode.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### O.88 — Visual event lacks required sound

**Failure ID:** `failure://o/visual_event_without_sound/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B022], [B023], [B024], [B046], [M004], [M019]

**Trigger.** A salient impact, splash, door, or speech event occurs.

**Observable symptom.** Expected audio is absent or masked.

**Likely cause.** The model satisfies visual semantics but omits a lower-salience audio consequence. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L6 (postproduction/compositing).** Retain event metadata and synthesize/mix deterministic sound in post; verify presence and onset.

**Fallback — L8 (provider/model substitution).** Use a provider/model with an officially documented control input matching the missing constraint and rerun qualification.

**Verification.** `metric_audio_visual_semantic_match` is the primary metric; companion checks: `metric_audio_visual_temporal_offset`, `metric_lip_speech_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `audio`, `actions`, `beats`, `continuity.voice_state`, `verification_requirements`.

**Prompt risks.** does not bind sound events to visual event IDs; asks a joint model to preserve multiple voices without speaker references; uses BPM numerals without a shared timecode.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### O.89 — Speaker or voice drift

**Failure ID:** `failure://o/speaker_voice_drift/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B022], [B023], [B024], [B046], [M004], [M019]

**Trigger.** Multi-shot or multi-speaker dialogue changes camera view or scene.

**Observable symptom.** Voice identity, language, accent, or turn assignment changes.

**Likely cause.** Voice embeddings/identity are not persistently bound across shots. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L3 (reference image or storyboard).** Use speaker-specific voice references and turn IDs; separate dialogue production from video generation when exact casting matters.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_audio_visual_semantic_match` is the primary metric; companion checks: `metric_audio_visual_temporal_offset`, `metric_lip_speech_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `audio`, `actions`, `beats`, `continuity.voice_state`, `verification_requirements`.

**Prompt risks.** does not bind sound events to visual event IDs; asks a joint model to preserve multiple voices without speaker references; uses BPM numerals without a shared timecode.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### O.90 — Music or beat accent misalignment

**Failure ID:** `failure://o/music_action_accent_misalignment/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B022], [B023], [B024], [B046], [M004], [M019]

**Trigger.** Choreography, cuts, or impacts must land on musical beats.

**Observable symptom.** Visual apex/cut occurs off beat.

**Likely cause.** Textual BPM/beat instructions do not create an executable shared timeline. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Use a timecoded beat map/control track and edit generated clips to the beat; verify event-to-beat offset.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_audio_visual_semantic_match` is the primary metric; companion checks: `metric_audio_visual_temporal_offset`, `metric_lip_speech_consistency`, `metric_voice_identity_consistency`.

**Compiler/score impact.** `audio`, `actions`, `beats`, `continuity.voice_state`, `verification_requirements`.

**Prompt risks.** does not bind sound events to visual event IDs; asks a joint model to preserve multiple voices without speaker references; uses BPM numerals without a shared timecode.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Provider qualification requirement

Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.

## Evidence boundary

The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence.
