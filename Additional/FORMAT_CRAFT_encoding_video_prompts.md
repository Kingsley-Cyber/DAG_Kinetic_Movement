---
id: cpcs.reference.format_craft
kind: authoring_reference
epistemic_status: PROJECT_DERIVED
acquisition: authored
primary_route: (portable authoring asset)
companion: cpcs.reference.living_performance_realism
version: 1.0
---

# Format Craft — encoding video prompts in NL / YAML / JSON / XML (and every combo)

How to choose and combine encodings when writing prompts for video models — the **mindset,
creative superpower, pros/cons, and best-fit style** of each format alone and in every 2- and
3-way combination, seen through **T2V vs I2V** and **cinematography**.

> **The one law behind all of it (read first):** you never author a *format* — you hold **one
> canonical, time-indexed meaning** (subject · action-over-time · camera · invariants) and each
> format is that meaning **projected** for a specific reader. Same skeleton, different clothing.
> And whatever structure you author in, the video model ultimately reads **prose** — so structure is
> *scaffolding that forces your specificity*, which you then **compile down** to the prose the model
> consumes. Structure protects meaning; it doesn't replace the prose.

---

## 0. The running example (one meaning, projected four ways)

**Canonical beat:** *8s, 9:16. A subject at a kitchen counter in soft morning window light pours
coffee; their phone buzzes; they glance down; a small genuine smile spreads as they read it. Slow
handheld push-in. Deep focus, ambient only, identity locked.*

Watch the **same object** render differently below. That "sameness under projection" is the skill.

---

## 1. The four single formats

