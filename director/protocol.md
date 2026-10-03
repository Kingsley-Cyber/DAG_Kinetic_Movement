# Director protocol — how an LLM runs one ask

You are the reasoner. The repo gives you material (treatments, cards, manuals) and two code tools
(`check`, `emit`). You write the IR and the decision records; you never declare your own output
valid. Text-only output: the prompt is pasted into a model's prompt field.

## 1. Intent brief

Restate the ask in one paragraph: what the user locked (subject, action, duration, device,
style), what is open, the target model. Write it to `runs/<n>_<slug>/ask.md` under the ask.

## 2. Pass plan

Read `passes.yaml`. For every pass write one line in `ir.json → pass_plan`:
`{pass, active: true|false, reason}`. Mandatory passes are always active. Conditional passes are
active when their `when` condition holds for this ask. One override exists: a conditional pass
whose condition holds may still close when an active pass has already written everything this
pass would own for the ask; the reason must name that pass (run 001: world and action closed as
"covered by interaction"). `after` applies to active passes only. Synthesis runs twice: once after
the last active Reason-tier pass (logic) and once after the last active Style- or Render-tier pass
(taste); there is no third run.

## 3. Run the active passes in `after` order

For each active pass, the same eight steps:

1. **Input state**: the IR so far.
2. **Check research**: open only the treatments under `treatments/<pass>/` whose `triggers`
   match the ask and whose `not_when` does not. Follow their `backs` and `from` pointers only
   when the treatment is not enough.
3. **Check treatments already applied**: do not duplicate a control another pass owns.
4. **Identify gaps**: what this pass must decide that no treatment covers.
5. **Reason where allowed**: decide, choosing a thinking mode (direct · compare alternatives ·
   calculation · aggregation · repair). Pick "compare alternatives" when the choice is
   high-impact and uncertain. Pick "calculation" for durations, frames, speech capacity.
6. **Resolve decisions**: write controls into the IR with `pass`, `field` (within this pass's
   `owns`), `value`, `importance`, `lock`, `origin`, `treatment`, `capability`, `disposition`.
7. **Write output state**: beats, pathways, hands, entities, controls as the schema requires.
8. **Declare uncertainty**: any decision made without research is `origin: INFERENCE` and is
   appended to `director/gaps.jsonl` as `{date, run, pass, gap, why_it_matters}`.

A pass with nothing to decide closes in one line in `pass_plan.reason`.

Tier rule: Style and Render passes may add controls and weights; they never change `beats`,
`pathways` or `hands`.

## 4. Record shapes

**Origin** (the tree's `epistemic_status`): SOURCE_EVIDENCE · INFERENCE · CREATIVE_CHOICE ·
PROJECT_DERIVED · PROVIDER_EXPERIMENT · UNVERIFIED · CONTRADICTED · UNKNOWN.

**Decision record** (`decisions.jsonl`, one JSON object per line) for every decision that changes
the prompt:

```json
{"decision_id": "d001", "pass": "interaction", "question": "...",
 "alternatives": ["a", "b"], "selected": "a", "criteria": ["..."], "confidence": 0.6,
 "problem": "...", "treatment": "treatment id or null", "control": "control id",
 "expected_visual_effect": "...", "verification_target": "...", "origin": "PROJECT_DERIVED"}
```

`selected` must be one of `alternatives`. Confidence is your belief that the decision serves the
ask, not a probability of render success.

**Control** (in `ir.json → controls[]`):

```json
{"id": "c_grip", "pass": "interaction", "field": "interaction.grip", "value": "...",
 "importance": 0.8, "lock": false, "origin": "PROJECT_DERIVED",
 "treatment": "interaction.grip_power_bottle", "capability": "semantic",
 "disposition": "semantic", "exactness": "approximate",
 "expected_visual_effect": "...", "check": "..."}
```

A control may carry `beat` (a beat id) to apply to that beat only; a camera control scoped to a
beat must agree with that beat's contact state (a hidden contact is not shown in close-up; a
confirmed contact is not cut away from).

`capability` for the target model: native · approximate · semantic · unsupported · unknown.
`disposition` (exactly one): native · approximated · semantic · omitted · unsupported · unknown.
In text-only work nearly everything is `semantic`; `native` only for API fields the model profile
lists. A locked control with `exactness: exact` that the model cannot enforce blocks emission.

**Beat**: `{id, order, label, actor, description, min_s, min_s_origin, after: [], caused_by: [],
key_pose, importance}`. `after` is order only; `caused_by` is causation. Describe what a camera
would see, not what someone feels.

**Pathway** (one per physical task): `{id, object, end_state, stages: [...]}`. Stage kinds, in
order: precondition · anticipation · approach · contact · transfer · effect · follow_through ·
recovery · postcondition. A stage: `{id, kind, beat, hands_required, hands: [{actor, hand}],
state_before, state_after, reaction}`. Any stage that changes state needs a `contact` and a
`transfer` stage before it. Every `contact` needs a later `effect` with a stated `reaction`.
Plan pose-to-pose: write `end_state` first.

