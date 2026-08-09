# 13 — Computational Laban: State of the Art and Detector Feasibility

## Executive finding

A useful Laban inference system is feasible, but no broadly validated, real-time, full-BESS “OpenFace for Laban” was identified. Existing work falls into notation editors/interchange, semantic representation, selected-feature inference, gesture/action classification, affect annotation, motion segmentation, expressive generation, or emerging neurosymbolic/generative systems. Expert reliability evidence and dataset scarcity remain core bottlenecks. [S006; S007; S008; S012]

## Existing systems

| System | Category | Input | Output | Scope | Sources |
|---|---|---|---|---|---|
| LabanWriter | manual notation editor | human notation | Labanotation score | — | S005 |
| LabanXML/LabanEditor2 | notation interchange/editor | symbolic score | XML/score | — | S009 |
| MovementXML | semantic representation | movement semantics | XML | — | S010 |
| Laban ontology | semantic/knowledge representation | dance movement concepts | ontology graph | — | S011 |
| EMOTE | expressive synthesis | motion + Effort/Shape parameters | styled motion | — | S031 |
| Samadani et al. | feature correlates/classification | mocap hand/arm trajectories | selected Effort/Shape estimates | small constrained dataset | S007 |
| Guo et al. | supervised BESS classification | video-derived motion features | BESS-related annotations | research prototype | S006 |
| MoRTELaban | neurosymbolic representation | motion | Laban representation | recent research | S012 |
| BoME | expert-annotated dataset/modeling | video clips | 11 selected emotion-related motor elements | not full BESS | S071 |
| LaMoGen | generation guidance | text + Laban features | 3D motion | preprint, not detector | S072 |
| Bouchard/Badler | mocap segmentation | mocap | semantic segments | — | S073 |
| Bayesian LMA perspective model | gesture classification | tracked gesture features | limited LMA-inspired classes | — | S074 |
| LMA + HMM dynamic gesture recognition | gesture recognition | motion sequence | gesture class | — | S075 |

LabanWriter, LabanXML, MovementXML, and ontology work answer how to **represent** motion. EMOTE and LaMoGen answer how to **generate/transform** motion using Laban-related controls. Samadani et al., Guo et al., BoME, Bouchard/Badler, Bayesian LMA, and LMA-HMM research provide pieces of **inference/classification**. They are not interchangeable.

## Datasets

| Dataset | Native Laban labels? | Labels | Size | Status |
|---|---|---|---|---|
| BoME | True | 11 selected emotion-related LMA motor elements | 1,600 clips | — |
| AMASS | False | mocap/SMPL motion archive | — | — |
| BABEL | False | semantic action labels over AMASS | — | — |
| HumanAct12 | False | 12 action categories | — | — |
| BEAT | False | speech, gesture, emotion, semantics | — | — |
| AIST++ | False | dance/music alignment | — | — |
| CMD | unknown | — | — | ambiguous acronym in supplied query; no Laban-native dataset verified |

AMASS, BABEL, HumanAct12, BEAT, and AIST++ can supply motion diversity, action labels, speech/gesture, or music alignment, but they require new expert annotation or weak-label conversion for Laban training. BoME is directly relevant but covers eleven selected emotion-related motor elements over 1,600 clips, not the complete BESS vocabulary. [S071]

`CMD` in the supplied query is ambiguous. No Laban-native corpus could be verified under that exact acronym, so CPCS does not guess which dataset was intended.

## Unverified aliases

No reliable system was located under the exact names `LabanWRML` or `ChoosenMove`. `MoveScape` was not verified as an automatic LMA detector. They remain in the gap log but are excluded from curated system entities. This cannot be verified with 100% certainty because an unpublished, renamed, or inaccessible project may exist; the reliable evidence located does not support asserting them.

## Proposed detector architecture

