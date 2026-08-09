# 01 — Laban Movement Analysis: Full BESS Framework

## Executive finding

The complete framework is **Body, Effort, Shape, and Space (BESS)**. CPCS should not treat “Laban” as a synonym for four Effort factors. Effort describes dynamic quality; Shape describes how the body changes form; Space describes where and along what geometry movement occurs; Body describes participation, initiation, organization, and sequencing. LIMS presents Laban/Bartenieff Movement Analysis as a detailed system for qualitative movement, while Bartenieff and Lewis organize the framework across body, effort, shape, and space-related concerns. [S001, Movement Analysis Overview; S002, Chs.3–6]

The key engineering decision is to preserve LMA’s **qualitative poles** while offering a separate computational view. CPCS stores every bipolar factor on signed `[-1, +1]`, then exposes a unit interval through `u=(x+1)/2`. A unit value of `0.5` means midrange, mixed, or unspecified. It is not an official “neutral Laban quality.” This prevents schemas from confusing an engineering normalization with source doctrine.

## Body layer

Body answers four production questions:

1. **What participates?** Track active parts and relative participation, not merely a single skeleton pose.
2. **Where does movement initiate?** Core, head, tail, proximal joint, distal extremity, multiple sites, or an external contact.
3. **How does activation sequence?** Simultaneous, proximal-to-distal, distal-to-proximal, upper-to-lower, ipsilateral, cross-lateral, spiral, or mixed.
4. **How is support organized?** Explicit contacts, balance state, symmetry/asymmetry, and weight transfer.

A pose prompt such as “the actor punches” is under-specified. A Body-aware direction says: `core initiation → pelvis/trunk rotation → shoulder → elbow → fist`, with a rear-foot support contact maintained until the stroke. That sequencing is semantically different from a distal arm-only punch even when the fist follows a similar path.

## Effort factors

| Factor | Negative pole | Positive pole | Negative descriptors | Positive descriptors | Caution |
|---|---|---|---|---|---|
| weight | light | strong | delicate, buoyant, gentle | powerful, heavy, forceful | Perceived Weight is not measured external force. |
| time | sustained | sudden | lingering, gradual, unhurried | urgent, quick, abrupt | Context dependent |
| space_effort | indirect | direct | wandering, multi-focused, flexible attention | targeted, single-focused, straight | Context dependent |
| flow | free | bound | released, ongoing, unrestrained | controlled, checked, restrained | Flow is latent control/tension and is harder to infer from vision than geometric factors. |

CPCS should retain `space_effort` as the field name to avoid collision with the separate **Space** category. Path efficiency and curvature can support Direct/Indirect inference, but attention focus is not reducible to geometry. Likewise, Weight is perceived dynamic emphasis, not force in newtons, and Flow includes control/releasability that can remain visually latent. Samadani et al. demonstrate that physical features can correlate with selected Effort/Shape labels in constrained hand/arm data, but the dataset size and motion scope do not justify universal formulas. [S007, §§II–V, Tables I–IV]

### Effort States

States combine two motion factors and leave two latent or less salient.

| State | Present factors | Missing factors | Alias |
|---|---|---|---|
| awake | space_effort, time | weight, flow | alert |
| dreamlike | weight, flow | space_effort, time | dream |
| distant | space_effort, flow | weight, time | remote |
| near | weight, time | space_effort, flow | rhythm |
| stable | space_effort, weight | time, flow | — |
| mobile | time, flow | space_effort, weight | labile |

### Effort Drives

Drives combine three factors and omit one.

| Drive | Present factors | Omitted factor |
|---|---|---|
| action_drive | space_effort, weight, time | flow |
| passion_drive | weight, time, flow | space_effort |
| vision_drive | space_effort, time, flow | weight |
| spell_drive | space_effort, weight, flow | time |

The Action Drive contains Space, Weight, and Time while Flow recedes; its eight pole combinations produce the basic effort actions: Float, Punch/Thrust, Glide, Slash, Dab, Wring, Flick, and Press. Drives and States are categorical compositional patterns. CPCS can calculate whether a continuous vector is close to a pattern, but should store both the continuous values and the named interpretation.

## Shape layer

Shape must be represented in two complementary ways.

**Shape modes** describe the relation by which form changes: Shape Flow is self-referential change such as breath expansion; Directional movement bridges toward a goal along spoke-like or arc-like paths; Carving/Shaping accommodates three-dimensional volume.

**Dimensional Shape** supplies three bipolar axes:

| Axis | Negative | Positive | CPCS unit anchors |
|---|---|---|---|
| vertical | sinking | rising | {'sinking': 0, 'neutral': 0.5, 'rising': 1} |
| horizontal | enclosing | spreading | {'enclosing': 0, 'neutral': 0.5, 'spreading': 1} |
| sagittal | retreating | advancing | {'retreating': 0, 'neutral': 0.5, 'advancing': 1} |

Useful computational features include body convex-hull volume, width/height/depth ratios, distances of limbs from torso, and rates of change. These are proxies, not complete substitutes for expert Shape interpretation. A person can advance sagittally through the environment while the torso simultaneously retreats from interpersonal contact; CPCS therefore permits actor-root Shape, torso Shape, and per-part Shape tracks.

## Space layer

Space includes kinesphere, level, direction, pathway, orientation, planes, and spatial harmony. `reach=0` means near-kinesphere and `reach=1` means actor-specific far reach after normalization. Pathways should be named and geometric: spoke-like, arc-like, carved/multi-planar, peripheral, or central. Spatial harmony cannot responsibly be collapsed to one scalar; encode direction vectors and ordered transitions through forms or spatial-scale sequences.