**Hand ledger**: `{actor, hand: left|right, beat, state}` where state is `free`, `camera`,
`holding:<object id>` or `on:<surface>`. A selfie or handheld shot keeps one hand on `camera`
for every beat unless a stage explicitly props or releases the phone.

**Anchors and deltas** (relative prompting): `anchors[] = {id, quality, beat, label, description}`
where `quality` is one of speed, weight, reach, size, intensity, distance, tempo, `label` is the
short phrase used to refer back ("the first reach") and `description` is a visible fact. A later
beat carries `relative: [{quality, relative_to: <anchor id>, step: slightly | more | much,
direction: more | less}]`; one delta per quality per beat; the anchor's beat must be earlier.
The emitter writes the anchor once after its beat and the delta as "…, slightly slower than the
first reach".

**Physics event** (one per beat at most): `physics_events[] = {event_id, beat, trigger: {actor,
part, action}, contact_surface, contact_state, force?, primary_reaction, secondary[], settle,
depends_on[], must_not_imply[], risk, origin}`. `contact_state` is physical_contact_confirmed,
near_contact, occluded_contact, editorial_impact or unknown. `force` is `{relative_to: <weight or
intensity anchor id, earlier beat> | null, step, direction}`; a first event with `relative_to:
null` needs such an anchor on its own beat. Write `trigger.action` as a verb phrase that follows
"<Actor>'s <part>" ("twist the cap", "comes down"). `must_not_imply` lines go to `verdict.md`,
never into the prompt. The emitter writes: cause, landing on the surface; reaction as the
secondary effects, then the settle.

**Laban** (performance pass): never a bare pole word. Each factor is a scaled position with a
confidence: `{"weight": 0.3, "time": 0.4, "space": 0.7, "flow": 0.6, "confidence": 0.5}` where 0 is
the first pole (light, sustained, indirect, free) and 1 the second (strong, sudden, direct,
bound). The emitter turns scales into wording.

## 4·0 Three invariants for every pass

1. **Relative, never absolute.** Set one anchor per quality as a visible fact on a named beat
   (`anchors[]`). Every later magnitude is a delta against that anchor (`relative_to`, step,
   direction), one escalation per quality. Avoid bare magnitude words in descriptions (the checker
   warns); named techniques such as "slow motion" or "real-time" are fine.
2. **Explicit where the contract says so** (`plan/ARCHITECTURE.md` §2.7): actors, hands, contact
   surfaces, event order, the reaction to every contact, end states, camera grammar. Where the ask
   is silent you author the scene, label it CREATIVE_CHOICE or INFERENCE, and stay inside the
   explicit column. Soft defaults ("a fight is fast") are overridable with a recorded reason.
3. **Read before you decide.** Each pass lists `reads` in `passes.yaml`; take those earlier
   decisions as fixed inputs and make yours consistent with them.

## 4·1 The scratchpad and how passes hand off

The run folder is the shared scratchpad: `ir.json` holds accepted decisions only;
`decisions.jsonl` the rationale and source of each consequential choice; `open.jsonl` open
alternatives, conflicts and revision requests; `check_report.json` the validation results.

- Take your pass's view (question, `reads`, treatments, locks). Propose your contribution, run the
  check for your pass, and only then treat it as accepted.
- Pass forward accepted decisions, a one-line rationale and unresolved questions. Do not pass
  draft thoughts or abandoned options.
- If you need another pass's decision changed, write a revision request to `open.jsonl`
  (`{"from_pass", "to_pass", "field", "reason"}`); never overwrite it. Synthesis closes or
  escalates every open item before emit.
- Reasoning again from the same scratchpad is a new creative run: give it a new variant id.

## 4·2 Writing rules

- Replace a vague style word with the variables behind it: not "cinematic" but the colour,
  framing, lens, frame rate, mount and light that produce the intended meaning.
- Lead each description with the main idea: the core action and the force of the pose first,
  small details last.
- Budget seconds as a timeline, not adjectives. Start the clip as late as the story allows.
- Declare spacing on every moving beat (`ease_in`, `ease_out`, `ease_in_out`; `even` only with a
  reason) and name the key poses. Constant motion throughout is the default failure.

## 4a. Camera grammar (mandatory on every ask)

Choose the camera move from `director/vocab/camera_moves.yaml` (48 moves in 7 categories, each
with a `function` hint: what the move does for the viewer). State it in the four-part grammar:
move phrase · Movement · Speed · Framing · End. Name the layer: a move is the camera body moving or
rotating; a zoom or tilt-shift is a lens change and must never be written as camera motion. One
move per shot; a second move needs its own beat and an order word. If no catalog move fits, use
`move: custom` and justify it in `decisions.jsonl`. For a propped or fixed selfie use
`camera.selfie_framing` instead.

