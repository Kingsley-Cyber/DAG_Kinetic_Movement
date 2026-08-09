---
id: cpcs.gov.automation_doctrine
kind: policy
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001, SRC-004, SRC-006, SRC-011, SRC-012]
primary_route: cpcs/00_governance/policies/
secondary_routes:
  - cpcs/research/gaps/
interfaces:
  - cpcs.gov.control_plane_reference
  - cpcs.gaps.outstanding_actions
  - cpcs.gov.promotion_rules
---

# Control Plane Automation Doctrine

> **BOOT-ADJACENT.** Read after `control_plane_reference.md`. This policy
> defines how the control plane is **agent-automated**: governance decisions
> are resolved by the decision tree below and executed without user
> consultation. The user is consulted only when a decision brief is raised
> (§6). Asking is the exception, not the default.

## 1. Operating principle

The CPCS control plane runs itself. A new session or agent resolves every
governance decision through the rules in this document, executes the outcome,
and records it in the applied-decisions register (§5). User consultation is a
**bounded exception** — a decision brief (§6) is one page: context, tree path,
options, and a recommended default. Everything else is executed.

This refines the operating prompt's consultation points; when this doctrine
and the operating prompt conflict, this doctrine wins for decision-making,
and the difference is recorded in §5.

## 2. Decision tree

### D1 — Source intake

1. Match the supplied folder/file against the source registry (§8 of the
   control plane reference) and `research/source_registry/identities/`.
   Already distilled → SKIP, record in the ledger.
2. Overlap audit: does most content map to an existing source's claims?
   Yes → distill as EXTEND/SUPPORT into that source's objects; otherwise →
   new source (next free SRC-NNN).
3. Multiple packages supplied → distill **all of them**, in priority order
   (P1 before P2, then file size). No scope question is raised.
4. Each distillation runs PASS 0–11 plus housekeeping H1–H5 (§4) and this
   doctrine's placement rules (D2).

### D2 — Placement (object creation)

Binding priority (control plane §4):
`REUSE > EXTEND > SUPPORT > SPECIALIZE > MERGE > CREATE`

- **REUSE** — existing object covers the meaning → cite it; do not duplicate.
- **EXTEND** — content maps onto an existing canonical owner → add an
  `## Section title (SRC-NNN EXTEND)` section with a `> **Source:**` blockquote
  and verification tests. Frontmatter `sources` is NOT changed on EXTEND.
- **SUPPORT** — additional evidence for an existing owner → SUPPORT.
- **SPECIALIZE** — parent too broad → child card in the parent's route.
- **MERGE** — two owners redundant → MERGE with a DIST ledger note (rare).
- **CREATE** — only when no existing owner can absorb the meaning. Frontmatter
  per control plane §5; id per §6.4; kind/epistemic_status from the vocabularies.

Every new object must declare `interfaces` or `secondary_routes` to at least
one existing card (no orphan concepts), and every DAG edge vocabulary used in
a card must come from a canonical owner (e.g., `temporal_coupling` relations,
`relation_vocabulary`, `interaction_lifecycle` edges). Unknown edge names are
flagged in PASS 6.

### D3 — Vocabulary conformance (deviation checker)

Run `cpcs_ontology_check.ps1` after every distillation and every batch (H2).
Handle deviations by rule:

| Deviation | Rule |
|---|---|
| `[NO FRONTMATTER]` | Add canonical frontmatter for the file type (gap registers: `kind: gap_register`, `epistemic_status: PROJECT_DERIVED`). |
| `[INVALID KIND]` | Kind used by ≤ 2 files → re-tag to nearest canonical kind (mapping table §3). Used by ≥ 3 files or semantically distinct → vocabulary extension via D4. |
| `[INVALID EPISTEMIC_STATUS]` | Package evidence classes (e.g., `PACKAGE_ESTABLISHED`) describe the **source**, not the tree object → map to `SOURCE_EVIDENCE` (knowledge objects) or `PROJECT_DERIVED` (registers/gaps). Record mapping in §5. |
| `[ROUTE MISMATCH]` | Fix `primary_route` to the actual directory (move the file if the route is canonical). |
| `[DUPLICATE ID]` | Merge or rename; record in §5. |
| `[MISSING FIELD]` / `[EMPTY SOURCES]` | Add the field with the correct value. |

