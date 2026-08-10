# 02_FACS — FACS / Laban / Bartenieff Research-to-Representation Closure

## Closure status

**Status:** CONDITIONAL RESEARCH CLOSURE

This document applies the CPCS master deep-research protocol to the FACS/Laban/Bartenieff gap packet.

Important source-boundary note: the uploaded materials include the master protocol and the `02_FACS_LABAN_BARTENIEFF_GAP_CLOSURE.md` prompt, but the prompt's named frozen corpus `CPCS_FACS_Laban_AI_Video_Research_Package_v1.2.zip` was not attached. Therefore this is **not** a claim that the frozen package itself has been exhaustively distilled. The closure below is grounded in the supplied gap specification plus independent primary/authoritative/public research verification. Any package-only claim that cannot be verified externally remains an open reconciliation item.

The supplied packet requires the result to be implementation-ready rather than a literature summary: research → measurement definition → representation → canonical CPCS mapping → compiler behavior → provider-facing meaning → verification. The master protocol also fixes one universal semantic kernel, canonical JSON as resolved meaning, YAML as authoring, evidence/provenance separation, explicit uncertainty, separate knowledge/execution/VOG graphs, and fail-closed handling for unsupported controls. [Source: supplied master protocol, lines 33–45, 48–61.]

---

# 1. Executive gap closure

## 1.1 What the supplied research direction already establishes

The packet establishes five architectural requirements:

1. FACS must be treated as a **descriptive facial-movement vocabulary**, not as an emotion detector.
2. FACS needs temporal structure: onset, apex, offset, duration, coactivation and overlap.
3. Laban needs to be represented as a qualitative movement-analysis layer whose semantic labels are not silently converted into universal physical measurements.
4. Bartenieff connectivity needs explicit representation rather than being left as prose.
5. A single performance event must be able to combine facial action, gaze, head orientation, Laban qualities, connectivity, breath, posture and action phase.

The master protocol further requires every semantic addition to have an executable consumer and requires measured, detected, inferred, interpreted, authored and creative values to remain distinguishable.

## 1.2 What external verification establishes

### FACS

The Paul Ekman Group describes FACS as an anatomically based system for describing visually discernible facial movement using Action Units. The current public FACS page identifies the 2002 manual as the current scoring version. The manual is proprietary, so CPCS should not reproduce its detailed scoring criteria; it should store the public vocabulary, version metadata, provenance and project-level abstractions, while treating licensed FACS training/manual material as the authority for exact coder rules.

FACS is descriptive. Published psychometric work explicitly distinguishes the descriptive FACS score from any later interpretation into emotion categories. A 2002 psychometric study found good-to-excellent reliability for occurrence, intensity and timing across most commonly observed AUs in spontaneous expression, while also identifying weaker reliability for subtle/confusable actions such as AU7 and AU23 and improved temporal agreement when a tolerance window is used.

### FACS intensity

The published literature describes the FACS intensity code as an **ordinal A–E scale**, not a physical force or universally calibrated percentage. Therefore:

- `facs_intensity` must remain ordinal (`A`–`E`, where supported).
- `project_normalized` may exist as a derived convenience scale, but it must never be presented as equivalent to FACS intensity.
- A value such as `0.6` is legitimate only when explicitly labeled with its basis, e.g. `project_normalized`, `model_score`, or `measured_proxy`.
- Cross-subject/cross-camera/cross-model numeric comparison requires calibration and should not be assumed.

### Automated FACS

OpenFace demonstrates a practical machine pipeline: AU presence and intensity can be estimated frame-by-frame, but only a subset of FACS AUs is supported. Its documentation explicitly warns that presence and intensity models are separately trained and can disagree; video-based person calibration differs from image-only and multi-face conditions.

Therefore CPCS should treat automatic AU output as:

`detected` / `measured_proxy`

rather than automatically as `evidence` of the underlying FACS code at coder-grade reliability.

### Laban

Peer-reviewed work describes LMA using Body, Effort, Space and Shape, with Phrasing as an additional meta-category. Effort contains Weight, Time, Space and Flow factors, each represented by opposing qualitative elements:

- Weight: Light ↔ Strong
- Time: Sustained ↔ Sudden
- Space: Indirect ↔ Direct
- Flow: Free ↔ Bound

Space includes kinesphere/reach and directional concepts. Shape includes spreading/enclosing, rising/sinking and advancing/retreating. Phrasing describes where emphasis occurs in the movement phrase.

The strongest implementation finding is that LMA is not equivalent to a numeric kinematic feature vector. Research has shown that some LMA categories are more reliably coded than others and that Effort/Shape contain greater subjective inference than more spatially explicit dimensions.

### Laban reliability

A 2019 empirical reliability study with Certified Movement Analysts found only weak-to-acceptable overall reliability depending on how ratings were integrated. The authors specifically note category differences and the qualitative nature of Effort and Shape. This is a critical constraint: CPCS can encode Laban qualities as authored semantic controls and can compute proxies, but it should not label a kinematic proxy as "the true Laban value" without calibration.

### Bartenieff

The six connectivity patterns required by the packet are:

1. Breath
2. Core-Distal
3. Head-Tail
4. Upper-Lower
5. Body-Half
6. Cross-Lateral

The research literature distinguishes the Bartenieff Fundamentals as a broader movement-practice/system context from the individual connectivity patterns. For CPCS, the six patterns should be modeled as **connectivity relationships/patterns**, not as six universal scalar dimensions.

## 1.3 What is still missing

The important implementation gaps are:

- a versioned FACS catalog with explicit version semantics;
- a side-aware AU event model;
- an ordinal FACS intensity field separate from project-normalized values;
- temporal event semantics with explicit frame/timebase;
- AU detection confidence and observability states;
- a FACS confusion/coactivation relation layer;
- explicit separation of FACS observation from affect/emotion interpretation;
- a Laban semantic vocabulary with proxy measurements;
- a proxy-to-semantic calibration boundary;
- a six-pattern Bartenieff connectivity object;
- a multi-layer performance event joining all of these without flattening them into one "emotion" field;
- compiler loss records for providers that cannot express exact controls;
- verification fixtures that test left/right, temporal, semantic-vs-measurement and unsupported-control behavior.

## 1.4 What can be implemented now

Implement now:

- `facs_event`;
- `facs_intensity`;
- `facs_temporal_segment`;
- side-indexed bilateral representation;
- FACS evidence/provenance fields;
- `laban_effort`, `laban_shape`, `laban_space`, `laban_phrasing`;
- `laban_proxy_measurement`;
- `bartenieff_connectivity`;
- `performance_expression_event`;
- explicit `affect_target` separate from observed facial behavior;
- canonical JSON resolution;
- YAML authoring;
- provider compilation;
- loss/degradation records;
- deterministic validators and fixture suites.

## 1.5 What requires experiments

Requires controlled experiments:

- whether a given provider actually responds better to FACS identifiers versus natural-language descriptions;
- whether a provider interprets project-normalized intensity consistently;
- whether Laban qualitative labels improve generation compared with kinematic proxies;
- which Laban proxy formulas correlate with expert CMA ratings;
- whether six Bartenieff patterns improve provider adherence;
- cross-provider preservation of bilateral/asymmetric facial instructions;
- temporal adherence to onset/apex/offset;
- whether a combined FACS+Laban+connectivity representation increases adherence or merely increases prompt complexity.

## 1.6 What remains unknown

- Exact provider-side semantics for FACS and Laban tokens are not standardized.
- No evidence supports a universal numeric conversion from Laban qualitative elements to `[0,1]`.
- No evidence supports treating automatic AU confidence as equivalent to certified human FACS coding.
- Exact current FACS 2002 scoring rules remain licensed/proprietary and must not be reconstructed from secondary lists.
- The named frozen research ZIP was not supplied in this session, so package-vs-external reconciliation remains pending.

---

# 2. Evidence ledger

| Field/concept | Meaning | Evidence class | Primary/authoritative source | Confidence | Measurement status | CPCS status |
|---|---|---|---|---|---|---|
| `facs.version` | FACS scoring/version authority | established external fact | Paul Ekman Group | high | metadata | implement |
| `au_id` | FACS Action Unit identifier | established external fact | Paul Ekman Group / Ekman et al. | high | categorical | implement |
| `au_visible_action` | visible facial movement descriptor | established external fact | FACS literature | high | descriptive | implement |
| `side` | left/right/bilateral/unspecified | source-supported + proposed representation | FACS coding literature | high | observable when visible | implement |
| `facs_intensity` | ordinal FACS intensity | established external fact | FACS literature | high | ordinal annotation | implement |
| `project_normalized_intensity` | project-specific normalized control | proposed CPCS representation | derived engineering layer | medium | derived | implement, label derived |
| `onset/apex/offset` | temporal segmentation | established external fact | FACS literature | high | measured/detected | implement |
| `au_confidence` | detector/coder confidence | proposed CPCS representation | engineering requirement | high | confidence | implement |
| `observability` | observable/occluded/unobservable | proposed CPCS representation | master protocol + CV constraints | high | categorical | implement |
| `coactivation` | multiple AUs active together | established external fact | FACS literature | high | event relation | implement |
| `nonadditive_combination` | combination alters visible appearance | established external fact | AU literature | high | relation | implement |
| `confusable_with` | empirically difficult AU distinction | established external fact | Sayette et al. | high | relation | implement |
| `affect_interpretation` | higher-order interpretation of facial configuration | established conceptual boundary | Sayette et al.; FACS authority | high | inferred/interpreted | separate layer |
| `valence/arousal` | dimensional affect target | established external theory | Russell 1980 + continuous-affect literature | high | authored/inferred/measured depending source | implement separately |
| `laban_body` | what body/body parts move | established external framework | LMA literature | high | semantic observation | implement |
| `laban_effort` | qualitative how/energy organization | established external framework | LMA literature | high | semantic observation | implement |
| `laban_effort_proxy` | measurable kinematic approximation | proposed representation | engineering hypothesis | medium | measured proxy | implement as proxy only |
| `laban_space` | where/how movement is oriented | established external framework | LMA literature | high | semantic observation | implement |
| `laban_shape` | change of bodily form | established external framework | LMA literature | high | semantic observation | implement |
| `laban_phrasing` | temporal emphasis in phrase | established external framework | LMA literature | high | semantic observation | implement |
| `bartenieff_connectivity` | body connectivity pattern | established framework + proposed schema | Bartenieff literature | high | semantic observation / derived | implement |
| `connectivity_phase` | interval over which connectivity is expressed | proposed CPCS representation | engineering | medium | derived/observed | implement |
| `breath_phase` | inhale/exhale/hold/unknown | established physiological concept + proposed CPCS mapping | research/measurement layer | medium | measured/detected | implement with evidence |
| `provider_adherence` | whether generated output expresses requested control | proposed verification metric | engineering | high | measured | experiment |

---

# 3. Semantic representation specification

## 3.1 FACS event

Canonical object:

```json
{
  "type": "facs_event",
  "facs_version": "2002",
  "au_id": "AU12",
  "side": "left",
  "intensity": {
    "value": "C",
    "basis": "facs_ordinal"
  },
  "temporal": {
    "onset_s": 1.20,
    "apex_start_s": 1.48,
    "apex_end_s": 1.62,
    "offset_s": 2.10,
    "duration_s": 0.90,
    "timebase": "presentation_timestamp"
  },
  "evidence_class": "measured",
  "confidence": 0.91,
  "observability": "observable",
  "source_ref": "obs:video:001"
}
```

### What it means

A visible facial movement was assigned to a specified FACS AU, with version, side, ordinal intensity and temporal extent.

### What it does not mean

It does **not** mean:

- the person experienced an emotion;
- the person intended the display;
- the display has one universal psychological meaning;
- the intensity is physical force;
- a detector's score is automatically coder-equivalent.

## 3.2 Bilateral representation

Do not average left/right activation.

Preferred:

```json
{
  "au_id": "AU12",
  "activation": {
    "left": {"intensity": "C"},
    "right": {"intensity": "B"},
    "bilateral": false
  },
  "asymmetry": {
    "kind": "left_dominant",
    "basis": "ordinal_comparison"
  }
}
```

If both sides are present and materially equivalent:

```json
{
  "au_id": "AU12",
  "activation": {
    "left": {"intensity": "C"},
    "right": {"intensity": "C"},
    "bilateral": true
  }
}
```

The exact FACS coding rules for asymmetry remain governed by the licensed manual; this JSON structure is a CPCS representation, not a reproduction of proprietary scoring notation.

## 3.3 FACS intensity

Use:

```text
A | B | C | D | E
```

as the canonical FACS ordinal field where the underlying observation supports FACS intensity.

Do not define:

```text
A = 0.2
B = 0.4
C = 0.6
D = 0.8
E = 1.0
```

as if those were physical measurements.

If CPCS needs a normalized control:

```json
{
  "intensity": {
    "value": 0.6,
    "basis": "project_normalized",
    "source_scale": "facs_ordinal",
    "mapping_id": "project:facs_to_control_v1"
  }
}
```

This is a **derived control**, not FACS truth.

## 3.4 Temporal semantics

Use:

- `onset`: first accepted temporal point;
- `apex_start`: beginning of sustained maximum/peak interval when applicable;
- `apex_end`: end of peak interval when applicable;
- `offset`: end of visible action;
- `duration`: deterministic difference between onset and offset.

Always preserve the original timebase:

```json
"timebase": {
  "kind": "presentation_timestamp",
  "unit": "seconds",
  "source_fps": 30.0
}
```

If source timestamps are unavailable:

```json
"observability": "unobservable",
"reason": "missing_source_timestamps"
```

Do not fabricate exact timing.

---

# 4. FACS field dictionary

The following is a **version-aware public vocabulary layer**, not a reproduction of the proprietary FACS manual.

