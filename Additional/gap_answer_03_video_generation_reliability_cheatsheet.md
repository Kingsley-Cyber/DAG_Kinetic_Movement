# UG-008 Supplement — Causal video-generation reliability cheat sheet

Research-backed workflow for CPCS validation and human review  
Research date: 2026-08-09 (America/Denver)  
Status: staged research proposal; not curated repository truth  
Scope: Veo 3.1, Sora 2, Kling VIDEO 3.0/3.0 Turbo, Runway Gen-4.5, and mechanism-heavy video generation

## BLUF

Video generators are very good at producing a plausible-looking sequence and much less reliable at preserving a mechanically valid state transition. “World simulator” is a research direction, not a provider guarantee. OpenAI’s own Sora report lists incorrect interaction physics, wrong object-state changes, long-duration incoherence, and spontaneous objects among the model’s limitations [E1]. VideoPhy and PhyGenBench independently show that semantic prompt adherence and visual quality do not establish physical correctness or causal order [E2][E3].

For the sling-bag failure, the most reliable stack is:

`typed action operator → one causal event per clip → endpoint anchors → provider-specific prompt compiler → causal verifier → clip chaining`

The high-value conclusions are:

1. **Pin state, contact, and order—not just appearance.** The failure surface includes identity loss, effect-before-contact, broken attachment, invalid kinematics, non-monotonic motion, and incorrect final state.
2. **Your `pre / motion / post / forbid` contract is planning-inspired, but it is not literally a STRIPS operator.** `pre` maps to preconditions and `post` maps to add/delete effects. `motion` belongs to a trajectory or durative-action layer. `forbid` is an invariant or output validator; a STRIPS delete list means facts made false by the action, not unwanted imagery [E4][E5].
3. **First-and-last-frame conditioning is an endpoint constraint, not a deterministic physics solver.** It sharply reduces uncertainty about the two boundary states, but the model can still morph, teleport, penetrate, or reverse causality between them.
4. **One physical handoff per generation is the safest default.** For this case, zipper motion, contact transfer, panel folding, and cavity reveal should not be one unconstrained event. This is an engineering inference supported by the Sora guide’s recommendation for shorter clips and one clear action per shot, plus the benchmark evidence on causal-order failures [E3][E10].
5. **The negative-prompt assumption must be corrected for current products.** Veo exposes a dedicated API `negativePrompt`; current Kling 3.0’s new API combines positive and negative descriptions in one prompt; Sora 2 documents no separate negative field; Runway Gen-4.5 documents positive phrasing and exposes no negative field in its current video endpoint [E8][E9][E11][E12][E14].
6. **Camera vocabulary helps because current provider guides explicitly recognize shot, movement, lens, focus, lighting, and temporal terms.** The stronger claim that a particular provider “defaults to cinematic because its training captions came from film/stock” is plausible but not established by the cited official documentation.

### Refined one-line mental model

**Represent the endpoints and contact modes, constrain the path with invariants, express shortcuts through the provider’s actual control surface, and split at every causal handoff.**

## Current provider-control matrix

Provider behavior changes quickly. This table records only controls verified in official documentation as of the research date. “Not documented” does not prove that a consumer UI has no hidden or experimental control.

| Current model / surface | Prompt grammar that the official guide rewards | Endpoint conditioning | Negative handling | Verified text limit | Verified duration | Operational note |
|---|---|---|---|---:|---:|---|
| **Google Veo 3.1 on Gemini Enterprise Agent Platform / API** | Break the request into subject, action, scene/context, camera angle and movement, lens/optical effects, style, temporal elements, and audio [E8]. | API supports `image` as first frame and `lastFrame` as the ending frame. First frame is required when `lastFrame` is used [E9]. | **Dedicated `negativePrompt` string exists.** The guide recommends listing unwanted elements rather than writing commands such as “no” or “don’t” [E8][E9]. | Not stated in the cited public schema. | 4, 6, or 8 seconds for the documented Veo 3 first/last-frame workflow [E9]. | First/last frames constrain boundaries, not the intermediate mechanism. Prompt enhancement can also rewrite input unless the relevant setting is controlled. |
| **OpenAI Sora 2 Videos API** | Specify framing, depth of field, action beats, lighting/palette, and one plausible action. Treat the prompt as a wish list, not a contract [E10]. | `input_reference` anchors the **first** frame. The cited create API does not document a last-frame parameter [E11]. | **No dedicated negative field is documented.** Put invariants in positive language in the main prompt. | Not stated in the cited public guide/model page. | 4, 8, 12, 16, or 20 seconds in the current API guide [E11]. | The Sora 2 Videos API is deprecated and scheduled to shut down on **2026-09-24** [E11]. Do not build a new long-lived CPCS dependency without a migration plan. |
| **Kling VIDEO 3.0 new API** | Natural-language prompt; API explicitly allows positive and negative descriptions in the same prompt. Custom multi-shot uses `shot n, duration, words;` and supports up to six storyboards [E12]. | Supports first-frame-to-video and **first-and-last-frame-to-video**; last-frame-only is not supported [E12]. | **No separate negative field in the new API payload.** Positive and negative descriptions share the prompt text. Legacy surfaces may differ. | Maximum 3,072 characters; official recommendation is at most 2,500. A custom shot description is capped at 512 characters [E12]. | 3–15 seconds [E12]. | Multi-shot is available, but a mechanism-critical CPCS workflow should still prefer one causal event per clip unless multi-shot is itself the creative requirement. |
| **Kling VIDEO 3.0 Turbo new API** | Single prompt text can include positive and negative descriptions [E12]. | Current Turbo image-to-video API supports a first frame only; it says first+last is not yet supported [E12]. | Combined in the prompt, not a separate field. | 2,500 characters [E12]. | 3–15 seconds [E12]. | Do not assume the controls of Kling 3.0 and 3.0 Turbo are identical. |
| **Runway Gen-4.5 web/API** | Text-to-video describes visuals and motion; image-to-video should focus on motion because the image supplies appearance and composition [E13]. | Gen-4.5 image-to-video API uses an image as the first frame. The separate **Animate with Keyframes** app accepts starting and ending frames [E15]. | **No dedicated negative field in the current endpoint.** Runway explicitly recommends positive phrasing because negative concepts can still be rendered [E14]. | `promptText`: 1–1,000 UTF-16 code units [E16]. | 2–10 seconds [E13][E16]. | Gen-3 keyframes are retired. Use the current Animate with Keyframes app rather than an obsolete Gen-3 recipe [E15]. |

