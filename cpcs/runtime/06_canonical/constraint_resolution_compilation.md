---
id: cpcs.runtime.constraint_compilation
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §26]
primary_route: cpcs/runtime/06_canonical/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/knowledge/06_body_motion/biomechanics/
interfaces:
  - cpcs.runtime.canonical_schema
  - cpcs.body.skeleton_topology
  - cpcs.runtime.motion_matching
  - cpcs.runtime.format_ownership
---

# Constraint Resolution and Compilation

> **Source:** SRC-005 §26 — "Constraint resolution and compilation"

## Principle

A score becomes executable only after inheritance, references, conflicts, and
target capabilities have been resolved. The compiler is not a serializer. It
is a typed constraint-resolution system that produces an execution package and
an auditable loss report.

## Scope cascade

CPCS-MX permits defaults and overrides at multiple scopes:

```text
studio → production → sequence → scene → shot → beat → action → event → frame/sample
```

Specificity alone is not sufficient. A lower scope cannot override a locked
higher-scope safety or identity rule unless the authority policy explicitly
permits it. The effective precedence tuple is:

\[
P = (\text{authority},\; \text{lock},\; \text{specificity},\; \text{revision},\; \text{source order}).
\]

`source order` is a final deterministic tie-breaker, not a substitute for
meaningful precedence.

## Typed merge behavior

| Type | Default operation | Example |
| --- | --- | --- |
| scalar setting | replace | gravity profile |
| object | recursive merge | cinematography profile |
| keyed entity array | merge by stable ID | actions, constraints |
| ordinary ordered array | replace or append by policy | prompt clauses |
| numerical curve | splice/blend/replace interval | AU intensity |
| interval descriptor | interval algebra | Laban phrase |
| hard constraint | union, then feasibility check | foot lock + hand target |
| asset reference | replace with provenance | character reference |
| lock | monotonic unless authorized unlock | contact frame |

A generic deep-merge library is insufficient. It may append duplicate
constraints, merge incompatible coordinate systems, or overwrite one temporal
key without recomputing interpolation.

## Curve composition

Curve fields specify: operation (`replace`, `add`, `multiply`, `max`, `min`,
`blend`, `warp_time`), interval, blend envelope, unit, coordinate frame,
priority, and whether the operation is commutative. A root-position curve
would not normally be composed additively; a breathing curve might be.

## Constraint graph

The compiler builds a graph whose nodes are variables, tracks, events, and
assets. Edges express: equality or inequality, temporal relation, geometric
relation, dependency, derivation, authority, and mutual exclusion. If the
target is unreachable without moving a locked root or violating joint limits,
the compiler reports an infeasible set. It can suggest alternatives but must
not silently choose.

## Hard and soft solving

\[
\min_x \sum_i w_i E_i(x)
\quad \text{subject to} \quad
h_j(x)=0,\quad g_k(x)\le 0,
\]

where hard contacts, non-penetration, and locked events become constraints,
while pose fidelity, smoothness, style, and energy become weighted objectives.
CPCS-MX adds a policy layer: `hard_failure: reject`, `soft_failure:
emit_metric`, with a deterministic seed and a declared priority order.

## Three joint-limit profiles

1. `anatomical_reference`: documented human range or research model
2. `rig_safe`: transform range that preserves the specific character mesh
3. `virtual_stylized`: deliberately nonhuman range in the stylization layer

The skeleton solver should not exceed `rig_safe` merely because a
`virtual_stylized` deformation allows the rendered silhouette to stretch
farther. That stretch is implemented through mesh deformation, camera
perspective, smear geometry, or a separate nonhuman rig.

## 15 compilation passes

1. Parse YAML/JSON/XML authoring inputs
2. Resolve includes and stable references
3. Normalize types, units, clocks, and coordinate systems
4. Expand profiles and inheritance
5. Apply authority and lock rules
6. Build event and constraint graphs
7. Detect temporal and geometric conflicts
8. Resolve or report feasibility
9. Generate or import dense base motion
10. Apply retargeting and IK
11. Apply style and superhuman transforms under invariants
12. Generate face, gaze, breath, and secondary tracks
13. Compile camera, audio, VFX, and edit events
14. Negotiate target capabilities
15. Emit target package, loss report, and verification plan

Each pass writes an immutable intermediate artifact with a hash when
reproducibility is required.

## Compilation products

The same resolved score can produce different packages: DCC package (FBX/scene
+ rig curves + contacts + camera + notes), engine package (animation clips +
root trajectory + state/action graph + IK tasks), text-to-motion package
(action prompt + event tokens + sparse joint constraints), video package
(prompt + references + pose/depth/mask controls + camera render), and RAG
package (semantic chunks + field docs + examples + source records).

## Deterministic build identity

A build identity includes: canonical score hash, dense asset hashes, compiler
version and commit, profile versions, model and adapter version, solver
settings, random seeds, platform-dependent settings, capability report, and
unresolved warnings. Without this identity, "same prompt" is not a
reproducible specification.

## Reference implementation (SRC-008 EXTEND)

The frozen package provides a working reference compiler
(`compile_authoring_yaml.py`, 437 lines) whose concrete behavior is documented
in `cpcs.runtime.mx_compiler`. Key implementation details:

- **3 append-path suffixes** where lists concatenate: `hard_constraints`,
  `soft_constraints`, `verification.recommended_metrics`.
- **6 ID keys** for list-item matching: `id`, `action_id`, `constraint_id`,
  `event_id`, `track_id`, `system_id`.
- **4 exit codes**: 0 (success), 2 (authoring error), 3 (canonical error),
  4 (unresolved items).
- **Profile URIs** use `profile://<category>/<name>` with regex whitelist and
  path-traversal protection.
- **Imports** are SHA-256 verified and sandboxed to the authoring parent dir.
- **Deterministic serialization**: `json.dumps(candidate, indent=2, ensure_ascii=False)`.

The reference compiler does NOT synthesize motion. Its capability report always
includes `"dense_motion_synthesis": "not_implemented"`.

## Typed merge algebra (SRC-009 EXTEND)

SRC-009 formalizes the merge behavior above into a typed merge algebra with
10 data kinds and 9 merge policies. Each candidate value is a tuple
c = (p, v, a, s, q, ℓ, h, o, r) with 9 fields (field path, value, authority
class, specificity, priority, lock, hard/soft, order, provenance).

The 9 merge policies are: `replace`, `deep_merge_typed`, `merge_by_id`,
`append_ordered`, `set_union`, `replace_track`, `splice_interval`,
`blend_interval`, `conjoin_or_conflict`. The schema declares which policy
governs each path. `blend_interval` is forbidden for hard boolean contact.

Authority precedence (6 levels): safety > asset_identity > continuity >
director_hard > department > adapter.

See `cpcs.runtime.typed_merge_algebra` for the complete algebra.
