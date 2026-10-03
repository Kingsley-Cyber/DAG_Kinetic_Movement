# Decisions

## Decisions taken

| # | Date | Decision | Why | Reversible by |
|---|---|---|---|---|
| D1 | 2026-10-02 | Build in a fresh clone of `Kingsley-Cyber/DAG_Kinetic_Movement` at `/Users/king/cpcs-director`, branch `director` | It is the current router-and-relay architecture, its GitHub copy is newer than the local one, and it has no gate that fights new folders. The prompt-system repo's 18-step gate maps every tracked file | moving `director/` and `plan/` into another repo |
| D2 | 2026-10-02 | No DAG or graph executor; the LLM session reasons; code validates and emits | Owner principle; Claude Code is the reasoning graph at runtime | — |
| D3 | 2026-10-02 | Text-only: Mode C compiler, Mode A artifact, L0–L1 | Owner scope | adding a reference-image channel later |
| D4 | 2026-10-02 | Prompt wording lives in `director/treatments/`, not in card frontmatter | Cards carry one `epistemic_status`; owner wording is a different origin; wording draws on many cards | — |
| D5 | 2026-10-02 | All load-path files in one flat `director/` folder; `cpcs/runtime/**` untouched | Stage folders with "research-only" flags are a weak fence; cards there still specify a graph runtime | — |
| D6 | 2026-10-02 | Vertical slice before any migration; bulk migration is never a phase | Evidence before machinery | — |
| D7 | 2026-10-02 | Old `AGENTS.md`/`CLAUDE.md` kept in `plan/legacy/` rather than `cpcs/00_governance/legacy/` | A file without frontmatter under `cpcs/` would break the tree's own checker | — |
| D8 | 2026-10-02 | Origin tags use the tree's `epistemic_status` values | Already defined and enforced there; no second vocabulary | — |
| D9 | 2026-10-02 | Seedance profile starts all-unknown with a 1,000-character budget | Only figure in the research (Runway route, "not established") | owner states route and limits |
| D10 | 2026-10-02 | Light & Color is its own pass | Lighting had no owner among the 14 | — |
| D11 | 2026-10-02 | Model-agnostic semantic core with per-model dialects (owner) | Wording differs per model; order and IR do not | — |
| D12 | 2026-10-02 | Seedance prompt limit set to 2,000 chars from third-party API docs (seedanceapi.org, docs.laozhang.ai), tagged `documented_thirdparty`; Runway route stays 1,000 | Replaces the 1,000 guess with a sourced figure; still not ByteDance's own page | owner confirms route; a render measures |
| D13 | 2026-10-02 | Run 001 props the phone so both hands are free for a screw cap | Hand ledger: a selfie hand cannot also twist a cap; alternatives recorded in `runs/001_bottle_selfie/decisions.jsonl` d001 | a one-hand opening treatment |
| D14 | 2026-10-02 | Budget handling: compress to short wording first, then drop unlocked lines, then block with options; locked content never squeezed | Research compression order and fail-closed rule | — |

## Governance of the tree: honored and overridden

Honored: the epistemic firewall; the evidence two-axis model; the promotion ladder; no universal
carrier-superiority claim; REUSE > EXTEND > SUPPORT > SPECIALIZE > MERGE > CREATE; never invent
numeric precision; never silently merge conflicting presets; open questions are never closed by
assumption.

Overridden (for `director/` and `plan/` only):

| Rule | Where | Override |
|---|---|---|
| Implementation order "emit from existing reasoning runtime, keep six executors" | `cpcs/00_governance/policies/promotion_rules.md` | No executors; the LLM runs thinking modes |
| Automation doctrine passes 0–11 and hooks H1–H7 (need `pwsh`) | `control_plane_automation_doctrine.md` | Not run; `pwsh` is not installed and the doctrine assumes a DAG runtime |
| Mandatory frontmatter and closed `kind` list on every `cpcs/**/*.md` | `control_plane_reference.md` §5–6 | Applies to `cpcs/**` (unchanged); `director/` uses its own small frontmatter |
| `DIRECTORY.md` regeneration after any route change | `plan/legacy/AGENTS_2026-08.md` | Not applied to `director/` or `plan/` |
| Boot sequence for the distillation agent | `README.md`, `control_plane_reference.md` §12 | Replaced by the load path in `plan/README.md` |