### The practical negative-prompt rule

Negative controls are useful for excluding static content, but they are a weak way to encode temporal physics. “No teleporting slider” names the failure; “the gripped tab and slider remain attached and co-move continuously along the same rail” describes the desired relation.

Use this precedence:

1. Put causal and geometric invariants in **positive language** in the main prompt.
2. Use endpoint frames to show the boundary states.
3. If a dedicated negative field exists, use it as a secondary exclusion list.
4. Reject causally invalid outputs in verification; do not expect prompt syntax to guarantee them.

## 1. Why video models break

### 1.1 “World simulator” is a capability hypothesis

The 2024 Sora report presents a diffusion transformer operating on spacetime patches and argues that scaling video models is a promising path toward general-purpose simulators. The same report is explicit that the model often fails basic interaction physics, object-state changes, long-duration coherence, and spontaneous-object control [E1]. The label therefore describes an aspiration and observed emergent capabilities, not a formal simulator contract.

The strongest operational interpretation is:

> A video model estimates a visually likely continuation under its conditioning. It is not required to maintain an explicit, inspectable object graph, contact state, joint constraint, or conservation law.

That distinction explains why a clip can look polished while a slider teleports, a flap opens before the hand touches it, or the bag interior appears without a valid seam-and-panel transition.

### 1.2 What the physics benchmarks add

**VideoPhy** contains 688 prompts spanning solid–solid, solid–fluid, and fluid–fluid interactions. Its evaluation separates semantic adherence from physical commonsense. In the study’s historical model set, the best joint score for satisfying both was only 19.7%; the number is evidence of difficulty at that time, not a current ranking of Veo, Sora, Kling, or Runway [E2].

VideoPhy’s failure analysis is directly useful for mechanism prompts:

- conservation/amount errors;
- velocity changes without an external cause;
- momentum or force-response errors;
- rigid solids deforming incorrectly;
- fluids behaving like solids or losing material character;
- interpenetration and invalid contact.

**PhyGenBench** contains 160 prompts covering 27 physical laws across mechanics, optics, thermal phenomena, and material properties. Its evaluation separates: (1) whether the key physical phenomenon occurs, (2) whether the causal order is correct, and (3) whether the result looks natural. The benchmark reports that scaling and prompt engineering help some simple cases but do not solve dynamic physical reasoning [E3].

For CPCS, this yields a crucial verification order:

`required event exists → cause precedes effect → constraints hold → final state is correct → visual naturalness`

Do not score beauty first.

### 1.3 Mechanism failure taxonomy

| Failure class | What it looks like | Why prose alone is weak | What to pin down |
|---|---|---|---|
| **Object permanence / identity** | A hand, tab, slider, tooth row, or panel disappears, duplicates, or changes identity across occlusion. | The model may preserve local appearance without a persistent entity record. | Named parts, reference images, stable framing, identity-bearing tracks where supported, and pre/mid/post verification. |
| **Causal ordering** | Seam opens before slider motion; panel rises before hand contact; contents appear before cavity reveal. | Text can mention all events without forcing their order. | Separate clips or explicit beats; require contact before effect; check ordering at sampled frames. |
| **Contact / attachment** | Hand passes through the tab, loses the grasp, or moves independently while the slider follows. | Contact is a relation over time, not a static noun. | `contact_mode`, `grasp_owner`, co-motion, and over-all invariants. |
| **Kinematic constraint** | Slider leaves the rail; drawer moves sideways; lid hinges about the wrong edge. | A caption describes the action class but not the allowed configuration manifold. | Part–joint graph, motion axis/path, fixed parent, and boundary images. |
| **State-transition correctness** | Eating leaves the object intact; zipper motion does not release the seam; the panel self-opens. | The model can render a familiar action without applying the correct effects. | Explicit add/delete effects and final-state predicates. |
| **Monotonic motion** | Slider advances, jumps backward, then appears at the end; flap re-closes mid-open. | “Moves from A to B” leaves the path unconstrained. | A qualitative monotonic invariant and midpoint inspection. Do not invent an unsupported numeric tolerance. |
| **Material / topology** | Rigid slider melts; fabric tears or merges; gussets inflate without panel separation. | Appearance priors do not guarantee material or topological continuity. | Rigid/deformable typing, topology-preservation checks, and a separate deformation phase. |
| **Long-horizon coherence** | Later events contradict earlier states or introduce new objects. | Every added action and cut increases state and timing ambiguity. | One event per clip, last-frame chaining, and state handoff records. |