| AU | Public descriptor | CPCS operational region | Side model | Intensity | Typical machine status |
|---|---|---|---|---|---|
| AU1 | Inner Brow Raiser | upper face | bilateral/side-aware | ordinal | detectable candidate |
| AU2 | Outer Brow Raiser | upper face | bilateral/side-aware | ordinal | detectable candidate |
| AU4 | Brow Lowerer | upper face | bilateral/side-aware | ordinal | detectable candidate |
| AU5 | Upper Lid Raiser | eye/upper face | side-aware | ordinal | candidate; visibility-sensitive |
| AU6 | Cheek Raiser | eye/cheek | bilateral/side-aware | ordinal | detectable candidate |
| AU7 | Lid Tightener | eye | side-aware | ordinal | difficult/confusable |
| AU8 | Lips Toward Each Other | mouth | bilateral | ordinal | candidate |
| AU9 | Nose Wrinkler | nose | bilateral/side-aware | ordinal | candidate |
| AU10 | Upper Lip Raiser | mouth | bilateral/side-aware | ordinal | candidate |
| AU11 | Nasolabial Deepener | cheek | bilateral/side-aware | ordinal | limited automation |
| AU12 | Lip Corner Puller | mouth | side-aware | ordinal | common automation target |
| AU13 | Sharp Lip Puller / Cheek Puffer terminology varies in secondary sources | mouth/cheek | side-aware | ordinal | version/source controlled |
| AU14 | Dimpler | cheek | side-aware | ordinal | common automation target |
| AU15 | Lip Corner Depressor | mouth | side-aware | ordinal | common automation target |
| AU16 | Lower Lip Depressor | mouth | bilateral/side-aware | ordinal | limited automation |
| AU17 | Chin Raiser | chin | bilateral/side-aware | ordinal | common automation target |
| AU18 | Lip Puckerer | mouth | bilateral | ordinal | candidate |
| AU19 | Tongue Out / Tongue Show | mouth | side/pose dependent | ordinal/presence | limited automation |
| AU20 | Lip Stretcher | mouth | bilateral/side-aware | ordinal | common automation target |
| AU21 | Neck Tightener | neck | bilateral | ordinal | limited automation |
| AU22 | Lip Funneler | mouth | bilateral | ordinal | limited automation |
| AU23 | Lip Tightener | mouth | bilateral/side-aware | ordinal | confusable with AU24 |
| AU24 | Lip Pressor | mouth | bilateral/side-aware | ordinal | common candidate |
| AU25 | Lips Part | mouth | bilateral | ordinal/presence | common automation target |
| AU26 | Jaw Drop | jaw | bilateral | ordinal | common automation target |
| AU27 | Mouth Stretch | mouth/jaw | bilateral | ordinal | candidate |
| AU28 | Lip Suck | mouth | bilateral | ordinal | detector support varies |
| AU29 | Jaw Thrust | jaw | bilateral | ordinal | limited automation |
| AU30 | Jaw Sideways | jaw | side-specific direction | ordinal | limited automation |
| AU31 | Jaw Clencher | jaw | bilateral | ordinal | limited automation |
| AU32 | Lip Bite | mouth | bilateral/side-aware | ordinal | limited automation |
| AU33 | Cheek Blow | cheek | bilateral | ordinal | limited automation |
| AU34 | Cheek Puff | cheek | bilateral | ordinal | limited automation |
| AU35 | Cheek Suck | cheek | bilateral | ordinal | limited automation |
| AU36 | Tongue Bulge | mouth | side-aware | ordinal | limited automation |
| AU37 | Lip Wipe | mouth | side/direction | event | limited automation |
| AU38 | Nostril Dilator | nose | bilateral/side-aware | ordinal | limited automation |
| AU39 | Nostril Compressor | nose | bilateral/side-aware | ordinal | limited automation |
| AU41/AU42/AU44 | **version-sensitive legacy/reassigned identifiers** | eye/brow | do not treat as unqualified current AU labels | n/a | reject unless version-qualified |
| AU43 | Eyes Closed | eye | side-aware | ordinal/event | common candidate |
| AU45 | Blink | eye | side-aware | event | common automation target |
| AU46 | Wink | eye | side-aware | event | limited automation |

### Version rule

The 2002 revision changed the handling/meaning of several earlier identifiers. Published documentation specifically warns that AU41, AU42 and AU44 were eliminated as separate actions in the 2002 scoring system and that those numbers were reused for other strands. Therefore CPCS must require:

```json
"facs_version": "2002"
```

before interpreting version-sensitive AU numbers.

Do not build a universal catalog that silently merges 1978 and 2002 semantics.

---

# 5. FACS coactivation, incompatibility and confusion

Three different relations must be distinguished.

## `coactivates_with`

Two AUs are observed simultaneously.

```json
{
  "relation": "coactivates_with",
  "source": "AU6",
  "target": "AU12",
  "evidence_class": "observed"
}
```

This says nothing by itself about emotion.

## `nonadditive_with`

The visual appearance of one AU changes when another AU is present.

This must remain a distinct relation because the FACS literature documents non-additive combinations.

## `confusable_with`

This is a measurement/reliability relation.

Example:

```json
{
  "relation": "confusable_with",
  "source": "AU7",
  "target": "AU6",
  "reason": "subtle lower-lid appearance difference and frequent co-occurrence",
  "evidence_class": "empirical_reliability"
}
```

Published psychometric work identifies AU7/AU6 and AU23/AU24 as difficult distinctions.

Do **not** convert `confusable_with` into `incompatible_with`.

---

# 6. FACS automatic-detection contract

Automatic detection should produce a machine observation:

```json
{
  "type": "facs_detection",
  "au_id": "AU12",
  "presence": 1,
  "intensity_proxy": 3.42,
  "model": "example_model",
  "model_version": "x.y",
  "confidence": 0.91,
  "frame_index": 42,
  "timestamp_s": 1.40,
  "evidence_class": "detected"
}
```

The observation must not be silently promoted to:

```text
evidence_class = measured
```

unless the detector has been validated against the target measurement protocol.

## Recommended machine states

```text
detected
measured
unknown
unobservable
```

`detected` means an algorithm produced a signal.

`measured` means the signal has a defined measurement contract and calibration/validation.

`unknown` means the system lacks sufficient evidence.

`unobservable` means the phenomenon cannot be recovered from the available media.

---

# 7. FACS measurement contract

```text
what is measured:
  AU presence, optional ordinal intensity, temporal segment

measurement source:
  certified FACS coder OR validated automated detector

sampling:
  source-frame timestamps; never assume 30 fps

timebase:
  source PTS preferred; frame index retained

coordinate:
  facial coordinate frame only when geometric measurement is used

normalization:
  detector-specific; identity-normalized only if validated

left/right:
  preserve separately

units:
  FACS intensity = ordinal A-E
  time = seconds/frame index
  detector intensity = model-defined numeric scale

confidence:
  coder agreement or detector confidence, explicitly named

error/tolerance:
  temporal tolerance in seconds/frames
  AU detection precision/recall/F1 or appropriate class-imbalance metric
  intensity ICC/MAE where applicable

missing data:
  unknown

occlusion:
  unobservable or low-confidence; never force a label

camera motion:
  head-pose normalization or landmark-quality gate

aggregation:
  preserve event-level data first; derive phrase-level summaries second
```

## Verification metrics

For AU presence:

- precision;
- recall;
- F1;
- per-AU support;
- macro and micro averages;
- calibration error if probabilities are used.

For AU intensity:

- ICC where the task is continuous/ordinal agreement and assumptions are satisfied;
- MAE;
- rank correlation where appropriate;
- per-AU error;
- confidence/error calibration.

For temporal behavior:

- onset absolute error;
- apex-start error;
- apex-end error;
- offset error;
- event IoU over time;
- tolerance-window agreement.

For bilateral behavior:

- left/right classification accuracy;
- bilateral agreement;
- asymmetry preservation.

Avoid relying on a single F1-binary score for highly imbalanced AU detection. Recent work has specifically argued that AU evaluation can be distorted by class imbalance and occurrence patterns.

---

# 8. Affect boundary

CPCS must enforce:

```text
AU12 activated
≠
person is happy
```

The layers are:

```text
visible_facial_movement
        ↓
facial_configuration
        ↓
contextual/affective interpretation
        ↓
emotion hypothesis
        ↓
private mental-state claim
```

Only the first layer is directly represented by FACS.

A director can author:

```yaml
facial:
  display:
    description: restrained_smile
    facs:
      - au: AU12
        target_intensity: B
      - au: AU6
        target_intensity: A
    affect_interpretation:
      valence: positive
      arousal: low
      basis: authored
```

The final two fields are **authorial intent**, not observations.

This lets CPCS express:

> display a restrained smile

without asserting:

> the actor is happy.

---

# 9. Affect representation

Affect should be modeled separately from FACS.

Recommended canonical representation:

```json
{
  "type": "affect_target",
  "dimensions": {
    "valence": {
      "value": 0.35,
      "scale": "project_normalized",
      "basis": "authored"
    },
    "arousal": {
      "value": 0.20,
      "scale": "project_normalized",
      "basis": "authored"
    }
  },
  "temporal": {
    "kind": "trajectory"
  }
}
```

Affect trajectories should be represented as time-indexed points or segments:

```json
{
  "trajectory": [
    {"t": 0.0, "valence": 0.10, "arousal": 0.15},
    {"t": 1.0, "valence": 0.25, "arousal": 0.20},
    {"t": 2.0, "valence": 0.40, "arousal": 0.35}
  ]
}
```

The numeric scale is project-defined unless a source explicitly specifies a scale.

Russell's circumplex model supports valence/pleasure and arousal/activation as dimensions of affect. Continuous affect research demonstrates that valence/arousal can be modeled over time. This does not establish that FACS AUs uniquely determine an individual's private affect.

---

# 10. Laban semantic representation

## 10.1 Body

```json
{
  "laban_body": {
    "parts": ["head", "torso", "left_arm"],
    "action": "gesture"
  }
}
```

`Body` answers what moves.

It should not be collapsed into Effort.

## 10.2 Effort

```json
{
  "laban_effort": {
    "weight": "strong",
    "time": "sudden",
    "space": "direct",
    "flow": "bound"
  }
}
```

Canonical values:

```text
weight: light | strong
time: sustained | sudden
space: indirect | direct
flow: free | bound
```

Do not interpret these as universal physical measurements.

## 10.3 Space

```json
{
  "laban_space": {
    "reach": "far",
    "zone": "forward",
    "direction": "right_forward_high",
    "pathway": "curved"
  }
}
```

The directional vocabulary must remain coordinate-aware.

## 10.4 Shape

```json
{
  "laban_shape": {
    "horizontal": "spreading",
    "vertical": "rising",
    "sagittal": "advancing"
  }
}
```

These are qualitative shape-change descriptors.

## 10.5 Phrasing

```json
{
  "laban_phrasing": {
    "emphasis": "beginning",
    "pattern": "impulsive"
  }
}
```

Phrasing is temporal organization, not merely speed.

---

# 11. Laban proxy measurements

The correct architecture is:

```text
LMA semantic control
        ↓
optional measurable proxy
        ↓
video/mocap measurement
        ↓
calibration/validation
```

Never:

```text
kinematic feature
        =
Laban truth
```

## Candidate proxies

### Directness

A possible geometric proxy:

```text
path_straightness =
straight_line_distance(start,end) / path_length
```

Lower straightness can be associated with more indirect movement.

But:

```text
path_straightness ≠ Laban Space quality
```

unless validated against CMA ratings.

### Sudden/Sustained

Candidate measurements:

- acceleration/deceleration profile;
- movement duration;
- peak velocity;
- time-to-peak;
- velocity concentration.

These are proxies, not definitions.

### Strong/Light

Possible proxies:

- acceleration;
- estimated interaction force where instrumentation exists;
- momentum change;
- movement amplitude combined with temporal profile.

2D/3D video alone cannot directly recover physical effort.

### Bound/Free

Possible proxies:

- movement interruption;
- trajectory smoothness;
- endpoint constraints;
- jerk;
- repeated correction;
- multi-segment coordination.

Again, these are candidate proxies.

### Shape

Use normalized body-keypoint geometry:

- torso width/height;
- limb spread;
- center-to-distal distances;
- body envelope area;
- vertical/sagittal displacement.

### Phrasing

Use temporal emphasis:

- velocity/acceleration peaks;
- energy distribution across phrase thirds;
- onset-to-apex ratio;
- repetition intervals.

---

# 12. Laban numeric policy

## Canonical rule

Laban semantics are categorical/qualitative by default.

Optional numeric fields must be typed as:

```json
{
  "proxy": {
    "name": "path_straightness",
    "value": 0.72,
    "unit": "ratio",
    "basis": "kinematic_proxy",
    "validation_status": "uncalibrated"
  }
}
```

Never:

```json
{
  "directness": 0.72
}
```

unless a project-specific calibration has explicitly established that mapping.

## Calibration contract

A proxy can be promoted from:

```text
uncalibrated_proxy
```

to:

```text
validated_proxy
```

only after:

1. CMA-coded reference data exists;
2. independent motion measurements are extracted;
3. mapping is trained/fitted;
4. held-out agreement is reported;
5. cross-subject performance is measured;
6. failure cases are documented.

---

# 13. Laban reliability contract

The empirical literature supports using reliability testing rather than assuming all LMA categories are equally objective.

Recommended metric:

```text
Krippendorff's alpha
```

for categorical/multi-rater annotation where appropriate.

For continuous proxy values:

- ICC;
- MAE;
- rank correlation;
- calibration error.

For categorical Laban elements:

- per-category precision/recall;
- Cohen's kappa for two coders when appropriate;
- Krippendorff's alpha for multiple coders/missing data.

The 2019 reliability study is especially important because it shows that an apparently formal movement vocabulary does not automatically imply high agreement across expert observers.

---

# 14. Bartenieff six connectivity patterns

## 14.1 Breath

Semantic meaning:

Whole-body connectivity organized around breath-related expansion/contraction and three-dimensional torso change.

Observable manifestation:

- torso/ribcage expansion;
- torso narrowing;
- coordinated movement associated with inhale/exhale;
- phrase-level breath timing.

Representation:

