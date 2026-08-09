---
id: cpcs.gaps.understanding_register
kind: gap_register
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008, SRC-009, SRC-010, SRC-011, SRC-012, SRC-013, SRC-014, SRC-015, SRC-016]
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
| UG-008 | WHAT/HOW | How must articulated and deformable hand–object state transitions be represented, causally compiled, and verified — the sling-bag zipped→open hard-cut bridge (typed part graph, durative causal transitions, contact identity, action-specific verification)? | interaction_lifecycle, affordance_constraints, continuity_state, failure_mode_catalog | — | CLOSED — research returned 2026-08-09 (gap_answer_01/02 + supplements 03/04/05), ingested as SRC-013/014/015/016; see closure note below |
| UG-009 | APPLY | Which carrier hierarchy does a provider surface follow best — the declared quad (YAML+XML+JSON+prose with explicit format_policy), a pair, or prose-only? (renumbered from UG-008 2026-08-09 — UG-008 adopted for the returned hand-object research) | format_policy, carrier_role_semantics, carrier_effect_design | — | OPEN |

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
| UG-008 | Research return SRC-013 (E1–E14: OpenUSD, NVIDIA deformables, PDDL2.1, BDDL, ARCTIC, ContactPose, TAP-Vid, VBench, PhyGenBench, Veo, Runway, Firefly); supplements SRC-014 (reliability cheat sheet), SRC-015 (manipulation directing), SRC-016 (hand diagnosis) |
| UG-009 | SRC-010 A/B experiment patterns (carrier effect unmeasured — see carrier_effect_design) |

## 4. Research alignment (D9 — return and ingestion)

1. The user returns deep research for any UG id — in chat or as files dropped
   in `Research_return_folder/`.
2. The agent matches the return to the nesting node, ingests it like a source
   (REUSE/EXTEND/SUPPORT/CREATE per D2, evidence class from return strength).
3. Status update: `RESEARCHING` when taken on, `RETURNED` once ingested,
   `CLOSED` with evidence link + closure note, or `REFINED` with re-scoped
   children (partial resolution never closes a gap by assumption).
4. Housekeeping H1–H7 + agent-log entry (H6) after every ingestion.

## 5. Research briefs (grad-student assignments)

Each brief turns its gap into a falsifiable research assignment: a primary
question, structured sub-questions, exact queries (tree + source + field),
evidence requirements, acceptance criteria, and a deliverable spec. Research
that satisfies the acceptance criteria closes the gap; anything less is a
partial resolution that REFINES it (D6 — never close by assumption).

**How to execute a brief:** (1) read the four concept cards listed under
Concepts; (2) run the tree queries against `DIRECTORY.md` and the concept
cards; (3) consult the source queries in `Research_distillation_folder/`;
(4) form claims with evidence links; (5) produce the deliverable and drop it
in `Research_return_folder/` with the UG id in the filename.

### UG-001 — Timing query selection (WHEN · parent)

**Primary question:** Which canonical object answers a timing query, and by
what decision rule?

**Structured sub-questions:**
1. What is the distinct intent of each candidate — `rhythm_metrics_contract`
   (sequence/scene/phrase/exchange/action/phase/micro-event/frame hierarchy,
   production profiles, master_clock_s), `phase_timing_presets` (normalized
   7-phase ratios, preset families explosive/ballistic/controlled/sustained/
   microgesture, CPCS_CONVENTION), `beat_syncpoint_alignment` (BML sync
   points, phase →(mapped_to)→ sync_point), `temporal_coupling` (relative
   phase, phase_locks_to, timing profiles vs durations)?
2. Which query intents map to each object — tempo/musical-grid questions
   (tempo, tempo curve, cadence, meter, beat phase, syncopation, swing,
   rubato, entrainment), phase-ratio questions (initiation…settle ratios),
   beat-anchoring questions (anticipation beats, accent strength, contact_s),
   relative-phase questions (actor/limb phase vs master clock or beat)?
3. When must two objects co-answer a single query (e.g., a query asking for
   beat-anchored phase ratios), and which object owns the authoritative part?
4. What happens when a query's intent is ambiguous — is there a default
   object, and what is the tie-break rule?

**Exact queries:**
- Tree: `master_clock_s`, `frame_clock`, `musical_grid`, `phase_locks_to`,
  `mapped_to`, `sync_point`, `normalized phase ratios`, `production
  profiles`, `contact_s`, `beat phase`, `entrainment`, `timing profiles`