Zero deviations before any further work (checker must exit 0).

### D4 — Controlled-vocabulary extension

Justified only when: ≥ 3 existing objects share the new value, OR the value
encodes a semantic the canonical vocabulary lacks, OR a frozen source
mandates it. Execute as **one change**: update `control_plane_reference.md`
§6 AND `cpcs_ontology_check.ps1`, record in §5, re-run the checker. Never
invent per-card values outside this path (control plane §6.1).

### D5 — Preset/delta conflicts (e.g., rhythm vs phase presets)

Never silently merge conflicting conventions. Document the delta as a
blockquote in both cards; the compiler reconciles as a recorded decision.
Conflicts between sources go to PASS 7 and the contradictions register.

### D6 — Open questions

Never closed by assumption. Closed only with an immutable experiment result,
a provider probe, or new source evidence — then update
`outstanding_actions.md` with a closure note and evidence link. Promotion of
`CPCS_CONVENTION` to canonical requires experiment (`promotion_rules`).

### D7 — Error handling

- Checker deviation → D3; never proceed with open deviations.
- Source unreadable/partial → distill what exists, note the reconstruction in
  the gaps file (precedent: KB topic 14).
- Ambiguous source claim → record a question, choose the conservative reading
  (`CPCS_CONVENTION` tag), never upgrade an evidence class.
- A decision not covered by D1–D6 → raise a brief (§6) with a recommended
  default; until resolved, take the conservative action and record it.

### D8 — Understanding-gap capture (while working)

The agent acts like a student who has learned something but cannot yet say
what it is, why it holds, how to use it, or how to apply it. While working
(distillation, EXTEND, query answering, verification, housekeeping), record
GENUINE understanding gaps automatically in
`research/gaps/understanding_gap_register.md`. Record when the agent:

- cannot state WHAT a concept is with confidence,
- cannot say WHY a principle holds (rationale missing from the tree),
- cannot operationalize HOW to produce or use an object,
- cannot decide WHEN to apply one concept over another (selection), or
- cannot APPLY a concept against a live query, or trace a cross-concept
  relationship (BLEND) the query demands.

Each entry: type (WHAT/WHY/HOW/WHEN/APPLY/BLEND), concepts involved, symptom
(where it surfaced), parent gap (nesting), research target, status. Never
close by assumption (D6); never record process friction as a gap — only
understanding gaps. Capture is continuous; the register is reviewed each
batch (H7).

### D9 — Research return and ingestion

The user performs deep research on an open gap and returns it (chat text or
files dropped in `Research_return_folder/`). The agent:

1. Matches the return to the register by gap id/topic and to its nesting node.
2. Ingests it like a source: REUSE/EXTEND/SUPPORT/CREATE per D2; evidence
   class from the return's strength (never upgraded by assumption, D7).
3. Updates the gap: RESEARCHING → RETURNED → CLOSED with evidence link and
   closure note, or REFINED (children re-scoped, parents narrowed).
4. Runs housekeeping H1–H7 and appends an agent-log entry (H6).

A return that only restates existing content is SUPPORT, not new evidence.
Contradictions go to PASS 7 and the contradictions register.

## 3. Kind mapping table (D3 — nearest canonical kind)

| Non-canonical kind (in use) | Canonical mapping | Files |
|---|---|---|
| `protocol` | `method` | `lab_ab_test_protocol`, `information_transfer_protocol` |
| `lineage` | `mechanism` | `variant_lineage` |
| `procedure` | `method` | `lab_runbooks` |
| `architecture` | `mechanism` | `reference_video_distillation`, `structured_prompting_architecture` |
| `schema` | `schema_draft` | `video_observation_graph` |
| `reference` | `contract` / `catalog` | `cross_format_compiler_reference` → contract; `ugc_realism_reference` → catalog |
| `methodology` | `method` | `pegasus_fight_analysis` |
| `framework` | `experiment_design` / `mechanism` | `cpcs_experimental_program` → experiment_design; `evaluation_framework` → mechanism |
| `registry` | `catalog` | `empirical_pattern_registry` |
| `workflow` | `method` | `graph_aware_rag_bundle` |
| `tooling` | `method` | `kinematic_validation_tooling` |

## 4. Housekeeping (every distillation, every batch)

