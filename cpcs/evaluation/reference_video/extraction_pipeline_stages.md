---
id: cpcs.evaluation.extraction_pipeline_stages
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 Extraction Guide §7-29, Appendix H]
primary_route: cpcs/evaluation/reference_video/
interfaces:
  - cpcs.evaluation.video_observation_graph
  - cpcs.evaluation.reference_video_distillation
  - cpcs.runtime.information_transfer_protocol
  - cpcs.runtime.observation_contract
---

# Extraction Pipeline Stages

> Distilled from the Video-to-CPCS Extraction Guide (v1.2). Defines the 12
> operational extraction stages (Stage 0–11), confidence fusion rules, provider
> orchestration pattern, and round-trip verification protocol.

## 12 extraction stages

| Stage | Name | Key tools | Primary outputs |
| --- | --- | --- | --- |
| 0 | Rights, consent, source registration | Manual + manifest | Rights record, source hash, consent scope |
| 1 | Media normalization, forensic manifest | FFprobe, FFmpeg | Probe JSON, analysis proxy, audio stem, semantic frames |
| 2 | Shot, transition, scene, beat segmentation | TransNetV2, PySceneDetect | Shot candidates, scene boundaries, beat proposals |
| 3 | Multimodal semantic analysis | Gemini, Pegasus, Marengo | Narrative hierarchy, action labels, ambiguity proposals |
| 4 | Actor, face, gaze, performance extraction | OpenFace, face mesh | AU curves, gaze tracks, head pose, identity tracks |
| 5 | Body pose, 3D reconstruction, camera disentanglement | AlphaPose, SMPL-X, COLMAP, RAFT | Skeleton, root trajectory, camera 6DoF, optical flow |
| 6 | Action atoms, motion phases, contacts, combat | Custom fusion | Action graph, phase tracks, contact events, kinetic chain |
| 7 | Laban movement qualities | Derived from stage 5-6 | Candidate Laban readings (Weight, Time, Space, Flow, Shape) |
| 8 | Camera, lens, framing, editorial grammar | Camera solver, OTIO | Shot scale, angle, movement type, edit events, OTIO timeline |
| 9 | Audio, dialogue, rhythm, impact | Whisper, audio analysis | Transcript, speech rate, pauses, music beat, impact transients |
| 10 | VFX and stylization extraction | VFX detector, compositor | Speed lines, trails, dust, shake, smear, flash, retime curves |
| 11 | UGC and marketing extraction | Multimodal model | Communication graph, 15 measurable tracks, variant plan |

## Stage 0 — Rights and consent

Before any processing: register source hash, verify consent scope (identity use,
voice, body, training, inference, distribution, duration, revocation), flag
prohibited content, and record rights policy in the extraction manifest.

## Stage 1 — Media normalization

FFprobe for authoritative metadata. FFmpeg for: constant-frame-rate analysis
proxy, mono speech-analysis stem (16 kHz), low-rate semantic frames (1 FPS).
All derivatives hashed and recorded in the source manifest.

## Stage 2 — Segmentation

Shot boundary detection (frame-accurate), scene clustering, beat proposal from
semantic analysis. Output: shot candidates with confidence, transition types,
scene groups.

## Stage 3 — Semantic analysis

Multimodal models provide: narrative arc, shot purpose, action naming, social
context, UGC function (hook, proof, CTA), ambiguity proposals. Semantic
hypotheses are NOT ground truth — they carry `inferred` or `interpreted`
evidence class.

## Stage 4 — Face and performance

Frame-level AU estimation, head pose, gaze direction, blink events, jaw/speech.
Face quality gating: blur, profile, and occlusion reduce confidence. AU values
carry evidence class `detected` unless human-reviewed.

## Stage 5 — Body and camera

Skeleton (2D/3D keypoints), root trajectory, body-part identity tracking.
Camera 6DoF estimation with actor/camera separation via optical flow and SfM.
Output: normalized pose tracks, camera path, optical flow magnitude.

## Stage 6 — Action and contact