## 2. Planning operators: the formal version of the contract

### 2.1 What maps to STRIPS—and what does not

Classical STRIPS represents an action using preconditions plus an add list and delete list [E4]. PDDL2.1 adds temporally annotated start, over-all, and end conditions/effects for durative actions [E5].

| CPCS contract field | Closest planning concept | Important distinction |
|---|---|---|
| `pre` | Preconditions / `at start` conditions | Facts required before the action may begin. |
| `motion` | Continuous controller, motion plan, or durative action implementation | Classical STRIPS does not represent the path. PDDL2.1 can represent interval conditions and limited continuous numeric change, but it is not a video-motion solver. |
| `post` | Add and delete effects / `at end` effects | An add list makes a predicate true; a delete list makes a predicate false. |
| `forbid` | State invariant, trajectory constraint, or output validator | It is **not** the STRIPS delete list. “No teleportation” is a forbidden trajectory, whereas deleting `closed(seam)` is an intended action effect. |

The CPCS structure is therefore best described as a **durative symbolic operator with a motion contract and visual validators**.

### 2.2 Minimal systematic recipe for any mechanism

For a drawer, buckle, lid, jacket, carton, zipper, or folding object:

1. **Name parts and identities.** Example: hand, handle/tab, moving body, fixed body, rail/hinge/closure, revealed region.
2. **Declare connections.** Fixed, revolute, prismatic, distributed closure, deformable attachment, support, or unknown.
3. **Declare qualitative state variables.** Examples: `contact_mode`, `closure_state`, `joint_region`, `panel_pose_region`, `cavity_visibility`.
4. **Declare affordances.** Which part can be grasped, pulled, rotated, pressed, supported, or released. In robotics, affordance is an agent–object action possibility, not merely a visual label [E6].
5. **Write preconditions.** Include the required contact and current mechanism state.
6. **Write the motion law.** Direction/path, co-motion, monotonicity, and the only permitted degrees of freedom.
7. **Write over-all invariants.** Contact persists, part stays on its joint, fixed body stays fixed, topology remains valid.
8. **Write effects.** Add the new state; delete the old mutually exclusive state.
9. **Write failure predicates.** Effect before contact, detachment, path violation, identity change, wrong final state.
10. **Choose the evidence carrier.** Text, first frame, first+last frames, reference video, edit, masks/tracks, or hard cut.

This mirrors robotics planning’s separation between a symbolic action sequence and a continuous trajectory over robot and scene kinematics [E7].

### 2.3 Sling-bag state variables

Use qualitative or source-derived values. Do not create arbitrary metric thresholds.

```yaml
entities:
  rear_shell: rigid_or_semi_rigid_parent
  front_panel: deformable_movable_panel
  zipper_slider: rigid_prismatic_part
  closure_seam: distributed_closure
  top_handle: attached_part
  side_gussets: deformable_expansion_parts
  interior_cavity: revealed_region
  left_hand: articulated_agent_part
  right_hand: articulated_agent_part

state:
  slider_region: [start, intermediate, end, unknown]
  seam_ahead_of_slider: [interlocked, unknown]
  seam_behind_slider: [interlocked, released, unknown]
  panel_state: [closed, separating, folded_open, unknown]
  gusset_state: [compressed, expanding, expanded, unknown]
  cavity_visibility: [not_visible, partially_visible, visible, unknown]
  left_contact: [none, slider_tab, panel_edge, support, occluded_unknown]
  right_contact: [none, slider_tab, panel_edge, support, occluded_unknown]
```

### 2.4 Example durative operator

```yaml
operator: translate_zipper_slider
parameters: [acting_hand, slider, tab, rail, closure_seam]

pre:
  - contact(acting_hand, tab)
  - grasped_by(tab, acting_hand)
  - on_rail(slider, rail)
  - slider_region(start)
  - seam_ahead_of_slider(interlocked)

motion:
  - acting_hand, tab, and slider co-move continuously along the rail
  - slider progress is monotonic from start toward end
  - the rear shell and camera-relative mechanism frame remain stable

over_all:
  - contact(acting_hand, tab)
  - attached(tab, slider)
  - on_rail(slider, rail)
  - seam_ahead_of_slider(interlocked)
  - no_topology_change(rear_shell, front_panel, gussets)

effects_add:
  - slider_region(end)
  - seam_behind_slider(released)

effects_delete:
  - slider_region(start)
  - seam_behind_slider(interlocked)

failure_predicates:
  - seam_release_before_slider_passes
  - slider_motion_before_hand_contact
  - hand_slider_detachment_during_motion
  - slider_leaves_rail
  - reverse_or_teleporting_slider_progress
  - panel_opens_during_slider_only_operator
```

This operator deliberately does **not** open the panel. That is a later operator with new preconditions.

### 2.5 Full causal chain

```text
closed
→ contact acquired on zipper tab
→ slider translates along rail
→ seam releases behind slider
→ slider stops
→ contact releases or transfers
→ hand grasps movable panel edge
→ panel separates and folds
→ gussets expand
→ interior cavity becomes visible
→ stable open state
```

If the reference hard-cuts from the zipper shot to the already-open bag, CPCS may depict:

```text
observed zipper span → authored edit cut → observed open-state span
```

The omitted contact transfer, panel fold, and gusset expansion remain **unobserved**, not implicitly recovered.

## 3. First/last-frame conditioning

### 3.1 What it actually buys

An endpoint pair reduces uncertainty about:

