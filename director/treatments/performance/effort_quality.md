---
id: performance.effort_quality
pass: performance
triggers: ["strike", "block", "interception", "movement quality", "effort", "how the move is delivered", "punch", "shove"]
not_when: ["no performer on screen", "an overall manner or register is asked rather than one action's quality (use performance.casual_register)"]
backs: [cpcs.motion.laban.layering_not_canonical, cpcs.laban.numeric_calibration_contract, cpcs.body.combat_coding]
from: "plan/ARCHITECTURE.md §3.5.1 (movement control: Laban Effort as scaled values with confidence) and §3.5.4 (Bartenieff: where the action starts and which parts follow); plan/EXPERIMENTS.md E3 (wording rungs: numeric, term, visible)"
origin: PROJECT_DERIVED
importance: 0.8
---
# One action's movement quality, written as visible behaviour

The control stores the quality as Laban Effort scales (`weight`, `time`, `space`, `flow`, each 0–1,
with a `confidence`) plus `subject` (who moves) and `visible`: one sentence the performance pass
writes that says where the action starts in the body, what it passes through and how it arrives.
The default wording is that sentence only. The scales never reach the prompt as numbers or pole
words unless an experiment arm asks for it (`emit --rung term|numeric`, experiment E3).

## Wording
```prompt core
{visible}.
```

## Failure signs
- The action is delivered by the arm alone; feet and hips do not take part.
- The quality reads as a pose change, not a motion with a start and an arrival.
- The move is stiff or exaggerated beyond what the anchor comparison asks for.

## Effects
- claim: a visible start-through-arrival sentence is followed better than a Laban term or a numeric block for the same quality · evidence_status: unverified · model: seedance · runs: — (experiment E3, run 006)