1. decode video and estimate/stabilize camera motion;
2. multi-person tracking;
3. whole-body 2D pose, hands, face;
4. calibrated 3D triangulation or uncertainty-aware lifting;
5. actor-scale normalization;
6. contact/support inference;
7. kinematic and geometric feature bank;
8. separate BESS factor heads;
9. temporal smoothing/segmentation;
10. expert-calibrated uncertainty and explanation.

OpenPose and MediaPipe are suitable front ends, while Pose2Sim/OpenCap support calibrated 3D and biomechanical workflows. “World coordinates” from a monocular model are not automatically metric ground truth. [S024; S025; S063; S064]

## Observability

| Factor | Visual observability | Reason |
|---|---|---|
| Space | high | geometry/path |
| Time | high | timing/derivatives |
| Shape | medium-high | body volume/axes, but mode interpretation contextual |
| Body | medium | requires reliable segmentation/initiation/contacts |
| Weight | low-medium | perceived force and support are partly latent |
| Flow | low | control/tension/reversibility are not uniquely visible |

Space and Time are comparatively geometric. Shape axes are observable but Shape mode remains relational/contextual. Body needs robust onset, sequencing, and support estimation. Weight and Flow are hardest because effective mass, muscle/control state, resistance, and reversibility are partly latent. Target response, ground contacts, and inverse dynamics can improve Weight estimates; Flow should remain a distribution with low-confidence when only monocular RGB is available.

## Learning strategy

Use multi-task heads for continuous/ordinal factors, per-part tracks, and phase segmentation. Ground truth should be the **distribution of expert ratings**, not a single label. At least two qualified analysts plus adjudication are recommended for a gold subset. Use actor-, camera-, style-, culture-, and domain-disjoint splits.

Metrics should include weighted kappa, ICC, macro F1, ordinal MAE, Brier score, calibration error, segment IoU, and cross-dataset degradation. A fast but uncalibrated detector is not production-ready.

## Real-time target

A practical first release should infer:

- reach and kinesphere;
- directness/path geometry;
- timing and suddenness;
- dimensional Shape axes;
- initiation/segment sequencing;
- contact/support state.

Weight and Flow should initially be “assisted inference” with visual evidence, confidence, and human correction. Only after calibration should CPCS promote them to automated derived labels.

## Output example

```json
{
  "interval": [1.20, 2.05],
  "space": {"reach": {"value": 0.81, "confidence": 0.92}, "pathway": "spoke_like"},
  "effort": {
    "time": {"value": 0.78, "confidence": 0.87},
    "space_effort": {"value": 0.74, "confidence": 0.66},
    "weight": {"value": 0.69, "confidence": 0.41, "evidence": ["support_loading","target_response"]},
    "flow": {"value": 0.58, "confidence": 0.28}
  },
  "shape": {"sagittal": 0.88, "horizontal": 0.54, "vertical": 0.61},
  "body": {"initiation": "core", "sequence": "proximal_to_distal"}
}
```

## References and locators

