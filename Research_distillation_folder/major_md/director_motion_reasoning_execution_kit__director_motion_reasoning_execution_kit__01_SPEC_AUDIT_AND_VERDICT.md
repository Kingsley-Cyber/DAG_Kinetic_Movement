# Director Motion Reasoning Specification Audit

## Executive verdict

The uploaded specification is strong as a **domain inventory**, but it is not safe to execute literally against the current repository. It instructs an agent to create a large new package under `research/director_motion_reasoning/`, while the repository's governing `AGENTS.md` declares `research/` frozen, SHA-protected, and non-editable in place. The repository already contains two mature research packages, a concept corpus, a derived knowledge graph, a 14-layer universal motion skeleton, a format-control map, canonical schemas, compilers, RAG corpora, examples, and deterministic validation gates.

The correct action is therefore **gap-first integration**, not a second parallel ontology. The uploaded specification itself requires repository inspection, convention reuse, and avoidance of duplication, so this interpretation follows the source task rather than weakening it.

## Audit classification

This audit clusters the 1,400-line request into 55 implementation requirements.

- Existing strong coverage: 20
- Existing partial coverage: 22
- Missing coverage: 12
- Direct repository conflict: 1

Priority distribution:

- P0 blocking/integrity: 15
- P1 core implementation: 34
- P2 interoperability/research depth: 6
- P3 optional: 0

These counts are an implementation audit, not a claim that a fixed percentage of the research is complete. A row is `existing_strong` only where a concrete repository artifact was observed; `existing_partial` means the concept exists but one or more requested contracts, tests, or evidence layers remain absent.

## What already exists and must be reused

1. **CPCS FACS–Laban package v1.2**: 90 reference records, 178 RAG records, reverse video analysis, Video Observation Graph, evidence classes, fight/UGC examples, schemas, scripts, tests, and round-trip design.
2. **CPCS-MX package v1.0**: 80-source index, canonical and authoring schemas, RAG corpus, profiles, deterministic compiler, observation merger, package validator, natural/UGC/staged-action/anime examples, and explicit project-synthesis disclaimers.
3. **Active lab control plane**: concept cards, retrieval script, blocks, variants, experiments, a derived knowledge graph, sync manager, root gate, and route-before-write governance.
4. **14-layer universal motion skeleton**: YAML intent, JSON canonical truth, XML ordered triggers, JSONL evidence, and dense media/array separation.
5. **Format-control map**: separates authoring responsibilities from the question of what is pasted into a model.

Creating the requested 70-plus-document tree without an overlap gate would duplicate these assets and violate the repository's one-concern/one-file and route-before-write laws.

## Highest-priority genuine gaps

### 1. Bartenieff connectivity

The six recognized Patterns of Total Body Connectivity are not searchable in the repository: Breath, Core-Distal, Head-Tail, Upper-Lower, Body-Half, and Cross-Lateral. They should be added as an established movement framework, while computational proxies such as phase lag, chain participation, contralateral coordination, and center-of-mass effects must be labeled as research-derived or project-specific.

### 2. Behavior Markup Language alignment

The repository has XML trigger tracks but no explicit BML treatment. Add a mapping for speech, gaze, gesture, posture, face, head, sync references, and realization layers. Do not claim BML compliance unless XML is validated against a verified BML specification/profile.

### 3. Normalized phase model with an explicit non-universality verdict

No single universal seven-phase scientific movement model was verified. Different domains use different abstractions: facial behavior commonly uses onset/apex/offset; gesture research uses preparation/stroke/optional holds/retraction; gait models use stance/swing or eight functional phases; BML commonly exposes seven synchronization points around six behavior phases. BML's seven sync points are not a universal movement ontology. The requested seven-stage model may be useful, but it must be named and versioned as a project-specific normalization with domain mappings and optional phase merges.

### 4. Five-way semantic-equivalence compiler and tests

The repository explains the roles of Markdown, YAML, XML, JSON, and JSONL, but a verified canonical-to-all-formats-to-canonical test suite was not found. Add semantic IDs, typed values, temporal order, provenance, confidence, and intentional-loss reports. Compare semantic hashes, not byte equality.

### 5. Closed-loop compliance verification

The repository designs re-extraction and comparison but marks full verification as unexplored. This is the highest-leverage engineering gap: authored score → render → re-extract → normalize → compare contact timing, action order, camera, identity drift, cuts, and support/foot slip.

### 6. Scene graph versus knowledge graph separation

The Video Observation Graph represents evidence about a scene. `lab/graph.json` represents concepts, sources, variants, experiments, and evidence. They need explicit bridge records, not a single merged node namespace.