```json
{
  "pattern": "breath",
  "phase": "inhale",
  "regions": ["ribcage", "torso"],
  "evidence_class": "detected",
  "confidence": 0.82
}
```

Measurement:

Possible video proxy:

- ribcage width/depth;
- torso volume proxy;
- vertical torso movement;
- respiratory audio if available.

Breath is not equivalent to torso width alone.

## 14.2 Core-Distal

Semantic meaning:

Connectivity between central/core organization and distal limbs.

Observable manifestation:

- movement gathering toward the center;
- movement radiating outward;
- coordinated core-to-limb or limb-to-core organization.

Proxy:

```text
distal_distance_from_core(t)
```

combined with temporal direction of change.

## 14.3 Head-Tail

Semantic meaning:

Connectivity along the longitudinal head/spine/tail axis.

Observable manifestation:

- sequential head-to-spine-to-pelvis organization;
- body-level change;
- spinal wave/curvature patterns.

Proxy candidates:

- head-to-pelvis phase lag;
- spinal curvature propagation;
- vertical center-of-mass changes.

## 14.4 Upper-Lower

Semantic meaning:

Connectivity between upper and lower body, often involving grounding/support and coordination.

Observable manifestation:

- upper body movement coordinated with lower-body/ground relationship;
- transfer between upper and lower segments.

Proxy candidates:

- upper/lower segment phase relationship;
- foot-ground contact timing;
- center-of-mass and limb coordination.

## 14.5 Body-Half

Semantic meaning:

Connectivity/organization around one side of the body.

Observable manifestation:

- ipsilateral movement organization;
- one side stabilizing while the other mobilizes;
- lateral organization.

Representation must preserve:

```json
"side": "left"
```

or:

```json
"side": "right"
```

Do not collapse it into a bilateral scalar.

## 14.6 Cross-Lateral

Semantic meaning:

Cross-body coordination between opposite sides.

Observable manifestation:

- left/right diagonal coordination;
- contralateral limb relationships;
- rotation with locomotion/travel.

Proxy:

```text
cross_lateral_index =
coordination(left_upper, right_lower)
+
coordination(right_upper, left_lower)
```

The exact numeric formula is a project-specific derived metric, not a Bartenieff standard.

---

# 15. Bartenieff representation

```json
{
  "type": "bartenieff_connectivity",
  "pattern": "cross_lateral",
  "side_relationship": "contralateral",
  "regions": [
    "left_arm",
    "right_leg"
  ],
  "phase": {
    "start_s": 2.0,
    "end_s": 3.1
  },
  "evidence_class": "interpreted",
  "confidence": 0.78,
  "measurement": {
    "type": "kinematic_proxy",
    "status": "uncalibrated"
  }
}
```

The object stores the semantic classification and separately stores the measurement basis.

---

# 16. FACS/Laban/Bartenieff combined performance event

The major architectural closure is to **not create one mega-label**.

Use layered components:

```json
{
  "type": "performance_expression_event",
  "event_id": "evt_0042",
  "actor_id": "actor_01",
  "phase": "restrained_dialogue",
  "temporal": {
    "start_s": 1.0,
    "end_s": 3.5
  },
  "facial": [
    {
      "au_id": "AU12",
      "side": "bilateral",
      "target_intensity": "B"
    },
    {
      "au_id": "AU6",
      "side": "bilateral",
      "target_intensity": "A"
    }
  ],
  "gaze": {
    "direction": "camera",
    "basis": "authored"
  },
  "head_orientation": {
    "yaw": 0,
    "pitch": 2,
    "roll": 0,
    "unit": "degrees",
    "basis": "authored"
  },
  "laban": {
    "effort": {
      "weight": "light",
      "time": "sustained",
      "space": "direct",
      "flow": "bound"
    },
    "shape": {
      "horizontal": "slightly_enclosing"
    },
    "phrasing": {
      "emphasis": "middle"
    }
  },
  "bartenieff": [
    {
      "pattern": "breath",
      "phase": "exhale"
    },
    {
      "pattern": "upper_lower",
      "phase": "continuous"
    }
  ],
  "affect_target": {
    "valence": 0.25,
    "arousal": 0.15,
    "basis": "authored"
  }
}
```

This is a universal semantic object. Domain/profile layers may constrain values, but they do not create a competing ontology.

---

# 17. Worked example 1 — restrained dialogue

## Authoring YAML

```yaml
performance:
  phase: restrained_dialogue
  duration_s: 3.5

  face:
    - au: AU12
      side: bilateral
      intensity: B
    - au: AU6
      side: bilateral
      intensity: A

  gaze:
    direction: camera
    stability: high

  head:
    yaw_deg: 0
    pitch_deg: 2
    roll_deg: 0

  laban:
    effort:
      weight: light
      time: sustained
      space: direct
      flow: bound
    shape:
      horizontal: slightly_spreading
    phrasing:
      emphasis: middle

  bartenieff:
    - pattern: breath
      phase: exhale
    - pattern: upper_lower
      phase: continuous

  affect:
    valence: 0.25
    arousal: 0.15
```

## Resolved JSON

The YAML resolves to the canonical event shown above.

## Natural-language provider projection

> Maintain direct eye contact with the camera. Deliver the line calmly and continuously. Use a restrained bilateral smile: slight lip-corner lift with minimal cheek involvement. Keep the head nearly centered with only a slight upward pitch. The movement should feel light, controlled and contained, with emphasis around the middle of the phrase.

## Semantic preservation

Preserved:

- bilateral facial intent;
- relative intensity;
- temporal phrase;
- gaze;
- head orientation;
- Laban effort;
- shape;
- phrasing;
- breath/connectivity;
- affect target.

Compressed:

- formal FACS identifiers may be translated into natural-language visual descriptions;
- Bartenieff semantics may be expressed indirectly.

Not preserved exactly:

- provider-specific internal interpretation of AU labels.

---

# 18. Worked example 2 — explosive action

```yaml
performance:
  phase: explosive_action

  face:
    - au: AU4
      side: bilateral
      intensity: D
    - au: AU5
      side: bilateral
      intensity: C
    - au: AU26
      side: bilateral
      intensity: D

  laban:
    effort:
      weight: strong
      time: sudden
      space: direct
      flow: free
    shape:
      horizontal: spreading
      vertical: rising
      sagittal: advancing
    phrasing:
      emphasis: beginning

  bartenieff:
    - pattern: core_distal
      phase: expansion
    - pattern: cross_lateral
      phase: action
```

Natural-language projection:

> Begin with a sudden, forceful burst. Drive the movement directly toward the target with strong weight and rapid timing. Expand outward from the core through the limbs. The face should show pronounced brow lowering, widened upper eyelids and a strong jaw opening. Keep the first beat sharply emphasized.

Important: `strong`, `sudden`, and `free` are Laban semantics. They are not literal force, acceleration or absence of constraints.

---

# 19. Worked example 3 — stylized/anime performance

```yaml
performance:
  style: stylized_anime

  face:
    - au: AU1
      side: bilateral
      intensity: C
    - au: AU2
      side: bilateral
      intensity: C
    - au: AU5
      side: bilateral
      intensity: D

  gaze:
    direction: upward

  laban:
    effort:
      weight: light
      time: sudden
      space: indirect
      flow: free
    shape:
      vertical: rising
      horizontal: spreading

  bartenieff:
    - pattern: core_distal
      phase: expansion

  provider:
    style_policy: stylized
```

Compiler rule:

The provider adapter must not assume the provider can literally render anatomical AU semantics. It may translate the intent into visible descriptions:

> Exaggerated upward gaze, enlarged-looking eyes, raised brows, sudden light expansion, heightened stylized facial openness.

The adapter must record whether FACS-specific controls were:

```text
native
approximate
semantic
unsupported
```

---

# 20. Compiler semantics

The canonical flow is:

```text
research concept
  ↓
retrieved evidence
  ↓
director decision
  ↓
canonical semantic field
  ↓
control candidate
  ↓
provider capability check
  ↓
native / approximate / semantic / unsupported
  ↓
provider representation
  ↓
verification
  ↓
compilation-loss record
```

## Example: provider cannot express exact AU intensity

Canonical:

```json
{
  "au_id": "AU12",
  "intensity": {
    "value": "C",
    "basis": "facs_ordinal"
  }
}
```

Provider capability:

```json
{
  "control": "facs_AU12",
  "support": "semantic_only"
}
```

Compiler output:

> slight-to-moderate lip-corner lift, restrained smile, sustained through the middle of the phrase

Loss:

```json
{
  "control": "facs_AU12_intensity_C",
  "requested": "facs_ordinal:C",
  "compiled_as": "natural_language_visual_description",
  "loss_class": "representation_loss",
  "severity": "medium",
  "reason": "provider_has_no_native_facs_intensity_control"
}
```

The compiler must not claim exact preservation.

---

# 21. Provider capability taxonomy

Every provider-facing control should resolve to one of:

```text
native
  exact control exists

approximate
  measurable approximation exists

semantic
  natural-language semantic instruction is the only supported path

unsupported
  provider cannot meaningfully express the control
```

A fifth state is useful for research:

```text
unknown
  capability has not been verified
```

Unknown is not supported.

---

# 22. Representation equivalence

## YAML

Best for:

- human authoring;
- inheritance;
- profile overrides;
- compact scenario definitions.

## Canonical JSON

Best for:

- resolved meaning;
- validation;
- deterministic compiler input;
- schema checking;
- round-trip comparison.

## XML

Use only when an ordered/namespaced envelope provides an actual benefit.

Example:

```xml
<performance-event id="evt-0042">
  <face>
    <facs au="AU12" side="bilateral" intensity="B"/>
    <facs au="AU6" side="bilateral" intensity="A"/>
  </face>
  <laban>
    <effort weight="light" time="sustained" space="direct" flow="bound"/>
  </laban>
</performance-event>
```

XML adds:

- explicit ordering;
- namespace support;
- mixed-content possibilities.

It should not become a second semantic authority.

## Natural language

Natural language is the provider projection.

It should express **visible behavior and intended control**, not unsupported claims about private mental state.

---

# 23. Model-conditioning/data-language experiment

No evidence justifies declaring JSON, YAML, XML or natural language universally superior for CPCS providers.

Run a controlled experiment.

## Fixed semantic payload

Create 100 scenes with identical canonical JSON meaning.

Generate:

1. JSON;
2. YAML;
3. XML;
4. structured Markdown;
5. natural language;
6. hybrid structured + natural language.

Randomize presentation order.

## Measure

- schema adherence;
- control preservation;
- AU preservation;
- bilateral preservation;
- temporal-order preservation;
- Laban-factor preservation;
- Bartenieff-pattern preservation;
- omission rate;
- contradiction rate;
- provider adherence;
- token count;
- latency;
- regeneration rate.

## Statistical design

Use paired scene-level comparisons because the same semantic payload is tested across carriers.

Report:

```text
mean adherence
median adherence
95% CI
omission rate
contradiction rate
token cost
latency
```

Do not infer general superiority from one provider.

---

# 24. Verification suite

## Schema

```text
valid_json
valid_yaml
canonical_schema_pass
unknown_enum_rejected
missing_version_rejected
```

## FACS

```text
AU ID valid for declared version
intensity enum valid
left/right preserved
bilateral not silently averaged
temporal order valid
offset >= onset
apex inside onset/offset
unobservable state accepted
confidence range valid
```

## Laban

```text
effort factor enums valid
proxy != semantic field
unvalidated proxy cannot become canonical semantic value
coordinate frame declared for direction
```

## Bartenieff

```text
pattern enum valid
side preserved
connectivity interval valid
measurement basis explicit
```

## Affect

```text
affect_target != observed_emotion
private_mental_state rejected unless explicitly authored/hypothesized
valence/arousal scale declared
trajectory timestamps monotonic
```

## Compiler

```text
native control preserved
approximate control creates loss record
semantic projection creates loss record
unsupported required control fails closed
unknown capability cannot be silently treated as supported
```

---

# 25. Fixtures

Minimum fixture set:

```text
facs/
  au12_bilateral_b
  au12_left_c_right_b
  au7_vs_au6_confusion
  au23_vs_au24_confusion
  au12_temporal_overlap_au6
  legacy_41_version_rejection
  legacy_44_version_rejection
  occluded_left_eye
  missing_timestamp
  detector_presence_intensity_disagreement

laban/
  effort_strong_sudden_direct_free
  effort_light_sustained_indirect_bound
  shape_spread_rise_advance
  phrasing_beginning
  phrasing_middle
  phrasing_end
  directness_proxy_uncalibrated
  cross_subject_normalization_required

bartenieff/
  breath_inhale
  breath_exhale
  core_distal_expand
  core_distal_condense
  head_tail
  upper_lower
  body_half_left
  body_half_right
  cross_lateral
  connectivity_unknown

integration/
  restrained_dialogue
  explosive_action
  stylized_anime
  unsupported_facs_provider
  semantic_only_provider
  bilateral_loss
```

---

# 26. Implementation placement

Do not create a parallel subsystem.

Recommended placement:

```text
existing CPCS universal semantic kernel
  ├── facial/
  │   ├── facs schema/catalog
  │   ├── facs temporal event
  │   └── facs observation/audit
  │
  ├── movement/
  │   ├── laban schema
  │   ├── laban proxy measurement
  │   └── bartenieff connectivity
  │
  ├── expression/
  │   └── performance_expression_event
  │
  ├── affect/
  │   └── affect_target / trajectory
  │
  └── compiler/
      ├── provider capability mapping
      ├── approximation mapping
      └── compilation-loss records
```

Authority tiers:

```text
FACS:
  external authoritative vocabulary
  ↓
  CPCS versioned adapter/catalog

Laban:
  external semantic framework
  ↓
  CPCS universal semantic representation

Bartenieff:
  external connectivity framework
  ↓
  CPCS connectivity representation

Provider:
  provider documentation + measured experiments
  ↓
  adapter capability map
```

Graph status:

- research KG: stores source concepts, evidence, definitions and relationships;
- execution graph: stores runtime reasoning/selection;
- VOG: stores observed/measured facial/movement evidence;
- canonical semantic JSON: stores resolved intended controls;
- provider adapter: stores capability mappings and losses.

Do not put every raw FACS frame into the reusable research graph.

---

# 27. FACS/Laban/Bartenieff field dictionary

| Field | Type | Allowed values / shape | Meaning | Not meaning | Authority |
|---|---|---|---|---|---|
| `facs_version` | enum | `2002` etc. | scoring vocabulary version | not provider version | FACS authority |
| `au_id` | identifier | AU code | facial action identifier | not emotion | FACS |
| `side` | enum | left/right/bilateral/unknown | laterality | not body orientation | CPCS representation |
| `intensity.value` | ordinal | A-E | FACS intensity category | not force | FACS |
| `intensity.basis` | enum | facs_ordinal/project_normalized/model_score | scale basis | not interchangeable scales | CPCS |
| `onset_s` | number | >=0 | temporal onset | not causal onset | FACS temporal coding |
| `apex_start_s` | number | >= onset | peak interval start | not necessarily single frame | CPCS |
| `apex_end_s` | number | >= apex_start | peak interval end | not guaranteed by source | CPCS |
| `offset_s` | number | >= onset | temporal offset | not disappearance from all possible views | FACS temporal coding |
| `confidence` | number | 0..1 | confidence estimate | not probability of emotion | CPCS |
| `observability` | enum | observable/occluded/unobservable/unknown | measurement visibility | not truth value | CPCS |
| `laban.weight` | enum | light/strong | qualitative effort factor | not Newtons | LMA |
| `laban.time` | enum | sustained/sudden | qualitative temporal effort | not duration alone | LMA |
| `laban.space` | enum | indirect/direct | qualitative focus/path effort | not path straightness alone | LMA |
| `laban.flow` | enum | free/bound | qualitative control of flow | not jerk alone | LMA |
| `laban.shape.horizontal` | enum | spreading/enclosing | horizontal shape change | not width alone | LMA |
| `laban.shape.vertical` | enum | rising/sinking | vertical shape change | not height alone | LMA |
| `laban.shape.sagittal` | enum | advancing/retreating | sagittal shape change | not position alone | LMA |
| `laban.phrasing.emphasis` | enum | beginning/middle/end/etc. | phrase emphasis | not simply velocity peak | LMA |
| `bartenieff.pattern` | enum | six patterns | connectivity pattern | not scalar intensity | Bartenieff |
| `proxy.name` | identifier | project-defined | measurable approximation | not canonical semantic truth | CPCS experiment |
| `proxy.validation_status` | enum | uncalibrated/validated | calibration state | not confidence | CPCS |
| `affect.valence` | number | declared scale | authored/measured affect dimension | not FACS | affect model |
| `affect.arousal` | number | declared scale | activation dimension | not AU intensity | affect model |

---

# 28. Recommended universal ontology relations

Do not create dozens of new domain predicates.

Use existing universal relations where available and add only relationships that have executable consumers.

Useful relations:

```text
describes
targets
coactivates_with
temporally_overlaps
precedes
follows
measured_by
detected_by
derived_from
has_proxy
calibrated_by
confusable_with
nonadditive_with
constrained_by
compiled_to
approximates
unsupported_by
```

`approximates` is particularly important:

```text
Laban.direct
  --approximates-->
path_straightness
```

This prevents a proxy from becoming a semantic synonym.

---

# 29. Research-derived implementation decisions

## Decision 1 — FACS is a semantic control vocabulary, not an emotion ontology

**Implement now.**

## Decision 2 — FACS intensity remains ordinal

**Implement now.**

A project-normalized control can exist but must retain its mapping identity.

## Decision 3 — bilateral data is side-indexed

**Implement now.**

Never average left/right AU activation.

## Decision 4 — temporal events are first-class

**Implement now.**

Do not represent facial expression as a static bag of AUs.

## Decision 5 — automatic AU detection is evidence-producing, not authority-producing

**Implement now.**

Detector output is `detected` until validated under the project measurement contract.

## Decision 6 — Laban semantics and kinematic measurements remain separate

**Implement now.**

## Decision 7 — Bartenieff patterns are connectivity relationships

**Implement now.**

## Decision 8 — affect is a separate semantic layer

**Implement now.**

## Decision 9 — provider adapters may approximate but must disclose loss

**Implement now.**

## Decision 10 — numerical Laban mappings require calibration

**Experiment first.**

---

# 30. CPCS_CLOSURE_MATRIX

| Gap | Existing CPCS support | New knowledge required | New representation | Measurement | Compiler effect | Experiment needed | Priority |
|---|---|---|---|---|---|---|---|
| FACS versioning | partial temporal slice | 2002 version authority | `facs_version` | schema/version validation | reject ambiguous AU versions | no | P0 |
| AU catalog | partial | versioned AU vocabulary | AU catalog | coder/detector support matrix | map supported subset | yes for provider coverage | P0 |
| AU laterality | partial/unknown | bilateral/asymmetry semantics | side-indexed AU event | left/right agreement | preserve or loss | yes | P0 |
| AU intensity | partial | ordinal A-E semantics | typed intensity object | agreement/ICC/MAE | normalize only as derived | yes | P0 |
| AU timing | partial | onset/apex/offset | temporal event | onset/offset error | preserve timeline | yes | P0 |
| AU coactivation | partial | coactivation/nonadditivity | relation objects | co-occurrence | preserve combination | yes | P1 |
| AU confusion | absent | AU7/6, AU23/24 evidence | `confusable_with` | confusion matrix | lower confidence/flag | yes | P1 |
| Automatic AU evidence | partial | detector limitations | detection observation | precision/recall/F1 | gate promotion | yes | P0 |
| Affect separation | partial | FACS ≠ emotion | `affect_target` | trajectory agreement | project separately | yes | P0 |
| VAD trajectory | partial | continuous affect modeling | trajectory | CCC/MAE | compile semantic arc | yes | P1 |
| Laban Body | partial | BESS vocabulary | `laban_body` | keypoint/body-part detection | semantic projection | yes | P1 |
| Laban Effort | partial | four factors/elements | `laban_effort` | expert agreement | semantic/native/proxy | yes | P0 |
| Laban Space | partial | kinesphere/directions/pathways | `laban_space` | direction/path metrics | map to provider motion language | yes | P0 |
| Laban Shape | partial | shape qualities | `laban_shape` | body-envelope proxies | semantic projection | yes | P1 |
| Laban Phrasing | partial | phrase emphasis | `laban_phrasing` | temporal emphasis | preserve sequence | yes | P1 |
| Laban numeric mapping | partial | calibration evidence | typed proxy | ICC/MAE/held-out | never silently equate | yes | P0 |
| Laban reliability | partial | empirical limitations | confidence/reliability metadata | Krippendorff alpha | confidence-aware compilation | yes | P1 |
| Bartenieff six patterns | gap | pattern definitions | `bartenieff_connectivity` | classification agreement | semantic projection | yes | P0 |
| Breath | partial | pattern/phase semantics | breath event | audio/video/torso proxy | semantic projection | yes | P1 |
| Core-Distal | absent/partial | connectivity semantics | connectivity event | core-distal distance/phase | semantic projection | yes | P1 |
| Head-Tail | absent/partial | connectivity semantics | connectivity event | spine propagation proxy | semantic projection | yes | P1 |
| Upper-Lower | absent/partial | connectivity semantics | connectivity event | phase/contact proxy | semantic projection | yes | P1 |
| Body-Half | absent/partial | laterality | connectivity event | side coordination | preserve side | yes | P1 |
| Cross-Lateral | absent/partial | contralateral coordination | connectivity event | cross-body coordination | preserve relation | yes | P1 |
| Combined performance event | partial | cross-layer composition | `performance_expression_event` | multi-layer adherence | compile layered controls | yes | P0 |
| Provider capability | partial | actual provider behavior | capability map | adherence | native/approx/semantic/unsupported | yes | P0 |
| Representation carrier | existing YAML/JSON/XML | controlled carrier comparison | experiment harness | adherence/token/latency | choose per provider | yes | P1 |
| Verification fixtures | partial | semantic invariants | fixture suite | automated tests | fail closed | no | P0 |

---

# 31. PROPOSED_AGENT_BUILD_PACKET

## Concepts

```text
facs_version
facs_au
facs_event
facs_intensity
facs_temporal_segment
facs_coactivation
facs_confusion
facs_observation
affect_target
affect_trajectory
laban_body
laban_effort
laban_space
laban_shape
laban_phrasing
laban_proxy
bartenieff_connectivity
breath_event
performance_expression_event
provider_capability
compilation_loss
```

## Fields

Minimum FACS:

```text
facs_version
au_id
side
intensity.value
intensity.basis
temporal.onset
temporal.apex_start
temporal.apex_end
temporal.offset
timebase
evidence_class
confidence
observability
source_ref
```

Minimum Laban:

```text
body.parts
body.action
effort.weight
effort.time
effort.space
effort.flow
space.reach
space.zone
space.direction
space.pathway
shape.horizontal
shape.vertical
shape.sagittal
phrasing.emphasis
```

Minimum Bartenieff:

```text
pattern
side_relationship
regions
phase.start
phase.end
evidence_class
confidence
measurement.type
measurement.validation_status
```

## Schemas

Create:

```text
facs_event.schema.json
facs_observation.schema.json
affect_target.schema.json
affect_trajectory.schema.json
laban.schema.json
laban_proxy.schema.json
bartenieff_connectivity.schema.json
performance_expression_event.schema.json
provider_capability.schema.json
compilation_loss.schema.json
```

Do not duplicate schemas across domain profiles.

## Mappings

```text
FACS AU → visible facial description
FACS ordinal → project control only through explicit mapping
Laban semantic → provider natural-language projection
Laban proxy → semantic only after calibration
Bartenieff pattern → movement-relationship description
affect trajectory → provider emotional-performance language
```

## Compiler operations

```text
resolve_facs_version
validate_facs_event
preserve_laterality
compile_facs_to_provider
compile_laban_to_provider
compile_bartenieff_to_provider
compile_affect_to_provider
negotiate_capability
emit_approximation
emit_compilation_loss
fail_closed_on_required_unsupported_control
```

## Metrics

```text
AU precision
AU recall
AU F1
AU calibration
intensity ICC
intensity MAE
onset error
apex error
offset error
temporal IoU
left/right accuracy
bilateral preservation
Laban Krippendorff alpha
Laban proxy ICC
Laban proxy MAE
Bartenieff classification F1
provider adherence
semantic round-trip equivalence
omission rate
contradiction rate
token cost
latency
```

## Fixtures

Use the fixture list in Section 25.

## Tests

At minimum:

```text
test_facs_version_required
test_legacy_au_rejected_without_version
test_facs_intensity_not_numeric_truth
test_project_normalized_intensity_requires_mapping_id
test_left_right_not_averaged
test_bilateral_preserved
test_temporal_order
test_unknown_observability
test_detector_output_not_promoted_to_measured
test_affect_not_inferred_from_au
test_laban_proxy_not_semantic
test_unvalidated_proxy_not_compiled_as_exact
test_bartenieff_side_preserved
test_cross_lateral_not_collapsed
test_provider_unsupported_fails_closed
test_approximation_creates_loss
test_yaml_json_roundtrip
test_xml_semantic_equivalence
test_natural_language_projection_preserves_required_controls
```

## Open research questions

1. Which exact FACS AU subset should CPCS support natively versus through semantic projection?
2. Which provider models actually honor AU identifiers?
3. Which providers preserve bilateral/asymmetric instructions?
4. What is the provider-specific response to ordinal versus natural-language intensity?
5. Can Laban proxy features predict CMA labels across subjects?
6. Which Bartenieff patterns are reliably detectable from monocular video?
7. How should breath be estimated when audio is absent?
8. Which temporal carrier yields the highest provider adherence?
9. How much combined FACS/Laban/Bartenieff structure improves output versus a simpler semantic instruction?
10. What are the minimum controls required for each CPCS provider profile?

---

# 32. Final implementation conclusion

The closure should **not** create a new FACS graph, a new Laban ontology, a second movement compiler, or a monolithic "emotion" object.

The correct architecture is:

```text
AUTHOR / RESEARCH
       ↓
typed semantic intent
       ↓
canonical JSON
       ↓
 ┌───────────────┬────────────────┬──────────────────┐
 │ FACS          │ Laban          │ Bartenieff       │
 │ facial action │ movement       │ connectivity     │
 │ temporal      │ effort/space   │ patterns         │
 │ laterality    │ shape/phrasing │ breath           │
 └───────────────┴────────────────┴──────────────────┘
       ↓
measurement / observation / VOG
       ↓
provider capability negotiation
       ↓
native / approximate / semantic / unsupported
       ↓
provider projection
       ↓
rendered video
       ↓
VOG measurement
       ↓
adherence verification
       ↓
compilation loss / correction
```

The key semantic boundary is:

```text
FACS = visible facial action
Laban = qualitative movement organization
Bartenieff = connectivity organization
VAD/affect = higher-level authored/interpreted target
kinematics = measurement/proxy layer
provider prompt = projection
```

The most important implementation rule is that **qualitative movement frameworks must not be made artificially scientific by assigning arbitrary numbers to their labels**. Numeric measurements can be attached as proxies, but only after declaring what was measured, how it was measured, its coordinate/time basis, uncertainty, and whether the proxy has been calibrated against expert annotation.

This gives CPCS a single universal representation that is precise enough for compilation while retaining the epistemic distinction required by the master protocol.

---

# Source register

## FACS

