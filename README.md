# CPCS — Knowledge Tree for Kinetic Cinematic Performance

> **Boot file for humans and agents.** This repository is a *living knowledge
> tree*, not a codebase: research sources are distilled into a DAG-style
> ontology, agents operate it through an automated control plane, and gaps in
> agent understanding are surfaced as research assignments. Read this file
> top to bottom once — it contains the granular operational detail needed to
> pick up and continue work without asking.

**Identity:** `github.com/Kingsley-Cyber/DAG_Kinetic_Movement` (public) ·
branch `main` · HEAD `122e785` · 733 tracked files

---

## 1. Live state (as of 2026-08-09)

| Property | Value |
| --- | --- |
| Sources distilled | 12 (SRC-001 … SRC-012) |
| Knowledge objects | 183 `cpcs.*` objects (178 cards + 5 system files) |
| Files with frontmatter | 209 — ontology checker: **0 deviations** |
| Routes (directories) | 1,124 (1,011 leaves) — DIRECTORY.md LIVE |
| Open research questions | 155 across 12 sources (0 closed) |
| Pending distillation sources | 6 (04b, 07, 08, 09, 10, `11 Polyglot Compiler.md`) |
| SRC-003 EXTENDs | 14 PENDING + 1 PARTIAL + 3 APPLIED |
| Understanding gaps (UG) | 7 open, nested (UG-001 … UG-007) |
| Evidence classes | 8 epistemic statuses · 15 kinds · 10 acquisitions |
| Control plane | agent-automated via decision tree D1–D9 |

## 2. What this is

**CPCS** = Cinematic Performance Control System: a structured, DAG-style
knowledge and runtime architecture for directing, compiling, and verifying
kinetic cinematic performance (live-action, anime, documentary, UGC).
Twelve research sources — a frozen KB, the CPCS directorial paper + Pegasus
extraction system, the empirically validated Prompt Lab, the ADRG reasoning
package, gap-closure research, and more — have been distilled into three
planes:

- **Knowledge plane** (`cpcs/knowledge/`) — domain taxonomy: foundations,
  story, character performance (FACS/Laban/Bartenieff), action/combat, phase
  grammar, rhythm/time, interaction/contact, force physics, camera,
  style, continuity, generation complexity, interfaces.
- **Research plane** (`cpcs/research/`) — source registry (identities),
  distillation ledger (DIST-001…012), gaps (per-source questions +
  understanding register), experiments.
- **Runtime plane** (`cpcs/runtime/`) — request → retrieval → synthesis
  (ADRG) → strategy/constraints → canonical control → compiler →
  provider negotiation, plus `evaluation/`, `verification/`,
  `maintenance/` loops around it.

## 3. How an agent auto-picks this up (boot sequence)

Run these in order at session start (control plane reference §12):

1. `cpcs/00_governance/policies/control_plane_reference.md` — live state,
   vocabularies, registry, queue.
2. `cpcs/00_governance/policies/control_plane_automation_doctrine.md` —
   resolves governance decisions WITHOUT user consultation; briefs only on
   its §6 triggers.
3. `cpcs/00_governance/agent_logs/working_agent_log.md` — what previous
   sessions did, what is in flight, what to pick up (read latest 3–5
   entries; continue `IN FLIGHT` threads first).
4. `cpcs/research/gaps/understanding_gap_register.md` — open student gaps
   awaiting user deep research.
5. `CPCS Research Distillation Agent - Persistent Operating Prompt.md` —
   the PASS 0–11 distillation workflow.
6. `DIRECTORY.md` (root) — route tree.
7. Run the checker (see §8) — tree must be clean before any work.
8. Check the distillation queue (control plane §14).
9. Read the most recent DIST ledger (`cpcs/research/distillation/ledger/`).
10. Read `cpcs/research/gaps/outstanding_actions.md` — EXTEND statuses,
    open questions, pending sources.

## 4. Control plane — how the tree is governed

**Operating principle:** the control plane runs itself. A new session
resolves every governance decision through the doctrine's decision tree and
records the outcome in its §5 applied-decisions register. The user is
consulted ONLY on the five brief triggers (§6): uncovered case, external
irreversibility, budget conflict, demotion of an ESTABLISHED claim, explicit
review request.

**Decision tree (doctrine §2):**

