---
id: cpcs.reference.hands_contact_manipulation
kind: feature_spec
epistemic_status: PROJECT_DERIVED
acquisition: authored
primary_route: (buildable, dynamic spec for the 2nd brain)
companions: [cpcs.reference.living_performance_realism, cpcs.reference.capture_surface_realism, cpcs.reference.natural_dialogue_mode, cpcs.reference.format_craft]
builds_on: [c_dag_proximal_to_distal, c_dag_staged_impact, c_dag_robotic_movement_diagnostic]
maps_to: [profile://movement/staged_action_base_v2, profile://style/anime_sakuga_action_v3, RUNBOOK_cross_style_switching, LPR-004]
version: 1.0
status: ready_to_build
---

# Hands, Contact & Interaction — the causal-physics module

The hardest surface in AI video. Hands, contact, object interaction, and combat **fail differently**
from talking-heads — so they get their **own module, own locks, own cut strategy, and one shared
spine: cause and effect.** Fine manipulation (a zipper), object handoff, a hug, and an anime punch are
**the same causal event** — different contact types and different stylization on **one grammar.**

> **The one law:** every interaction is a **causal chain** — nothing happens to a thing until
> something touches it, and no reaction precedes its cause. Get the chain right and it reads real
> (or reads *weighty*, in anime); break it and the eye catches the lie instantly.

---

## 0. Why it's its own module
- Hands are the **#1 anatomy failure** (extra fingers, warping, fusion). You *engineer* around it, you
  don't hope.
- Contact is the **expensive frame** — the moment two things touch/pass is where models fuse, clip,
  and morph.
- Interaction is **causal** — order violations (effect before cause) are the loudest tell, especially
  in fights.
- It needs a **cut strategy**, not just description — sometimes the fix is to *not render* the hard
  frame.

---

## 1. The causal grammar (the spine — cause and effect)

Every interaction resolves to one phrased chain (this generalizes `c_dag_proximal_to_distal` +
`c_dag_staged_impact` to **all** contact):

```
PRECONDITION (state, support, distance)
→ ANTICIPATION (wind-up / reach / gaze-leads-target)
→ APPROACH (travel to minimum distance)
→ CONTACT (touch at the closest point — the causal instant)
→ TRANSFER (force / object / grip established)
→ EFFECT (displacement / reaction / state change)
→ FOLLOW-THROUGH (overshoot / recoil)
→ RECOVERY (settle) → POSTCONDITION (new state)
```

**The inviolable causal laws** (from the DAG motion grammar — these are the *protected invariants*
that survive any stylization):
- **Contact precedes displacement.** A thing doesn't move/open/break before it's touched/hit.
- **A reaction cannot precede its cause.** No flinch/knockback/blood before the strike lands.
- **Support precedes force.** Plant/weight before a push or punch; no force from an unsupported body.
- **No teleportation / no ownership change without contact.** An object changes hands only during a
  contact overlap.
- **Contact is continuous once made** (grip/weight) until deliberately released — no flicker.
- **Screen direction is conserved** (the 180° axis) across a contact and its reaction.

Everything below is *how to render each phase* for a contact type + style, while these laws hold.

---

## 2. Hand / fine-manipulation sub-module

### 2.1 Invariants (forbid, not hope)
`extra_fingers, missing_fingers, finger_duplication, warped_hand, hand_object_fusion,
hand_hand_fusion, floating_object, morphing_object, grip_not_matching_object`.

### 2.2 Name the grip (grip taxonomy)
Vague "holds it" → morph. Name the grip so the hand has a job:
- **Power grip** (wrap: bottle, handle) · **precision pinch** (thumb+index: zipper pull, coin) ·
  **tripod** (thumb+2: pen) · **hook** (bag strap) · **lateral/key pinch** (card, key) ·
  **palm/support** (hold a base steady).
Match grip to the object's **affordance**; keep the **object rigid** and its **label/face readable**.

### 2.3 The 4-way engineering (the "be careful" craft)
1. **Invariant-forbid** the classic failures (§2.1).
2. **One specific bounded motion** — exact grip, one direction, once. (Zipper: *precision-pinch the
   pull, draw screen-left→right, once, teeth interlocking.*)
3. **Cut around the impossible frame** — identify the frame the model can't render (insertion,
   fusion-prone contact) and **cut across it** (§5). e.g. `empty → hard match-cut → loaded`,
   `no_insertion`.
