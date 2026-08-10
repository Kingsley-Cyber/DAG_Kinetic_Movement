---
id: cpcs.provider.kling.src001_findings
kind: provider_finding
epistemic_status: SOURCE_EVIDENCE
acquisition: observed
sources: [SRC-001 §15, SRC-001-U14]
primary_route: cpcs/providers/kling/
secondary_routes:
  - cpcs/runtime/08_provider_negotiation/capability_matching/
interfaces: []
---

# Kling — SRC-001 Findings

> Version caveat: findings reflect Kling's camera-control documentation as
> summarized in SRC-001 at its writing date. Capabilities are per
> model/version, not timeless (open question Q4).

## Documented controls

Kling's camera-control documentation exposes explicit camera movement
controls and **displacement parameters** for:

```text
horizontal
vertical
zoom
pan
tilt
roll
```

## CPCS implications

Canonical fields:

```text
camera.motion.kind
camera.motion.direction
camera.motion.amount
```

can sometimes map to **native** controls rather than NL projection (see
capability classes in `runtime/07_compiler/semantic_mapping/`).

The adapter must still record whether the provider's control is exact
relative to the canonical semantics — a native control is not automatically
a semantically exact one.

## Links

- Capability classes & loss records: `runtime/07_compiler/semantic_mapping/`
- Camera three-layer semantics: `knowledge/12_camera_image_formation/`