- Paul Ekman Group. *Facial Action Coding System (FACS).* Current public FACS authority and 2002-version statement.
- Ekman, Friesen & Hager. *Facial Action Coding System*, 2002.
- Sayette, Cohn, Wertz, Perrott & Parrott. *A Psychometric Evaluation of the Facial Action Coding System for Assessing Spontaneous Expression.* Journal of Nonverbal Behavior.
- Cohn, Ambadar & Ekman. Research on automated measurement of facial expressions.
- Baltrušaitis et al. *OpenFace 2.0: Facial Behavior Analysis Toolkit.*
- Jacob & Stenger. *Facial Action Unit Detection With Transformers.* CVPR 2021.
- Fan et al. *Joint Facial Action Unit Intensity Prediction and Region Localisation.* ICME 2020.
- Russell, J. A. *A Circumplex Model of Affect.* Journal of Personality and Social Psychology, 1980. DOI: 10.1037/h0077714.

## Laban

- Bernardet et al. *Assessing the reliability of the Laban Movement Analysis system.* PLOS ONE, 2019. DOI: 10.1371/journal.pone.0218179.
- Palnick Tsachor & Shafir. *How Shall I Count the Ways? A Method for Quantifying the Qualitative Aspects of Unscripted Movement With Laban Movement Analysis.* Frontiers in Psychology, 2019. DOI: 10.3389/fpsyg.2019.00572.
- Laban/Bartenieff Institute of Movement Studies — authoritative institutional context.

## Bartenieff

- Bartenieff & Lewis. *Body Movement: Coping with the Environment.*
- Literature describing the six connectivity patterns of Bartenieff Fundamentals.
- Contemporary LBMS research distinguishing the broader Bartenieff Fundamentals practice from individual connectivity patterns.

---

# Evidence limitation

This document is **not a 100%-complete distillation of `CPCS_FACS_Laban_AI_Video_Research_Package_v1.2.zip`**, because that ZIP was named by the supplied prompt but was not attached in this session. The external verification is strong for the core semantic and measurement decisions, but package-specific claims, existing CPCS file names, existing schemas, and package-specific research conclusions cannot be certified until the frozen package itself is available.

The implementation decisions above are therefore suitable as a **research closure candidate / coding-agent build packet**, with the package-reconciliation pass still required before declaring the 02_FACS research layer fully closed.

---

# 18. OPERATIONAL REASONING / APPLICATION CLOSURE

## 18.1 Purpose of this expansion

The preceding closure establishes a strong semantic and measurement representation for FACS, Laban Movement Analysis, and Bartenieff concepts. It does not by itself make those concepts operationally selectable by an autonomous creative director.

This section closes that second layer.

The distinction is deliberate:

```text
semantic representation
    = what a concept means

operational knowledge
    = when the concept should be considered

application knowledge
    = when the concept should actually be selected

realization knowledge
    = what visible behavior the selected concept is intended to produce

composition knowledge
    = how selected concepts interact across frameworks and time

compiler knowledge
    = how the canonical control survives provider translation

verification knowledge
    = how the rendered result can be judged against the target
```

The operational layer must not silently redefine FACS, Laban, or Bartenieff. It is a CPCS reasoning layer around them.

The architecture therefore remains:

```text
research authority
      ↓
framework semantics
      ↓
APPLICATION KNOWLEDGE
      ↓
selected semantic controls
      ↓
REALIZATION KNOWLEDGE
      ↓
canonical performance-control IR
      ↓
provider compiler
```

### Epistemic rule

Every operational statement must identify its basis:

```text
source_established
source_supported_interpretation
cpcs_policy
derived
experimental_hypothesis
unknown
```

A coding agent must never convert `cpcs_policy` or `experimental_hypothesis` into an externally established fact.

---

# 19. THE APPLICATION KNOWLEDGE MODEL

## 19.1 Required concept lifecycle

Every framework concept that CPCS can retrieve should be traversable through the following lifecycle:

```text
concept
  ↓
meaning
  ↓
applicability
  ↓
contraindication
  ↓
context conditioning
  ↓
scope
  ↓
temporal behavior
  ↓
interaction
  ↓
observable realization
  ↓
provider compilation
  ↓
verification
```

A concept is **reasoning-complete** only when all applicable stages have either:

1. evidence-backed information;
2. an explicitly labeled CPCS policy;
3. an explicitly labeled experimental hypothesis; or
4. an explicit `unknown` state.

Silently leaving a stage unspecified is a closure gap.

## 19.2 `ApplicabilityRule`

`ApplicabilityRule` describes conditions under which a concept is relevant to a directing decision.

It is not itself a framework concept.

```yaml
applicability_rule:
  id: rule.laban.flow.bound.performance_control
  target_concept: laban.effort.flow.bound

  applies_when:
    - movement_requires_visible_control
    - director_intent_requires_restraint
    - action_requires_controlled_progression

  avoid_when:
    - intended_motion_requires_unrestricted_release

  does_not_imply:
    - rigid_motion
    - frozen_joints
    - low_velocity

  evidence_class: source_supported_interpretation
  confidence: medium
```

The example above is a representation pattern. Individual `applies_when` statements must be researched and classified before being promoted to authoritative CPCS knowledge.

## 19.3 Applicability dimensions

Applicability should be conditioned by the following context where relevant:

| Dimension | Example values | Why it matters |
|---|---|---|
| intent | restrained, explosive, hesitant | determines candidate behavior |
| action | walk, reach, strike, recoil | changes visible realization |
| actor role | initiator, reactor | changes timing and causality |
| shot scale | ECU, CU, medium, full-body, wide | determines observability |
| camera | static, tracking, handheld | changes movement interpretation |
| body scope | face, upper-body, full-body | determines useful controls |
| interaction | solo, dyadic, crowd | changes coordination |
| style | realistic, stylized, anime | changes acceptable exaggeration |
| temporal phase | anticipation, action, recovery | changes control application |
| provider | provider-specific capability profile | changes compilation |
| evidence state | authored, observed, measured | controls epistemic status |

These are contextual dimensions, not a second ontology.

---

# 20. `ContraindicationRule`

A reasoning system must know not only when to use a concept but when **not** to use it.

```yaml
contraindication_rule:
  id: rule.facs.au12.not_private_emotion
  target_concept: facs.au12

  do_not_infer:
    - private_happiness
    - sincerity
    - internal_emotional_state

  allowed_use:
    - authored_smile_display
    - observed_facial_movement

  evidence_class: source_established
```

The fundamental evidence boundary remains:

```text
AU12 observed
≠
person is happy
```

Likewise:

```text
Laban Strong
≠
actor is angry
```

and:

```text
Bartenieff Cross-Lateral
≠
actor is confident
```

A director may intentionally author an expressive performance that uses these concepts, but the observation layer must not reverse that authored control into an unsupported private-state claim.

---

# 21. GENERATIVE REALIZATION LAYER

## 21.1 Purpose

The research concepts are not necessarily the language understood directly by a video generator.

CPCS therefore needs an intermediate representation between semantic framework controls and provider syntax:

```text
framework semantic control
        ↓
observable / generative realization
        ↓
provider projection
```

This is **not** a replacement ontology for FACS, Laban, or Bartenieff.

It is a compiler-facing operational representation.

## 21.2 `RealizationPrimitive`

```yaml
realization_primitive:
  id: realization.decisive_weight_commitment
  source_controls:
    - laban.effort.weight.strong

  action_classes:
    - strike
    - push
    - pull

  observable_targets:
    - visible_weight_commitment
    - decisive_acceleration
    - grounded_support

  not_guaranteed:
    - exact_force_measurement
    - exact_laban_coder_score

  evidence_class: cpcs_proposed
  verification:
    - support_stability
    - trajectory_commitment
    - action_adherence
```

## 21.3 Realization primitive categories

Use a small number of operational categories rather than one primitive for every imaginable behavior:

```text
facial_change
facial_temporal_change
attention_shift
gaze_change
head_orientation_change
postural_change
weight_transfer
support_change
joint_chain_action
trajectory_change
acceleration_profile
movement_amplitude
movement_confinement
movement_release
shape_change
breath_change
rhythmic_accent
pause_or_hold
inter_actor_response
continuity_constraint
```

The category describes the **observable target**, not a claim about the underlying Laban or Bartenieff semantics.

---

# 22. ACTION-CONDITIONED REALIZATION

## 22.1 Why generic mappings are insufficient

A qualitative control does not necessarily have one universal visible manifestation.

The correct reasoning structure is:

```text
semantic control
× action class
× body scope
× temporal phase
× scene context
→ candidate realization
```

For example, the research may support `Strong` as a qualitative Effort factor, but CPCS should not assume that a single realization phrase works identically for a punch, walk, reach, recoil, or head turn.

## 22.2 Action realization matrix

The coding agent should maintain a matrix of evidence status:

| Semantic control | Action | Candidate realization | Status |
|---|---|---|---|
| Weight Strong | strike | committed weight transfer | proposed/verify |
| Weight Strong | walk | grounded weight transfer | proposed/verify |
| Weight Strong | reach | deliberate extension/commitment | proposed/verify |
| Time Sudden | strike | localized rapid action onset | source-supported + experiment |
| Time Sudden | head turn | rapid orientation change | proposed/verify |
| Flow Bound | delicate gesture | controlled progression | proposed/verify |
| Flow Free | ballistic release | less constrained continuation | proposed/verify |

The table is deliberately not an authority table. Each mapping requires source evidence or experiment before promotion.

## 22.3 Minimal-pair requirement

For every important realization mapping, create a minimal pair:

```text
same action
same actor
same camera
same scene
one semantic variable changed
expected visible difference
```

Example:

```text
A: Weight = Strong
B: Weight = Light

Expected test question:
Does the generated performance show a systematic difference in
weight commitment while preserving action identity and timing?
```

This becomes a regression fixture for the compiler and provider adapter.

---

# 23. CONTROL SCOPE

## 23.1 Scope is mandatory

A control without scope is ambiguous.

The same `bound` value could mean:

```text
whole performance
whole actor
upper body
right arm
single gesture
anticipation phase
recovery phase
```

CPCS therefore needs explicit scope.

## 23.2 Canonical scope object

```json
{
  "scope": {
    "scene": "scene_07",
    "shot": "shot_03",
    "actor": "actor_A",
    "interaction": "interaction_02",
    "action": "counter",
    "body_region": "right_arm",
    "phase": "preparation"
  }
}
```

All unspecified dimensions inherit from the enclosing execution context rather than becoming implicit global controls.

## 23.3 Scope inheritance

Recommended precedence:

```text
explicit local scope
    > event scope
    > shot scope
    > scene scope
    > project default
```

This is a **CPCS policy**, not a claim about FACS/Laban/Bartenieff.

If two controls conflict at the same scope and priority, the director must resolve the conflict explicitly or mark it unresolved.

---

# 24. CONTROL ENVELOPES

## 24.1 Static labels are insufficient

Performance qualities often evolve through a phrase.

CPCS should therefore support:

```text
state
transition
apex
recovery
```

rather than only:

```text
value = X
```

## 24.2 Canonical envelope

```json
{
  "control": "laban.effort.flow",
  "scope": {
    "actor": "A",
    "action": "counter"
  },
  "envelope": [
    {
      "phase": "anticipation",
      "value": "bound"
    },
    {
      "phase": "release",
      "transition": "bound_to_free"
    },
    {
      "phase": "action",
      "value": "free"
    },
    {
      "phase": "recovery",
      "value": "bound"
    }
  ]
}
```

This does not assert that every Laban factor has a universally correct numerical trajectory.

For qualitative controls, symbolic phase states are preferable unless the research establishes a defensible numeric representation.

## 24.3 Envelope types

```text
categorical_state_envelope
ordinal_envelope
continuous_measurement_envelope
event_envelope
phase_envelope
```

Each must declare its semantic basis.

---

# 25. TEMPORAL COUPLING

## 25.1 Performance is coordinated, not simultaneous

A `performance_expression_event` should not merely contain a bag of simultaneous fields.

It should support temporal relations:

```text
precedes
lags
synchronizes_with
peaks_with
holds_during
releases_after
triggered_by
```

## 25.2 Example

```yaml
coordination:
  - relation: precedes
    source: gaze_shift
    target: head_orientation

  - relation: precedes
    source: head_orientation
    target: torso_reorientation

  - relation: holds_during
    source: breath_hold
    target: anticipation

  - relation: synchronizes_with
    source: exhale
    target: action_release

  - relation: peaks_with
    source: facs.au4
    target: action_apex
```

The exact causal status must be separate from temporal status.

---

# 26. CAUSAL PERFORMANCE GRAPH

## 26.1 Temporal order is not causality

CPCS must distinguish:

```text
A precedes B
A causes B
A enables B
A correlates with B
A is motivated by B
```

These cannot be collapsed.

## 26.2 Example

```text
threat_recognition
      ↓ causes
attention_shift
      ↓ enables
head_orientation
      ↓ enables
visual_confirmation
      ↓ causes
postural_preparation
      ↓ enables
counter_action
```

This can coexist with temporal edges:

```text
recognition --precedes--> gaze
recognition --causes----> gaze
```

The two relations answer different questions.

## 26.3 Causal edge requirements

Every causal relation should contain:

```yaml
causal_edge:
  source:
  relation: causes | enables | prevents | motivates
  target:
  evidence_class:
  confidence:
  source_ref:
```

For creative authoring, a causal relation may be `authored` rather than empirically established.

---

# 27. CONTINUITY, PERSISTENCE, AND OCCLUSION

## 27.1 Observation versus world state

The following states must remain separate:

```text
visible
partially_visible
occluded
out_of_frame
unobservable
unknown
```

`occluded` does not mean `absent`.

## 27.2 Continuity contract

```yaml
continuity:
  entity: actor_A
  identity:
    status: persistent

  wardrobe:
    status: persistent

  pose:
    status: continuous
    allowed_changes:
      - authored_action

  facial_state:
    status: dynamic

  visibility:
    intervals:
      - start: 1.2
        end: 1.9
        state: occluded
```

## 27.3 Persistence semantics

Every important property should declare its lifetime:

```text
frame
instant
action_phase
action
shot
scene
sequence
project
```

Example:

```text
identity → project/scene persistent
AU activation → event/interval transient
Laban Effort quality → event/phrase scoped
wardrobe → scene/project persistent
gaze target → interval/event scoped
```

