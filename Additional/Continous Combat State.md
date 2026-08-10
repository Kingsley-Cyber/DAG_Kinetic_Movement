# Continuous Combat State, Contact, Coarticulation, Anime Time, and Volumetric Cinematography

## Gap-closure research packet

**Version:** 1.0  
**Research date:** 2026-08-08  
**Scope:** controllable AI-video fight direction, reference decomposition, canonical intermediate representation, provider compilation, and verification  
**Priority order:** combat dramaturgy → coupled contact → coarticulation → anime temporal composition → volumetric cinematography

---

## Executive closure

### Existing

The present motion-direction knowledge base can already describe actions, biomechanics, animation principles, camera vocabulary, and provider prompts. It can also carry the same intent through natural language, YAML, JSON, or XML.

Those capabilities are necessary but do not solve the central failure: a fight prompt can still be interpreted as a succession of move cards. Each move begins from a convenient pose, produces a local spectacle, and then releases its consequences before the next move. The result resembles a side-view fighting game even when every individual action is attractive.

### Missing

Five mechanisms are missing or under-specified:

1. A **persistent fight state** whose objective, tactic, initiative, knowledge, emotion, fatigue, injury, ownership, and geography survive every beat.
2. A **time-indexed contact topology** that says which surfaces touch, how long they touch, whether they stick, slide, roll, pivot, support, redirect, or release, and what subsequent motion that contact permits.
3. A **phase-overlap model** in which action B begins changing action A before A ends, including anticipatory postural adjustment, counter-motion, residual momentum, interruption, and recovery-as-preparation.
4. A **presentation-time score** comparable to an exposure sheet: key-pose hierarchy, held drawings, variable exposure, smears, moving backgrounds, layer-specific timing, and purposeful discontinuity.
5. A **world/camera/image-space model** that preserves depth, occlusion, parallax, screen direction, lens-relative velocity, and action continuity across camera motion and cuts.

### Implementable now

These gaps can be closed immediately at the representation and compiler layers:

- Make a canonical **Fight IR** the source of truth; treat YAML, XML, JSON, and natural language as carriers.
- Represent every beat with preconditions, observations, motor phases, contacts, effects, and post-state.
- Maintain separate world-space, actor-local, camera-space, and image-space coordinates.
- Build an interaction graph whose contact edges are intervals rather than single-frame labels.
- Compile a variable-exposure presentation timeline from continuous stage action.
- Use reference video, pose, depth, edge, optical-flow, start/end-frame, and camera signals when the provider supports them.
- Verify the output against state, contact, pose, timing, and camera invariants instead of judging only visual appeal.

### Requires experiment

The following cannot be established from documentation alone:

- how much of the canonical IR each proprietary model actually follows;
- which prompt wording most reliably evokes maintained contact and coarticulation;
- whether raw YAML/XML tags help, harm, or do nothing for a particular provider;
- the provider-specific tradeoff between reference-motion adherence and identity/style preservation;
- tolerance thresholds that predict expert judgments for anime action rather than ordinary human motion.

These require controlled, multi-seed ablations with the same scene and explicit success gates.

### Unknown

No public evidence establishes that a general text-to-video interface exposes deterministic joint trajectories, contact forces, exact 6-DoF body paths, or frame-exact camera transforms through prose. Proprietary systems may internally estimate these quantities, but internal representation is not user control.

The precise influence of YAML, XML, or JSON syntax on proprietary prompt encoders cannot be verified with 100% certainty. Unless an API declares structured fields, the safe interpretation is that these formats are text tokens. Their real value is upstream: validation, inheritance, compilation, and measurement.

---

## Primary conclusion

The game-like structure is not caused mainly by weak move vocabulary. It is caused by **state disposal at action boundaries**.

A continuous fight is not:

```text
attack A → attack B → attack C
```

It is:

```text
state S0
→ observation
→ tactic selection
→ preparation while prior motion persists
→ coupled interaction/contact
→ physical and informational consequences
→ state S1
→ adaptation under those consequences
```

The scene becomes coherent when the next action is the only plausible continuation of the current state, not merely the next item in a list.

---

## Claim classes

| Class | Meaning |
| --- | --- |
| **E** | Empirical or peer-reviewed research finding |
| **D** | Doctrine, production documentation, or established professional practice |
| **C** | Current provider capability documented by the provider |
| **P** | Proposed operational definition, schema, metric, or compiler rule |
| **H** | Testable hypothesis requiring experiment |

Proposed normalized values are not physical measurements. Every normalized field must declare its scale, annotator, and evidence basis.

---

## Evidence ledger