## Important terminology corrections

- **FACS** is an anatomically grounded coding system for visible facial actions; it is not an emotion decoder. The proprietary manual should be cited, not reproduced.
- **Laban Effort numeric axes** such as `[-1,1]` are computational conventions unless a cited method defines the scale.
- **Bartenieff patterns** are a recognized framework, but pose-derived proxy metrics are not part of the original qualitative system.
- **BML seven sync points** (`start`, `ready`, `stroke-start`, `stroke`, `stroke-end`, `relax`, `end`) should not be relabeled as a universal seven-phase movement law.
- **CAU/CACS** should remain project-specific names, if used at all.
- **Affect** is an interpretation with evidence and uncertainty, not an objective fact inferred from movement.
- **JSONL** is a practical newline-delimited convention; RFC 8142 JSON text sequences are related but not identical. Name the chosen framing precisely.

## Recommended target architecture

```text
EXISTING FROZEN RESEARCH PACKAGES
  CPCS v1.2 + CPCS-MX v1.0 + RDC
                 |
                 v
ACTIVE LAB INTEGRATION LAYER
  concepts.jsonl / CONCEPT_INDEX / profiles / blocks / runbooks
                 |
                 +--> knowledge graph (repo retrieval/governance)
                 |
                 +--> canonical score + VOG (scene evidence/control)
                 |
                 v
DELTA MODULES
  Bartenieff connectivity
  BML/EmotionML alignment
  normalized phase profile
  semantic-equivalence compiler
  compliance verification
                 |
                 v
TARGET ADAPTERS + LOSS REPORTS
```

## Required execution modes

### Default: integration-first

Use existing active files and create the minimum new routed artifacts. Do not edit frozen package files. Add concepts, mappings, schemas, tests, and runbooks in `lab/`, regenerate derived graph state, and run the root gate.

### Exceptional: new frozen upstream package

Use only when the overlap audit demonstrates a genuinely independent research product. The owner must explicitly override the current frozen-research law; `AGENTS.md` must be updated in the same commit; the new package must include its own integrity manifest; and `sync_repo.py` must see aliases, concept cards, index coverage, and a regenerated graph.

## Blocking acceptance gates

1. No duplicate file or concept owner.
2. Every material research claim has a source ID or explicit synthesis label.
3. No project convention is presented as a standard.
4. Canonical JSON remains the single resolved semantic source of truth.
5. All serializers either preserve semantics or emit an explicit loss record.
6. Every derived claim has provenance, method, confidence, and alternatives where appropriate.
7. Every new runbook is routed; every new concept is retrievable; every derived graph is rebuilt.
8. Root validation gate exits zero after all final edits.
9. Git diff is clean of accidental generated/binary changes.
10. Remote branch SHA is verified against local SHA before success is reported.

## Full gap matrix

