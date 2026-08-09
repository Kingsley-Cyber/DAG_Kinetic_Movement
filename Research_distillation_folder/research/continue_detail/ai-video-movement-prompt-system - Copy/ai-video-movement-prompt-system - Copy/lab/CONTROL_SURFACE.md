# Control Surface — the full map of what we can control (and what's unexplored)

> This is the *working* view of active channels. The **complete research-grounded inventory** — every
> modular concept in the paper with section refs and lab status — is `CONCEPT_INDEX.md`.

There are **two control paradigms** in this system. Most work so far has explored only the first.
This file catalogs every control *channel*, its paradigm, whether it's been tested, and a test idea —
so the lab can drive experiments against the gaps. Update `status` + `evidence` as runs come in.

## The two paradigms

| Paradigm | What the model consumes | Best for | Proven in |
|---|---|---|---|
| **descriptive_prose** | natural-language description | look, skin, vibe, performance *feel* (UGC) | v001–v004 |
| **numeric_canonical_truth** | explicit numeric tracks (keyframes, timings, vectors) | precise motion, choreography, timing, contact, identity lock | v005 (combat) |

Key finding (p008): for **motion/choreography**, numeric canonical truth carries precision prose
cannot — v005 was driven by JSON *alone* ("really good hand-to-hand… good for anime"). This refines
p006: format is realism-neutral for *look*, but numeric structure is a genuine control channel for
*motion*.

## Channel catalog

Status: `proven` (a good run confirms it) · `partial` (bundled/seen, not isolated) · `unexplored`.

### A. Descriptive-prose channels (look & feel)
| Channel | Controls | Status | Evidence |
|---|---|---|---|
| camera.device / iPhone signature | realism of image | proven | v001 |
| lighting (flat/window/…) | cinematic vs raw | partial | v003 vs v001 |
| skin.strategy (microtexture vs smooth) | the #1 AI tell | **proven** | v001 vs v004 |
| performance.direction (loose vs scored) | ad vs candid | partial | v003 |
| face.motion (descriptive) | stiff vs alive face | partial | v001 |
| render_style (raw vs cinematic) | reads as UGC vs ad | partial | v003 vs v001 |

### B. Numeric-canonical-truth channels (motion & precision)
| Channel | Controls | Status | Evidence / Test idea |
|---|---|---|---|
| body kinematics (`root_motion` + `joint_tracks` position keyframes) | exact limb/body trajectories | **proven** | v005 |
| contact solver (`contacts`: region_a/region_b, timing, tolerance, type impact/near_miss/grasp) | strikes land, timing, no phasing | **proven** | v005 |
| Laban effort as numeric vectors (`lab_control` weight/time/space/flow ∈ [-1,1] over intervals) | movement *quality* per beat | **proven (combat)** | v005 — **unexplored for UGC/face** |
| camera keyframes (position/orientation over time) | shot path, framing over time | proven (combat) | v005 — **unexplored for UGC** |
| hard-constraint + verification blocks (identity_lock, no_slow_mo, contact tolerance, machine-checkable) | enforce & auto-grade the render | partial | v005 authored them; **verification not yet run against an output**. But `scripts/validate_kinematics.py` now auto-checks the CANON for internal consistency BEFORE render (v006). |
| kinematic self-consistency (reach feasibility, frame math, velocity coherence, contact geometry, foot grounding) | catch impossible motion in the canon before it reaches the model | **proven-tooling** | `validate_kinematics.py` caught v005's 0.18m reach deficit (fighters too far apart to touch at a declared contact) — the source of "good but not precise." v006 is reach-verified, 0 failures. |
| joint rotations + velocity vectors + per-segment easing (cpcs/1.2) | strike snap, pronation, accel-to-contact — precision v005's position-only tracks lacked | partial | v006 authored; not yet A/B'd vs v005 |
| foot-contact track (plant/release/pivot) | kills foot-sliding, the #1 AI motion tell | partial | v006 new channel |
| microvariation / transition_smoothness / biomechanical realism | naturalness of motion | unexplored | present in YAML, never isolated |

### C. Unexplored control sub-concepts (the frontier you flagged)
These are the biggest opportunities — none tested yet.

1. **FACS as a numeric AU track (facial canonical truth).** We've only used FACS *descriptively*.
   Build a time-indexed AU-intensity track (like `joint_tracks`, but per action unit) as canonical
   truth for a talking-head. *Test:* does an AU curve improve lip-sync + expression precision vs prose
   FACS? Domain: ugc_talkinghead + anime.
2. **Body-control adjustment as tracks.** Center-of-mass / balance curve, weight-shift curve, gaze
   vector over time, breathing amplitude — as numeric channels rather than words. *Test:* gaze-vector
   track vs "gaze-to-lens 0.7" prose — which holds eye contact better?
3. **Effort-vector control for non-combat.** Apply `lab_control` effort ramps to a UGC gesture or a
   dance. *Test:* does a light/sudden effort vector on the hook beat read as more alive than prose?
4. **Contact taxonomy beyond combat.** grasp / press / tap / hold-object contacts for product
   handling. *Test:* does a `contact` on hand↔product fix floaty product holds in UGC?
5. **Style medium channel.** `medium: photorealistic | anime_cel | 2.5d`. v005 was flagged "good for
   anime." *Test:* same kinematic truth, medium=anime_cel vs photorealistic.
6. **Speed / time-warp channel.** Currently forced to 1.0x. *Test:* controlled ramp on the apex frame
   only — does it help or break "no slow-mo" realism?
7. **Identity-lock tokens / reference binding.** v005 asserts `identity_score>=0.95` as a constraint;
   we haven't tested what actually holds identity across fast motion (reference image? seed? token?).
8. **Verification loop (closed feedback).** Actually *run* the `verification.metrics` against a
   generated clip (contact timing, identity drift, cut detection) instead of only authoring them.
   This turns the lab from manual scoring toward auto-scoring. **PARTIAL:** the *pre-render* half is
   done — `scripts/validate_kinematics.py` grades the canon for internal consistency (reach, frame
   math, velocity, geometry, grounding) and caught the v005 reach deficit. The *post-render* half
   (measuring an actual output) is still open.

### The v005 -> v006 precision lesson (key finding, 2026-07-20)

v005 (numeric kinematic JSON) was rated "good but not as precise — it forced a weak model to actually
produce good outputs." Root cause, found by tooling not by eye: **v005's contact events asserted
strikes the position tracks could not physically produce** — fighters were 1.60m apart at the c01
contact but their combined reach is 1.42m (0.18m deficit). Given contradictory numbers (positions say
"apart", contacts say "touching"), the model reconciles them by approximating — which reads as
imprecise. **Takeaway: numeric canonical truth only helps if it is internally consistent. An
inconsistent canon is worse than prose because it actively fights itself.** v006 fixes the geometry,
adds the missing precision channels (rotations, velocity, easing, foot-contacts, impulse), and ships
`validate_kinematics.py` so the canon is machine-checked before it ever reaches the model.

## How to explore a channel

Pick a row with `status: unexplored`, create a variant that toggles just that channel (hold the rest
constant), render A/B, log runs, and — if it moves a dimension — promote a pattern. Add new lever
values to `registry.yaml → levers` when a channel becomes a recurring knob (e.g.
`facial_control: {values: [prose_facs, au_track]}`).
