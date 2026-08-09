# UG-008 — Articulated and deformable hand–object state transitions for generative video

Research-backed proposal for CPCS validation and human review  
Research date: 2026-08-09 (America/Denver)  
Status: staged research proposal; not curated repository truth

## BLUF and findings

The sling-bag failure is primarily a representation and execution-carrier failure, not merely a weak prompt. The reference establishes a zipper shot and a later open state, but it does not observe the physical bridge between them. A continuous generation was therefore asked to invent contact transfer, seam release, panel motion, gusset deformation, and cavity reveal at once.

The proposed CPCS response is:

1. Represent the object as a typed part–connection graph plus explicit state variables. Rigid articulation, distributed closure, surface deformation, affordances, and observable state must be separate fields. OpenUSD supplies a useful rigid-body vocabulary, while NVIDIA's deformable schema demonstrates why rest shape, simulation topology, collision geometry, and material response cannot be collapsed into one generic “object” label [E1][E2].
2. Compile `open` as a durative causal transition with start conditions, interval invariants, phase effects, end conditions, and named failure states. This follows the useful formal distinction in PDDL2.1 between start, over-all, and end conditions/effects, without adopting PDDL as CPCS's storage format [E3].
3. Track contacts as identity-bearing, time-bounded hypotheses. Monocular RGB can support observed or detected contact evidence, but it does not by itself measure contact force, depth, or exact 3D finger trajectories. Datasets that report accurate 3D contact use additional capture instrumentation or multi-view supervision [E5][E6].
4. Verify the transition with action-specific predicates, not a generic “looks plausible” score. Required checks include causal order, closure release, panel displacement, contact persistence, gusset expansion, cavity reveal, topology preservation, and a consistent final state. Generic video benchmarks remain useful secondary quality checks but do not prove this task's causal success [E7][E8][E9].
5. Preserve an authored hard cut when the source uses one. The intermediate physical stages may be omitted from the depiction, but they must not be claimed as observed or measured. If a continuous opening is required, compile it as a new authored span and prefer a carrier that constrains both boundaries or supplies the missing motion: first/last frames, a genuine transition reference video, composition/depth guidance, an edited source clip, or provider-supported tracks/masks [E10]–[E14].

For UG-008, the default recommendation is:

`zipper shot → hard cut → verified open-state shot`

Use continuous synthesis only when the product requirement explicitly rejects the cut. In that case, request or author additional evidence for the missing transition and mark the result as generated, not recovered from the reference.

### Epistemic status contract

CPCS should never flatten the following statuses into a single “fact” field:

| Status | Meaning | Permitted example |
|---|---|---|
| `observed` | A reviewer can directly see it in the source or output. | “The slider changes image position.” |
| `detected` | An algorithm produced a label, mask, keypoint, or track. | “Tracker H-L remains associated with the left hand.” |
| `measured` | A calibrated sensor, benchmark annotation, or explicit provider contract establishes a quantity. | “This dataset frame has a MoCap-derived mesh.” |
| `inferred` | A latent state is the best explanation of evidence but is not directly visible. | “The hidden seam is probably released.” |
| `interpreted` | A semantic judgment maps evidence to a concept. | “The motion is an opening action.” |
| `authored` | CPCS or a human intentionally specifies structure or behavior. | “Panel separation must precede cavity reveal.” |
| `creative_choice` | An intentionally invented visual or physical detail. | “The left hand takes over the flap after the cut.” |

Every assertion should also carry `source_refs`, a frame/time span, subject identity, and `visibility = visible | occluded | out_of_frame | unknown`. `Occluded` is not equivalent to `absent`, and `unknown` is not equivalent to `false`.

## Source and evidence registry

Each entry below records the material claim it supports. Quoted passages are deliberately short; the linked source and locator are authoritative.

### E1 — OpenUSD Physics schema

- Source: Alliance for OpenUSD, *UsdPhysics: USD Physics Schema*.
- URL: <https://openusd.org/release/api/usd_physics_page_front.html>
- Locator: “Rigid Body Simulation Primer,” “Rigid Bodies,” “Joints,” and “Articulations.”
- Supporting passage: “Constraints describe physical limits between bodies.”
- Evidence class: official technical schema/documentation.
- Supports: separate bodies, colliders, physical materials, contacts, joints, joint frames, limits, and articulations.
- Limitations: the documented baseline is rigid-body oriented; it is a representation precedent, not evidence that a video model simulates these dynamics.
- CPCS concepts affected: object affordance constraints; persistent object state; typed object-part graph; topology preservation.

### E2 — NVIDIA Omni Physics deformable bodies

- Source: NVIDIA, *Deformable Bodies — Omni Physics*.
- URL: <https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/deformables/deformable_bodies.html>
- Locator: “Surface Deformable Hierarchy,” “Volume Deformable Hierarchy,” and “Create and Assign Materials.”
- Supporting passage: “Physics materials define how a deformable body’s volume reacts to external forces.”
- Evidence class: official implementation documentation.
- Supports: explicit rest shape, simulation mesh, collision mesh, render geometry, mass, material response, and surface/volume distinction.
- Limitations: PhysX/Omni Physics implementation details are not a universal CPCS ontology; cloth-like bags need validation against the selected solver or generator.
- CPCS concepts affected: material behavior; deformable topology; provider capability negotiation; execution-carrier selection.

### E3 — PDDL2.1 durative-action semantics