| Node | Resolves |
| --- | --- |
| D1 | Source intake — match registry, overlap audit (EXTEND vs new SRC), distill ALL supplied packages, no scope question |
| D2 | Placement — binding priority `REUSE > EXTEND > SUPPORT > SPECIALIZE > MERGE > CREATE`; no orphan concepts (interfaces required) |
| D3 | Vocabulary conformance — deviation checker rules: NO FRONTMATTER → add; INVALID KIND ≤2 files → re-tag per §3 mapping; ≥3 → D4; PACKAGE_ESTABLISHED → SOURCE_EVIDENCE/PROJECT_DERIVED |
| D4 | Vocabulary extension — one change: reference §6 + checker + register, never per-card values |
| D5 | Preset/delta conflicts — never merge; document as blockquote; compiler reconciles |
| D6 | Open questions — never closed by assumption; require experiment/probe/evidence + closure note |
| D7 | Error handling — conservative action; uncovered decisions → brief with default |
| D8 | Understanding-gap capture — record genuine WHAT/WHY/HOW/WHEN/APPLY/BLEND gaps while working (§5) |
| D9 | Research return — user returns deep research → ingest like a source, close/refine UG gap with evidence |

**Housekeeping order (every distillation, every batch):**
`H5 (identity/ledger/gaps) → H1 (DIRECTORY.md) → H2 (checker green) →
H3 (control plane reference) → H4 (outstanding_actions) → H6 (agent log) →
H7 (gap-register review)`.

**Controlled vocabularies (must match checker exactly):**

- Kinds (15): `agent_log · catalog · contract · doctrine · experiment_design ·
  fixture_set · gap_register · mechanism · method · metric_contract · policy ·
  principle · provider_finding · schema_draft · vocabulary`
- Epistemic statuses (8): `SOURCE_EVIDENCE · INFERENCE · CREATIVE_CHOICE ·
  PROJECT_DERIVED · PROVIDER_EXPERIMENT · UNVERIFIED · CONTRADICTED · UNKNOWN`
- Acquisitions (10): `authored · observed · detected · measured · estimated ·
  inferred · derived · interpreted · simulated · creative_choice`
- IDs: `cpcs.<domain>.<concept>` (cards), `SRC-NNN` (registrations),
  `DIST-NNN` (ledgers) — the only non-`cpcs.*` ids in the tree.

## 5. The gap loop — homework for deep research

`cpcs/research/gaps/understanding_gap_register.md` is the agent's "student
gap" register: things the tree has ingested but the agent cannot yet
confidently state (**WHAT**), justify (**WHY**), produce (**HOW**), select
(**WHEN**), apply to a query (**APPLY**), or integrate (**BLEND**). Gaps are
captured automatically while working (D8) — never process friction, never
closed by assumption.

- Gaps are **nested** (UG-001 parents UG-002/003/006). Closing a child
  refines the parent; research aligns to the exact nesting level it answers.
- The user does deep research on UG ids and returns it via
  `Research_return_folder/` or chat; the agent ingests it per **D9**:
  match → ingest (REUSE/EXTEND/SUPPORT/CREATE) → status
  `OPEN → RESEARCHING → RETURNED → CLOSED (evidence)` or `REFINED`.
- Current seeds: UG-001 (WHEN: timing-query object selection), UG-002
  (BLEND: rhythm vs phase preset reconciliation), UG-003 (WHEN: 7/4/10-phase
  granularity), UG-004 (BLEND: evidence-class vocabularies), UG-005 (WHY:
  master-clock seconds authority), UG-006 (APPLY: BML sync points → camera
  impact binding), UG-007 (WHAT: `sequencing_delay_ms` 55 ms transferability).

## 6. Working agent log — session continuity

`cpcs/00_governance/agent_logs/working_agent_log.md` (kind `agent_log`):
append-only journal. Every session/batch appends an entry with fields:
Date · Session · Focus · Work done · Decisions (doctrine §5 ids) · Gaps
captured (UG ids) · Open threads · Next steps. Past entries are NEVER
rewritten — correct forward. New sessions read the latest entries to pick up
exactly where the previous session stopped.

## 7. Object conventions

