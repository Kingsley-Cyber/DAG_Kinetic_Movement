---
id: cpcs.provider.veo.src001_findings
kind: provider_finding
epistemic_status: SOURCE_EVIDENCE
acquisition: observed
sources: [SRC-001 §15, SRC-001-U13]
primary_route: cpcs/providers/veo/
secondary_routes:
  - cpcs/runtime/08_provider_negotiation/capability_matching/
interfaces: []
---

# Google Veo — SRC-001 Findings

> Version caveat: findings reflect the Veo 3 prompting guide as summarized
> in SRC-001 at its writing date. Capabilities are per model/version, not
> timeless (open question Q4).

## Documented prompt structure

Google's Veo prompting guide explicitly calls out:

```text
shot framing/motion
style
lighting
character description
```

## CPCS implications

Projection mapping:

```text
canonical camera   → framing + camera movement
canonical style    → visual style projection
canonical lighting → lighting projection
```

**Do not collapse these into a single `style` string.**

## Links

- Camera three-layer semantics: `knowledge/12_camera_image_formation/`
- Style constraint model: `knowledge/16_style_visual_language/invariants/`