## 4b. Intents and the dialect lens

The IR is model-agnostic. When you want the model to do something a prompt can carry in
different ways (stress a word, hold a beat, move the camera, speak a line, exclude something),
write the **intent** in agnostic form on the control (for example `value.emphasis: ["not"]` on a
dialogue control, `hold: true` on a beat). Never write model syntax (`<i>`, asterisks, API field
names) into the IR.

During model fit (the synthesis pass after Style), read `director/profiles/<model>.yaml →
dialect.levers`. If the dialect has no lever for an intent that matters, lower the control's
importance or choose another way to carry the meaning, and record the decision. `emit` applies the
lever at assembly and writes `lever: <intent>` into the receipt so the render verdict can credit or
blame it. A lever's `evidence` (owner_observed, documented, measured, unknown) is per model and per
route; treat `owner_observed` as a hypothesis.

## 4c. Reasoning control layer: how to think per pass

| Situation | Mode | What you produce |
|---|---|---|
| one plausible plan, validators strong | direct | the control, one line of reason |
| creative fork, or high impact with uncertainty | compare alternatives | a DecisionRecord with ≥ 2 alternatives and criteria |
| durations, frames, speech capacity, distances | calculation | the number with its inputs and their origins |
| merging partial decisions across passes | aggregation (synthesis) | the resolved control and the conflicts you removed |
| a failed render or read-back | repair | the smallest IR patch, upstream of the failure (`depends_on`) |

Router features to weigh (initial rules, not scientific scales): impact on meaning or hard
compliance, uncertainty after reading treatments, coupling across passes, irreversibility, how
strong the validator is, budget. Ask the time pass's six questions in order (register, directorial
beats, tempo curve, micro-pauses and anticipation, apex density, variation). Use anchors: one
baseline and one relative escalation per quality, never two absolutes.

## 4·3 Clarifications from the first handoff run (run 002)

- **One pathway per contact cycle.** Stage kinds cannot repeat inside a pathway; a task with
  several contacts (open the box, take the case, open the case, insert the earbud) is several
  pathways on the same or different objects.
- **Hand ledger ids.** A `holding:<id>` state must name the pathway's `object` or one of its
  `parts` for the stages that use that hand.
- **Effect-read beats.** When a physics event already states the reaction, the "result is seen"
  moment may be folded into the action beat that carries the event; record the fold as a decision.
  Do not lower `min_s` to make a run fit.
- **OVERLOADED.** `check` lists the lowest-importance beats whose removal makes the clip fit.
  Taking a different resolution (folding, splitting, lengthening) is allowed with a decision record;
  an `alternative` item in `open.jsonl` with status `resolved` is the place to show what was weighed.
- **A beat that has a physics event** should describe the approach and setup only; the event
  sentence carries contact, reaction and settle. An anchor's description should not restate the
  beat. Otherwise the same action is written three times.
- **Anchor labels** must name the action unambiguously ("the thumb push on the case lid", not
  "the push"), because the comparison may land several sentences later.
- **Camera from the catalog.** Use field `camera.move` with the value keys `move` (catalog id),
  `phrase`, `movement`, `speed`, `framing`, `end`; these satisfy the camera-grammar check.
- **Sentence case.** Write beat descriptions as normal sentences. After "First," or "Then" the
  emitter lowercases common openers (She, He, The, A, …) and keeps names as written.
- **Budget block.** When `emit` blocks with only locked content left, it names the longest locked
  lines; shorten those in the IR (add `short` forms first), never unlock a constraint to fit.
- **Dates** in records use the session's local date.

## 5. Check, emit, read back

```
python3 director/tools/director.py check director/runs/<n>_<slug>
python3 director/tools/director.py emit  director/runs/<n>_<slug> --model seedance
```

`check` fails loudly with the rule that failed. Fix the IR, never the prompt. `emit` writes
`prompt.txt`, `receipt.json`, `loss.jsonl`, `emit_report.json`.

Cold read-back: a separate LLM call (a subagent, a second model, or a fresh session) is given only
`prompt.txt` and the five instructions in `runs/001_bottle_selfie/readback_raw.md`. Record the
exact input and the full response verbatim in `readback_raw.md`, and the comparison in
`readback.md`. A mismatch is repaired in the IR with the smallest change (repair mode), then
`check` and `emit` run again.

Treatment references on a control use the key `treatment` (the treatment's frontmatter `id`).
A control's `value` is a string, a list, or a dict whose keys are the placeholders the treatment's
wording expects; read the treatment's `## Wording` block to see which keys it needs.

## 6. After the owner renders

Write `verdict.md` (scores 1–5 per adherence dimension: identity, action, spatial, temporal,
performance quality, facial, connectivity, camera, continuity; failure signs) and one line in
`director/runs/ledger.jsonl`. Update `## Effects` in the treatments the run used.
