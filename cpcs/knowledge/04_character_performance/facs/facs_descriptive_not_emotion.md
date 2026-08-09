---
id: cpcs.facs.descriptive_not_emotion
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §8, §1.2, SRC-002-U01, SRC-002-U03]
primary_route: cpcs/knowledge/04_character_performance/facs/
secondary_routes:
  - cpcs/knowledge/00_foundations/invariants/
  - cpcs/knowledge/04_character_performance/affect/
interfaces: [state_x_continuity]
---

# FACS Is Descriptive, Not an Emotion Detector

## Boundary

```text
AU12 activated  ≠  person is happy
```

FACS describes **visually discernible facial movement**; it does not detect
emotion, intent, sincerity, or private mental state. The layers are strictly
ordered, and only the first is directly represented by FACS:

```text
visible_facial_movement → facial_configuration
    → contextual/affective interpretation → emotion hypothesis
    → private mental-state claim
```

## Authoring

A director may author a display with an explicit affect target that is
**authorial intent**, not observation:

```yaml
facial:
  display:
    description: restrained_smile
    facs:
      - { au: AU12, target_intensity: B }
      - { au: AU6,  target_intensity: A }
    affect_interpretation:
      valence: positive
      arousal: low
      basis: authored
```

This expresses "display a restrained smile" without asserting "the actor is
happy."

## Firewall

Cross-reference: `knowledge/00_foundations/invariants/epistemic_firewall.md`.
The observation layer must not reverse an authored control into an
unsupported private-state claim (`test_facs_does_not_infer_private_emotion`).
