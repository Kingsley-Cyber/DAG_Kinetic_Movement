# AI Video Movement Prompt System (CPCS)

> **AI agents:** this repo is AI-managed. Read **[`AGENTS.md`](AGENTS.md)** first — it routes every
> task to its home and carries the editing laws (anti-bloat, validation gate, commit conventions).

A modular, **movement-theory-based prompt system** for generating realistic UGC / talking-head video
with AI video models (Veo 3 / 3.1, Sora 2, Kling, Runway) and image models (e.g. Nano Banana Pro).

It packages research on **how human performance and motion can be captured and modularized into a
prompt** — using **FACS** (Facial Action Coding System) for the face and **Laban Movement Analysis**
for movement quality — into a reusable, structured "control score" that compiles down to a
ready-to-paste prompt. This repo is also a drop-in **Claude Code / Agent skill** (`SKILL.md`).

## The core idea

Realistic AI video comes from **directing a performance, not writing a vibe.** A vague prompt gives
the model nothing to render, so it defaults to a glassy, evenly-lit, robotically-still avatar — the
"AI tell." Instead you specify the performance in time (face + movement + body + camera), then
**compile it into the plain-language prompt the model actually reads.**

```
CPCS score (FACS + Laban + body + camera)  ──compiles──▶  prose prompt  ──▶  video model
```

The structured layers are scaffolding that force specificity; the model consumes the compiled prose.

## What's inside

| Path | What it is |
|---|---|
| `SKILL.md` | The method + workflow (install as a skill, or read as the guide) |
| `references/facs_laban_reference.md` | FACS action-unit catalog, Laban efforts/shape, plain-language translations |
| `references/method_details.md` | Realism lock list, reference-still pattern, captions/assembly, verification, per-model notes, reverse (video→prompt) extraction |
| `references/iphone_rawugc_realism.md` | **Field-tested preset** — the raw iPhone-UGC look, anti-AI-skin recipe, preferred formats |
| `assets/clip.iphone12_rawugc.hybrid.xml` | Compact YAML-in-XML clip package (< 2000 chars) |
| `assets/clip.iphone12_rawugc.yaml_json.txt` | YAML + embedded-JSON dual-parse clip package (< 2000 chars) |
| `assets/reference_still.iphone12_morning.txt` | Reference-still prompt (image-to-video identity + skin anchor) |
| `assets/clip_control_package.template.yaml` | Blank fully-scored control template |
| `assets/minified_control_package.example.json` | Minified JSON control example |
| `assets/combat_control_package.template.yaml` | **Combat authoring template** (YAML) — creative direction layer with kinematics, frame timing, spatial geometry, power curves, and mathematical constraints |
| `assets/combat_kinematics.template.json` | **Combat kinematic data template** (JSON) — motion solver layer with joint xyz tracks, typed contact events, Laban continuous floats, camera spatial path, verification metrics |
| `assets/combat_kinematics.fast_exchange.example.json` | **Worked kinematic example** — 8s kung fu exchange with full coordinate data, 5 typed contacts, Laban floats, camera path |
| `references/combat_choreography.md` | Full combat choreography reference — two-document architecture, metrics, Laban float encoding, contact types, timing ratios, style-specific notes |
| `lab/variants/naruto_sasuke_rooftop_clash.yaml` | **Worked authoring example** — 10s shonen anime fight with full CPCS scoring + combat metrics + compiled prompt |

## Key findings (learned from real renders)

