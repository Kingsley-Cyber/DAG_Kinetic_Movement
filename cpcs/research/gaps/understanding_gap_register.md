---
id: cpcs.gaps.understanding_register
kind: gap_register
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008, SRC-009, SRC-010, SRC-011, SRC-012]
primary_route: cpcs/research/gaps/
interfaces:
  - cpcs.gov.working_agent_log
  - cpcs.gaps.outstanding_actions
---

# Understanding Gap Register

> **BOOT-ADJACENT.** The agent's "student gaps": concepts the tree has
> ingested but the agent cannot yet confidently state, justify, produce,
> select, apply, or blend. Captured automatically while working (doctrine D8).
> The user performs deep research on them and returns it for ingestion (D9) —
> the register is the research-alignment surface for that loop.

## 1. Gap taxonomy (the six student questions)

| Type | The student question | Example symptom while working |
| --- | --- | --- |
| WHAT | What is this concept, exactly? | Two cards use the term with different scope; definitional boundary unclear |
| WHY | Why does this principle hold? | Only the rule is recorded; rationale/provenance missing |
| HOW | How do I produce or use this object? | No operational path from intent to artifact |
| WHEN | When do I select this over that? | Competing concepts overlap; selection rule absent |
| APPLY | How do I apply it to a live query? | Query demands the concept but application fails or is hand-waved |
| BLEND | How does it integrate with the ecosystem? | Cross-concept edges undefined; DAG relationship missing |

## 2. Capture rules (D8)

Record automatically while working when any of the six student questions
cannot be answered from the tree with confidence. Entry fields: id (UG-NNN),
type, gap (the student question), concepts, parent (nesting), status.
Never close by assumption (D6). Never record process friction (tooling
annoyances, time pressure, file churn) as a gap — only genuine understanding
gaps. Capture is continuous; the register is reviewed each batch (H7).

## 3. Live register (nested)

Status flow: `OPEN → RESEARCHING → RETURNED → CLOSED (with evidence)` or
`REFINED` (re-scoped; children re-targeted). Closing a child refines its
parent; closing a parent promotes its remaining children to parent level.

| ID | Type | Gap (student question) | Concepts | Parent | Status |
| --- | --- | --- | --- | --- | --- |
| UG-001 | WHEN | Which canonical object answers a timing query: rhythm_metrics_contract, phase_timing_presets, beat_syncpoint_alignment, or temporal_coupling? | rhythm_metrics_contract, phase_timing_presets, beat_syncpoint_alignment, temporal_coupling | — | OPEN |
| UG-002 | BLEND | How do KB rhythm presets (production profiles) and phase presets (normalized execution) reconcile at compile time — is the 3-split setup_strike_recovery a scene field or authoring convenience? | rhythm_metrics_contract, phase_timing_presets, canonical_schema_design | UG-001 | OPEN |
| UG-003 | WHEN | When analyzing a query, which phase granularity applies: KB 7-phase (contact as event), SRC-010 4-phase (contact as bin), or tree 10-step engineering grammar? | evidence_vs_engineering_phases, combat_math_metrics_layer | UG-001 | OPEN |
| UG-004 | BLEND | Do the package evidence-class vocabularies (KB 5, SRC-005 7, SRC-009 VOG 5, SRC-011 6) map onto evidence_two_axis_model, and which label wins when they disagree? | evidence_two_axis_model, promotion_rules | — | OPEN |
| UG-005 | WHY | Why is seconds the authoritative master-clock base while frame/musical references derive — what breaks if a source binds to frames? | temporal_coupling, timebase_systems | — | OPEN |
| UG-006 | APPLY | How do I apply BML sync points to camera impact binding (phase_locks_to → binds chain) when the provider surface lacks phase controls? | beat_syncpoint_alignment, camera_impact_sync, provider_capability_snapshots | UG-001 | OPEN |
| UG-007 | WHAT | What exactly distinguishes sequencing_delay_ms (single 55 ms CPCS_CONVENTION sample) from per-pattern lag calibration — is 55 ms transferable across actors? | bartenieff_six_patterns, phase_timing_presets | — | OPEN |

### Cross-links to source questions

Several seeds track source-level open questions — research that closes the
source question feeds the gap, and vice versa:

| UG | Source question |
| --- | --- |
| UG-002 | SRC-012 Q3 (rhythm object as canonical scene field vs authoring convenience) |
| UG-003 | SRC-012 Q8 (KB 5 phase presets vs SRC-010 4-phase strike ratios) |
| UG-004 | SRC-012 Q4 (evidence-class vocabulary adoption) |
| UG-006 | SRC-012 Q5 (provider surfaces carrying timing/phase/contact controls) |
| UG-007 | SRC-012 Q7 (sequencing_delay_ms calibration per actor/technique) |

## 4. Research alignment (D9 — return and ingestion)

1. The user returns deep research for any UG id — in chat or as files dropped
   in `Research_return_folder/`.
2. The agent matches the return to the nesting node, ingests it like a source
   (REUSE/EXTEND/SUPPORT/CREATE per D2, evidence class from return strength).
3. Status update: `RESEARCHING` when taken on, `RETURNED` once ingested,
   `CLOSED` with evidence link + closure note, or `REFINED` with re-scoped
   children (partial resolution never closes a gap by assumption).
4. Housekeeping H1–H7 + agent-log entry (H6) after every ingestion.

## Verification

`test_gap_statuses_only_change_with_evidence`,
`test_no_process_friction_entries`,
`test_research_returns_land_in_return_folder_ingestion`,
`test_nesting_parents_refine_when_children_close`.