- object identity and count at the boundaries;
- camera composition and viewpoint;
- the initial and final mechanism state;
- the location of major parts;
- the visible effect that must exist at completion.

It does **not** guarantee:

- the correct path between the frames;
- cause-before-effect;
- contact persistence;
- collision avoidance;
- topology preservation;
- exact hand or finger trajectories.

The right claim is: **endpoint anchoring is usually the strongest broadly available control for a state transition, but it is still stochastic interpolation.**

### 3.2 Authoring a useful endpoint pair

The two frames should differ by one intended state change:

- same camera pose, lens character, crop, and aspect ratio;
- same object identities and object count;
- same lighting direction and background where possible;
- physically reachable final configuration;
- no hidden cut, camera jump, or unrelated appearance change;
- enough visible mechanism geometry to judge the transition.

Bad endpoint pair:

`closed bag, wide front view → open bag, overhead view with hands swapped`

Better endpoint pair:

`locked close-up, hand grasping tab at rail start → same view, same hand and grasp, slider at rail end, seam released only behind it`

### 3.3 Endpoint availability by provider

- **Veo 3.1:** native first+last-frame API control [E9].
- **Kling VIDEO 3.0:** native first+last-frame control; Kling 3.0 Turbo’s new API currently documents first frame only [E12].
- **Runway:** current Gen-4.5 API uses a first image; the Animate with Keyframes app accepts start and end frames [E15][E16].
- **Sora 2 API:** current documentation exposes a first-frame `input_reference`, not a last-frame input [E11].

## 4. Decomposition: one causal event per generation

There is no universal peer-reviewed law that every AI clip must be exactly five to eight seconds. Current providers support different ranges. The defensible rule is:

> Use the shortest supported clip that gives one causal event enough visible time to complete, and cut before a new contact mode or mechanism operator begins.

OpenAI’s Sora guide explicitly says shorter clips are followed more reliably and recommends stitching two four-second clips instead of demanding one eight-second clip when reliability matters. It also recommends one clear camera move and one clear subject action per shot [E10]. PhyGenBench’s cause-order findings explain why every additional dependent event raises risk [E3].

### 4.1 Four-clip sling-bag plan

| Clip | Single event | Start predicate | End predicate | Over-all invariants | Preferred carrier |
|---|---|---|---|---|---|
| **A — acquire** | Hand reaches and closes on zipper tab. | Hand separate; bag closed; slider at start. | Stable tab grasp; no slider displacement. | Bag, slider, seam, and panel remain stationary. | First frame plus short motion prompt; first+last if available. |
| **B — translate** | Gripped hand pulls slider from start to end. | Stable tab grasp; seam closed ahead. | Slider at end; seam released behind; panel still closed. | Hand–tab–slider attachment; slider on rail; monotonic travel; no panel self-opening. | **First+last frames strongly preferred.** |
| **C — transfer** | Hand releases tab and grasps the movable panel edge; other hand may support shell. | Slider stopped; seam released; panel closed. | Stable panel-edge grasp and optional support contact. | No panel lift before the new grasp; slider remains at end. | Short clip or authored cut. |
| **D — reveal** | Hands separate/fold panel; gussets expand; cavity is revealed. | Stable panel grasp; closure released. | Panel folded open; gussets expanded; cavity visible; stable final state. | Correct hinge/fold region, persistent contact until support is no longer needed, topology preserved. | First+last frames or a genuine reference transition. |

### 4.2 Last-frame-as-next-first-frame chaining

For each accepted clip:

1. select a clean terminal frame after the operator’s effects have stabilized;
2. use that frame as the next clip’s first frame where the provider supports it;
3. carry forward the symbolic state record separately;
4. re-state only the invariants relevant to the next action;
5. edit at a stable moment, not during contact acquisition or release.

The image carries appearance continuity. The state record carries causal continuity. Neither substitutes for the other.

### 4.3 When to preserve the hard cut

Use the reference’s hard cut when:

- the missing transition is not observed;
- no trustworthy transition reference or endpoint pair exists;
- the product does not require continuous physical motion;
- synthesis would create more unsupported detail than value.

Use continuous synthesis only when the transition is an explicit authored requirement and its generated status is retained.

## 5. Provider-specific prompt compilers

### 5.1 Provider-neutral source contract

Author once in CPCS:

```yaml
shot:
  framing: locked close-up of zipper mechanism and acting hand
  start_state: hand firmly grasps tab; slider at rail start; seam fully interlocked
  event: hand pulls tab and slider continuously along the rail to the end
  end_state: slider stops at end; seam is released behind and interlocked ahead; panel remains down
  invariants:
    - hand, tab, and slider stay attached and co-move
    - slider stays on rail
    - travel never reverses
    - rear shell, panel, handle, and camera stay fixed
    - panel does not lift during this clip
  style: realistic product demonstration, neutral light, shallow but sufficient depth of field
```

Compile that contract to each provider rather than pasting the YAML verbatim.

### 5.2 Veo 3.1

Main prompt:

```text
Locked close-up product-demonstration shot of a sling-bag zipper and one hand.
At the start, the hand already holds the zipper tab and the slider is at the
start of its rail. In one continuous motion, the hand, tab, and slider move
together along the same rail to the end. The slider stays attached and its
progress is steady and one-directional. Teeth are interlocked ahead of the
slider and released only behind it. The front panel remains down throughout.
Neutral soft light, realistic material response, clear mechanism detail.
```

Dedicated `negativePrompt` field:

```text
teleporting slider, detached hand, slider off rail, reversed zipper travel,
self-opening panel, duplicated fingers, merged zipper teeth, changing bag shape
```