- **[S005]** Ohio State University Department of Dance (2026), *LabanWriter*. **Locator:** § LabanWriter; description of 700+ symbols and notation editor  
- **[S006]** Wenbin Guo et al. (2022), *AI-driven Human Motion Classification and Analysis using Laban Movement System*. **Locator:** Abstract; §§3–5; manuscript pp.1–12  
- **[S007]** Ali-Akbar Samadani; SarahJane Burton; Rob Gorbet; Dana Kulić (2013), *Laban Effort and Shape Analysis of Affective Hand and Arm Movements*. **Locator:** pp.343–348; §§II–V; Tables I–IV  
- **[S008]** Bernardet et al. (2019), *Assessing the Reliability of the Laban Movement Analysis System*. **Locator:** Methods; Results; Discussion on inter-rater reliability  
- **[S009]** Minako Nakamura; Kozaburo Hachimura (2006), *An XML Representation of Labanotation, LabanXML, and Its Implementation on the Notation Editor LabanEditor2*. **Locator:** Review of the National Center for Digitization 9, pp.47–51  
- **[S010]** Metadata varies across indexes; verify against thesis repository record (2006), *MovementXML: A Representation of Semantics of Human Movement Based on Labanotation*. **Locator:** Chs.3–5 and Movement XML schema appendix  
- **[S011]** Katerina El Raheb; Yannis Ioannidis (2012), *A Labanotation Based Ontology for Representing Dance Movement*. **Locator:** LNCS 7206, Ch.10  
- **[S012]** Perez-Martinez et al. (2025), *MoRTELaban: A Neurosymbolic Framework for Motion Representation Through Laban Movement Analysis*. **Locator:** Abstract; framework and evaluation sections  
- **[S019]** OpenFace project; Tadas Baltrušaitis et al. (2026), *OpenFace Action Units Documentation*. **Locator:** Supported AUs; presence and 0–5 intensity outputs  
- **[S024]** Scott D. Uhlrich et al. (2023), *OpenCap: Human Movement Dynamics from Smartphone Videos*. **Locator:** Methods pipeline; validation; limitations  
- **[S025]** David Pagnon; Mathieu Domalain; Lionel Reveret (2022), *Pose2Sim: An Open-Source Python Package for Multiview Markerless Kinematics*. **Locator:** JOSS 7(77), article 4362, pp.1–4  
- **[S030]** Haiyang Liu et al. (2022), *BEAT: A Large-Scale Semantic and Emotional Multi-Modal Dataset for Conversational Gestures Synthesis*. **Locator:** ECCV 2022; dataset statistics and §§3–5  
- **[S031]** Diane Chi; Monica Costa; Liwei Zhao; Norman Badler (2000), *The EMOTE Model for Effort and Shape*. **Locator:** SIGGRAPH 2000, pp.173–182  
- **[S035]** Abhinanda Punnakkal et al. (2021), *BABEL: Bodies, Action and Behavior with English Labels*. **Locator:** CVPR 2021; dataset and annotation sections  
- **[S045]** Ruilong Li et al. (2021), *AIST++ Dance Motion Dataset*. **Locator:** ICCV 2021; dataset, beat alignment, evaluation  
- **[S063]** Zhe Cao et al. (2019), *OpenPose: Realtime Multi-Person 2D Pose Estimation Using Part Affinity Fields*. **Locator:** IEEE TPAMI 43(1), pp.172–186  
- **[S064]** Google AI Edge (2026), *MediaPipe Pose Landmarker*. **Locator:** Outputs, landmarks, world coordinates, video/live modes  
- **[S065]** Naureen Mahmood et al. (2019), *AMASS: Archive of Motion Capture as Surface Shapes*. **Locator:** ICCV 2019; dataset documentation  
- **[S066]** Guo et al. (2020), *HumanAct12*. **Locator:** Dataset categories and action-to-motion paper  
- **[S071]** Chenyan Wu et al. (2023), *Bodily Expressed Emotion Understanding Through Integrating Laban Movement Analysis*. **Locator:** BoME dataset and experiment sections  
- **[S072]** Heechang Kim; Gwanghyun Kim; Se Young Chun (2025), *LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation*. **Locator:** §§1–4; Laban features; experiments  
- **[S073]** Durell Bouchard; Norman I. Badler (2007), *Semantic Segmentation of Motion Capture Using Laban Movement Analysis*. **Locator:** IVA 2007, LNCS 4722, pp.37–44  
- **[S074]** Joerg Rett; Jorge Dias; Juan-Manuel Ahuactzin (2008), *Laban Movement Analysis Using a Bayesian Model and Perspective Projections*. **Locator:** Feature construction, Bayesian classifier, perspective projection  
- **[S075]** Anh-Tuan Truong; Titus Zaharia (2017), *Dynamic Gesture Recognition with Laban Movement Analysis and Hidden Markov Models*. **Locator:** §3 descriptors/HMM; experiments and limitations
