---
id: performance.casual_register
pass: performance
triggers: ["casual", "UGC", "films herself", "talking to the phone", "natural", "not an ad", "like a friend"]
not_when: ["scored or choreographed performance", "cinematic drama"]
backs: [cpcs.ugc.realism_reference, cpcs.motion.laban.layering_not_canonical]
from: "Additional/LIVING_PERFORMANCE_REALISM.md §4 (time is the differentiator), §8 (compile AU and effort terms to plain language), §9 (reads-real checklist); prompt-system lab/blocks.yaml blk_face_motion_alive, pattern p004 (loose beats scored)"
origin: PROJECT_DERIVED
importance: 0.7
---
# Casual register, with movement quality as visible behaviour

Loose, low-key, unforced. Each beat gets its own small schedule rather than one generic
"natural" bundle. Laban qualities are scaled values; they compile to what the camera sees, never
to the term itself.

## Wording
```prompt core
Her manner is {register}: {weight_word} {time_word} movements, {space_word} in reaching for the bottle, grip {flow_word}. A small breath before she reaches, a glance down at the cap as it turns, eyes back to the lens after the drink, one faint satisfied exhale. Face alive but not performed: a blink, a slight brow lift, uneven small expressions, no fixed smile.
```

```prompt core short
Her manner is {register}; {weight_word}, {time_word} movements; a breath before she reaches, a glance down as the cap turns, eyes back to the lens after the drink; face alive, no fixed smile.
```

## Failure signs
- Actor hitting marks: even energy, held smile, locked stare at the lens.
- Frozen face between actions; perfectly symmetrical expression.
- Uniform "aliveness" reused on every beat.

## Effects
- claim: casual register with a per-beat schedule reads as candid, not acted · evidence_status: supported (bundled) · model: veo-3.1 · runs: prompt-system r001 vs r003
- claim: same on Seedance · evidence_status: unverified · model: seedance · runs: —