Action atomization with 12 labels: setup, approach, weight shift, step-in,
plant, pivot/load, attack-like motion, defense/dodge/redirect, near-contact/
contact/occluded impact, reaction, follow-through, recovery. Kinetic chain
ordering: support foot → pelvis → torso → shoulder → elbow → hand/prop.
Contact events with staged-near-contact classification.

## Stage 7 — Laban proxies

Candidate readings only. Weight (acceleration, CoM displacement, loading
duration). Time (preparation-to-apex, acceleration concentration). Space
(directness ratio D = chord/path-length). Flow (jerk distribution, holds,
reversibility). Shape (spreading/enclosing, rising/sinking from skeletal
geometry). Each proxy stored separately from the interpreted label.

## Stage 8 — Camera and editorial

Shot scale from subject occupancy (not just labels). Camera movement: base
path ⊕ operator perturbation ⊕ post-production. Editing: cut type, J/L cuts,
reaction cuts, cut-on-action, speed ramps, OTIO export.

## Stage 9 — Audio

ASR transcript with timestamps. Speech rate, pauses, breath points, sentence
stress. Music tempo, impact transients, whooshes, risers, room tone. Audio
lead/lag relative to cuts.

## Stage 10 — VFX

8 event types: speed lines, energy trails, dust bursts, camera shake, smear
frames, impact flashes, freeze/hold, speed ramps. Physical event and effect
are separately addressable.

## Stage 11 — UGC/marketing

Communication graph with 12 node types (hook → CTA). 15 measurable tracks
(time-to-first-face, gaze-to-lens duty cycle, product visibility ratio,
caption update rate, etc.). Director controls separated from marketing
hypotheses.

## Confidence fusion rules

1. **Do not average unlike evidence.** A language model's 0.82 confidence is
   not calibrated against a pose detector's keypoint probability.
2. **Preserve confidence type and calibration scope.**
3. **Precedence for geometric/temporal facts:**
   source timestamps > calibrated geometry > uncalibrated detector >
   multimodal semantic inference > free-form description.
4. **Precedence for narrative/marketing interpretations:**
   human-approved > multiple independent analyses > single analysis >
   geometry-only guess.
5. **Contradictions are first-class outputs**, not silently resolved.

## Provider orchestration

| Provider | Role |
| --- | --- |
| Gemini / Pegasus | Semantic hierarchy, narrative, action naming, ambiguity |
| Marengo | Retrieval, clustering, similarity search, comparable-shot discovery |
| FFprobe / FFmpeg | Authoritative metadata, PTS, proxies, audio stems |
| Shot detectors | Frame-accurate cut and transition proposals |
| Face / gaze tools | Landmarks, head pose, AUs, gaze candidates |
| Pose / mesh / tracking | Skeleton, root, body parts, identities |
| Optical flow / SfM / SLAM | Dense motion, background camera, camera/actor separation |
| ASR and audio analysis | Words, rhythm, pauses, impact and music events |
| Fusion compiler | Evidence graph, CPCS projection, capability-aware package |

No provider should be the sole source of truth for all layers.

## Round-trip verification (10 metrics)

1. Shot-boundary and event-time error
2. Action-node and causal-edge agreement
3. Normalized root/joint trajectory agreement
4. Contact/near-contact timing
5. Gaze-to-target intervals
6. AU event timing (where face quality permits)
7. Shot scale, screen direction, camera-motion agreement
8. Speech, caption, impact, music-beat alignment
9. Product visibility, proof order, CTA hold (marketing)
10. Unresolved contradictions and reviewer decisions

No single score should hide failures in a critical layer.

## 19-item deterministic verification checklist

Covers: schema validation, source hash verification, time-range legality,
identifier resolution, evidence class typing, confidence calibration scope,
contradiction reporting, provider profile versioning, rights policy
compliance, clock consistency, coordinate normalization, track coverage,
action graph connectivity, Laban proxy separation, camera/actor separation,
audio-visual sync, marketing graph completeness, VFX event independence,
and round-trip metric thresholds.