## Admission ledger (old item → named consumer)

| Old item | Admitted as | Consumer |
|---|---|---|
| Capability classes, dispositions, loss record fields | vocabulary | `emit`, `check` |
| Bridge chain, DecisionRecord subset | record shape | `decisions.jsonl` |
| `epistemic_status` values | origin tags | every record |
| Temporal relations, master clock, `[start, end)` | IR time fields | `check` |
| HANDS causal chain and laws | pathway template | `check`, treatments |
| Timing profiles, phase presets (as conventions) | treatments and `calc` | time pass |
| Clause order and compression order (`format_ownership`) | emitter defaults | `emit` |
| Kitchen trigger phrases and blocks (prompt-system repo) | read on demand | treatments |
| Experiment-branch hand-resource, beat-budget and narrative-beat modules | rules only, no code | `check` design |
| `dmr_runtime_starter/compiler.py` (research package) | reference reading only | `emit` design |

## Not doing

DAG or graph executor · bulk card migration · implementing the cards' 316 test names ·
`interfaces` resolution checks · pose, depth, mocap, reference-image conditioning · video harvest
(TwelveLabs, pose measurement) · structured carriers before the prose slice has evidence ·
changes to `/Users/king/ai-video-movement-prompt-system` or `/Users/king/Documents/New project`
· pushing without the owner's word · `index.json` before about 30 treatments.

## Open questions (defaults in place)

1. Seedance route (Runway-hosted, native, other) and its real prompt limit. Default: 1,000
   characters, all capabilities unknown.
2. Fate of the uncommitted Aug 8 work in `New project` (`lab/dag/`, 22 files). Default: untouched.
3. Whether `director/` later moves into the prompt-system repo. Default: stays here.
4. Agent-run (the LLM session drives; current default) versus a Python orchestrator loop (code
   calls the LLM per pass, validates and retries, logs each pass, sets temperature per pass type).
   Shared pieces (`pack`, per-pass `check`, pass log) serve both. Owner to choose.
5. What "Laban has three layers" names: the movement control stack or the wording rungs.

## Owner inputs log