- **Anti-AI skin (the #1 tell):** never ask for "smooth" skin — that *causes* the waxy plastic look.
  Instead name real microtexture (fine pores, uneven tone, fine lines, under-eye puffiness, T-zone
  sheen) **and** forbid `smooth_ai_skin / waxy / poreless / airbrushed`. For image-to-video, skin is
  locked by the **reference still**, not the video prompt.
- **iPhone-realism levers:** `30fps` (not cinematic 24), Smart-HDR flat tone, cool white balance,
  deep focus / no bokeh, floaty built-in stabilization.
- **Natural facial motion:** add a `face_motion` layer (eye darts, blinks, brow flickers, talking
  mouth shapes) so the face is never stiff/frozen.
- **Loosen the performance for raw UGC:** casual, low-key, a small "um," a glance away — over-direction
  reads as an actor hitting marks.
- **Format doesn't drive realism — content does.** XML/YAML/JSON are organizational scaffolding; the
  model reads the descriptive text. The compact **YAML-in-XML** and **YAML+JSON** packages are useful
  because they carry every realism lever in one paste under the ~2000-char input cap.

## Combat / fight choreography

CPCS extends beyond UGC into **fight and action sequences** with a mathematical metrics layer. Fight
choreography requires biomechanical precision that talking-head video doesn't — strike velocities,
frame-level timing ratios (anticipation : contact : follow-through), spatial geometry, power
escalation curves, and constraints with numerical tolerances.

The combat extension adds per-beat **kinematics** (closing speed m/s, strike velocity, screen
velocity, gap distances, rotation degrees), **frame timing breakdowns** per strike (with frame budget
validation against `duration × fps`), **character profiles** with body proportions and fighting
archetypes, **tempo/BPM curves** that escalate across the arc, **power curves** (normalized 0–1
force scaling), and **mathematical constraints** (contact accuracy < 0.05m, identity preservation
≥ 0.95, held impact frame minimums, audio sync ±2 frames).

Combat uses a **two-document architecture**: an **authoring layer** (YAML) for creative direction and
a **kinematic data layer** (JSON) for coordinate-level motion data. The authoring doc says WHAT
happens; the kinematic doc says WHERE and WHEN in coordinate space. Provenance links connect them.

- **Reference:** [`references/combat_choreography.md`](references/combat_choreography.md) — two-doc
  architecture, Laban float encoding, contact event types, metrics catalog, style-specific notes
- **Authoring template:** [`assets/combat_control_package.template.yaml`](assets/combat_control_package.template.yaml)
- **Kinematic template:** [`assets/combat_kinematics.template.json`](assets/combat_kinematics.template.json)
- **Authoring example:** [`lab/variants/naruto_sasuke_rooftop_clash.yaml`](lab/variants/naruto_sasuke_rooftop_clash.yaml)
  — 10s shonen fight, 6 beats, FACS + Laban + kinematics + compiled prompt
- **Kinematic example:** [`assets/combat_kinematics.fast_exchange.example.json`](assets/combat_kinematics.fast_exchange.example.json)
  — 8s kung fu exchange, joint xyz tracks, 5 typed contacts, Laban floats, camera path

## Output Formats

CPCS produces prompts in multiple formats. **The model always reads the prose description** — the
structured layers are scaffolding that forces specificity and keeps every realism lever from getting
dropped. Pick the format that fits your workflow:

| Format | Example file | Best for |
|---|---|---|
| **Compiled prompt only** | *(prose string inside any package)* | Pasting directly into a model input box. Under ~1500 chars, plain text, no structure to parse. |
| **Full YAML control package** | [`assets/clip_control_package.template.yaml`](assets/clip_control_package.template.yaml) | Full directorial scoring — every FACS action unit, Laban effort, body-movement beat, and camera parameter laid out with timestamps. Use when you want to design or review the performance before compiling to prose. |
| **Minified JSON** | [`assets/minified_control_package.example.json`](assets/minified_control_package.example.json) | Pipeline integration, API automation, programmatic workflows. Same data as the YAML package, machine-first. |
| **YAML-in-XML hybrid** | [`assets/clip.iphone12_rawugc.hybrid.xml`](assets/clip.iphone12_rawugc.hybrid.xml) | The compact house style — XML tags handle routing/metadata, YAML inside `<![CDATA[...]]>` carries the description the model reads. Under 2000 chars. Dual-parseable (XML parser gets the structure, the CDATA block is human-readable YAML). |
| **YAML + embedded JSON** | [`assets/clip.iphone12_rawugc.yaml_json.txt`](assets/clip.iphone12_rawugc.yaml_json.txt) | Alternative compact house style — the whole file is valid YAML, and the `json:` value is valid JSON (JSON is a YAML subset). Under 2000 chars. One file, two parsers, no realism lever dropped. |
| **Reference still** | [`assets/reference_still.iphone12_morning.txt`](assets/reference_still.iphone12_morning.txt) | Image-to-video identity anchor — a single image-model prompt that locks the face, skin texture, room, and wardrobe so they don't drift across clips. |

### Which format should I use?

- **Just pasting into Veo / Sora / Kling / Runway?** → Use the **compiled prompt only**. It's the
  prose string at the bottom of any package, or ask the skill to output just the prompt.
- **Building a multi-clip ad and want to version/review each beat?** → Use the **full YAML control
  package**. One file per clip, every layer visible for editing.
- **Need to stay under a ~2000-char input cap AND keep every lever?** → Use the **YAML-in-XML** or
  **YAML+JSON** compact format. These are the validated house styles — structured enough that no
  lever gets silently dropped, compact enough for model input boxes.
- **Feeding clips into an automated pipeline?** → Use the **minified JSON**. Same data, no comments,
  machine-first.
- **Using image-to-video and need face/skin consistency across clips?** → Generate a **reference
  still** first — it's the identity anchor that every video clip inherits from.

> **Tip:** format doesn't drive realism — content does. The structured layers exist to force you (or
> the agent) to be specific about performance, skin, camera, and body movement. Once that specificity
> is captured, the compiled prose carries it regardless of whether the scaffolding was YAML, JSON, or
> XML.

