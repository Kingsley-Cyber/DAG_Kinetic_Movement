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
active when their `when` condition holds for this ask. Keep inactive passes inactive.

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

**Laban** (performance pass): never a bare pole word. Each factor is a scaled position with a
confidence: `{"weight": 0.3, "time": 0.4, "space": 0.7, "flow": 0.6, "confidence": 0.5}` where 0 is
the first pole (light, sustained, indirect, free) and 1 the second (strong, sudden, direct,
bound). The emitter turns scales into wording.

## 5. Check, emit, read back

```
python3 director/tools/director.py check director/runs/<n>_<slug>
python3 director/tools/director.py emit  director/runs/<n>_<slug> --model seedance
```

`check` fails loudly with the rule that failed. Fix the IR, never the prompt. `emit` writes
`prompt.txt`, `receipt.json`, `loss.jsonl`, `emit_report.json`.

Cold read-back: a separate LLM call is given only `prompt.txt` and asked to list, in order, the
beats it sees and every state change. Compare with the IR. A mismatch is repaired in the IR with
the smallest change (repair mode), then `check` and `emit` run again.

## 6. After the owner renders

Write `verdict.md` (scores 1–5 per adherence dimension: identity, action, spatial, temporal,
performance quality, facial, connectivity, camera, continuity; failure signs) and one line in
`director/runs/ledger.jsonl`. Update `## Effects` in the treatments the run used.