| ID | Claim | Class | Source and locator | Confidence | Measurement implication |
| --- | --- | --- | --- | --- | --- |
| E-01 | Rational action benefits from separate beliefs, desires/goals, and intentions/committed plans. | E | [Rao & Georgeff, *BDI Agents: From Theory to Practice*](https://cdn.aaai.org/ICMAS/1995/ICMAS95-042.pdf), architecture and interpreter sections | High | Store private belief state separately from objective and current tactic. |
| E-02 | Dramatic beats can be sequenced through preconditions and effects on story state. | E | [Mateas & Stern, *Integrating Plot, Character and Natural Language Processing in the Interactive Drama Façade*](https://users.soe.ucsc.edu/~michaelm/publications/mateas-tidse2003.pdf), p. 3 | High | Every fight beat requires preconditions and postconditions. |
| E-03 | Moment-to-moment responsiveness and higher-level beat organization can coexist. | E | [Mateas & Stern, *Structuring Content in the Façade Interactive Drama Architecture*](https://cdn.aaai.org/ojs/18722/18722-52-22361-1-10-20210928.pdf), abstract and beat organization | High | Separate reactive micro-actions from dramatic beat selection. |
| D-01 | Initiative and response form a continuous interplay; opportunity, speed, surprise, and vulnerability change outcomes. | D | [U.S. Marine Corps, MCDP 1 *Warfighting*](https://www.marines.mil/portals/1/Publications/MCDP%201%20Warfighting%20GN.pdf), pp. 48–55 and 77–80 | High | Advantage is a changing vector, not a winner label. |
| D-02 | Terrain affects movement, visibility, engagement, and both sides' dispositions. | D | [U.S. Marine Corps, MCDP 1-3 *Tactics*](https://www.marines.mil/Portals/1/Publications/MCDP%201-3%20Tactics.PDF), pp. 48–50 | High | Geography must be stateful and asymmetric in its effects. |
| E-04 | Kinematic pose estimates can look plausible while violating contacts and dynamics through foot float, penetration, and unnatural lean. | E | [Rempe et al., *Contact and Human Dynamics from Monocular Video*](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123500069.pdf), pp. 1–2 | High | Pose similarity alone is an insufficient success metric. |
| E-05 | Contact is discontinuous and contact combinations grow rapidly over time. | E | Rempe et al., pp. 1–2 | High | Contact must be an explicit switched/interval state. |
| E-06 | Simultaneous contact and behavior optimization can discover complex behavior. | E | [Mordatch, Todorov & Popović, *Discovery of Complex Behaviors through Contact-Invariant Optimization*](https://dl.acm.org/doi/10.1145/2185520.2185539) | High | Contact scheduling is part of motion planning, not post-description. |
| E-07 | Spatial relationships in close interactions can be represented and preserved as an interaction mesh. | E | [Ho, Komura & Tai, *Spatial Relationship Preserving Character Motion Adaptation*](https://dl.acm.org/doi/10.1145/1833349.1778770) | High | Evaluate pairwise spatial relations, not two isolated skeletons. |
| E-08 | Static friction, sliding friction, and normal forces impose different constraints. | D/E | [Drake, *Modeling of Dry Friction*](https://drake.mit.edu/doxygen_cxx/group__friction__model.html), “Physical Model” | High | Distinguish sticking from sliding contacts and validate force direction qualitatively. |
| E-09 | Contact and friction remain difficult even in physics-based animation. | E | [SIGGRAPH 2022 course, *Contact and Friction Simulation for Computer Graphics*](https://siggraphcontact.github.io/assets/files/SIGGRAPH22_friction_contact_notes.pdf), introduction | High | Do not claim prose alone solves contact physics. |
| E-10 | Explicit global relations in a shared world frame improve representation of two-person interaction. | E | [Liang et al., *InterGen*](https://arxiv.org/abs/2304.05684), representation and regularization sections | High | Both performers must share one world frame. |
| E-11 | Sequential actions may coarticulate; the form depends on task constraints. | E | [Kalidindi et al., *Task-dependent coarticulation of movement sequences*](https://elifesciences.org/articles/96854) | High | Phase overlap is conditional, not a universal fixed blend. |
| E-12 | Anticipatory postural adjustments precede voluntary movement to manage expected perturbation. | E | [Berg et al., *Advances in the Study of Anticipatory Postural Adjustments*](https://pmc.ncbi.nlm.nih.gov/articles/PMC11726838/) | High | Encode preparation onset before visible primary action. |
| E-13 | Sensorimotor coarticulation allows later actions to influence execution of earlier sequence elements. | E | [Donnarumma et al., *Sensorimotor Coarticulation in the Execution and Recognition of Intentional Actions*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5322223/) | High | The successor action must be known before predecessor recovery finishes. |
| E-14 | Linear and angular momentum patterns are useful constraints for editing highly dynamic character motion. | E | [Abe, Liu & Popović, *Momentum-based Parameterization of Dynamic Character Motion*](https://grail.cs.washington.edu/projects/charanim/mb.pdf), abstract and §§4–5 | High | Measure residual momentum and boundary velocity, not pose only. |
| E-15 | Motion graphs represent streams of motion through clips and transitions, with nodes as compatible choice points. | E | [Kovar, Gleicher & Pighin, *Motion Graphs*](https://research.cs.wisc.edu/graphics/Papers/Gleicher/Mocap/mograph.pdf), pp. 1–2 | High | Transitions are first-class objects, not empty gaps. |
| D-03 | An X-sheet/timeline operates on frame cells that reference drawings; repeated cells create holds and step-2/3/4 exposure. | D | [OpenToonz 1.7.1, *Working in Xsheet/Timeline*](https://opentoonz.readthedocs.io/en/latest/working_in_xsheet.html), “Working with Cells” | High | Separate output frames from unique drawings per layer. |
| D-04 | An exposure sheet maps drawing identifiers to displayed frames. | D | [Toon Boom Harmony, *About Exposure*](https://docs.toonboom.com/help/harmony-24/premium/timing/about-exposure.html) | High | Anime timing needs exposure runs, not only FPS. |
| E-16 | Smear frames can be generated as art-directable elongated in-betweens along motion trajectories. | E | [Basset, Bénard & Barla, *SMEAR*](https://dl.acm.org/doi/10.1145/3641519.3657457) | High | Smear placement should be velocity- and trajectory-aware. |
| E-17 | Violating the 180-degree rule can confuse or disorient viewers, although it does not necessarily reduce liking. | E | [Kachkovski et al., *Exploring the Effects of Violating the 180-Degree Rule*](https://journals.sagepub.com/doi/10.1177/0093650219838959), abstract | High | Axis crossing is allowed but must be marked as motivated or disorienting. |
| E-18 | Continuity editing influences event segmentation and comprehension across cuts. | E | [Magliano & Zacks, *The Impact of Continuity Editing in Narrative Film on Event Segmentation*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3208769/) | High | Preserve the event state payload across cuts. |
| E-19 | Motion parallax is a time-integrated depth cue based on relative motion. | E | [Nawrot & Stroyan, *Integration time for the perception of depth from motion parallax*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3349336/) | High | Depth staging must be evaluated through time, not from one frame. |
| E-20 | Camera and object motion are separable controls when camera poses and object trajectories are explicit conditions. | E | [Wang et al., *MotionCtrl*](https://wzhouxiff.github.io/projects/MotionCtrl/), abstract and methods | High | Compile independent camera and subject trajectories where supported. |
| E-21 | Optical flow can encode camera/background motion and support detailed camera control. | E | [Jin et al., *FloVD*](https://jinwonjoon.github.io/flovd_site/), abstract and framework | High | Lens-relative velocity and parallax can be verified with optical flow. |
| E-22 | Body-movement kinematics provide cues about emotion, but mappings are probabilistic rather than one-to-one. | E | [Sowden et al., *The Role of Movement Kinematics in Facial Emotion Expression and Emotion Recognition*](https://pmc.ncbi.nlm.nih.gov/articles/PMC8582590/), review | High | Affect must modulate whole-body movement without using rigid stereotypes. |
| E-23 | Fatigue can change coordination, posture, stability, and kinematic variability rather than merely slowing all motion uniformly. | E | [Gates & Dingwell, *The Effects of Muscle Fatigue and Movement Height on Movement Stability and Variability*](https://pmc.ncbi.nlm.nih.gov/articles/PMC9116437/) | High | Store local capacity and coordination effects, not only global exhaustion. |
| E-24 | Symptomatic injury can produce compensatory muscle recruitment and movement patterns. | E | [Veen et al., *Compensatory Movement Patterns Are Based on Abnormal Activity...*](https://pmc.ncbi.nlm.nih.gov/articles/PMC7899608/) | High for the studied shoulder condition | Injury effects must propagate through allowed motions and compensations; do not universalize one clinical pattern. |
| C-01 | Runway Gen-4.5 currently accepts text or image input and produces 2–10 second clips at 24/25 fps. | C | [Runway, *Creating with Gen-4.5*](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5), specs | High as of research date | Treat detailed choreography as prompt guidance, not joint control. |
| C-02 | Current Google video tooling documents first/last frames, image ingredients, extension, and object insert/remove. | C | [Google Cloud, video generation overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/overview), “Key features,” updated 2026-08-07 | High as of research date | Compile keyframes and references when exact paths are unavailable. |
| C-03 | Seedance 2.0 on Runway accepts text, image, video, and audio references; video references may preserve motion or structure. | C | [Runway, *Creating with Seedance 2.0*](https://help.runwayml.com/hc/en-us/articles/50488490233363-Creating-with-Seedance-2-0), inputs and reference guidance | High as of research date | Prefer reference video for choreography transfer experiments. |
| C-04 | Official LTX tooling documents depth, pose, and Canny control adapters; the active LTX-2 repository currently identifies LTX-2.3 checkpoints. | C | [LTX trainer control modes](https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/training-modes.md); [LTX-2 repository](https://github.com/Lightricks/LTX-2) | Medium | Verify adapter/checkpoint compatibility before routing a job. |
| C-05 | Sora web/app ended on 2026-04-26; the API is scheduled to end on 2026-09-24. | C | [OpenAI, Sora discontinuation](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation) | High as of research date | Do not make Sora a future production target. |
| C-06 | OpenAI’s historical Sora guidance states that shorter clips follow instructions more reliably and that longer detailed prompts still may not be followed reliably. | C | [OpenAI, *Sora 2 Prompting Guide*](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide), “Video Length” and “Prompt anatomy” | High | Prompt detail cannot be equated with deterministic motion authority. |

---

# Part I — The control ceiling

## 1. What prompting can and cannot control

Prompting is strong at **semantic intent**:

- who wants what;
- what kind of action occurs;
- the visible style and emotional register;
- broad temporal order;
- approximate framing and camera movement;
- which event should feel dominant.

Prompting is weak as an exact numerical controller for:

- joint positions at every frame;
- grip location and duration;
- force and impulse exchange;
- 6-DoF root trajectories;
- exact camera extrinsics and focal changes;
- frame-exact exposure and cut timing;
- conservation of all consequences across a long stochastic generation.

This is not a wording defect. A text prompt describes a set of acceptable videos. It does not normally identify one unique trajectory within that set.

## 2. Control ladder

| Level | Control source | Reliable use | Main ceiling |
| --- | --- | --- | --- |
| **L0 — prose semantics** | Natural-language prompt | genre, intent, broad action, style, broad camera | high ambiguity; stochastic geometry and timing |
| **L1 — compiled state/timeline** | Fight IR → timed prompt blocks | causal beats, persistent consequences, provider-specific phrasing | provider may ignore or blur fine fields |
| **L2 — visual anchors** | reference images, ingredients, start/end frames, storyboard panels | identity, composition, endpoints, pose anchors | path between anchors remains underdetermined |
| **L3 — motion conditions** | reference video, pose sequence, trajectories, depth, edges, optical flow, camera poses | approximate path, timing, structure, camera/object separation | control adapters vary; contacts still may fail |
| **L4 — articulated constraints** | rig animation, IK, mocap, contact schedule, physics optimization | exact body paths, contact intervals, momentum, support | requires tools beyond ordinary prompting |
| **L5 — editorial realization** | compositing, retiming, cuts, VFX, paint fixes | frame-exact presentation, exposure, continuity repair | no longer a single raw generation |

**Operational conclusion:** exact, recognizable, Naruto-versus-Sasuke-level choreography is an L3–L5 problem. L0–L1 can produce a scene with the same dramatic meaning and broad motion family, but not reliably the same choreography.

## 3. Structured syntax does not raise the ceiling by itself

```text
same semantics + different delimiters ≠ new physical control channel
```

YAML, JSON, and XML matter when they enable:

- schema validation;
- inheritance and defaults;
- deterministic ordering;
- state-delta computation;
- provider capability negotiation;
- automatic prompt rendering;
- reference-signal attachment;
- output verification.

They do not become pose, contact, or camera signals merely because the text resembles code.

---

# Part II — Combat dramaturgy and persistent fight state

## 4. Definition

**Combat dramaturgy** is the causal organization of violent or competitive physical action so that each beat changes what the characters want, know, can do, feel, risk, and occupy.

**Persistent fight state** is the minimum sufficient record of those changes at time `t`, carried into every later decision until an explicit event changes it.

### Non-meaning and boundaries

Persistent state is not:

- a list of attacks;
- a prose recap with no typed fields;
- a single scalar saying who is “winning”;
- an omniscient state shared by both characters;
- a health bar that ignores mechanics and perception;
- a visual continuity note limited to wardrobe and identity.

It is a causal state used to constrain later action.

## 5. State factorization

Let the full scene state be:

\[
S_t = \{W_t, A^1_t, A^2_t, R_t, C_t, P_t\}
\]

where:

- `W_t`: world and geography state;
- `A^i_t`: private state of actor `i`;
- `R_t`: relationships between actors, props, and objectives;
- `C_t`: active contact topology;
- `P_t`: presentation/camera state.

An event updates state:

\[
S_{t+\Delta} = F(S_t, e_t, o_t)
\]

where `e_t` is what physically occurs and `o_t` is what each actor actually observes. The distinction matters: world truth and character belief may diverge.

## 6. Required actor fields

| Object | Required fields | Units or scale | Update trigger |
| --- | --- | --- | --- |
| Objective | goal, priority, success condition, failure condition, deadline | priority 0–1 or ordinal | new information, achieved/blocked condition |
| Tactic | current method, target vulnerability, commitment, alternatives | commitment 0–1 | observation, failure, interruption, opportunity |
| Intention | selected near-term plan and horizon | seconds or beats | commitment/replanning |
| Belief | proposition, confidence, evidence, acquired time, expiry | confidence 0–1 | perception or inference |
| Advantage | initiative, position, balance, reach, weapon, information, energy, tempo | each dimension 0–1 with evidence | physical or informational event |
| Emotion | valence, arousal, dominance, control, target | valence −1..1; others 0–1 | appraisal of event |
| Fatigue | global exertion, local capacity, breath, recovery rate | RPE 0–10 and/or normalized capacity | effort, impact, rest |
| Injury | body region, severity, pain, mobility/force effect, compensation | severity ordinal; pain 0–10; capacity 0–1 | impact, aggravation, recovery |
| Pose/support | root transform, support set, balance strategy, guarded regions | SI units or normalized | every sampled time step |
| Inventory | item, owner/controller, hand, state, accessibility | categorical | pickup, transfer, drop, break |

### 6.1 Affect, fatigue, and injury are control states

These states must change later action selection and execution. They are not adjectives appended after choreography is chosen.

#### Affect

Use an appraisal update:

```yaml
affect_update:
  trigger: expected interception fails and north lane opens
  appraisal:
    goal_congruence: -0.72
    controllability: 0.34
    certainty: 0.61
  prior: {valence: -0.20, arousal: 0.58, dominance: 0.56}
  posterior: {valence: -0.48, arousal: 0.76, dominance: 0.38}
  behavioral_effects:
    - attention narrows toward the exit lane
    - recovery becomes urgent but less mechanically clean
    - risk tolerance rises for one recovery attempt
```

Do not compile “anger = always faster” or “fear = always retreat.” Research supports kinematic cues to emotion at population level, not a deterministic universal mapping. Character, culture, task, injury, and tactical intent remain moderators.

Useful movement-facing affect fields are:

- movement initiation latency;
- preferred interpersonal distance;
- acceleration profile;
- amplitude and contraction/expansion of posture;
- gaze/attention allocation;
- willingness to accept unstable support;
- recovery patience versus urgency.

#### Fatigue

Factor fatigue into global exertion and local capacity:

```yaml
fatigue:
  global:
    rpe_0_10: 6.5
    breath_cycle_s: 1.25
    recovery_rate_per_s: 0.025
  local_capacity:
    left_leg: 0.46
    right_leg: 0.78
    right_shoulder: 0.63
  coordination_effects:
    - increased step-width variability
    - longer stabilization after hard redirection
    - greater trunk contribution when right shoulder is taxed
```

A simple compiler-state proposal is:

\[
f_{r,t+\Delta} = clamp(f_{r,t} + work_{r,t} + impact_{r,t} - recovery_{r,t}, 0, 1)
\]

where `f` is fatigue, not remaining capacity. The work, impact, and recovery terms must be calibrated; they are not inferred reliably from prose alone.

#### Injury

An injury object must specify mechanical consequences and compensations:

```yaml
injury:
  region: left_knee
  structural_status: unspecified
  pain_0_10: 5
  severity_0_4: 2
  effects:
    load_acceptance: 0.46
    flexion_tolerance: 0.58
    push_off_capacity: 0.52
  compensations:
    - favors right-leg support
    - shortens left stance interval
    - increases trunk lean during emergency recovery
  uncertainty:
    source: dramatic annotation, not clinical measurement
    confidence: 0.70
```

This is a performance model, not a medical diagnosis. A real injury should not be assigned precise capacity values without evidence. For fictional direction, the values maintain internal consistency and permit measurement.

#### Coupling rule

At each beat, derive candidate tactics from objective and belief, then filter them by geography, contact, fatigue, injury, and affect:

```text
candidate tactics
→ information-feasible
→ geographically feasible
→ contact/support feasible
→ fatigue/injury feasible
→ affect-modulated preference
→ committed intention
```

This prevents a character with a damaged support leg, lost grip, obscured view, and high arousal from executing the same clean neutral-stance option that would have been available at the start.

### Advantage is a vector

Do not write:

```yaml
advantage: fighter_a
```

Write:

```yaml
advantage:
  initiative: {fighter_a: 0.72, fighter_b: 0.28}
  balance: {fighter_a: 0.55, fighter_b: 0.38}
  position: {fighter_a: 0.44, fighter_b: 0.61}
  information: {fighter_a: 0.80, fighter_b: 0.35}
  energy: {fighter_a: 0.63, fighter_b: 0.47}
  evidence:
    - fighter_a forced fighter_b to turn away from the north exit
    - fighter_b still controls the inside lane near the wall
```

Two actors can hold different advantages simultaneously. Dramatic reversals come from transforming the vector, not flipping a winner bit.

## 7. Belief and knowledge state

Each actor needs a private ledger:

```yaml
beliefs:
  fighter_a:
    - proposition: fighter_b protects the injured left leg
      confidence: 0.78
      source: observed shortened step after landing
      acquired_at_s: 1.42
    - proposition: north exit is clear
      confidence: 0.40
      source: partial glance; pillar blocks full view
      acquired_at_s: 1.70
  fighter_b:
    - proposition: fighter_a intends another high strike
      confidence: 0.66
      source: repeated shoulder cue
      acquired_at_s: 1.55
      truth_status: false
```

The false belief is dramatically useful. It causes a plausible defensive choice without requiring irrationality.

## 8. Geography as an active participant

Represent geography through affordances, constraints, and visibility:

```yaml
geography:
  world_frame: W
  zones:
    - id: north_exit
      polygon_m: [[-0.6, 4.0], [0.8, 4.0], [0.8, 4.5], [-0.6, 4.5]]
      affordances: [escape, funnel]
    - id: east_wall
      plane: {normal: [-1, 0, 0], offset_m: 2.8}
      affordances: [brace, pin, rebound, occlude]
  obstacles:
    - id: pillar_1
      position_m: [0.4, 2.1, 0]
      radius_m: 0.35
      occludes: [north_exit_from_west]
  hazards:
    - id: wet_patch
      friction_class: low
      polygon_m: [[1.1, 1.5], [2.0, 1.5], [2.0, 2.2], [1.1, 2.2]]
```

The wall is not decoration if it changes balance, escape routes, visibility, or contact options. If the environment never constrains or enables a later beat, it is set dressing rather than fight geography.

## 9. Beat contract

Every beat must contain:

```yaml
beat:
  id: b03
  interval_s: [1.60, 2.35]
  dramatic_function: mistaken defense creates an exit lane
  preconditions:
    - fighter_b believes another high strike is likely
    - fighter_b loads the uninjured right leg
    - fighter_a is outside direct contact
  observations:
    fighter_a:
      - fighter_b guard rises early
    fighter_b:
      - fighter_a shoulder begins the familiar high-line cue
  intentions:
    fighter_a: draw the guard upward, enter the north lane
    fighter_b: intercept the expected high line
  motor_plan:
    - fighter_a begins lateral foot plant before the feint resolves
    - fighter_b raises forearm and shifts weight right
  contacts: [c17, c18]
  effects:
    world:
      - north lane opens for 0.42 s
    fighter_a:
      - information advantage increases
      - left foot becomes primary support
    fighter_b:
      - left-leg pain rises
      - belief in high-line attack is falsified
  postconditions:
    - fighter_a is inside fighter_b's reach
    - fighter_b cannot return to the previous stance without a recovery step
```

## 10. Persistence invariants

The compiler and evaluator should reject or flag:

1. **Uncaused advantage reversal** — a dimension changes materially without an event.
2. **Knowledge teleportation** — an actor acts on information not observed or inferred.
3. **Injury amnesia** — capacity returns without elapsed recovery or explicit stylization.
4. **Fatigue reset** — exertion returns to baseline between adjacent shots.
5. **Geography amnesia** — actors or props cross obstacles, exits, or walls without a path.
6. **Ownership reset** — weapons or props change hands without transfer/release.
7. **Pose reset** — the next action begins from a neutral stance incompatible with the previous endpoint.
8. **Emotion decal** — emotion is described but does not alter speed, hesitation, target selection, risk, posture, or recovery.

## 11. Why this closes the game-like gap

A game-like prompt repeatedly asks, “What impressive move happens next?”

A persistent-state prompt asks, “Given this exact imbalance, belief, contact, injury, and geography, what can this person attempt next?”

That question eliminates many disconnected continuations before generation begins.

---

# Part III — Coupled interaction and contact topology

## 12. Definition

**Contact topology** is the time-varying graph of physical contacts among body regions, objects, and the environment.

It records connectivity and contact mode. It does not claim exact force unless force is measured or simulated.

### Non-meaning and boundaries

Contact topology is not:

- “they grapple”;
- a point event called “hit”;
- two independent character descriptions that happen to mention each other;
- a permanent edge for the entire scene;
- a claim that visible overlap proves force transfer.

## 13. Contact graph

At time `t`, define:

\[
G_C(t) = (V, E_t)
\]

Nodes `V` are typed body regions, prop surfaces, and environment surfaces. Each edge in `E_t` has an interval and a mode.

### Recommended node granularity

- hands: palm, back, thumb web, fingers;
- forearm: radial/ulnar surface;
- upper arm, shoulder, chest, back, pelvis;
- thigh, knee, shin, heel, toe, sole;
- prop grip, blade/shaft/body, tip, guard;
- floor, wall, rail, pillar, vehicle, debris.

Use the lowest granularity that affects the constraint. “Hand” is sufficient for a brief parry; a grip transfer may require palm/finger and object-handle surfaces.

## 14. Contact modes

| Mode | Operational definition | Expected relative motion |
| --- | --- | --- |
| `impact` | short contact with rapid normal-velocity change | normal approach becomes separation or sustained contact |
| `stick` | contacting points remain approximately fixed relative to each other | tangential slip near zero |
| `grip` | maintained multi-surface stick contact with intentional retention | constrained relative pose within compliance |
| `slide` | contact maintained while tangential position changes | nonzero tangential relative velocity |
| `roll` | contact location migrates over surfaces with low local slip | surface points exchange while contact persists |
| `pivot` | contact anchors rotation around a point/line | constrained translation, allowed rotation |
| `support` | contact transmits load to environment or partner | body balance depends on edge |
| `press` | maintained normal force without full positional lock | normal gap remains closed |
| `hook_or_trap` | geometry blocks one or more escape directions | constrained subset of relative motion |
| `near` | proximity relationship without physical contact | no contact constraint; useful precondition only |

`release`, `break`, `acquire`, and `mode_change` are events, not persistent modes.

## 15. Contact interval object

```yaml
contact:
  id: c17
  interval_s: [1.94, 2.18]
  a:
    actor: fighter_a
    region: left_forearm_ulnar
  b:
    actor: fighter_b
    region: right_forearm_radial
  mode_sequence:
    - mode: impact
      interval_s: [1.94, 1.99]
    - mode: slide
      interval_s: [1.99, 2.11]
      tangent_direction_world: [0.22, 0.96, 0.0]
    - mode: pivot
      interval_s: [2.11, 2.18]
  intended_function: redirect fighter_b's guard while fighter_a passes outside
  maintained_by: forward pressure plus left-foot support
  release:
    cause: fighter_a clears the shoulder line
    event_time_s: 2.18
  confidence: 0.86
  evidence: manual reference-video annotation
```

One narrative “contact” may contain multiple mechanical modes. Split the interval whenever the constraint changes.

## 16. Constraint graph and force-transfer chain

A believable contact is connected to support:

```text
floor
↔ fighter A left foot
↔ fighter A pelvis/trunk
↔ fighter A forearm
↔ fighter B forearm
↔ fighter B trunk
↔ fighter B right foot
↔ floor
```

This is a **force-transfer chain**, not necessarily a claim of measured force magnitude. It identifies the body segments that must visibly organize around the interaction.

If the contacting hand moves but the trunk, support foot, and partner do not respond, the scene often reads as a pantomime or a visual effect rather than coupled motion.

## 17. Support changes

Support is a subset of contact topology:

```yaml
support_state:
  fighter_a:
    interval_s: [1.80, 2.22]
    contacts: [left_sole_floor]
    secondary_contacts: [right_toe_floor, left_forearm_fighter_b]
    balance_strategy: dynamic_single_support_with_partner_brace
  fighter_b:
    interval_s: [1.95, 2.30]
    contacts: [right_sole_floor]
    unloaded_or_protected: [left_leg]
```

For highly dynamic action, the center of mass may move outside a static support polygon. Therefore “COM inside support polygon” is only a quasi-static check. Dynamic balance should also consider momentum, upcoming contacts, and allowable steps.

## 18. Contact invariants

- Contact onset requires closing distance and compatible orientation.
- Maintained contact requires continuous endpoints; it cannot jump from wrist to shoulder without a slide, release, or reacquisition.
- A sticking grip should not visibly slip unless the mode changes.
- A sliding contact must remain nonpenetrating and approximately surface-tangent.
- A release must have a cause: voluntary disengagement, loss of normal force, geometry clearing, or contact break.
- The receiving body must respond through local deformation, joint motion, root motion, support adjustment, or explicit stylized override.
- A redirected limb retains momentum unless an impulse, muscular action, or support change redirects it.
- Contact identity survives a camera cut.

## 19. Contact failure taxonomy

| Failure | Observable symptom | Likely missing representation |
| --- | --- | --- |
| Contact flicker | hands touch for alternating single frames | interval and hysteresis |
| Grip teleport | hand jumps between body regions | continuous surface path |
| Phantom force | partner moves before/without contact | causal timing and impulse |
| Dead contact | limbs touch but bodies remain independent | force-transfer chain |
| Penetration | surfaces pass through each other | nonpenetration constraint |
| Unmotivated release | grip vanishes to enable next move | release event/cause |
| Support swap | weight-bearing foot changes without transfer | support subgraph |
| Bilateral authorship | both actors “win” the same constraint | coupled solver/priority |

---

# Part IV — Motion coarticulation and transition dynamics

## 20. Definition

**Coarticulation** is the influence of neighboring actions on the form and timing of the current action.

In fight direction, it means the body begins solving the next problem before the current action has fully ended.

### Non-meaning and boundaries

Coarticulation is not generic smoothing. A smooth blend can erase weight, contact, or intent. Coarticulation may be sharp, asymmetric, interrupted, or deliberately discontinuous.

## 21. Action phase object

Each action should expose phases rather than a single verb:

```yaml
action:
  id: a12
  actor: fighter_a
  semantic_action: high-line feint into outside pass
  phases:
    - {name: orient, interval_s: [1.55, 1.66]}
    - {name: anticipatory_adjustment, interval_s: [1.61, 1.75]}
    - {name: visible_feint, interval_s: [1.66, 1.91]}
    - {name: lateral_plant, interval_s: [1.78, 2.02]}
    - {name: forearm_redirect, interval_s: [1.94, 2.18]}
    - {name: pass_through, interval_s: [2.05, 2.42]}
    - {name: recovery_or_successor_prep, interval_s: [2.25, 2.60]}
```

The overlaps are the point. The lateral plant begins before the visible feint resolves; the pass begins while redirection contact persists.

## 22. Six transition mechanisms

### 22.1 Anticipatory postural adjustment

Before a voluntary limb action disturbs balance, the body can alter trunk, pelvis, support pressure, or muscle activity. In a prompt or animation plan, encode the visible consequence:

```text
Before the arm commits, the pelvis shifts over the left foot and the rear heel lightens, quietly preparing the lateral exit.
```

### 22.2 Counter-motion

Visible movement may be prepared by a smaller opposite motion: hip turns against the strike, shoulder closes before opening, or the center of mass lowers before rising.

Counter-motion must name:

- segment;
- direction;
- amplitude or qualitative scale;
- time relative to the primary action;
- intended effect.

### 22.3 Residual momentum

At a boundary, store root linear velocity, root angular velocity, and major limb momentum direction. The next action must accept, dissipate, or redirect them.

```yaml
boundary_state:
  at_s: 2.18
  root_velocity_world_mps: [0.72, 1.14, 0.03]
  yaw_rate_deg_s: 86
  left_arm_momentum_direction_world: [0.18, 0.97, -0.05]
  resolution: convert forward-left momentum into outside pass
```

### 22.4 Recovery-as-preparation

The return from one action should often become the wind-up, guard, support, or line for the next. Returning to a generic neutral pose is a special case, not a default.

### 22.5 Interruption

An interrupted action carries partial commitment:

```yaml
interruption:
  action_id: a12
  at_s: 1.88
  commitment_fraction: 0.58
  carried_state:
    - trunk already rotating clockwise
    - weight already leaving right foot
    - right hand unavailable for 0.12 s
  new_stimulus: opponent closes elbow line early
  response: shorten step and turn forearm contact into a frame
```

The interruption cannot pretend the body had not started the original action.

### 22.6 Phase-dependent successor selection

The available next actions depend on the current phase. A successor chosen at 20% commitment differs from one chosen at 90% commitment. The planner should filter successor actions by:

- support set;
- free limbs;
- active contacts;
- root velocity;
- orientation;
- injury capacity;
- visibility and belief.

## 23. Transition continuity

For ordinary continuous motion, check at boundary `t_b`:

\[
\|q(t_b^-) - q(t_b^+)\| \approx 0
\]

\[
\|\dot{q}(t_b^-) - \dot{q}(t_b^+)\| \text{ is small unless an impulse or stylized cut is declared}
\]

For dynamic action, exact joint-angle continuity is not enough. Also inspect:

- root velocity;
- center-of-mass trajectory;
- linear and angular momentum;
- support/contact state;
- facing and gaze;
- guarded/open regions;
- prop ownership.

## 24. Coarticulation metrics

Let action `i` end at `t_i^end` and successor preparation begin at `t_{i+1}^prep`.

\[
T_{overlap} = \max(0, t_i^{end} - t_{i+1}^{prep})
\]

\[
R_{overlap} = \frac{T_{overlap}}{t_i^{end}-t_i^{start}}
\]

These are descriptive measurements, not targets. Some beats require no overlap or a deliberate hold.

Additional metrics:

- root-velocity jump at transition;
- angular-velocity jump;
- joint jerk around boundary;
- unintended contact break count;
- neutral-reset rate;
- successor-preparation visibility;
- interruption response latency;
- momentum-resolution label accuracy: `carry`, `redirect`, `dissipate`, or `impulse_change`.

---

# Part V — Anime temporal composition

## 25. Definition

**Anime temporal composition** is the authored mapping from the scene's implied continuous action to displayed frames, unique drawings, layer motion, camera motion, effects, holds, and deliberate discontinuities.

It is not “low FPS.” A 24 fps file can expose one drawing for several frames, animate the background on ones, hold the character, insert a single smear, and then land on a long key pose.

## 26. Stage time and presentation time

This packet proposes two separate clocks:

- **Stage time `τ`**: the time in the implied world/action.
- **Presentation time `t`**: the time occupied by displayed frames.

A mapping `τ = φ(t)` relates them. It can:

- run near real time;
- compress action;
- expand an impact;
- hold a drawing while implied motion continues in other layers;
- freeze stage time for emphasis;
- replay or reorder time if explicitly declared.

### Hold types

| Hold type | Character drawing | Implied stage time | Other layers |
| --- | --- | --- | --- |
| `world_pause` | held or minimally changing | character truly pauses | environment may continue normally |
| `drawing_hold_with_implied_motion` | held | action continues symbolically | background, camera, lines, debris, or sound carry motion |
| `presentation_freeze` | held | stage time suspended | optional graphic/VFX motion only |
| `impact_hold` | key contact pose held | impact duration expanded | shake, flash, debris, sound may evolve |

Do not label all repeated frames “slow motion.”

## 27. Key-pose hierarchy

| Rank | Pose type | Function |
| --- | --- | --- |
| K0 | story/decision key | changes intention, belief, or dramatic direction |
| K1 | interaction/contact key | establishes impact, grip, redirect, or release topology |
| K2 | support/weight key | makes balance and force chain readable |
| K3 | directional/extreme key | defines silhouette, trajectory, and line of action |
| K4 | breakdown/transition key | specifies how one extreme becomes another |
| K5 | smear/accent key | depicts fast path or perceptual emphasis |
| K6 | corrective in-between | repairs volume, arc, contact, or spacing |

Exposure allocation should follow hierarchy. A K0/K1 pose may receive more screen time than several mechanically intermediate poses combined.

## 28. Exposure sheet representation

At 24 output frames per second:

| Frames | Fighter A | Fighter B | Contact | Background | Camera/FX | Stage-time function |
| --- | --- | --- | --- | --- | --- | --- |
| 1–3 | decision key held | wary guard micro-shift | none | slow lateral drift | static camera | expanded anticipation |
| 4–6 | feint breakdown on twos | guard begins rising | near only | drift accelerates | 1 px equivalent counter-pan | near real time |
| 7 | smear/accent | defensive extreme | first impact | speed-line burst | brief shake onset | compressed motion |
| 8–10 | forearm redirect key held | torso absorbs turn | slide contact | rapid opposing pan | shake decays | impact expansion |
| 11–14 | pass-through on twos | recovery step begins | pivot → release | parallax layers move on ones | track A | near real time |
| 15–20 | exit-lane story key held | failed interception held | none | debris continues | slow dolly out | dramatic hold |
| 21–24 | successor-prep drawing | breath/injury cue | none | settles | cut motivation builds | resumes stage time |

This table directs different layers independently. “Animate on twos” is a layer-local decision, not a global clip setting.

## 29. Exposure density

For layer `l` in window `w`:

\[
D_l(w) = \frac{N_{new\ drawing\ onsets,l}(w)}{duration(w)}
\]

Unit: unique drawing onsets per second.

Also record:

- mean and maximum hold length in frames;
- distribution of exposure steps (1, 2, 3, 4+);
- high-velocity frames assigned to smear or motion-line treatment;
- which layers move while the principal character drawing is held;
- key-pose dwell by hierarchy rank.

Exposure density is not quality. It is an allocation profile. Elite action often alternates low-density readability with concentrated high-density transition or effect motion.

## 30. Smears and deliberate discontinuity

A smear is not a malformed frame. It is a path-aware representation of motion over an interval. Store:

```yaml
smear:
  interval_frames: [7, 7]
  source_pose: a_feint_extreme
  destination_pose: a_redirect_contact
  trajectory_space: image
  principal_path: left_forearm
  style: elongated_single_form
  preserve:
    - head identity anchor
    - contact destination
  may_violate:
    - ordinary limb volume
    - instantaneous anatomy
```

Deliberate discontinuity must declare what is broken and what is preserved:

```yaml
discontinuity:
  type: pose_snap
  motivation: make defensive realization legible
  break: intermediate arm trajectory
  preserve: [screen_direction, support_foot, gaze_target, contact_destination]
```

Without that contract, generation errors and authored anime timing are indistinguishable.

## 31. Anime timing failure taxonomy

| Failure | Symptom | Missing control |
| --- | --- | --- |
| Uniform-fluid washout | every motion receives equal interpolation | exposure hierarchy |
| Random stutter | repeated frames lack semantic placement | X-sheet intent |
| Impact mush | contact receives no accent/hold | K1 exposure allocation |
| Smear hallucination | distorted anatomy appears away from fast transition | trajectory-bound smear interval |
| Dead hold | character freezes and nothing carries time | layer-specific motion plan |
| Camera substitution | camera shake replaces body/contact change | separate camera and body states |
| Unreadable density | too many unique poses around decision/contact | key-pose hierarchy |

---

# Part VI — Volumetric action cinematography

## 32. Definition

**Volumetric action cinematography** directs moving bodies and a moving camera inside a persistent 3D scene while controlling depth, parallax, occlusion, projected motion, screen direction, and cuts.

### Non-meaning and boundaries

It is not a list of camera terms. “Dolly left, 35 mm, dynamic” is insufficient unless the camera path is related to actor paths, depth layers, visibility, and the current dramatic beat.

## 33. Coordinate frames

Use four distinct spaces:

| Frame | Symbol | Purpose |
| --- | --- | --- |
| World | `W` | persistent geography and actor positions |
| Actor-local | `B_i` | pose and facing relative to actor root |
| Camera | `C` | depth and velocity relative to camera |
| Image/screen | `I` | composition, screen direction, occlusion, optical flow |

Perspective projection is conceptually:

\[
x_I \sim K [R_{CW} | t_{CW}] X_W
\]

where `K` contains camera intrinsics and `[R|t]` transforms world points into camera coordinates.

This separation prevents a common mistake: using camera motion to imply actor speed while the actors themselves lack coherent world-space motion.

## 34. Depth staging

For every beat, define:

- actor and prop depth order;
- foreground occluders;
- traversable depth lanes;
- intended crossing of near/mid/far planes;
- minimum readable separation;
- which spatial relationship the audience must understand.

```yaml
depth_staging:
  near: [pillar_edge]
  mid: [fighter_a, fighter_b]
  far: [north_exit]
  required_relation: fighter_a passes between fighter_b and north_exit
  depth_crossing:
    actor: fighter_a
    from_m: 5.2
    to_m: 3.8
    interval_s: [1.80, 2.45]
```

## 35. Parallax and lens-relative velocity

World speed and screen speed are different. Approximate image motion depends on:

- actor velocity;
- camera translation and rotation;
- depth;
- focal length/FOV;
- target tracking;
- shutter/exposure.

When the camera tracks the actor, subject screen velocity may be small while foreground and background optical flow communicate speed. This is **camera/body counter-motion**.

Store both:

```yaml
motion:
  actor_root_velocity_world_mps: [0.8, 1.2, 0.0]
  camera_velocity_world_mps: [0.3, 0.9, 0.1]
  subject_centroid_velocity_image_px_s: [42, -8]
  background_median_flow_px_s: [-118, 15]
```

The image-space values may be measured after rendering rather than authored.

## 36. Occlusion graph

At time `t`, represent visibility as a directed graph:

```yaml
occlusion:
  - interval_s: [1.72, 1.91]
    occluder: pillar_edge
    occluded: fighter_a_left_foot
    allowed: true
    reason: preserves surprise while torso and trajectory remain readable
  - interval_s: [2.00, 2.18]
    occluder: fighter_a_torso
    occluded: contact_c17
    allowed: false
    reason: contact mode change must remain visible
```

Occlusion can create energy and surprise, but hiding the exact event that explains a state change creates incoherence unless sound, reaction, or a subsequent reveal supplies the missing causal evidence.

## 37. Axis management

Define the current line of action in world space and the camera's side:

```yaml
axis:
  id: axis_a_b
  endpoints: [fighter_a_root, fighter_b_root]
  camera_side: positive
  screen_direction:
    fighter_a_forward: right
    fighter_b_forward: left
```

Crossing the axis is allowed when:

- the camera visibly moves across it;
- a neutral/axis shot bridges the crossing;
- geography has already reoriented the action;
- deliberate disorientation is the dramatic goal.

An unmarked crossing is a continuity defect; a motivated crossing is a directorial choice.

## 38. Motivated cuts

A cut should respond to a change in narrative, perception, contact, or spatial need.

```yaml
cut:
  at_s: 2.20
  motivation: reveal the opened north lane and fighter_b's failed recovery
  type: spatial_clarification
  outgoing_payload:
    active_contact: c17_released
    fighter_a_phase: pass_through
    fighter_b_support: right_foot
    screen_direction_a: right
  incoming_requirements:
    - fighter_a continues rightward
    - fighter_b remains behind and left of fighter_a
    - north exit is newly visible
    - injury compensation persists
```

Useful motivations include:

- impact/accent;
- reaction or discovery;
- contact clarification;
- conceal/reveal;
- change of objective or tactic;
- geography clarification;
- temporal compression;
- point of view.

## 39. Camera object

```yaml
camera:
  shot_id: s03
  interval_s: [1.50, 2.20]
  intrinsics:
    focal_length_mm: 35
    sensor_width_mm: 36
    focus_distance_m: 4.2
    aperture_t: 4.0
    shutter_angle_deg: 144
  extrinsics_keyframes:
    - time_s: 1.50
      position_world_m: [-3.2, 0.8, 1.55]
      look_at: interaction_centroid
    - time_s: 2.20
      position_world_m: [-2.7, 1.5, 1.48]
      look_at: fighter_a_torso
  movement:
    type: lateral_track_with_slight_counter_dolly
    motivation: keep forearm redirection readable while background parallax carries speed
  visibility_requirements:
    - contact c17 visible from 1.94 to 2.11 s
    - north exit may remain hidden until the cut
```

If a provider accepts only prose, these fields are compiled into a compact shot description. If it accepts camera trajectories, they become conditions rather than adjectives.

---

# Part VII — Integrated canonical representation

## 40. Canonical object model

```text
Project
├── semantics
│   ├── dramatic objective
│   ├── actor private states
│   └── world/geography
├── stage timeline
│   ├── beats
│   ├── actions and overlapping phases
│   ├── contact intervals
│   └── state deltas
├── presentation timeline
│   ├── exposure tracks
│   ├── key-pose hierarchy
│   ├── camera shots/cuts
│   └── FX/audio cues
├── control assets
│   ├── reference video/images
│   ├── pose/depth/edge/flow
│   └── camera reconstruction
└── verification
    ├── hard invariants
    ├── metrics
    └── human review
```

## 41. JSON Schema sketch

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/fight-ir.schema.json",
  "title": "FightIR",
  "type": "object",
  "required": [
    "version",
    "timebase",
    "coordinate_frames",
    "actors",
    "geography",
    "beats",
    "contacts",
    "presentation",
    "verification"
  ],
  "properties": {
    "version": {"const": "1.0"},
    "timebase": {
      "type": "object",
      "required": ["seconds", "output_fps"],
      "properties": {
        "seconds": {"type": "number", "exclusiveMinimum": 0},
        "output_fps": {"type": "number", "exclusiveMinimum": 0}
      }
    },
    "coordinate_frames": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "kind", "units", "handedness", "up_axis"]
      }
    },
    "actors": {
      "type": "array",
      "minItems": 2,
      "items": {"$ref": "#/$defs/actor"}
    },
    "beats": {
      "type": "array",
      "items": {"$ref": "#/$defs/beat"}
    },
    "contacts": {
      "type": "array",
      "items": {"$ref": "#/$defs/contact"}
    },
    "presentation": {"$ref": "#/$defs/presentation"},
    "verification": {"$ref": "#/$defs/verification"}
  },
  "$defs": {
    "interval": {
      "type": "array",
      "prefixItems": [
        {"type": "number", "minimum": 0},
        {"type": "number", "minimum": 0}
      ],
      "minItems": 2,
      "maxItems": 2
    },
    "actor": {
      "type": "object",
      "required": ["id", "objective", "tactic", "beliefs", "fatigue", "injuries"],
      "properties": {
        "id": {"type": "string"},
        "objective": {"type": "object"},
        "tactic": {"type": "object"},
        "beliefs": {"type": "array"},
        "fatigue": {"type": "object"},
        "injuries": {"type": "array"}
      }
    },
    "beat": {
      "type": "object",
      "required": [
        "id",
        "interval_s",
        "preconditions",
        "intentions",
        "actions",
        "effects",
        "postconditions"
      ],
      "properties": {
        "id": {"type": "string"},
        "interval_s": {"$ref": "#/$defs/interval"},
        "preconditions": {"type": "array"},
        "intentions": {"type": "object"},
        "actions": {"type": "array"},
        "effects": {"type": "object"},
        "postconditions": {"type": "array"}
      }
    },
    "contact": {
      "type": "object",
      "required": ["id", "interval_s", "a", "b", "mode_sequence", "release"],
      "properties": {
        "id": {"type": "string"},
        "interval_s": {"$ref": "#/$defs/interval"},
        "a": {"type": "object"},
        "b": {"type": "object"},
        "mode_sequence": {"type": "array", "minItems": 1},
        "release": {"type": "object"}
      }
    },
    "presentation": {
      "type": "object",
      "required": ["shots", "exposure_tracks"],
      "properties": {
        "shots": {"type": "array"},
        "exposure_tracks": {"type": "array"}
      }
    },
    "verification": {
      "type": "object",
      "required": ["hard_gates", "metrics"],
      "properties": {
        "hard_gates": {"type": "array"},
        "metrics": {"type": "array"}
      }
    }
  }
}
```

Production schema additions should enforce `interval[1] > interval[0]`, unique IDs, valid references, interval containment, mode-sequence coverage, and monotonic state versions. JSON Schema alone cannot express all graph and temporal invariants; a semantic validator is required.

## 42. Canonical JSON example

```json
{
  "version": "1.0",
  "timebase": {"seconds": 3.0, "output_fps": 24},
  "coordinate_frames": [
    {"id": "W", "kind": "world", "units": "m", "handedness": "right", "up_axis": "+Z"},
    {"id": "C_s01", "kind": "camera", "units": "m", "handedness": "right", "up_axis": "+Y"}
  ],
  "actors": [
    {
      "id": "fighter_a",
      "objective": {
        "goal": "reach north_exit",
        "priority": 0.95,
        "success_condition": "root enters north_exit polygon"
      },
      "tactic": {
        "current": "induce early high guard then pass outside",
        "commitment": 0.72
      },
      "beliefs": [
        {
          "proposition": "fighter_b protects left leg",
          "confidence": 0.78,
          "acquired_at_s": 1.42
        }
      ],
      "fatigue": {"rpe_0_10": 5.0, "local_capacity": {"left_shoulder": 0.82}},
      "injuries": []
    },
    {
      "id": "fighter_b",
      "objective": {
        "goal": "deny north_exit for three seconds",
        "priority": 0.90,
        "success_condition": "fighter_a remains south of exit at 3.0 s"
      },
      "tactic": {"current": "intercept high line", "commitment": 0.66},
      "beliefs": [
        {
          "proposition": "fighter_a will repeat high strike",
          "confidence": 0.66,
          "truth_status": false
        }
      ],
      "fatigue": {"rpe_0_10": 6.5, "local_capacity": {"left_leg": 0.46}},
      "injuries": [
        {
          "region": "left_knee",
          "severity_0_4": 2,
          "pain_0_10": 5,
          "mechanical_effect": "reduced load acceptance"
        }
      ]
    }
  ],
  "geography": {
    "world_frame": "W",
    "zones": [{"id": "north_exit", "affordances": ["escape", "funnel"]}],
    "obstacles": [{"id": "pillar_1", "affordances": ["occlude", "brace"]}]
  },
  "beats": [
    {
      "id": "b03",
      "interval_s": [1.6, 2.42],
      "preconditions": [
        "fighter_b believes a high strike is likely",
        "fighter_b protects left leg"
      ],
      "intentions": {
        "fighter_a": "open and enter north lane",
        "fighter_b": "intercept expected high line"
      },
      "actions": ["a12"],
      "contacts": ["c17"],
      "effects": {
        "fighter_a": ["information advantage rises", "enters outside lane"],
        "fighter_b": ["belief falsified", "left-leg pain rises"],
        "world": ["north lane opens for 0.42 s"]
      },
      "postconditions": [
        "fighter_a is inside fighter_b reach",
        "fighter_b requires recovery step"
      ]
    }
  ],
  "contacts": [
    {
      "id": "c17",
      "interval_s": [1.94, 2.18],
      "a": {"actor": "fighter_a", "region": "left_forearm_ulnar"},
      "b": {"actor": "fighter_b", "region": "right_forearm_radial"},
      "mode_sequence": [
        {"mode": "impact", "interval_s": [1.94, 1.99]},
        {"mode": "slide", "interval_s": [1.99, 2.11]},
        {"mode": "pivot", "interval_s": [2.11, 2.18]}
      ],
      "release": {"event_time_s": 2.18, "cause": "fighter_a clears shoulder line"}
    }
  ],
  "presentation": {
    "shots": [
      {
        "id": "s01",
        "interval_s": [1.5, 2.2],
        "focal_length_mm": 35,
        "movement": "lateral track with slight counter-dolly",
        "must_show": ["c17 from 1.94 through 2.11 s"]
      }
    ],
    "exposure_tracks": [
      {
        "layer": "fighter_a",
        "runs": [
          {"frames": [1, 3], "drawing": "decision_key"},
          {"frames": [4, 6], "drawing_sequence": ["f1", "f2"], "step": 2},
          {"frames": [7, 7], "drawing": "smear_1"},
          {"frames": [8, 10], "drawing": "redirect_contact_key"}
        ]
      }
    ]
  },
  "verification": {
    "hard_gates": [
      "no identity swap",
      "c17 endpoints remain continuous",
      "fighter_b injury persists",
      "north_exit geography remains stable"
    ],
    "metrics": [
      "contact_interval_iou",
      "root_velocity_jump",
      "exposure_density_by_layer",
      "axis_crossing_count",
      "background_optical_flow"
    ]
  }
}
```

## 43. YAML authoring form

```yaml
fight_ir: 1.0
timebase: {seconds: 3.0, output_fps: 24}

dramatic_question: can fighter_a reach the north exit before fighter_b recovers?

state:
  fighter_a:
    objective: reach north_exit
    tactic: induce early high guard, then pass outside
    knows:
      - fighter_b protects left leg
    fatigue_rpe: 5.0
  fighter_b:
    objective: deny north_exit for three seconds
    tactic: intercept expected high line
    falsely_believes:
      - fighter_a will repeat high strike
    injury:
      region: left_knee
      effect: reduced load acceptance

beat:
  interval_s: [1.60, 2.42]
  preparation_overlap:
    - fighter_a shifts pelvis over left foot before feint resolves
  contact:
    endpoints: [fighter_a.left_forearm, fighter_b.right_forearm]
    modes:
      - {mode: impact, interval_s: [1.94, 1.99]}
      - {mode: slide, interval_s: [1.99, 2.11]}
      - {mode: pivot, interval_s: [2.11, 2.18]}
    release: fighter_a clears shoulder line
  consequence:
    - north lane opens
    - fighter_b must recovery-step on painful left side

presentation:
  character_exposure: variable
  contact_key_hold_frames: 3
  smear_frames: [7]
  background: moves on ones during contact hold
  camera: lateral track; contact remains visible
```

## 44. XML interchange form

```xml
<fightIR version="1.0" durationSeconds="3.0" outputFps="24">
  <actor id="fighter_a">
    <objective target="north_exit" priority="0.95" />
    <tactic commitment="0.72">induce early high guard then pass outside</tactic>
  </actor>
  <actor id="fighter_b">
    <objective target="deny_north_exit" priority="0.90" />
    <injury region="left_knee" severity="2" pain="5">
      reduced load acceptance
    </injury>
  </actor>
  <beat id="b03" start="1.60" end="2.42">
    <precondition>fighter_b expects a repeated high strike</precondition>
    <action ref="a12" />
    <contact ref="c17" />
    <effect subject="fighter_b">belief falsified</effect>
    <effect subject="world">north lane opens for 0.42 seconds</effect>
  </beat>
  <contact id="c17" start="1.94" end="2.18">
    <endpoint actor="fighter_a" region="left_forearm_ulnar" />
    <endpoint actor="fighter_b" region="right_forearm_radial" />
    <mode type="impact" start="1.94" end="1.99" />
    <mode type="slide" start="1.99" end="2.11" />
    <mode type="pivot" start="2.11" end="2.18" />
    <release at="2.18">fighter_a clears shoulder line</release>
  </contact>
</fightIR>
```

## 45. Natural-language render

```text
Fighter A is not trying to win an exchange; A is trying to reach the north exit before Fighter B can reset. B is delaying A while protecting a painful left knee and wrongly expects A to repeat the same high-line attack.

As A begins the familiar high shoulder cue, A is already shifting the pelvis over the left foot and lightening the rear heel for an outside pass. B reacts to the belief rather than the truth: the guard rises early and weight loads onto the healthier right leg. Before the feint has fully resolved, A's left forearm meets B's right forearm. The contact does not bounce away. It impacts, slides along the guard, then becomes a short pivot while A's body passes outside. The release happens only after A clears B's shoulder line.

B's torso and support foot turn under that maintained pressure. The painful left leg accepts weight late and forces a recovery step, so B cannot return to the previous stance. The north lane opens as a consequence of the mistaken defense.

Present the initial decision pose for three frames, the feint on twos, one trajectory-aligned smear into contact, and a three-frame contact key while the background moves rapidly on ones. Track laterally so the forearm contact stays visible; reveal the north exit only on the motivated cut after release.
```

---

# Part VIII — Compiler and provider routing

## 46. Compiler

```text
research evidence
→ semantic decision
→ persistent Fight IR
→ state-delta validation
→ contact/phase solve
→ exposure and camera plan
→ capability negotiation
→ provider carrier package
→ generation
→ measurement
→ repair or acceptance
```

## 47. Compilation order

1. Resolve the dramatic objective and opposing objectives.
2. Build initial private actor states and world geography.
3. Author beats with preconditions and state effects.
4. Convert actions into overlapping phases.
5. Add contact intervals and support changes.
6. Validate state persistence and mechanical reachability.
7. Map stage time to presentation time and exposure tracks.
8. Design shots from world-space requirements.
9. Query provider capabilities.
10. Attach the highest-authority available controls.
11. Render concise provider-facing instructions.
12. Generate multiple seeds.
13. Measure hard gates before aesthetic scoring.
14. Repair the earliest failed layer, not the visible symptom alone.

## 48. Capability negotiation

| Desired control | Preferred carrier | Fallback | Do not pretend |
| --- | --- | --- | --- |
| exact actor identity | character/reference asset | reference image + repeated description | text name alone guarantees identity |
| exact start/end pose | pose/keyframe images | concise pose description | adjective equals joint configuration |
| choreography path | reference video or pose trajectory | timed beat prompt | move names specify paths |
| contact timing | contact-aware rig/pose sequence | interval language + visible contact keyframe | “hits” specifies contact duration |
| camera trajectory | camera poses/extrinsics/flow | camera prose and reference video | “dolly” defines exact path |
| anime exposure | frame-level edit/X-sheet | prompt holds and accents | output FPS equals drawing exposure |
| physics/contact | simulation/optimization | contact graph + post verification | prose enforces friction or momentum |

## 49. Current carrier notes

### Runway Gen-4.5

Current documentation advertises complex sequenced instructions and precise event timing, but the exposed base inputs are text or text-plus-image. Use it for L0–L2 compilation and measure adherence. Do not infer exposed pose/contact trajectories from marketing language.

### Google Veo / Gemini video tooling

Current documentation exposes first frame, first/last frames, ingredients, extension, and object edits. This is suitable for L2 endpoints and continuity anchors. Exact intermediate contact remains underdetermined unless another control path is available.

### Seedance 2.0 through Runway

Current documentation accepts reference video and states that motion or structure can be preserved while style or characters change. This makes it a strong candidate for L3 choreography-transfer experiments. “Can preserve” is not a deterministic guarantee; test identity, contact, and camera retention separately.

### LTX

The official LTX-2 repository currently identifies LTX-2.3 checkpoints. Separate official LTX training documentation exposes pose, depth, and Canny IC-LoRA controls. Because repositories and checkpoint families change, the adapter must verify the exact model/workflow compatibility at runtime rather than assume every historical control adapter loads into LTX-2.3.

### Sora

Sora's former prompt and API guidance remains useful evidence about prompt reliability and clip length, but Sora is not a future production target: the product is discontinued and the API has a declared sunset.

### Unverified providers

This packet does not make capability claims for Kling, Hailuo, Luma, or other providers without current primary documentation. Their adapters should begin as `unknown`, then be upgraded only through official capability evidence and a passing fixture.

---

# Part IX — Measurement

## 50. Hard gates before scores

A visually beautiful clip fails if any critical invariant fails. Use ordered gates:

1. identity and body-count integrity;
2. geography and ownership integrity;
3. critical contact topology;
4. persistent state consequences;
5. action order and phase continuity;
6. camera visibility and axis intent;
7. anime timing intent;
8. aesthetic quality.

Do not average a contact failure away with high lighting or style scores.

## 51. Metric table

| Metric | Definition | Input | Formula/algorithm | Unit | Proposed tolerance / use | Failure state |
| --- | --- | --- | --- | --- | --- | --- |
| State persistence recall | expected state facts visible or causally respected later | IR + annotated output | respected facts / expected facts | ratio | report per state class | injury, belief, ownership, or geography vanishes |
| Uncaused state-change rate | changed facts with no observed cause | state deltas | unexplained changes / all changes | ratio | target 0 for hard facts | advantage or injury flips without event |
| Beat causal completeness | beats with precondition → action → effect visible | beat annotations | complete beats / total beats | ratio | critical beats must pass | move occurs without setup or consequence |
| Affect-to-action coupling | declared affect changes with at least one visible or tactical consequence | affect deltas + action annotation | coupled affect changes / material affect changes | ratio | report by character; avoid stereotype scoring | emotion appears only in label or face |
| Fatigue propagation | taxed regions alter later capacity, variability, timing, or tactic | effort events + later motion | expected fatigue effects respected / expected effects | ratio | state-specific | exertion never changes later action |
| Injury compensation consistency | declared mechanical effects and compensations persist | injury model + pose/support | passing affected beats / affected beats | ratio | critical injury effects must pass | injured region performs at baseline without cause |
| Contact onset error | predicted vs reference onset | frame labels | `|f_pred - f_ref|` | frames/ms | initial calibration: ±2 frames at 24 fps | early/late phantom contact |
| Contact interval IoU | temporal overlap of contact intervals | predicted/reference intervals | intersection / union | ratio | calibrate by contact type | contact flicker or truncated hold |
| Contact endpoint accuracy | correct body/surface pair | endpoint labels | exact or hierarchy-aware match | ratio | critical contacts exact | wrong hand/region/object |
| Contact topology edit distance | graph changes needed to match reference | per-frame/interval graphs | normalized graph edit distance | ratio | lower is better | missing/extra contacts |
| Slip error in stick/grip | relative tangential drift during declared stick | tracked contact points | path length / character height | normalized distance | near zero; noise-calibrated | grip visibly slides |
| Penetration rate | frames exceeding body-surface overlap tolerance | masks/meshes/depth | failing frames / contact frames | ratio | target near zero | bodies pass through each other |
| Support-contact accuracy | correct load-bearing contact set | pose/contact annotation | F1 or interval IoU | ratio | phase-dependent | floating or impossible weight transfer |
| Neutral-reset rate | transitions returning to generic stance without cause | pose/state labels | resets / transitions | ratio | target 0 unless authored | game-like move cards |
| Root velocity jump | discontinuity at action boundary | root trajectory | `||v^- - v^+||` | m/s or height/s | compare to declared impulse/cut | abrupt stop/start |
| Angular velocity jump | rotational discontinuity | root/joint trajectory | `||ω^- - ω^+||` | deg/s | compare to contact impulse | spin vanishes or appears |
| Coarticulation overlap | successor prep before predecessor end | phase intervals | `max(0, end_i-prep_{i+1})` | s, ratio | descriptive | every action waits for full reset |
| Interruption carryover | committed state preserved after interruption | phase + pose | checklist/trajectory comparison | ratio | critical carried facts must pass | aborted action erases momentum/pose |
| Exposure density | new drawings per displayed second per layer | X-sheet/output | drawing onsets / seconds | drawings/s | compare to plan | uniform-fluid or random stutter |
| Key-pose dwell error | actual vs planned exposure | X-sheet/output | absolute frame difference | frames | critical K0/K1 exact in edited workflow | impact/decision underexposed |
| Smear placement precision | smears occur only at declared fast transitions | frame labels | TP / predicted smears | ratio | target high | random anatomy distortion |
| Stage/presentation warp error | output event-time mapping vs plan | event timestamps | deviation from `φ(t)` | frames/s | event-specific | hold or acceleration mistimed |
| Subject off-screen rate | required subject/region absent | detection/masks | absent frames / required frames | ratio | 0 for must-show intervals | contact hidden |
| Occlusion contract accuracy | allowed/forbidden occlusions respected | occlusion graph | passing intervals / total | ratio | critical intervals must pass | causal action concealed |
| Axis crossing count | camera changes side of action axis | camera/scene reconstruction | sign changes | count | each crossing classified | unintended screen reversal |
| Screen-direction continuity | actor projected direction across shots | tracks | sign agreement or declared reversal | ratio | critical continuation exact | spatial confusion |
| Parallax rank consistency | near layers move more than far layers under lateral camera motion | optical flow + depth rank | rank correlation | Spearman ρ | compare to intended shot | flat/cardboard depth |
| Camera/object separation | actor motion is not replaced by camera motion | root track + optical flow | compare world and image motion components | diagnostic | no universal threshold | camera performs the action |
| Cut motivation coverage | cuts with declared dramatic/spatial reason | cut annotations | motivated cuts / all cuts | ratio | target 1 in authored sequence | decorative/random cuts |

### Tolerance warning

The tolerances above are starting calibration proposals, not universal standards. Pose extraction, stylization, occlusion, and smear frames introduce annotation noise. Estimate inter-annotator agreement and measurement uncertainty before setting release gates.

## 52. Recommended evaluation protocol

### Corpus

Use licensed or self-created reference clips in three bands:

- 2–4 second single-contact exchange;
- 4–8 second maintained-contact and redirection sequence;
- 6–12 second multi-shot anime-style action with deliberate holds and discontinuities.

### Ground truth

For each clip annotate:

- actor/object identity;
- root and key-joint trajectories where recoverable;
- active support contacts;
- body/body, body/object, and body/environment contact intervals;
- contact mode transitions;
- beat preconditions/effects;
- actor private beliefs and objectives where the story establishes them;
- X-sheet/exposure approximation by layer;
- camera intrinsics/extrinsics or best available reconstruction;
- cuts, axis side, screen direction, occlusion, and optical flow.

### Ablation conditions

| Condition | Controls |
| --- | --- |
| A | ordinary sequential natural-language move prompt |
| B | A + persistent objectives, beliefs, injury, fatigue, geography, and state effects |
| C | B + contact graph and support changes |
| D | C + overlapping action phases and momentum boundary state |
| E | D + exposure sheet and volumetric camera plan |
| F | E + reference video/pose/depth/flow/camera controls supported by provider |

Use the same semantic scene, provider settings, duration, aspect ratio, and a recorded set of random seeds. Twelve or more seeds per condition is a practical initial reliability sample, but it is not a substitute for a statistical power analysis.

### Report

Report:

- per-seed hard-gate pass/fail;
- pass-rate confidence intervals;
- metric distributions, not only means;
- failure taxonomy counts;
- human pairwise preference for causal coherence, contact realism, temporal design, spatial clarity, and aesthetics;
- provider version/date and every input asset.

### Stopping rule

Stop adding prompt detail when:

- the same failure persists across wording variants;
- the missing variable belongs to a higher control level;
- added detail reduces adherence elsewhere;
- the provider lacks a carrier for the required signal.

Escalate from prose to reference, pose, contact, camera, or editorial control.

---

# Part X — Failure-directed repair

## 53. Repair the earliest broken layer

| Visible defect | Earliest likely layer | Repair |
| --- | --- | --- |
| disconnected move cards | persistent state / beat causality | add preconditions, state deltas, successor filtering |
| hands pass through | contact topology | add endpoints, interval, mode, visibility; use structural control |
| actors take turns unnaturally | coupled phase planning | overlap perception, preparation, and response |
| motion is smooth but weightless | momentum/support | carry root velocity, support set, contact impulse consequence |
| anime looks like low-FPS live action | presentation timeline | author X-sheet, layer-specific exposure, key hierarchy |
| scene feels flat | world/camera separation | add depth lanes, parallax, occlusion, camera counter-motion |
| cut causes orientation confusion | axis/payload | preserve direction or declare motivated crossing |
| prompt is huge and adherence falls | compiler/carrier | emit only provider-relevant fields; attach stronger controls |

## 54. Minimal compiler rule set

```text
RULE 1: No beat without a precondition and effect.
RULE 2: No actor action may use knowledge absent from that actor's belief ledger.
RULE 3: No active contact may disappear without a release event.
RULE 4: No action boundary may discard support, root velocity, orientation, injury, ownership, or active contact.
RULE 5: Successor preparation may overlap the predecessor; neutral reset requires justification.
RULE 6: Output FPS and drawing exposure are separate fields.
RULE 7: Camera, actor, and image motion are separate trajectories.
RULE 8: Every cut transfers a continuity payload.
RULE 9: Structured syntax is never treated as a control capability unless the provider exposes it.
RULE 10: A failed hard invariant blocks aesthetic acceptance.
```

---

# Part XI — Research priorities after this packet

## 55. Immediate implementation sequence

1. Add `FightState`, `Beat`, `ActionPhase`, `ContactInterval`, `ExposureTrack`, `CameraShot`, and `CutPayload` to the canonical IR.
2. Implement semantic validation for IDs, intervals, persistence, contact release, and state deltas.
3. Build a measured-video adapter that produces candidate pose, contact, optical-flow, and camera annotations with confidence.
4. Build a provider capability registry that distinguishes prompt, image, keyframe, reference-video, pose, depth, edge, flow, and camera controls.
5. Compile provider prompts from the validated IR rather than authoring provider prompts as the source of truth.
6. Run the ablation protocol on a small sealed reference corpus.
7. Calibrate tolerances against expert ratings.

## 56. Do not prioritize yet

- additional FACS coverage;
- larger martial-arts move-name dictionaries;
- untested YAML-versus-XML-versus-JSON prompt folklore;
- global “cinematic” adjectives;
- a single composite quality score that can hide contact or state failure.

These may improve local expression or ergonomics, but they do not close the continuous-action mechanism.

## 57. Follow-on research packets

After implementing and measuring this IR, the next useful packets are:

1. **Reference-video decomposition and uncertainty** — pose, camera, contact, occlusion, flow, and stylized-frame ambiguity.
2. **Contact-aware retargeting** — how to preserve topology across different body proportions, costumes, and props.
3. **Anime force abstraction** — when to preserve physics, when to exaggerate, and which invariants survive stylization.
4. **Provider control adapter certification** — fixtures, capability detection, degradation behavior, and version drift.
5. **Editorial repair compiler** — selecting regeneration, retiming, interpolation, compositing, or manual correction from measured failure.

---

## Final closure judgment

The proposed five priorities are correct and ordered correctly.

The first three repair the **continuous motor and causal system**. The fourth controls how that system is **shown in animated time**. The fifth controls how it is **projected and edited through space**. Reversing that order risks using camera energy, smears, or more detailed prompts to disguise a fight whose underlying state and contact logic still reset between moves.

The practical ceiling is now explicit:

```text
Prompting specifies meaning.
Persistent IR specifies causality.
Contact and phase graphs specify interaction.
X-sheets specify presentation time.
Camera reconstruction specifies viewpoint.
Pose/rig/constraint signals specify exact motion.
Verification determines whether the result actually obeyed them.
```

That is the bridge from “a sequence of cool attacks” to a continuously evolving fight scene.

---

## Selected primary and official sources

- [Rao & Georgeff — BDI Agents: From Theory to Practice](https://cdn.aaai.org/ICMAS/1995/ICMAS95-042.pdf)
- [Mateas & Stern — Integrating Plot, Character and NLP in Façade](https://users.soe.ucsc.edu/~michaelm/publications/mateas-tidse2003.pdf)
- [Mateas & Stern — Structuring Content in the Façade Interactive Drama Architecture](https://cdn.aaai.org/ojs/18722/18722-52-22361-1-10-20210928.pdf)
- [U.S. Marine Corps — MCDP 1 Warfighting](https://www.marines.mil/portals/1/Publications/MCDP%201%20Warfighting%20GN.pdf)
- [U.S. Marine Corps — MCDP 1-3 Tactics](https://www.marines.mil/Portals/1/Publications/MCDP%201-3%20Tactics.PDF)
- [Mordatch, Todorov & Popović — Contact-Invariant Optimization](https://dl.acm.org/doi/10.1145/2185520.2185539)
- [Ho, Komura & Tai — Spatial Relationship Preserving Character Motion Adaptation](https://dl.acm.org/doi/10.1145/1833349.1778770)
- [Rempe et al. — Contact and Human Dynamics from Monocular Video](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123500069.pdf)
- [SIGGRAPH — Contact and Friction Simulation for Computer Graphics](https://siggraphcontact.github.io/assets/files/SIGGRAPH22_friction_contact_notes.pdf)
- [Drake — Modeling of Dry Friction](https://drake.mit.edu/doxygen_cxx/group__friction__model.html)
- [Liang et al. — InterGen](https://arxiv.org/abs/2304.05684)
- [Donnarumma et al. — Sensorimotor Coarticulation](https://pmc.ncbi.nlm.nih.gov/articles/PMC5322223/)
- [Kalidindi et al. — Task-dependent Coarticulation of Movement Sequences](https://elifesciences.org/articles/96854)
- [Berg et al. — Advances in Anticipatory Postural Adjustments](https://pmc.ncbi.nlm.nih.gov/articles/PMC11726838/)
- [Abe, Liu & Popović — Momentum-based Parameterization of Dynamic Character Motion](https://grail.cs.washington.edu/projects/charanim/mb.pdf)
- [Kovar, Gleicher & Pighin — Motion Graphs](https://research.cs.wisc.edu/graphics/Papers/Gleicher/Mocap/mograph.pdf)
- [OpenToonz — Working in Xsheet/Timeline](https://opentoonz.readthedocs.io/en/latest/working_in_xsheet.html)
- [Toon Boom — About Exposure](https://docs.toonboom.com/help/harmony-24/premium/timing/about-exposure.html)
- [Basset, Bénard & Barla — SMEAR](https://dl.acm.org/doi/10.1145/3641519.3657457)
- [Magliano & Zacks — Continuity Editing and Event Segmentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC3208769/)
- [Kachkovski et al. — Effects of Violating the 180-Degree Rule](https://journals.sagepub.com/doi/10.1177/0093650219838959)
- [Nawrot & Stroyan — Depth from Motion Parallax](https://pmc.ncbi.nlm.nih.gov/articles/PMC3349336/)
- [Wang et al. — MotionCtrl](https://wzhouxiff.github.io/projects/MotionCtrl/)
- [Jin et al. — FloVD](https://jinwonjoon.github.io/flovd_site/)
- [Sowden et al. — Movement Kinematics in Emotion Expression and Recognition](https://pmc.ncbi.nlm.nih.gov/articles/PMC8582590/)
- [Gates & Dingwell — Muscle Fatigue, Movement Stability, and Variability](https://pmc.ncbi.nlm.nih.gov/articles/PMC9116437/)
- [Veen et al. — Compensatory Movement Patterns in Symptomatic Rotator Cuff Tears](https://pmc.ncbi.nlm.nih.gov/articles/PMC7899608/)
- [Runway — Creating with Gen-4.5](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5)
- [Google Cloud — Video Generation Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/overview)
- [Runway — Creating with Seedance 2.0](https://help.runwayml.com/hc/en-us/articles/50488490233363-Creating-with-Seedance-2-0)
- [Lightricks — LTX-2 repository](https://github.com/Lightricks/LTX-2)
- [Lightricks — LTX Control Adapter Documentation](https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/training-modes.md)
- [OpenAI — Sora Discontinuation](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)
- [OpenAI — Sora 2 Prompting Guide](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
