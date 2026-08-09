---
id: cpcs.evaluation.video_observation_graph
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §30, Appendix H, schemas/CPCS_Video_Observation_Graph_Schema.json]
primary_route: cpcs/evaluation/reference_video/
interfaces:
  - cpcs.knowledge.evidence_two_axis_model
  - cpcs.verification.observation_record_contract
---

# Video Observation Graph (VOG)

> Distilled from CPCS paper §30, Appendix H, and the VOG JSON Schema (236 lines).
> The VOG is the canonical evidence container for reverse-compiling a reference video
> into CPCS controls. It separates raw observations from resolved claims, retains
> contradictions, and carries provenance for every assertion.

## Design principles

1. **Evidence-aware** — every claim cites its supporting observations
2. **Contradiction-tolerant** — disagreements are first-class outputs, not silently resolved
3. **Identity-independent** — observations are normalized away from performer identity
4. **Clock-authoritative** — all timestamps reference source PTS or source seconds
5. **Provider-agnostic** — any extractor can contribute observations; the graph merges them
6. **Re-auditable** — observations and source locators remain the audit record

## 5 evidence classes

| Class | Definition | Examples |
| --- | --- | --- |
| `measured` | Derived from media timing or numeric signal with reproducible operation | PTS, duration, frame size, audio peak, optical-flow magnitude |
| `detected` | Output of a trained detector or classifier | Shot boundary, face box, AU intensity estimate, body keypoint |
| `inferred` | Computed from multiple measurements under assumptions | Camera pan, likely foot contact, near-contact, local phase |
| `interpreted` | Semantic or directorial reading not uniquely observable | Intimidation, concealed fear, reaction shot purpose, hook function |
| `authored` | Deliberate production decision added during retargeting | Replace product; make motion heavier; move reveal 0.3s earlier |

## VOG canonical schema (required fields)

```json
{
  "schema": "cpcs-video-observation-graph/1.0",
  "graph_id": "<string>",
  "source": { "id", "sha256", "duration_s", "media_type", "width?", "height?", "nominal_fps?" },
  "clock": { "canonical": "source_pts|source_seconds", "timebase": {"numerator", "denominator"} },
  "rights": { "basis?", "permitted_uses", "restricted_elements" },
  "segments": { "shots": [], "scenes": [], "beats": [] },
  "entities": { "actors": [], "objects": [], "locations": [] },
  "observations": [],
  "resolved_claims": [],
  "contradictions": [],
  "cpcs_projection": {},
  "provider_profiles": [],
  "assets": [],
  "validation": { "schema_valid", "semantic_valid", "issues" }
}
```

## Segment model

Each segment (shot, scene, beat) has: `id`, `kind` (shot|scene|beat|transition|clip),
`start_s`, `end_s`, `label?`, `confidence?`, `transition_type?`, `parent_id?`,
`evidence_refs[]`, `metadata{}`.

## Entity model

Each entity (actor, object, location) has: `id`, `kind` (actor|object|location|camera|audience|unknown),
`anonymous_role?`, `identity_resolution` (anonymous|ephemeral_track|authorized_identity|unknown),
`attributes{}`, `track_refs[]`.

## Resolved claim model

Each resolved claim: `id`, `layer`, `claim: {type, value}`, `time_range`,
`entity_refs[]`, `observation_refs[]` (min 1), `resolution` (direct_measurement|
detector_agreement|rule|model_fusion|human_review|authored_override|unresolved),
`resolved_confidence` (0-1), `status` (accepted|tentative|rejected|needs_review).

## Contradiction model

7 contradiction types: `value_conflict`, `time_conflict`, `entity_conflict`,
`causal_conflict`, `source_hash_conflict`, `duplicate_id`, `other`.
3 statuses: `open`, `resolved`, `waived`.

## Provider profile

Each provider: `provider`, `model`, `api_version?`, `verified_on` (date),
`roles[]`, `sampling_assumptions{}`, `known_limits[]`, `documentation_source_id?`.
Dated profiles are part of reproducibility because hosted APIs can change.

## Confidence fusion rules

1. **Do not average unlike evidence** — a language model's 0.82 confidence is not
   calibrated against a pose detector's keypoint probability
2. **Evidence bundle** — each resolved field cites supporting observations
3. **Precedence for geometric/temporal facts:**
   source timestamps > calibrated geometry/track > uncalibrated detector >
   multimodal semantic inference > free-form description
4. **Precedence for narrative/marketing interpretations:**
   human-approved interpretation > multiple independent multimodal analyses >
   single semantic analysis > geometry-only guess
5. **Contradiction is a first-class output** — do not silently resolve

## Minimum observation contract

Every observation must include: `record_id`, `source_id`, `time_range` or
`frame_index`, `layer`, `claim`, `evidence_class`, `confidence`, `extractor`
(name, version), and optionally `uncertainty`, `alternatives`, `review_status`.

## Round-trip verification

After generation, re-extract the output and compare graphs. Report:
- Shot-boundary and event-time error
- Action-node and causal-edge agreement
- Normalized joint trajectory agreement (DTW when elastic timing allowed)
- Contact/near-contact timing
- Gaze-to-target intervals
- AU event timing (where face quality permits)
- Shot scale, screen direction, camera-motion agreement
- Speech, caption, impact, music-beat alignment
- Product visibility, proof order, CTA hold (marketing)
- Unresolved contradictions and reviewer decisions

No single score should hide failures in a critical layer.
