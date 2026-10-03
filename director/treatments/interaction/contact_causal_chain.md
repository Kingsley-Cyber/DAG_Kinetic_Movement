---
id: interaction.contact_causal_chain
pass: interaction
triggers: ["opens", "picks up", "puts down", "hands over", "hits", "catches", "throws", "any object handling"]
not_when: ["no contact between an actor and an object or another actor"]
backs: [cpcs.contact.interaction_lifecycle, cpcs.found.causality.causal_event_semantics]
from: "Additional/HANDS_CONTACT_MANIPULATION.md §1 (causal grammar and the inviolable laws), §5 (reaction shot proves causality)"
origin: SOURCE_EVIDENCE
importance: 0.9
---
# The causal chain every contact follows

precondition → anticipation → approach → contact → transfer → effect → follow-through → recovery
→ postcondition. Laws that survive any style: contact precedes displacement; a reaction cannot
precede its cause; support precedes force; no ownership change without a contact overlap; a grip
is continuous until deliberately released; screen direction is conserved.

The emitted wording states the causal order and the reaction explicitly, in positive language.
Negative phrasing names failures; it does not encode physics.

## Wording
```prompt core
Every change follows its cause in order: {chain}. Nothing moves, opens or changes before it is touched, and each contact has a visible result.
```
```prompt core short
In order: {chain}; nothing changes before it is touched.
```

## Failure signs
- Effect before contact (the cap is off while the hand is still reaching).
- Grip flickers or the object teleports between hands.
- A reaction with no cause, or a cause with no reaction.

## Effects
- claim: stating the causal order reduces effect-before-contact errors · evidence_status: unverified · model: seedance · runs: —