## Using it as a skill

Point Claude Code (or a compatible agent) at this folder as a skill, or open the packaged `.skill`
and install it. It triggers on requests like "make my product video look real," "write me a UGC ad
prompt," or "why does my AI creator look fake." Then it walks the workflow above.

## Use it from another agent

`AGENT_PROMPT.md` has a ready-to-paste kickoff prompt for a Codex-style / coding agent. It clones this
repo, internalizes the method, and works at full depth — the iPhone-12 raw-UGC realism, the
anti-AI-skin recipe, and the compact YAML-in-XML / YAML+JSON output under 2000 characters. Hand it
your product and it produces the reference still + clips.

## Prompt Lab (A/B testing + pattern curation)

`lab/` is a tracking system for A/B testing prompt variations and curating the patterns that drive
good output. Every variant, render result, and finding is a structured, machine-readable record, so
an AI agent loads one file (`lab/registry.yaml`) and **recommends prompt combinations** for a goal.

- **`lab/registry.yaml`** — levers vocabulary + variants + patterns + experiments (the source of truth)
- **`lab/AGENTS.md`** — how an agent recommends a combination and logs results
- **`lab/variants/`** — tracked prompt bodies · **`lab/runs/results.csv`** — scored results ledger ·
  **`lab/experiments/`** — A/B tests · **`lab/schema/`** — record shapes

Ask an agent: *"using lab/, recommend a combination for max realism, iPhone look, 4s talking-head."*
See `lab/README.md`.

## Research

The `research/` folder contains the underlying research package — the CPCS directorial-control paper,
the FACS/Laban framework, schemas, a RAG corpus, reference indexes, and the reverse (video → CPCS)
extraction pipeline. Start with
`research/CPCS_FACS_Laban_AI_Video_Research_Package_v1.2/paper/` and that package's own `README.md`.
The skill in this repo is the practical, generation-side distillation of that research.

## Ethics & rights

Preserve *structure* (timing, movement quality, camera grammar), not identity or unverifiable hype.
Keep product/proof claims truthful and substantiated. When recreating a reference video, swap identity,
voice, logos, and any distinctive/recognizable choreography — extract movement quality and timing, not
a clone.

## License

[MIT](LICENSE) — free to use, modify, and distribute. Open-source research release.