For AI-video prompting, the distinction between Effort Space and category Space is practical:

- `space_effort=direct` means focused, single-targeted dynamic intent.
- `pathway=arc_like` means the geometry is curved.
- A curved path can still be dynamically Direct when the actor is unwaveringly focused on one target.

## Digitization and notation

| System | Purpose | Automatic detector? | Sources |
|---|---|---|---|
| LabanWriter | manual notation editor | False | S005 |
| LabanXML | XML notation interchange | False | S009 |
| MovementXML | semantic movement XML | False | S010 |
| Laban ontology | semantic ontology | False | S011 |
| EMOTE | expressive generation | n/a | S031 |
| Samadani et al. | continuous feature correlates | n/a | S007 |
| Guo et al. | supervised BESS-related classification | n/a | S006 |
| MoRTELaban | neurosymbolic representation | n/a | S012 |

LabanWriter, LabanXML, MovementXML, and ontology work show that the notation can be digitized, exchanged, and represented semantically. They do **not** constitute an OpenFace-like detector. EMOTE, Samadani et al., Guo et al., and MoRTELaban demonstrate generation, feature correlation, classification, or neurosymbolic representation under specific conditions. Inter-rater reliability evidence means CPCS training data must retain coder identity, disagreement, confidence, and adjudication rather than pretending one annotation is absolute ground truth. [S008, Methods/Results/Discussion]

## CPCS encoding recommendation

```json
{
  "body": {"initiation_locus": "core", "sequencing": "proximal_to_distal"},
  "effort": {"weight": 0.75, "time": 0.80, "space_effort": 0.85, "flow": 0.35},
  "shape": {"vertical": 0.60, "horizontal": 0.45, "sagittal": 0.90, "mode": "directional"},
  "space": {"reach": 0.85, "pathway": "spoke_like", "level": "middle"},
  "provenance": {"normalization": "CPCS_CONVENTION", "framework": ["S001","S002","S004"]}
}
```

## Prompt compilation examples

**Combat:** “Initiate from the rear foot and core, sequence pelvis–trunk–shoulder–elbow–fist, advance on a direct mid-level spoke, strong and sudden, with controlled recoil.”

**Comfort:** “Breath-supported core-distal reach, sustained and light, gently advancing while the torso spreads only slightly; free enough to feel welcoming but bound enough to stop before unwanted contact.”

**Fashion:** “Rise and spread through the upper body while gliding on a peripheral arc; sustained time, light weight, controlled flow, and far-kinesphere reach.”

## Implementation rules

- Never infer force in newtons from `weight` alone.
- Never infer Flow from jerk alone.
- Store continuous factors, categorical labels, confidence, and annotator provenance together.
- Permit per-part and multi-scale tracks; whole-body averages erase meaningful opposition.
- Keep notation representation, movement analysis, and model-generation controls as separate layers.

## References and locators

- **[S001]** Laban/Bartenieff and Somatic Studies International (LSSI/LIMS) (2026), *Movement Analysis Overview*. **Locator:** § What is Laban/Bartenieff Movement Analysis?  
- **[S002]** Irmgard Bartenieff; Dori Lewis (1980), *Body Movement: Coping with the Environment*. **Locator:** Ch.3 pp.23–48; Ch.4 pp.49–68; Ch.5 pp.69–82; Ch.6 pp.83–100; Appendix B from p.229  
- **[S004]** Rudolf Laban; F. C. Lawrence (1947), *Effort: Economy of Human Movement*. **Locator:** Parts on motion factors and basic effort actions; edition-specific pagination  
- **[S005]** Ohio State University Department of Dance (2026), *LabanWriter*. **Locator:** § LabanWriter; description of 700+ symbols and notation editor  
- **[S006]** Wenbin Guo et al. (2022), *AI-driven Human Motion Classification and Analysis using Laban Movement System*. **Locator:** Abstract; §§3–5; manuscript pp.1–12  
- **[S007]** Ali-Akbar Samadani; SarahJane Burton; Rob Gorbet; Dana Kulić (2013), *Laban Effort and Shape Analysis of Affective Hand and Arm Movements*. **Locator:** pp.343–348; §§II–V; Tables I–IV  
- **[S008]** Bernardet et al. (2019), *Assessing the Reliability of the Laban Movement Analysis System*. **Locator:** Methods; Results; Discussion on inter-rater reliability  
- **[S009]** Minako Nakamura; Kozaburo Hachimura (2006), *An XML Representation of Labanotation, LabanXML, and Its Implementation on the Notation Editor LabanEditor2*. **Locator:** Review of the National Center for Digitization 9, pp.47–51  
- **[S010]** Metadata varies across indexes; verify against thesis repository record (2006), *MovementXML: A Representation of Semantics of Human Movement Based on Labanotation*. **Locator:** Chs.3–5 and Movement XML schema appendix  
- **[S011]** Katerina El Raheb; Yannis Ioannidis (2012), *A Labanotation Based Ontology for Representing Dance Movement*. **Locator:** LNCS 7206, Ch.10  
- **[S012]** Perez-Martinez et al. (2025), *MoRTELaban: A Neurosymbolic Framework for Motion Representation Through Laban Movement Analysis*. **Locator:** Abstract; framework and evaluation sections  
- **[S031]** Diane Chi; Monica Costa; Liwei Zhao; Norman Badler (2000), *The EMOTE Model for Effort and Shape*. **Locator:** SIGGRAPH 2000, pp.173–182