4. **Minimize interacting parts** — **one hand** when possible; one object; fewer moving parts = fewer
   warps.

---

## 3. Person↔object & person↔person interactions

**Object events** (pick up / set down / hand off / open-close / use): each is a causal event with
**pre/post state**. Hand-off = a **two-agent contact overlap** (both grips co-exist for a beat, *then*
ownership changes — never a teleport). Open/close and load/unload are **state changes** best done as a
**match cut** across the hard middle (the `no_insertion` trick).

**Person contact** (handshake / hug / grab / guide / lean): fixed, consistent **contact points**; no
**clipping** (limbs through bodies) or **fusion**; **shared weight/support** (a lean needs a brace);
conserve **screen geography** (who is where, which side the contact is on).

---

## 4. ANIME & stylized combat (the transfer — same spine, exaggerated phases)

**Key idea:** anime doesn't break the causal chain — it **exaggerates the *timing and effects* of the
phases** while the causal *order* and *screen direction* stay locked. That's a **typed style transform
on the same skeleton** (`c_style_transform_vector`) with the §1 laws as **protected invariants**.

### 4.1 The punch (staged impact for combat) — full phase breakdown
```
ANTICIPATION (wind-up, big in anime)  — coil, weight back, gaze locks target
→ TRAVEL (fist crosses)               — SMEAR frames / speed lines / motion streak
→ CONTACT at minimum distance         — the causal instant (often HIDDEN by the flash)
→ IMPACT FRAME (1–3 frames)           — white/graphic flash, radial lines (also hides the hard contact frame)
→ HIT-STOP (freeze 2–6 frames)        — the signature of WEIGHT; everything holds on contact
→ EFFECT / KNOCKBACK                   — target displaces ALONG the force vector; debris/dust/blood AFTER contact
→ FOLLOW-THROUGH / OVERSHOOT           — fist continues past; body rotates through
→ RECOVERY                            — settle to guard; secondary motion (hair/cloth) trails
```
This is `c_dag_staged_impact` in anime dress. **A hit with no wind-up and no recovery reads
weightless** — the classic bad-CG/AI fight tell.

### 4.2 Power comes from the ground (proximal-to-distal)
A real/weighty strike initiates **pelvis → torso → shoulder → elbow → fist** (`c_dag_proximal_to_distal`;
DAG `staged_action_base_v2`). **All-arm punches read weightless.** Plant the foot (**support before
force**), transfer weight, rotate the hips.

### 4.3 Anime-specific levers (give the impact its feel)
- **Anticipation expansion** (bigger wind-up = bigger perceived power)
- **Key-pose holds** (freeze on the strongest silhouette)
- **Smear frames** on fast travel (motion the eye reads)
- **Impact frame** (1–3 frame flash — *also* conveniently hides the exact fusion-prone contact frame)
- **Hit-stop** (brief freeze on contact = weight; the single most important "it landed" cue)
- **Speed lines / screen shake / debris / dust ring** as **effects of** contact (never before)
- **Follow-through & overshoot**; **secondary motion** (hair, cloth, straps trail the action)

### 4.4 Multi-actor geography & causality (fights break here)
- **Screen direction / 180° axis:** attacker screen-left → defender screen-right; reactions travel
  **along the force vector** (a right-cross sends the target screen-right + back). Don't flip the axis
  across the exchange (DAG: `ActionAxis`, screen direction).
- **Cause→effect order (the loudest tell):** the **hit lands → then** the flinch/knockback/blood; a
  **block must intercept *before* contact**; a **dodge must start on the anticipation**, not after the
  hit. Never render the reaction first.
