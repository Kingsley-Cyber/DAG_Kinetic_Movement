---
id: cpcs.reference.natural_dialogue_mode
kind: feature_spec
epistemic_status: PROJECT_DERIVED
acquisition: authored
primary_route: (buildable spec for the 2nd brain)
companions: [cpcs.reference.living_performance_realism, cpcs.reference.format_craft]
version: 1.0
status: ready_to_build
---

# Natural Dialogue Mode — a foolproof, elite spec

A **behavior mode** for the 2nd brain that guarantees spoken lines come out as *a real person /
creature talking*, not AI-voice. It activates on dialogue, forces the audio + breath coverage the
brain otherwise skips, retrieves dialogue-realism knowledge, and **directs delivery in time** — then
compiles to the prose the model reads (or to SSML for dubbing).

> **Core theorem:** natural dialogue = **spoken-register CONTENT** + **time-directed DELIVERY**, both
> present, both bounded. Miss either and it reads AI. This is the exact same law as face realism
> (§ living-performance): *direct it in time; don't describe it as a vibe.*

---

## 0. Why this exists — the verified gap

- Dialogue realism lives across the `audio` and `breath and performance` / `performance and dialogue`
  layers (all registered in the ontology).
- **The UGC domain does not require `audio`:** `required_layers: [attention and hooks, camera,
  marketing, performance]`. So on the most common case (talking-head ads) the brain can **skip
  dialogue realism and nothing complains.** That's the leak this mode closes.
- The mechanism to fix it already exists: `activation_labels`, `query_term_gate`, `retrieval_frame`
  `required_coverage_slots` (merged into `required_layers` by `reason()`), and `reasoning_policies`.

---

## 1. The AI-voice tell taxonomy (the foolproof checklist — kill every row)

If any of these is present, it reads AI. The mode exists to eliminate all of them.

### A. Content tells (the words themselves — the half everyone forgets)
| Tell | Symptom | Fix |
|---|---|---|
| Written register | "This bag is stylish, spacious, and perfect for everyday use." | rewrite to spoken register (§5) |
| Adjective stacking | 3+ adjectives in a row | one vivid detail; show don't list |
| Ad-copy / CTA-speak | "You'll love it!" | only if a real person would say it, in their words |
| Complete, balanced sentences | grammatically perfect, no fragments | fragments, incomplete thoughts, self-interrupts |
| No reaction | leads with the feature, not the human | front-load the reaction ("okay I did *not* expect…") |
| Generic, no specificity | "great quality" | one concrete, personal detail |

### B. Delivery tells (the timing)
| Tell | Symptom | Fix |
|---|---|---|
| Evenly metered | every word same weight/pace | vary pace; one stressed payload word |
| Breathless | no inhale, no phrasing | pre-line breath + breath at thought boundaries (§7) |
| Zero disfluency | too clean | bounded disfluency budget (§8) — 0 is also a tell |
| No pre-emphasis pause | reveal lands flat | ~200–300ms pause before the payload |
| Wrong stress | stress on a function word ("the", "is") | stress the new/contrastive content word |
| Uptalk on everything | every clause rises | contour by intent (§9) |
| Flat affect | one monotone emotion | VAD→acoustic mapping (§10) |

### C. Embodiment / AV tells
| Tell | Symptom | Fix |
|---|---|---|
| Mouth desync | lips don't match audio | short clear line; phoneme-lockable; provider that supports it |
| Still body while talking | no accent on stress | small lean/gesture on the stressed word (§11) |
| Dead gaze | locked stare through the line | look away while forming the thought, back on delivery |
| No breath visible | chest/shoulders static | visible inhale before speaking |
| No non-lexical | robotic cleanliness | breath, lip-smack, swallow (§11) |

If all three blocks pass → it reads real. That is the mode's definition of done.

---

## 2. How it maps to the brain (verified primitives)

| Concept | Primitive |
|---|---|
| behavior mode | `mode/natural_dialogue.yaml` profile (activation_labels, required coverage, defaults) + `rp_natural_dialogue` reasoning policy |
| activation prompt | detection rule → `activation_labels` + `retrieval_frame.required_coverage_slots` |
| context query | relevance-gated retrieval — the dialogue concept cluster surfaces via `query_term_gate` |
| "make it think" | `rp_natural_dialogue.execution_strategy` (ordered thinking steps) |
| the output | a **Delivery Plan** (§6) compiled to NL for the model / SSML for dub |