| ID | Area | Status | Priority | Gap/risk | Action |
|---|---|---|---|---|---|
| DMR-001 | Repository governance | existing_strong | P0 | None in capability; the uploaded task must obey rather than override it silently. | Make repository-law compliance the first hard gate. |
| DMR-002 | Target path | conflict | P0 | Blind creation under research/ violates the current directory contract and creates a fourth overlapping package. | Default to gap-first integration in lab/. Create a new frozen research package only through an explicit owner override and same-commit AGENTS.md update. |
| DMR-003 | Research package | existing_strong | P0 | Requested monograph substantially overlaps two existing packages. | Build a coverage/delta map and research only unsupported claims. |
| DMR-004 | RAG corpus | existing_strong | P1 | No unified delta corpus for newly added concepts. | Append concept cards and, only if justified, build a small additive delta corpus. |
| DMR-005 | Source catalog | existing_strong | P1 | New domains need source additions and claim-to-source coverage. | Add only missing sources and generate source-coverage reports. |
| DMR-006 | Canonical score | existing_strong | P0 | No reason to create a second root schema. | Extend by versioned optional modules or aligned properties; retain one authority per quantity. |
| DMR-007 | Authoring model | existing_strong | P1 | Missing explicit modules for Bartenieff and normalized phase semantics. | Add typed extensions to active lab/compiler layer. |
| DMR-008 | Observation records | existing_strong | P1 | Need new evidence types for connectivity and BML-aligned behavior. | Extend vocabularies without weakening provenance classes. |
| DMR-009 | Video Observation Graph | existing_strong | P1 | Need explicit alignment for new node/edge types and temporal relations. | Extend VOG schema or add a backward-compatible overlay. |
| DMR-010 | Knowledge graph | existing_strong | P0 | Uploaded specification conflates repo knowledge graph and scene graph. | Document and test the two-graph architecture; never merge their identities. |
| DMR-011 | FACS | existing_partial | P1 | Need a stronger computational event contract, visibility/unscorable states, and reliability/calibration guidance. | Add a FACS event profile and evidence-calibration tests; do not reproduce proprietary manual content. |
| DMR-012 | Facial dynamics | existing_partial | P1 | Numeric AU track remains untested and only partially implemented. | Implement and A/B-test AU spline track versus descriptive prose. |
| DMR-013 | Gaze/head/blink/breath | existing_partial | P1 | No unified BML-aligned synchronization contract. | Map gaze/head/blink/breath events to canonical sync anchors. |
| DMR-014 | Laban BESS | existing_partial | P1 | Effort/Shape are stronger than Body/Space/phrasing; numerical axes may look more authoritative than evidence permits. | Label qualitative canon versus project numeric proxies; complete Body/Space/phrasing definitions. |
| DMR-015 | Laban Effort vectors | existing_partial | P1 | Project convention exists but needs explicit source/proxy metadata and calibration. | Require convention_id, proxy_method, uncertainty, and mapping version. |
| DMR-016 | Bartenieff connectivity | missing | P0 | Major gap in full-body organization and propagation reasoning. | Add six recognized patterns, aliases, observable proxies, phase-lag/chain fields, caveats, and concept cards. |
| DMR-017 | Proximal-distal sequencing | existing_partial | P1 | Not formalized as reusable measured relations with lag/tolerance. | Add propagation graph and lag metrics linked to Bartenieff and kinematic tracks. |
| DMR-018 | Biomechanics frames | existing_strong | P1 | Need alignment documentation to ISB recommendations and projection uncertainty. | Add normative project frame registry and source alignment notes. |
| DMR-019 | Kinematics/dynamics | existing_partial | P1 | CoM/support/force evidence remains largely untested; derived quantities need method metadata. | Require authority/evidence_class/derivation_method for every derived track. |
| DMR-020 | Affect | existing_partial | P1 | No formal alignment with EmotionML; experienced versus displayed state needs broader examples. | Add EmotionML mapping and preserve interpretation/evidence separation. |
| DMR-021 | EmotionML alignment | missing | P2 | Missed interoperability opportunity. | Add optional EmotionML export/import adapter without claiming affect truth. |
| DMR-022 | Gesture phases | existing_partial | P1 | No explicit canonical alignment to gesture research/BML sync anchors. | Add domain phase profile and mapping table. |
| DMR-023 | Behavior Markup Language | missing | P0 | XML trigger design currently resembles BML but does not document compliance or mapping. | Implement BML alignment profile, namespace policy, and conformance disclaimer; do not claim BML compliance unless validated. |
| DMR-024 | Seven-phase abstraction | missing | P0 | No universal model established; risk of presenting synthesis as a standard. | Create a project-specific normalized phase profile with domain mappings and optional/merged phases. |
| DMR-025 | Universal phase claim | missing | P0 | Evidence across FACS, gesture, gait, BML, and animation uses different phase systems. | Record an explicit negative verification result: no single universal seven-phase scientific standard verified; distinguish BML seven sync points. |
| DMR-026 | Action ontology | existing_strong | P1 | Need named project-specific Screen Combat Action Ontology and tighter safety semantics. | Formalize existing atoms as project-specific ontology; avoid CAU/CACS standard claims. |
| DMR-027 | Multi-actor coordination | existing_partial | P1 | Need stronger role, target, dependency, and synchronization validation. | Add temporal constraint checks and actor-target reference integrity. |
| DMR-028 | Product handling contacts | missing | P1 | Floaty product handling remains an observed control gap. | Add product-contact ontology and one isolated A/B experiment. |
| DMR-029 | Locomotion | existing_partial | P2 | No comprehensive gait-phase profile or verification suite. | Add domain-specific locomotion profile; do not force seven-phase abstraction onto gait. |
| DMR-030 | Director controls | existing_strong | P1 | Need model capability adapters and perceptual-effect uncertainty. | Extend adapter capability matrix and loss reports. |
| DMR-031 | Animation/anime/VFX | existing_strong | P1 | Need tests that style transforms preserve motion invariants. | Add cross-style invariant and ablation tests. |
| DMR-032 | Marketing controls | existing_partial | P1 | Need evidence-backed audience hypotheses and stronger claim substantiation schema. | Require hypothesis/evidence/confidence and approved-claim IDs. |
| DMR-033 | Cultural/individual variation | existing_partial | P1 | Not yet enforced by schema or tests. | Add context qualifier and alternative-interpretation requirements for inferential claims. |
| DMR-034 | Observation vs inference | existing_strong | P0 | Need consistent use across new modules and prompts. | Reuse the existing evidence class enum everywhere. |
| DMR-035 | Markdown/CNL | existing_partial | P2 | No deterministic canonical Markdown serializer with loss report. | Add serializer only if canonical JSON remains source of truth. |
| DMR-036 | YAML | existing_strong | P1 | Implicit typing and merge behavior need explicit hardened policy. | Use safe_load, typed merge, restricted profile resolution, and canonical normalization. |
| DMR-037 | XML | existing_partial | P1 | No BML/EmotionML conformance mapping and no XSD for active envelope. | Add namespace-aware XML schema and import/export tests. |
| DMR-038 | JSON | existing_strong | P1 | Schema modularity/version migration needs hardening. | Use one canonical root with $defs/modules and migration tests. |
| DMR-039 | JSONL | existing_strong | P1 | Need canonical event-stream ordering and tombstone/correction semantics. | Define event envelope with record_type, revision, supersedes, source hash. |
| DMR-040 | Cross-format equivalence | missing | P0 | High-value missing test layer. | Build deterministic canonical->formats->canonical adapters and semantic hashes; report intentional losses. |
| DMR-041 | Format effects on LLMs | missing | P1 | Need model/task-specific evidence; no format is universally best. | Add empirical source review and local benchmark matrix; separate reasoning from serialization. |
| DMR-042 | Constrained decoding | existing_partial | P2 | Schema validation after generation is not equivalent to constrained decoding. | Add optional Outlines/LMFE/provider-native adapter and semantic validator. |
| DMR-043 | Explicit reasoning records | existing_partial | P1 | Need one shared transformation-record contract. | Add immutable transformation records and source/target hashes. |
| DMR-044 | Temporal causal graph | existing_partial | P1 | Need Allen-style interval relation validation and causal-evidence distinctions. | Add temporal relation validator and inferred-causality caveats. |
| DMR-045 | Ontology alignment | missing | P2 | Interoperability and graph validation are weaker than they could be. | Add optional alignment layer and SHACL shapes; keep canonical JSON independent. |
| DMR-046 | Provenance/confidence | existing_strong | P1 | Need claim-level citation coverage checks in new research docs. | Add source-ID linter and coverage threshold. |
| DMR-047 | Inter-rater reliability | missing | P2 | Manual coding quality cannot be evaluated reproducibly. | Add calibration set, coding guide, Cohen kappa/ICC guidance appropriate to variable type. |
| DMR-048 | Model capability negotiation | existing_partial | P1 | Current provider templates are intentionally not executable clients. | Create adapter contracts that are data-driven and version-pinned; avoid stale model claims. |
| DMR-049 | Prompt compression | existing_partial | P1 | No deterministic salience/loss scoring. | Add field-priority policy and machine-readable compression report. |
| DMR-050 | Examples | missing | P1 | Large duplication risk if written as nine monographs. | Create a compact fixture matrix generated from canonical JSON and reuse shared serializers. |
| DMR-051 | Acceptance tests | existing_partial | P0 | Missing cross-format, BML, Bartenieff, phase-profile, and claim-coverage tests. | Extend tests and root validation gate without slowing basic checks excessively. |
| DMR-052 | Round-trip verification | missing | P0 | Highest-leverage correctness gap. | Implement metric contract and at least one synthetic/authorized fixture before claiming closed loop. |
| DMR-053 | Security/parsing | existing_partial | P1 | New XML/Markdown/import paths expand attack surface. | Add defused XML or hardened parser policy, path allowlists, digest checks, untrusted-text separation. |
| DMR-054 | Ethics/rights | existing_strong | P0 | New modules must inherit, not restate inconsistently. | Reference one canonical policy and add domain-specific checks only. |
| DMR-055 | Git integration | existing_strong | P0 | Uploaded spec omits current control-plane-specific integration sequence. | Use one branch; update CHANGELOG; regenerate derived graph last; run gate after every final edit; push only green state. |

## Evidence base used for this audit

Repository evidence was taken from the current `main` branch artifacts listed above. External seed sources are recorded in `07_SOURCE_SEED_CATALOG.csv`; they include official FACS/Laban pages, Hackney's foundational Bartenieff book listing, foundational BML papers/specification material, W3C EmotionML/PROV-O/SHACL/Time, IETF/W3C serialization standards, and empirical structured-output papers. The seed catalog is not a finished bibliography: the executing research agent must verify version, status, access date, and the exact claims supported before adding a source to the repository.
