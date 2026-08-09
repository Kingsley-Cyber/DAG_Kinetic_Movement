# 07 — Interaction Layer: Motion Predicates and Contact Topology

## Executive finding

Interaction must be represented as relations among entities over time, not inferred from isolated poses. A hand near a cup is not necessarily grasping it; a block is not simply two wrists that overlap in image space. CPCS uses a temporal attributed multigraph with actor/body-part/object/surface nodes and contact, grasp, support, constraint, proximity, and gaze edges.

HICO-DET supplies a broad seed vocabulary of human-object verbs and objects, while BABEL, Inter-X, InterGen, and contact-guided HOI work contribute temporal labels, two-person interaction, generation, or contact conditioning. None is a complete continuous-force ontology, so CPCS must add explicit contact states and physics metadata. [S034; S035; S036; S037; S038]

## Predicate vocabulary

| Predicate | Definition | Core roles | Optional roles |
|---|---|---|---|
| support | maintain load/stability | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| touch | non-load-bearing contact | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| contact | generic physical contact | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| grasp | constrain target against free separation | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| hold | maintain grasp/support | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| release | terminate contact constraint | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| push | apply force increasing distance | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| pull | apply force reducing distance | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| press | sustained compression | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| slide | tangential motion under contact | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| roll | rotational progression with limited slip | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| carry | support and transport | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| lift | increase height against gravity | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| lower | controlled decrease in height | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| throw | accelerate then release into flight | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| catch | intercept and transition to support/grasp | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| place | transport then release at intended pose | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| open | change articulated object toward open state | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| close | change articulated object toward closed state | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| strike | transient impact | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| block | interpose to prevent/absorb path | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| parry | briefly redirect incoming path | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| deflect | change trajectory away | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| redirect | change force/motion direction | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| trap | constrain degrees of freedom | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| pin | constrain against environment/body | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| evade | avoid predicted contact | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| dodge | rapid evade with readiness | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| intercept | arrive at future path/time | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| collide | neutral/unplanned impact | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| stagger | balance loss/recovery after perturbation | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| yield | allow displacement under controlled compliance | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| resist | oppose force/displacement | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| guide | low-force directional constraint | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| embrace | bilateral enclosing social/support contact | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| shield | interpose to protect | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| mount | establish supported position atop target | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| disarm | cause held object release | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| handoff | transfer grasp/support ownership | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| point_at | orient distal effector to indicate | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| look_at | orient gaze | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| approach | reduce distance | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| retreat | increase distance | agent, patient_or_target | instrument, surface, beneficiary, opponent |
| circle | move around target while oriented | agent, patient_or_target | instrument, surface, beneficiary, opponent |

Predicates should use controlled definitions and preconditions/effects. `throw` is compound: grasp → accelerate object → release → free flight. `catch` is intercept → absorb relative motion → establish support/grasp. `block` changes or terminates an incoming path through interposition; `parry` usually creates brief redirecting contact; `evade` succeeds without required contact.

## Predicate record

```json
{
  "predicate_id": "block",
  "agent": "fighter_b",
  "patient": "fighter_a.right_fist",
  "agent_body_parts": ["left_forearm"],
  "t_start_s": 0.42,
  "t_end_s": 0.51,
  "phase_links": ["defense_01.stroke"],
  "contact_ids": ["contact_44"],
  "preconditions": ["fist_on_collision_course"],
  "effects": ["incoming_path_redirected", "head_contact_prevented"],
  "confidence": 0.91
}
```

## Contact topology

A contact edge stores interval, body/object parts, point or surface patch, normal and tangent basis, mode (`stick`, `slide`, `roll`, `impact`, `separate`), relative velocity, force if known, friction, compliance, and confidence.

Core invariants:

- a sticking contact has near-zero tangential relative velocity within tolerance;
- a support contact contributes load-bearing or stability;
- a grasp constrains the intended degrees of freedom;
- a release closes the active constraint before free flight;
- meshes do not penetrate beyond configured tolerance;
- a reaction cannot causally precede contact unless it is anticipation/evasion.

## Two-person patterns

**Combat exchange:** attack → defense/interception → counter → reaction/recovery. Actions overlap in time; the counter may prepare during the attacker’s overshoot, but its causal effects cannot precede the defense.

**Dance partnering:** shared support, counterbalance, lead/follow information, synchronized and complementary trajectories, and role changes. A visual model can produce plausible silhouettes while violating the shared-force relation; contact validation remains necessary.

**Conversation:** proxemics, gaze, turn-taking, gesture holds, mirroring, and culturally conditioned touch.

**Handoff:** giver support/grasp → shared grasp → receiver support/grasp → giver release. There should be no unsupported interval unless dropping is intended.

## Person-object and environment patterns

- tool use: approach → grasp → align → engage → apply → disengage → release;
- wall: touch, brace, push, slide, collide, rebound;
- floor: support, step, kneel, roll, slide, fall, recover;
- obstacle: approach, vault, climb, duck, evade, collide;
- prop/weapon choreography: stowed, grasped, ready, moving, contact, released. CPCS encodes cinematic state and safety constraints, not operational weapon instruction.

## Chained example

`block → redirect → strike → push → stagger`

1. Block establishes defensive contact.
2. Redirect changes the incoming path and opens a line.
3. Strike applies a brief impulse.
4. Push extends contact and displaces COM.
5. Stagger describes balance loss/recovery, not merely backward translation.

The validator checks temporal order, contact continuity, causal target, support margin, and incompatible simultaneous constraints.

## Model prompting

Text-only prompt:

> “The defender’s left forearm meets the attacker’s right wrist before the fist reaches the face. The contact redirects the wrist outward rather than stopping dead. Without breaking contact, the defender steps in and presses the attacker’s shoulder, shifting the attacker’s center of mass beyond the rear foot; the attacker takes two recovery steps.”

Reference-conditioned generation should supply the contact path or performance video; prose alone is a lossy fallback.

## References and locators

- **[S034]** Yu-Wei Chao et al. (2018), *HICO-DET: A Benchmark for Recognizing Human-Object Interactions in Images*. **Locator:** WACV 2018; 600 HOI classes, 117 verbs, 80 objects  
- **[S035]** Abhinanda Punnakkal et al. (2021), *BABEL: Bodies, Action and Behavior with English Labels*. **Locator:** CVPR 2021; dataset and annotation sections  
- **[S036]** Han Liang et al. (2023), *Inter-X: Towards Versatile Human-Human Interaction Analysis*. **Locator:** CVPR 2023; dataset statistics and interaction annotations  
- **[S037]** Han Liang et al. (2023), *InterGen: Diffusion-Based Multi-Human Motion Generation Under Complex Interactions*. **Locator:** Paper §§3–5 and repository documentation  
- **[S038]** CG-HOI authors (2024), *Contact-Guided Human-Object Interaction Synthesis*. **Locator:** Contact representation and synthesis sections  
- **[S068]** Alexandros Paraschos et al. (2013), *ProMPs: Probabilistic Movement Primitives*. **Locator:** Representation, conditioning, blending