- H1: regenerate `DIRECTORY.md` — `pwsh -NoProfile -File .\update_directory_md.ps1`
- H2: run `pwsh -NoProfile -File .\cpcs_ontology_check.ps1` → exit 0
- H3: update `control_plane_reference.md` (§2 state, §8 registry, §9 objects,
  §14 queue)
- H4: update `outstanding_actions.md` (EXTEND statuses, question closures,
  §3 queue, §4 notes)
- H5: write identity + DIST ledger + gaps files
- H6: append a working-agent-log entry
  (`00_governance/agent_logs/working_agent_log.md`) — every session/batch:
  focus, work done, decisions, gaps captured, open threads, next steps
- H7: gap-analysis pass — review `understanding_gap_register.md`: re-scope
  stale gaps, refine nested parents when children close, verify statuses
Order: H5 → H1 → H2 → H3 → H4 → H6 → H7. Gap capture is continuous (D8),
not a step.

## 5. Applied-decisions register

| Date | ID | Decision | Rule | Status |
| --- | --- | --- | --- | --- |
| 2026-08-09 | D-2026-08-09-01 | Re-tag 15 non-canonical `kind` values per §3 mapping table (16 deviations incl. `graph_aware_rag_bundle` which carried both kind + epistemic fixes) | D3 | APPLIED |
| 2026-08-09 | D-2026-08-09-02 | Map `PACKAGE_ESTABLISHED` → `SOURCE_EVIDENCE` (objects) / `PROJECT_DERIVED` (gap registers) — package establishment lives in the identity `epistemic_class` | D3 | APPLIED |
| 2026-08-09 | D-2026-08-09-03 | Add canonical frontmatter to `src012_open_research_questions.md` (`cpcs.gaps.src012`, `gap_register`, `PROJECT_DERIVED`) | D3 | APPLIED |
| 2026-08-09 | D-2026-08-09-04 | Reconcile distillation queue to 6 pending incl. `11 Polyglot Compiler.md`; DMR execution kit stays SRC-013 candidate (overlap audit with SRC-007 before distillation) | D1 | APPLIED |
| 2026-08-09 | D-2026-08-09-05 | SRC-012 pass executed without scope consultation (4 CREATE + 6 EXTEND + identity + ledger + gaps); user consulted only for the SRC-013 deferral brief | D1/D2 | APPLIED |
| 2026-08-09 | D-2026-08-09-06 | Extend `kind` vocabulary with `agent_log` (D4: distinct semantic — chronological agent work record; no existing kind covers it); applied to reference §6.1 + checker in one change | D4 | APPLIED |
| 2026-08-09 | D-2026-08-09-07 | Create `working_agent_log.md` (`cpcs.gov.working_agent_log`) + `understanding_gap_register.md` (`cpcs.gaps.understanding_register`); seeded with genuine gaps surfaced during SRC-012 + automation batch | D3/D8 | APPLIED |
| 2026-08-09 | D-2026-08-09-08 | Establish research-return loop: `Research_return_folder/` intake + D9 ingestion; the user returns deep research on nesting gaps and the agent ingests it without consultation | D1/D9 | APPLIED |
| 2026-08-09 | D-2026-08-09-09 | Representation route first content: capture user-supplied quad-carrier prompt as specimen (`fixture_set`, verbatim in `representation/hybrids/`) + structure analysis (`method`, INFERENCE — no carrier superiority claimed per §11.7) | D2/D3 | APPLIED |

## 6. User decision briefs (the ONLY consultation points)

A brief is raised only when:

1. **Uncovered case** — the tree has no rule for the decision; escalate with
   the doctrine's recommended default.
2. **External irreversibility** — provider contracts, public claims, licensing,
   or anything outside the repo.
3. **Budget conflict** — multiple packages compete for a single execution
   budget and D1's priority ordering cannot decide (rare; default is priority
   order P1 → P2, then file size).
4. **Demotion of an ESTABLISHED claim** — a new source would downgrade an
   existing evidence class with provenance implications.
5. **Explicit review request** — the user asks to review a batch.

No other prompts are raised. Briefs are one page: context, tree path, options,
recommended default.

## Verification

`test_doctrine_decisions_recorded_in_register`,
`test_housekeeping_runs_after_every_batch`,
`test_checker_exit_zero_before_proceeding`,
`test_user_consulted_only_on_brief_triggers`.
