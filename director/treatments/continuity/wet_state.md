---
id: continuity.wet_state
pass: continuity
triggers: ["wet", "soaked", "fully clothed", "falls into the pool", "gets splashed", "comes up out of the water", "rain", "drenched"]
not_when: ["the actor stays dry", "the clothes are meant to dry within the clip", "the water is only touched with the hands"]
backs: [cpcs.mx.continuity_state, cpcs.mx.material_response]
from: "Additional/07 CPCS World Model _ Causal State _ Attention Gap Closure.md §1 (persistent changes: a delta persists after its cause; persistence and reversibility) and the persistent character state list (wardrobe and wetness as a state transition); cpcs/knowledge/17_vfx_secondary_motion/material_response.md (persistence mode: decay)"
origin: PROJECT_DERIVED
importance: 0.85
---
# Wet stays wet

A state that changes once stays changed: after the water entry, clothing and hair stay wet and
cling for the rest of the clip, and the water itself keeps moving as the splash decays. State the
persistent result as a visible outcome after the event, not as a rule.

## Wording
```prompt core
From the moment he hits the water, {wet}, and {surface}.
```
```prompt core short
From the water on, {wet_short}, and {surface_short}.
```

## Failure signs
- The shirt or hair is dry again after he surfaces, or the wetness appears before the entry.
- Clothes look dry-draped instead of clinging.
- The pool is flat the instant after the splash, or the ripples never decay.

## Effects
- claim: stating the persistent result after the event keeps the wet state through the last frame · evidence_status: unverified · model: seedance · runs: —
