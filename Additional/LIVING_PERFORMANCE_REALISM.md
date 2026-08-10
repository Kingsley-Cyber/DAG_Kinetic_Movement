---
id: cpcs.reference.living_performance_realism
kind: authoring_reference
epistemic_status: PROJECT_DERIVED
acquisition: authored
primary_route: (portable authoring asset — usable standalone or ingestible into cpcs/knowledge)
interfaces:
  - cpcs-ugc-video-prompts (skill)
  - lab/second_brain (compiler + concepts)
version: 1.0
---

# Living Performance & Capture Realism — a reusable authoring spec

**Applies to any prompt, any gender, any living thing** (human of any gender, mammal, bird,
reptile, fish, insect, or edge cases like plants/slow-life). It is the "why it feels alive, not
rendered" layer, generalized so you can reuse it across every video prompt.

> **The one rule:** *direct behavior and capture as time-indexed systems, not as adjectives.*
> "Realistic" is not a control. A **timed involuntary micro-behavior track + a motivated capture
> track + bounded imperfection** is. The video model consumes **prose** — the structured score
> below is scaffolding that forces specificity; the deliverable you paste is the compiled prose.

---

## 0. The realism theorem

A living thing reads as real when three conditions hold **at the same time**:

1. **Involuntary micro-behavior** — it is never perfectly still or perfectly symmetric; autonomic
   systems (breath, blink, balance, micro-gaze) keep running under the intended action.
2. **Motivated capture** — the camera is a real device with real behavior (it drifts, hunts focus,
   adapts exposure) and its imperfections are **caused by events**, not decorative.
3. **Bounded imperfection** — every imperfection is small and lawful. Random jitter reads *broken*;
   zero imperfection reads *AI*; small-and-lawful reads *real*.

Corollary — **the differentiator is TIME.** The gap between "good" and elite is almost always that
the good prompt gives realism as a *list* ("blinks, breathes, natural motion") and the elite prompt
gives it as a *timeline* keyed to beats / words / events. Convert every list into a schedule.

---

## 1. Direct systems, not stereotypes (gender & species neutrality)

- **Gender:** the realism math is identical across all genders. Do **not** gender the performance
  ("she smiles softly," "he stands tough"). Direct the same involuntary systems (gaze, breath,
  affect action units, effort) for everyone. **Identity — including gender presentation — is a
  locked `[swap]` slot** (set by the reference still / cast), never expressed through performance
  adjectives. This makes one score reusable across any cast.
- **Species:** the seven layers below are universal *functions*; only their **signal set** changes
  by species (a dog shows affect with ears/tail/hackles; a human with facial action units). Author
  the function, then map it to the creature's real signal set (§5).
- **Anatomy is an invariant, not a style choice** — see §7.

---

## 2. The seven universal performance layers

Author every living subject through these. Each is a *track over time*, not a single value.

| # | Layer | What it controls | Human signal | Cross-species note |
|---|---|---|---|---|
| L1 | **Aliveness / autonomic** | never fully still | breathing rise/fall, resting micro-sway, swallow | respiration visible in flanks/gills; idle tail/ear/antenna motion |
| L2 | **Attention & gaze** | where focus goes + how it moves | gaze target, saccades, blink, **eyes→head→torso lead order** | ears/eyes orient *before* head; prey vs predator scan patterns |
| L3 | **Affect display** | visible emotional change | FACS action units (see L3 note) | ears, tail, piloerection, posture, pupil/dilation, gular/throat |
| L4 | **Motor initiation & phrasing** | how movement is produced | **proximal-to-distal** (root→limb), anticipation→action→follow-through→recovery | quadruped weight over 4 supports; wing/tail as balancers; wave propagation in fish/snakes |
| L5 | **Emphasis dynamics** | the accent beat | a **sudden Laban effort accent + a small lean (advancing Shape)** on the key word/moment | a pounce, a head-snap, a tail flick as the accent |
| L6 | **Asymmetry & micro-noise** | breaks the uncanny | bilateral asymmetry, microvariation (correlated, *not* white noise) | no creature is bilaterally identical in motion; jitter must correlate |
| L7 | **Surface realism** | skin/coat/scale/feather | **name microtexture positively; forbid the tell** (see §7) | fur clumping, feather barbs, scale sheen, wet specular |

**L3 note (FACS for humans):** don't give one static expression — give an **AU sequence in time**.
A genuine smile is **AU6 (cheek raiser) + AU12 (lip corner) together** — cheeks and eyes, never the
mouth alone (mouth-only = the pasted-on AI smile). Direct the *change* (neutral → onset → apex →
offset), not a label like "happy."

**Voice / vocalization (the co-equal layer people under-spec):**
- Human: pace (~150–190 wpm conversational), a **small breath before the line**, natural fillers,
  vocal texture (slight fry / uptalk), micro-pauses before an emphasis or a proof point.
