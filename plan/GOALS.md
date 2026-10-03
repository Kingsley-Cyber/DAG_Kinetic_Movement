# Goals and intent (the control layer for whoever implements this)

Read this before any other file in `plan/`. It says what the owner wants, how to tell when it is
achieved, what is out of scope, and which decisions the implementer may take alone.

## The goal, in the owner's terms

The owner does deep research on how to prompt AI video models so they stop producing weak,
generic output. The repo must **cannibalize that research** into reusable nuances and know **how a
user's plain language maps to the deep knowledge**, so that any LLM can turn an ask into a proper
prompt. It must reason about motion, movement, hands and the logical sequence of a physical
action, compile that into a prompt (natural language or structured), and do it with taste and
diversity rather than one formula.

## Success looks like

1. A plain ask ("a woman films herself opening a water bottle and drinking, 8 seconds, phone
   selfie") goes through named director passes to an IR, a validator, and a deterministic emitter,
   and comes out as a prompt whose every sentence traces to research (a treatment) or is marked
   as reasoned.
2. The validator refuses the impossible: a hand that is holding the phone does not also twist a
   cap; a bottle is not suddenly open; seven seconds of content are not crammed into three.
3. A cold read-back by a second LLM lists the same beats in the same order.
4. On renders, compiled prompts beat plain prompts on most asks (owner-judged, per adherence
   dimension). If they do not, the project stops and rethinks (kill criterion).
5. New research becomes new treatments, sub-modules or passes without code changes.
6. The same semantic core emits different wording per model (dialects), and variation is seeded,
   labelled, and never touches what the user locked.

## Non-goals (do not build)

- A DAG or graph executor, a runtime reasoning engine, or a second knowledge graph. The LLM
  session reasons; the repo is material plus validators plus an emitter.
- Pose, depth, mocap, reference-image or video conditioning. Text only, control levels L0–L1.
- Bulk migration of the 132 kitchen cards or the 220 tree cards. Treatments are created when an
  ask needs them.
- Implementing the test names cited inside the tree's cards; resolving the tree's `interfaces`.
- Video harvest (TwelveLabs, pose measurement).
- Changes to `/Users/king/ai-video-movement-prompt-system` or `/Users/king/Documents/New project`.
- Pushing to GitHub. Commits are local on branch `director` until the owner says push.

## Principles (owner-agreed; violating one is a defect)

1. Repo = rationalized material; LLM = reasoner; code = validate and emit.
2. Mode C compiler, Mode A artifact (`text_interpretation_only`), L0–L1.
3. Planner, verifier, repairer are separate. No self-validation.
4. Order first, texture second. Reason-tier beats and action stages are never reordered by
   Style or Render.
5. No invented precision. Every number inherits the origin of its inputs; conventions are
   labelled conventions.
6. Everything scaled, nothing absolute: Laban and other qualities are positions on a scale with a
   confidence; prompts use one anchor and one relative escalation, never two absolutes.
7. Camera grammar is mandatory on every prompt. Every contact has a stated reaction.
8. Old plans and old code enter only as knowledge or as a validator of LLM output, with a named
   consumer (admission ledger in `DECISIONS.md`).
9. Evidence before machinery. Each phase adds treatments or render evidence, not only code.

## Decision rights

The implementer (a Sonnet-class session) may decide alone:

- Code structure inside `director/tools/`, test layout, helper naming.
- Wording of treatments when a `from:` source is cited and the origin is tagged honestly.
- Adding a validator when a real run shows the failure it catches.

The implementer must record in `DECISIONS.md` and may proceed:

- Any new field in `ir.schema.json` (must name the check or emitter step that reads it).
- Any new pass or sub-module in `passes.yaml`.
- Any change to the budget or compression rules.

The implementer must stop and ask the owner:

- Anything that would push to GitHub, touch the other checkouts, or delete research.
- Adopting code from the old systems beyond the admission ledger.
- Changing a principle above, or the model list, or spending money (renders, APIs).
- Treating a convention or a third-party doc as fact.

## Quality bar

- Python 3.9, stdlib + pyyaml + jsonschema. `python3 -m unittest discover -s director/tools/tests`
  green before every commit. New rule → RED test first, then GREEN.
- Every emitted sentence traceable (receipt). Every dropped or weakened control recorded (loss).
- `plan/STATUS.md` updated at the end of every session; `plan/DECISIONS.md` for every decision.
- Load path per ask stays: `plan/README.md`, `director/protocol.md`, `director/passes.yaml`, one
  treatment set per active pass.
