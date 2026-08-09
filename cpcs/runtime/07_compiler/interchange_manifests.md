---
id: cpcs.runtime.interchange_manifests
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §21]
primary_route: cpcs/runtime/07_compiler/
secondary_routes:
  - cpcs/knowledge/06_body_motion/biomechanics/
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.body.skeleton_topology
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.format_ownership
  - cpcs.found.timebase_systems
---

# BVH, FBX, Dense Arrays, and Canonical Interchange

> **Source:** SRC-005 §21 — "BVH, FBX, dense arrays, and canonical interchange"

## Principle

CPCS-MX does not replace established animation files. It assigns them a
narrower and more precise role. A motion-capture or DCC format carries
geometry and animation data; a CPCS-MX score carries the meaning, authority,
constraints, evidence, and compilation policy surrounding that data. The two
are linked rather than conflated.

## BVH as transparent skeletal-motion interchange

BVH strengths: simplicity, portability, human inspectability. An extractor
can deterministically recover hierarchy, channel order, root translation,
Euler rotations, sample cadence, and a dense motion matrix.

BVH limitations:

```text
no declared physical unit
coordinate handedness and up-axis are workflow conventions
Euler channel order varies and must be preserved
no contacts, force, torque, facial AUs, Laban, camera intent, safety, or evidence
not a complete character rig (may omit twist, fingers, facial, deformers)
bone length and topology may differ from target skeleton
```

A CPCS-MX importer wraps raw motion in an explicit manifest:

```json
{
  "asset_id": "motion.bvh.reference_walk.001",
  "uri": "tracks/reference_walk.bvh",
  "media_type": "application/x-bvh",
  "sha256": "…",
  "declared_units": {"translation": "centimeter", "rotation": "degree"},
  "coordinates": {"handedness": "right", "up_axis": "+Y", "forward_axis": "+Z"},
  "rotation_channels": "preserve_source_order",
  "source_fps": 60,
  "import_transform": {"scale_to_meter": 0.01, "basis_change": "bvh_y_up_to_cpcs_y_up"}
}
```

The importer must verify the reconstructed global pose at selected frames.

## FBX as production container

A deterministic FBX intake records: SDK/importer version, source and target
units, axis conversion, transform inheritance mode, pre/post-rotation
handling, animation stack and layer selection, curve interpolation and tangent
mode, resampling rate, constraint baking policy, and skeleton/mesh bind-pose
hashes. Two FBX files are never assumed equivalent merely because they contain
the same number of frames; their evaluated global transforms must be compared
after the same import policy.

## Canonical score versus dense tracks

JSON is suitable for hierarchy, events, constraints, intervals, provenance,
and references. It is inefficient for millions of floating-point samples.
The recommended architecture:

```text
canonical CPCS-MX JSON
├── project, characters, rigs, actions, phases, contacts
├── Laban, face, breath, mannerism, style, camera
├── hard/soft/perceptual constraints
├── track manifests and content hashes
└── references to dense assets

external track assets
├── root transforms, joint rotations, optional joint positions
├── velocities and accelerations
├── pose-confidence arrays, contact probabilities
├── dense facial coefficients, simulation caches
```

Dense arrays may be stored as NumPy-compatible, HDF5, Arrow/Parquet, engine
clips, or video control passes. The score must declare encoding, shape, dtype,
ordering, timebase, coordinate system, and checksum.

## Canonicalization pipeline

```text
BVH / FBX / engine clip / mocap stream
                 ↓
parse without semantic loss
                 ↓
normalize units and coordinate basis
                 ↓
map source joints to canonical semantic joints
                 ↓
resample only when necessary
                 ↓
compute global transforms and verification landmarks
                 ↓
externalize dense arrays
                 ↓
write canonical JSON manifest and provenance
```

The original asset remains immutable. Every conversion creates a new asset
record linked through `derived_from`.

## Loss accounting

Every exporter produces a loss report:

```yaml
loss_report:
  source: motion.fbx.take_03
  target: motion.bvh.take_03
  unsupported:
    - facial_blendshapes
    - animation_layers
    - constraints
    - camera
  baked:
    - control_rig_constraints
  resampled:
    from_hz: 120
    to_hz: 60
  maximum_global_joint_error_m: 0.0042
  maximum_root_orientation_error_deg: 0.18
```

Without this report, an agent may retrieve a simplified BVH and incorrectly
assume it contains the full source performance.

## Interchange verification

At minimum: joint-name and parent mapping, bind/rest pose, root transform and
facing, scale and limb lengths, global transforms at first/middle/last/contact
frames, left/right consistency, quaternion sign continuity or Euler unwrap,
sample count and exact time span, event alignment after resampling, preserved
locks and constraints, and content hashes. The expected output is a quantified
equivalence statement, not simply "import succeeded."

## Boundary

This card defines interchange manifests. It does not replace BVH, FBX, or
engine-native formats; it wraps them with semantic metadata and loss
accounting.