- Animal: species-true vocalization only; sync mouth/throat/body to the sound; ambient, not scored.

---

## 3. The capture system (separate from performance)

The camera is its own living-ish system. Keep it **distinct** from the subject so you can restyle
either independently.

- **Device grammar:** name the device and hold behavior (handheld arm's-length; tripod; on-body;
  drone-follow). Add **bounded** shake + **one** small reframe/recentre. "Imperfect but bounded."
- **Focus behavior:** autofocus **hunts then snaps**; specify **one** AF settle event, ideally
  *motivated* (triggered by a hand/object entering frame or the subject moving).
- **Exposure behavior:** exposure **drifts/adapts** — e.g., blooms when moving from dim to bright,
  or lifts toward a window. Motivate it by a lighting change in the scene.
- **Focus depth:** for "real phone" default to **deep focus, NO heavy bokeh** (shallow DOF reads as
  "ad/cinema"). Reserve shallow DOF only when you *want* the produced look.
- **Light:** available / location-motivated (window key on one side; flat fluorescents in a store).
  No 3-point studio rig unless the produced look is the goal.
- **Audio:** close on-device mic + room tone/ambience; **no music** for authenticity (music =
  "produced"). Designed SFX only if the scene demands.
- **Framing honesty:** mild wide-angle distortion at arm's length; slightly off-center; the subject
  occasionally under- or over-fills the frame the way a real operator would.

---

## 4. TIME is the differentiator — convert lists to a schedule

**Weak (list):** "she blinks, breathes, has natural expressions and gestures."
**Elite (schedule), gender/species-neutral:**

```
0.0–0.4s  small pre-line breath; gaze to lens; neutral face
0.4–1.2s  brow flash (AU1+2) on the first word; one right-hand gesture rises
1.2–1.8s  EMPHASIS: sudden light effort accent + 3cm lean-in on the key word; blink just after
1.8–2.6s  genuine smile onset (AU6+12, cheeks+eyes); head settles; shoulders release
2.6–3.0s  brief glance off-axis and back; hold; hand lowers
```

Every selfie/close beat should get its **own** schedule. Reusing one generic aliveness bundle across
all beats is itself an AI tell (uniformity). Tie accents to the actual emphasis word/event.

---

## 5. Species adaptation table

Map the seven layers to the creature's real signal set. Author the *function*, render the *signal*.

| Species class | L1 aliveness | L2 attention | L3 affect | L4 motor | L7 surface |
|---|---|---|---|---|---|
| **Human (any gender)** | breath, micro-sway, swallow | saccades, blink, eyes→head lead | FACS AU sequence | proximal-to-distal; anticipation/recovery | pores, uneven tone, T-zone sheen |
| **Quadruped mammal** | flank breathing, ear/tail idle | ears orient before head; scent-check | ears, tail carriage, lip/hackle | 4-support weight shift, gait phase | fur direction/clumping, wet nose specular |
| **Bird** | rapid breath, feather settle | fast head saccades, one-eye turn | crest, feather sleeking/fluffing | perch balance, tail as rudder, wing tuck | barb detail, iridescence |
| **Reptile/amphibian** | slow flank/gular pulse | still-then-snap gaze; slow blink | throat/gular, posture | low center, lateral-wave propagation | scale sheen, moisture |
| **Fish/aquatic** | gill motion, fin idle | eye independent of body | fin flare, color shift | body-wave thrust, fin steering | wet specular, scale glint |
| **Insect/arthropod** | antenna/leg micromotion | compound-eye orient via body turn | posture, wing/leg display | many-leg phase, sudden dart | chitin sheen, hair detail |
| **Plant / slow-life** | sway from air, turgor micromotion | (phototropic bias) | — | growth/spring-back elasticity | surface translucency, edge fuzz |

Universal across all: **never fully still, never perfectly symmetric, motion initiates from a root
and propagates, and micro-noise is correlated (not random).**

---

## 6. Invariants vs tunables (what may never drift vs what you direct)

Encode both explicitly (this is what makes a prompt *safe* and *reusable*).

- **Invariants (hard — never drift, express as outcomes + machine-checkable):**
  identity & anatomy (limb/finger/eye count, proportion), continuity (wardrobe, markings, product
  packaging/spelling/colors), physics (contact before displacement; a reaction cannot precede its
  cause; support/weight), screen direction, and any factual claim. State these as *outcomes*
  ("hands remain anatomically correct; label text stays exactly as reference"), not mechanisms.
- **Tunables (free — you direct these per beat):** the micro-behavior schedule, capture events,
  emphasis placement, framing, pacing. Restyle freely; the invariants hold.

> Rule of thumb: hardness tracks epistemic class. Physics/anatomy (measured/observed) = invariant.
> Stylistic defaults (deep focus, pacing, grade) = tunable. Never delete invariants to gain
> variance; **scope** them and express them as outcomes so any style can satisfy them its own way.

