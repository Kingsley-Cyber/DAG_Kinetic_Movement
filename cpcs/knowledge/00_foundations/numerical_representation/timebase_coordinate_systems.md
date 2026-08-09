---
id: cpcs.found.timebase_systems
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §4]
primary_route: cpcs/knowledge/00_foundations/numerical_representation/
secondary_routes:
  - cpcs/knowledge/00_foundations/architecture/
  - cpcs/verification/
interfaces:
  - cpcs.found.exactness_taxonomy
  - cpcs.runtime.canonical_schema
  - cpcs.found.numeric.motion_field_separation
---

# Timebase and Coordinate Systems

> **Source:** SRC-005 §4 — "Time, clocks, units, and coordinate systems"

## Principle

Precision begins with a clock. Frame numbers alone are insufficient when the
source is variable-frame-rate, retimed, or edited from multiple streams.
CPCS-MX stores a canonical time in seconds or rational media time, then permits
frame indices as views derived from a declared frame rate.

## Time representation

A project declares a timebase object:

```json
{
  "timebase": {
    "canonical": "seconds",
    "fps": {"numerator": 24000, "denominator": 1001},
    "source_clock": "presentation_timestamp",
    "sample_rate_hz": 120,
    "rounding": "nearest_source_frame"
  }
}
```

Events carry both a time and, when relevant, a source-frame identifier. Time
intervals use half-open semantics — `[start, end)` — unless explicitly declared
otherwise. A one-frame impact drawing at 24 fps is not equivalent to a 41.67 ms
continuous event if the target renderer performs motion interpolation; the score
must state whether the frame is a held drawing, an exposure, or a sample in a
continuous trajectory.

## Eight coordinate frames

| Frame | Meaning |
| --- | --- |
| `world` | scene-level coordinates |
| `character_root` | orientation and translation of the character controller |
| `pelvis_body` | anatomical or rig-centered reference |
| `joint_local` | child transform relative to parent |
| `camera` | coordinates relative to the optical center |
| `screen` | normalized image coordinates |
| `object` | prop-relative coordinates |
| `contact` | local tangent, normal, and binormal at an interaction surface |

Every vector requires a frame. `force: [0, 500, 0]` is meaningless without
units, coordinate axes, point of application, and whether it is measured,
inferred, or simulated.

## Units and normalization

CPCS-MX uses SI units internally by default: meters, seconds, kilograms,
Newtons, Newton-meters, radians, and radians per second. Screen-space
coordinates can be normalized to `[0,1]`, but the schema must identify image
dimensions and origin convention. Laban values, affect values, style
intensities, and confidence values are dimensionless and require declared
ranges.

Normalized values should not erase physical values. A `root_speed_norm: 0.8`
can be useful to a learned model, but the canonical record should retain the
scale used to compute it. A joint's normalized range should reference a
rig-specific minimum and maximum rather than implying universal anatomy.

## Multi-modal synchronization

Motion, audio, face, camera, and VFX often have different sampling rates. The
system retains source clocks and defines synchronization transforms. An impact
may have visual near-contact at `t = 2.4167 s`, a one-frame flash at the same
exposure, camera shake beginning 8 ms later, impact sound onset 20 ms later,
and facial tightening reaching an apex 100 ms later. These are separate events
with causal links, not one overloaded timestamp.

When timing is inferred from compressed video, the record should include the
temporal resolution and confidence instead of reporting false precision.

## Boundary

This card defines the canonical time and coordinate contract. It does not
prescribe a single physical unit convention for all exports; adapters may
convert, but every conversion must be explicit and loss-accounted.