- Source: SRC-012 frozen KB `rhythm` object section (profile + contact_s +
  setup_strike_recovery 3-split) in `Research_distillation_folder/`; SRC-012
  Q1/Q2/Q3 question section
- Field: "beat-synced motion phase anchoring cinematography timing systems"

**Evidence requirements:** the four concept cards + DIRECTORY.md route
ownership; SRC-012 identity + ledger; 5 real query examples traced end-to-end.

**Acceptance criteria (CLOSE when):** a decision table maps ≥8 query intents
(tempo, meter, beat phase, phase ratios, preset selection, beat anchoring,
relative phase, timing profiles, sync point mapping, contact timing) to
exactly one owning object each; no ambiguous rows; each row cites the card
section that justifies ownership; the default/tie-break rule is stated.

**Deliverable:** `UG-001_timing_query_decision_table.md`

### UG-002 — Rhythm vs phase preset reconciliation (BLEND · child of UG-001)

**Primary question:** How do the KB rhythm presets (production profiles) and
phase-grammar presets (normalized execution) reconcile at compile time, and
is the 3-split `setup_strike_recovery` a scene field or an authoring
convenience?

**Structured sub-questions:**
1. Are the two preset families semantically equivalent (same 7 phase names)
   but different encodings, or different abstractions — production profile
   (rhythm-oriented: initiation/preparation/acceleration/stroke/overshoot/
   recovery/settle, e.g. explosive 0.05/0.22/0.18/0.10/0.10/0.20/0.15) vs
   normalized execution (explosive 0.03/0.09/0.19/0.22/0.14/0.22/0.11)?
2. What does "reconciled by the compiler" mean operationally — a recorded
   decision (`mx_compiler`/`constraint_compilation`), a canonical
   downcasting, or a third merged preset family?
3. Where must `setup_strike_recovery` live: `canonical_schema_design` scene
   fields, or compiler-internal authoring convenience (SRC-012 Q3)?
4. What is the precedence order when rhythm and phase presets disagree, and
   is there any silent-override path left in the tree?

**Exact queries:**
- Tree: `reconciled by the compiler`, `explosive`, `0.05/0.22/0.18`,
  `0.03/0.09/0.19`, `setup_strike_recovery`, `canonical_schema_design`,
  `mx_compiler`, `constraint_compilation`, `CPCS_CONVENTION`,
  `delta (documented, do not merge)`
- Source: SRC-012 Q3; SRC-010 lab preset references; SRC-008 mx_profiles
- Field: "animation timing preset reconciliation scene field vs authoring"

**Evidence requirements:** both preset tables in full (all 5 presets × 7
ratios); the two delta blockquotes; SRC-012 Q3; canonical_schema_design
field list; compiler cards.

**Acceptance criteria (CLOSE when):** a stated reconciliation precedence
(which preset wins under which compile condition, who records the decision);
a ruling on setup_strike_recovery with rationale grounded in
canonical_schema_design; zero silent-override paths enumerated.

**Deliverable:** `UG-002_preset_reconciliation_spec.md`

### UG-003 — Phase granularity selection (WHEN · child of UG-001)

**Primary question:** Which phase granularity applies when analyzing a query:
KB 7-phase (contact as event), SRC-010 4-phase (contact as bin), or the tree
10-step engineering grammar?

**Structured sub-questions:**
1. What is each granularity's purpose — 7-phase evidence analysis
   (initiation…settle with contact as event), 4-phase strike ratios
   (setup_strike_recovery [0.4, 0.18, 0.42], contact as bin), 10-step
   engineering grammar (`evidence_vs_engineering_phases` E18)?
2. Which query conditions select each granularity — analysis/evidence
   queries vs metric-layer queries vs compile/engineering queries?
3. Can one query demand two granularities simultaneously (analysis then
   compile)? What is the boundary translation rule between representations?
4. Where do the granularities conflict (contact as event vs bin vs
   engineering step) and who arbitrates?

**Exact queries:**
- Tree: `evidence_vs_engineering_phases`, `contact`, `strike ratios`,
  `setup_strike_recovery`, `bin`, `10-step`, `7-phase`, `4-phase`,
  `combat_math_metrics_layer`, `phase_timing_presets`