Why: Veo’s guide recognizes structured camera/lens/action vocabulary and its API exposes `negativePrompt`. The positive invariants stay in the main prompt because temporal relations are too important to delegate to exclusions [E8][E9].

### 5.3 Sora 2

```text
Locked close-up, shallow depth of field with the complete zipper rail sharp.
One realistic action only.

Beat 1: the hand is already closed around the zipper tab; the slider and bag
are still; the front panel is closed.
Beat 2: the hand pulls the tab steadily along the rail. The hand, tab, and
slider remain attached and move together. The slider never leaves the rail or
reverses. Teeth remain interlocked ahead and separate only after the slider
passes them.
Beat 3: the slider stops at the end. The front panel is still down. Hold the
completed state briefly.

Neutral product lighting, realistic fabric and metal, fixed camera.
```

Use the closed-start image as `input_reference`. Do not invent a separate negative field. If the motion fails, shorten the clip, freeze the camera, simplify the event, or use an edit/reference workflow as the official guide recommends [E10][E11].

Migration note: this API is scheduled to shut down on 2026-09-24 [E11].

### 5.4 Kling VIDEO 3.0

Use first and last frames when the full 3.0 endpoint supports are available. The new API accepts positive and negative descriptions in one prompt [E12].

```text
Locked close-up of one hand pulling a sling-bag zipper. The hand already grips
the tab. Hand, tab, and slider remain attached and move together continuously
along one rail from the first-frame position to the last-frame position. The
motion is steady and one-directional. Teeth stay interlocked ahead of the
slider and release only behind it. The front panel stays closed and stationary
for the entire shot. Avoid a detached hand, an off-rail or teleporting slider,
reverse travel, early seam opening, a self-opening panel, duplicate fingers,
or changing bag geometry.
```

Keep within the documented 3,072-character maximum and preferably within the provider’s 2,500-character recommendation. For Kling 3.0 Turbo, do not compile a last-frame input: the current new API documents first-frame-only control and a 2,500-character prompt cap [E12].

### 5.5 Runway Gen-4.5

For image-to-video, let the image define composition and appearance. Prompt motion in positive language [E13][E14].

```text
The hand, zipper tab, and slider remain firmly attached and move together in
one continuous, steady direction along the existing zipper rail. The slider
stays on the rail. The teeth remain interlocked in front of it and separate
only after it passes. The front panel remains closed and still. The camera is
locked. The action ends with the slider stationary at the rail endpoint.
```

Use Gen-4.5’s first image for the start state, or use the Animate with Keyframes app when both starting and ending frames are required [E15][E16]. Keep API `promptText` within 1,000 UTF-16 code units [E16]. Do not write “not blurry” or “no teleporting” as the primary instruction; Runway’s current guide explicitly recommends the wanted state in positive terms [E14].

## 6. Camera and lens vocabulary

Veo, Sora, Kling, and Runway all expose or document cinematic language to varying degrees. Useful prompt dimensions include:

| Dimension | Examples | Mechanism use |
|---|---|---|
| **Shot size** | extreme close-up, close-up, medium shot, wide shot | Use close-up when contact and joint motion must be judged; include the whole allowed motion path. |
| **Angle** | eye level, overhead, low angle, over-the-shoulder, POV | Choose an angle that keeps contact and the fixed/moving parts visible. |
| **Camera motion** | locked-off, pan, tilt, truck, push-in, tracking, handheld | Locked-off is the diagnostic default. Add at most one camera move after the mechanism is reliable. |
| **Lens / field of view** | macro, wide-angle, telephoto, shallow/deep depth of field | Avoid distortion that makes rail direction or panel geometry ambiguous. Keep the mechanism sharp across its path. |
| **Temporal look** | real time, slow motion, timelapse, single continuous take | Use real time or mild slow motion for causal inspection; avoid timelapse for a contact-critical action. |
| **Lighting / palette** | neutral soft light, high key, low key, warm/cool palette | Use stable light so state changes are not confused with shadows or reflections. |

### Physics-critical camera default

```text
locked close-up; entire mechanism path visible; minimal lens distortion;
stable exposure; no cut; no occlusion at contact acquisition, midpoint, or release
```

“POV, head-locked, ultra-wide fisheye” is valid creative vocabulary and is recognized as a visual/camera description. It is a poor diagnostic view for a small mechanism because perspective distortion and hand occlusion make kinematic verification harder. A practical workflow is:

1. establish the mechanism in a locked, legible close-up;
2. accept a causally valid take;
3. create the stylized POV/fisheye shot as a separate carrier or edit;
4. do not let camera style consume the same generation budget as an already difficult physical transition.

## 7. Verification: reject shortcuts after generation

Prompts are requests. Verification is where CPCS turns a stochastic sample into an accepted artifact.

### 7.1 Causal acceptance gates

| Gate | Required checks | Reject if |
|---|---|---|
| **G0 — initial state** | Correct parts, identities, contacts, joint state, closure state, and camera view exist at the beginning. | Slider or seam is already in the target state; the wrong hand owns the contact; a part is missing. |
| **G1 — cause before effect** | Hand contact precedes slider motion; panel contact precedes panel motion; seam release follows slider passage. | Any effect starts before its causal contact or mechanism state permits it. |
| **G2 — motion law** | Slider remains on rail; progress is qualitatively monotonic; hinge/fold occurs about the permitted region. | Teleportation, reversal, off-axis motion, or joint switching occurs. |
| **G3 — persistence and topology** | Contact identity survives occlusion; hand–tab attachment persists during pull; object identities and topology remain stable. | Hand detaches without release, parts merge, material tears, or an object duplicates/disappears. |
| **G4 — effects / final state** | The intended add/delete effects hold and incompatible old state is gone. | Slider ends correctly but seam remains closed; panel opens but cavity is absent; final state is unstable. |
| **G5 — visual quality** | Natural motion, material response, lighting, composition, and style. | Visual flaws remain after all causal gates pass. |

