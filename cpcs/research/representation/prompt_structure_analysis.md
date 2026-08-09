---
id: cpcs.representation.prompt_structure_analysis
kind: method
epistemic_status: INFERENCE
acquisition: authored
sources: [SRC-010, SRC-012]
primary_route: cpcs/research/representation/
interfaces:
  - cpcs.representation.pov_glasses_bag_specimen
  - cpcs.canonical.temporal_coupling
  - cpcs.gov.control_plane_reference
  - cpcs.gaps.understanding_register
---

# Prompt Structure Analysis — Smart-Glasses POV Sling-Bag Video

> Analysis of the agent-produced hybrid prompt captured in
> [`hybrids/pov_glasses_bag_prompt_specimen.md`](hybrids/pov_glasses_bag_prompt_specimen.md):
> a 20 s, first-person smart-glasses UGC video of a compact black sling bag.
> Status: INFERENCE — reasoned analysis over tree conventions; the governance
> rule *no carrier superiority* applies (control plane reference §11.7):
> these claims require experiments (`carrier_effect_design`) before any
> format is promoted over another.

## 1. What the document is

A **quad-carrier document with a declared authority hierarchy** — the first
known specimen that operationalizes the format-stack discussion:

| Layer | Carrier | Role declared in the document |
| --- | --- | --- |
| Shell + order | XML | document skeleton, shot/cut graph, policies (`format_policy`, `input_policy`, `pov_policy`), CDATA embedding |
| Directing | YAML | `control` — the semantic contract: project laws, hand law, object state machine, shots, render rules, forbid list |
| Precision | JSON | `precision` — the exact clock: timebase, retiming, shot/cut frames, speech schedule, object events, verification assertions |
| Delivery | prose | `execution` — final imperative restating the core laws for the model to follow |

The authority hierarchy is **self-declared**: `format_policy primary="yaml+xml"
precision="json"` and, in the execution prose, "Read YAML as the primary
directing layer, execute the XML shot and hard-cut order, and use JSON as the
exact clock and state authority." The document does not leave format roles to
chance — it assigns them.

## 2. Document anatomy (the five-part skeleton)

1. **Policy block** (`format_policy`, `input_policy`, `pov_policy`) — three
   one-line declarations that set the frame for everything below: which
   carriers are used and which is authoritative; that no reference media
   exists; that the camera grammar is head-mounted glasses POV.
2. **Shot graph** (`<order>`) — 7 shots + 6 cuts with cut types and
   continuity annotations (`continuity_state="closure_released"` on cut_04,
   `hard_match` on cut_05). Pure sequence structure, no content.
3. **Directing contract** (`<control lang="yaml">`) — the semantic core:
   project, hand_law, continuity, performance, object_mechanics (part_graph +
   zipper state machine), per-shot cards, render_rules, a 27-item forbid
   list.
4. **Precision contract** (`<precision lang="json">`) — the exact clock and
   state authority: timebase, retiming, frame-exact shots and cuts, speech
   schedule, object events with pre/post, wear events, and an 18-assertion
   verification block.
5. **Execution imperative** (`<execution>`) — the single prose paragraph that
   would survive even if every structured layer were stripped: two-hand law,
   contact preservation, head-locked POV, causal law, negative operations,
   stability locks.

The CDATA technique is the structural key: it makes XML the universal
carrier — one document, three embedded languages, zero escaping hazards,
and ordered sections that cannot be reordered by an authoring tool.

## 3. The eight control axes — coverage by layer

| Axis | What it controls | Covered by | Strength |
| --- | --- | --- | --- |
| Temporal (T) | shot boundaries, pacing, duration, continuity | `<order>`, JSON timebase/retiming/cuts, speech schedule | strong — frame-exact, seconds-authoritative (master clock doctrine honored: seconds authoritative, frames derived) |
| Camera (C) | shot size, angle, movement, lens character | `pov_policy`, YAML capture grammar, render_rules camera lock | strong — a full POV grammar (head-locked, fisheye, hands-from-bottom, AE shifts) |
| Object (O) | topology, states, transitions, permanence | YAML part_graph, zipper state machine, JSON object_events, forbid items 8–14 | strong — two independent systems with pre/motion/post per operation |
| Performance (P) | action, gaze, micro-motion, energy | YAML performance block, per-shot action, voice_arc | strong — unrehearsed baseline, gaze-as-camera, breathing micro-bob |
| Narrative (N) | dialogue, pacing, shot intent | YAML shots (purpose/dialogue/audio), JSON speech schedule | strong — wpm-exact speech with word counts |
| Constraint (F) | anti-artifacts, negative space | 27 forbid items, render_rules locks, JSON verification negatives | strongest in class — each forbid maps to a known failure mode |
| Determinism (D) | reproducibility, versioning, loss | JSON verification block (post-hoc), exact clock | partial — no hash/version field, no schema; assertions are post-generation |
| Provider adaptability (A) | downcasting, multi-surface | `<execution>` prose as implicit fallback | weak — no target provider declared, no downcast plan, no loss budget |