- Source: Maria Fox and Derek Long, *PDDL2.1: An Extension to PDDL for Expressing Temporal Planning Domains*, JAIR 20 (2003).
- URL: <https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume20/fox03a-html/node5.html>
- DOI: <https://doi.org/10.1613/jair.1129>
- Locator: “Durative Actions,” especially the paragraphs defining start, end, and over-all annotations.
- Supporting passage: “All conditions and effects of durative actions must be temporally annotated.”
- Evidence class: peer-reviewed primary research/formal language specification.
- Supports: phase-aware preconditions, interval invariants, delayed effects, and explicit temporal ordering.
- Limitations: PDDL2.1 exposes only restricted time points and does not model perception uncertainty, contact geometry, or deformable physics by itself.
- CPCS concepts affected: interaction lifecycle; action preconditions and effects; causal transition schema.

### E4 — BEHAVIOR/BDDL object states and transition rules

- Source: Stanford Vision and Learning Lab, *BEHAVIOR — Important Concepts*.
- URL: <https://behavior.stanford.edu/getting_started/important_concepts.html>
- Locator: “Tasks,” “Objects,” “Transition Rules,” and “BDDL.”
- Supporting passage: “They specify input and output synsets, conditions for transitions.”
- Evidence class: official benchmark and simulator documentation.
- Supports: symbolic initial/goal conditions, object abilities, articulated metadata, and explicit transition rules.
- Limitations: BEHAVIOR targets embodied-agent simulation; its rules are not video-generation guarantees and may abstract away visually important intermediate motion.
- CPCS concepts affected: affordances; preconditions/effects; persistent and transient state; verification predicates.

### E5 — ARCTIC bimanual articulated hand–object dataset

- Source: Fan et al., *ARCTIC: A Dataset for Dexterous Bimanual Hand-Object Manipulation*, CVPR 2023.
- URL: <https://arxiv.org/abs/2204.13662>
- Locator: Abstract; §1; §3.1 “Data Characteristics”; §4 “Evaluation Protocol.”
- Supporting passage: “hand poses and object states evolve jointly in time.”
- Evidence class: peer-reviewed primary dataset and benchmark paper.
- Supports: joint temporal modeling of two hands, articulated objects, contact, articulation, relative position, and motion consistency.
- Limitations: ARCTIC objects are modeled as two rigid parts with a one-dimensional articulation; it does not cover a multi-part deformable zipper bag directly. Its 3D annotations use synchronized multi-view and MoCap capture, not monocular RGB alone.
- CPCS concepts affected: bimanual ownership; contact persistence; object articulation; verification by contact/motion consistency.

### E6 — ContactPose contact ground truth

- Source: Brahmbhatt et al., *ContactPose: A Dataset of Grasps with Object Contact and Hand Pose*, ECCV 2020.
- URL: <https://arxiv.org/abs/2007.09545>
- DOI: <https://doi.org/10.1007/978-3-030-58601-0_22>
- Locator: Abstract and §3 “Dataset Acquisition.”
- Supporting passage: “contact is represented as a contact map on the object mesh surface.”
- Evidence class: peer-reviewed primary dataset paper.
- Supports: contact should be a localized relation with provenance, not a free-text claim.
- Limitations: contact is captured with thermal and RGB-D instrumentation and the dataset emphasizes static grasps; it does not establish contact force or dynamic bag-opening trajectories from monocular video.
- CPCS concepts affected: contact evidence class; palm/finger regions; measured versus detected contact.

### E7 — TAP-Vid tracking benchmark

- Source: Doersch et al., *TAP-Vid: A Benchmark for Tracking Any Point in a Video*, NeurIPS 2022.
- URL: <https://arxiv.org/abs/2211.03726>
- Locator: Abstract; §3 “The TAP-Vid Benchmark”; evaluation metrics.
- Supporting passage: “real-world videos with accurate human annotations of point tracks.”
- Evidence class: peer-reviewed primary benchmark paper.
- Supports: identity-bearing tracks and explicit visibility/occlusion evaluation are separable from semantic contact.
- Limitations: a 2D point track does not prove 3D contact, object ownership, force, or topology.
- CPCS concepts affected: contact identity across occlusion; visibility is not existence; track-based verification.

### E8 — VBench general video-generation evaluation

- Source: Huang et al., *VBench: Comprehensive Benchmark Suite for Video Generative Models*, CVPR 2024.
- URL: <https://arxiv.org/abs/2311.17982>
- Locator: Abstract and §3 benchmark dimensions.
- Supporting passage: “VBench comprises 16 dimensions in video generation.”
- Evidence class: peer-reviewed primary benchmark paper.
- Supports: subject consistency, temporal flicker, motion smoothness, and related quality checks are multidimensional.
- Limitations: its generic dimensions do not certify seam release, correct contact transfer, cavity reveal, or bag topology.
- CPCS concepts affected: secondary video-quality verification; failure taxonomy.

### E9 — PhyGenBench physical-commonsense evaluation

- Source: Meng et al., *Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation*, ICML 2025.
- URL: <https://proceedings.mlr.press/v267/meng25c.html>
- Locator: Abstract; benchmark and evaluation-method sections.
- Supporting passage: “evaluate physical commonsense correctness in T2V generation.”
- Evidence class: peer-reviewed primary benchmark paper.
- Supports: visual quality and physical commonsense are distinct evaluation targets.
- Limitations: broad physical-commonsense evaluation does not replace an object-specific causal contract or calibrated contact measurement.
- CPCS concepts affected: physics-aware verification; separation of plausibility from causal success.