These are proposed CPCS defaults and must remain overridable by explicit authored intent.

---

# 28. OBSERVABILITY-CONDITIONED CONTROL SELECTION

## 28.1 Principle

A semantic control can remain part of canonical intent even when it is not worth sending to a provider because the shot cannot meaningfully display it.

Therefore distinguish:

```text
semantic relevance
visual observability
compilation value
```

## 28.2 Shot-scale guidance

This is a CPCS selection heuristic and requires provider experiments before being treated as a hard rule.

| Shot | High-value controls | Lower-value controls |
|---|---|---|
| ECU | FACS, gaze, eyelid/eye behavior | full-body connectivity |
| CU | FACS, gaze, head orientation | distal locomotor details |
| MCU | face + head + upper-body Effort | subtle foot mechanics |
| Medium | gaze, posture, Effort, Shape | tiny AU asymmetries |
| Full body | Laban, Bartenieff, support, trajectory | micro-FACS |
| Wide | spacing, trajectory, major Shape, rhythm | facial AU detail |
| Extreme wide | actor relationships, path, major action | most micro-expression |

The canonical intent is not deleted when a control is suppressed.

Instead:

```yaml
projection_decision:
  control: facs.au12
  semantic_status: required
  observability: low
  provider_projection: suppressed
  loss_type: low_observability
  verification: not_applicable
```

---

# 29. CONTROL PRIORITY AND ATTENTION BUDGET

## 29.1 Canonical richness versus provider bandwidth

The semantic model may legitimately contain many constraints.

The provider prompt should not necessarily contain all of them.

The compiler should perform:

```text
canonical intent
      ↓
salience ranking
      ↓
provider capability filtering
      ↓
attention budget
      ↓
minimal sufficient projection
```

## 29.2 Priority classes

Recommended CPCS policy vocabulary:

```text
locked
required
high
medium
low
optional
```

This is an engineering control vocabulary, not a Laban/FACS term.

## 29.3 Priority example

```yaml
priorities:
  identity: locked
  actor_count: locked
  action_order: locked
  contact_relationship: locked
  spatial_relationship: required
  performance_quality: high
  camera_behavior: high
  micro_expression: medium
  secondary_style: low
```

## 29.4 Attention budget

The compiler should be capable of saying:

```text
canonical controls: 31
provider-safe controls: 12
projected controls: 8
suppressed controls: 23
```

Suppression must produce a reason code.

Possible reasons:

```text
low_observability
provider_unsupported
redundant
conflicting
lower_priority
already_encoded_by_stronger_control
token_budget
```

---

# 30. CROSS-FRAMEWORK COMPOSITION

## 30.1 Non-additivity

FACS, Laban, Bartenieff, gaze, breath, posture and camera controls should not be treated as independent additive sliders.

A composition may:

```text
reinforce
constrain
conflict
subordinate
substitute
sequence
```

## 30.2 Composition record

```yaml
composition:
  id: composition.defensive_counter

  controls:
    - facs.au4
    - gaze.target.hands
    - laban.effort.flow.bound
    - laban.effort.space.direct
    - bartenieff.upper_lower

  interactions:
    - type: reinforces
      source: gaze.target.hands
      target: defensive_preparation

    - type: reinforces
      source: laban.effort.flow.bound
      target: restrained_action

    - type: constrains
      source: laban.effort.flow.bound
      target: follow_through

  evidence_class: cpcs_proposed
```

## 30.3 Saturation policy

A director should not stack multiple semantically redundant controls merely because they are available.

The compiler may reduce redundant controls when:

```text
control A already strongly expresses the same realization
control B adds little independent information
provider attention is limited
```

This must be logged as deterministic compiler behavior.

---

# 31. BODY TOPOLOGY AND SUPPORT BRIDGE

## 31.1 Purpose

Bartenieff connectivity often refers to relationships among body regions and patterns of whole-body organization. To become operational, CPCS needs a body-topology bridge.

The bridge is not another movement-analysis ontology.

It is an anatomical/kinematic representation layer.

## 31.2 Required body-topology concepts

```text
body_region
joint
joint_chain
effector
support_region
core
proximal_segment
distal_segment
ipsilateral_pair
contralateral_pair
support_chain
load_path
```

## 31.3 Example

```yaml
body_topology:
  actor: A
  action: counter_punch

  support_chain:
    - right_foot
    - right_leg
    - pelvis
    - torso
    - left_shoulder
    - left_arm
    - left_hand

  contralateral_relationship:
    - left_arm
    - right_leg
```

This is a **CPCS anatomical representation**, not a claim that Bartenieff itself defines this exact machine schema.

## 31.4 Support state

```yaml
support_state:
  base:
    type: asymmetric
    planted:
      left: true
      right: false

  load:
    dominant_side: left

  center_of_mass:
    direction: lowered

  transfer:
    from: left_leg
    through:
      - pelvis
      - torso
    toward: right_arm
```

Measurement of this state requires a declared pose/kinematic source and uncertainty.

---

# 32. MULTI-ACTOR PERFORMANCE COORDINATION

## 32.1 Why actor-local controls are insufficient

Cinematic performance is relational.

A response is often conditioned by another actor's action:

```text
Actor A initiates
       ↓
Actor B detects
       ↓
Actor B shifts attention
       ↓
Actor B prepares
       ↓
Actor A completes
       ↓
Actor B reacts
```

## 32.2 Interaction primitives

Use a small universal set:

```text
initiates
reacts_to
attends_to
tracks
mirrors
counters
synchronizes_with
leads
follows
turn_takes_with
approaches
withdraws_from
```

These are interaction semantics, not new FACS/Laban predicates.

## 32.3 Phase-offset representation

```json
{
  "interaction": {
    "initiator": "actor_A",
    "reactor": "actor_B",
    "trigger": "weapon_raise",
    "response": "defensive_shift",
    "phase_offset": {
      "value": 0.35,
      "unit": "s",
      "basis": "authored"
    }
  }
}
```

If the phase offset is measured from video rather than authored, it must be marked `measured` and include the timebase.

---

# 33. HIGH-LEVEL INTENT TO FRAMEWORK CONTROL

## 33.1 Avoid fixed semantic lookup

The reasoning system should not implement:

```text
restrained confidence → AU12 + Bound + Direct
```

as a universal lookup.

Instead:

```text
creative intent
      ↓
context interpretation
      ↓
candidate realizations
      ↓
framework candidate controls
      ↓
selection based on shot/action/interaction
```

## 33.2 Candidate mapping object

```yaml
intent_mapping:
  source_intent: restrained_confidence

  context:
    scene_type: dialogue
    shot_scale: close_up
    actor_role: speaker

  candidates:
    - control: facs.au12
      rationale: restrained_smile_candidate
      confidence: medium

    - control: gaze.stable_target
      rationale: sustained_attention_candidate
      confidence: high

    - control: laban.effort.flow.bound
      rationale: movement_restraint_candidate
      confidence: medium

  forbidden_inference:
    - private_confidence_state

  evidence_class: cpcs_proposed
```

The candidate list is not an instruction to use every item.

The director selects after considering context and salience.

---

# 34. SEMANTIC GUARDRAILS

Every high-value concept should have a machine-readable guardrail record.

```yaml
semantic_guardrail:
  concept: laban.effort.time.sudden

  means:
    - sudden_temporal_quality

  does_not_mean:
    - entire_clip_is_fast
    - maximum_velocity
    - zero_anticipation

  common_provider_failure:
    - globally_speed_up_motion

  mitigation:
    - localize_control_to_action_phase

  evidence_class: source_supported_interpretation
```

The same pattern applies to FACS and Bartenieff.

### FACS example

```yaml
semantic_guardrail:
  concept: facs.au12
  means:
    - visible_facial_action_as_defined_by_facs
  does_not_mean:
    - happiness
    - sincerity
    - private_emotional_state
  provider_failure:
    - exaggerated_smile
```

### Bartenieff example

```yaml
semantic_guardrail:
  concept: bartenieff.cross_lateral
  means:
    - cross_body_connectivity_pattern
  does_not_mean:
    - any_left_right_alternation
    - generic_coordination
  provider_failure:
    - arbitrary_arm_leg_crossing
```

The final statements require source/package verification before promotion to authority.

---

# 35. MINIMAL-PAIR AND COUNTEREXAMPLE CORPUS

## 35.1 Purpose

A reasoning model learns application boundaries more reliably when it can compare near-identical examples.

The closure package should therefore contain:

```text
positive example
negative example
minimal pair
counterexample
```

## 35.2 FACS minimal pair

```text
same actor
same shot
same action
same timing

A: AU12 lower ordinal intensity
B: AU12 higher ordinal intensity

Expected:
  visible magnitude difference
Not expected:
  automatic inference of happiness
```

## 35.3 Laterality minimal pair

```text
A: bilateral activation
B: left-dominant activation
```

Expected difference:

```text
left/right asymmetry
```

Not expected:

```text
automatic emotional interpretation
```

## 35.4 Laban minimal pair

```text
A: Strong
B: Light
```

All non-target variables remain constant.

Measure:

```text
action identity preserved?
trajectory preserved?
timing preserved?
visible weight-quality difference?
```

## 35.5 Bartenieff minimal pair

```text
A: Cross-Lateral
B: Body-Half
```

The fixture must define the intended movement context so that the distinction is not reduced to arbitrary limb crossing.

---

# 36. PROVIDER FALLBACK LADDER

## 36.1 Required behavior

Unsupported abstract concepts must not simply disappear.

The compiler should attempt a controlled fallback ladder.

```text
canonical semantic control
        ↓
provider-native exact control
        ↓ if unavailable
provider-native semantic equivalent
        ↓ if unavailable
observable behavioral realization
        ↓ if inadequate
reference/control representation
        ↓ if unavailable
unsupported
```

Each fallback creates a loss record.

## 36.2 FACS example

```text
FACS AU target
      ↓
provider has no AU control
      ↓
visible facial action description
      ↓
provider prompt
      ↓
verification
```

The provider prompt is not allowed to claim:

```text
"the actor feels happy"
```

when the canonical target was only a facial action.

## 36.3 Bartenieff example

```text
Cross-Lateral
      ↓
provider lacks Bartenieff vocabulary
      ↓
contralateral body-action realization
      ↓
provider projection
      ↓
video verification
```

## 36.4 Loss taxonomy

```text
unsupported_semantic
approximation
observability_loss
scope_loss
temporal_loss
laterality_loss
intensity_loss
causal_loss
continuity_loss
interaction_loss
priority_suppression
provider_attention_loss
```

---

# 37. VERIFICATION EXPECTATION MODEL

## 37.1 Metric alone is insufficient

Every compiled control should ideally resolve to:

```text
target
→ observable expectation
→ measurement method
→ metric
→ threshold
→ verdict
```

## 37.2 Example

```yaml
verification_expectation:
  target:
    control: laban.effort.flow.bound

  observable_expectations:
    - controlled_progression
    - reduced_uncontrolled_follow_through
    - continuous_articulation

  failure_signatures:
    - rigid_freeze
    - robotic_stiffness
    - excessive_follow_through

  measurement:
    type: mixed_human_kinematic_assessment

  verdict:
    threshold_status: experimental
```

The threshold remains experimental until validated.

## 37.3 FACS verification

Potential fields:

```yaml
facs_verification:
  au_id:
  target_presence:
  target_intensity:
  target_side:
  target_onset:
  target_apex:
  target_offset:

  observed:
    source: VOG

  metrics:
    presence_precision:
    presence_recall:
    intensity_agreement:
    onset_error_ms:
    apex_error_ms:
    offset_error_ms:
    side_accuracy:
```

## 37.4 Provider adherence

Provider adherence should be decomposed rather than represented as one opaque score:

```text
identity_adherence
action_adherence
spatial_adherence
temporal_adherence
performance_quality_adherence
facial_adherence
connectivity_adherence
camera_adherence
continuity_adherence
```

The final aggregate score is derived from these dimensions and must not hide catastrophic failure of a high-priority constraint.

---

# 38. PERFORMANCE EXPRESSION EVENT — REVISED CANONICAL FORM

The existing combined performance event should be extended to become an executable directing package.

```json
{
  "performance_expression_event": {
    "id": "evt_004",
    "actor": "actor_A",

    "intent": {
      "summary": "restrained defensive readiness",
      "evidence_class": "authored"
    },

    "context": {
      "action": "counter",
      "shot_scale": "medium",
      "interaction": "duet",
      "visibility": "full_upper_body"
    },

    "controls": [
      {
        "framework": "facs",
        "control": "AU04",
        "scope": {
          "actor": "actor_A",
          "phase": "anticipation"
        },
        "priority": "medium"
      },
      {
        "framework": "laban",
        "control": "effort.flow.bound",
        "scope": {
          "actor": "actor_A",
          "action": "counter",
          "phase": "preparation"
        },
        "priority": "high"
      },
      {
        "framework": "bartenieff",
        "control": "upper_lower",
        "scope": {
          "actor": "actor_A",
          "action": "counter"
        },
        "priority": "high"
      }
    ],

    "temporal_coordination": [],
    "causal_dependencies": [],
    "realizations": [],
    "persistence": [],
    "continuity": [],
    "conflicts": [],
    "observability": [],
    "provider_budget": {},
    "verification": {}
  }
}
```

This object remains a universal CPCS object. FACS/Laban/Bartenieff are typed values inside it rather than competing schemas.

---

# 39. YAML → JSON → XML → NATURAL LANGUAGE

## 39.1 Authoring YAML

```yaml
performance_event:
  intent: restrained_counter

  controls:
    - framework: laban
      concept: effort.flow.bound
      scope:
        phase: preparation
      priority: high

    - framework: laban
      concept: effort.time.sudden
      scope:
        phase: release
      priority: high

    - framework: bartenieff
      concept: cross_lateral
      scope:
        action: counter
      priority: medium

  temporal:
    - relation: transition
      source: effort.flow.bound
      target: effort.flow.free
      phase: release
```

## 39.2 Resolved JSON

