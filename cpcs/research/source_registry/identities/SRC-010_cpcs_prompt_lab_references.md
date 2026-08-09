---
id: SRC-010
title: CPCS Prompt Lab (lab/) + References (references/)
version: 1.0
epistemic_class: authored
status: COMPLETE
lines: 44 files (~1,100 KB)
file: research/continue_detail/ai-video-movement-prompt-system - Copy/ai-video-movement-prompt-system - Copy/{lab,references}/
kind: empirical
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-010 — CPCS Prompt Lab + References

- **Location:** `lab/` (40 files: registry, blocks, concepts, runbooks, profiles, experiments, runs, schema, scripts, variants) + `references/` (4 files: combat choreography, FACS/Laban reference, iPhone raw-UGC realism, method details)
- **Date:** 2026-07-18 to 2026-07-20 (authoring session + two follow-up sessions)
- **Relationship:** The lab is the **only empirically validated component** of the CPCS ecosystem. The papers (SRC-009) define the theory; the lab records what actually happened when prompts were rendered on Veo-3.1 and LTX-2.3. Its epistemic class is PROVIDER_EXPERIMENT — render results, user verdicts, and pattern attributions, each with honest confidence.

## Source identity

The Prompt Lab is a tracking system for A/B testing prompt variations for AI video generation. Model: `levers → variants → runs (results.csv) → experiments (A/B) → patterns → recommendations`. `registry.yaml` is the single source of truth; `AGENTS.md` defines how an AI agent operates the lab (compose, recommend, log); `blocks.yaml` is the tested modular block library; `concepts.jsonl` is the semantic-retrieval concept corpus; 4 runbooks encode named workflows; 6 Python scripts implement the control plane (validation, sync, graph, pose extraction).

The references folder carries the domain reference cards: combat choreography math layer, FACS+Laban for talking-head UGC, field-tested iPhone raw-UGC realism preset, and method details (capture grammar, verification checklist, per-model notes).

## Source units

| Unit | Component | Lines | Distilled to |
| --- | --- | --- | --- |
| U01 | `lab/README.md` + `lab/AGENTS.md` | 202 | CREATE prompt_lab_architecture |
| U02 | `lab/registry.yaml` | 274 | CREATE prompt_lab_architecture, CREATE empirical_pattern_registry |
| U03 | `lab/blocks.yaml` | 180 | CREATE prompt_lab_architecture |
| U04 | `lab/CONTROL_SURFACE.md` | 94 | CREATE prompt_lab_architecture (2 paradigms, channel catalog, unexplored frontier) |
| U05 | `lab/FORMAT_CONTROL_MAP.md` | 79 | EXTEND format/representation cards |
| U06 | `lab/UNIVERSAL_MOTION_SKELETON.md` | 356 | EXTEND canonical_schema_design (14 layers × 3 formats) |
| U07 | `lab/CONCEPT_INDEX.md` | 302 | CREATE concept_kitchen (paper crosswalk, 3 papers → lab status) |
| U08 | `lab/concepts.jsonl` | 58 KB | CREATE concept_kitchen |
| U09 | `lab/profiles/` (8 profiles + README) | ~100 | CREATE concept_kitchen |
| U10 | `lab/experiments/` (e001-e003) | 3 files | CREATE lab_ab_test_protocol |
| U11 | `lab/runs/results.csv` | 7 rows | CREATE variant_lineage |
| U12 | `lab/schema/records.schema.json` | 1 file | CREATE lab_ab_test_protocol |
| U13 | `lab/scripts/validate_kinematics.py` | 19.7 KB | CREATE kinematic_validation_tooling |
| U14 | `lab/scripts/extract_pose_tier2.py` | 16.3 KB | CREATE kinematic_validation_tooling |
| U15 | `lab/scripts/validate_repo.py` + `sync_repo.py` + `build_graph.py` + `graph.py` + `concepts.py` | ~35 KB | CREATE concept_kitchen |
| U16 | `lab/variants/` (8 files incl. v001-v006, naruto) | ~115 KB | CREATE variant_lineage |
| U17 | `lab/RUNBOOK_pegasus_extraction.md` | 139 | CREATE lab_runbooks |
| U18 | `lab/RUNBOOK_reference_to_kinematic_truth.md` | 172 | CREATE lab_runbooks |
| U19 | `lab/RUNBOOK_cross_style_switching.md` | 101 | CREATE lab_runbooks |
| U20 | `lab/RUNBOOK_format_mixing_and_tinkering.md` | 114 | CREATE lab_runbooks |
| U21 | `references/combat_choreography.md` | 478 | CREATE combat_math_metrics_layer, EXTEND combat_action_coding |
| U22 | `references/facs_laban_reference.md` | 118 | CREATE ugc_realism_reference, EXTEND facs_au_catalog |
| U23 | `references/iphone_rawugc_realism.md` | 88 | CREATE ugc_realism_reference |
| U24 | `references/method_details.md` | 134 | CREATE ugc_realism_reference |

## Self-declared limitations

- All run scores are **qualitative, single-observer, single-session** (authoring session 2026-07-18) — not seed-controlled statistics.
- `confidence` on a pattern reflects **evidence, not conviction**; bundled evidence stays `low` until an isolated A/B confirms.
- Only e002 (skin microtexture vs smooth) is `isolated_confirmed`; e001 and e003 remain `hypothesis`.
- Profiles are `production_example`/`safety_scoped_example` — structurally sound but **not yet lab-render-validated**.
- The verification loop's post-render half (measuring an actual output) is open; only the pre-render half (kinematic self-consistency) is tooled.
- Pose Tier-2 output is 2D image-space `detected` evidence — never relabeled `measured`; camera motion not separated from subject motion.
- Sora 2 / Videos API are deprecated (shutdown Sept 2026); per-model notes may become outdated.

## Distilled object count

9 new cards + 6 EXTENDs + 1 gaps file + DIST-010 ledger + source identity registration.
