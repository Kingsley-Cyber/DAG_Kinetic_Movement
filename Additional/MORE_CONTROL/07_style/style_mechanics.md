---
id: cpcs.mx.style_mechanics
kind: doctrine
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §90]
primary_route: cpcs/knowledge/16_style_visual_language/
interfaces: [cpcs.style.constraint_model]
---

# Style Mechanics

Style controls should map into measurable/observable dimensions rather than
accumulate adjectives.

## Style dimensions

```text
amplitude · tempo · onset sharpness · duration · path curvature ·
symmetry · effort · stability · variability · settling
```

Then `snappy` can become:

```text
short onset + high acceleration + low dwell + rapid recovery
```

rather than a stack of synonyms.

## Verification

`test_style_maps_to_dimensions`,
`test_no_synonym_accumulation`.

## Style transformation vector (SRC-005 §28)

SRC-005 models style as a typed transformation from a neutral or source score
to a target score, subject to invariants. A scalar `style_intensity` is a
convenience control that the compiler expands into named dimensions:

```json
{
  "style_transform": {
    "source_profile":"natural_human",
    "target_profile":"anime_sakuga_action",
    "dimensions": {
      "timing_compression":1.35,
      "anticipation_expansion":1.20,
      "key_pose_hold_frames":2,
      "arc_exaggeration":1.18,
      "silhouette_separation":1.25,
      "secondary_overlap":1.15,
      "microvariation":0.45,
      "graphic_smear":0.80,
      "impact_frame":1.0,
      "camera_emphasis":1.25
    },
    "invariants":["action_order","support_contact_sequence","target_identity","screen_direction"]
  }
}
```

Values are project controls, not standardized perceptual units.

## Five style profiles (SRC-005 §28.3–§28.7)

| Profile | Key characteristics |
| --- | --- |
| Natural human | physically plausible weight transfer, moderate asymmetry, realistic limits |
| High-fidelity UGC | direct lens address, self-framing, speech gesture, product handling |
| Feature animation | anticipation, staging, follow-through, overshoot, controlled squash/stretch |
| Anime/limited | held drawings, low exposure cadence, smear frames, impact grammar |
| Superhuman | virtual physics changes, phase-specific transforms, graphic deformations |

## Cross-style invariants (SRC-005 §28.8)

Recommended invariants: action identity and order, participant and target
identity, support/contact topology, safety classification, shot purpose,
critical gaze or product visibility, start/end narrative state, locked
dialogue and audio events, rights and identity replacements.

## Style ablation (SRC-005 §28.9)

To test a style profile, generate the same action with one dimension changed
at a time: base action, +anticipation only, +key-pose holds only, +arc
exaggeration only, +microvariation only, +VFX only, +full profile. This
identifies which controls actually produce the perceived style and which
merely add noise.