The compiler resolves inheritance, aliases, defaults, explicit scope and evidence.

```json
{
  "event": "counter",
  "controls": [
    {
      "id": "laban.effort.flow",
      "value": "bound",
      "phase": "preparation",
      "priority": "high",
      "basis": "authored"
    },
    {
      "id": "laban.effort.time",
      "value": "sudden",
      "phase": "release",
      "priority": "high",
      "basis": "authored"
    },
    {
      "id": "bartenieff.cross_lateral",
      "value": true,
      "scope": "counter",
      "priority": "medium",
      "basis": "authored"
    }
  ]
}
```

## 39.3 Natural-language projection

```text
During the preparation, keep the movement controlled and restrained.
At the counter release, make the action sudden and decisive while
preserving the intended cross-body coordination. Maintain continuity
of the actor and the established body position.
```

This is a projection, not canonical truth.

## 39.4 XML

XML should only be emitted where ordered/namespaced event envelopes provide a real integration advantage.

```xml
<performance-event id="counter">
  <control framework="laban" concept="effort.flow" phase="preparation">
    <value>bound</value>
  </control>
  <control framework="laban" concept="effort.time" phase="release">
    <value>sudden</value>
  </control>
  <control framework="bartenieff" concept="cross_lateral">
    <value>true</value>
  </control>
</performance-event>
```

The XML adds ordering/namespacing, not new semantics.

---

# 40. RESEARCH-TO-RUNTIME GRAPH RELATIONS

The operational layer requires relations that answer application questions.

Recommended small closed relation vocabulary:

```text
applies_when
contraindicated_when
expressed_by
realized_by
modulates
reinforces
constrains
conflicts_with
requires
precedes
lags
synchronizes_with
causes
enables
persists_until
scoped_to
verified_by
compiled_via
fallback_to
```

These relations should not be dumped into the general research graph indiscriminately.

Recommended separation:

```text
Research Knowledge Graph
    = source-grounded concepts and evidence

Execution/Reasoning Graph
    = application rules, candidate controls, dependencies,
      temporal/causal decisions and runtime state

Video Observation Graph
    = measured/detected observations from rendered media
```

This preserves the master protocol's graph separation requirement.

---

# 41. RETRIEVAL REQUIREMENTS FOR AN AI DIRECTOR

A retrieval result should not return only:

```text
Laban Flow — Bound
```

It should ideally retrieve a compact application bundle:

```text
CONCEPT
DEFINITION
NON-MEANING
APPLICABILITY
CONTRAINDICATIONS
REALIZATION CANDIDATES
SCOPE
TEMPORAL BEHAVIOR
INTERACTIONS
GUARDRAILS
PROVIDER FALLBACKS
VERIFICATION
EVIDENCE
```

This is the difference between a dictionary lookup and reasoning-ready knowledge.

## 41.1 Retrieval packet example

```yaml
retrieval_packet:
  concept: laban.effort.flow.bound

  semantic:
    definition_ref: source_123

  application:
    applies_when:
      - rule_014
    avoid_when:
      - rule_022

  realization:
    candidates:
      - realization_031
      - realization_044

  composition:
    reinforces:
      - control_071
    conflicts:
      - control_082

  compiler:
    fallback:
      - fallback_009

  verification:
    fixture:
      - fixture_laban_flow_003
```

The model receives a decision-support packet instead of isolated terminology.

---

# 42. DIRECTOR DECISION PROCEDURE

The reasoning layer should follow a bounded procedure.

## Step 1 — Characterize intent

Extract:

```text
what should happen
how should it feel/appear
what must not happen
who acts
who reacts
where
when
shot scale
style
```

Do not infer private mental state as fact.

## Step 2 — Identify observable targets

Convert abstract intent into visible targets where possible:

```text
attention
facial display
posture
weight transfer
movement timing
trajectory
shape
connectivity
breath
interaction
```

## Step 3 — Retrieve candidate framework controls

Retrieve FACS/Laban/Bartenieff candidates with application rules.

## Step 4 — Filter by applicability

Reject concepts that:

```text
are contraindicated
are unobservable
are redundant
conflict with locked controls
lack sufficient evidence for the intended interpretation
```

## Step 5 — Scope controls

Attach:

```text
actor
body region
action
phase
shot
interaction
```

## Step 6 — Compose

Resolve:

```text
reinforcement
conflict
sequence
causal dependency
priority
```

## Step 7 — Generate realizations

Translate semantic controls into observable realization candidates.

## Step 8 — Negotiate provider capability

For each selected control:

```text
native
semantic equivalent
behavioral realization
reference/control
unsupported
```

## Step 9 — Apply attention budget

Keep the minimal sufficient set of provider instructions.

## Step 10 — Compile

Produce provider-specific projection and loss record.

## Step 11 — Verify

Compare rendered video against the original canonical target.

## Step 12 — Localize failure

Never rewrite the entire intent because one control failed.

Classify failure:

```text
identity
action
spatial
temporal
performance_quality
facial
connectivity
camera
continuity
provider_translation
```

Then correct the smallest responsible layer.

---

# 43. WORKED REASONING EXAMPLE — RESTRAINED DIALOGUE

## 43.1 Intent

```text
A veteran is confident but deliberately avoids displaying dominance.
He listens closely, maintains attention, gives a restrained response,
and does not overplay the emotion.
```

## 43.2 Canonical interpretation

```yaml
intent:
  display_targets:
    - sustained_attention
    - restrained_facial_display
    - controlled_gesture

  prohibited:
    - exaggerated_smile
    - theatrical_head_movement
    - excessive_gesture

  evidence_class: authored
```

## 43.3 Candidate controls

```text
FACS:
  candidate facial-action controls

Gaze:
  stable target attention

Laban:
  controlled movement quality candidate

Bartenieff:
  only if visible full-body organization is relevant
```

No automatic mapping to a private emotional state is permitted.

## 43.4 Shot conditioning

If the shot is a close-up:

```text
FACS → high value
gaze → high value
head orientation → high value
Laban full-body → suppressed
Bartenieff → suppressed unless upper-body pattern is visible
```

## 43.5 Projection

```text
Maintain direct visual attention and a restrained facial response.
Keep gestures controlled and economical. Avoid exaggerated emotional
facial movement or theatrical head motion.
```

The exact provider wording remains a compiler concern.

---

# 44. WORKED REASONING EXAMPLE — EXPLOSIVE ACTION

## 44.1 Intent

```text
The actor has been holding back. He suddenly commits to a decisive
counterattack and immediately regains control.
```

## 44.2 Temporal decomposition

```text
preparation
    ↓
controlled restraint
    ↓
release
    ↓
sudden action
    ↓
apex/contact
    ↓
controlled recovery
```

## 44.3 Candidate controls

```text
Laban:
  Time = Sudden at action release
  Weight = Strong candidate
  Flow = Bound → release → controlled recovery

Bartenieff:
  connectivity candidate conditioned by action mechanics

FACS:
  only if facial visibility makes it relevant
```

## 44.4 Important non-equivalences

```text
Sudden ≠ entire clip fast
Strong ≠ maximum physical force
Bound ≠ frozen
Cross-Lateral ≠ arbitrary limb crossing
```

## 44.5 Provider projection

The compiler should localize each quality to the relevant phase rather than producing a globally fast, globally exaggerated action.

---

# 45. WORKED REASONING EXAMPLE — STYLIZED / ANIME PERFORMANCE

## 45.1 Intent

```text
A stylized character appears motionless for a beat, then performs
an exaggerated directional action with a readable accent and recovery.
```

## 45.2 Reasoning

```text
pause/hold
    ↓
anticipatory state
    ↓
accented release
    ↓
large shape/trajectory
    ↓
recovery
```

The director may select exaggerated realization values as **creative choices**.

That does not alter the semantic definition of FACS, Laban, or Bartenieff.

The compiler should represent exaggeration as:

```yaml
style_modifier:
  exaggeration:
    basis: authored
    scope: action
```

not as:

```text
Laban Strong = exaggerated
```

because that would corrupt the domain semantics.

---

# 46. MEASUREMENT CONTRACT EXTENSION

The original measurement contract remains authoritative. This operational layer adds the following fields when a realization is being evaluated:

```text
semantic target
measurement source
observable manifestation
proxy definition
sampling rate
timebase
coordinate system
normalization
uncertainty
occlusion policy
camera-motion handling
aggregation
threshold
verdict
```

## 46.1 Semantic annotation versus measurement

Never write:

```text
measured_laban_strong = 0.82
```

unless a validated mapping exists.

Prefer:

```json
{
  "semantic_target": {
    "framework": "laban",
    "concept": "effort.weight.strong"
  },
  "proxy": {
    "name": "normalized_peak_acceleration",
    "value": 0.82,
    "basis": "derived"
  },
  "mapping_status": "experimental"
}
```

This preserves the difference between the qualitative construct and its kinematic proxy.

Research has demonstrated methods for quantifying selected LMA variables, but that does not establish a universal equivalence between every LMA category and a single physical measurement. citeturn0search3turn0search2

---

# 47. FACS AUTOMATION BOUNDARY

Automatic facial analysis should remain explicitly typed.

OpenFace publicly documents AU presence and intensity outputs, supports a subset of AUs, and warns that presence and intensity predictors are independently trained and may disagree. It also documents lower reliability for multi-person videos due to the lack of person-specific calibration. citeturn0search0turn0search1

Therefore CPCS should use:

```yaml
facs_observation:
  au_id: AU12
  presence:
    value: true
    basis: detected

  intensity:
    value: 3.2
    basis: model_score

  coder_equivalence:
    status: not_established

  calibration:
    status: unknown
```

The detector output may be useful for verification without being promoted to ground-truth FACS annotation.

---

# 48. LMA NUMERIC ENCODING BOUNDARY

LMA can be prepared for quantitative analysis, but quantitative analysis does not automatically transform qualitative LMA categories into universal physical measurements.

The research literature provides a methodology for selecting, coding and quantifying LMA-described variables for controlled studies. It explicitly describes repeated observation, expert coding, reduction of variables, Motif construction and statistical analysis. citeturn0search3

CPCS should therefore support three distinct representations:

```text
1. semantic LMA value
2. ordinal/project encoding
3. physical measurement proxy
```

Example:

```json
{
  "semantic": {
    "factor": "weight",
    "value": "strong"
  },
  "project_encoding": {
    "value": 1.0,
    "scale": "project_ordinal",
    "basis": "authored"
  },
  "measurement_proxy": {
    "name": "normalized_kinematic_feature",
    "value": 0.82,
    "basis": "derived",
    "calibration": "experimental"
  }
}
```

These values must never be silently substituted for one another.

The LMA reliability literature also supports maintaining uncertainty around coder-derived qualitative values rather than presenting them as mechanically objective measurements. citeturn0search2

---

# 49. MODEL-CONDITIONING EXPERIMENTS FOR THE OPERATIONAL LAYER

The master protocol requires controlled carrier experiments. The operational layer adds experiments for **semantic compression**.

## Experiment A — dictionary versus application packet

Compare:

```text
Condition A:
concept definition only

Condition B:
concept + applicability + guardrails

Condition C:
concept + applicability + guardrails + realization
```

Measure:

```text
concept selection accuracy
incorrect framework selection
unsupported inference rate
provider adherence
prompt length
latency
```

## Experiment B — generic versus action-conditioned mapping

```text
A: Strong → generic realization
B: Strong × action → realization
```

Measure action preservation and quality adherence.

## Experiment C — static versus temporal envelope

```text
A: Flow = Bound
B: Bound → Free → Bound
```

Measure temporal performance and phase localization.

## Experiment D — full graph versus compact retrieval packet

```text
A: retrieve all related research
B: retrieve compact application bundle
```

Measure:

```text
decision accuracy
contradiction rate
unsupported invention
token usage
latency
```

## Experiment E — minimal pair reasoning

Give the model controlled pairs and ask what visible change should result.

This measures whether the research has become operational knowledge rather than merely retrievable terminology.

---

# 50. REASONING COMPLETENESS SCORE

A concept-level closure score can be defined for internal auditing.

```text
RCS =
  semantic
+ applicability
+ contraindication
+ scope
+ temporal
+ interaction
+ realization
+ compiler
+ verification
```

Each dimension is scored:

```text
0 = absent
1 = proposed
2 = evidence-supported / experimentally validated
```

Do not interpret this as a scientific score. It is a CPCS engineering completeness index.

Example:

```yaml
reasoning_completeness:
  semantic: 2
  applicability: 2
  contraindication: 2
  scope: 1
  temporal: 2
  interaction: 1
  realization: 1
  compiler: 2
  verification: 1
  status: partial
```

A concept should not be marked `reasoning_complete` merely because its semantic definition scores 2.

---

# 51. AGENT RETRIEVAL CONTRACT

The retrieval layer should return structured knowledge with evidence boundaries.

```json
{
  "concept": "laban.effort.flow.bound",
  "semantic": {},
  "applicability": [],
  "contraindications": [],
  "scope_rules": [],
  "temporal_rules": [],
  "interaction_rules": [],
  "realization_candidates": [],
  "provider_fallbacks": [],
  "verification_expectations": [],
  "evidence": [],
  "uncertainty": []
}
```

The agent should be able to answer all of these questions before selecting the concept:

```text
What is it?
Why would I use it?
When should I avoid it?
What does it change?
Where does it apply?
How long does it apply?
What else does it interact with?
What visible result should I expect?
Can the provider express it?
How will I know whether it worked?
```

If retrieval cannot answer these questions, the concept should be treated as incomplete application knowledge.

---

# 52. IMPLEMENTATION PLACEMENT

The operational additions should be distributed into existing CPCS structures rather than creating a parallel FACS runtime.

