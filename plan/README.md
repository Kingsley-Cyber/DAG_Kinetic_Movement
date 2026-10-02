# CPCS Director — living plan

A text-only prompt compiler for AI video models, built on the owner's research in this repo.
An LLM session reasons over a user's ask in named director passes, writes a small IR, and code
validates it and emits the prompt with a receipt and a loss record.

Files in this folder:

| File | Holds |
|---|---|
| `README.md` | this page: principles, map, load path |
| `ARCHITECTURE.md` | control layer, reasoning layer, time and beats, knowledge format, dialects, mapping onto the research |
| `PHASES.md` | phases with exit tests, budgets, kill criteria |
| `STATUS.md` | dated log of what is done, next, blocked |
| `DECISIONS.md` | decisions, governance overrides, admission ledger, not-doing list, open questions, owner inputs |
| `legacy/` | previous AGENTS/CLAUDE instructions (not operative) |

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
6. Old plans enter only as knowledge or as validators of LLM-written output, with a named
   consumer (see the admission ledger).
7. Evidence before machinery. One ask end to end, rendered and judged, before breadth.

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