### E10 — Google Veo first/last-frame generation

- Source: Google Cloud, *Generate videos using first and last video frames*.
- URL: <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames>
- Locator: page introduction and “Create a video from first and last frames.”
- Supporting passage: “specifying the first and last frames of the video.”
- Evidence class: official provider documentation, last updated 2026-08-07 UTC when researched.
- Supports: a provider carrier can constrain both boundary states.
- Limitations: boundary images do not guarantee the causal correctness of the invented intermediate motion.
- CPCS concepts affected: provider capability negotiation; anchor-image carrier; postcondition conditioning.

### E11 — Google Veo asset/style reference images

- Source: Google Cloud, *Guide video generation using asset and style images*.
- URL: <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/use-reference-images-to-guide-video-generation>
- Locator: “Veo,” “Subject image,” and “Style image.”
- Supporting passage: “Veo preserves the subject’s appearance in the output video.”
- Evidence class: official provider documentation, last updated 2026-08-07 UTC when researched.
- Supports: identity/style references are different control semantics from first/last state anchors.
- Limitations: subject appearance preservation is not part tracking, contact control, or topology enforcement.
- CPCS concepts affected: carrier semantics; subject identity; capability negotiation.

### E12 — Runway Gen-4.5 input controls

- Source: Runway, *Creating with Gen-4.5*.
- URL: <https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5>
- Locator: Introduction; “Gen-4.5 spec details”; “Step 2 — Drafting the prompt.”
- Supporting passage: “currently offers Text to Video and Image to Video control.”
- Evidence class: official provider documentation.
- Supports: text and initial-image conditioning, with image-to-video prompts focused on motion.
- Limitations: the cited interface does not itself establish mask, depth, hand-track, or object-part-track inputs; provider capabilities must be re-queried at execution time.
- CPCS concepts affected: provider capability negotiation; first-frame carrier; prompt compilation.

### E13 — Runway Edit Studio / Aleph 2.0

- Source: Runway, *Creating with Edit Studio*.
- URL: <https://help.runwayml.com/hc/en-us/articles/51683104370451-Creating-with-Edit-Studio>
- Locator: introduction; “Step 2 — Uploading your video”; “Step 3 — Choosing an editing mode.”
- Supporting passage: “transform existing traditional or generated footage using simple prompts.”
- Evidence class: official provider documentation.
- Supports: source-video editing and selected-keyframe edits as a distinct carrier from de novo generation.
- Limitations: an edit can preserve source timing better than text-only generation but still does not guarantee contact physics or topology.
- CPCS concepts affected: video-editing carrier; source preservation; execution-carrier selection.

### E14 — Adobe Firefly composition-reference video

- Source: Adobe, *Use video as composition reference*.
- URL: <https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/use-video-as-composition-reference.html>
- Locator: introduction; upload instructions; note beneath the Composition section.
- Supporting passage: “the arrangement of edges, depth, and composition.”
- Evidence class: official provider documentation, updated 2026-06-16 when researched.
- Supports: a reference-video carrier can transfer structural/compositional cues beyond text.
- Limitations: Adobe states that Composition is unavailable when an image keyframe has been added; composition transfer is not a guarantee of exact hand contact or material dynamics.
- CPCS concepts affected: provider combinability constraints; reference-video carrier; depth/composition guidance.

## Typed object-part and articulation schema

### Minimal representation

The smallest useful representation is not a full physics scene. It is a typed graph that can express what must persist, what may move, how it may move, what affords interaction, and what can be checked.

```yaml
ObjectModel:
  id: EntityId
  class: SemanticType
  parts: [Part]
  regions: [Region]
  connections: [Connection]
  affordances: [Affordance]
  state_variables: [StateVariable]
  evidence_refs: [EvidenceRef]

Part:
  id: PartId
  role: SemanticRole
  body_model: rigid | articulated_rigid | surface_deformable |
              volume_deformable | distributed_closure | unknown
  rest_representation: mesh_ref | contour_ref | mask_ref | unknown
  visible_representation: appearance_ref | mask_ref | unknown
  material_behavior:
    class: rigid | flexible | foldable | stretchable | compressible | unknown
    parameters: optional          # only measured or authored with lineage
  persistence: persistent | consumable | transient
  observables: [ObservableId]

Region:
  id: RegionId
  role: interior_cavity | opening | exterior | other
  bounded_by: [PartId]
  existence: persistent | transient
  visibility_state: visible | occluded | enclosed | out_of_frame | unknown

Connection:
  id: ConnectionId
  a: PartId
  b: PartId
  kind: fixed | revolute | prismatic | flexure | seam | zipper_path |
        fold_line | attachment | distributed_constraint | unknown
  permitted_motion: qualitative_constraint | measured_range | unknown
  closure_state: engaged | partially_engaged | released | unknown
  topology_rule: must_persist | may_release | may_break | unknown

Affordance:
  id: AffordanceId
  target: PartId | ConnectionId | RegionId
  action: grasp | pinch | pull | slide | support | separate | fold | release
  contact_regions: [SemanticContactRegion]
  preconditions: [Predicate]
  effects: [Predicate]

StateVariable:
  id: StateId
  domain: finite_enum | ordered_enum | boolean | qualitative_scalar |
          measured_scalar
  value: any | unknown
  epistemic_status: observed | detected | measured | inferred |
                    interpreted | authored | creative_choice
  source_refs: [EvidenceRef]
  valid_span: TimeSpan
```

Design rules:

