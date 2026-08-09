---
id: cpcs.runtime.mx_compiler
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-008 §scripts/compile_authoring_yaml.py, SRC-008 §scripts/validate_cpcs_mx_package.py]
primary_route: cpcs/runtime/06_canonical/
secondary_routes:
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.constraint_compilation
  - cpcs.runtime.text_compilation
  - cpcs.runtime.interchange_manifests
---

# CPCS-MX Reference Compiler Implementation Contract

> Distilled from the frozen package's `compile_authoring_yaml.py` (437 lines) and
> `validate_cpcs_mx_package.py` (311 lines). This card captures the concrete
> compiler behavior that `constraint_resolution_compilation` describes abstractly.

## Pipeline

```text
authoring YAML
  → safe_load (yaml.safe_load)
  → authoring schema validation (JSON Schema Draft 2020-12)
  → profile URI resolution (profile:// → filesystem path)
  → deep_merge(base=profile_defaults, override=authoring_body)
  → import resolution (json/yaml/asset with SHA-256 verification)
  → compile_candidate(merged, profile_trace, import_trace)
  → canonical schema validation
  → write candidate JSON + compilation report
```

## Profile URI resolution

- URI scheme: `profile://<category>/<name>` → `<profiles_root>/<category>/<name>.yaml`
- Security: regex whitelist `[A-Za-z0-9_.\-/]+`, path traversal check against
  `profiles_root`.
- Each resolved profile contributes a `defaults` dict that is deep-merged before the
  authoring body. Profile trace records `uri`, `status`, `path`, `version`, `sha256`.

## Deep merge behavior

| Input types | Rule |
| --- | --- |
| dict + dict | recursive key-by-key merge |
| list + list (append path) | concatenate: `base + override` |
| list + list (ID-keyed items) | match by ID key, merge matched, append new |
| list + list (no IDs, not append path) | override replaces base |
| scalar + scalar | override replaces base |
| any type mismatch | override replaces base |

### Append-path suffixes

Lists at these JSON paths are concatenated rather than replaced:

- `hard_constraints`
- `soft_constraints`
- `verification.recommended_metrics`

### ID keys (checked in order)

`id`, `action_id`, `constraint_id`, `event_id`, `track_id`, `system_id`

Items sharing an ID key:value pair are merged in-place. New IDs are appended.

## Import resolution

| Import type | Content |
| --- | --- |
| `json` | parsed JSON object |
| `yaml` | parsed YAML mapping |
| `asset` | `{asset_path, type, sha256}` metadata wrapper |
| `jsonl` | same as asset (reference; not expanded by compiler) |
| `xml` | same as asset |

Every import is SHA-256 verified against an optional expected hash. Path traversal
is blocked: import paths must stay within the authoring file's parent directory.

## Candidate compilation

The compiler transforms the merged authoring dict into a canonical JSON candidate:

1. Normalize actors → `characters[]` with `character_id` + mannerism refs.
2. Compile `action_graph` beats → beats with actions, intervals, objectives.
3. Extract `phase_markers` → events with typed time anchors.
4. Promote `hard_constraints` / `soft_constraints` → typed constraint objects with
   `constraint_id`, `scope`, `priority`, `failure_policy`.
5. Extract `performance.laban` → `laban_controls[]` with effort maps.
6. Extract `performance.face` → `facial_events[]` with AU lists.
7. Extract `performance.breath` → `breath_tracks[]` grouped by subject.
8. Extract `style_transform` / `style_switch` → `style_transforms[]`.
9. Extract `secondary_motion` → typed secondary_motion entries.
10. Extract `verification.gates` → acceptance gates + recommended metrics.
11. Wrap unresolved items in `extensions[urn:cpcs-mx:resolved-authoring:1]`.

## Constraint object shape

```json
{
  "constraint_id": "constraint.hard.003",
  "scope": {"shot_ref": "shot_001"},
  "type": "textual_constraint",
  "value": "no body or prop penetration",
  "priority": "hard",
  "failure_policy": "reject_candidate",
  "evidence": {"class": "authored", "confidence": 1.0}
}
```

Hard constraints use `reject_candidate`; soft constraints use `report`.

## Exit codes

| Code | Meaning |
| --- | --- |
| 0 | success — valid candidate, zero unresolved |
| 2 | authoring schema validation error |
| 3 | canonical schema validation error |
| 4 | valid candidate but unresolved semantic items remain (`--allow-unresolved` suppresses) |

## Capability report

Every compiled candidate includes:

```json
{
  "dense_motion_synthesis": "not_implemented",
  "semantic_mapping": "partial",
  "unresolved_count": <int>
}
```

The compiler explicitly declares what it does not do. A production compiler still
needs motion retrieval, IK, dynamics, retargeting, or a learned motion generator.

## Deterministic serialization

Repeated builds must be byte-stable after canonical JSON serialization. The compiler
uses `json.dumps(candidate, indent=2, ensure_ascii=False)`.
