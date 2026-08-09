---
id: cpcs.evaluation.reference_video_distillation
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §30, extraction guide §1-30]
primary_route: cpcs/evaluation/reference_video/
interfaces:
  - cpcs.evaluation.video_observation_graph
  - cpcs.knowledge.evidence_two_axis_model
  - cpcs.runtime.structured_prompting_architecture
---

# Reference-Video Distillation and Reverse Directorial Compilation

> Distilled from CPCS paper §30 and the extraction guide (1,378 lines).
> RVD decomposes a source video into synchronized evidence streams.
> RDC interprets those streams as a hierarchy of controls. The output is an
> identity-independent, retargetable CPCS score.

## Core concept

A known video is treated as an observable execution trace of decisions about
performance, blocking, action, timing, camera, editing, sound, VFX, and audience
communication. The challenge is to recover a reusable, identity-independent
control score that can be recompiled for a different cast, location, product,
visual style, duration, or video-generation backend.

## Forward vs reverse compilation

```text
Forward:  screenplay → CPCS score → model controls → video
Reverse:  reference video → measurements + detections + semantic hypotheses
          → resolved VOG → identity-independent CPCS score → new production
```

The inverse is underdetermined. A visible dolly-in might be physical camera,
digital crop, zoom, stabilized handheld, or generated transform. A recoil might
result from staged contact, near-contact plus acting, edit, sound, camera shake,
or combination. Therefore, the reverse compiler reports possible explanations
and confidence rather than claiming access to original intentions.

## 7 properties of a useful "core"

1. **Temporal** — describes changes, not only static labels
2. **Relational** — preserves actor-to-actor, actor-to-object, actor-to-camera, sound-to-picture relationships
3. **Identity-independent** — retargetable to another performer or character
4. **Coordinate-normalized** — not trapped in source resolution or one body size
5. **Causally ordered** — preserves anticipation, initiation, contact, reaction, follow-through, recovery
6. **Presentation-aware** — separates staged world from camera/edit visibility
7. **Evidence-aware** — distinguishes observation from interpretation

## 11-level extraction hierarchy

| Level | Portable information |
| --- | --- |
| Production | global format and communication goal |
| Sequence | dramatic and persuasive arc |
| Scene | setting, participants, continuity state |
| Shot | camera and edit unit |
| Beat | meaningful state change |
| Action event | executable physical unit |
| Performance track | face, gaze, affect, posture, Laban quality |
| Physical track | pose, root, phase, contact, momentum |
| Presentation track | lens, camera, framing, speed, VFX |
| Audio track | speech, breath, music, impact, silence |
| Marketing track | attention and conversion hypothesis |

## Temporal pyramid (7 passes)

| Pass | Sampling | Purpose |
| --- | --- | --- |
| Asset | container/stream level | codecs, timebase, duration, rotation, frame rate, audio layout |
| Sequence | 0.2-1 FPS or full long-context | story, topic, persuasive arc, scene structure |
| Shot | every frame or shot detector | cuts, dissolves, fades, shot duration, transition type |
| Beat | 2-8 FPS plus audio | meaningful state changes, dialogue turns, reveals, reactions |
| Performance | 24-60 FPS | face, gaze, pose, gesture, gait, camera motion |
| Impact/micro | source FPS, optical flow | contact, fast action, microexpression, smear, flash, transient |
| Audio | 16-48 kHz | words, pauses, breaths, impacts, music, ambience |

## 15-stage extraction architecture

| Stage | Tool examples | Output |
| --- | --- | --- |
| 0. Rights and consent | Policy check | Rights declaration, identity policy |
| 1. Media normalization | ffprobe, FFmpeg | Probe manifest, proxy, audio stem |
| 2. Shot/scene/beat | TransNetV2, PySceneDetect, Gemini | Shot boundaries, scene groups, beat candidates |
| 3. Multimodal semantic | Gemini, Pegasus, Marengo | Narrative structure, shot purpose, action naming |
| 4. Actor/face/gaze | OpenFace, face detectors | Face tracks, AU candidates, gaze targets |
| 5. Pose/3D/camera | AlphaPose, 4DHumans, COLMAP, RAFT | Body tracks, camera estimate, optical flow |
| 6. Coordinate normalization | Geometry | Normalized joints, root trajectory |
| 7. Action atoms/contacts | Rule-based, ASFormer, ActionFormer | Action graph, contact candidates, causal edges |
| 8. Laban proxies | Operationalized interpretation | Effort candidates with supporting features and confounds |
| 9. Camera/editing | Flow decomposition, OTIO | Camera track, edit events, cut-on-action |
| 10. Audio/dialogue | Whisper, Essentia | Transcript, word timing, impacts, music beats |
| 11. VFX/stylization | Detection | Effect events, timing, attachment |
| 12. UGC/marketing | Multimodal analysis | Communication graph, measurable tracks |
| 13. Confidence fusion | Evidence merging | Resolved claims, contradictions |
| 14. VOG assembly | Schema validation | Canonical VOG JSON |
| 15. Reverse CPCS compilation | Projection | Identity-independent CPCS score |

## Non-copying normalization

Before using an extracted graph as a generative control source:

- **Retain:** authorized causal order, duration pattern, motion quality, camera grammar, proof sequence
- **Parameterize:** timing tolerances, shot scale, action intensity, gaze duty cycle, product visibility
- **Replace:** identity, voice, dialogue wording, logos, wardrobe, environment, protected characters
- **Exclude:** private information, disallowed biometric identifiers, unsafe stunt instructions, unlicensed assets

## Similarity budget (default from pipeline config)

| Dimension | Target |
| --- | --- |
| temporal_structure | 0.80 |
| action_causality | 0.85 |
| movement_quality | 0.70 |
| camera_grammar | 0.65 |
| surface_appearance | 0.15 |
| identity | 0.00 |
| voice_identity | 0.00 |

## 4-tier minimum viable implementation

| Tier | Components |
| --- | --- |
| 1 — Semantic reverse storyboard | ffprobe manifest, shot detection, transcript, Gemini/Pegasus descriptions, canonical JSON, human review |
| 2 — Performance-aware | + actor tracking, face/head/gaze, 2D pose, action events, camera/edit, UGC/marketing |
| 3 — Motion reconstruction | + monocular 3D, camera/scene reconstruction, local phases, contact inference, Laban, pose/depth/mask export |
| 4 — Closed-loop | + target adapter, clip generation, editorial assembly, re-extraction, compliance report, patch revision |

## Provider orchestration pattern

```text
Gemini / Pegasus → semantic hierarchy, custom events, narrative, UGC function
Marengo          → retrieval, clustering, similarity search
FFprobe / FFmpeg → authoritative media metadata, PTS, proxies, audio stems
Shot detectors   → frame-accurate cut and transition proposals
Face / gaze      → landmarks, head pose, AUs, gaze candidates
Pose / mesh      → skeleton, root, body parts, identities, normalized motion
Flow / SfM       → dense motion, background camera model, camera/actor separation
ASR / audio      → words, turns, rhythm, pauses, impact and music events
Fusion compiler  → evidence graph, CPCS projection, capability-aware target package
```

No provider should be the sole source of truth for all layers.
