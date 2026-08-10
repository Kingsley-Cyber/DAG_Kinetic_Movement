---
id: cpcs.provider.runway.src001_findings
kind: provider_finding
epistemic_status: SOURCE_EVIDENCE
acquisition: observed
sources: [SRC-001 §15, SRC-001-U12]
primary_route: cpcs/providers/runway/
secondary_routes:
  - cpcs/runtime/08_provider_negotiation/capability_matching/
interfaces: []
---

# Runway — SRC-001 Findings

> Version caveat: findings reflect Runway Gen-4 guidance as summarized in
> SRC-001 at its writing date. Capabilities are per model/version, not
> timeless (open question Q4).

## Documented prompt structure

Runway's Gen-4 guidance recommends focusing the video prompt on motion and
separates four components:

```text
subject_motion
scene_motion
camera_motion
style
```

Documented camera concepts include locked camera, handheld, tracking, and
focus-related concepts.

## CPCS implications

1. The four components **should compile separately** before being serialized
   into the provider prompt — do not merge them into one prose blob.
2. Runway states overly conceptual language can produce less predictable
   motion. This supports a compiler that turns abstract intent into
   observable action descriptions rather than passing abstract Laban/VAD
   labels directly to the provider.

## Links

- Carrier/semantic mapping: `runtime/07_compiler/semantic_mapping/`
- Laban non-canonicity: `knowledge/06_body_motion/laban_bess/`