- Source: SRC-010 4-phase strike ratio tables; SRC-012 Q8; SRC-012 E18
- Field: "motion phase segmentation granularity contact event vs bin"

**Evidence requirements:** the three granularity definitions with their
canonical owners; SRC-012 Q8; evidence_vs_engineering_phases card;
combat_math_metrics_layer strike ratios.

**Acceptance criteria (CLOSE when):** a selection rule table (query
condition → granularity) with no overlapping conditions; a boundary
translation rule for contact across all three representations; arbitration
owner named.

**Deliverable:** `UG-003_granularity_selection_rule.md`

### UG-004 — Evidence-class vocabulary mapping (BLEND · top-level)

**Primary question:** Do the package evidence-class vocabularies (KB 5,
SRC-005 7, SRC-009 VOG 5, SRC-011 6) map onto `evidence_two_axis_model`, and
which label wins when they disagree?

**Structured sub-questions:**
1. What are the two axes of `evidence_two_axis_model` (acquisition ×
   epistemic state) and how does each package vocabulary decompose onto
   them (PACKAGE_ESTABLISHED, REPO_OBSERVED, VOG classes, ADRG classes)?
2. Is the 4-dimension orthogonality expansion (knowledge basis ×
   acquisition × epistemic state × confidence — SRC-004 E6 PENDING) a
   prerequisite for the mapping?
3. Which precedence chain resolves label conflicts (per E1 confidence
   fusion 5 rules, E3 precedence chains)?
4. Does `promotion_rules` already define the threshold CPCS_CONVENTION →
   canonical (requires experiment), and does it subsume package labels?
5. Recommendation: tree-wide adoption of one vocabulary vs package-local
   vocabularies with a canonical mapping layer (SRC-012 Q4)?

**Exact queries:**
- Tree: `evidence_two_axis_model`, `evidence class`, `PACKAGE_ESTABLISHED`,
  `REPO_OBSERVED`, `confidence fusion`, `precedence`, `promotion_rules`,
  `acquisition`, `epistemic state`, `CPCS_CONVENTION`, `orthogonality`
- Source: SRC-005 7-class table; SRC-009 VOG 5-class table; SRC-011 ADRG
  6-class table; SRC-012 Q4; SRC-004 E6
- Field: "evidence classification provenance epistemics knowledge graphs"

**Evidence requirements:** the four vocabulary tables verbatim; the two-axis
model card (E1/E3 applied, E6 PENDING); promotion_rules threshold.

**Acceptance criteria (CLOSE when):** a full mapping table (5+7+5+6 labels →
two-axis coordinates) with a conflict precedence chain; an explicit ruling on
E6 prerequisite; a tree-wide adoption recommendation with rationale.

**Deliverable:** `UG-004_evidence_vocabulary_map.md`

### UG-005 — Master-clock seconds authority (WHY · top-level)

**Primary question:** Why is seconds the authoritative master-clock base while
frame/musical references derive — what breaks if a source binds to frames?

**Structured sub-questions:**
1. What does the tree already guarantee — master_clock_s → frame_clock
   (derived: fps) → musical_grid (derived: bpm, meter, beat phase); never
   round intermediate timeline values; re-derive musical-grid fields
   (tempo, tempo curve, cadence, meter, beat phase, syncopation, micro-
   pauses, anticipation beats, accent strength, event density, swing,
   rubato, entrainment, phase lock)?
2. Failure-mode analysis: what breaks under frame authority — repeated
   rounding drift across long sequences, variable frame rates, tempo
   changes mid-sequence, quantize-to-frame render targets?
3. What breaks under musical-grid authority — rubato/entrainment vs fixed
   beats, independent axes (fast tempo + long micro-pause, slow scene +
   high-acceleration accent)?
4. Does `timebase_systems` define conversion guarantees, and is any
   card in the tree already binding to frames in a way that violates the
   doctrine?

**Exact queries:**
- Tree: `master clock`, `master_clock_s`, `frame_clock`, `musical_grid`,
  `derived`, `rounding`, `drift`, `quantize`, `variable frame rate`,
  `timebase_systems`, `entrainment`, `rubato`, `phase lock`
- Source: SRC-012 E1 master-clock section; temporal_coupling E16 content
- Field: "timebase authority continuous time quantization drift animation"