- `Part`, `Connection`, and `Region` are different node types. The cavity exists while enclosed; lack of visibility does not delete it.
- A zipper is not one scalar object. Its slider is a rigid moving part; the teeth/seam are a distributed closure connection; the released opening is a changing region boundary.
- A deformable panel needs a rest representation and a topology rule even if CPCS never stores Young's modulus or other solver parameters. Numeric material properties remain `unknown` unless measured or authored for a specific execution system [E2].
- Qualitative permitted motion is valid when monocular evidence cannot recover a calibrated range. CPCS should store “panel may fold away from rear shell along attached boundary,” not invent an angle.
- The rendered appearance, collision/simulation representation, and semantic identity must be allowed to differ. This follows the separation used in physics schemas, but CPCS need only retain the levels required by its compiler and verifier [E1][E2].

### Sling-bag instance

| Entity | Type and role | Connection/behavior | Key state variables | Observable evidence |
|---|---|---|---|---|
| `bag.rear_shell` | `surface_deformable`; structural base | attached to gussets and panel boundary | pose; deformation class; support status | persistent contour/texture; relative pose |
| `bag.front_panel` | `surface_deformable`; movable flap/panel | attached along intended boundary; closure along seam | `panel_relation = closed/aligned/separating/folded_open` | panel mask, rim displacement, fold silhouette |
| `bag.zipper_slider` | `rigid`; closure actuator | constrained to `zipper_path` | path progress as qualitative/observed unless measured | slider track and direction |
| `bag.closure_seam` | `distributed_closure` | couples front panel to rear shell while engaged | `engaged/partial/released/unknown` | seam continuity and separation |
| `bag.top_handle` | flexible appendage | permanently attached to shell | pose; visibility | identity-preserving track; not an opening actuator by default |
| `bag.side_gussets` | `surface_deformable`; expansion structure | attached to shells/panel; folds and expands | `collapsed/expanding/expanded/unknown` | side-width/contour change and fold pattern |
| `bag.interior_cavity` | persistent `Region` | bounded by rear shell, panel, gussets, opening rim | `enclosed/partly_visible/visible/unknown` | interior-labeled region with correct occlusion boundary |
| `hand.left` | articulated actor effector | dynamic contact edges | owner, contact region, support role, visibility | hand identity track and contact hypothesis |
| `hand.right` | articulated actor effector | dynamic contact edges | owner, contact region, support role, visibility | hand identity track and contact hypothesis |

Required persistent topology:

```text
rear_shell --attached_to--> side_gussets --attached_to--> front_panel
rear_shell --closure_path--> closure_seam --closure_of--> front_panel
zipper_slider --constrained_to--> closure_seam/path
interior_cavity --bounded_by--> rear_shell, front_panel, side_gussets
```

The closure relation may change from engaged to released. The structural attachment of the gussets and intended panel boundary must persist. A generated panel that detaches, duplicates, merges with a hand, or changes identity violates topology even if the final frame resembles an open bag.

## Causal action and state-transition schema

### Generic durative action type

```yaml
ActionTransition:
  id: ActionId
  verb: open
  actors: [EntityId]
  patient: EntityId
  depiction_mode: continuous | segmented | editorial_ellipsis
  preconditions: [Predicate]
  phases: [Phase]
  interval_invariants: [Predicate]
  postconditions: [Predicate]
  failure_states: [FailureStateId]
  required_observations: [CheckId]
  carrier_requirements: [Capability]
  provenance: [EvidenceRef]

Phase:
  id: PhaseId
  entry_conditions: [Predicate]
  required_contacts: [ContactRequirement]
  permitted_changes: [TypedEffect]
  forbidden_changes: [Predicate]
  exit_conditions: [Predicate]
```

This schema borrows the useful start/interval/end distinction from durative-action formalisms [E3] and the initial/goal/transition-rule separation used by BEHAVIOR [E4]. CPCS adds perception provenance, phase-level contacts, carrier requirements, and failure states because a video compiler must reason about both depiction and uncertain evidence.

### Sling-bag causal sequence

| Stage | Preconditions and contact | Permitted effect | Required observable result |
|---|---|---|---|
| `S0 closed` | panel aligned with rear shell; seam engaged; cavity enclosed | none | closed seam and no claimed cavity visibility |
| `A1 slider moves` | a hand contacts the slider; slider is on the closure path | slider progresses along path | slider identity and directed path motion persist |
| `S1 seam releasing` | slider movement remains causally associated with closure | engaged portion decreases; released portion may grow | released seam region follows, rather than precedes, slider progress |
| `S2 seam released` | closure is released sufficiently for panel motion; exact amount may be unknown | panel becomes separable without tearing | visible seam separation or `unknown` if occluded; never silently “measured” |
| `A2 contact transfer` | at least one hand can reach an affordance on the panel; the other may support shell/bag | contact episode on slider ends or changes role; panel-control contact begins | explicit old-contact termination and new-contact identity |
| `S3 panel controlled` | panel has an owning/manipulating hand; bag is supported | panel may separate while attached at intended boundary | hand and panel co-move through the contact episode |
| `A3 panel separates and folds` | closure released; permitted attachment/fold constraints preserved | panel relation changes through separating to folded/open | increasing visible gap; panel displacement; no teleportation or detachment |
| `A4 gussets expand` | panel separation creates space; gussets remain attached | gusset state changes collapsed → expanding → expanded | coherent side contour/fold change |
| `S6 cavity becomes visible` | opening geometry exposes the persistent cavity | cavity visibility changes enclosed → partly visible → visible | interior region appears behind a stable opening rim and correct occlusion order |
| `S7 stable open` | panel open, seam released, topology intact, contacts supported or cleanly released | transient motion settles into final configuration | end interval satisfies all open-state predicates consistently |