| Date | Input | Where it landed |
|---|---|---|
| 2026-10-02 | Router and relay, not DAG; Claude Code is the reasoner | Principles, D2 |
| 2026-10-02 | 14 director passes + synthesis; sub-modules activate on demand; World as a pass | ARCHITECTURE §2.1 |
| 2026-10-02 | Light and color | D10 |
| 2026-10-02 | Camera sub-layers (movement, optics) | ARCHITECTURE §3.4 (plus the research's third layer) |
| 2026-10-02 | Laban: Weight factor, strength numbers, importance weights | ARCHITECTURE §3.5 |
| 2026-10-02 | Three tiers Reason / Style / Render; order first, texture second; action integrity graph; pose-to-pose | ARCHITECTURE §1, §2.5, §7 |
| 2026-10-02 | Text-only; calculations from research papers | D3, ARCHITECTURE §9 |
| 2026-10-02 | Timing algorithm: master clock, rhythm fields, profiles, punch formula, emotional formula, fight granularity, six questions | ARCHITECTURE §4 |
| 2026-10-02 | Sakuga approach: silhouette first, motion grammar not anatomy, short motion-focused clips | ARCHITECTURE §7 |
| 2026-10-02 | Model-agnostic semantic core + dialects (Hailuo, Seedance, Kling, Gemini/Veo, Wan) | D11, ARCHITECTURE §6 |
| 2026-10-02 | Laban AI references (LaMoGen, Guo 2022, LMA emotion); Bartenieff sources | ARCHITECTURE §12 |
| 2026-10-02 | Seedance first | D9 |
| 2026-10-02 | Movement control layer: world bundle → Laban Effort (scaled) × Shape (3 planes) × Bartenieff (6 patterns) → constraint resolution → strength-scaled emission; four anti-arcade signatures as detectors; priority order | ARCHITECTURE §3.5.1; phases 3–5 |
| 2026-10-02 | Relative prompting: one anchor, one escalating unit at a time, never two absolutes | ARCHITECTURE §3.5.2; emitter rule |
| 2026-10-03 | Relative prompting promoted to a compile invariant with anchors in the IR; explicit-versus-open contract per pass; passes connect through `reads` and coupling checks; creative gaps authored by the LLM and labelled | GOALS principle 6; ARCHITECTURE §2.7, §2.8, §3.5.3; protocol §4·0; CONTROL_LAYER R-16, R-56, R-57; TASKS T16, T17 |
| 2026-10-03 | Owner's eight content layers mapped onto the passes (§2.1a); camera expanded to 12 sub-layers in five groups + stance, shot function, locked-off control; world bundle gains friction, drag, scale, atmosphere; dialect-file fields (defaults_to_counter, access_path, version, date_tested) added to profiles; evidence status recorded: nothing verified on a video model yet | ARCHITECTURE §2.1a, §3.4, §6; passes.yaml; profiles; R-54, R-55; T39 |
| 2026-10-03 | Camera move catalog (48 moves) as `director/vocab/camera_moves.yaml`, wording UNVERIFIED from aicameramovements.com, function hints PROJECT_DERIVED; camera pass picks by function and states the four-part grammar; zoom is optics, never motion | ARCHITECTURE §3.4; protocol §4a; CONTROL_LAYER R-53; TASKS T38 |
| 2026-10-03 | Research ingest is the engine, not the last phase: `INGEST.md` written now from the DMR prompt's own output contract; first ingest = the DMR package (T36); IR-not-authority invariant, typed validator outcomes, provider lifecycle adopted (R-50…R-52) | INGEST.md; TASKS T36, T37, T70; CONTROL_LAYER |
| 2026-10-02 | Agnostic core first; dialects as lenses with an intent catalog and per-model levers carrying evidence; Hailuo emphasis levers recorded as owner_observed; reasoning control layer written into the protocol (modes, router features, dialect lens) | ARCHITECTURE §6.1; protocol §4b–4c; CONTROL_LAYER R-47…R-49; TASKS T53; `profiles/hailuo.yaml` |
| 2026-10-02 | Specialized physics layer: causal event schema, contact_state, risk-tagged capability check with degradation, eval log (3 yes/no, ≥3 seeds), failures registry, hypotheses flagged | ARCHITECTURE §3.5.7; CONTROL_LAYER R-41…R-46; TASKS T35 |
| 2026-10-02 | Detail requested for Bartenieff six patterns, Shape planes, FACS, valence–arousal | ARCHITECTURE §3.5.4–3.5.6; CONTROL_LAYER R-37…R-40; TASKS T28, T29 |
| 2026-10-02 | FACS as a spatiotemporal event (AUs, laterality, A–E intensity, onset/apex/offset, co-occurrence, head pose, gaze, visibility); Laban = 4 Effort controls within BESS | ARCHITECTURE §3.5.2; CONTROL_LAYER R-34…R-36; TASKS T27 |
| 2026-10-02 | Three layers of movement text control: Laban (quality), Bartenieff (origination), film grammar (camera); independent dials per layer; Laban as scaled Bayesian output, never absolute terms; impact-and-physics language sub-layer with explicit stated reactions; camera grammar mandatory | ARCHITECTURE §3.5, §2.1, §9; `passes.yaml` |
