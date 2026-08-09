---
id: cpcs.runtime.information_transfer_protocol
kind: method
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 Pegasus paper Part IV §30-40]
primary_route: cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.runtime.capability_negotiation_protocol
  - cpcs.evaluation.video_observation_graph
---

# Information Transfer Protocol

> Distilled from Pegasus paper Part IV. Defines how CPCS controls transfer from
> a source (reference video, fight score, extraction) to a new production through
> 5 transformation stages, with XML semantic envelope and compiler resolution.

## 5 transformation stages

| Stage | What happens | Preserved |
| --- | --- | --- |
| 1. Structural abstraction | Extract timing, causality, motion quality, camera grammar from source | Beat order, action causality, Laban profile, screen direction |
| 2. Identity normalization | Remove performer identity, voice, wardrobe, protected elements | Anonymized tracks, normalized coordinates, abstract action graph |
| 3. Parameterization | Scale timing, intensity, displacement for new context | Relative durations, effort ratios, camera motion shapes |
| 4. Target compilation | Map to specific backend capabilities via adapter | Prompt text, control media, camera path, evaluation constraints |
| 5. Verification | Re-extract generated output and compare with intended score | Compliance metrics, contradiction report, human review |

## XML semantic envelope

The XML envelope wraps a canonical JSON score in a directorial/narrative context:

```xml
<cpcs:sequence xmlns:cpcs="urn:cpcs:core:1.1"
               xmlns:face="urn:cpcs:facs:1.1"
               xmlns:cam="urn:cpcs:camera:1.1"
               id="campaignA.sequence03">
  <cpcs:scene id="roof_encounter">
    <cpcs:shot id="shot014" scoreRef="asset://scores/shot014.cpcs.json">
      <cpcs:direction>
        The audience sees Mara's fear only after she recognizes the blood.
      </cpcs:direction>
      <face:event actor="mara" au="AU04" apex="2.74s" peak="0.28"/>
      <cam:move type="dolly-in" start="2.20s" end="3.20s"/>
    </cpcs:shot>
  </cpcs:scene>
</cpcs:sequence>
```

XML serves as the ordered director envelope. JSON serves as the canonical resolved
score. Both reference the same ontology. XML namespaces qualify names so that
multiple vocabularies (face, camera, VFX, marketing) coexist without collisions.

## Compiler resolution order

```text
studio defaults
  → production profile
    → sequence profile
      → scene profile
        → shot profile
          → beat overrides
            → event/frame overrides
              → locks (final authority)
```

At each level, typed merge rules apply per the merge-policy registry. The schema
declares which policy governs each path.

## Provider adapter contract

```json
{
  "provider": "generic",
  "model": "prompt-video-v1",
  "api_version": "2026-07",
  "verified_on": "2026-07-18",
  "accepts": {
    "prompt_text": {"support": "native"},
    "duration_s": {"support": "native"},
    "first_frame": {"support": "native"},
    "pose_video": {"support": "approximate"},
    "au_curve": {"support": "none"},
    "camera_6dof": {"support": "none"}
  }
}
```

## RAG storage (10 record types)

| Record type | Purpose |
| --- | --- |
| `document` | Source document metadata |
| `paper_chunk` | Heading-aware chunk of paper content |
| `concept_card` | Distilled concept with route and interfaces |
| `movement_atom` | Reusable motion primitive |
| `performance_template` | Parameterized performance pattern |
| `shot_template` | Camera/edit pattern |
| `calibration_profile` | Per-performer or per-model calibration |
| `source_record` | Bibliographic provenance |
| `failure_record` | Known failure mode and mitigation |
| `experiment_record` | Reproducible experiment result |

## 4-phase implementation blueprint

| Phase | Focus |
| --- | --- |
| 1 — Semantic | Shot detection, transcript, semantic analysis, canonical JSON |
| 2 — Frame-level | Pose, face, gaze, camera estimation, optical flow |
| 3 — Modular recreation | Action graph, contact inference, Laban, control media export |
| 4 — Corpus/learning | Multi-video corpus, learned priors, automatic quality gates |

## 13 failure modes (Pegasus)

| Failure | Cause | Mitigation |
| --- | --- | --- |
| Missed fast action | Low sampling rate | Clip and resample; frame-level pose/flow |
| False shot boundary | Flash, shake, VFX | Multi-detector fusion |
| Wrong actor identity | Occlusion or cut | Track confidence; cross-shot review |
| Pose jitter | Detector instability | Confidence-aware smoothing; 3D prior |
| Foot skating from camera | Camera/actor conflation | Background motion model |
| False contact | Monocular depth ambiguity | Near-contact class; multi-cue fusion |
| Laban overclaim | Metric treated as definition | Label as candidate interpretation |
| AU overclaim | Blur/profile/calibration | Face-quality gating |
| Semantic hallucination | One-pass MLLM output | Structured schema, evidence timestamps |
| UGC style clone | Identity and surface copied | Extract timing/grammar; replace protected elements |
| Model ignores score | Unsupported controls | Capability negotiation; evaluator |
| RAG retrieves speculation | Evidence classes flattened | Metadata filters; reviewed status |
| Contact timing drift | Audio-visual offset | Cross-modal synchronization check |