### NL (natural language / prose)
- **Native job:** gestalt, tone, causal story — *what the model actually reads.*
- **Mindset:** a **director whispering to an actor.** You think in momentum and cause ("…and *because*
  the phone buzzes, they glance down").
- **Creative superpower:** subtext, mood, and causal flow. Evocation.
- **Weak at:** exact order, exact values, non-drift guarantees.
- **T2V/I2V:** shines for **I2V** (appearance is locked by the image, so prose only carries
  motion+feel) and for **single expressive shots** in T2V.
- **Example:**
> Vertical 9:16, ~8s, a soft morning kitchen. [swap: a person] pours coffee, relaxed; their phone
> buzzes and they glance down, then a small genuine smile spreads — cheeks lifting, eyes creasing —
> as they read it. The handheld camera drifts slowly closer. Real skin texture, deep focus, true
> color, ambient room tone, no music. (no on-screen text)

### YAML
- **Native job:** human-authored intent, hierarchy, **defaults & inheritance.**
- **Mindset:** a **production designer with a layered spec sheet.** You think in fields you can
  override.
- **Creative superpower:** **remixing** — change one field and get a variant; compose from profiles.
  Best format for iterating a *family* of prompts.
- **Weak at:** machine-exact truth, guaranteed ordering.
- **T2V/I2V:** great authoring layer for both; pairs with a reference still in I2V.
- **Example:**
```yaml
shot: {aspect: "9:16", dur_s: 8, mode: i2v}
subject: "[swap: person], relaxed morning energy"   # identity locked by reference still
setting: kitchen counter; soft window key from left
beats:
  - {t: "0-3", do: "pours coffee, easy posture"}
  - {t: "3-5", do: "phone buzzes; glances down (eyes lead, head follows)"}
  - {t: "5-8", do: "reads it; genuine smile (cheeks+eyes); small nod"}
camera: handheld slow push-in
look: {focus: deep, grade: none, skin: real_microtexture}
audio: ambient room tone; no music
```

### JSON
- **Native job:** resolved, exact, **machine-checkable** truth — timings, booleans, verification.
- **Mindset:** an **editor/engineer with a timeline and a checklist.** You think in exact values.
- **Creative superpower:** **precision as expression** — exact timings *create rhythm*; constraints
  become a creative force; verification makes intent auditable.
- **Weak at:** human readability, nuance/tone.
- **T2V/I2V:** the **invariant + clock** channel — essential in **T2V** (nothing is locked, so you
  pin identity/timing/booleans here).
- **Example:**
```json
{"aspect":"9:16","fps":29.97,"duration_s":8,"mode":"i2v",
 "timeline":[{"t":[0,3],"action":"pour_coffee"},
             {"t":[3,5],"action":"glance_at_phone","gaze":"eyes_lead_head"},
             {"t":[5,8],"action":"read_and_smile","au":["AU6","AU12"]}],
 "camera":{"move":"push_in","rig":"handheld","dof":"deep"},
 "invariants":{"identity_locked":true,"music":false,"on_screen_text":false},
 "verify":{"smile_is_duchenne":true,"first_action_by_s":3}}
```

### XML
- **Native job:** **ordered mixed-content** + typed/namespaced **triggers** + routing (tags = cues,
  CDATA = payload).
- **Mindset:** a **composer writing a score with time signatures** + a **stage manager calling
  cues.** You think in sequence + attributes.
- **Creative superpower:** **orchestration** — explicit shot order, hard cuts, event triggers, and
  wrapping mixed content the other formats can't hold cleanly.
- **Weak at:** verbosity; raw tags can confuse a generator (keep model-facing text in CDATA).
- **T2V/I2V:** the **sequence** channel — indispensable for **multi-shot / multi-cut** work.
- **Example:**
```xml
<clip aspect="9:16" dur="8" mode="i2v">
  <shot t="0-3">pours coffee, relaxed</shot>
  <shot t="3-5" trigger="phone_buzz">glances down, eyes lead head</shot>
  <shot t="5-8">reads message, <emph>genuine smile</emph> (cheeks+eyes)</shot>
  <camera rig="handheld" move="push_in"/>
  <render focus="deep" music="false" text="false"/>
</clip>
```

---

## 2. The combos — who owns what, and the style each unlocks

Combine formats when **one artifact must serve two+ readers at once** (a human to tweak, a tool to
parse, a model to render) — while staying under an input-box char cap. Rule: **each field goes in the
one channel that owns it.**

### YAML + JSON  — *"author it, then lock it"*
- **Division:** YAML = readable intent you edit; embedded JSON = exact clock + invariants + verify.
  **Dual-parse** in one file.
- **Mindset:** designer **and** engineer pairing at one desk.
- **Uniqueness:** the **repeatable-product** format — readable enough to tweak, exact enough to run
  a pipeline over.
- **Excels at:** **batch variant generation**, UGC product systems, anything a friend re-runs with
  small edits. (This is the house `yaml_json` asset.)

### XML + YAML  — *"call the shots, direct the performance"*
- **Division:** XML tags = shot order + hard cuts + triggers (routing); YAML-in-CDATA = the
  human-readable directive payload the model reads.
- **Mindset:** stage manager **and** director.
- **Uniqueness:** ordered structure *with* rich per-shot performance direction, still legible.
- **Excels at:** **shot-listed narrative UGC / multi-beat ads** (this is exactly your Wonder Belly
  shape: XML `<order>` + YAML `control`).

### XML + JSON  — *"cut to the timecode"*
- **Division:** XML = ordered shots/cuts; JSON = exact timebase, cut times, compression math, verify.
- **Mindset:** an **editor cutting to a metronome.**
- **Uniqueness:** rhythm is *guaranteed*, not hoped for.
- **Excels at:** **music-sync, montage, action & dance, anime staged impacts** — anything where the
  *timing is the art.*

### XML + YAML + JSON  — *"the full production"* (max control)
- **Division:** XML owns **order**, YAML owns **intent/performance**, JSON owns **clock + invariants
  + verification.** NL is emitted at the end for the model.
- **Mindset:** a film production with a **score (XML)**, a **design bible (YAML)**, and an
  **edit-decision-list + QC sheet (JSON)** — all at once.
- **Uniqueness:** nothing drifts and everything is auditable; the most *directable* config that
  exists.
- **Excels at:** **cinematic narrative, branded films, client-critical or verifiable pieces,
  multi-shot recreations** (your Wonder Belly precision layer is effectively this).

### NL alone (and NL as the always-present emit layer)
- **Excels at:** **raw single shots** — iPhone-selfie UGC, mood/dream pieces, single-take talking
  heads — and any time the **model box is small** so prose-only is the deliverable.
- **Remember:** even under the all-three config, you *compile to NL* for the generator. NL is never
  optional as the final projection; it's optional only as the *authoring* layer.

---

## 3. Singular vs 2-way vs 3-way — pick by stakes, not by flex

| Layers | Control | Overhead | Use when |
|---|---|---|---|
| **1 (usually NL)** | low | tiny | one-off shot, mood, raw UGC, small input box |
| **2 (a hybrid)** | medium | moderate | a product you re-run, a multi-beat piece, a rhythm-critical edit |
| **3 (XML+YAML+JSON)** | max | high | client work, verifiable recreations, complex multi-shot cinema |

**Don't over-engineer a mood shot with all three** — format is not quality. The *specificity in time*
is the quality; format only protects it from being lost. Match layers to stakes.

---

## 4. T2V vs I2V changes the encoding weight

- **I2V (image-to-video):** identity, wardrobe, scene, and **texture are locked by the reference
  still.** The prompt's job **shrinks to motion + behavior + camera + time.** → favors **lighter
  encodings**: NL, or YAML+timeline. The reference image does the invariant heavy-lifting that JSON
  would otherwise do. *Lock appearance in the still; direct behavior in prose.*
- **T2V (text-to-video):** **nothing is locked.** The prompt must carry identity, scene, wardrobe,
  texture **and** motion/time/camera, and hold them stable across the clip. → favors **more
  structure**: JSON for invariants/exact values, XML for order, YAML for the layered spec, plus a
  strong NL gestalt because there's no anchor image. *Structure is the anchor the image would have
  been.*
- **Consistency across shots (both):** the **reference still** (I2V) or a **locked identity/verify
  block** (T2V JSON) is what prevents drift. Reuse it across every clip.

---

## 5. The cinematography lens (where camera/light/edit info goes)

A cinematographer's information naturally *sorts itself* into channels:

| Cine element | Best channel | Why |
|---|---|---|
| Shot order, cuts, coverage | **XML** | ordered, named, sequential |
| Exact lens / fps / aspect / shutter / DOF | **JSON** | precise numbers, no ambiguity |
| Cut timecodes / rhythm | **XML order + JSON `cuts[]`** | sequence + exact time |
| **Motivated** camera ("it leans in *because* they realize") | **NL / YAML** | intent & cause |
| Lighting: available/motivated | **NL / YAML** | qualitative |
| Lighting: exact ratios / color temp | **JSON** | numbers |
| Blocking / screen direction (invariant) | **JSON verify + NL** | must-not-drift, stated as outcome |

Net: serious cinematography trends toward **XML + JSON (+ YAML for intent)** — i.e., the all-three
config — because it has *both* ordered coverage *and* exact optics *and* motivated intent.

---

## 6. Style → recommended encoding (cheat sheet)

| Style / goal | Encoding | Why |
|---|---|---|
| Raw iPhone-UGC selfie (I2V) | **NL** (or YAML+NL) | feel > precision; small box |
| Polished multi-beat UGC ad | **XML + YAML** | shot order + rich per-beat direction |
| Batch product-variant pipeline | **YAML + JSON** | tweakable + runnable, dual-parse |
| Cinematic narrative (verifiable) | **XML + YAML + JSON** | order + intent + non-drift + QC |
| Action / dance / music-sync | **XML + JSON** | timing is the art |
| Anime / stylized staged action | **XML + JSON** (+ YAML style profile) | staged impacts, timed; style layer |
| Mood / dream / abstract | **NL** | gestalt, no hard structure to protect |
| Educational / explainer | **YAML** (+ NL) | layered, readable, easy to revise |
| Multi-shot recreation of a reference | **XML + YAML + JSON** | order + directive + exact clock + invariants |

---

## 7. Anti-patterns
- **Format ≠ quality.** Adjectives in JSON are still adjectives. Put *specific, timed, causal* detail
  in whatever channel — that's the quality.
- **Raw tags/keys to the model.** Don't feed a generator bare XML/JSON as the *final* prompt; compile
  to NL (keep structure as scaffolding / in CDATA).
- **Over-layering a simple shot.** Three formats on a single mood beat = overhead with no gain.
- **Under-structuring a T2V multi-shot.** Prose-only across 5 cuts will drift — add order + invariants.
- **Two authorities.** Never let the prose and the JSON disagree; JSON is the resolved truth, prose is
  its projection.

---

## 8. The transferable loop (teach your friends this)
```
1. Hold the canonical meaning (subject · action-in-time · camera · invariants)
2. Sort each field by hardness:  must-not-drift → JSON/XML ;  directed → YAML/NL
3. Sort by shape:  ordered → XML ; exact → JSON ; hierarchical → YAML ; gestalt → NL
4. Pick layers by stakes (1 / 2 / 3)
5. Adjust weight for T2V (more structure) vs I2V (lock the still, lighten the prose)
6. COMPILE to NL for the model — structure was scaffolding
```
Master that loop and the format is never the hard part again — the meaning is.
