---
id: cpcs.runtime.observation_contract
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-008 §schemas/CPCS_MX_Observation_Record_Schema.json, SRC-008 §examples/observations/, SRC-008 §scripts/merge_cpcs_mx_observations.py, SRC-008 §scripts/validate_jsonl_stream.py]
primary_route: cpcs/verification/
secondary_routes:
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.verification.measurement_record_form
  - cpcs.runtime.mx_compiler
  - cpcs.found.uncertainty.evidence_two_axis_model
---

# CPCS-MX Observation Record Contract

> Distilled from the frozen package's observation schema (146 lines), observation
> merger script (119 lines), JSONL stream validator (98 lines), and worked
> observation examples. This is the JSONL evidence stream contract that feeds
> verification and compliance checking.

## Schema identity

- `$id`: `urn:cpcs-mx:observation-record:1.0`
- `$schema`: JSON Schema Draft 2020-12
- Format: one JSON object per non-blank line (JSONL)

## Required fields

| Field | Type | Notes |
| --- | --- | --- |
| `record_id` | string (min 1) | unique within stream |
| `source_id` | string (min 1) | video, clip, or measurement source |
| `layer` | string | semantic layer (pose, interaction, laban, etc.) |
| `claim` | object (requires `type`) | the observation content; `additionalProperties: true` |
| `evidence_class` | enum (7 values) | see below |
| `extractor` | object (requires `name`, `version`) | tool identity |

### Temporal anchoring (anyOf — at least one required)

| Field | Type |
| --- | --- |
| `frame_index` | integer ≥ 0 |
| `pts_s` | number |
| `time_range` | object `{start_s, end_s}` |

## Evidence class enum (7)

| Value | Meaning |
| --- | --- |
| `measured` | directly quantified from source data |
| `detected` | identified by a detector (pose, contact, cut) |
| `inferred` | derived through a model from observations |
| `interpreted` | a human or model interpretation of meaning |
| `authored` | declared by authoring or human review |
| `defaulted` | filled from a default profile |
| `derived` | computed from other fields within the score |

These are consistent with the 7 CPCS-MX evidence classes from SRC-005 E1
(`evidence_two_axis_model` EXTEND).

## Review status lifecycle

```text
unreviewed → reviewed → locked
                     ↘ rejected
```

- `unreviewed` — default state
- `reviewed` — human or automated review completed
- `locked` — reviewed and frozen; supersedes weaker records
- `rejected` — review determined the claim is invalid

## Supersession model

A record may carry a `supersedes` array listing `record_id` values it replaces.
The merger script tracks supersession chains and reports:

```json
{
  "conflict_count": 0,
  "conflicts": [],
  "superseded_by": {
    "obs.contact.actor_a.actor_b.000148": "human.lock.contact.000148"
  }
}
```

When a human-locked record supersedes an inferred one, the inferred record remains
in `normalized_all.jsonl` for audit but is replaced in `merged_active.jsonl`.

## Optional fields

| Field | Type | Notes |
| --- | --- | --- |
| `subject_ref` | string | actor or character reference |
| `confidence` | number [0, 1] | extractor confidence |
| `alternatives` | array of objects | competing hypotheses |
| `clock` | string | time domain (source_pts, output_pts, etc.) |
| `metadata` | object | free-form extension |

## Worked example

```jsonl
{"record_id":"obs.pose.actor_a.000144","source_id":"example_reference_001","frame_index":144,"pts_s":6.0,"clock":"source_pts","layer":"pose","subject_ref":"actor_a","claim":{"type":"joint_positions_2d","asset_ref":"pose/actor_a_000144.json"},"evidence_class":"detected","confidence":0.91,"extractor":{"name":"pose_fusion","version":"1.0.0"},"review_status":"reviewed"}
{"record_id":"obs.contact.actor_a.actor_b.000148","source_id":"example_reference_001","frame_index":148,"pts_s":6.1667,"clock":"source_pts","layer":"interaction","subject_ref":"actor_a","claim":{"type":"staged_near_contact","source_site":"right_hand","target_site":"actor_b.head_target_volume","minimum_screen_distance_norm":0.011,"occluded":true},"evidence_class":"inferred","confidence":0.79,"alternatives":[{"type":"camera_cheated_separation","confidence":0.44}],"extractor":{"name":"contact_fusion","version":"0.3.0"},"review_status":"unreviewed"}
{"record_id":"human.lock.contact.000148","source_id":"example_reference_001","frame_index":148,"pts_s":6.1667,"clock":"source_pts","layer":"interaction","subject_ref":"actor_a","claim":{"type":"staged_near_contact","value":true},"evidence_class":"authored","confidence":1.0,"extractor":{"name":"human_review","version":"1.0"},"review_status":"locked","supersedes":["obs.contact.actor_a.actor_b.000148"]}
```

## JSONL stream validation

`validate_jsonl_stream.py` validates line-by-line without loading the full file:

- Each line parsed as independent JSON
- Records validated against the observation schema
- Unique `record_id` enforcement (duplicates configurable as error/warning)
- SHA-256 hash verification of `content` field (for RAG records)
- Quarantine malformed records rather than silently dropping them

## VOG observation schema (SRC-009 EXTEND)

The Video Observation Graph (v1.2) extends this contract with additional
fields for the extraction pipeline:

### Additional required fields

| Field | Type | Notes |
| --- | --- | --- |
| `clock` | string | time domain (source_pts, output_pts, etc.) — now required in VOG |
| `evidence` | array | source locators (asset URI + bbox/object locator) |

### Extractor extended contract

The `extractor` object gains `parameters_digest` (sha256 of extractor
configuration) for reproducibility. Provider profiles must include:
`provider`, `model`, `api_version`, `verified_on`, input sampling
assumptions, schema support, and known limits.

### Evidence class alignment

VOG uses 5 evidence classes (measured, detected, inferred, interpreted,
authored) — a subset of this schema's 7. The `defaulted` and `derived`
classes are handled at the resolved-claim layer, not the observation layer.

### Contradiction records

The VOG adds `contradictions` as first-class objects with 7 types
(temporal, action_label, identity, contact, camera, causal, numeric),
3 statuses (unresolved, resolved_by_precedence, resolved_by_review),
and linked observation references.

See `cpcs.evaluation.video_observation_graph` for the full VOG schema.