**Evidence requirements:** temporal_coupling master clock doctrine;
rhythm_metrics_contract; timebase_systems card; a scan of the tree for
frame-bound declarations.

**Acceptance criteria (CLOSE when):** a failure-mode table with ≥3 concrete
failure mechanisms under frame authority (mechanism + consequence + affected
route), a like analysis for musical-grid authority, and a preservation
argument for seconds authority grounded in the doctrine text.

**Deliverable:** `UG-005_master_clock_failure_analysis.md`

### UG-006 — BML sync points → camera impact binding (APPLY · child of UG-001)

**Primary question:** How do I apply BML sync points to camera impact binding
(phase_locks_to → binds chain) when the provider surface lacks phase
controls?

**Structured sub-questions:**
1. What is the concrete chain — beat_syncpoint_alignment (phase
   →(mapped_to)→ sync_point) → camera_impact_sync (binds) — and where do
   the sync points attach (anticipation beats, accent strength, contact_s)?
2. What does canonical downcasting do to phase fidelity per
   `provider_capability_snapshots` status (7-status vocabulary, dated model
   matrix 2026-07-30, loss report, adapter contract fields)?
3. Which losses are acceptable when phase_timing/FACS/BESS are high-loss in
   prose (SRC-012 Q5 downcasting note) — time-warped sync vs dropped sync vs
   nearest-beat approximation?
4. What does `provider_fallback_ladder` do when the selected provider lacks
   the capability, and what must the adapter contract declare?

**Exact queries:**
- Tree: `phase_locks_to`, `binds`, `sync_point`, `mapped_to`,
  `beat_syncpoint_alignment`, `camera_impact_sync`, `downcasting`,
  `loss report`, `adapter contract`, `provider_fallback_ladder`,
  `provider_capability_snapshots`, `canonical downcasting`
- Source: SRC-007 provider cards (G007/G008 contracts and adapters, G021
  lifecycle); SRC-012 Q5; SRC-012 E1 sync vocabulary
- Field: "motion control downcasting capability negotiation fallback"

**Evidence requirements:** the sync-point cards; provider_capability_snapshots
status vocabulary + dated matrix; fallback ladder; SRC-012 Q5.

**Acceptance criteria (CLOSE when):** a step-by-step binding procedure
(query → sync points → downcast decision → loss budget → fallback); a loss
budget table per provider status (which losses are acceptable); the adapter
contract fields that must declare phase fidelity.

**Deliverable:** `UG-006_camera_binding_procedure.md`

### UG-007 — sequencing_delay_ms vs per-pattern lag calibration (WHAT · top-level)

**Primary question:** What exactly distinguishes `sequencing_delay_ms` (single
55 ms CPCS_CONVENTION sample) from per-pattern lag calibration — is 55 ms
transferable across actors?

**Structured sub-questions:**
1. What does the 55 ms encode — primitive sequencing delay
   (bartenieff_six_patterns E4: Basic Six vs patterns separation, primitive
   encoding) vs the worked cross-punch value from an immutable experiment?
