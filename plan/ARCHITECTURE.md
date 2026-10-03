# Architecture

Scope: text-only prompts for AI video models. In the research's own terms this is a **Mode C
compiler** (parses, validates, negotiates, emits) producing a **Mode A artifact** (text pasted
into a prompt field, `text_interpretation_only`), at **control levels L0 (prose semantics) and
L1 (compiled state and timeline)**. Mode D, L2–L5, pose, depth, mocap and reference images are
out of scope and are recorded only as exclusions.

Sources cited by short name are listed at the end.

## 1. Pipeline

```
ASK → intent brief → pass plan → Reason tier → Style tier → Render tier → IR → check → emit → read-back
```

- **Intent brief** (LLM): restate the clip in one paragraph: what is locked by the user, what is
  open, target model, duration if given.
- **Pass plan** (LLM, from `director/passes.yaml`): each pass is mandatory, conditional (with a
  trigger) or optional. A simple ask activates few passes.
- **Three tiers** (owner): Reason fixes what happens and in what order; Style decides which
  moments matter and how they read; Render adds texture and locks. Later tiers never reorder or
  remove what Reason fixed.
- **IR** (`ir.json`, written by the LLM): clip → shots → beats, plus entities, hand ledger,
  action pathways, controls, decisions, verification targets. A field exists only if `check` or
  `emit` reads it.
- **check** (code): validators over the IR. **emit** (code): deterministic prompt assembly from
  treatment wording, per model profile, with a receipt and a loss record.
- **Cold read-back** (separate LLM call): reads only the prompt, lists the beats it sees, in
  order, with state changes. Mismatch = repair the IR, never patch the prompt by hand.

## 2. Reasoning layer

### 2.1 Passes

| Pass | Tier | Owns | Sub-modules |
|---|---|---|---|
| intent | Reason | objective, dramatic function, conflict, reveal, consequence, directorial beats (every change of relationship or intention) | action, objective, obstacle, relationship, subtext, audience information |
| entity | Reason | who and what, and what stays true | identity, wardrobe, anatomy, sides, possessions |
| world | Reason | what changes in the scene and how the world responds | environment state, object state, affordances, material response, persistent changes |
| action | Reason | what bodies do | locomotion, phase, root path, support and balance, speed and force, recovery, secondary motion |
| interaction | Reason | contacts between entities and objects | grasp, hand ledger, action pathways, collision, impact, support, release, impact-and-physics language (stated reactions) |
| physics | Reason | why and how it happens | cause and effect, recoil, momentum, material response, feasibility |
| time | Reason | when, how long, how dense | beats, rhythm fields, timing profiles, holds, overload |
| staging | Reason | where things are relative to each other | blocking, depth, screen direction, action axis, proxemics |
| continuity | Reason / Render | what must persist | state carry-over, wetness, damage, object state, locks |
| performance | Style | how it is acted | acting intent, body, face (FACS when useful), gaze and blink, posture, breath, gesture, Laban Effort (Weight, Time, Space, Flow), Shape, Body, Space, Bartenieff connectivity, affect |
| camera | Style (mandatory on every ask) | how it is seen; explicit camera grammar is always emitted | motion layer, optics layer, framing, shot length, cuts |
| attention | Style | what the viewer sees, misses, discovers | reveal, withhold, hooks, key-pose ranking |
| style | Style / Render | how it looks and feels | visual style, motion style (sakuga, limited animation), realism, capture texture, VFX |
| light_color | Style | how it is lit and coloured | sources, direction, quality, exposure, white balance, palette, grade, colour continuity |
| audio | Render | what is heard | speech, pauses, effects, music, sync |
| synthesis | after Reason and after Style | the whole treatment | contradictions, competing controls, excess complexity, alignment across passes |

Rules: one owner pass per IR field; a sub-module becomes a pass only when it needs its own IR
state and activates on its own; adding a sub-module or pass is a `passes.yaml` entry plus
treatments, with no code change; provider and format handling are never passes.

### 2.2 The pass pattern

```
input state → check research → check treatments → identify gaps
→ reason where allowed → resolve decisions → write output state → declare uncertainty
```

A pass with no research closes in one line: "no research; reasoned: X". Full records are kept
only for decisions that change the prompt.

### 2.3 Records

Every decision that changes the prompt carries the **bridge chain** from the ADRG closure:
`problem → treatment → directorial decision → canonical control → expected visual effect →
verification target`, and the DecisionRecord subset: `decision_id, question, alternatives,
selected, criteria, confidence`. `selected` must be one of `alternatives`. Confidence is not a
probability of being right; `selected` does not mean rendered success.

**Origin** uses the tree's `epistemic_status` values: SOURCE_EVIDENCE, INFERENCE,
CREATIVE_CHOICE, PROJECT_DERIVED, PROVIDER_EXPERIMENT, UNVERIFIED, CONTRADICTED, UNKNOWN.
INFERENCE decisions are appended to `director/gaps.jsonl` (the research-gap log). Gaps that
recur become the owner's next research prompts.

### 2.4 Thinking modes (instructions to the LLM, not executors)

| Mode | Use when | Maps to the existing registry |
|---|---|---|
| direct | one plausible plan, validators strong | rp_direct |
| compare alternatives | a creative fork or a high-impact, uncertain choice | tree-of-thoughts |
| calculation | durations, frames, speech capacity, distances | chain-of-code → `calc` |
| aggregation | merging partial decisions from several passes | graph-of-thoughts → synthesis pass |
| repair | an observed failure | failure-directed repair: smallest patch, never a full rewrite |