Interval invariants for a continuous depiction:

- left/right hand identities remain distinct;
- bag-part identities persist through occlusion;
- the interior cavity continues to exist while invisible;
- only declared connections may release;
- panel motion remains compatible with its attachments;
- a contacting hand and its controlled part have compatible motion while the contact episode is active;
- unsupported object motion is not asserted as caused by a hand;
- all status changes retain evidence lineage.

### Hard-cut semantics

The source cut may compile as:

```yaml
- shot: zipper_closeup
  terminal_state: slider_moving | seam_state_unknown
- transition: hard_cut
  semantics: editorial_ellipsis
  unobserved_physical_span:
    - seam_release_completion
    - contact_transfer_to_panel
    - panel_separation_and_fold
    - gusset_expansion
    - cavity_reveal_transition
- shot: bag_open
  initial_state: stable_open_observed_or_interpreted
```

These stages are skipped only in the depiction. They are not removed from the causal model, and CPCS must not synthesize a hidden trajectory, contact assignment, or material measurement. The post-cut open state can be observed independently; the path between shots remains `unobserved` unless another source supplies it.

If a deliverable requires continuous motion, `editorial_ellipsis` must be replaced with an `authored` transition span. That span needs its own carrier and verification contract. Any invented hand assignment, fold shape, or timing is `creative_choice`, not recovered reference truth.

## Hand-contact and occlusion representation

### Contact episode

```yaml
ContactEpisode:
  id: ContactId
  hand_id: hand.left | hand.right
  hand_region: thumb | index | fingers | palm | wrist | unknown
  target_entity: PartId | ConnectionId
  target_region: SemanticRegion | track_ref | unknown
  role: manipulate | support | stabilize | guide | incidental | unknown
  state: candidate | active | occluded_active | released | contradicted | unknown
  start_evidence: [ObservationRef]
  persistence_evidence: [ObservationRef]
  end_evidence: [ObservationRef]
  epistemic_status: observed | detected | inferred | measured
  ownership: manipulator | supporter | shared | unknown
```

Rules:

1. Contact is an edge between a named hand region and a named object part/region, not a property of a whole frame.
2. `active` may be observed from visible adjacency plus co-motion; it remains a contact hypothesis unless measured by instrumented data. ContactPose illustrates that contact ground truth requires a dedicated acquisition method [E6].
3. When contact becomes occluded, transition to `occluded_active` if identity and motion evidence support persistence. Do not terminate the episode merely because pixels disappear. TAP-Vid supports the general separation between point identity and visibility, while ARCTIC documents the severity of occlusion in dexterous interaction [E5][E7].
4. `ownership` is task-semantic. One hand may manipulate the panel while the other supports the rear shell. Ownership can transfer, but the transfer needs explicit end/start evidence.
5. Palm, finger, and pinch contacts can be semantically labeled even when exact surface coordinates are unavailable. Exact vertices, distances, forces, or pressure remain `unknown` unless a calibrated source establishes them.
6. A release is an event with evidence. It is not inferred solely from a later distant hand if a cut or occlusion intervenes.

### Monocular-safe assertions

Allowed without calibration:

- 2D adjacency, overlap, or separation as `observed`/`detected`;
- hand and part identity tracks with visibility states;
- qualitative co-motion or relative motion;
- semantic contact hypotheses and support/manipulation roles;
- phase order and visible state changes;
- qualitative opening, folding, or expansion.

Not allowed as measurements from ordinary monocular video:

- exact 3D contact point or trajectory;
- force, pressure, friction, stiffness, or material modulus;
- metric depth or displacement;
- invisible finger configuration;
- precise joint limits;
- physical topology behind an occluder;
- a claim that a prompt enforces any of the above.

ARCTIC's accurate 3D meshes and dynamic contact use synchronized multi-view and MoCap capture; ContactPose uses thermal/RGB-D acquisition [E5][E6]. Those sources justify a conservative authority boundary for monocular CPCS evidence.

## Verification requirements and failure taxonomy

### Verification result type

Every check returns:

```text
pass | fail | unknown | not_applicable
```

`unknown` is mandatory when occlusion, a cut, insufficient resolution, or unsupported sensing prevents a decision. CPCS must not invent numeric tolerances. A threshold may be added only when a source, provider contract, benchmark, calibrated measurement, or reviewed project specification establishes it.

### Required checks