G0–G4 are hard gates for a mechanism shot. A beautiful G5 result does not rescue a causal failure.

### 7.2 Minimum inspection frames

Inspect at least the observable phases, not an arbitrary frame count:

- pre-action stable frame;
- first contact / grasp frame;
- first mechanism-motion frame;
- one or more mid-motion frames where the joint/contact is visible;
- effect-onset frame;
- terminal stable frame;
- contact-release or transfer frame when present.

If occlusion prevents a claim, record `occluded_unknown`. Do not convert invisibility into evidence of continued contact or absence.

### 7.3 Regeneration diagnosis

| Observed failure | First change to try |
|---|---|
| Effect starts before contact | Split contact acquisition into its own clip; start the next clip with the grasp already established. |
| Slider teleports | Supply matched first/last frames; shorten to slider motion only; lock camera; expose full rail. |
| Hand detaches | Make co-motion the primary positive sentence; reduce occlusion; use a reference transition if available. |
| Panel self-opens | End the zipper clip with the panel explicitly still down; move panel opening to a later operator. |
| Cavity appears incoherently | Anchor the open endpoint; make panel fold/gusset expansion/cavity reveal one dedicated clip; otherwise retain a hard cut. |
| Prompt seems ignored | Remove style clauses and secondary actions; compile to the current provider grammar; check prompt cap and control availability. |

## 8. Compact production playbook

1. **Parse the mechanism.** Parts, connections, affordances, persistent identities, qualitative state.
2. **Choose one operator.** Stop before a contact transfer, joint change, or new effect.
3. **Author the contract.** `pre`, `motion`, `over_all`, `effects_add`, `effects_delete`, `failure_predicates`.
4. **Choose the carrier.** Prefer a genuine transition reference; otherwise matched first+last frames; otherwise first frame plus a short prompt; otherwise an authored hard cut.
5. **Compile per model.** Respect current field semantics, character limits, duration support, and UI/API differences.
6. **Generate variants.** Stochastic generation still requires selection; a prompt is not a proof.
7. **Verify causality before aesthetics.** Apply G0–G5 in order.
8. **Chain state.** Use the accepted terminal frame plus a separate symbolic state handoff.
9. **Preserve lineage.** Mark what is observed, detected, measured, inferred, interpreted, authored, or a creative choice.

### Decision rule

```text
If the reference omits the transition:
  preserve the cut by default.

If continuous motion is required:
  obtain or author boundary evidence,
  split the transition into contact-mode operators,
  use the strongest provider control,
  and verify every causal gate.
```

## 9. Contradictions, limitations, and unanswered questions

### Corrections to the initial working assumptions

- **“The model is a world simulator.”** Too strong. The Sora report presents a path and emerging capabilities while documenting basic physics failures [E1].
- **“`forbid` is the STRIPS delete list.”** Incorrect. Delete effects describe intended facts made false. Forbidden shortcuts belong to invariants or validation [E4][E5].
- **“First/last frames remove the freedom to teleport.”** Too strong. They remove endpoint ambiguity, not path ambiguity.
- **“Kling and Runway have real negative fields; Veo mostly does not.”** Incorrect for the current documented surfaces. Veo has `negativePrompt`; Kling 3.0’s new API combines positive/negative text; Runway Gen-4.5 has no documented negative field and recommends positive phrasing [E9][E12][E14][E16].
- **“Every clip should be five to eight seconds.”** Not a universal rule. Use one causal event and the shortest sufficient duration inside the selected provider’s supported range.
- **“Cinematic defaults are known to come from film/stock captions.”** Not established by the official sources reviewed. The verified fact is that current guides explicitly expose cinematic vocabulary.

### Remaining limitations

- No reviewed provider claims exact hand trajectories, force, contact pressure, collision-free motion, or topology preservation from a text prompt.
- Endpoint frames can conflict with one another or encode a physically unreachable transition.
- Consumer UI controls can differ from API controls and can change without stable versioning.
- Provider prompt rewriters may alter carefully authored constraints.
- Benchmarks evaluate selected prompt sets and model snapshots; their historical scores must not be treated as current provider rankings.
- A monotonic or contact-persistence check from monocular video is an observable judgment, not a measurement of 3D pose or force.
- The best current execution carrier for a particular shot still requires empirical evaluation against the exact model version, plan, region, and UI/API surface used in production.

## Source and evidence registry

Each entry records a short supporting passage or exact documented field, evidence class, limitation, and CPCS impact.

### E1 — Sora technical report

- Source: OpenAI, *Video generation models as world simulators* (2024).
- URL: <https://openai.com/index/video-generation-models-as-world-simulators/>
- Locator: “Discussion” and “Limitations.”
- Supporting passage: “The model does not accurately model the physics of many basic interactions.”
- Evidence class: official technical report and qualitative model disclosure.
- Supports: world-simulator framing is aspirational; basic interaction physics, object-state transitions, long-duration coherence, and spontaneous objects remain failure modes.
- Limitations: the report omits many model/implementation details and does not provide a standardized physics benchmark.
- CPCS concepts affected: provider capability negotiation; failure taxonomy; authority boundary.

