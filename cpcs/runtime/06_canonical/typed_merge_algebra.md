---
id: cpcs.runtime.typed_merge_algebra
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §19.10-19.12, Appendix G]
primary_route: cpcs/runtime/06_canonical/
interfaces:
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.constraint_compilation
---

# Typed Merge Algebra

> Distilled from CPCS paper §19.10-19.12 and Appendix G. Defines how CPCS resolves
> multiple sources of truth (studio defaults, project styles, scene overrides, shot
> specifics, measured tracks) into one canonical value per field.

## Candidate resolution tuple

Every field value is a tuple: c = (p, v, a, s, q, ℓ, h, o, r)

| Field | Meaning |
| --- | --- |
| p | Field path (e.g., `/tracks/face/0/AU04/apex_intensity`) |
| v | Value |
| a | Authority class (safety, asset_identity, continuity, director_hard, department, adapter) |
| s | Specificity (studio < project < sequence < scene < shot < beat < event) |
| q | Priority within same specificity |
| ℓ | Lock status (locked = cannot be overridden without explicit unlock) |
| h | Hard/soft (hard constraint vs soft preference) |
| o | Order (for temporal sequences) |
| r | Provenance (source URI, locator, digest) |

## 10 data kinds with merge policies

| Data kind | Merge policy | Examples |
| --- | --- | --- |
| Scalar | Replace | duration_s, lens_mm |
| Numeric style | Replace per field (not averaged) | AU intensity, Laban Weight |
| Object | Typed deep merge (child policy from schema) | performance{}, camera{} |
| Set | Union (canonical value identity) | tags, keyword sets |
| Ordered list | Append (source then override) | beats[], action_events[] |
| Keyed entity | Merge by ID key (error on duplicate without policy) | actors[], constraints[] |
| Temporal track | Replace track (requires timebase + boundary policy) | face_tracks[], pose_tracks[] |
| Hard constraints | Conjoin or conflict → error if incompatible | contact_policy, safety rules |
| Asset reference | Replace (with digest verification) | rig URIs, texture paths |
| Optional removal | Explicit null or delete marker (distinguished from missing) | removing a style override |

## Merge-policy registry

```json
{
  "merge_policies": {
    "replace":            { "allowed_types": ["string","number","boolean","null","object","array"] },
    "deep_merge_typed":   { "allowed_types": ["object"], "child_policy_source": "schema" },
    "merge_by_id":        { "allowed_types": ["array"], "identity_field": "id", "duplicate_without_policy": "error" },
    "append_ordered":     { "allowed_types": ["array"], "ordering": "source_then_override" },
    "set_union":          { "allowed_types": ["array"], "identity": "canonical_value" },
    "replace_track":      { "allowed_types": ["array","object"], "requires": ["timebase","boundary_policy"] },
    "splice_interval":    { "allowed_types": ["array","object"], "requires": ["interval","boundary_policy","overlap_policy"] },
    "blend_interval":     { "allowed_types": ["array","object"], "requires": ["interval","blend_curve"], "forbidden_for": ["hard_boolean_contact"] },
    "conjoin_or_conflict":{ "allowed_types": ["array"], "on_incompatible_hard_constraints": "error" }
  }
}
```

## Scope cascade resolution

When the same field is set at multiple levels:

```text
studio defaults
  → project profile (extends studio, typed merge per style domain)
    → sequence (extends project)
      → scene (extends sequence)
        → shot (extends scene)
          → beat (extends shot)
            → event/frame (extends beat)
```

At each level, the merge policy for that path determines how the override combines
with the inherited value. Locks prevent override without explicit unlock.

## Authority precedence

When two values at the same specificity conflict:

1. **Safety** — never overridden (e.g., stunt clearance, content rating)
2. **Asset identity** — locked references, rig integrity
3. **Continuity** — cross-shot consistency requirements
4. **Director hard** — explicit director overrides
5. **Department** — FACS, Laban, camera, VFX, audio, marketing
6. **Adapter** — model-specific constraints

## Key rules

- Every inheritable path MUST declare a typed merge policy
- `extends` and `overrides` MUST NOT remain as unresolved instructions in canonical JSON
- `effective_styles` MUST contain resolved values
- `provenance` MUST retain enough information to reconstruct why each effective field exists
- Null, missing, and delete are distinguished
- Locked fields require explicit unlock before override
- Hard constraints from different sources conjoin; if incompatible → error
