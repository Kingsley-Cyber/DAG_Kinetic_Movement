# CPCS Director — plan folder (the handoff pack)

A text-only prompt compiler for AI video models, built on the owner's research in this repo. An
LLM session reasons over a user's ask in named director passes, writes a small IR, and code
validates it and emits the prompt with a receipt and a loss record.

This folder is the complete plan an implementing model (Sonnet-class) works from. Read in this
order:

| Order | File | Holds |
|---|---|---|
| 1 | `GOALS.md` | goal and intent, success criteria, non-goals, principles, decision rights, quality bar |
| 2 | `STATUS.md` | dated log: done, next, blocked |
| 3 | `TASKS.md` | ordered tasks with files, acceptance tests, dependencies, status |
| 4 | `HANDOFF.md` | boot sequence, working loop, conventions, what exists on disk |
| 5 | `ARCHITECTURE.md` | the design in depth: pipeline, reasoning layer, control layer, time and beats, movement control layer, knowledge format, dialects, steering, mapping onto the research |
| 6 | `CONTROL_LAYER.md` | the control layer as checkable requirements R-01…R-33 with status |
| 7 | `OWNER_INPUTS.md` | the owner's intents from the planning conversation, in full |
| 8 | `PHASES.md` | phases, exit tests, budgets, kill criteria, render-evidence procedure |
| 9 | `DECISIONS.md` | decisions, governance overrides, admission ledger, not-doing list, open questions |
| — | `legacy/` | previous AGENTS/CLAUDE instructions (not operative) |

Reference implementation of phases 0–1: `director/` (see `HANDOFF.md → What exists on disk`).

## Principles

1. The repo is rationalized material. The LLM session reasons. Code validates what the LLM wrote
   and emits deterministically. No DAG executor.
2. Text only: Mode C compiler emitting a Mode A artifact (`text_interpretation_only`), control
   levels L0–L1.
3. Reasoning thinks and decides; the control layer emits and validates. Planner, verifier and
   repairer are separate.
4. Order first, texture second. Reason-tier beats and action stages are fixed before Style and
   Render add weights and texture.
5. No invented precision. Numbers inherit the origin of their inputs.
6. Everything scaled, nothing absolute; one anchor, one relative escalation.
7. Camera grammar is mandatory; every contact has a stated reaction.
8. Old plans enter only as knowledge or as validators of LLM-written output, with a named
   consumer (admission ledger).
9. Evidence before machinery. One ask end to end, rendered and judged, before breadth.

## Map

```
ASK
 → intent brief                           LLM
 → pass plan   (director/passes.yaml)     LLM switches passes on/off
 → REASON tier  beats · action pathways · hands · state · cause → synthesis (logic)
 → STYLE tier   per-beat priorities · performance · camera · light/color → synthesis (taste)
 → RENDER tier  capture texture · continuity locks · audio
 → ir.json                                written by the LLM
 → check → emit                           code: prompt.txt + loss.jsonl + receipt
 → cold read-back                          separate LLM call
 → owner renders → verdict.md             evidence
```

Folders: `director/` (everything on the load path), `cpcs/` and `Additional/` (citable
knowledge, read-only), `plan/` (this).

## Load path for one ask

1. `plan/README.md` (this page) → `director/protocol.md` → `director/passes.yaml`
2. Treatments for the active passes: `director/treatments/<pass>/*.md`
3. Cards and manuals only where a treatment points: `cpcs/...`, `Additional/...`
4. Write the run: `director/runs/<n>_<slug>/{ask.md, ir.json, decisions.jsonl}`
5. `python3 director/tools/director.py check director/runs/<n>_<slug>`
6. `python3 director/tools/director.py emit director/runs/<n>_<slug> --model seedance`
7. Cold read-back by a separate LLM call → compare beat order and state changes
8. Owner renders; verdict logged in `verdict.md`

Budget: an ordinary ask reads this page, the protocol, the passes file and one treatment set per
active pass. Nothing else.