### E2 — VideoPhy

- Source: Bansal et al., *VideoPhy: Evaluating Physical Commonsense for Video Generation* (2024).
- URL: <https://arxiv.org/abs/2406.03520>
- Locator: Abstract; §3 benchmark construction; §5 evaluation; §6 fine-grained error analysis.
- Supporting passage: “The best model obtains only 19.7% on the joint metric.”
- Evidence class: primary benchmark paper.
- Supports: physical commonsense and semantic adherence are separable; failure classes include conservation, Newtonian motion, material law, and penetration.
- Limitations: evaluated models and scores are historical and do not rank current versions in this cheat sheet.
- CPCS concepts affected: verification gates; physical failure taxonomy; benchmark selection.

### E3 — PhyGenBench

- Source: Meng et al., *Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation* (PhyGenBench).
- URL: <https://proceedings.mlr.press/v267/meng25c.html>
- arXiv: <https://arxiv.org/abs/2410.05363>
- Locator: Abstract; §3 benchmark; §4 evaluation framework; §5 experiments and analysis.
- Supporting passage: “Physics Order Verification” evaluates whether causal physical events occur in the correct sequence.
- Evidence class: peer-reviewed primary benchmark paper.
- Supports: separate phenomenon detection, causal-order verification, and naturalness; scaling/prompting do not solve dynamic physics.
- Limitations: prompt coverage and evaluated model versions are bounded; benchmark success does not guarantee an articulated hand–object transition.
- CPCS concepts affected: causal verification; sequence decomposition; provider evaluation.

### E4 — STRIPS

- Source: Fikes and Nilsson, *STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving*, IJCAI 1971.
- URL: <https://www.ijcai.org/Proceedings/71/Papers/055.pdf>
- Locator: operator representation and world-model transformation sections.
- Supporting concept: an operator uses preconditions and changes a symbolic world model through add/delete effects.
- Evidence class: foundational primary planning paper.
- Supports: repeatable symbolic action representation.
- Limitations: classical STRIPS does not represent continuous motion, uncertainty, occlusion, contact geometry, or visual failure validators.
- CPCS concepts affected: action preconditions/effects; persistent/transient state; typed operators.

### E5 — PDDL2.1 durative actions

- Source: Fox and Long, *PDDL2.1: An Extension to PDDL for Expressing Temporal Planning Domains*, JAIR 20 (2003).
- URL: <https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume20/fox03a-html/node5.html>
- DOI: <https://doi.org/10.1613/jair.1129>
- Locator: “Durative Actions,” paragraphs defining start, end, and over-all annotations.
- Supporting passage: “All conditions and effects of durative actions must be temporally annotated.”
- Evidence class: peer-reviewed formal-language specification.
- Supports: start conditions, interval invariants, end conditions, and delayed effects.
- Limitations: still not a perception model, deformation solver, or video controller.
- CPCS concepts affected: interaction lifecycle; durative contracts; temporal invariants.

### E6 — Affordances in robotic tasks

- Source: Ardón et al., *Affordances in Robotic Tasks — A Survey* (2020).
- URL: <https://arxiv.org/abs/2004.07400>
- Locator: Abstract and taxonomy of affordance components.
- Supporting passage: “Affordances are key attributes” for an agent interacting with novel objects.
- Evidence class: robotics survey.
- Supports: affordance as a relation among agent capability, object/part, and possible action.
- Limitations: survey taxonomies do not themselves establish a CPCS ontology or video-generation guarantee.
- CPCS concepts affected: object affordance constraints; grasp/action typing; operator preconditions.

### E7 — Integrated robot and scene kinematics

- Source: Jiao et al., *Integration of Robot and Scene Kinematics for Sequential Mobile Manipulation Planning* (accepted by IEEE Transactions on Robotics, 2025).
- URL: <https://arxiv.org/abs/2508.18627>
- Locator: Abstract and tri-level planning framework.
- Supporting passage: the framework models “desired configurations for both the robot and scene elements.”
- Evidence class: primary robotics planning paper.
- Supports: symbolic task sequence plus continuous planning over robot and articulated-scene kinematics.
- Limitations: robot-planning results do not mean a video generator executes the planner or exposes equivalent controls.
- CPCS concepts affected: contact-state transitions; kinematic-chain model; execution-carrier separation.

### E8 — Veo video-generation prompt guide

- Source: Google Cloud, *Video generation prompt guide*.
- URL: <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide>
- Locator: “Anatomy of a prompt,” camera/lens sections, temporal elements, and “Negative prompts.”
- Supporting passage: “Breaking your idea down into key components is the most effective way.”
- Evidence class: current official provider documentation; page last updated 2026-08-07 UTC.
- Supports: Veo prompt grammar and recommended negative-prompt phrasing.
- Limitations: examples and recommendations are not guarantees of causal or physical correctness.
- CPCS concepts affected: provider prompt compiler; camera vocabulary; negative handling.

### E9 — Veo first/last frames and API schema

- Source: Google Cloud, *Generate videos using first and last video frames*; `VideoGenerationModelInstance`; `VideoGenerationModelParams`.
- URLs:
  - <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames>
  - <https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance>
  - <https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelParams>
