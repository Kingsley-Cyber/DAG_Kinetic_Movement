---
id: cpcs.motion.laban.layering_not_canonical
kind: doctrine
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §20.1, §24-P2.6, §15, SRC-002 §10, §13]
primary_route: cpcs/knowledge/06_body_motion/laban_bess/
secondary_routes:
  - cpcs/knowledge/06_body_motion/kinematics/
interfaces: [style_x_motion, motion_x_camera]
---

# Laban/BESS Layering Doctrine

## Doctrine

Laban/BESS is valuable for expressive movement semantics but is **not the
canonical kinematic representation**. It is not a substitute for position,
orientation, velocity, acceleration, phase timing, or contact state.

Recommended layering:

```text
kinematics + phase + Laban/BESS        (layered, each owning its dimension)
```

never:

```text
Laban/BESS → everything
```

## Five-category LMA structure (SRC-002 §10)

Laban is represented across five owned fields — never collapsed:

| Field | Question | Canonical values |
|---|---|---|
| `laban_body` | what moves | parts + action |
| `laban_effort` | how / energy | weight: light\|strong · time: sustained\|sudden · space: indirect\|direct · flow: free\|bound |
| `laban_space` | where oriented | reach · zone · direction · pathway |
| `laban_shape` | bodily form change | horizontal: spreading\|enclosing · vertical: rising\|sinking · sagittal: advancing\|retreating |
| `laban_phrasing` | temporal emphasis | beginning/middle/end etc. |

## Reliability (SRC-002 §13, U09)

A 2019 CMA-rater study found only weak-to-acceptable reliability;
Effort/Shape carry greater subjective inference than spatially explicit
dimensions. CPCS may encode Laban as authored semantic controls and compute
proxies, but must not label a kinematic proxy as "the true Laban value"
without calibration. See `laban_proxy_measurement_contract.md`.

## Directing implications

- Effort qualities (`weight/time/space/flow`) travel in their own fields and
  inform provider-facing prose and style compilation.
- Direct Laban-to-provider compilation is a **P2 experiment**, not default
  behavior: Runway guidance indicates overly conceptual language yields less
  predictable motion, so abstract Laban/VAD labels should be compiled into
  observable action descriptions before provider projection.

## Applies when

Any motion object carries expressive quality attributes alongside kinematics.

## Failure mode

Emitting raw Laban labels to providers expecting observable descriptions
(unpredictable motion adherence).