## 4. Control techniques worth naming (grad-student level)

**T1 — Failure-mechanism reasoning, not symptom forbidding.** The most
sophisticated move in the document: the execution prose states *why* the
right hand must never leave the bag — "an empty reaching hand is what makes
the model hallucinate an extra hand." The agent identified the causal
mechanism of the artifact and engineered the constraint to prevent the
*cause*. The forbid list then re-states each failure mode as a negative —
but the positive law comes first.

**T2 — Negative specification of the state machine.** `close_panel` and
`zip` are fully defined (pre/motion/post) but marked
`execute_in_this_video: false`. Defining the operations the model must NOT
perform, with the same rigor as the operations it must, closes the state
space: the model cannot invent a closing beat because the closing transition
already exists and is explicitly excluded. This is the state-machine
equivalent of an exhaustiveness proof.

**T3 — Causal decomposition into independent systems.** The causal law
declares the zipper and the panel as TWO SEPARATE SYSTEMS: slider controls
closure; hands control the panel; unzipping releases but never self-opens.
Every forbid item and render rule traces to this decomposition (teeth change
only behind the slider; panel moves only after the grip; cavity follows
panel rotation). One root principle, many enforced consequences — the
opposite of a flat list of unrelated don'ts.

**T4 — Policy-then-reference DRY.** The POV grammar is declared once at the
top (`pov_policy`) and enforced in three places (`render_rules.camera`,
`pov_integrity`, per-shot camera fields) — and the JSON `verification` block
carries the machine-checkable form (`camera_is_head_locked_pov`,
`no_third_person_or_selfie_shot`). One source of truth, multiple binding
sites.

**T5 — Cut-edge continuity contracts.** Continuity is declared at the *cut*,
not just inside shots: cut_04 preserves `closure_released`; cut_05 is
`hard_match` with `changed_field: content_state_only` and a seven-field
preserve list (bag_geometry, panel_angle, both hand positions, camera,
head_angle, lighting). The match cut is a contract between two shots about
what may differ — exactly one field.

**T6 — Self-verification block.** The JSON `verification` object is an
18-assertion acceptance checklist the generation is measured against
(shot_order_exact, exactly_two_hands_all_frames, identity_drift_allowed:
false, …). The prompt carries its own post-hoc test suite — the seed of the
tree's verification/ route (verification_expectation_model) applied to
prompting itself.

**T7 — Internally consistent timing.** The retiming method is named
(`proportional_source_clock_expansion`, 14.558912 s → 20.0 s) and the speech
schedule is arithmetically self-consistent: s01 is 6 words over 1.946 s at
185 wpm (6/185 × 60 = 1.946). Seconds are authoritative; frames are derived
at 30 fps — the master clock doctrine applied literally.

**T8 — Layered reinforcement (five restatements of one law).** The two-hand
law appears as: positive rule (`hand_law`), render rule (`hand_integrity`),
machine model (JSON `hand_model`), negatives (forbid items 1–7), and prose
(execution). Deliberate redundancy: each carrier restates the law in its own
register (semantics / enforcement / data / negative / imperative). The
drift risk is the cost; the reinforcement is the benefit — see critique C2.

## 5. What it gets right

1. **Role-assigned carriers** — no format is asked to do what it is bad at:
   XML holds order, YAML holds semantics, JSON holds numbers, prose holds
   the final imperative.
2. **Cause-level artifact prevention** (T1) — the strongest known pattern for
   hand/object generation failures (extra hands, morph, state jumps).
