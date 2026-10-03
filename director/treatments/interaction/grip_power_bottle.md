---
id: interaction.grip_power_bottle
pass: interaction
triggers: ["opens a bottle", "unscrews the cap", "twist-off cap", "opening a water bottle", "takes the lid off"]
not_when: ["bottle is already open", "sports cap or flip top (use a one-hand thumb flick instead)", "only one hand is free and nothing braces the bottle"]
backs: [cpcs.contact.interaction_lifecycle, cpcs.mx.affordance_constraints]
from: "Additional/HANDS_CONTACT_MANIPULATION.md §2.2 (grip taxonomy), §2.3 (one bounded motion), §3 (object events have pre/post state)"
origin: PROJECT_DERIVED
importance: 0.85
---
# Power grip + precision pinch for a screw-cap bottle

Name the grip so the hand has a job. A screw cap needs two contacts: one hand wraps the bottle
body (power grip) and holds it still; the other hand pinches the cap with thumb and index
(precision pinch) and turns it. One bounded motion, one direction, once.

## Wording
```prompt core
Her {bottle_hand} hand wraps the bottle body in a full grip and holds it still; her {cap_hand} thumb and index finger pinch the cap and turn it once, counter-clockwise, in one short motion. The cap turns while the bottle stays still, label facing the camera.
```

## Failure signs
- Hand and bottle fuse or the fingers wrap through the plastic.
- The bottle body rotates with the cap, or both hands blur into one.
- The cap is off before the fingers reach it.
- Extra or missing fingers at the moment of the pinch.

## Effects
- claim: naming power grip + precision pinch yields a readable, stable open · evidence_status: unverified · model: seedance · runs: —