---

## 3. Part 1 — Activation (the trigger)

### 3.1 Detection ruleset (foolproof; runs in intent normalization)
Activate Natural Dialogue Mode when the normalized request contains **any**:
- a **quoted line**: `"..."` or `'...'` of ≥2 words
- speech verbs: `says|say|saying|said|speaks|tells|asks|replies|whispers|shouts`
- narration markers: `voiceover|voice-over|VO|narration|narrates|talking to camera|piece to camera|monologue|dialogue`
- script layout: `line:`, `script:`, `<character>:` name-colon turns, `(V.O.)`, `(O.S.)`
- performance intent: `he/she/they/it says|creator says|talks about`

**Do NOT activate** on: pure b-roll / product-only shots, "text on screen" (that's captions, not
speech), or ambient-only scenes. When ambiguous, activate but set `speech_present: uncertain` and ask.

### 3.2 The mode profile
```yaml
schema: cpcs.profile/1.0
profile_id: profile://mode/natural_dialogue/1.0
profile_kind: mode                       # composes ON TOP of the active domain (ugc, dialogue, anime…)
extends: []
priority: 70                             # above domain defaults so coverage is forced
activation_labels: [dialogue, voiceover, talking, spoken, monologue, narration]
query_term_gate: {any: [dialogue, voiceover, says, talking, line, script, speaks, narration, monologue]}
required_layers: [audio, "breath and performance", "performance and dialogue"]  # the slots UGC skips
retrieval_frame:
  required_coverage_slots: [audio, "breath and performance"]   # merged into required_layers by reason()
  excluded_layers: []
defaults:
  audio:
    register: spoken            # not written
    delivery: time_directed     # not even-metered
    music: false                # authenticity default; override intentionally
    mic: on_device_or_close     # room tone present
  performance:
    breath: phrased
    disfluency: bounded
    gaze: think_away_deliver_back
component_profiles: [profile://capture/authentic_ugc_v2]   # inherits phone-mic realism when UGC
verification_metrics:
  - {metric_id: metric_spoken_register, target_paths: [audio.register], method: register_classifier, observability: measured}
  - {metric_id: metric_delivery_timed, target_paths: [audio.delivery], method: prosody_present_check, observability: measured}
```

### 3.3 Composition (how it stacks)
- **UGC + natural_dialogue** → phone-mic register, casual friend delivery, ambient, no music.
- **cinematic dialogue + natural_dialogue** → keeps `dialogue.yaml`'s subtext/blocking, adds delivery timing + breath.
- **anime/creature + natural_dialogue** → routes to §12 (species/creature vocalization) instead of human prosody.
Mode wins on the audio/delivery fields (priority 70); the domain keeps its camera/marketing/style.

---

## 4. Part 2 — The knowledge cluster (what the context query pulls)