| Check | Pass condition | Failure signal | Evidence status |
|---|---|---|---|
| `V1 causal_order` | slider motion precedes associated seam release; release precedes panel separation; separation precedes cavity reveal | effect appears before cause or multiple stages collapse into an impossible morph | observed/interpreted |
| `V2 seam_release` | the closure relation changes from engaged toward released along the intended seam | slider moves but seam stays closed, crosses geometry, or releases elsewhere | observed/detected; may be unknown under occlusion |
| `V3 contact_transfer` | slider contact ends/changes role and a named hand begins a panel-control episode | hand identity swaps, contact jumps, or panel moves with no supported owner | detected/inferred |
| `V4 contact_persistence` | active contact has consistent identity and compatible hand/part motion until release | slipping, interpenetration, merge, unexplained gap, or ownership flicker | detected/inferred; measured only with suitable ground truth |
| `V5 panel_displacement` | the panel separates from the rear shell while preserving intended attachment/fold constraints | panel remains glued, teleports, detaches, duplicates, or changes identity | observed/detected |
| `V6 gusset_expansion` | side gusset contour/fold state changes coherently with panel opening | gussets remain collapsed, vanish, or inflate independently | observed/interpreted |
| `V7 cavity_visibility` | an interior-labeled region becomes visible behind a coherent opening boundary | a dark texture patch is mistaken for a cavity; interior appears before opening | observed/interpreted |
| `V8 topology_preservation` | persistent parts and required attachments remain; only the closure releases | tearing, part-count change, merge, duplication, or forbidden disconnection | detected/interpreted |
| `V9 final_state_consistency` | an end span simultaneously satisfies released seam, open panel, expanded/compatible gussets, visible cavity, intact topology | final frame contains mutually inconsistent predicates | observed/interpreted |
| `V10 editorial_truth` | a hard cut labels the hidden span unobserved and verifies shots separately | the report claims the cut contains a recovered physical transition | provenance audit |

For contact verification, ARCTIC's Contact Deviation and Motion Deviation motivate checking both spatial compatibility and co-motion during a stable contact episode [E5]. CPCS should not copy ARCTIC's numeric thresholds into UG-008 because the source and output do not share ARCTIC's mesh ground truth.

Point/part tracks can help verify persistence and occlusion handling [E7]. VBench-style subject consistency, motion smoothness, and flicker checks can detect generic video defects [E8]. PhyGenBench-style physical-commonsense evaluation can add a broader plausibility signal [E9]. None substitutes for `V1`–`V10`.

### Failure taxonomy

| Code | Failure | Description |
|---|---|---|
| `F-EPISTEMIC-OVERCLAIM` | unobserved-as-observed | A hard-cut span or occluded state is reported as recovered fact. |
| `F-ORDER` | causal inversion | Cavity, panel, or seam state changes appear before their enabling actions. |
| `F-SEAM-NORELEASE` | actuator/effect decoupling | Slider moves but the distributed closure does not release coherently. |
| `F-CONTACT-DROP` | premature loss | A required manipulation/support contact disappears before its phase effect completes. |
| `F-CONTACT-SWAP` | identity/ownership swap | Left/right hand or contacted-part identity changes without a transfer event. |
| `F-CONTACT-PENETRATION` | invalid geometry | Hand and object visibly merge or pass through each other. |
| `F-PANEL-TELEPORT` | unsupported displacement | Panel changes pose without compatible contact or permitted connection motion. |
| `F-GUSSET` | deformation inconsistency | Gussets fail to expand, vanish, or change independently of the opening. |
| `F-FALSE-CAVITY` | appearance-only interior | A dark patch suggests depth without a coherent rim, occlusion order, or part state. |
| `F-TOPOLOGY` | structural mutation | Persistent parts detach, duplicate, merge, tear, or change connection illegally. |
| `F-OCCLUSION-DELETION` | visibility/existence collapse | A hidden hand, part, or cavity ceases to exist or returns with new identity. |
| `F-POSTCONDITION` | unstable/inconsistent open state | The final shot fails one or more required open predicates. |
| `F-CARRIER-MISMATCH` | inadequate control surface | CPCS selects text or appearance reference when the task requires motion, topology, or state-boundary control. |

## Provider-control carrier decision matrix

Carrier selection should be capability-based, not provider-name-based. Provider/model/version and control combinability are volatile and must be re-queried immediately before execution.

| Carrier | Select when | What it constrains | Main limitation | UG-008 decision |
|---|---|---|---|---|
| Text only | action is simple, fully observed, and low-risk | semantics and broad motion intent | weak binding to contacts, parts, topology, and final geometry | Reject for continuous opening; acceptable only to describe already anchored shots |
| Single first-frame image | starting appearance and composition are the main constraints | initial state, identity, composition | final open state and intermediate causality remain invented | Insufficient alone |
| First + last frame anchors | both boundary states are known and a continuous bridge is required | initial and terminal appearance/state | transition path still not guaranteed | Preferred minimum continuous carrier [E10] |
| Asset/subject/style references | identity or style drift is the main risk | subject appearance or style | does not encode contact, articulation, or state transition | Supplementary only [E11] |
| Genuine reference transition video | a correct analogous opening motion can be captured | timing, composition, part motion, occlusion pattern | analogy may mismatch bag geometry; exact transfer semantics depend on provider | Strongest generative reference if available |
| Composition/depth reference video | provider accepts structural video guidance | edges, depth organization, layout, possibly camera path | may conflict with keyframe controls; not physical simulation | Strong option when a complete transition reference exists [E14] |
| Masks | local edits or protected regions are needed and the provider contract accepts temporal masks | spatial edit scope and protected regions | mask identity through occlusion may still fail | Use for seam/panel isolation only if supported |
| Depth | spatial ordering and cavity geometry dominate and calibrated/estimated depth is available | coarse geometry and occlusion order | depth does not encode contact ownership or topology | Useful supplement, not sufficient |
| Pose/hand tracks | human motion must follow an observed performance and provider accepts the control | hand/body trajectory | pose does not prove hand–object contact or deformable response | Use only with part/interaction controls |
| Object-part tracks | part identity and relative motion are the main risks and the interface accepts tracks | panel, slider, seam, gusset trajectories | cannot guarantee material behavior by itself | High-value control if available |
| Segmented clips + hard cut | reference intentionally omits the transition or continuity is unnecessary | truthful shot boundaries and per-shot states | no continuous opening is depicted | Default for this reference |
| Video editing | source footage contains useful timing/structure that should be preserved | source motion and selected-frame edits | generated edits can still violate contacts/topology | Prefer over de novo generation when suitable footage exists [E13] |
| 3D/simulation render | physics-critical motion must be explicitly authored and a renderer/reference interface is available | topology, joints, contacts, camera, state path | higher production cost; solver/material calibration still required | Escalation path for exact continuous opening |

