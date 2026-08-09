# Combat Choreography Reference (for fight / action sequences)

Extends the CPCS method from talking-head UGC into fight choreography. The core FACS + Laban + body
movement layers still apply — this document adds the **mathematical metrics layer** that fight
sequences require: kinematics, frame timing ratios, spatial geometry, power curves, and constraints
with numerical tolerances.

Use this alongside `facs_laban_reference.md` (the face + movement quality catalog) and the combat
templates:
- **Authoring layer** (YAML): `../assets/combat_control_package.template.yaml`
- **Kinematic data layer** (JSON): `../assets/combat_kinematics.template.json`

Worked examples:
- `../lab/variants/naruto_sasuke_rooftop_clash.yaml` (10s shonen anime fight, authoring layer)
- `../assets/combat_kinematics.fast_exchange.example.json` (8s kung fu exchange, kinematic layer)

## Table of contents
0. Two-document architecture
1. Why fights need math that UGC doesn't
2. Kinematics (the motion numbers)
3. Frame timing (animation math)
4. Spatial geometry (the arena)
5. Tempo and rhythm (fight BPM)
6. Power curves (escalation math)
7. Character profiles (body math)
8. FACS for combat (face in a fight)
9. Laban for combat (movement quality in strikes)
10. Constraints with tolerances
11. Camera math for fights
12. Style-specific notes (shonen anime, wuxia, MMA, etc.)

---

## 0. Two-document architecture

Combat CPCS uses two companion documents that serve different consumers:

```
┌──────────────────────────────────┐     ┌──────────────────────────────────┐
│  AUTHORING LAYER (YAML)          │     │  KINEMATIC DATA LAYER (JSON)     │
│                                  │     │                                  │
│  Human-readable creative         │     │  Machine-readable motion data    │
│  direction. The director's       │◄───►│  from a solver or hand-authored. │
│  intent.                         │     │  The physics.                    │
│                                  │     │                                  │
│  Contains:                       │     │  Contains:                       │
│  • beats (action descriptions)   │     │  • joint-level xyz tracks        │
│  • FACS (AU codes, categorical)  │     │  • root motion paths             │
│  • Laban (named Efforts)         │     │  • typed contact events          │
│  • body mechanics (prose)        │     │  • Laban (continuous floats)     │
│  • camera (descriptive)          │     │  • camera spatial path           │
│  • constraints (rules)           │     │  • verification metrics          │
│  • compiled_prompt (output)      │     │  • provenance links              │
└──────────────────────────────────┘     └──────────────────────────────────┘
              │                                        │
              └──────────────┬─────────────────────────┘
                             │
                    compiled_prompt (prose)
                             │
                        video model
```

**The authoring doc says WHAT happens.** It's where the creative decisions live — beat structure,
facial performance, movement quality, camera intent, narrative arc. A human (or agent) writes this.

