# Research ingest — how a coding model turns a deep-research return into compiler rules

This is the engine of the project. The owner produces deep-research returns (example: the DMR
Gap Closure prompt and its packages under
`Research_distillation_folder/research/continue_detail/director_motion_reasoning_complete_package/`).
The implementing model must turn each return into treatments, validators, schema fields, profile
facts and runs, without inventing a competing authority and without importing machinery that has
no consumer. Knowledge stays thin exactly as long as this procedure is not run.

## 0a. Every return lands on the layer tree (owner rule)

A research return must **add, change or edit the current layers of prompt composition**
(`director/passes.yaml`: passes and their sub-modules). Each accepted claim ends as exactly one
of: a new sub-module or pass (add), a changed rule, owner, activation or validator on an existing
layer (change), or new or revised treatments and vocab for an existing layer (edit). A claim that
touches no layer is parked, however interesting. The camera move catalog is an example of
"edit" (the `motion_layer` sub-module gained a vocabulary); the physics causal-event schema was
"add" (the `causal_events` sub-module); FACS as an event was "change" (the `face_facs` sub-module
became `facs_events` with a record and validators).

## 0. The rule that governs everything

A definition or schema **without a decision path is not implementable** and is parked. Every
claim that enters the compiler must be traceable along the owner's chain:

```
scene condition → evidence or authored intent → Director decision → IR field
→ validator or calculator → capability decision (per model) → emitted control
→ observed result (render verdict) → accept, repair, degrade, or fail closed
```

Each step is labelled: deterministic (code), constraint-solved (calc), model-mediated (the LLM
following the protocol), human-authored (owner), observed, measured, or experimental.

## 1. What a research return must contain (the return contract)

Ask deep research for these sections; a return missing them gets a triage pass first.

| Section | Holds | Becomes |
|---|---|---|
| claim register | each claim with id, source, evidence class (package-derived, external primary source, proposed representation, experimental hypothesis) and a status: closed · implementable_now · requires_experiment · unknown · deferred · rejected | `DECISIONS.md` admission rows; `gaps.jsonl` for unknown/experimental |
| decision table | condition · consulted object · rule · output · failure path · owner | validators (R-ids), protocol lines, treatment `not_when` |
| field ownership matrix | every proposed field: owner, smallest executable consumer, origin/value status | `ir.schema.json` additions (only with a consumer), `passes.yaml → owns` |
| wording candidates | prompt phrasings per claim, what the camera sees, per model where known | treatments (`core`, `core short`, `dialect=`) |
| typed validator specs | inputs, algorithm, tolerance source, outcome ∈ pass · fail · indeterminate · not_applicable · unobservable, repair scope, what blocks vs warns | `check` rules with RED→GREEN tests |
| provider evidence | documented capability, observed behavior, adapter support, unverified assumption; evidence date; expiry and reprobe condition | `profiles/<model>.yaml` facts and levers |
| fixture trace | one stable scene traced end to end through the chain above | a run folder (`director/runs/`) |
| acceptance and falsification | observable tests and the result that rejects the claim | `TASKS.md` acceptance column; `ledger.jsonl` fields |
| deferred scope | what is excluded and the evidence needed to add it | `DECISIONS.md → Not doing` or `deferred` rows |

## 2. The ingest procedure (one return, one session)

1. **Locate and freeze.** Note the return's path and hash in `STATUS.md`. Never edit the return.
2. **Triage every claim** into the six statuses. Text-only scope applies: anything needing pose,
   depth, mocap, 3D measurement or reference media is `deferred` with the evidence it would need.
3. **Admission check** (`GOALS.md → Principles 8`): knowledge or validator of LLM output; adds
   nothing to the load path; no tie to old gate, second brain or frozen runtime; named consumer.
4. **For each `implementable_now` claim, pick the artifact type:**

   | If the claim is… | Make… | Proof |
   |---|---|---|
   | a way to word something the model reads | treatment with ≥ 3 triggers, `not_when`, `backs`, `from`, origin | a run uses it; `## Effects` line unverified until rendered |
   | a rule about what the LLM wrote | `check` rule with an R-id, typed outcome, repair scope | RED test from a real or constructed IR, then GREEN |
   | a formula or scale | `calc` function; output carries input origins; conventions labelled | unit test with the source value |
   | a fact about a model or route | profile fact with tag and date; or a lever with evidence | profile parses; lifecycle state set |
   | a new reasoning concern | sub-module (or pass) in `passes.yaml` with question, `owns`, activation | an ask activates it; a treatment serves it |
   | a new IR field | schema addition | the check or emitter that reads it, in the same commit |