### Provider examples verified during this research

- Google documents Veo generation from both first and last frames [E10]. This is the clearest documented boundary-state carrier for a continuous UG-008 attempt, but the intermediate sequence still requires CPCS verification.
- Google's asset/style reference interface targets appearance and style semantics [E11]. CPCS must not treat those images as part tracks or contact controls.
- Runway Gen-4.5 documents Text-to-Video and Image-to-Video controls, with image-to-video prompts focused on motion [E12]. Its cited page does not establish the stronger controls UG-008 needs.
- Runway Edit Studio uses an existing video and a selected keyframe edit, making it a better carrier when useful source timing already exists [E13].
- Adobe Firefly documents a composition-reference video that transfers edge/depth/composition structure, but the same page says this control is unavailable when an image keyframe has been added [E14]. CPCS capability negotiation must therefore include combinations, not just individual features.

### Capability contract

```yaml
ProviderCapabilitySnapshot:
  provider: string
  model: string
  model_version: string
  checked_at: timestamp
  documentation_refs: [URL]
  inputs:
    text: supported | unsupported | unknown
    first_frame: supported | unsupported | unknown
    last_frame: supported | unsupported | unknown
    reference_video: supported | unsupported | unknown
    composition_depth: supported | unsupported | unknown
    temporal_masks: supported | unsupported | unknown
    pose_or_hand_tracks: supported | unsupported | unknown
    object_part_tracks: supported | unsupported | unknown
    source_video_edit: supported | unsupported | unknown
  combinations:
    - inputs: [Capability]
      status: supported | conflicting | unknown
      source_ref: EvidenceRef
  semantics:
    - capability: Capability
      controls: appearance | boundary_state | composition | camera |
                edit_scope | trajectory | unknown
  guarantees:
    exact_contact: false_or_not_documented
    deformable_physics: false_or_not_documented
    topology_preservation: false_or_not_documented
```

Selection rule:

```text
if source uses a hard cut and continuous motion is not required:
    compile segmented shots + editorial_ellipsis
else if a real complete transition clip exists:
    prefer source-video edit or structural reference-video control
else if closed and open anchors exist:
    require first+last boundary support; add any accepted tracks/masks/depth
else:
    request new reference capture or author a 3D/simulation transition

if no carrier exposes the controls required by the verification contract:
    do not claim the continuous transition is reliably executable
```

## Proposed CPCS concepts, mappings, and typed edges

All items in this section are proposals and remain staged.

### Proposed concepts

| Proposed concept | Purpose | Maps to existing CPCS concepts |
|---|---|---|
| `ObjectPartGraph` | persistent typed parts, regions, and connections | object affordance constraints; persistent object state |
| `DistributedClosure` | zipper/seam whose state changes along a path | articulation; affordance constraints |
| `DeformationClass` | qualitative material behavior without invented parameters | object affordance constraints; provider negotiation |
| `VisibilityState` | visible/occluded/enclosed/out-of-frame/unknown independent of existence | visibility is not existence |
| `ContactEpisode` | identity-bearing hand-region ↔ part relation over time | contact identity across occlusion; interaction lifecycle |
| `ContactOwnership` | manipulator/supporter/shared/unknown role | bimanual lifecycle; support and release |
| `StateAssertion` | value + epistemic status + time span + provenance | persistent/transient state; action effects |
| `DurativeInteractionPhase` | phase preconditions, interval invariants, effects, failures | interaction lifecycle; action preconditions/effects |
| `EditorialEllipsis` | explicit unobserved physical span hidden by a cut | visibility is not existence; provenance boundary |
| `VerificationContract` | action-specific observable predicates with pass/fail/unknown | provider negotiation; execution validation |
| `CarrierCapabilitySnapshot` | versioned provider controls and combination constraints | provider capability negotiation |
| `CarrierRequirement` | controls demanded by a transition before provider selection | execution-carrier selection |

### Typed edges

```text
ObjectPart       -[part_of]->                 Object
Region           -[bounded_by]->              ObjectPart
ObjectPart       -[connected_to]->            ObjectPart
DistributedClosure-[closure_of]->             ObjectPart
ObjectPart       -[affords]->                 Action
HandRegion       -[contact_with]->            ObjectPart
Hand             -[supports]->                ObjectPart
Hand             -[manipulates]->             ObjectPart
Entity           -[occludes]->                Entity
Entity           -[visible_in]->              Observation
ActionPhase      -[requires]->                StateAssertion
ActionPhase      -[maintains]->               ContactEpisode
ActionPhase      -[causes]->                  StateAssertion
ActionPhase      -[releases]->                Connection | ContactEpisode
ActionTransition -[results_in]->               StateAssertion
StateAssertion   -[evidenced_by]->             Observation | Source
StateAssertion   -[has_epistemic_status]->     EpistemicStatus
TransitionSpan   -[editorially_elided_by]->    HardCut
ActionTransition -[conditioned_by]->           Carrier
ActionTransition -[compiled_to]->              ProviderInvocation
ActionTransition -[verified_by]->              VerificationCheck
ProviderInvocation-[constrained_by]->          CapabilitySnapshot
FailureState     -[violates]->                 Predicate | TopologyRule
```