2. What is the definitional boundary — sequencing_delay_ms (pattern-level
   encoding constant) vs per-pattern lag calibration (per action, actor,
   genre, model — phase_timing_presets "learn them … through immutable
   experiments")?
3. What variance sources affect transferability — actor morphology,
   technique class, genre, model — and which are first-order?
4. How would an immutable experiment calibrate it (SRC-012 Q7), and what
   design minimizes samples per actor?
5. Where must the value live — the pattern card, `phase_timing_presets`,
   or a convention layer — and does `exhale synchronizes_with
   action_release` (temporal_coupling) interact with it?

**Exact queries:**
- Tree: `sequencing_delay_ms`, `55`, `lag`, `calibration`, `immutable
  experiments`, `bartenieff_six_patterns`, `primitive encoding`, `exhale
  synchronizes_with`, `CPCS_CONVENTION`, `worked cross-punch`
- Source: SRC-012 Q7; bartenieff_six_patterns E4 section; SRC-010 lab
  worked-example `ex_cross_punch_01`
- Field: "motor primitive sequencing delay calibration biomechanics timing"

**Evidence requirements:** the 55 ms occurrence(s) with context; the E4
primitive-encoding section; phase_timing_presets learn-via-experiments
statement; SRC-012 Q7.

**Acceptance criteria (CLOSE when):** a precise definition of
sequencing_delay_ms vs per-pattern lag (with the boundary in terms of
primitive encoding vs calibration); a variance hypothesis ranking sources;
an immutable-experiment design (per actor/technique) with sample budget;
the transferability boundary stated (where 55 ms holds, where it does not).

**Deliverable:** `UG-007_lag_calibration_design.md`

### Closure note — UG-008 (2026-08-09)

Closed with evidence, not assumption (D6): the user returned a research
package (`gap_answer_01_Articulated and Deformable Hand-Obj.txt` +
`gap_answer_02_articulated_deformable_hand_object_transitions.md`) that
answers the primary question with a 14-source evidence registry (E1–E14),
a typed part–connection–region schema, a durative causal transition schema,
a contact-identity model, action-specific verification metrics, and a
provider carrier decision matrix. Ingested as SRC-013 (identity + DIST-013
ledger + 5 EXTENDs). The return itself is **staged research** ("not curated
repository truth"): the EXTENDs record its actionable core; numeric claims
(2 mm penetration, V ≥ 0.70, ≤ 0.05 m/s, ≤ 11.3 mm²) stay SRC-013 evidence
until experiments validate them.

**Supplements (same day):** the user also returned three UG-008 supplements,
all dropped in the repo root and ingested automatically — `gap_answer_03`
(causal video-generation reliability cheat sheet → SRC-014, provider
control-surface matrix + negative-prompt precedence in
capability_classes_and_loss_records), `gap_answer_04` (AI video directing
for causal human-object manipulation → SRC-015, mechanism vocabulary in
affordance_constraints + bimanual role permanence/regrasp observability in
interaction_lifecycle), and `gap_answer_05` (why AI video adds extra or
mismatched hands → SRC-016, hand-identity label stability in
interaction_lifecycle + role_renaming/hand_spawn/reentry_reset rows in
failure_mode_catalog). All three corroborate the SRC-013 core; their
provider facts and artifact-rate claims stay staged evidence.

### UG-009 — Provider carrier-hierarchy following (APPLY · top-level)

**Primary question:** Which carrier hierarchy does a provider surface follow
best — the declared quad (YAML+XML+JSON+prose with explicit `format_policy`),
a pair, or prose-only?

**Structured sub-questions:**
1. What does `carrier_role_semantics`/`format_ownership` (SRC-004 compiler
   cards) say about how carriers should be assigned roles, and does the
   quad's `format_policy primary="yaml+xml" precision="json"` conform?
2. Which provider surfaces accept structured input at all (per
   `provider_capability_snapshots` dated matrix) vs text-only — and does
   carrier order in the prompt change adherence?
3. Does the CDATA quad beat the pair (YAML+XML) or prose-only on the same
   scene (artifact rate: extra hands, morph, state jumps; shot adherence;
   cut-edge continuity)?
4. What experiment design (`carrier_effect_design`) isolates the carrier
   variable from content — same scene, same laws, different carriers?
5. What is the loss hierarchy when a surface rejects a carrier (drop JSON
   first vs YAML first) — which axis degrades first?

**Exact queries:**
- Tree: `carrier_role_semantics`, `format_ownership`, `format_policy`,
  `provider_capability_snapshots`, `carrier_effect_design`, `downcasting`,
  `loss report`, `capability_classes_loss_records`, `prompt_budget`
- Source: SRC-010 lab A/B protocol (`lab_ab_test_protocol`); SRC-004
  compiler cards; specimen `pov_glasses_bag_prompt_specimen`
- Field: "structured vs prose prompts video generation adherence ablation"

**Evidence requirements:** carrier_effect_design harness; the specimen run
at least twice per carrier variant; provider capability matrix rows for the
tested surfaces.

**Acceptance criteria (CLOSE when):** a measured adherence table per
carrier-variant × provider (artifact rate, shot adherence, cut continuity);
a stated loss hierarchy with which axis degrades first per surface; a
conformance verdict for `format_policy` against carrier_role_semantics.

**Deliverable:** `UG-008_carrier_following_matrix.md`

## 6. Verification

`test_gap_statuses_only_change_with_evidence`,
`test_no_process_friction_entries`,
`test_research_returns_land_in_return_folder_ingestion`,
`test_nesting_parents_refine_when_children_close`.