**The kinematic doc says WHERE and WHEN in coordinate space.** It's the motion data — actual xyz
positions per joint per timestep, contact events with body-region mapping, Laban as continuous float
values, camera as a motion path. A solver generates this (or it's hand-authored for precision work).

**Provenance links connect them.** The kinematic JSON's `provenance` field points back to the
authoring YAML that defined the creative intent. The authoring YAML's `imports` can reference the
kinematic JSON as input data.

### Key differences between the two layers:

| Aspect | Authoring (YAML) | Kinematic (JSON) |
|--------|-----------------|-------------------|
| Laban representation | Categorical ("Thrust", "Slash") | Continuous floats (weight: 0.8, time: 0.9) |
| Body mechanics | Prose ("torso rotates 35°") | xyz coordinates per joint per timestep |
| Camera | Descriptive ("low angle tracking") | Spatial path (x/y/z + yaw/pitch over time) |
| Contacts | Implied by beat descriptions | Explicit events with actor/region/time/type/tolerance |
| Validation | Constraint rules (prose) | Metric targets with numerical tolerances |
| Consumer | Human author / AI agent | Motion solver / validator / pipeline |

### Laban float encoding:

The kinematic layer encodes Laban as continuous values instead of categories:

| Axis | Range | Low end | High end |
|------|-------|---------|----------|
| weight | 0.0 – 1.0 | light (0.2) | strong (0.8) |
| time | 0.0 – 1.0 | sustained (0.2) | sudden (0.9) |
| space | 0.0 – 1.0 | indirect (0.3) | direct (0.9) |
| flow | -1.0 – 1.0 | bound (-0.5) | free (0.5) |

Named Effort float signatures:

| Effort | weight | time | space | flow |
|--------|--------|------|-------|------|
| Thrust | 0.8 | 0.9 | 0.9 | -0.3 |
| Slash | 0.8 | 0.9 | 0.3 | 0.3 |
| Punch | 0.8 | 0.9 | 0.9 | 0.2 |
| Press | 0.8 | 0.2 | 0.9 | -0.4 |
| Flick | 0.2 | 0.9 | 0.3 | 0.4 |
| Dab | 0.2 | 0.9 | 0.9 | -0.3 |
| Float | 0.2 | 0.2 | 0.3 | 0.4 |
| Wring | 0.8 | 0.2 | 0.3 | -0.4 |
| Glide | 0.2 | 0.2 | 0.9 | 0.3 |

### Contact event types:

| Type | Meaning |
|------|---------|
| `impact` | Strike lands on target (punch connects, kick lands) |
| `near_miss` | Strike passes close but doesn't connect (dodge, duck) |
| `block` | Defensive stop — force absorbed, no pass-through |
| `grasp` | Grab and hold (clinch, arm catch) |
| `grasp_and_shove` | Grab then push (catch and redirect) |

Each contact specifies `actor_a`/`actor_b`, `region_a`/`region_b` (body part labels from the
skeleton ref), `start_s`/`end_s`, and `tolerance_m` (maximum allowed distance between regions at
contact time).

### When to use which layer:

- **Just writing a prompt for a video model?** Authoring YAML only. The compiled_prompt is prose.
- **Building a motion pipeline / validating choreography?** Both layers. The kinematic JSON feeds
  the solver/validator; the authoring YAML carries the creative intent.
- **Hand-authoring precise coordinate data?** Write the kinematic JSON directly, then back-derive
  the authoring YAML for the human-readable version.
- **Using a motion solver?** Author the YAML first (creative intent), feed it to the solver, get
  the kinematic JSON back, validate contacts, then compile both into prose.

## 1. Why fights need math that UGC doesn't

A UGC talking-head prompt needs **performance specificity** — the face, the body language, the
micro-movements that read as "real person." The CPCS method handles that with FACS events, Laban
efforts, and body-movement tracks.

A fight sequence needs all of that **plus biomechanical precision**:
- How fast is the fist moving at contact?
- How many frames between anticipation and contact?
- What's the exact rotation on a spinning kick?
- How far apart are the fighters at each moment?
- Does the power escalate across the arc or plateau?

Without these numbers, the compiled prompt becomes vague action description — "they fight fast" — and
the model defaults to generic motion with no choreographic specificity. The mathematical scaffolding
forces you (or the agent) to commit to exact values, which produces prompts with concrete physical
detail the model can render.

## 2. Kinematics (the motion numbers)

Every beat in a combat control package needs a `kinematics` block with measured values. These are the
physics of the fight.

### Required per beat:

| Metric | Unit | What it measures | Example |
|--------|------|------------------|---------|
| `closing_speed_ms` | m/s | Combined velocity of both fighters closing the gap | 16.0 (both at 8 m/s) |
| `char_a_velocity_ms` | m/s | Individual fighter velocity | 3.5 |
| `screen_velocity_pct_s` | % | How fast a character crosses the screen width per second | 45 |
| `gap_start_m` | m | Distance between fighters at beat start | 10.0 |
| `gap_end_m` | m | Distance at beat end | 0.6 |
| `strike_velocity_ms` | m/s | Fist/weapon speed at contact | 8.5 |
| `torso_rotation_per_strike_deg` | ° | Rotational power generation per strike | 35 |
| `body_lean_angle_deg` | ° | Forward/backward pitch of the body | 25 |
| `recoil_distance_m` | m | How far a limb bounces back on a blocked strike | 0.08 |
| `weight_transfer_time_ms` | ms | Time to shift weight between strikes | 120 |

### Domain-specific additions:

| Context | Metrics to add |
|---------|---------------|
| Aerial / flips | `flip_arc_height_m`, `flip_rotation_deg`, `flip_duration_s`, `flip_peak_at_s` |
| Projectiles | `projectile_velocity_ms`, `deflection_angle_deg` |
| Energy / VFX | `sphere_radius_growth`, `sphere_rpm`, `shockwave_radius_growth_ms` |
| Grappling | `grip_force_relative`, `leverage_angle_deg`, `rotation_axis` |
| Weapons | `blade_arc_deg`, `swing_speed_ms`, `parry_angle_deg` |

### Velocity reference (realistic human ranges):

| Action | Typical m/s | Elite m/s |
|--------|-------------|-----------|
| Walking | 1.4 | — |
| Sprint | 7–9 | 10–12 |
| Jab | 6–8 | 10–14 |
| Cross / straight | 8–10 | 12–15 |
| Roundhouse kick | 10–14 | 16–20 |
| Thrown projectile (knife) | 10–15 | 18–25 |
| Anime / superhuman | scale up 1.5–3× | — |

## 3. Frame timing (animation math)

Frame timing is how long each phase of a strike lasts, measured in frames. This is the single most
important layer for fight readability — it determines whether a strike reads as powerful or weak.

### The strike timing breakdown:

```
anticipation → contact → follow-through → recovery
(wind-up)      (impact)   (momentum)       (reset)
```

| Phase | Purpose | Typical frames (24fps) | Ratio |
|-------|---------|----------------------|-------|
| Anticipation | Wind-up, loading power | 2–4 | 25–35% |
| Contact | Impact moment | 1–2 | 10–15% |
| Follow-through | Momentum carrying past target | 2–4 | 25–35% |
| Hold / recovery | Held impact frame or reset | 1–4 | 15–30% |

### Animation exposure (1s, 2s, 3s):

| Exposure | Meaning | Use for |
|----------|---------|---------|
| **On 1s** | Every frame is unique | Impacts, fast strikes, critical moments |
| **On 2s** | Every other frame is unique | General motion, running, mid-action |
| **On 3s** | Every third frame is unique | Held poses, tension beats, slow buildup |
| **Held** | Same frame repeated N times | Impact frames, time-stops, dramatic pauses |
| **Smear** | Exaggerated blur frame | Fastest strikes (shonen/anime signature) |

### Frame budget validation:

**Every beat's frame count must equal `(end_s - start_s) × fps`.** No exceptions. If you're running
a 1.5s beat at 24fps, you have exactly 36 frames to distribute across your strikes. If your
per-strike timing doesn't sum to the beat frame count, the choreography is broken.

```
beat_frames = (end_s - start_s) × fps
Σ(per_strike.total_f) = beat_frames  ← validate this
```

### Held impact frames (the shonen signature):

The held impact frame is where a contact pose is frozen for multiple frames, often with radiating
speed lines, screen-tone, or ink splatter effects. It's the fight equivalent of a dramatic pause.

| Duration | Frames (24fps) | Effect |
|----------|---------------|--------|
| Light tap | 1–2 frames | Subtle emphasis |
| Solid hit | 3–4 frames | Standard impact read |
| Power strike | 5–6 frames | Major moment |
| Climax collision | 6–8 frames | Time-stop, the "money frame" |

## 4. Spatial geometry (the arena)

Define the fight space with real measurements. The model needs to know how much room the fighters
have, how far they can move, and what the environment constrains.

```yaml
spatial_geometry:
  arena_width_m: 12.0         # how wide the fighting area is
  arena_depth_m: 8.0          # how deep
  elevation_m: 25.0           # height above ground (0 for ground-level)
  engagement_range_m: 0.6     # striking distance for this fight style
  max_aerial_height_m: 4.0    # peak height of jumps/flips above the surface
  environmental_obstacles:     # things fighters can use or avoid
    - { type: "railing", position: "perimeter", height_m: 1.0 }
    - { type: "water_tower", position: "corners", height_m: 3.0 }
```

### Engagement ranges by style:

| Style | Typical engagement range (m) |
|-------|----------------------------|
| Boxing / close-quarters | 0.4–0.6 |
| Kickboxing / MMA | 0.6–1.0 |
| Weapons (sword) | 1.0–1.5 |
| Weapons (staff / spear) | 1.5–2.5 |
| Anime / superhuman | 0.3–0.6 (they close distance fast) |

## 5. Tempo and rhythm (fight BPM)

Fights have a rhythmic pulse — a BPM that drives pacing. Real fights are **not metronomic** — the
tempo shifts by beat to create tension and release.

### The escalation pattern (most fight arcs):

```
approach (building) → first exchange (peak density) → evasion (dip for contrast)
→ power-up (slow, sustained tension) → commit (fastest) → collision (time-dilation)
```

| Beat type | Typical BPM | Strikes/sec | Energy |
|-----------|-------------|-------------|--------|
| Approach / stalk | 100–140 | 0 | Building |
| Fast exchange | 160–200 | 2.5–4.0 | Peak action density |
| Evasion / dodge | 100–130 | 0–1 | Contrast dip |
| Charge / power-up | 80–110 | 0 | Sustained tension |
| Launch / commit | 180–220 | — | Maximum velocity |
| Collision / climax | 40–80 | — | Time dilation |

### Rest beats:

Audiences need micro-pauses between exchanges to process what happened. Budget 2–6 frames of
recovery between beats. Zero rest reads as noise. Too much rest kills momentum.

## 6. Power curves (escalation math)

Normalize the perceived power of each beat to a 0.0–1.0 scale. The curve should **generally
escalate** — each beat hits harder than the last. Dips are allowed for tension (an evasion beat
that dips to 0.4 before the power-up climbs to 0.75 creates anticipation).

```yaml
power_curve:
  normalized_by_beat:
    b01: 0.30   # approach — kinetic but no contact
    b02: 0.55   # exchange — real strikes
    b03: 0.40   # evasion — tension dip
    b04: 0.75   # charge — accumulating
    b05: 0.90   # commit — maximum velocity
    b06: 1.00   # collision — payoff
```

The constraint `power_escalation_monotonic` enforces this (with documented dip exceptions).

## 7. Character profiles (body math)

Each fighter needs measured body proportions and a defined fighting archetype. These drive the
kinematics — a shorter fighter with less reach closes distance differently than a tall interceptor.

```yaml
characters:
  char_a:
    height_m: 1.45
    reach_m: 0.58
    weight_kg: 40
    fighting_style: "brawler — aggressive, forward-pressure, emotionally driven"
    stance: "wide, low, weight forward"
    dominant_hand: "right"
```

### Fighting archetypes (maps to Laban effort baselines):

| Archetype | Laban baseline | Behavior |
|-----------|---------------|----------|
| Brawler | strong / sudden / direct / free (Punch) | Forward-pressure, emotionally driven |
| Interceptor | light / sudden / direct / bound (Dab) | Reactive, efficient, exploits openings |
| Grappler | strong / sustained / indirect / bound (Wring) | Close-range control |
| Speedster | light / sudden / indirect / free (Flick) | Evasive, hit-and-run |
| Tank | strong / sustained / direct / bound (Press) | Absorbs damage, slow but powerful |

## 8. FACS for combat (face in a fight)

Fight faces are different from UGC faces. The intensity range shifts up (C–E vs. B–C for UGC), and
the expression arc maps to the fight arc, not a sales pitch.

### Combat-relevant AU combinations:

| Expression | AUs | Intensity | When to use |
|-----------|-----|-----------|-------------|
| Attack aggression | AU4+AU5+AU25 | C–D | Throwing a strike |
| Maximum exertion | AU4+AU5+AU7+AU10+AU25 | D–E | Climax / desperation |
| Cold focus | AU7+AU23 | B | Technical fighter scanning |
| Surprise / disrupted | AU1+AU2+AU5 | C | When a strike gets through |
| Pain / absorb impact | AU4+AU6+AU9+AU43 | C–D | Taking a hit |
| War cry | AU4+AU5+AU25+AU26 | D–E | Full commitment yell |
| Composure crack | AU14 → AU4+AU5 | B → C | Smirk dropping to real engagement |
| Post-impact daze | AU4+AU7+AU23 | C | After a collision, assessing |

### Rules:
- Minimum 2 FACS events per beat per character (no frozen faces in a fight)
- Maximum hold 1.0s on any single expression
- Fighters should have **contrasting expression registers** (one emotionally open, one controlled)
- The expression arc should mirror the power curve (intensity escalates with force)

## 9. Laban for combat (movement quality in strikes)

Laban maps perfectly to martial arts. Each strike has an Effort signature. The fight arc should use
at least 3 distinct named Efforts for variety.

### Strike-to-Effort mapping:

| Strike type | Named Effort | Why |
|-------------|-------------|-----|
| Jab / straight | Thrust (sudden/strong/direct/bound) | Committed, linear |
| Hook / roundhouse | Slash (sudden/strong/indirect/free) | Arcing, rotational |
| Parry / deflection | Dab (light/sudden/direct/bound) | Quick, precise, minimal |
| Evasion / dodge | Flick (light/sudden/indirect/free) | Effortless, unpredictable |
| Power charge | Press (strong/sustained/direct/bound) | Sustained force containment |
| Grapple / clinch | Wring (strong/sustained/indirect/bound) | Grinding, continuous |
| Counter-strike | Punch (strong/sudden/direct/bound) | Explosive response |

### Shape in combat:

| Shape | Fight meaning |
|-------|--------------|
| Advancing | Pressing forward, closing distance, attacking |
| Retreating | Pulling back, resetting, creating space |
| Rising | Jumping, uppercut, powering up |
| Sinking | Ducking, dropping under a strike, absorbing |
| Spreading | Opening up to throw wide (hooks, kicks) |
| Enclosing | Tightening guard, clinching, containing energy |

### The bound→free transition:

The climax of most fights is the moment **bound flow breaks into free flow** — contained energy
releasing explosively. A power-up (Press: strong/sustained/direct/**bound**) transitioning into a
collision (Slash: strong/sudden/indirect/**free**) is the Laban signature of a fight climax.

## 10. Constraints with tolerances

Every combat control package must include mathematical constraints. These are machine-checkable
rules that validate the choreography.

### Required constraints:

| Constraint | Mode | Typical tolerance |
|-----------|------|-------------------|
| Frame budget | hard | sum must equal duration × fps exactly |
| Identity preservation | hard | score ≥ 0.95 |
| Contact accuracy | hard | fist-to-target < 0.05m at contact frames |
| Power escalation | hard | monotonic (with documented dip exceptions) |
| Held impact minimum | hard | ≥ 4 frames on climax |
| Facial continuity | hard | no single expression > 1.0s, ≥ 2 events/beat |
| Body mechanics completeness | hard | all body parts specified per beat per character |
| Audio-visual sync | hard | impacts aligned ±2 frames |
| Laban effort variation | soft | ≥ 3 distinct named Efforts across the sequence |
| Style consistency | soft | speed lines on motion > 5 m/s (anime), etc. |

## 11. Camera math for fights

Fight cameras need quantified parameters, not just type labels.

| Parameter | Unit | What it controls |
|-----------|------|-----------------|
| `focal_length_mm` | mm | Field of view (18mm = wide/environmental, 50mm = tight/intimate) |
| `angle_deg` | ° | Vertical angle (negative = looking up, positive = looking down) |
| `tracking_speed_match` | 0–1 | 1.0 = camera matches subject speed, < 1 = slightly behind |
| `shake_amplitude_px` | px | Camera shake on impacts (0 = none, 4 = rattles, 12 = violent) |
| `shake_frequency_hz` | Hz | How fast the shake oscillates (8–15 Hz for sharp impacts) |
| `shake_decay_frames` | frames | How quickly shake dies after impact |
| `whip_pan_speed_deg_s` | °/s | Rotation speed on whip pans (120–240° for fight exchanges) |

### Camera patterns by beat type:

| Beat type | Camera pattern |
|-----------|---------------|
| Approach | Low-angle tracking, wide lens (18–24mm) |
| Exchange | Tight medium, whip-pan between strikes, shake on impacts |
| Evasion | Pull back to wide to capture the full arc / dodge |
| Power-up | Split composition, alternating CUs, low angle |
| Launch | Side-tracking, fast scroll, profile composition |
| Collision | Tight impact → whiteout → rapid pullback to extreme wide |

## 12. Style-specific notes

### Shonen anime (Naruto, Dragon Ball, Bleach)
- Speed lines on all motion > 5 m/s screen velocity
- Held impact frames on all force contacts (3–8 frames)
- Smear frames on the fastest strikes
- Mixed frame-rate: 1s on impacts, 2s on motion, 3s on held tension
- Power-up beats are slow and sustained (BPM drops to 80–110)
- Climax collision uses time-dilation (BPM drops to 40–60)
- Energy VFX is character-specific (each fighter has a distinct color/shape)
- Ink splatter / screen-tone effects on the money frame

### Wuxia / wire-fu
- Longer aerial sequences (2–4s airborne)
- Wire-suspension physics: slower fall rate, horizontal gliding
- Weapon clashes get metallic ring audio + spark particles
- Camera: lots of upward angles, silhouettes against sky/moon
- Flowing fabric / hair is a character in itself

### MMA / realistic
- biomechanical realism = 1.0 (no anime scaling)
- Human velocity ranges only (see table in §2)
- No held impact frames — continuous motion
- Camera shake = documentary handheld, not stylized
- Audio: real bone/body impact sounds, breathing, crowd

### Superhero / comic-book
- Speed lines + halftone dots + panel-composition framing
- Impact frames with Ben Day dot radiations
- Mixed frame-rates per character (faster character on 1s, slower on 2s)
- Color shifts on impacts (complementary color flash)