| Addition | Preferred owner | New subsystem? |
|---|---|---|
| ApplicabilityRule | research/application knowledge | No |
| ContraindicationRule | research/application knowledge | No |
| RealizationPrimitive | canonical control library | No |
| ControlScope | universal semantic kernel | No |
| ControlEnvelope | universal semantic kernel | No |
| TemporalCoupling | execution/intent IR | No |
| CausalRelation | execution/intent IR | No |
| PersistenceConstraint | universal execution semantics | No |
| ContinuityState | VOG/execution bridge | No |
| ObservabilityRequirement | compiler/director policy | No |
| ControlPriority | universal execution semantics | No |
| ControlConflict | reasoning/validation | No |
| SupportState | body/kinematic representation | No |
| Interaction relation | execution reasoning graph | No |
| FallbackStrategy | provider compiler | No |
| VerificationExpectation | verification layer | No |

The existing CPCS components should own these concepts wherever an existing component can reasonably do so.

---

# 53. TEST FIXTURE REQUIREMENTS

The coding agent should create fixtures before implementing large runtime changes.

## Fixture classes

```text
FACS presence
FACS intensity
FACS laterality
FACS temporal onset/apex/offset
FACS occlusion
Laban effort minimal pair
Laban shape minimal pair
Laban phrasing
Bartenieff connectivity
Bartenieff body topology
cross-framework coordination
multi-actor response
control scope
control envelope
causal ordering
continuity through occlusion
provider fallback
provider attention suppression
```

## Fixture invariant

Every fixture must identify:

```text
canonical target
source/evidence basis
expected realization
forbidden realization
provider projection
verification metric
expected failure class
```

---

# 54. PROPOSED DIRECTOR CONTROL IR

A compact implementation target is:

```yaml
director_control:
  intent:
  context:
  controls:
    - framework:
      concept:
      value:
      scope:
      envelope:
      priority:
      evidence_class:

  composition:
    interactions:
    conflicts:
    dependencies:

  realizations:
    - primitive:
      target:
      confidence:
      basis:

  continuity:
  observability:
  provider_strategy:
  verification:
```

This is the recommended universal operational envelope.

It does not replace the semantic domain objects.

---

# 55. FAILURE-MODE CATALOG

The reasoning system should classify predictable failure modes.

| Failure | Meaning | Correct response |
|---|---|---|
| semantic_invention | unsupported meaning added | remove / mark unknown |
| private_state_inference | visible movement converted to internal state | downgrade interpretation |
| scope_leak | local control becomes global | restore scope |
| temporal_flattening | phrase reduced to static label | restore envelope |
| framework_collapse | Laban/Bartenieff/FACS treated as same thing | restore typed semantics |
| realization_overclaim | proxy treated as framework measurement | relabel proxy |
| provider_overtranslation | abstract concept exaggerated | use guardrail |
| control_saturation | too many redundant controls | rank/suppress |
| observability_mismatch | invisible control prioritized | suppress projection with loss |
| continuity_break | hidden state changes without cause | preserve persistence |
| causal_confusion | succession treated as causation | separate relations |
| interaction_desync | actors act independently when coupled | add coordination |
| fallback_loss | unsupported control silently dropped | emit loss record |
| verification_ambiguity | no observable success criterion | add expectation |

This table should become a test taxonomy rather than merely documentation.

---

# 56. OPEN RESEARCH QUESTIONS

The following questions should remain open until evidence or experiments close them:

1. Which FACS temporal tolerance windows are appropriate for CPCS verification across different frame rates and annotation protocols?
2. Which automatic AU detectors are sufficiently calibrated for project-level verification rather than exploratory detection?
3. Can project-normalized FACS intensity be calibrated across subjects and camera conditions without becoming misleading?
4. Which Laban qualities have reliable measurable proxies under controlled video conditions?
5. Which Laban-to-kinematic mappings generalize across action classes?
6. Which Bartenieff connectivity patterns can be reliably classified from pose sequences?
7. Which cross-framework interactions are supported by published research versus being useful CPCS engineering hypotheses?
8. How much provider adherence improves when realization primitives are inserted between semantic controls and natural language?
9. How much semantic compression can occur before provider adherence degrades?
10. What attention budget maximizes provider adherence for each target model?
11. Which shot-scale observability heuristics generalize across providers?
12. Can generated-video verification reliably detect qualitative Laban adherence, or must human/expert judgment remain in the loop?
13. Which continuity constraints can be measured automatically from the VOG?
14. Which actor-to-actor temporal dependencies are best represented as causal versus authored narrative relations?
15. How should stylized/anime performance modify realization without corrupting the underlying semantic framework?

Until experimentally closed, these should remain `unknown` or `experimental` rather than being silently promoted to canonical knowledge.

---

# 57. REVISED CPCS CLOSURE CRITERIA

The FACS/Laban/Bartenieff research package should not be declared fully closed until the following are satisfied.

## Semantic closure

```text
[ ] every required framework concept has a canonical definition
[ ] non-meanings are explicit
[ ] terminology ambiguity is resolved
[ ] evidence/provenance is attached
```

## Application closure

```text
[ ] applicability rules exist
[ ] contraindications exist
[ ] scope is defined
[ ] temporal behavior is defined
[ ] action conditioning is defined
[ ] observability conditions are defined
```

## Composition closure

```text
[ ] cross-framework interactions are represented
[ ] temporal coupling is represented
[ ] causal dependencies are distinct from succession
[ ] priority/conflict rules exist
[ ] saturation/attention policies exist
```

## Realization closure

```text
[ ] major concepts have realization candidates
[ ] realization evidence class is explicit
[ ] body-topology bridge exists where necessary
[ ] support/grounding semantics exist for relevant actions
[ ] minimal-pair fixtures exist
```

## Compiler closure

```text
[ ] native provider controls identified
[ ] semantic equivalents identified
[ ] behavioral fallbacks identified
[ ] unsupported states fail closed
[ ] compilation loss is recorded
```

## Verification closure

```text
[ ] every high-priority control has an observable expectation
[ ] metric is defined
[ ] threshold is defined or explicitly experimental
[ ] VOG observation mapping exists
[ ] failure class is localized
```

---

# 58. REVISED CPCS_CLOSURE_MATRIX

| Gap | Existing CPCS support | New knowledge required | New representation | Measurement | Compiler effect | Experiment needed | Priority |
|---|---|---|---|---|---|---|---|
| Applicability | semantic concepts | when concept should be selected | `ApplicabilityRule` | selection accuracy | filters candidates | yes | P0 |
| Contraindication | partial semantic guardrails | when concept must not be used | `ContraindicationRule` | false-selection rate | rejects controls | yes | P0 |
| Realization | provider projection | visible manifestation | `RealizationPrimitive` | target adherence | adds behavioral projection | yes | P0 |
| Action conditioning | limited | concept × action mapping | realization matrix | action-conditioned adherence | action-specific wording | yes | P0 |
| Scope | partial event context | exact target scope | `ControlScope` | scope preservation | prevents leakage | yes | P0 |
| Temporal envelope | temporal FACS support | evolving qualitative controls | `ControlEnvelope` | phase adherence | localized projection | yes | P0 |
| Cross-framework timing | combined event | sequencing and coupling | `TemporalCoupling` | lag/peak errors | ordered projection | yes | P0 |
| Causality | generic relations | cause/enable/motivation | causal edges | causal consistency | preserves action logic | yes | P0 |
| Continuity | observability | persistence through occlusion | `ContinuityState` | identity/state continuity | continuity instructions | yes | P0 |
| Persistence | implicit | property lifetime | `PersistenceConstraint` | state consistency | state locking | yes | P1 |
| Observability | partial | shot-conditioned utility | `ObservabilityRequirement` | control usefulness | suppression | yes | P1 |
| Priority | runtime intent | control hierarchy | `ControlPriority` | critical-control adherence | attention budget | yes | P1 |
| Composition | framework separation | reinforce/conflict/subordinate | `ControlComposition` | interaction adherence | control pruning | yes | P1 |
| Body topology | Bartenieff semantics | executable body relations | topology bridge | pose-chain metrics | realization generation | yes | P1 |
| Support | qualitative grounding | explicit support state | `SupportState` | COM/load/foot stability | action realization | yes | P1 |
| Multi-actor | actor-local controls | relational timing | interaction graph | phase-offset error | coordinated projection | yes | P1 |
| Semantic guardrails | partial | systematic non-meaning/failure rules | `SemanticGuardrail` | unsupported inference rate | safer projection | yes | P0 |
| Minimal pairs | worked examples | causal discrimination | fixture corpus | pairwise accuracy | regression | yes | P0 |
| Provider fallback | capability classes | fallback ladder | `FallbackStrategy` | semantic loss | alternate projection | yes | P0 |
| Verification expectation | metrics | target→expectation→threshold | `VerificationExpectation` | pass/fail | correction loop | yes | P0 |
| Retrieval completeness | KG concepts | application bundles | retrieval packet | decision accuracy | better director reasoning | yes | P0 |

---

# 59. PROPOSED_AGENT_BUILD_PACKET — OPERATIONAL EXPANSION

## Concepts

```text
ApplicabilityRule
ContraindicationRule
RealizationPrimitive
ControlScope
ControlEnvelope
TemporalCoupling
CausalRelation
ContinuityState
PersistenceConstraint
ObservabilityRequirement
ControlPriority
ControlConflict
ControlComposition
SupportState
BodyTopology
InteractionRelation
FallbackStrategy
SemanticGuardrail
VerificationExpectation
```

## Fields

Every operational control should support, as applicable:

```text
id
framework
concept
value
basis
evidence_class
confidence
scope
envelope
priority
applicability
contraindications
interactions
realizations
observability
persistence
continuity
provider_strategy
verification
source_ref
```

## Graph mappings

Use application relations:

```text
applies_when
contraindicated_when
expressed_by
realized_by
modulates
reinforces
constrains
conflicts_with
requires
precedes
lags
synchronizes_with
causes
enables
persists_until
scoped_to
verified_by
compiled_via
fallback_to
```

Do not create a new graph database or parallel ontology solely for these relations.

## Compiler operations

```text
resolve_scope
resolve_inheritance
validate_applicability
remove_contraindicated_controls
build_temporal_envelopes
resolve_control_conflicts
rank_control_salience
select_realizations
negotiate_provider_capabilities
apply_fallback_ladder
apply_attention_budget
emit_provider_projection
emit_compilation_loss
emit_verification_plan
```

## Metrics

```text
concept_selection_accuracy
contraindication_violation_rate
scope_preservation
phase_preservation
causal_edge_preservation
realization_adherence
cross_framework_coordination
continuity_adherence
provider_adherence
semantic_loss
unsupported_inference_rate
minimal_pair_accuracy
```

## Fixtures

```text
facs_laterality_minimal_pair
facs_intensity_minimal_pair
facs_temporal_fixture
laban_effort_minimal_pair
laban_shape_minimal_pair
laban_phrase_fixture
bartenieff_connectivity_fixture
body_topology_fixture
cross_framework_timing_fixture
causal_performance_fixture
occlusion_continuity_fixture
multi_actor_response_fixture
provider_fallback_fixture
attention_budget_fixture
observability_fixture
```

## Required tests

```text
test_scope_does_not_leak

test_local_temporal_control_does_not_globalize

test_facs_does_not_infer_private_emotion

test_laban_proxy_does_not_claim_semantic_measurement

test_bartenieff_pattern_does_not_collapse_to_generic_crossing

test_occlusion_does_not_delete_persistent_state

test_unsupported_provider_control_emits_loss

test_low_observability_control_can_be_suppressed

test_locked_constraint_survives_attention_budget

test_minimal_pair_changes_only_target_control

test_causal_edges_are_not_serialized_as_temporal_edges

test_cross_framework_controls_preserve_framework_identity
```

## Open research questions

Use the open questions in Section 56 as the research queue. Do not close them through implementation convenience.

---

# 60. FINAL OPERATIONAL VERDICT

The FACS/Laban/Bartenieff closure should now be considered two-layered:

```text
LAYER 1 — SEMANTIC / MEASUREMENT CLOSURE

What is the concept?
What does it mean?
How is it measured?
What is observable?
What is uncertain?
```

and:

```text
LAYER 2 — APPLICATION / CONTROL CLOSURE

When should it be used?
When should it be avoided?
What does it scope over?
How does it evolve through time?
What does it interact with?
What visible behavior should it produce?
How does action context alter realization?
How does it survive provider compilation?
How is success verified?
```

The second layer is the major addition required to make this research usable by an autonomous CPCS director.

The architectural conclusion is therefore:

```text
DO NOT expand FACS/Laban/Bartenieff into larger parallel ontologies.

DO expand the universal CPCS operational layer around them.
```

The research frameworks remain authoritative semantic sources. The operational layer records evidence-backed application rules, explicit CPCS policy, experimentally supported mappings, and unresolved hypotheses without conflating those categories.

That keeps the universal semantic kernel intact while giving the reasoning layer enough structure to move from:

```text
"I know what Bound means."
```

to:

```text
"Given this intent, action, shot, actor, phase, and provider,
Bound is or is not an appropriate candidate; if selected it applies
only to this scope and phase, interacts with these controls, should
produce these observable characteristics, and has this fallback and
verification strategy."
```

That is the intended research-to-runtime closure.

---

# 61. FINAL STATUS

**Semantic closure:** STRONG / conditional on frozen-package reconciliation.

**Measurement closure:** STRONG / proxy calibration remains experimental where noted.

**Application closure:** SUBSTANTIALLY EXPANDED; remaining gaps are primarily evidence validation and controlled experiments.

**Composition closure:** PARTIAL; framework interactions require targeted research and fixtures.

**Compiler closure:** STRONG architectural contract; provider-specific realization quality remains empirical.

**Verification closure:** STRONG contract; thresholds for qualitative realization remain experimental.

**Autonomous reasoning readiness:** IMPROVED FROM REPRESENTATION-READY TO OPERATIONALLY REASONING-READY IN ARCHITECTURE, BUT NOT YET SCIENTIFICALLY VALIDATED AS A COMPLETE AUTONOMOUS DIRECTOR.

**Frozen research-package reconciliation:** OPEN until `CPCS_FACS_Laban_AI_Video_Research_Package_v1.2.zip` is supplied.

**Repository modification:** NONE.