Promote via the bridge (kinds = registered `technique`/`doctrine`; layers registered; namespaces
`audio.*`/`performance.*`; gates narrow so they don't intrude on the retrieval benchmark). Sourced
from LPR-005 (emphasis) and LPR-009 (voice).

| Concept id | Layer | Controls (mapping target) | Gate tokens |
|---|---|---|---|
| `c_spoken_register_scripting` | performance and dialogue | `performance.spoken_register` | script, dialogue, line, says, wording |
| `c_prosodic_stress_accent` | audio | `audio.prosodic_stress` | stress, emphasis, accent, delivery |
| `c_breath_phrasing` | breath and performance | `performance.breath_phrasing` | breath, breathe, phrasing, inhale |
| `c_bounded_disfluency` | performance and dialogue | `performance.disfluency_budget` | filler, um, natural speech, disfluency |
| `c_speech_pace` | audio | `audio.speech_pace` | pace, wpm, tempo, fast, slow talk |
| `c_thinking_pause` | audio | `audio.thinking_pause` | pause, beat, hesitation, thinking |
| `c_emotional_prosody` | audio | `audio.emotional_prosody` | tone, emotion, excited, sincere, warm |
| `c_av_speech_embodiment` | performance | `performance.av_sync` | lip sync, mouth, gesture, gaze, talking |
| `c_nonlexical_vocalization` | audio | `audio.nonlexical` | breath, sigh, laugh, lip smack, swallow |
| `c_turn_taking` | performance and dialogue | `performance.turn_taking` | conversation, two people, interrupt, back and forth |

**Example promotable concept (full shape):**
```json
{"id":"c_spoken_register_scripting","kind":"technique","layer":"performance and dialogue",
 "name":"Spoken-register scripting",
 "what":"Real speech is not written prose: it uses contractions, fragments, discourse markers (so/okay/honestly), self-interrupts, one concrete detail instead of adjective stacks, and leads with reaction not features. Rewriting a written line into spoken register removes the single biggest dialogue AI-tell before any audio model is involved.",
 "use_when":"any line a subject will speak on camera or in voiceover",
 "nl_triggers":["spoken register","natural dialogue wording","how a real person would say it","rewrite the line"],
 "query_term_gate":{"any":["script","dialogue","line","says","wording","voiceover","monologue"]},
 "status":"partial","evidence":[],
 "source":["DAG_Kinetic_Movement:RESEARCH_QUERY_living_performance_realism.md#LPR-009"],
 "provenance":{"origin":"natural_dialogue_mode","promoted_by":"claude_dag_bridge","promoted_at":"2026-08-09T00:00:00Z"}}
```
**Example mapping (concept → control, with prose projection):**
```json
{"id":"mapping_spoken_register","concept_id":"c_spoken_register_scripting","target_type":"control",
 "target_id":"performance.spoken_register","encoding":"prose",
 "mapping":{"directive":"rewrite written line into spoken register before delivery"},
 "representation_strategy":{"semantic_authority":"canonical_json_score","projections":[
   {"format":"natural_language","roles":["qualitative_direction"],
    "expresses":["spoken register","reaction-first"],
    "template":"Write the line the way a real person actually talks: contractions, a fragment or two, one discourse marker (so/okay/honestly), lead with the reaction not the feature, and one concrete specific detail instead of stacked adjectives.",
    "loss":"low","limitations":["content only; delivery timing handled by prosody controls"],"conditioning_effects":[]}]},
 "loss":"low","provider":null,"model_version":null,
 "sources":["DAG_Kinetic_Movement:RESEARCH_QUERY_living_performance_realism.md#LPR-009","lab/concepts.jsonl#c_spoken_register_scripting"]}
```

---

## 5. Part 3 — The reasoning policy (make it think about delivery)

```json
{"id":"rp_natural_dialogue","display_name":"Natural dialogue delivery",
 "concept_ids":["c_spoken_register_scripting","c_prosodic_stress_accent","c_breath_phrasing",
                "c_bounded_disfluency","c_speech_pace","c_thinking_pause","c_emotional_prosody",
                "c_av_speech_embodiment","c_nonlexical_vocalization"],
 "execution_strategy":[
   "1. CONTENT: rewrite each line into spoken register (c_spoken_register_scripting). Reject written-register/ad-copy.",
   "2. EMOTION: set VAD for the line; map to acoustic targets (c_emotional_prosody).",
   "3. STRESS: pick the single payload word; place a pre-emphasis pause before it (c_prosodic_stress_accent, c_thinking_pause).",
   "4. BREATH: place a pre-line inhale and breaths at thought boundaries (c_breath_phrasing).",
   "5. PACE: set wpm; vary fast(setup)->slow(payload) (c_speech_pace).",
   "6. DISFLUENCY: spend the bounded budget at thought boundaries only (c_bounded_disfluency).",
   "7. EMBODIMENT: body accent + gaze away/back + visible breath on the stress (c_av_speech_embodiment).",
   "8. NON-LEXICAL: add inhale/lip-smack/swallow sparingly (c_nonlexical_vocalization).",
   "9. VERIFY against the AI-voice tell taxonomy (§1); repair until all three blocks pass.",
   "10. COMPILE to NL for the model (and SSML for dub)."],
 "contraindications":["no speech present","pure b-roll","on-screen text only (that's captions)"],
 "epistemic_class":"authored","evidence_status":"qualified",
 "confidence":0.7,"confidence_basis":"assembled from FACS/Laban/prosody literature; conditioning effects require per-model experiment"}
```

---

## 6. The Delivery Plan (the heart — time-indexed output object)

Every spoken line resolves to this canonical object. It is provider-neutral; it compiles down to NL
or SSML.

```yaml
delivery_plan:
  line_id: s04_line
  speaker: "[swap: creator]"
  register: spoken
  text: "Okay so — I did not expect to like this this much."   # already spoken-register
  emotion_vad: {valence: 0.6, arousal: 0.55, dominance: 0.4}   # pleasantly surprised
  target_duration_s: 3.2
  pace_wpm: 165
  stress_words: ["not"]                # the single payload
  contour: downglide_warm              # statement, warm close
  events:                              # ordered, time-indexed
    - {t: 0.00, type: breath, value: small_inhale}
    - {t: 0.15, type: speech, value: "Okay so", pace: fast}
    - {t: 0.55, type: pause, value: thinking, dur_ms: 260}     # pre-emphasis beat
    - {t: 0.81, type: speech, value: "I did", pace: normal}
    - {t: 1.05, type: stress, value: "not", pitch: lift, body_accent: small_lean}
    - {t: 1.30, type: speech, value: "expect to like this", pace: normal}
    - {t: 2.35, type: speech, value: "this much", pace: slow, contour: trail_off}
    - {t: 2.70, type: nonlexical, value: soft_exhale}
  disfluency: {fillers: 0, false_starts: 0, repairs: 1}   # the "so —" self-interrupt counts as repair
  av_sync: {mouth: phoneme_locked, gaze: away_0.0_to_0.55_then_lens, blink_after_stress: true}
  invariants: {no_music: true, no_even_meter: true, no_written_register: true}
```

**JSON precision twin** (for verification/tooling) mirrors this with numeric `t`/`dur_ms` and the
`verify` booleans from §13.

---

## 7. Prosody & timing grammar (placement rules)

- **Stress = new/contrastive content word**, one primary per clause. Never a function word.
- **Pre-emphasis pause** 200–300ms *before* the payload word or the reveal (the "beat").
- **Pitch contour:** rise on stress; **downglide** to end a statement; **uptalk** only on a genuine
  question/uncertainty; **trail-off** (soft devoicing) at end-of-thought — never a clean cutoff.
- **Pace varies:** faster on setup/filler, **slower on the payload** (this contrast *is* emphasis).
- **Breath = phrasing:** inhale before a new thought/clause; audible when emotional.

## 8. Disfluency budget (bounded imperfection)

- **Types:** filler (`um/uh/so`), false start, self-repair (`—`), elongation (`soo`), glottal stop.
- **Budget:** ~1 per 5–7s; **max 2** in a short clip. **0 is also a tell** (too clean) → aim for 1.
- **Placement:** at thought boundaries or right before a hard word — **never on the stress word.**
- **Purposeful, not scattered.** Over-budget = "nervous/drunk"; that's a different (usually unwanted) character.

## 9. Contour presets
`downglide_warm` (sincere close) · `flat_rise` (curiosity) · `uptalk` (genuine question) ·
`trail_off` (thinking/soft) · `punch_drop` (confident claim: rise on stress, hard drop after).

## 10. Emotional prosody — VAD → acoustic

| Axis | + | − |
|---|---|---|
| **Valence** | brighter timbre, upward contour | darker, downward |
| **Arousal** | faster rate, higher pitch, more energy, sharper onsets | slower, breathier, softer |
| **Dominance** | lower pitch floor, steady | higher, more variable, hedged |

**Presets:** excited `{v+.7,a+.7,d+.4}` · sincere `{v+.5,a-.2,d+.3}` · conspiratorial `{v+.3,a+.2,d+.5,quiet}`
· tired `{v-.3,a-.6}` · amused `{v+.6,a+.3, breathy_laugh}` · awed `{v+.5,a+.4, slow, breath}`.

## 11. AV-sync & embodiment
- **Mouth** to phonemes (model-dependent — keep the line short + clear so it can lock).
- **Body accent** (small lean/gesture) on the stress word, synced to the audio peak (LPR-005).
- **Gaze:** look slightly **away while forming** the thought → **back to lens on the payload**.
- **Visible breath** before speaking; micro-nod on agreement words.

## 12. Species / creature / non-verbal (all living things — foolproof coverage)
- **Animals:** species-true vocalization synced to throat/body; **no lip-sync to human words**;
  emotional prosody expressed via species signals (ears/tail/posture) + call rate/pitch.
- **Creatures/monsters:** invented voice, but the **same timing grammar** (breath, stress, pause,
  contour) applied to the vocalization; add designed non-lexicals.
- **Non-verbal humans:** the "line" is carried by sign/gesture/expression; timing grammar applies to
  the *gesture* (anticipation, stress-hold, recovery).
- **Graceful degrade:** no speech → mode deactivates → ambient only (no forced VO).

## 13. Multi-speaker / turn-taking
- **Turn gap** ~200ms (natural); **overlap** only on backchannels (`mhm/yeah/right`);
  **interruption** cuts the prior line mid-word.
- Each speaker gets **their own** delivery plan + VAD — don't make two people sound identical.
- Backchannels from the listener during the speaker's line = strong realism.

---

## 14. Emit — compile the plan to what the model reads

The delivery plan is scaffolding. Compile to **NL** for the generator (translate the schedule to
plain language); keep the JSON plan as the precision/verify twin; export **SSML** for dub pipelines.

**Compiled NL (what you paste into Veo/Sora):**
> …[swap: creator] takes a small breath, then—quick—"Okay so," a short beat as if choosing the word,
> then lands with a lift on "*not*" (a tiny lean in on that word), easing warmer and slower into "like
> this this much" and trailing off with a soft exhale. Conversational, ~165 wpm, one small self-
> interrupt, eyes flicking away as they think then back to lens on the line; ambient room tone, no
> music. (no on-screen text)

**SSML twin (for TTS dub — Kling/Runway/mute paths):**
```xml
<speak><break time="150ms"/>Okay so<break time="260ms"/> I did <emphasis level="strong">not</emphasis>
<prosody rate="95%">expect to like this</prosody> <prosody rate="80%" pitch="-1st">this much</prosody><break time="120ms"/></speak>
```

## 15. Provider matrix
| Provider | Native voice | Use |
|---|---|---|
| **Veo 3.x** | yes (strong) | best; keep line ≤ ~10–12 words / 8s, one clear emotion; honors breath/pace loosely |
| **Sora 2** | yes | good; longer clips; native audio |
| **Kling 2.x** | limited/none | generate **mute**, dub with TTS via the **SSML twin**, lip-sync tool |
| **Runway** | none reliable | mute + SSML dub |

The SSML twin makes the delivery plan **provider-agnostic**: native models read the NL, dub models read the SSML — same plan.

## 16. Verification / gate (foolproof QC)
Machine-checkable booleans on the plan:
`spoken_register==true` · `has_pre_line_breath` · `exactly_one_primary_stress` ·
`pre_emphasis_pause_ms in [180,320]` · `disfluency_count in [1,2]` · `not_even_meter` ·
`no_written_register_phrases` · `body_accent_on_stress` · `line_words <= provider_budget`.
Repair loop until all pass (the `rp` step 9).
**Repo gate:** concept kinds = `technique` (registered), layers registered, `audio.*`/`performance.*`
namespaces registered, gates narrow (don't hit retrieval-benchmark forbidden lists) → `validate_repo.py` green.

## 17. Anti-patterns
- Over-disfluency (nervous/drunk) · written register creeping back (adjective stacks, CTA-speak) ·
  even meter · breath on every word · stress on a function word · uptalk on everything · line too
  long → model rushes → robotic · emotion *label* with no acoustic mapping.

## 18. Build plan (ordered, through the pipeline)
1. Green the pending promotion (kind fix), then **promote the 10-concept cluster + mappings** (bridge).
2. Add `mode/natural_dialogue.yaml` (activation + forced coverage slots + defaults).
3. Add `rp_natural_dialogue` to `reasoning_policies.jsonl`.
4. Add the **detection rule** (§3.1) into intent normalization.
5. Add the **delivery_plan schema** + NL/SSML emit templates.
6. `validate_repo.py` green → **before/after emit proof** (§ worked examples).

---

## Appendix — worked examples (before → after)

**A. UGC talking head**
- Before: "This sling bag is stylish, spacious, and perfect for everyday use. You'll love it!"
- After (line): "Okay so — I did *not* expect to like this bag this much." + delivery plan (§6).

**B. Cinematic confession (restrained)**
- Before: "I have always loved you and I never told you because I was afraid."
- After: "I— …I should've said this a long time ago." VAD `{v+.2,a+.3,d-.2}`, two breaths, a repair,
  trail-off, gaze down-then-up on "said."

**C. Two-person argument (turn-taking)**
- A: "You don't get to—" B (interrupts): "No, *you* don't." 200ms→0 overlap; B stress on "you";
  A backchannel-less (cut off). Two distinct VADs.

**D. Creature (non-human)**
- A small dragon's low chuff → rising trill on the "payload" beat; throat/chest sync; no human
  lip-shapes; ears forward on the trill (species affect). Same timing grammar, species signal set.