---

## 7. Surface realism (the #1 tell) — name it, don't forbid-only

Forbidding "smooth/plastic" alone still drifts waxy. **Positively name the real microtexture**, then
forbid the tell. For image-to-video, texture is locked by the **reference still**, not the video
prompt — fix it there first.

- **Human skin:** visible pores, subtly uneven tone, faint fine lines, under-eye softness, T-zone-only
  sheen, faint redness at nose/ears. Keep bilateral asymmetry.
- **Fur/feather/scale:** direction and clumping; stray strands; barb/edge detail; sheen only where
  oil/moisture would sit.
- **Forbid (all species):** `smooth_ai_skin, waxy, poreless, airbrushed, uniform_texture, plastic,
  bilateral_perfect_symmetry, frozen_face, dead_eyes`.

---

## 8. Reusable fill-in template (score → compiled prose)

```yaml
subject:                      # identity is a LOCKED swap slot — no gendered performance adjectives
  who: "[swap: species + individual identity; lock via reference still]"
  invariants: [anatomy_correct, markings_continuity, identity_stable]
capture:
  device: "[handheld arm-length | tripod | on-body | follow]"
  focus: "deep focus, no heavy bokeh; one motivated AF settle"
  exposure: "adapts to [light change]; bounded"
  imperfection: "small shake + one reframe (bounded, not random)"
  light: "[available/location light]"
  audio: "on-device mic + [ambience]; no music"
performance_timeline:        # one per beat — THIS is the differentiator
  - t: "0.0-0.4"  do: "pre-line breath; gaze to target; neutral"
  - t: "0.4-1.2"  do: "attention shift (L2); onset of intended action"
  - t: "1.2-1.8"  do: "EMPHASIS: sudden effort accent + small lean on key beat; blink after"
  - t: "1.8-2.6"  do: "affect apex (L3 AU/signal seq); recovery begins (L4)"
  - t: "2.6-3.0"  do: "micro-glance off and back; settle; hold"
surface: "[positive microtexture, §7]"
voice: "[pace, pre-line breath, texture]  OR  [species vocalization]"
forbid: [smooth_ai_skin, waxy, plastic, frozen_face, bilateral_perfect_symmetry, robotic_stillness, cinematic_grade_if_ugc]
```

**Compile rules:** translate every AU/effort term to plain language in the final prose ("cheeks lift
and eyes crease," not "AU6+12"). Keep the imperfections *in* the prose — they are the point. End with
`(no on-screen text, no subtitles)`. If the model box caps ~2000 chars, ship the **prose only**.

---

## 9. "Reads real vs AI tell" verification checklist

- [ ] Subject is never perfectly still (breath/idle micromotion present)
- [ ] Bilateral **a**symmetry present (face/body/motion)
- [ ] Gaze moves naturally (not a locked stare; correct lead order for the species)
- [ ] At least one **timed** affect change (not a static label)
- [ ] Emphasis has a **sudden** accent + small lean (not even energy)
- [ ] Motion initiates root→tip with anticipation & recovery (not smooth-glide)
- [ ] Capture imperfection is **bounded and motivated** (AF hunt caused by an event)
- [ ] Deep focus / true color if the goal is "real" (no cinematic grade)
- [ ] Surface microtexture named positively; waxy/plastic forbidden
- [ ] Ambient audio, no music (for authenticity)
- [ ] Invariants (identity/anatomy/continuity/claims) stated as outcomes and unbroken
- [ ] Each beat has its **own** schedule (no reused generic bundle)

---

## 10. Epistemic & honesty

- Label what is **observed/measured** vs **interpreted** vs **authored** (e.g., recreation dialogue
  = "authored condensation, not verbatim").
- **Recreations:** preserve *structure, timing, movement quality, capture grammar* — swap identity,
  voice, logos, and any distinctive choreography. Never clone a real person or invent packaging text.
- **No unsupported claims** (health, efficacy, performance) beyond verified source.

---

## 11. Feasibility (so the score is actually renderable)

- **Single continuous multi-cut clips** (10–20s with internal cuts) only hold on models that support
  it (e.g., Sora 2, Veo extend/scene, Kling extend). On 8s-capped models, split to one clip per beat
  and assemble.
- **Consistency across clips:** use one **reference still** as the identity/anatomy anchor (i2v) and
  reuse it — this locks the invariants that prose can't guarantee.
- **Native audio** models (Veo 3.x, Sora 2) for spoken/voiced beats; mute + add audio in edit for
  motion-only models.

---

## Appendix A — Deep-research query to enhance this via the DAG

See the companion research prompt (also inline in the delivery message):
`RESEARCH_QUERY_living_performance_realism.md`. It is written to the DAG's gap-closure format —
returns time-indexed, measurable, source-cited, provider/duration-scoped claims across all genders
and species that upgrade every layer (L1–L7 + capture + voice) from qualitative to measured.
