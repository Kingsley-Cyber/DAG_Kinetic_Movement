# AGENTS.md — CPCS Director (branch `director`)

This repository is the owner's AI-video prompting research (`cpcs/`, `Additional/`,
`Research_distillation_folder/`) plus a text-only prompt compiler (`director/`) and its living
plan (`plan/`). Read `plan/README.md` first (one page), then this file.

## Roles

- **You (the LLM session) reason.** You read the ask, decide which passes run, read the
  treatments for those passes, and write the IR (`ir.json`) and decision records.
- **Code validates and emits.** `director/tools/director.py check` validates what you wrote;
  `emit` writes the prompt deterministically with a receipt and a loss record.
- **A separate call verifies.** The cold read-back is done by a different LLM call that sees only
  the prompt. You never declare your own output valid.

## Load path for an ask

1. `plan/README.md` → `director/protocol.md` → `director/passes.yaml`
2. Treatments for the active passes only: `director/treatments/<pass>/*.md`
3. Cite `cpcs/**` cards and `Additional/*.md` manuals by path when a treatment points to them.
   Do not read the whole tree.
4. Write `director/runs/<n>_<slug>/{ask.md, ir.json, decisions.jsonl}`
5. `python3 director/tools/director.py check <run>` then `emit <run> --model <profile>`
6. Cold read-back → `verdict.md` after the owner renders.

## Rules

- No DAG or graph executor. The repo is material; you are the reasoner.
- Text only: Mode C compiler, Mode A artifact, control levels L0–L1. No pose, depth, mocap or
  reference-image conditioning.
- Order first, texture second. Reason-tier beats and action stages are never reordered or
  removed by Style or Render decisions.
- Every decision carries an origin from `epistemic_status` (SOURCE_EVIDENCE, INFERENCE,
  CREATIVE_CHOICE, PROJECT_DERIVED, PROVIDER_EXPERIMENT, UNVERIFIED, UNKNOWN). Reasoned
  decisions are logged to `director/gaps.jsonl`.
- Never invent numeric precision. A number inherits the origin of its inputs; conventions are
  labelled conventions.
- One owner pass per IR field. Other passes request; the owner writes.
- `cpcs/**` and `Additional/**` are read-only on this branch. Knowledge enters through the
  ingest procedure in `plan/INGEST.md`, which runs alongside every phase.
- Commits are local, on this branch, at phase exits. Nothing is pushed without the owner saying
  so. No changes to `/Users/king/ai-video-movement-prompt-system` or
  `/Users/king/Documents/New project`.
- `plan/legacy/` holds the previous AGENTS/CLAUDE instructions. They describe a DAG runtime and
  an automation doctrine and are **not operative**. `cpcs/00_governance/policies/` is honored
  except where `plan/DECISIONS.md` records an override.