Choice uses the research's router features (impact, uncertainty, coupling, irreversibility,
validator strength, budget) as starting rules. Thresholds are engineering conventions until
experiments set them.

### 2.5 Action pathways (the anti-magic guard)

Every physical task is an ordered stage list, planned pose-to-pose: the end state is declared
first, then the stages that reach it. Minimum three stages: anticipation → action → aftermath.
Template from `HANDS`: precondition → anticipation → approach → contact → transfer → effect →
follow-through → recovery → postcondition.

Rules checked by code:

- A state change (cap off, door open, object moved) needs a preceding contact stage and a force
  or transfer stage in the same pathway.
- No beat moves from the initial state to the completed state without the intermediate stages.
- Each stage names the hands or body parts it uses; the hand ledger must have them free.
- Continuity: the object's identity properties (scale, colour, shape) are listed as locks before
  and after.

Pathways are reusable per object type (bottle, door, phone, weapon, cup). Everyday task
decomposition is not research-backed: pathways are tagged INFERENCE and logged as gaps until
renders or research support them.

### 2.6 Hand ledger

Per actor, per beat: `left_hand` and `right_hand` each hold `free`, `holding <object>`,
`on <surface>` or `camera` (a selfie or handheld shot occupies one hand for the whole clip unless
a prop or release is declared). Code checks: no hand holds two things; a stage needing N hands
finds N free; ownership changes only through an overlapping grip; a held object persists until a
release stage.

## 3. Control layer

### 3.1 Controls

A control: `id, pass, field, value, importance 0..1, lock, origin, treatment_id`.

Each control gets, for the target model:

- a **capability class**: native, approximate, semantic, unsupported, unknown
- exactly one **terminal disposition**: native, approximated, semantic, omitted, unsupported, unknown
- a **realization status** on emission: native_exact, compressed_to_text, dropped_with_warning,
  unsupported_error (the reference and post-process statuses are recorded only as exclusions)

A phrase is never upgraded to native because it sometimes works. In text-only work nearly every
control is `semantic`; `native` applies only to API fields the model profile lists (duration,
aspect ratio, negative prompt, seed, frame rate where offered).

Exact requests text cannot enforce ("the release lands on frame 36") become order wording plus a
loss record (`temporal_precision_unenforceable`, policy `block_or_explicit_degrade`). If the user
locked the exact value, emission blocks and says why.

### 3.2 Loss record and receipt

Loss record fields (unchanged from the research): `loss_id, canonical_field, requested{value,
unit}, provider, capability, projection, replacement, loss{type, severity}, accepted`.
Loss types: unsupported_semantic, approximation, observability_loss, scope_loss, temporal_loss,
laterality_loss, intensity_loss, causal_loss, continuity_loss, interaction_loss,
priority_suppression, provider_attention_loss.

Receipt: every emitted sentence maps to a treatment id and a control id, or is marked INFERENCE.
Four validity levels are reported separately: parses, matches schema, decisions correct, render
succeeded.

### 3.3 Verification targets

Each control with visible intent carries `expected_visual_effect` and a check a human or vision
model can run (`target → observable expectation → measurement method → metric → threshold →
verdict`). Adherence is judged per dimension (identity, action, spatial, temporal,
performance quality, facial, connectivity, camera, continuity), never as one score. A vision
model's "looks right" is `interpreted`, not measured.

### 3.4 Camera sub-layers

From `camera_three_layer_semantics`:

| Layer | Contents | Owner |
|---|---|---|
| motion | locked/static, pan, tilt, roll, dolly, tracking, crane/elevate, orbit/arc, handheld/drift | camera |
| optics | focal length, field of view, distance, height, focus plane, depth of field, aperture, rack focus, motion blur / shutter | camera |
| image formation | exposure, white balance, dynamic range → **light_color**; device character, lens distortion, stabilization look, compression and noise → **style (capture texture)** | split |

Failure mode to guard: optical parameters emitted as camera motion.

**Camera move catalog** (`director/vocab/camera_moves.yaml`, from aicameramovements.com, read
2026-10-03; wording UNVERIFIED; 46 site moves + roll and dolly zoom): every move the camera pass may
choose, in 7 categories (pan/tilt, zoom/lens, dolly/track, physical moves, human camera,
drone/crane, specials), each with the site's four-part prompt grammar (Movement · Speed · Framing ·
End), its layer (motion, optics, special), the research's motion kind, and a `function` hint
for decision-making (intensify, reveal, accompany, energize, orient, embody). The camera pass picks
by function, states all four parts, one move per shot, and never writes a zoom as motion. Treatment:
`camera.move_from_catalog`. Validator R-53 (T38) checks the id exists and the layer is respected.

### 3.5 Movement text control: three layers (owner)

Movement and motion are controlled in text through three vocabularies, each with its own dials:

| Layer | Vocabulary | Controls | Pass |
|---|---|---|---|
| quality | Laban BESS: Body, Effort (4 factors), Shape, Space | how a movement feels: Effort Weight, Time, Space, Flow as scaled values; Shape planes; Body part and sequencing; Space reach, zone, pathway | performance |
| origination | Bartenieff | where a movement starts and how it travels: core-initiated, sequential weight shift, cross-lateral connection, proximal-to-distal | performance, action |
| film grammar | cinematography | how it is seen: motion layer, optics layer, framing, cuts | camera (**mandatory** on every ask) |