- Locator: supported models/request body; fields `image`, `lastFrame`, `negativePrompt`, `durationSeconds`, and `task`.
- Supporting field: `lastFrame` is “Image to use as the last frame of the generated video.”
- Evidence class: current official API documentation.
- Supports: first+last-frame carrier, dedicated negative field, and current duration options.
- Limitations: endpoint inputs do not guarantee the path between them; public schema does not state a prompt character cap.
- CPCS concepts affected: provider capability negotiation; anchor-image carrier; negative-field compiler.

### E10 — Sora 2 prompting guide

- Source: OpenAI, *Sora 2 Prompting Guide*.
- URL: <https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide>
- Locator: prompt anatomy, timing and action beats, clip length, image input, and iteration guidance.
- Supporting passage: “Treat your prompt as a wish list, not a contract.”
- Evidence class: current official provider guide; updated 2026-03-12.
- Supports: shorter clips, one clear action/camera move, visible action beats, first-image anchoring, and controlled edits.
- Limitations: recommendations do not produce deterministic output and do not expose a last-frame control.
- CPCS concepts affected: prompt compiler; decomposition; provider authority boundary.

### E11 — Sora 2 Videos API guide and model page

- Source: OpenAI, *Video generation with Sora* and *Sora 2 model*.
- URLs:
  - <https://developers.openai.com/api/docs/guides/video-generation>
  - <https://developers.openai.com/api/docs/models/sora-2>
- Locator: create parameters, image reference, supported seconds, deprecation notice, and model inputs/outputs.
- Supporting passage: the image reference “acts as the first frame of your video.”
- Evidence class: current official API/model documentation.
- Supports: first-frame input, absence of a documented negative/last-frame parameter, current duration options, and deprecation deadline.
- Limitations: absence from the public API schema is not proof about every consumer product surface.
- CPCS concepts affected: migration planning; provider capability negotiation; prompt compiler.

### E12 — Kling VIDEO 3.0 official guide and new API

- Source: Kling AI, *Kling VIDEO 3.0 Model User Guide*; official 3.0/3.0 Turbo API documentation; API updates.
- URLs:
  - <https://kling.ai/quickstart/klingai-video-3-model-user-guide>
  - <https://kling.ai/document-api/api/video/3-0-omni>
  - <https://kling.ai/document-api/api/video/3-0-turbo>
  - <https://kling.ai/document-api/updates/api>
- Locator: capabilities table; Image-to-Video request `contents`; prompt, `first_frame`, `last_frame`, duration, and update notices.
- Supporting field: “The prompt can include positive and negative descriptions.”
- Evidence class: current official provider guide and API documentation.
- Supports: 3.0 first+last frames, Turbo first-only distinction, prompt limits, duration, and current combined prompt semantics.
- Limitations: legacy APIs expose different shapes; the product guide’s quality claims are provider-authored, not independent benchmark findings.
- CPCS concepts affected: provider compiler; endpoint carrier; version-aware capability negotiation.

### E13 — Runway Gen-4.5 model guide

- Source: Runway, *Creating with Gen-4.5*.
- URL: <https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5>
- Locator: “Gen-4.5 spec details,” “Drafting the prompt,” and “Generating and iterating.”
- Supporting passage: image-to-video prompts should focus on “the motion of the scene.”
- Evidence class: current official provider guide.
- Supports: current model, input modes, 2–10 second duration, and prompt focus.
- Limitations: claims of model quality are provider-authored and do not guarantee mechanism physics.
- CPCS concepts affected: Runway prompt compiler; duration selection; execution-carrier choice.

### E14 — Runway positive-phrasing guide

- Source: Runway, *Introduction to Prompting*.
- URL: <https://help.runwayml.com/hc/en-us/articles/46182941379347>
- Locator: “Best practices” → “Use positive phrasing.”
- Supporting passage: models respond better to descriptions of what you want to happen.
- Evidence class: current official provider guidance.
- Supports: positive invariant phrasing and the unreliability of negative wording.
- Limitations: general guidance, not a causal-physics guarantee or API schema.
- CPCS concepts affected: negative-constraint compiler; prompt simplification.

### E15 — Runway current keyframe app

- Source: Runway, *Creating with Apps*.
- URL: <https://help.runwayml.com/hc/en-us/articles/45570040112531-Creating-with-Apps>
- Locator: “Video Generation Apps” → “Animate with Keyframes”; “Apps Tips.”
- Supporting passage: “Configure the starting and ending frames to create smooth transitions between them.”
- Evidence class: current official product documentation.
- Supports: current start/end-frame workflow and replacement for retired Gen-3 keyframes.
- Limitations: the app is a product workflow rather than the Gen-4.5 public API endpoint; availability can depend on plan and UI.
- CPCS concepts affected: keyframe carrier; provider capability negotiation.

### E16 — Runway video API reference

- Source: Runway, *API Reference — Image to video*.
- URL: <https://docs.dev.runwayml.com/api/#tag/Start-generating/paths/~1v1~1image_to_video/post>
- Locator: `model=gen4.5`, `promptText`, `promptImage`, `position`, and `duration`.
- Supporting field: `promptText` is limited to 1–1,000 UTF-16 code units.
- Evidence class: current official API schema.
- Supports: prompt limit, first-frame image semantics, lack of a documented negative field, and 2–10 second duration.
- Limitations: the API schema does not cover every Runway app or consumer UI workflow.
- CPCS concepts affected: API compiler; input validation; current provider matrix.

## Staging note

This document proposes a research-backed production method. It does not establish that any prompt or endpoint pair guarantees exact physics, finger motion, force, topology, or causal correctness. Promotion into curated CPCS truth requires provider-version testing, benchmarked examples, recorded acceptance criteria, and human review.