### Existing-concept mappings

- `interaction lifecycle` → action phases, contact episodes, ownership transfer, support, release, and final-state dwell.
- `object affordance constraints` → typed affordances on specific parts/connections, with preconditions and permitted effects.
- `action preconditions and effects` → phase entry conditions, interval invariants, exit effects, postconditions, and failures.
- `persistent and transient object state` → persistent parts/regions/connections versus transient contact and motion phases.
- `contact identity across occlusion` → stable hand/part IDs plus `occluded_active` contact state and visibility-aware tracks.
- `visibility is not existence` → region/entity existence separated from visibility state; cavity remains present while enclosed.
- `provider capability negotiation` → versioned input semantics, control combinations, and documentation lineage.
- `execution-carrier selection` → verification-driven choice among cuts, anchors, references, edits, tracks, or authored simulation.

## Contradictions, limitations, and unanswered questions

### Contradictions and tensions

1. **Symbolic versus geometric state.** BEHAVIOR-style predicates make initial and goal states explicit [E4], but an `open` boolean is too coarse for a deformable bag. CPCS needs the symbolic predicate and the part-level observable evidence.
2. **Rigid articulation versus deformation.** OpenUSD rigid joints provide clear bodies and constraints [E1], whereas bag panels and gussets need deformable rest shape/topology/material concepts [E2]. A single “joint angle” cannot represent the whole transition.
3. **Contact inference versus contact measurement.** Monocular imagery can support contact hypotheses, but ARCTIC and ContactPose obtain stronger ground truth with MoCap, multi-view, thermal, or RGB-D capture [E5][E6]. CPCS must preserve that difference.
4. **Boundary control versus causal control.** Veo can accept first and last frames [E10], yet this constrains endpoints, not the validity of the bridge. A successful-looking last frame does not prove seam release or contact transfer.
5. **Appearance identity versus part identity.** Provider subject references may preserve appearance [E11], but that is not equivalent to stable slider, seam, panel, or gusset tracks.
6. **Control availability versus control combinability.** Firefly documents composition transfer and image keyframes but states that the two cannot be combined in the cited workflow [E14]. Capability negotiation must represent conflicts.
7. **Generic quality versus task success.** VBench and PhyGenBench establish useful multidimensional and physical-commonsense evaluation [E8][E9], but neither encodes the sling bag's exact causal graph.

### Limitations of this proposal

- No source located here establishes a universal minimal ontology for zippers, cloth panels, gussets, and hand contacts. The schema is a research-backed synthesis for CPCS review.
- No numeric tolerance is proposed. Production thresholds require project data, benchmark alignment, provider contracts, or calibrated measurements.
- The sling bag's true construction is unknown. A real product may use a flap, hinged panel, full-perimeter zipper, partial zipper, lining, stiffener, magnets, or other attachments. Instance modeling requires inspection.
- The proposed verifier can detect visible contradictions but cannot prove hidden 3D physics from monocular output.
- Provider documentation changes quickly. The cited capability snapshot is research evidence, not a durable API contract; CPCS must refresh it at execution time.
- First/last frames, depth, masks, pose, or tracks are controls, not guarantees. The authority boundary remains unchanged.
- A physically authored 3D transition still depends on correct topology, material parameters, contact setup, and solver validation.

### Unanswered questions for CPCS validation

1. What is the repository's canonical distinction between `Part`, `Region`, and `Connection`, and can a region such as `interior_cavity` be persistent while enclosed?
2. Does CPCS already have a provenance-bearing assertion type that can encode the seven epistemic statuses without loss?
3. Should `DistributedClosure` be a first-class connection type or a composition of slider, path, and repeated local constraints?
4. Which qualitative deformation classes are sufficient across bags, jackets, folding cartons, doors, lids, and fabric closures?
5. How will a verifier establish part masks/tracks for small elements such as a zipper slider, especially under hand occlusion?
6. What project-level evidence is required before a detected 2D adjacency may be interpreted as an active contact episode?
7. How should CPCS express joint or material uncertainty when several constructions are consistent with the same video?
8. Which provider adapters can currently consume temporally coherent masks, hand tracks, object-part tracks, or depth, and which combinations are contractually supported?
9. When an exact transition is product-critical, who authorizes escalation from generative video to reference capture, video editing, or 3D/simulation authoring?
10. What human-review rubric will promote this staged proposal into curated CPCS truth?

## Recommended staged adoption

1. Add a provisional `ObjectPartGraph`, `StateAssertion`, `ContactEpisode`, `EditorialEllipsis`, and `VerificationContract` to a research namespace.
2. Encode UG-008 twice: the truthful hard-cut depiction and a separately authored continuous-transition test.
3. Run both through the same `V1`–`V10` checks, allowing `unknown` where the source cannot decide.
4. Test at least one boundary-anchor carrier and one source/reference-video carrier; record provider/model/version and capability conflicts.
5. Have a human reviewer inspect topology, contact ownership, cavity evidence, and epistemic labels before any promotion.
6. Generalize only after additional cases cover a rigid door/box, a flexible jacket or fabric closure, and a folding/package object.

The proposal should remain staged until those validations show that the schema is both minimal and sufficient across the required object families.