- **Contact types in combat:** **strike** (impact) · **grab/grapple** (sustained continuous contact) ·
  **block/parry** (interception before contact) · **weapon** (staged impact at the *weapon endpoint*,
  DAG's 9-landmark model incl. weapon tips).
- **Effort (DAG combat math):** strike = **strong / sudden / direct** (Laban weight/time/space); map
  the 7 strike→Effort types; readability first (sakuga: one clear action per beat, silhouette
  separation).

---

## 5. Cut strategy & camera for contact (modular — often the real fix)

- **Identify the impossible frame** (insertion, deep fusion-prone contact) → **cut across it**
  (match-cut state change) rather than rendering it.
- **Impact concealment (the pro move):** cut **to** the impact, or hide the exact contact with an
  **impact-frame flash**, a **whip-pan**, an **obstruction**, or a **hit-stop** — anime's impact
  frames exist partly *because* the true contact frame is the hardest to draw. Same trick works for AI.
- **Contact is the expensive frame:** either commit to rendering it clean (short, close, one hand,
  rigid object) **or** conceal it. Don't leave it vague and long.
- **Reaction shot:** show the **effect** on the target/face right after — proves causality cheaply.

---

## 6. The dynamic resolver (compute the interaction module)
```python
def resolve_interaction(inputs) -> block:
    chain = CAUSAL_CHAIN                                   # §1, always
    ctype = inputs.contact_type                            # manipulate|handoff|person|strike|grapple|block|weapon
    grip  = grip_for(inputs.object)                        # §2.2 affordance match
    timing = phase_timing(inputs.style)                    # realistic: subtle; anime: expand anticipation+recovery, add hit-stop
    fx     = effects_for(inputs.style, ctype)              # anime: smear, impact_frame, speed_lines, dust — as EFFECTS of contact
    geom   = screen_direction(inputs.participants)         # attacker→defender axis; reaction along force vector
    cut    = cut_strategy(ctype, inputs.provider)          # render clean OR conceal the impossible frame
    forbid = FAILURE_CATALOG(ctype)                        # §7
    block  = assemble(chain, ctype, grip, timing, fx, geom, cut, forbid)
    return enforce_invariants(block, laws=SECTION_1_LAWS)  # causal order + screen direction survive stylization
```
**Realistic ↔ anime is a timing/effects transform on the *same* causal skeleton.** The §1 laws are the
**protected invariants** that must survive the transform (per `RUNBOOK_cross_style_switching`).

---

## 7. Failure catalog (forbid / negative controls)
- **Hands:** extra/missing/duplicated fingers, warping, **hand-object/hand-hand fusion**, floating,
  morphing objects, grip mismatched to object.
- **Contact/physics:** clipping (limbs through bodies), **effect with no contact**, **effect before
  contact**, teleportation, ownership change without contact, foot sliding, broken/flickering grip,
  weight from an unsupported body.
- **Combat/anime:** **reaction before cause**, knockback **not along the force vector**, **axis break**
  (screen-direction flip), **weightless all-arm strike**, hit with **no anticipation / no recovery**,
  **effect (blood/debris) before contact**, floating feet during a power strike, hit-stop absent on a
  "heavy" blow.

---

## 8. Provider matrix
| Provider | Hands/contact | Combat/anime | Strategy |
|---|---|---|---|
| Veo 3.x / Sora 2 | decent short close-ups; degrades with 2 hands + object | limited multi-actor causality | one hand, short, **conceal** hard frames; keep exchanges to 1 cause→1 effect |
| Kling 2.x | good motion, hands vary | better stylized motion | use for the **travel/impact** beats; cut around contact |
| Runway | motion; hands weak | stylized ok | conceal contact; add impact-frame/flash in **post** |
| Any | — | — | **Conceal-and-cut** beats trying to render a clean deep-contact frame; add smear/impact-frame/hit-stop in edit |

---

## 9. Verification / QC (measurable)
- `finger_count_stable == true` (hand detector across frames) · `no_clipping` (limb intersection test)
- `contact_frame_present_or_cut == true` (either a clean contact frame or an intentional cut)
- **`effect_follows_cause == true`** (temporal order: cause_t < effect_t) — the key combat check
- `screen_direction_conserved == true` (axis not flipped across the exchange)
- `support_before_force == true` (foot plant / weight before strike; pose lane)
- `impact_has_anticipation_and_recovery == true` (phase presence)
- `object_rigid == true` (shape/label stable) — ties to LPR-004 (motor) + hand/pose detectors.

**Repo gate:** reuse the already-promoted `c_dag_proximal_to_distal`, `c_dag_staged_impact`,
`c_dag_robotic_movement_diagnostic` (kinds `technique`, layer `action` — registered); add the contact
concepts on the same pattern → `validate_repo.py` green.

---

## 10. Integration with the 2nd brain
- **Mode profile** `mode/hands_contact.yaml` — `activation_labels: [hands, holding, zipper, grab,
  handoff, punch, fight, combat, contact, weapon]`; forces coverage of `action` + physics/contact.
- **Concept cluster** (build ON the promoted DAG combat concepts): `c_causal_interaction_chain`,
  `c_grip_taxonomy`, `c_cut_around_impossible_frame`, `c_contact_before_displacement`,
  `c_one_hand_rule`, `c_object_rigidity`, `c_impact_frame_hit_stop`, `c_screen_direction_conservation`,
  `c_effect_follows_cause`. Kinds `technique`/`doctrine`; layer `action`; gated on contact/combat tokens.
- **Reasoning policy** `rp_interaction_causality`: build the causal chain → set contact type + grip →
  apply style timing/effects → decide render-vs-conceal cut → enforce §1 laws + screen direction →
  verify §9 → compile to prose.

**Build order:** promote cluster (on the DAG combat base) → add mode profile → add `rp_interaction_causality`
+ resolver → mappings → gate green → before/after emit proof.

---

## 11. Worked examples

**A. Fine manipulation (realistic) — zipper**
> Precision-pinch the orange pull (thumb+index), draw it screen-left→right **once**, teeth
> interlocking; other hand power-grips the base steady; deep-focus macro, short; object rigid, label
> readable. *Forbid:* finger duplication, hand-bag fusion, morphing zipper.

**B. Insertion (the cut solution) — phone into bag**
> `open_empty` (both hands hold mouth open, insert nothing) → **hard match-cut** → `open_loaded`
> (phone upper, slim item lower). `no_insertion` — never render the phone passing in.

**C. Person contact — hug**
> Two agents approach; arms wrap at consistent contact points (no clipping/fusion); shared weight lean;
> one settles head on shoulder; release = deliberate. Screen geography fixed.

**D. Anime punch (full staged impact)**
> Attacker screen-left: coil back, foot plant, gaze locks target (anticipation) → fist crosses with
> **smear + speed lines** (travel) → **impact frame** (2-frame white flash *hides contact*) →
> **hit-stop** (4-frame freeze = weight) → defender knocked **screen-right + back** along the force
> vector, dust ring (effect *after* contact) → attacker's fist overshoots, hair/cloth trail
> (follow-through) → settle to guard (recovery). Power = pelvis→shoulder→fist. *Forbid:* reaction
> before contact, axis flip, all-arm weightless strike.

**E. Anime weapon clash**
> Two blades travel (smears) → meet at the **weapon endpoints** at minimum distance → **impact frame +
> hit-stop + spark** (effect) → both recoil along their force vectors, sparks fall *after* → guard
> recovery. Contact is at the *weapon tips* (DAG 9-landmark incl. weapon endpoints), not the hands.

**F. Style transform (same punch, two styles) — proof the skeleton is shared**
- *Realistic:* subtle anticipation, real travel time, small recoil, no flash, motion blur, grounded
  weight, blood/impact **after** contact.
- *Anime:* expanded anticipation, smear travel, impact-frame flash, long hit-stop, big knockback,
  speed lines.
- **Held invariant in both:** contact precedes effect, reaction follows cause, screen direction,
  support-before-force, proximal-to-distal power. *Only timing + effects changed.*

---

## 12. The dynamic control object (workflows pass this downstream)
```json
{"interaction":{
  "contact_type":"strike","style":"anime",
  "causal_chain":["anticipation","travel","contact","impact_frame","hit_stop","knockback","follow_through","recovery"],
  "grip":null,"object":null,
  "geometry":{"attacker":"screen_left","defender":"screen_right","axis_locked":true,"reaction_vector":"screen_right_back"},
  "power_init":"proximal_to_distal","support":"foot_plant_before_strike",
  "effects":["smear","impact_frame_2f","hit_stop_4f","speed_lines","dust_ring_after_contact"],
  "cut_strategy":"conceal_contact_with_impact_frame",
  "laws":["contact_before_displacement","effect_follows_cause","screen_direction_conserved","support_before_force"],
  "forbid":["reaction_before_cause","axis_break","all_arm_weightless","effect_before_contact","hand_fusion"]}}
```
Compile to prose for the model; keep JSON as the verifiable twin; enforce `laws` and `forbid` every shot.

---

**Net:** hands, objects, people, and punches stop being four separate gambles and become **one causal
module** — same chain, different contact type, different stylization, same protected laws. Fine
manipulation and anime combat are the *same grammar* — one just exaggerates the phases and hides the
hard frame with a flash.