3. **Machine-checkable acceptance criteria** (T6) — the generation can be
   scored against the verification block, enabling regression comparison.
4. **Continuity at the cut edge** (T5) — match-cut discipline that most
   prompts never express.
5. **Exactness where exactness matters** — frame boundaries, wpm, retiming
   math: the clock layer is fully determined.

## 6. Critiques (severity-ordered)

**C1 (high) — `long_video_lock` vs provider capability.** The document
demands one 20 s single-pass generation ("never return separate clips"),
but no provider surface is declared (`provider_capability_snapshots` route
exists for exactly this). If the target surface cannot produce 20 s
single-pass output, the document is un-executable as written — the lock
conflicts with the only viable execution path (segment + stitch). The
document should declare the target surface and a downcasting fallback.

**C2 (high) — five-layer redundancy drift.** The two-hand law is restated
five times in five registers. If any layer is edited without the others,
the layers contradict (e.g., JSON `hand_model` says left holds "rear shell
then top handle" while YAML `hand_law` says "never lets go until the bag is
open" — consistent today, but nothing enforces consistency). The
reinforcement is deliberate (T8), but the document lacks a consistency
check — which is precisely what a schema/validation layer would provide.

**C3 (medium) — no schema for the precision layer.** `precision="json"` is
declared but no JSON Schema or XSD is attached: nothing in the document
enforces that `pre`/`post` reference declared states, that cut frames equal
shot boundaries (they do: cut_01 at frame 72 = s01 end — verified manually),
or that speech words × wpm fit the shot window. Validation is asserted by
hand, not by tooling.

**C4 (medium) — verification booleans are post-hoc, not pre-generation
constraints.** `exactly_two_hands_all_frames: true` cannot condition the
generation; it can only measure it. The document does not distinguish
"conditioning" from "measurement" — a provider could satisfy the letter
(return a video) and fail every assertion. This belongs in a separate
verification contract, not inside the prompt's precision layer.

**C5 (low) — determinism axis incomplete.** No version, hash, or
provenance field on the document itself; no prompt_budget accounting (the
`prompt_budget/` route exists); no declared loss tolerance per carrier if a
surface rejects structured input.

**C6 (low) — implicit carrier-superiority claim.** `format_policy
primary="yaml+xml" precision="json"` asserts a role hierarchy. Governance
(control plane reference §11.7) holds *no carrier superiority — experiment
required*. This document is therefore a hypothesis to be tested with
`carrier_effect_design`, not an established fact.

## 7. Where this sits in the format landscape

- **Singles (YAML-only / XML-only / JSON-only / prose-only)** would each
  lose at least one control axis: prose-only loses O/F discipline; YAML-only
  loses the shot graph and exact clock; XML-only loses the state machine's
  semantic density; JSON-only loses authoring expressiveness and comments.
- **Pairs** cover two layers (e.g., YAML+XML from the lineage prompt covers
  authoring but not precision/determinism).
- **This document is the quad** — the complete stack in one artifact, with
  the authority hierarchy explicit. It is the strongest structure for
  object-causality-heavy, multi-shot, long-form generations, and the
  heaviest for quick iteration.

## 8. Best-for verdict

| Scenario | Recommendation |
| --- | --- |
| Object-causality-heavy multi-shot generation (this case) | quad with declared hierarchy — as here, plus schema + target surface (fix C1/C3) |
| Rapid lookdev / style exploration | prose-only or prose+YAML |
| Multi-provider distribution | quad + canonical JSON extraction + per-surface downcast plan (loss report) |
| Regression / versioned prompting | quad + version/hash + verification contract extracted out (fix C4/C5) |
| Agent-automated pipelines | same quad, generated from the tree's canonical IR |

## 9. Open questions captured while working (D8)

- **UG-008 (APPLY/WHEN):** Which carrier hierarchy does each provider
  surface actually follow best — the declared quad, YAML+XML pair, or
  prose-only? No experiment data exists in the tree; `carrier_effect_design`
  is the natural harness. (Cross-linked to the understanding register.)

## Verification

`test_analysis_covers_eight_control_axes`,
`test_critiques_severity_ordered`,
`test_specimen_referenced`,
`test_carrier_claims_marked_inference_not_established`,
`test_ug008_cross_linked_to_register`.
