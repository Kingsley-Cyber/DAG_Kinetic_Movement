---
id: interaction.grip_case_and_earbud
pass: interaction
triggers: ["unboxes", "opens the charging case", "wireless earbuds", "earbuds", "puts one earbud in his ear", "hinged lid", "small part pinched by the stem"]
not_when: ["the case lid slides or pulls off instead of hinging", "the earbud insertion must be shown in close-up (frame it hidden instead)", "only one hand is free and nothing braces the case"]
backs: [cpcs.contact.interaction_lifecycle, cpcs.mx.affordance_constraints]
from: "Additional/HANDS_CONTACT_MANIPULATION.md §2.2 (grip taxonomy: palm/support, precision pinch), §2.3 (one bounded motion; minimize interacting parts; conceal the impossible frame), §3 (object events have pre/post state), §5 (contact is the expensive frame: commit short and rigid, or conceal)"
origin: PROJECT_DERIVED
importance: 0.85
---
# Palm support + precision pinch for a hinged case and an earbud

Name the grip so each hand has a job. The case is a rigid hinged box: one hand cradles it in the
palm (support) and keeps the thumb free for the lid; the other hand pinches the small part by its
stem (precision pinch). One bounded motion, one direction, once. The ear is the expensive frame:
the insertion is carried by the hand and the side of the head, not shown up close.

## Wording
```prompt core
His {case_hand} hand cradles the charging case in the palm, fingers around its sides, thumb free on the lid lip; his {bud_hand} thumb and index finger pinch one earbud by its stem. The box, the case and the earbuds stay rigid. One bounded move at a time, in one direction, once.
```
```prompt core short
His {case_hand} hand cradles the case, thumb on the lid lip; his {bud_hand} thumb and index pinch one earbud by its stem.
```

## Failure signs
- Hand and case fuse, or fingers wrap through the plastic.
- The lid is already open before the thumb reaches it, or the lid detaches.
- Both earbuds leave the case, or an earbud appears in the hand and in the ear at once.
- Extra or missing fingers at the pinch; the earbud grows or shrinks on the way to the ear.

## Effects
- claim: naming palm support + precision pinch yields a readable case-open and earbud pick-up · evidence_status: unverified · model: seedance · runs: —