Laban has a specialized sub-layer for cause and effect, **impact and physics language**: every
contact gets an explicit, stated reaction (recoil, displacement, material response, sound) in the
IR and the prompt. Reactions are never assumed. Owned jointly by interaction (the contact) and
physics (the consequence); `check` fails a contact with no stated reaction.

Laban values are **scaled, not absolute**, and reported as beliefs: each Effort factor is a
position between its poles in [0, 1] with a confidence (e.g. Weight 0.75 toward strong,
confidence 0.6), updated by render verdicts. The IR never stores bare pole words; the emitter maps
the scale to a wording rung (numeric experiment, Laban term, visible body consequence) by the
model profile and importance. The movement classes used in the Laban AI literature (dab, glide,
flick, float, and the rest of the eight Effort actions) are treatments that set all four factors
at once.

- Effort factors, all four: Weight (light ↔ strong), Time (sustained ↔ sudden), Space (indirect
  ↔ direct), Flow (free ↔ bound). Shape (rising/sinking, spreading/enclosing,
  advancing/retreating), Body and Space are sibling sub-modules.

#### 3.5.1 Movement control layer for action (owner; anti-arcade)

Flat, "2D arcade" fights are a dimensionality failure: motion treated as screen-space movement
instead of weighted, spatial, effort-driven body action. The fix is layered reasoning that every
motion decision passes through, whatever the model's strength:

```
WORLD BUNDLE  (world pass)      gravity · terrain · opponent/object mass · camera distance ·
                                momentum source (foot plant) · frame discipline (ones/twos)
      ↓
LABAN / BARTENIEFF REASONING    Effort: 4 factors, scaled, per beat
(performance + action passes)   Shape: 3 planes (Door · Table · Wheel) — plane transitions per beat
                                Body: Bartenieff connectivity (Core-Distal, Head-Tail, Upper-Lower,
                                Body-Half, Cross-Lateral) — the force-transmission path
      ↓
CONSTRAINT RESOLUTION (synthesis)   world × motion: heavy opponent → Strong Weight; slope +
                                gravity → root sinks on a lunge; close camera → Shape legible,
                                far camera → Effort only
      ↓
STRENGTH-SCALED EMISSION (emit, per model profile)
      strong model → full constraint set (Effort values, plane transitions, pathway, world facts)
      weak model   → minimal core (3–5 highest-leverage lines: weight + anticipation, grounding,
                     plane variation, follow-through) + camera/continuity compensation
                     (staggered cuts, angle changes, matched action)
```

Anti-arcade signatures the validators detect on the IR of any power action:

| Signature | Detection on the IR | Corrective constraint |
|---|---|---|
| single-plane motion | no Shape plane change across the action's beats | require a plane transition at impact (Table → Wheel for a hook; Door → Wheel for a kick) |
| zero anticipation | no anticipation stage before the action | require a wind-up beat with opposing weight build |
| momentumless impact | no weight-transfer path (foot → pelvis → torso → limb) recorded | require Upper-Lower and Cross-Lateral connectivity before impact |
| unbroken bound flow | Flow never alternates across beats | alternate bound (controlled) and free (committed) phases |

Priority order for building it: Effort quantification per beat → anti-arcade detectors →
Bartenieff pathways on all power strikes → strength-scaled emitter → world-bundle conditioning.
The numeric Laban calibration contract in the tree applies: values are typed proxies with
tolerances, never physical units.

#### 3.5.2 FACS as a spatiotemporal event (owner)

FACS is not a label. It is an event description close to a motion-capture log, with these
dimensions, all of which the IR carries for the face sub-module of the performance pass:

| Dimension | Values | Source cards |
|---|---|---|
| action units | which muscles are active (AU codes, e.g. AU6, AU12) | `facs.au_catalog` |
| laterality | bilateral, left, right (asymmetry is a realism cue) | `facs.bilateral_asymmetry`, `found.numeric.bilateral_side_semantics` |
| intensity | ordinal A–E; never converted to 0–1 as truth; B–C normal, D one peak, E caricature (lab convention) | `facs.intensity_ordinal_contract` |
| temporal phases | onset → apex start → apex end → offset, in master-clock seconds, inside a beat | `facs.temporal_event` |
| co-occurrence | AUs firing together as a combination (AU6+12 genuine smile, AU1+12 polite, AU4+5+7 negative flash, AU4+7 pre-contact in combat) | `facs.relation_layer`, `facs.au_catalog` |
| head pose and gaze | head orientation change and gaze direction coupled to the event (gaze leads the hand, about 0.12–0.18 s) | `mx.gaze_body_coupling` |
| visibility / occlusion | whether the action is visible to the camera; an occluded AU is `estimated`, never claimed | `continuity.visibility_not_existence` |

Working AU vocabulary (standard FACS; plain-language visible descriptions the emitter uses):
AU1 inner brow raise · AU2 outer brow raise · AU4 brow lowerer · AU5 upper lid raise · AU6 cheek
raise (eyes crease) · AU7 lid tightener · AU9 nose wrinkle · AU10 upper lip raise · AU12 lip
corner pull · AU14 dimpler (not a lip press; the prompt-system reference misdescribes it) · AU15
lip corner depress · AU17 chin raise · AU20 lip stretch · AU23 lip tightener · AU24 lip press ·
AU25 lips part · AU26 jaw drop · AU43/45 eyes closed / blink. Combinations beyond the tree's
cards follow the standard FACS prototypes (surprise AU1+2+5+26, fear AU1+2+4+5+20+26, sadness
AU1+4+15, anger AU4+5+7+23, disgust AU9+10+17, contempt unilateral AU12+14) and are **descriptive
patterns**, never emotion claims in a prompt. Blink about 0.135 s; a micro-expression apex is
under about 0.5 s (standard figures; conventions until measured).