5. **Fixture run.** Trace the return's fixture (or the nearest golden ask) as a run: `ask.md`,
   `ir.json`, `decisions.jsonl`, `check`, `emit`, cold read-back. The run is the proof that the
   rules compose; if the fixture cannot be traced, the claims go back to `requires_experiment`.
6. **Record.** `TASKS.md` (new tasks or closures), `DECISIONS.md` (admissions, overrides,
   deferrals), `gaps.jsonl` (unknowns), `STATUS.md` (what the return changed), `CONTROL_LAYER.md`
   (new R-ids). Commit locally with the return's id in the message.
7. **Refactor, not accrete.** If a claim supersedes an existing rule, change the rule and its test;
   do not add a parallel one. If two sources disagree (e.g. the two phase-preset tables), record
   the delta as a decision, never merge silently.

## 3. Provider lifecycle (from the DMR return; adopted)

Every profile fact and lever carries a state: `unverified → verified → stale → reprobe_due →
invalidated`, with dates. Compilation may proceed on `unverified` (flagged in the report) and
`verified`; `stale` warns; `reprobe_due` and `invalidated` block native dispositions for that fact.
Changed behavior is quarantined as a new dated fact; history is never rewritten.

## 4. What the DMR return gives this plan (first ingest, task T36)

| DMR gap | Status for a text-only compiler | Lands as |
|---|---|---|
| G001 ScenePlan authority | implementable_now, reduced: the IR is the execution projection; `cpcs/**` cards are semantic authority; the owner's inputs are authored intent | authority note in `ARCHITECTURE.md` §3; invariant "the IR never becomes a second semantic authority" (R-50) |
| G002 temporal solver | requires_experiment for solvers; implementable_now for arithmetic (fit, order, no false precision, uncertain duration stays UNDERSPECIFIED) | already R-13; add `pause_s`/latency fields only when a run needs them |
| G003/G004 action and persistent state | implementable_now: state variables catalogue (position, orientation, stance, gaze, held object, injury, wetness, fatigue display, wardrobe, lighting, ownership, damage, residue) as continuity locks and pathway states | treatments for continuity and world; `STATE(t) + EVENT → STATE(t+1)` as pathway stages (already) |
| G005 contact graph | implementable_now: lifecycle approach · near_contact · contact · impact · support · grasp · release · separation · reaction with visibility and occlusion | aligns with pathways and `contact_state`; extend stage kinds if a run needs `support`/`separation` |
| G006 feasibility validator | implementable_now with typed outcomes; 2D-only claims return `unobservable` | adopt the five outcomes for all validators (R-51) |
| G007/G008 provider contracts | implementable_now | profile facts with lifecycle (§3 above) |
| G009 compilation-loss | closed (R-03, R-19…R-21 already follow it) | — |
| G011–G013 measurement and evaluator | deferred (needs pose/3D); human or VLM yes/no scoring stays | eval log fields (R-45) |
| G014/G015 failure and repair | implementable_now: symptom → evidence → responsible layer → confidence → smallest patch → protected invariants → re-check | `failures.jsonl` (R-46) and repair mode in the protocol |
| G016/G017 benchmark harness | requires_experiment; v1 = golden asks + ledger with seeds and repeats | T13, T34 |
| G019 format doctrine | requires_experiment | T60 |
| G020 FACS/Laban calibration | implementable_now as rules: ordinal stays ordinal, no averaging, no cross-framework mapping without evidence | R-35, §3.5.5 |
| G021 provider lifecycle | implementable_now | §3 above |
| Shared fixture (Actor A strikes a glass; shards persist; B reacts after a latency; camera reframes; one unsupported control) | the next golden ask | run 004 in T12 |

## 5. Asking for research the compiler can eat

When the owner commissions a deep-research pass, the prompt should name the gap ids from
`director/gaps.jsonl`, require the return contract in §1, require the chain in §0 for every claim,
forbid redesigning the compiler, and require the shared fixture to be traced. The DMR prompt is
the model for this; `director.py gaps --prompts` (T71) will draft these prompts from the gap log.
