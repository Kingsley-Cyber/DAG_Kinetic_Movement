# Phases

Each phase ends with a test that must pass before the next begins. Every phase must add
treatments or evidence, not only code.

| # | Phase | Exit test | Status |
|---|---|---|---|
| 0 | Set up: back up the 7 local manuals and 8 extra Downloads files; clone `Kingsley-Cyber/DAG_Kinetic_Movement`; branch `director`; replace `AGENTS.md`/`CLAUDE.md`; write `plan/`; build graft and graphify graphs in a throwaway worktree | Clone clean apart from the new files; `plan/` present; the prompt-system repo and `New project` untouched | done 2026-10-02 |
| 1 | **Vertical slice, Reason tier.** Ask: "a woman films herself opening a water bottle and drinking, 8 seconds, phone selfie". `passes.yaml` (intent, entity, interaction, time, camera, synthesis active), `protocol.md`, `ir.schema.json`, `profiles/seedance.yaml`, about 5 treatments, `director.py check` + `emit`, run folder `runs/001_bottle_selfie` | Tests RED → GREEN: two-hand twist while a hand holds the phone fails; a beat that jumps straight to "open" fails; overloaded beats fail; every control has one disposition. `emit` gives prose within the budget with a complete receipt. Cold read-back lists the same beats in the same order | done 2026-10-02 (20 tests green; read-back MATCH) |
| 2 | **Evidence.** Five asks, each as a plain baseline prompt, a compiled prompt and a lean compiled variant (beats + camera + capture). Owner renders on Seedance and logs verdicts per adherence dimension | Compiled beats baseline on most asks; otherwise stop and rethink (kill criterion) | waiting on owner renders of run 001 |
| 3 | Style and Render tiers: per-beat weights, sakuga and UGC texture treatments, timing profiles, the "order first, texture second" check | Sakuga beats rendered with UGC texture keep beat order and locks under `check` | pending |
| 4 | Widen on demand: world reactions (pool example), camera three layers, light_color, attention; `index` once past about 30 treatments; trigger-matching test set vs the kitchen baseline | Each new treatment was needed by a real ask; hit rate recorded | pending |
| 5 | Validators and calculators that real runs needed | Each has a failing case from a real run | pending |
| 6 | Steering, diversity, beat patterns, model dialects | Same seed → same prompt; locked content never varies; a dialect block changes only wording, never order | pending |
| 7 | Structured and hybrid carriers as an experiment against prose on the same IR | Promoted only if renders show a gain | pending |
| 8 | Research ingest procedure, written after doing it by hand; gap log → research prompts | A new sub-module and a new pass added with no code edit | pending |
| 9 | More model profiles (Kling, Hailuo, Veo, Wan); evidence loop | Verdicts update treatment effects per model | pending |

## Budgets

- Slice tool: under about 600 lines of Python; stdlib + pyyaml + jsonschema; Python 3.9.
- Load path per ordinary ask: `plan/README.md`, `director/protocol.md`, `director/passes.yaml`,
  one treatment set per active pass. Nothing else.
- `director/` holds every load-path file. `cpcs/**` and `Additional/**` are read-only.
- No bulk migration of cards, ever.

## Kill criteria

- Phase 2: compiled prompts do not beat plain baselines on most asks → stop, write up, rethink.
- Any phase: a validator or calculator with no failing case from a real run is removed.
- Any phase: a file added to the load path without a named consumer is removed.

## Render evidence procedure

1. For each ask, `prompt.txt` (compiled) and `baseline.txt` (plain) are rendered on the same
   model with the same settings; seeds recorded if the model exposes them.
2. The owner scores each render per adherence dimension (identity, action, spatial, temporal,
   performance quality, facial, connectivity, camera, continuity) 1–5 and notes failure signs.
3. Verdicts go in `director/runs/<n>_<slug>/verdict.md` and one line in
   `director/runs/ledger.jsonl` (`run, model, prompt_hash, seed, scores, verdict, notes`).
4. Treatment `## Effects` lines are updated from the ledger, per model.