IR shape (to add in T27, read by `check` and `emit`):
`performance.face_events[] = {id, beat, aus: [], laterality, intensity, onset_s, apex_start_s,
apex_end_s, offset_s, combination, head_pose, gaze, visibility, origin}`.

Rules: FACS is descriptive, never an emotion claim (`facs.descriptive_not_emotion`); the emitter
compiles AUs to what the camera sees ("cheeks lift and the eyes crease", not "AU6+12", not "she is
happy"); onset < apex start ≤ apex end < offset and all inside the beat's span; an asymmetric
event names its side; an occluded event cannot be a verification target; intensity is emitted as a
relative word against the anchor expression, one step at a time (§3.5.3).

#### 3.5.3 Relative prompting with anchors (owner rule)

The prompt never states two absolute intensities side by side. It sets one **anchor** (the
baseline movement, stated once) and expresses each escalation **relative to the anchor, one unit at
a time**: "the second swing is faster and lands heavier than the first", not two separate
speeds. This matches the scaled Laban values: the IR stores the scale; the emitter writes the
anchor and the step. Validators flag two absolute magnitude words for the same quality in one
clause.
- Each quality has three strengths of wording: numeric (experiment only), the Laban term, and a
  visible body consequence (what a caption would say). The pole → visible-body mapping does not
  exist in the research yet and is a named gap.
- Each quality is localized to a phase: "Time = Sudden" is not "the whole clip is fast".
- Bartenieff gives initiation and sequencing language (core-initiated, sequential weight shift,
  cross-lateral connection). It has no AI-side research; treatments using it are UNVERIFIED
  until renders support them.
- Importance weights: each layer, beat and control carries `importance 0..1` (default from
  `passes.yaml`, raised or lowered per ask). Importance decides budget survival, position and
  word share in the prompt, and which strength rung is used.

#### 3.5.4 Bartenieff: the six patterns of total body connectivity (owner)

Source card: `cpcs/knowledge/06_body_motion/bartenieff/bartenieff_six_patterns.md` (SOURCE_EVIDENCE).
The six patterns (Hackney's developmental sequence) are **connectivity relationships**, not six
scalar dials, and are kept separate from the **Basic Six exercises** (Thigh Lift, Forward Pelvic
Shift, Lateral Pelvic Shift, Body Half, Knee Drop, Arm Circle). The order is pedagogical; one cross
punch can use several at once.

| Pattern | Meaning | Side rule | What the prompt says (visible consequence) |
|---|---|---|---|
| Breath | whole-body expansion and contraction around breathing | bilateral | "the torso widens on the inhale before the lift; the exhale lets the shoulders drop" |
| Core-Distal | centre ↔ limb ends; movement radiates from or returns to the core | — | "the reach starts in the belly and opens out to the fingertips" |
| Head-Tail | the spine as one axis from head to pelvis | — | "the head leads and the spine follows in a wave down to the hips" |
| Upper-Lower | grounding: lower body supports, upper body acts | — | "weight settles into the front foot before the arm pushes" |
| Body-Half | one side stabilizes while the other side moves | **left or right; never collapsed** | "the left side stays planted while the whole right side swings" |
| Cross-Lateral | diagonal, contralateral coordination (left upper ↔ right lower) | contralateral | "power turns from the rear right foot through the hips and shoulders into the left fist" |

Primitive encoding (from the card): `{connectivity_pattern, initiator, receiver_sequence,
intensity, range, sequencing_delay_ms}` with a worked value of about 55 ms per segment for
proximal-to-distal sequencing (project convention, not a Bartenieff standard).

IR shape (T28): `action.connectivity[] = {id, beat, pattern, side_relationship, initiator,
receiver_sequence: [], intensity 0..1, range 0..1, origin}`. Rules: a power action records at
least Upper-Lower and Cross-Lateral (anti-arcade "momentumless impact"); Body-Half names its side;
the emitter writes the travel of the movement in plain words, never the pattern name. Bartenieff
has no AI-side evidence yet: every connectivity treatment starts UNVERIFIED.

#### 3.5.5 Shape: planes and qualities (owner)

Source: `laban_layering_doctrine.md` (shape qualities), MX §12.3, the owner's anti-arcade note.

| Plane | Also called | Dimensions | Shape quality pair (scaled 0..1 with confidence) |
|---|---|---|---|
| Door | vertical plane | up–down and side–side | rising ↔ sinking (vertical) |
| Table | horizontal plane | side–side and forward–back | spreading ↔ enclosing (horizontal) |
| Wheel | sagittal plane | forward–back and up–down | advancing ↔ retreating (sagittal) |

Shape forms, from the LMA framework (standard vocabulary; not yet in the tree's cards):
**shape flow** (growing and shrinking around the body's own centre, breath-like), **directional**
(spoke-like straight reach, arc-like sweep toward a point in space), **carving / shaping** (the
body moulds itself to the space or an object, three-dimensional). Camera distance decides what is
legible: close → Shape readable, far → only Effort reads.

IR shape (T28): `beats[].shape = {plane_path: [door, wheel, …], form: shape_flow | directional_spoke
| directional_arc | carving, vertical, horizontal, sagittal (each 0..1), confidence}`. Rules: a
power action changes plane at least once across its beats (hook: Table → Wheel; kick: Door →
Wheel); a motion that stays in one plane is flagged (anti-arcade "single-plane motion"); qualities
are scaled and emitted as visible body change ("she rises and opens as she greets him"), never as
the Laban term.

#### 3.5.6 Affect: valence, arousal, dominance (owner)

Source card: `cpcs/knowledge/04_character_performance/affect/affect_vad_trajectory.md`
(SOURCE_EVIDENCE); FL §5.1–5.5; `NATURAL_DIALOGUE_MODE.md` §10 (VAD → acoustic presets).

Affect is a **separate layer** from FACS and from Laban. It is a trajectory of scaled values, not
an emotion label, and it is never inferred from action units (`test_affect_not_inferred_from_au`).

- Dimensions: **valence** (negative ↔ positive), **arousal** (calm ↔ activated), optional
  **dominance** (submissive ↔ dominant). Scale is project-normalized (the card) unless a source
  states one; each value carries `basis` (authored, inferred, …).
- Trajectory: knots `{t, valence, arousal, dominance}` with monotonic `t` in master-clock seconds,
  tied to beats. Example from the card: 0.0 → (0.10, 0.15), 1.0 → (0.25, 0.20), 2.0 → (0.40, 0.35).
- **Experienced vs displayed** (FL §5.3 masking, `M(t) = A_experienced − A_displayed`): two
  trajectories when the character hides a feeling ("smiles subtly while hiding disappointment").
  The displayed trajectory drives the face and voice; the difference drives leaks (a held breath,
  a late blink, a smile that does not reach the eyes: AU12 without AU6).
- Emission: affect is never written as an affect word (`format_ownership`: observable behaviour,
  not "she feels afraid"). It compiles into visible behaviour through FACS combinations
  (§3.5.2), breath and posture (Bartenieff Breath, Shape sinking/rising), Effort scaling (arousal
  raises Time toward sudden and Weight toward strong; a hypothesis to test), and voice presets
  (NATURAL_DIALOGUE §10: excited {valence .7, arousal .7, dominance .4}, sincere {.5, −.2, .3}).
- IR shape (T29): `performance.affect = {experienced: [knots], displayed: [knots] | null, basis,
  confidence}`. Validators: monotonic `t`; values within the declared scale; `displayed` present
  whenever a masking decision exists; no affect words in `prompt.txt` (a word list in the emitter,
  convention).

#### 3.5.7 Specialized physics layer: cause and effect (owner)

Laban says how a subject moves, camera grammar how the shot frames it, world-state the standing
rules of the scene. This layer covers **consequences**: a foot hits a face, a body hits water, a
hand pulls a zipper. Video models render plausible footage and do not simulate physics; they show
action and reaction as loosely associated visuals. The causal chain has to be written into the
prompt. Owned by the physics pass (consequences) with interaction (the contact itself).

**Anatomy of a causal event, in this order:** trigger (who acts, with what part or object) →
contact (the exact surface where the two things meet; the part models skip most) → force quality
(Laban Weight and Time, anchored to a baseline beat) → primary reaction (the immediate response of
what was hit) → secondary reactions (the world a beat later: water displacing, hair and cloth
whipping, dust lifting) → settle (the resting pose and state; where "weird position" failures live).

**Event record** (one per beat; T35; `physics.events[]`):

```json
{"event_id": "evt_01", "beat": "b4",
 "trigger": {"actor": "A", "part": "right boot", "action": "downward stomp"},
 "contact_surface": "B's face",
 "contact_state": "physical_contact_confirmed",
 "force": {"weight": 0.9, "time": 0.8, "relative_to": "evt_00"},
 "primary_reaction": "B's head snaps sideways into the ground",
 "secondary": ["dust bursts outward", "B's hair whips"],
 "settle": "B lies motionless, face turned away, arms limp",
 "depends_on": [], "must_not_imply": [], "risk": "high", "origin": "CREATIVE_CHOICE"}
```

`contact_state` ∈ physical_contact_confirmed · near_contact · occluded_contact · editorial_impact ·
unknown. `depends_on` records causes (the splash comes from the dive); `must_not_imply` records
what must stay false (A never touches B) and feeds the scoring checklist, not the prompt, until
tests show negatives help.

**Rules (hypotheses until runs confirm them):**

- Edge admission: no reaction enters the IR without a named trigger and contact. A noun list
  ("punch, recoil, dust") with no causal links is rejected.
- One causal event per beat. "One causal event per clip" is a trade-off to test, not a rule: a 15–30 s
  fight becomes many clips and each handoff risks drift.
- Force is relative: `relative_to` names an earlier event or beat; the emitter resolves the
  comparison into words ("much heavier than the previous strike"). Never two absolutes (§3.5.3).
- Settle pose named whenever the event ends on the ground or in water, or the owner marks it.
- Compile order is cause → contact → reaction → settle in one flowing sentence with connectors
  ("landing squarely on", "as", "on impact", "then"): "A's right boot comes down hard and fast,
  much heavier than the previous strike, landing squarely on B's face. B's head snaps sideways
  into the ground as dust bursts outward and his hair whips, then he lies motionless, face turned
  away, arms limp."
- No newtons, anthropometry or biomechanics in a text prompt; the relative dial is enough.
- Defer the typed event graph, sub-compilers and trajectory splines; add `depends_on` edges only
  when a beat has dependent events (dive, then kick).

**Capability check by risk, per dialect** (model profile `contact_risk`):

| Risk | Contact types | If the dialect is flagged unreliable |
|---|---|---|
| low | splashes, debris, cloth and hair reacting | emit as is |
| medium | body-on-body strikes, awkward falls | degrade: wind-up then cut to the reaction, or reaction-only shot |
| high | fine mechanisms (zippers, caps), graphic contact, exact choreography | degrade: hide the contact point with the camera angle (`occluded_contact`) or cut to the reaction (`editorial_impact`); log the downgrade as a loss |

Unknown reliability (the default for a new dialect) emits in full and marks the event for the eval
log. Vocabulary gaps (missing secondary effects, bad end poses, effect before cause) are fixed by
wording; ceilings (fine mechanisms, exact choreography, possibly graphic contact) are not.

**Eval log** (extends `director/runs/ledger.jsonl`): per render store IR hash, prompt hash,
dialect version, seed, access path, and three yes/no scores per event: contact happened, reaction
followed, end pose sane. At least three seeds per prompt; one good output can be luck.
Repair goes upstream: `depends_on` says which earlier event to fix when a reaction fails.

**Failures registry** (`director/failures.jsonl`): seeded with the A/B/C test on the stomp —
plain prompt vs causal prompt vs prop-instead-of-person. The result separates failures wording
fixes from model limits and tests the safety-avoidance hypothesis for graphic contact.

**Verification reality:** automatic checking of physical commonsense is unsolved (VideoPhy-2
trained a dedicated 7B video-language judge for it); v1 verification is the owner or a VLM
answering the three yes/no questions. "Negative phrasing cannot encode physics" and "causal wording
fixes reaction failures" are both hypotheses the eval log settles.

## 4. Time and beats (owner: "the big one")

### 4.1 Clocks and hierarchy

Master clock in seconds is authoritative; frame clock (`frames = seconds × fps`) and any musical
grid are derived. Never round intermediate values. Hierarchy: sequence → scene → phrase →
exchange → action → phase → micro-event → frame.

### 4.2 Rhythm is a set of fields, not a number

Independent fields (from `rhythm_metrics_contract`): tempo, tempo curve, cadence, meter, beat
phase, syncopation, micro-pauses, anticipation beats, accent strength, event density, swing,
rubato, entrainment, phase lock. A fast scene may hold a long micro-pause; a slow scene may
carry one sudden accent. Steering sets values on these axes, not "fast" or "slow".

### 4.3 Timing profiles (conventions, labelled as such)

| Profile | Onset | Accel | Impact hold | Settle | Status |
|---|---|---|---|---|---|
| snappy_24fps | 2–4 f | 2–4 f | 0–2 f | 3–7 f | CPCS_CONVENTION |
| floaty_24fps | 6–12 f | 6–14 f | 0–1 f | 8–18 f | CPCS_CONVENTION |
| anime_limited | key-pose hold 2–12 f | smear 1–2 f | impact 1–3 f | — | PRACTICE / CPCS_CONVENTION |
| ugc_natural | loose onsets, casual pauses, no designed impact | — | — | — | owner practice (UGC manuals) |

Punch of one action beat: `impact_frames = anticipation + strike + hold + settle`. Fewer
in-betweens read faster; one in-between turns a snap into a rolling hit. Small screens compress
motion: shorten action beats for phone playback.

### 4.4 Beat planning procedure (the LLM, in the time pass)

1. Emotional register: slow-hold, floaty or snappy.
2. Directorial beats: one per change of relationship or intention.
3. Tempo curve across the scene, not one tempo.
4. Micro-pauses and anticipation beats.
5. Event density at the apex (superhero low, kung fu maximal, boxing metered).
6. Variation: never one rhythm all scene.
7. Key poses named and ranked (K0–K6): the prompt says which frames matter and in what order.

Emotional formula (anime): slow onset 6–12 f + long key-pose hold 2–12 f + minimal smear + long
settle 8–18 f + a wide establishing shot before the apex + rest periods; the slow element sits
inside a fast context, never fast–stop–fast–stop.

### 4.5 Fit and overload (code)

Each beat carries a minimum readable time (convention, origin tagged). `check` computes
`load = Σ min_time`, then `load ÷ clip_length` → FITS / TIGHT / OVERLOADED. Duration is never
invented: unknown duration gives order and relative shares only. Overload returns options: cut
lowest-importance beats, overlap beats with no causal path between them, split into shots or
clips with a state handoff, lengthen if the model allows. Prompts are never squeezed.

Motion budget per shot (production heuristic): one dominant subject action, one major camera
move, one or two secondary body actions, one to three passive material responses. Three or four
ordered events outperform a paragraph of simultaneous actions. 8-second models: one clip per
beat.

### 4.6 Speech

Speech rate 150–190 words per minute; a Veo-class 8 s clip carries about 10–12 words of
dialogue; pre-emphasis pause 200–300 ms; turn gap about 200 ms; about one disfluency per 5–7 s
and never zero in a casual register. Line length is checked against clip length.

## 5. Knowledge format: treatments

Prompt wording lives in small files: `director/treatments/<pass>/<id>.md`.

```
---
id: interaction.grip_power_bottle
pass: interaction
triggers: ["opens a bottle", "unscrews the cap", "twist-off"]
not_when: ["bottle already open", "two-handed task impossible: one hand holds the camera"]
backs: [cpcs.contact.interaction_lifecycle, cpcs.mx.affordance_constraints]
from: "Additional/HANDS_CONTACT_MANIPULATION.md §2.2, §5"
origin: PROJECT_DERIVED
importance: 0.7
---
## Wording
```prompt core
<model-agnostic wording>
```
```prompt dialect=seedance
<optional override for one model>
```
## Failure signs
- ...
## Effects
- claim · evidence_status (unverified | supported | contradicted) · model · run ids
```

Rules: frontmatter is routing only; the body headings are fixed and parsed by `emit`; cards and
manuals stay whole as sources; nothing is migrated in bulk. The 132 kitchen cards and 15 blocks
in the prompt-system repo are read when an ask needs them and become treatments one at a time.

## 6. Semantic core and model dialects (owner)

The IR and the `core` wording are model-agnostic. Each model has a profile and may have a
dialect:

- **Profile** (`director/profiles/<model>.yaml`): prompt length limit, negative-prompt field,
  durations, aspect ratios, frame rate, audio, native API fields, every fact tagged documented /
  measured / guess, with source and date.
- **Dialect** (same file): clause order, vocabulary the model responds to, words to avoid, how
  it treats structure pasted as text, separate-field habits (Veo: shot, style, lighting,
  character kept as separate parts; Runway: subject motion, scene motion, camera motion, style
  compiled separately; Kling: camera moves may map to native parameters).
- Treatments carry `core` wording plus optional `dialect=<model>` blocks. `emit` picks the
  dialect block when present, else core.
- Candidate models named by the owner: Seedance, Kling, Hailuo, Gemini/Veo, Wan. Seedance first.
  Evidence is per model: a result on one model is UNVERIFIED on another.

### 6.1 Intent catalog and dialect levers (owner: "agnostic first, dialects as lenses")

The IR marks **intents** in model-agnostic form. A dialect is a lens applied at emission that maps
each intent to the lever that model responds to, with its own evidence status. Nothing
model-specific ever enters the IR.

| Intent (agnostic, in the IR) | IR representation | Example dialect levers (per profile, each with evidence) |
|---|---|---|
| emphasize a word or beat | `emphasis: [spans]` on a dialogue or performance control | Hailuo: `<i>word</i>`, `<emphasis>word</emphasis>`, `*word*` (owner-observed; asterisks sometimes read as a bleep) · others: unknown |
| pause or hold | beat with `hold: true` / `pause_s` | "beat", "pause", ellipsis, explicit seconds; per model |
| camera move | camera control (motion layer) | Kling: native camera parameters (horizontal, vertical, zoom, pan, tilt, roll) · prose elsewhere |
| speech line | `audio.dialogue` control | Veo: quoted line + "(no subtitles)" · models without audio: omit, loss record |
| order and timing | beats order; `time.*` controls | order words, timestamps, shot lists (Seedance guides: timecoded shot list for long clips) |
| exclusion | `negatives.*` controls | dedicated negative field (Veo) · shared prompt text (Kling) · none (Runway) |
| identity anchor | entity locks | reference image where supported (out of scope); descriptive locks in text |
| shot settings | `clip.duration_s`, `clip.aspect_ratio` | API fields where native; prose otherwise |

Rules:

- A lever lives only in `director/profiles/<model>.yaml → dialect.levers[]` with
  `{intent, syntax, evidence: owner_observed | documented | measured | unknown, caveats, runs}`.
  The owner's untested observations enter as `owner_observed`, never as fact.
- `emit` applies levers after assembly and records each application in the receipt
  (`lever: <intent>`), so a render verdict can credit or blame the lever.
- An intent with no lever in the target dialect is emitted in core wording and recorded as a loss
  (`provider_attention_loss`, severity low) when the intent mattered (importance ≥ 0.7).
- Lever evidence is per model and per route; a lever proven on one route is `unknown` on another.
- The reasoning layer sees the lever list during model fit (synthesis, taste pass) so it does not
  plan intents the dialect cannot carry, but it never writes lever syntax into the IR.

## 7. Stylized motion (sakuga, limited animation)

Design for silhouette and simplicity; prompt for motion grammar (key poses, holds, smears,
impact flashes, rhythm breaks), not anatomy; keep clips short and motion-focused; name which
frames matter and in what order. Style-tier weights per beat (e.g. silhouette 0.8, anticipation
0.7, impact 0.9) sit on top of Reason-tier order; Render may texture interstitial motion (for a
UGC look: handheld sway, imperfect hands) while the designed impact frame stays crisp and object
locks hold. A character-visualization stage (image first) is out of scope for text-only and is
recorded as an exclusion.

## 8. Steering and diversity

One small profile merged defaults → user → project → ask (later wins, locks hold):

| Group | Dials |
|---|---|
| Control | per pass off / auto / on; depth light / standard / deep; importance; locks |
| Reasoning diversity | lens (director, cinematographer, animator, choreographer, editor, marketer); thinking mode per pass; alternatives considered; risk (proven ↔ exploratory); seed |
| Output style | prose voice (terse caption, rich cinematic, shot list); words per beat; explicit numbers; `variation` 0–1; `n` variants |
| Time | the rhythm fields and timing profile of §4 |

Only free fields vary. Same seed and inputs → same prompt. Variants come back labelled by what
differs, so a batch doubles as an A/B test. A per-user taste profile (from verdicts) weights
sampling.

## 9. Validators and calculators

Validators check only what the LLM wrote; they never parse the ask:

hand ledger · action pathway completeness · stated reaction for every contact · explicit camera
grammar present · beat fit and order (`precedes` is not `causes`) · speech capacity · one owner
per field · exactly-once disposition · budget and channel validity · tier rule (Style and Render
did not reorder Reason) · receipt completeness.

Calculators (`calc`) hold research formulas and tag outputs with the origin of their inputs:
beat frames, phase ratios × duration, exposure time `shutter_angle / (360 × fps)`, apparent
image velocity `x = fX/Z` (qualitative use: long lens and follow-cam dampen perceived speed),
speech words from seconds, strike phase split (anticipation 25–35 %, contact 10–15 %,
follow-through 25–35 %, recovery 15–30 %), engagement range check.

Rig- or mocap-only quantities (jerk, path straightness, inverse dynamics, image-plane flow,
intrinsics) are out of scope.

## 10. Evaluation

- Baseline per ask: a plain prompt written without the compiler. Compiled vs baseline rendered on
  the same model; owner verdict per adherence dimension; logged in the run folder and
  `director/runs/ledger.jsonl`.
- Trigger matching: an ask test set (seeded from the prompt-system repo's
  `retrieval_benchmark.yaml` plus owner asks) scored against the kitchen's `concepts.py` as the
  baseline once there are enough treatments to matter.
- Kill criterion: if compiled prompts do not beat baselines on most asks in phase 2, stop and
  rethink before building more.

## 11. Research ingest (procedure written after doing it by hand)

Document route: new paper or notes → proposed treatments, sub-modules or passes (question, IR
fields, validators, slot), numbers and scales, model facts, parked claims → owner approves. Each
new treatment needs ≥ 3 triggers and ≥ 1 test ask. A package is integrated when every claim is a
treatment, a validator, a scale, a model fact, or explicitly parked. Video harvest is parked.

Known gaps to research: everyday task decomposition for object handling; Laban pole → visible
body mapping; clip capacity (events per clip length) per model; Seedance facts; light and colour;
attention; world reactions; Bartenieff applied to video prompting.

## 12. Mapping onto the existing research (cite, do not relocate)

| Director piece | Cites |
|---|---|
| Capability classes, dispositions, loss records | `cpcs/runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md` |
| Budget and what survives | `cpcs/runtime/07_compiler/salience_budgeting/control_priority_attention_budget.md` |
| Text fallback order | `cpcs/runtime/08_provider_negotiation/text_fallback/provider_fallback_ladder.md` |
| Modes A–D, carrier roles, clause order, compression order | `cpcs/runtime/07_compiler/structured_prompting_architecture.md`, `carrier_planner/carrier_role_semantics.md`, `format_ownership.md`, `Additional/FORMAT_CRAFT_encoding_video_prompts.md` |
| Decision record, bridge chain | `cpcs/runtime/04_synthesis/decision_record.md`; `Additional/04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE_COMPLETE.md` §10 (record shapes only) |
| Origin and evidence | `cpcs/knowledge/00_foundations/invariants/epistemic_firewall.md`, `.../uncertainty/evidence_two_axis_model.md`, `cpcs/00_governance/policies/control_plane_reference.md` §6 |
| Time vocabulary and profiles | `cpcs/runtime/06_canonical/temporal_tracks/temporal_coupling.md`, `cpcs/knowledge/10_time_rhythm/rhythm_metrics_contract.md`, `beat_syncpoint_alignment.md`, `cpcs/knowledge/06_body_motion/phase_grammar/` |
| Hands, contact, pathways | `Additional/HANDS_CONTACT_MANIPULATION.md`, `cpcs/knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md`, `cpcs/knowledge/08_objects_affordances/affordance_constraints.md` |
| Capture texture | `Additional/CAPTURE_SURFACE_REALISM.md`; prompt-system `lab/blocks.yaml` `blk_device_iphone12` |
| Performance | `Additional/LIVING_PERFORMANCE_REALISM.md`, `Additional/NATURAL_DIALOGUE_MODE.md`, FACS and Laban cards under `cpcs/knowledge/04_character_performance/`, `06_body_motion/laban_bess/`, `bartenieff/` |
| Camera | `cpcs/knowledge/12_camera_image_formation/` (three layers, impact sync, parallax) |
| Verification | `cpcs/verification/semantic/verification_expectation_model.md`, `cpcs/verification/failures/failure_mode_catalog.md`, `cpcs/verification/repair_strategy.md` |
| Sakuga, combat timing | `cpcs/knowledge/16_style_visual_language/anime_sakuga.md`, `cpcs/knowledge/05_action/combat/`, `Additional/Continous Combat State.md` (key-pose ranking, control ladder) |
| Provider findings | `cpcs/providers/{veo,kling,runway}/src001_findings.md`, `cpcs/runtime/08_provider_negotiation/provider_capability_snapshots.md` |

External references supplied by the owner (not yet read into treatments): LaMoGen
(arxiv 2509.24469, Laban-conditioned motion diffusion); Guo et al. 2022, Laban-based motion
classification; bodily expressed emotion via LMA (S2666389923001854); Bartenieff Fundamentals
overviews (Wikipedia; Academia "Using LMA Effort to Enhance Body Connectivity";
laban-analyses.org summary). Laban has AI-side evidence; Bartenieff is an untested vocabulary.