- Every `.md` under `cpcs/` MUST have YAML frontmatter: `id`, `kind`,
  `epistemic_status`, `acquisition`, `sources`, `primary_route`
  (must match the file's directory); optional `secondary_routes`,
  `interfaces` (cross-department links — required on new objects, no
  orphans).
- **EXTEND format:** add `## Section title (SRC-NNN EXTEND)` with a
  `> **Source:**` blockquote and verification tests. Frontmatter `sources`
  is NOT changed on EXTEND.
- **Identity files** (`research/source_registry/identities/`) use
  `epistemic_class` + `kind: research_package` — package establishment
  lives THERE, not on tree objects.
- Every DAG edge vocabulary used in a card must come from a canonical owner
  (e.g., `temporal_coupling` relations, `interaction_lifecycle` edges).

## 8. Commands

```powershell
# Ontology check (must exit 0 before/after any batch)
pwsh -NoProfile -File .\cpcs_ontology_check.ps1

# Regenerate DIRECTORY.md (after any route change)
pwsh -NoProfile -File .\update_directory_md.ps1
```

## 9. Git operations

```powershell
# Commits require BOTH flags (no global git identity; deep paths exceed MAX_PATH):
git -c core.longpaths=true -c user.name="Kingsley-Cyber" `
    -c user.email="239618402+Kingsley-Cyber@users.noreply.github.com" `
    commit -m "..."
# The longpaths flag is also required for add/status/ls-files on this tree.
```

- `.gitignore`: `.qoder/` (IDE cache), `.git.nested-backup/` (preserved
  nested-repo history of the prompt-system copy).
- **Pitfall:** source packages containing their own `.git` are committed as
  gitlinks (mode 160000) instead of files. After `git add`, verify:
  `git ls-files -s | Select-String "^160000"` → must be empty.
- Repo is PUBLIC: external-facing actions are reviewed, but routine commits
  are part of the normal loop.

## 10. Story so far (log)

### Distilled sources

| ID | Source | Objects written |
| --- | --- | --- |
| SRC-001 | AI video motion direction KB gap closure | 25 new |
| SRC-002 | FACS/Laban/Bartenieff gap closure | 37 new + 9 EXTEND |
| SRC-003 | MX hierarchical motion grammar gap closure | 30 new + 18 EXTEND |
| SRC-004 | ADRG director reasoning gap closure | 12 new + 8 EXTEND |
| SRC-005 | MX hierarchical motion grammar paper | 14 new + 6 EXTEND |
| SRC-006 | Video test-time reasoning gap closure | 10 new + 3 EXTEND |
| SRC-007 | Director motion reasoning runtime prompt | 6 new + 6 EXTEND |
| SRC-008 | MX grammar research package v1.0 (frozen) | 6 new + 4 EXTEND |
| SRC-009 | CPCS paper v1.2 + Pegasus v1.0 + extraction guide | 12 new + 6 EXTEND |
| SRC-010 | CPCS Prompt Lab (`lab/` + `references/`, 44 files) | 9 new + 5 EXTEND |
| SRC-011 | ADRG research package v1.0 | 3 new + 6 EXTEND |
| SRC-012 | AI Video Motion Direction KB v1.0.0 (frozen) | 4 new + 6 EXTEND |

### Sessions

| Date | Session | Outcome |
| --- | --- | --- |
| 2026-08-09 | SRC-012 pass | 4 CREATE + 6 EXTEND (E16/E18 applied); DIRECTORY 1,123 routes |
| 2026-08-09 | Automation doctrine batch | Doctrine D1–D7; 20 checker deviations → 0; control plane live (12 sources, 181 objects) |
| 2026-08-09 | GitHub publication | Public repo created; gitlink fix (733 files, HEAD 122e785) |
| 2026-08-09 | Gap + log loop | Understanding register (UG-001…007) + working agent log + D8/D9 + H6/H7; checker 209 files clean |
| 2026-08-09 | README | This file; AGENTS.md/CLAUDE.md de-skeletoned |

### Pending work (pick up here)

1. Distill the 6 pending queue sources (04b, 07, 08, 09, 10, `11 Polyglot Compiler.md`).
2. Apply 14 PENDING SRC-003 EXTENDs.
3. Close 155 open questions (requires evidence — D6).
4. Await user deep research on UG-001…007 → D9 ingestion.
5. Overlap-audit the DMR execution kit (SRC-013 candidate) vs SRC-007.

## 11. Key file map

| Path | Role |
| --- | --- |
| `cpcs/00_governance/policies/control_plane_reference.md` | BOOT file — live state, vocabularies, registry, queue |
| `cpcs/00_governance/policies/control_plane_automation_doctrine.md` | Decision tree D1–D9, brief triggers, applied-decisions register |
| `cpcs/00_governance/agent_logs/working_agent_log.md` | Session journal (H6) |
| `cpcs/research/gaps/outstanding_actions.md` | BOOT-CRITICAL action tracker |
| `cpcs/research/gaps/understanding_gap_register.md` | Student-gap register (D8/D9) |
| `cpcs/research/source_registry/identities/` | SRC-001…012 identities |
| `cpcs/research/distillation/ledger/` | DIST-001…012 ledgers |
| `Research_distillation_folder/` | Raw source packages (incl. nested `.git.nested-backup`) |
| `Research_return_folder/` | Deep-research intake for D9 ingestion |
| `cpcs_ontology_check.ps1` | Deviation checker (vocabularies must match reference §6) |
| `update_directory_md.ps1` | DIRECTORY.md generator (renders directories only) |
