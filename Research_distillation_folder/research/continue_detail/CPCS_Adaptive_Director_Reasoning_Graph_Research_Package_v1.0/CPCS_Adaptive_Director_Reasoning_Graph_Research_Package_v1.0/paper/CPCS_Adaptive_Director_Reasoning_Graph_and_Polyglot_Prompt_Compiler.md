---
title: "From Prompt Chains to Director Graphs"
subtitle: "An Adaptive Reasoning Control Plane, Graph-RAG Extension, and Polyglot Prompt Compiler for AI Video Generation"
short_title: "CPCS ADRG Research Paper"
document_id: "CPCS-ADRG-RP-2026-01"
version: "1.0"
date: "2026-07-23"
literature_cutoff: "2026-07-23"
status: "Research synthesis and testable systems proposal"
author: "OpenAI"
language: "en"
citation_style: "author-year with stable source identifiers"
framework_name: "Adaptive Director Reasoning Graph"
framework_acronym: "ADRG"
parent_framework: "Cinematic Performance Control Score (CPCS)"
rag_ready: true
rag_chunking:
  preferred_strategy: "marker-and-heading-aware semantic chunking"
  target_chunk_tokens: 650
  maximum_chunk_tokens: 950
  overlap_tokens: 90
  preserve_code_blocks: true
  preserve_tables: true
  retain_heading_path: true
  exclude_sections:
    - "Full Reference List"
    - "Document Change Log"
knowledge_domains:
  - ai_video_generation
  - prompt_compilation
  - graph_of_thoughts
  - tree_of_thoughts
  - chain_of_thought
  - model_scaled_reasoning
  - retrieval_augmented_generation
  - graph_rag
  - structured_prompt_languages
  - yaml
  - json
  - xml
  - compiler_intermediate_representations
  - constrained_generation
  - variant_search
  - provenance
  - verification
keywords:
  - ADRG
  - CPCS
  - director reasoning graph
  - reasoning control plane
  - model-adaptive reasoning
  - mini language models
  - large language models
  - Chain of Thought
  - Tree of Thoughts
  - Graph of Thoughts
  - Chain of Draft
  - RAG
  - GraphRAG
  - YAML
  - JSON
  - XML
  - JSONL
  - prompt compiler
  - decision ledger
  - variant lattice
  - semantic ownership
  - compilation loss
license_note: "This document synthesizes cited research and proposes a new engineering architecture. Proposed defaults require empirical calibration in the target repository and model stack."
---

<!-- RAG_DOC_SUMMARY: This paper extends CPCS with an Adaptive Director Reasoning Graph (ADRG): a model-scaled reasoning control plane that separates knowledge retrieval, creative planning, canonical video controls, target compilation, and verification. It argues that GoT is useful as an orchestration abstraction for dependency-rich directing, but not as a universal prompting instruction. Mini models should use fixed, narrow decision graphs, strict schemas, concise decision records, and external validators; larger models may use selective ToT branching, graph aggregation, self-consistency, and specialist critics. The paper defines typed nodes and edges, a reasoning router, a constrained variant lattice, graph-aware RAG, a no-raw-CoT decision ledger, and language ownership contracts for natural language, YAML, JSON, XML, and JSONL. It supplies repository-integration rules, schemas, examples, RAG records, proposed concept cards, and deterministic validation checkpoints. -->

<a id="adrg-abstract"></a>
# From Prompt Chains to Director Graphs

## Abstract

AI video prompting is increasingly treated as a directing problem, but most prompt systems still compress intention, performance, motion, camera, style, model capabilities, and validation into one untyped text block. The existing Cinematic Performance Control Score (CPCS) architecture improves this by separating natural-language intent from structured controls and by compiling YAML, JSON, XML, and media assets into target-specific packages. The next architectural problem is not another video-control vocabulary. It is the control of the planner itself: how a language model retrieves concepts, decomposes a request, explores alternatives, chooses a treatment, preserves invariants, compiles across formats, and exposes losses and uncertainties without turning an unverifiable chain of thought into production data.

This paper proposes the **Adaptive Director Reasoning Graph (ADRG)**, a model-agnostic reasoning control plane that sits above the CPCS authoring and compilation stack. ADRG represents planning as typed nodes and edges rather than one long reasoning transcript. It distinguishes five graph planes: knowledge and evidence, scene intent and controls, reasoning execution, compilation and realization, and verification and experiments. A director request is decomposed into bounded subproblems; relevant concept cards, templates, failures, and model capabilities are retrieved; branches are created only for high-impact uncertain decisions; alternatives are scored against explicit criteria; the selected plan is compiled into the canonical CPCS score; and independent validators test structure, constraints, timing, authority, and output compliance.

The central claim is deliberately narrower than “Graph of Thoughts is best.” Chain-of-Thought can improve reasoning in sufficiently large models, Tree-of-Thoughts supports deliberate branch search, Graph-of-Thoughts supports dependency-rich aggregation, ReAct links planning with external evidence, and program-aided methods transfer deterministic work to runtimes. These methods solve different problems and have different costs. Mini or small models often benefit more from fixed decomposition, constrained output, retrieved exemplars, and distilled concise decision patterns than from broad, free-form search. Large models can justify wider branching, specialist critics, and graph synthesis, but should still produce auditable decision records rather than raw private reasoning. The routing decision must therefore depend on impact, uncertainty, coupling, reversibility, model capability, context budget, and the cost of generation.

The paper also defines a **polyglot prompt compiler contract**. Natural language owns intention, audience effect, observable behavior, and priority. YAML owns human-authored configuration, reusable profiles, reasoning policy, and overrides. JSON owns the fully resolved canonical graph, exact arrays, schemas, patches, model capability profiles, and compile reports. XML owns ordered narrative, mixed content, and namespaced event envelopes. JSONL owns append-only RAG, decision, evidence, experiment, and verification records. Dual-format prompting is supported only when each format has a declared ownership boundary; two formats may not silently claim authority over the same semantic path.

ADRG is presented as a falsifiable systems proposal. The package accompanying this paper includes a heading-aware RAG corpus, a JSON Schema for the reasoning graph, model-policy examples, dual-format examples, proposed concept cards for the repository, an integration plan, and validation scripts. The intended outcome is not longer prompts. It is higher information preservation per token, more deliberate variation, better use of both mini and large models, explicit compilation loss, and a graph that can explain how a concept became a prompt, a control asset, a variant, and eventually a measured render result.

**Keywords:** adaptive reasoning; director graph; model-scaled planning; Chain-of-Thought; Tree-of-Thoughts; Graph-of-Thoughts; Chain-of-Draft; RAG; GraphRAG; AI video; prompt compiler; YAML; JSON; XML; JSONL; structured output; provenance; variant search; verification.

---

<!-- RAG_CHUNK id="adrg.00" title="Evidence and terminology legend" concepts="evidence labels, ADRG, reasoning record, raw chain of thought, compiler" -->
<a id="adrg-evidence-legend"></a>
## Evidence and Terminology Legend

This paper keeps published findings, repository observations, and new design choices separate.

| Label | Meaning |
|---|---|
| **[ESTABLISHED]** | A published method, standard, or repeatable repository fact supported by the cited source. |
| **[EMERGING]** | A recent preprint or direction whose generality has not been established across models and tasks. |
| **[PROPOSED]** | A new ADRG architecture, field, policy, heuristic, or default introduced in this paper. |
| **[OPERATIONALIZATION]** | A computable proxy for a qualitative construct; it requires calibration and must not be treated as the construct itself. |
| **[PROJECT-OBSERVED]** | A behavior or result recorded in the target repository, not a universal scientific finding. |
| **[CAUTION]** | A limitation, uncertainty, rights constraint, security issue, or likely misuse. |

The term **reasoning** is used at three levels. First, a model may perform internal computation that is not directly observable. Second, a model may emit intermediate text commonly called a chain of thought. Third, a production system may record an external, typed sequence of tasks, evidence, choices, and validations. ADRG is concerned primarily with the third level. Published work shows that emitted chains can improve performance in some settings [S001], but they are not guaranteed to be faithful explanations of the mechanism that produced the answer [S009, S010]. ADRG therefore does not define raw chain-of-thought text as a source of truth.

A **decision record** is a concise, externally auditable object containing the decision question, alternatives considered, criteria, scores or constraints, selected option, evidence references, confidence, and known loss. It is not a transcript of hidden reasoning. A **reasoning graph** is the executable dependency graph of tasks and decisions. A **scene control graph** is the canonical video-control structure that contains beats, affect, face, movement, contact, camera, sound, VFX, marketing, rights, and validation targets. These graphs may reference each other but are not interchangeable.

The target repository already treats `lab/graph.json` as a deterministic derived artifact built from concept cards, blocks, patterns, variants, experiments, runs, and research packages [S038]. ADRG extends the source vocabulary and builder inputs; it does not authorize hand-editing the derived graph. The repository also requires research packages to be integrated through aliases, concept cards, index updates, graph rebuilding, and validation [S036].

---

<!-- RAG_CHUNK id="adrg.01" title="Executive thesis" concepts="reasoning control plane, directing, compilation, graph orchestration" -->
<a id="adrg-executive-thesis"></a>
# 1. Executive Thesis

A video-prompt model should not be instructed merely to “think like a director.” That phrase is too broad to define what the model should retrieve, which departments it should coordinate, where it may branch, how it should compare alternatives, what must remain invariant, or how its plan becomes executable controls. A production-grade system requires a **reasoning control plane** above the existing video-control plane.

The proposed architecture is:

```text
human request / screenplay / reference analysis
                    │
                    ▼
       Adaptive Director Reasoning Graph
  retrieve → decompose → branch selectively → choose
  → compile plan → report uncertainty and loss
                    │
                    ▼
      CPCS Authoring Source Layer (ASL)
  natural language + YAML + XML + measured JSON tracks
                    │
                    ▼
      Canonical Intermediate Representation (CIR)
 fully resolved, typed, unit-normalized canonical JSON
                    │
                    ▼
         Target Execution Package (TEP)
 prompt + API fields + images/video/pose/audio/control assets
                    │
                    ▼
      Verification Evidence Records (VER/JSONL)
 metrics + violations + decisions + provenance + render results
```

**[PROPOSED]** ADRG does not replace CPCS. It answers a different question. CPCS specifies **what the shot should contain and how it should be controlled**. ADRG specifies **how the planner should arrive at, compare, compile, and verify those controls**.

The architecture is built on five principles.

1. **Reasoning strategy is routed, not globally fixed.** CoT, least-to-most, ToT, GoT, ReAct, program-aided execution, self-consistency, and critique are available operators. The system chooses the smallest operator that matches the decision.
2. **Model scale changes the control policy.** A mini model receives a narrow graph, strong retrieval, explicit schemas, one responsibility per call, and deterministic validation. A larger model may coordinate a wider graph and compare more alternatives, but it remains bounded by schemas, budgets, and evidence.
3. **No raw reasoning transcript becomes canonical data.** Production stores decision records, dependencies, evidence, scores, and tests. This avoids confusing plausible explanations with verified causes [S009, S010].
4. **One semantic ontology supports multiple serializations.** Natural language, YAML, JSON, XML, and JSONL are carriers with different ownership. They are not competing truths.
5. **Every compilation step has a loss account.** A control is reported as preserved, transformed, approximated, compressed to text, baked into a reference, retained for evaluation, dropped under policy, or rejected.

The result is closer to a compiler and test harness than to a prompt trick. The goal is to maximize **useful controlled information per token and per generation**, not the apparent sophistication or length of the model’s reasoning.

---

<!-- RAG_CHUNK id="adrg.02" title="Repository baseline and architectural gap" concepts="existing graph, concept cards, CPCS, control surface, gap analysis" -->
<a id="adrg-repository-baseline"></a>
# 2. Repository Baseline and the Missing Layer

## 2.1 Existing Strengths

The target repository already contains several architectural decisions that ADRG should preserve.

- `lab/concepts.jsonl` stores compact concept cards with natural-language triggers, pairings, conflicts, evidence, source pointers, status, and layer [S037].
- `lab/scripts/build_graph.py` deterministically derives `lab/graph.json` from concept cards, blocks, registry entries, run evidence, and research-package presence [S038].
- `lab/CONTROL_SURFACE.md` separates descriptive prose for look and feel from numeric canonical truth for precise motion, contact, timing, and camera [S039].
- `lab/FORMAT_CONTROL_MAP.md` assigns human-readable intent and profiles to YAML, exact canonical data to JSON, ordered mixed content and triggers to XML, and evidence streams to JSONL [S040].
- The CPCS paper already defines ASL, CIR, TEP, VER, typed merge behavior, capability negotiation, compilation loss, RAG objects, and model adapters [S041].
- The lab operating procedure separates authoring, compiler, and verifier roles and requires isolated A/B tests before confidence is increased [S042].

These are not small foundations. They mean the repository does not need a second prompt-format doctrine or a second canonical video schema. It needs a way to connect the existing concepts into a **planner execution graph**.

## 2.2 What the Current Graph Does Not Yet Represent

The current graph can answer questions such as:

- Which concept pairs with `c_contact_solver`?
- Which run supports a block?
- Which research package sourced a concept?
- Which technique conflicts with loose UGC performance?
- Which node belongs to the camera or action layer?

It does not yet represent, as first-class data:

- which subproblem was created from a director request;
- which retrieval query supported that subproblem;
- which candidate treatments were proposed;
- why one candidate was selected over another;
- which model class and token budget were used;
- which controls were preserved or lost during compilation;
- which validator rejected an output and which repair followed;
- how a successful reasoning policy performed across models;
- which variation axes were intentionally changed and which invariants were protected.

Without these objects, the graph stores knowledge but not the **causal execution trace of design and compilation**. The model may produce a good prompt, but the repository cannot yet distinguish whether the improvement came from retrieval, decomposition, branching, format packaging, a model-specific capability, or chance.

## 2.3 The Architectural Boundary

**[PROPOSED]** ADRG adds new source records and edge types, then projects them into the existing derived graph. It should not place ephemeral token-by-token model thoughts into `lab/graph.json`. Instead it should add durable records only when they are useful for retrieval, compilation, debugging, or experiments.

Durable records include:

- reasoning policies;
- decision templates;
- model capability profiles;
- variant axes;
- compile-loss rules;
- failure and repair cards;
- experiment results that compare reasoning modes;
- selected decision summaries for a specific build.

Ephemeral scratch work remains outside the knowledge graph and may be discarded after the decision record is emitted.

---

<!-- RAG_CHUNK id="adrg.03" title="Reasoning methods as operators" concepts="CoT, least-to-most, ToT, GoT, ReAct, self-consistency, program-aided reasoning" -->
<a id="adrg-reasoning-operators"></a>
# 3. Reasoning Methods as Operators, Not Ideologies

## 3.1 Chain-of-Thought as Local Decomposition

**[ESTABLISHED]** Chain-of-Thought prompting can improve performance on multi-step reasoning tasks for sufficiently large language models [S001]. For video-prompt planning, its most defensible role is local decomposition inside a bounded node:

```text
emotional objective
→ observable facial behavior
→ gaze and head behavior
→ body organization
→ timing and visibility requirement
```

CoT is weak as the only production architecture because it usually follows one linear path. Early assumptions can propagate, several departments can become entangled, and the output often lacks explicit branch comparison or dependency management.

## 3.2 Least-to-Most as a Reliable Default Decomposer

**[ESTABLISHED]** Least-to-most prompting decomposes a difficult task into simpler subproblems and solves them sequentially [S003]. This is particularly useful for mini and mid-sized models because the decomposition can be externally fixed:

```text
1. identify shot intent and hard constraints
2. identify actors, objects, and timebase
3. retrieve relevant concepts and failures
4. produce one scene-control plan
5. compile to the requested format
6. validate and repair
```

The planner does not need to invent an entire graph. It fills a known graph template. This reduces output entropy and makes failures localizable.

## 3.3 Tree-of-Thoughts as Selective Creative Search

**[ESTABLISHED]** Tree-of-Thoughts explores multiple coherent candidate paths, evaluates them, and can backtrack [S004]. In ADRG, ToT is used only at branch points where alternatives materially change audience experience or generation reliability, such as:

- handheld close-up versus composed tracking medium;
- concealed fear versus overt fear;
- single continuous shot versus beat-per-clip construction;
- semantic prompt-only execution versus pose-conditioned execution;
- raw UGC capture versus polished cinematic treatment.

Branching every field creates combinatorial waste and inconsistent plans. A shot does not need three alternatives for a fixed frame rate or an approved product asset. ADRG branches on **high-impact uncertainty**, not on every possible adjective.

## 3.4 Graph-of-Thoughts as Orchestration

**[ESTABLISHED]** Graph-of-Thoughts generalizes linear and tree reasoning by allowing arbitrary dependency and aggregation relationships between units [S005]. Film direction is dependency-rich: performance affects framing, action timing affects contacts and camera motion, marketing visibility affects blocking, and model capability affects which controls can be realized. GoT is therefore useful as the **orchestration abstraction** for the full planner.

However, “use GoT” is not a complete implementation. The graph still needs typed nodes, permitted edges, budgets, authority, selection rules, and validators. A mini model should not be asked to free-form an arbitrary graph. It should traverse a fixed or partially fixed graph compiled by the application.

## 3.5 ReAct and Program-Aided Execution

**[ESTABLISHED]** ReAct interleaves reasoning and actions against external sources or environments [S006]. For this repository, actions include concept retrieval, schema lookup, model-capability lookup, graph traversal, prompt compilation, file validation, and render-metric extraction. The model should not guess whether a concept exists, whether a JSON path is valid, or whether a generated XML document is well formed when tools can answer those questions.

Program-of-Thoughts and Program-Aided Language Models separate semantic decomposition from deterministic computation [S016, S017]. ADRG applies the same principle to video prompting:

- the model chooses or proposes a beat structure;
- code verifies frame sums, time ordering, references, graph cycles, hashes, and schema conformance;
- the model interprets validator errors and proposes a repair;
- code applies and rechecks the repair.

## 3.6 Self-Consistency and Critique

**[ESTABLISHED]** Self-consistency samples multiple reasoning paths and selects the most consistent answer [S002]. It is useful for high-impact decisions with an objective or semi-objective score. It is wasteful when a deterministic compiler can validate one answer.

Self-Refine shows that iterative feedback can improve generated outputs in many tasks [S007], but intrinsic self-correction without external feedback can fail or degrade reasoning [S008]. ADRG therefore distinguishes:

- **intrinsic critique:** useful for style, clarity, and alternative wording;
- **external validation:** required for schema, timing, graph integrity, reference resolution, capability support, and hard constraints;
- **render evidence:** required to claim that a prompting or reasoning choice improves video output.

## 3.7 Concise Reasoning for Cost Control

**[EMERGING]** Chain-of-Draft reports that concise intermediate drafts can preserve task performance while reducing tokens in evaluated settings [S013]. Recent work also studies disciplined or depth-sensitive reasoning rather than treating longer output as automatically better [S014, S015]. These findings should not be generalized to every video-planning task, but they support a practical rule: allocate reasoning by **decision value**, not by verbosity.

---

<!-- RAG_CHUNK id="adrg.04" title="Why raw chain of thought is not a production artifact" concepts="faithfulness, decision ledger, auditability, external verification" -->
<a id="adrg-decision-ledger"></a>
# 4. Why Raw Chain-of-Thought Is Not the Production Artifact

## 4.1 Performance Benefit Does Not Equal Faithful Explanation

Published evidence shows two facts that must be held together. Intermediate reasoning text can improve task performance [S001], and that text can be unfaithful or weakly coupled to the true basis of the answer [S009, S010]. A plausible narrative explaining why a camera treatment was selected is not proof that the treatment was actually selected for those reasons.

For a repository that learns from experiments, storing raw model rationales as evidence creates three risks:

1. **False provenance:** an eloquent explanation may be treated as the cause of a successful render.
2. **Retrieval contamination:** later models may retrieve speculative reasoning as if it were validated doctrine.
3. **Token and privacy overhead:** long scratchpads consume storage and may expose irrelevant or sensitive intermediate content.

## 4.2 Decision Ledger Contract

**[PROPOSED]** ADRG stores a compact decision ledger:

```json
{
  "decision_id": "dec.shot07.camera_treatment",
  "question": "Which camera treatment best communicates controlled mastery?",
  "alternatives": [
    "handheld_close",
    "low_medium_tracking",
    "telephoto_observer"
  ],
  "criteria": [
    "action_readability",
    "gauntlet_visibility",
    "generation_reliability",
    "continuity"
  ],
  "scores": {
    "handheld_close": [0.62, 0.70, 0.58, 0.64],
    "low_medium_tracking": [0.90, 0.88, 0.81, 0.86],
    "telephoto_observer": [0.74, 0.65, 0.78, 0.82]
  },
  "selected": "low_medium_tracking",
  "evidence_refs": ["c_perceptual_constraints", "profile://camera/impact_readability_v1"],
  "assumptions": ["single actor remains unobstructed"],
  "confidence": 0.81,
  "unresolved": ["target model camera adherence is not yet measured"],
  "loss": []
}
```

The scores are not presented as psychological truth. They are decision-support values under a declared rubric. The record can be compared with later render outcomes.

## 4.3 What May Be Retained

A durable reasoning record may retain:

- task decomposition;
- retrieved object IDs;
- accepted and rejected controls;
- branch labels;
- selection criteria and normalized scores;
- assumptions and unresolved questions;
- compiler transformations;
- validation errors and repairs;
- model, prompt, schema, and source hashes;
- measured output metrics.

It should not claim to expose the model’s hidden internal process. The practical target is **auditability of the system workflow**, not mind reading.

---

<!-- RAG_CHUNK id="adrg.05" title="Adaptive Director Reasoning Graph architecture" concepts="ADRG, planner graph, canonical score, execution trace" -->
<a id="adrg-architecture"></a>
# 5. Adaptive Director Reasoning Graph Architecture

## 5.1 Definition

**[PROPOSED]** An Adaptive Director Reasoning Graph is a typed, versioned directed multigraph:

\[
G_R = (V_R, E_R, P, B, A),
\]

where:

- \(V_R\) is the set of reasoning nodes;
- \(E_R\) is the set of typed dependency, evidence, conflict, selection, and compilation edges;
- \(P\) is the model and project policy;
- \(B\) is the resource budget;
- \(A\) is the set of acceptance conditions.

The graph may contain cycles only in explicitly bounded feedback loops such as `validate → repair → revalidate`. The dependency subgraph used for compilation must be acyclic.

## 5.2 Input Contract

The planner receives:

```yaml
request:
  id: "shot07"
  intent: "communicate controlled mastery, not rage"
  audience_takeaway: "precision is chosen"
  duration_s: 5.0
  target_model_profile: "adapter://vendor/model@verified-date"
  requested_outputs:
    - canonical_json
    - xml_director_envelope
    - compiled_natural_language
  hard_invariants:
    - "one staged near-contact strike"
    - "signature gauntlet visible at action apex"
    - "identity remains stable"
  variation_axes:
    - camera_treatment
    - performance_intensity
  evidence_policy: "project_evidence_then_primary_research"
```

The input specifies what may vary and what may not. Without this separation, “make variants” can accidentally change the story, product, action identity, or safety class.

## 5.3 Output Contract

ADRG returns four distinct artifacts:

1. **Reasoning graph:** tasks, retrieval, branches, decisions, dependencies, and validation events.
2. **Decision ledger:** compact auditable summaries for selected decisions.
3. **Canonical scene-control proposal:** CPCS-compatible data ready for the deterministic compiler.
4. **Compile and loss report:** how each requested control will reach the target model or why it cannot.

The final video prompt is only one compiled projection. It is never the sole source of truth.

## 5.4 Execution Phases

```text
Phase 0  normalize request and identify authority
Phase 1  classify domain, control paradigm, and risk
Phase 2  decompose into bounded directing subproblems
Phase 3  retrieve concept bundles, templates, failures, and capabilities
Phase 4  construct dependency graph and detect missing coverage
Phase 5  branch selectively at high-value decisions
Phase 6  score, prune, and choose a coherent treatment
Phase 7  compile treatment into CPCS authoring and canonical forms
Phase 8  negotiate model capabilities and produce target package
Phase 9  validate structure, semantics, constraints, and loss budget
Phase 10 generate candidates, measure outputs, and update evidence
```

A small model may execute each phase as a separate schema-constrained call. A large model may execute several phases together, but the emitted artifacts remain identical.

---
<!-- RAG_CHUNK id="adrg.06" title="Five graph planes" concepts="knowledge graph, scene control graph, reasoning graph, compilation graph, experiment graph" -->
<a id="adrg-five-planes"></a>
# 6. Five Graph Planes

A single undifferentiated graph is easy to build and difficult to govern. ADRG separates five planes, then permits a derived union graph for retrieval and visualization.

## 6.1 Plane A: Knowledge and Evidence

This is the repository’s durable concept graph. It contains:

- concept cards;
- evidence cards and source records;
- prompt blocks and profiles;
- performance and shot templates;
- failure and repair cards;
- model capability profiles;
- compiler rules;
- experiment findings.

Typical edges are `pairs_with`, `conflicts_with`, `supported_by`, `sourced_from`, `requires`, `mitigates`, and `applies_to`. This plane answers **what is known or proposed**.

## 6.2 Plane B: Scene Intent and Control

This plane contains the planned video itself:

- narrative beats;
- actor objectives and subtext;
- experienced and displayed affect;
- facial, gaze, body, Laban, action, contact, and camera controls;
- sound, VFX, editing, marketing, rights, and safety controls;
- temporal and spatial relationships;
- protected invariants.

Typical edges are `precedes`, `overlaps`, `triggers`, `targets`, `contacts`, `observed_by`, `must_preserve`, and `synchronizes_with`. This plane answers **what the shot means and does**.

## 6.3 Plane C: Reasoning Execution

This plane contains the planner workflow:

- task nodes;
- retrieval queries and result sets;
- candidate treatments;
- decision nodes;
- branch and merge nodes;
- critic and validator nodes;
- repair nodes;
- budget and model-policy nodes.

Typical edges are `decomposes_to`, `depends_on`, `proposes`, `grounds`, `selected_over`, `rejected_because`, `validated_by`, and `repaired_by`. This plane answers **how the plan was selected**.

## 6.4 Plane D: Compilation and Realization

This plane connects semantic controls to executable artifacts:

- ASL documents;
- canonical JSON paths;
- prompt clauses;
- API parameters;
- keyframes, poses, masks, depth, audio, camera tracks, and edit assets;
- adapter mappings;
- compile-loss records.

Typical edges are `compiled_to`, `approximated_by`, `baked_into`, `compressed_to_text`, `retained_for_evaluation`, `dropped_under_policy`, and `unsupported_by`. This plane answers **how intent reaches a target**.

## 6.5 Plane E: Verification and Experiments

This plane contains:

- schema results;
- semantic violations;
- rendered candidates;
- metric records;
- human reviews;
- A/B experiments;
- promoted or demoted patterns;
- causal confidence.

Typical edges are `measured_by`, `passes`, `fails`, `compared_with`, `supports`, `contradicts`, and `promotes`. This plane answers **what actually worked**.

## 6.6 Cross-Plane Invariants

**[PROPOSED]** The following invariants keep the planes coherent:

1. Every scene-control node created from retrieval links back to one or more knowledge objects or is marked `authored_without_retrieval`.
2. Every selected candidate has a decision record.
3. Every canonical control has a compilation status for each target adapter.
4. Every hard control that cannot be realized causes an error or an approved policy exception.
5. Every empirical claim links to an experiment or run; literature support alone does not prove a target-model effect.
6. Every derived graph node has a source record; the derived graph is not edited manually.

---

<!-- RAG_CHUNK id="adrg.07" title="Typed node ontology" concepts="node types, task, candidate, decision, validation, provenance" -->
<a id="adrg-node-ontology"></a>
# 7. Typed Node Ontology

## 7.1 Core Node Envelope

Every reasoning node uses a common envelope:

```json
{
  "id": "node.unique.id",
  "type": "decision",
  "plane": "reasoning_execution",
  "title": "Select camera treatment",
  "status": "resolved",
  "scope": {
    "project": "gameLaunch",
    "sequence": "teaser",
    "shot": "shot07",
    "beat": null
  },
  "authority": "director_approved",
  "confidence": 0.81,
  "inputs": ["cand.camera.handheld", "cand.camera.tracking"],
  "outputs": ["control.camera.treatment"],
  "evidence_refs": ["c_perceptual_constraints"],
  "provenance": {
    "model_profile": "planner.large.v1",
    "prompt_digest": "sha256:...",
    "created_at": "2026-07-23T00:00:00Z"
  },
  "acceptance": {
    "required": true,
    "validator_ids": ["val.camera.coverage"]
  }
}
```

The envelope intentionally resembles compiler intermediate data. It is not optimized for literary readability.

## 7.2 Node Types

### Goal

A user or project objective. Examples: “read as raw UGC,” “communicate concealed fear,” “preserve choreography while switching to anime presentation.”

### Constraint

A hard, soft, or perceptual requirement. Examples: “no cut,” “product visible before 3 seconds,” “strike remains staged near-contact,” “pose silhouette readable.”

### Question

A bounded decision problem. Examples: “which shot size reveals subtle facial leakage?” or “which execution carrier can preserve exact contact timing?”

### Retrieval Query

A structured query with filters, semantic text, graph-expansion policy, and expected object types.

### Evidence Result

A retrieved concept, source, experiment, failure card, or model capability record with score and provenance.

### Candidate

A proposed value, treatment, template composition, or execution path. Candidates must declare what they change and what they preserve.

### Decision

A selected candidate plus criteria, comparison, assumptions, confidence, and unresolved risk.

### Transform

A deterministic or model-mediated operation, such as `affect_to_performance`, `yaml_to_canonical_json`, `cpcs_to_prompt_text`, or `control_to_reference_keyframe`.

### Compile Mapping

A field-level mapping from canonical control to target channel, with realization status and information loss.

### Validation

A test definition and result. Tests may be syntactic, structural, semantic, physical, perceptual, rights-related, or empirical.

### Failure

A known or observed violation with detector, likely cause, affected controls, and severity.

### Repair

A proposed or applied change linked to the failure and followed by revalidation.

### Metric and Experiment

A measured outcome, comparison, or evidence update. These nodes are the only basis for promoting a repository pattern from unexplored to supported.

## 7.3 Status Vocabulary

Recommended statuses are:

```text
planned → ready → running → resolved
                  ↘ blocked
                  ↘ failed → repaired → revalidated
                  ↘ superseded
```

Status transitions should be event records, not silent overwrites, when the graph is used for production audit.

---

<!-- RAG_CHUNK id="adrg.08" title="Typed edge ontology" concepts="edge types, graph semantics, conflict, selection, compilation loss" -->
<a id="adrg-edge-ontology"></a>
# 8. Typed Edge Ontology

Edges carry semantics that generic `related_to` links cannot provide.

## 8.1 Knowledge Edges

| Edge | Meaning |
|---|---|
| `pairs_with` | Two concepts are usually composed together. |
| `conflicts_with` | Concepts or controls are incompatible under stated conditions. |
| `supported_by` | A claim or pattern is supported by evidence. |
| `contradicted_by` | Evidence weakens or reverses a claim. |
| `sourced_from` | A node was extracted or proposed from a document. |
| `alias_of` | Two retrieval terms resolve to one canonical concept. |
| `specializes` | A child concept narrows a parent concept. |

## 8.2 Reasoning Edges

| Edge | Meaning |
|---|---|
| `decomposes_to` | A task is split into a bounded subtask. |
| `depends_on` | A node cannot resolve until another node resolves. |
| `grounds` | Retrieved evidence supports a candidate or decision. |
| `proposes` | A planner or template creates a candidate. |
| `variant_of` | A candidate changes declared axes relative to a parent. |
| `selected_over` | A decision chooses one candidate over another. |
| `rejected_because` | A candidate failed a criterion or constraint. |
| `aggregates` | Several compatible nodes are combined into one plan. |
| `requires_tool` | Resolution depends on an external parser, solver, retriever, or metric. |

## 8.3 Scene and Temporal Edges

| Edge | Meaning |
|---|---|
| `precedes` | One event must occur before another. |
| `overlaps` | Intervals overlap intentionally. |
| `triggers` | An event initiates another control or effect. |
| `synchronizes_with` | Events share a timing landmark or tolerance. |
| `targets` | An action, gaze, camera, or effect is directed toward an entity. |
| `contacts` | Regions establish typed physical contact. |
| `observed_by` | A camera or viewer perspective presents a control. |
| `preserves` | A transform must retain an invariant. |

## 8.4 Compilation Edges

| Edge | Meaning |
|---|---|
| `compiled_to` | A semantic control maps to a target artifact or field. |
| `native_exact` | Target channel matches the control semantics. |
| `native_approximate` | Target channel is similar but not equivalent. |
| `baked_into_reference` | Control is rendered into media supplied to the model. |
| `compressed_to_text` | Control is summarized in prompt language. |
| `postprocess_only` | Control is applied after generation. |
| `evaluation_only` | Control can be measured but not supplied to the model. |
| `dropped_with_warning` | A permitted soft control is omitted. |
| `unsupported_error` | A required control cannot be realized. |

## 8.5 Validation Edges

| Edge | Meaning |
|---|---|
| `validated_by` | A node has a test or validator. |
| `passes` / `fails` | A result satisfies or violates a test. |
| `caused_by` | A failure is attributed to a supported cause hypothesis. |
| `mitigated_by` | A repair or concept addresses a failure. |
| `repaired_by` | A concrete repair was applied. |
| `revalidated_by` | The repaired result was tested again. |

## 8.6 Edge Constraints

**[PROPOSED]** The graph schema should enforce or semantically validate:

- no dangling endpoints;
- unique edge IDs;
- no `selected_over` edge without a decision node;
- no `compiled_to` edge without a target adapter or artifact;
- no `supported_by` edge to an unresolved evidence ID;
- no cycle in the strict `depends_on` subgraph;
- bounded cycles for repair loops;
- no hard conflict silently resolved by declaration order.

---

<!-- RAG_CHUNK id="adrg.09" title="Model-scaled reasoning policy" concepts="mini models, large models, reasoning budget, branching, schema adherence" -->
<a id="adrg-model-scaled-policy"></a>
# 9. Model-Scaled Reasoning Policy

## 9.1 Why One Prompting Policy Is Insufficient

CoT gains were originally associated with sufficiently large models [S001]. Smaller models can benefit from distilled rationales and structured supervision [S011, S012], but that does not imply they should perform wide free-form search at inference time. Token budget, instruction following, context retention, and schema adherence vary by model. ADRG therefore uses a versioned **planner capability profile**.

## 9.2 Capability Profile

```yaml
planner_profile:
  id: "planner.mini.strict.v1"
  verified_on: "2026-07-23"
  model_class: "mini"
  capabilities:
    long_context_retrieval: "limited"
    structured_output: "moderate"
    multi_branch_search: "limited"
    tool_use: "available"
    self_critique: "weak_without_external_feedback"
  budgets:
    maximum_context_tokens: 16000
    maximum_output_tokens: 1800
    retrieval_top_k: 4
    branch_width: 2
    branch_depth: 1
    critic_passes: 1
  policies:
    decomposition: "fixed_dag"
    decision_record: "compact"
    structured_output: "schema_constrained"
    invalid_output: "repair_once_then_fail"
    unsupported_hard_control: "error"
```

The numbers above are **[PROPOSED] starting defaults**, not universal thresholds. They must be calibrated against the selected models and tasks.

## 9.3 Mini-Model Policy

For a mini model:

- provide one bounded responsibility per call;
- retrieve a small bundle with explicit filters;
- use a fixed decomposition graph;
- allow zero or one high-impact branch point per pass;
- provide field descriptions, allowed enums, and an example;
- generate strict JSON or shallow YAML, then validate externally;
- use concise decision records rather than verbose rationales;
- offload arithmetic, frame counting, schema checks, graph checks, hashing, and file conversion to code;
- use a stronger model offline to create templates, few-shot examples, or distilled decision traces where economical [S011, S012];
- fail closed on missing hard controls.

Mini models are best used as specialists: query builder, beat classifier, format converter, constraint extractor, prompt compressor, or repair agent. They should not be forced to act as director, compiler, capability negotiator, and verifier in one call.

## 9.4 Standard-Model Policy

A standard model may:

- execute two or three adjacent graph stages;
- generate two to three candidate treatments;
- perform local least-to-most decomposition;
- use one external critic plus deterministic validation;
- synthesize several retrieved concept cards;
- produce both canonical and human-readable outputs under schema.

The system should still isolate high-risk operations such as rights decisions, hard-constraint arbitration, and canonical patches.

## 9.5 Large-Model Policy

A large model may:

- build or extend a partially specified reasoning graph;
- branch at several high-impact decision nodes;
- coordinate specialist subgraphs for story, performance, movement, camera, and compilation;
- use self-consistency for selected decisions [S002];
- aggregate compatible branches through GoT-style operations [S005];
- evaluate more diverse variants;
- compress a selected plan into multiple target representations.

Large models do not receive unlimited freedom. They still operate under:

- explicit authority and locks;
- graph and schema contracts;
- branch and token budgets;
- source and evidence requirements;
- independent compiler and verifier roles;
- loss-budget enforcement.

## 9.6 Adaptive Escalation

A mini model may escalate a node rather than hallucinate a resolution:

```json
{
  "status": "needs_escalation",
  "node_id": "question.camera_contact_visibility",
  "reason": "retrieved constraints conflict and no compatible camera template was found",
  "required_capability": "cross_domain_constraint_arbitration",
  "preserved_context_refs": ["retrieval.camera.12", "constraint.contact.03"]
}
```

Escalation can route to a larger model, a human director, or a deterministic solver. This is more reliable than encouraging a small model to produce confident prose under insufficient capability.

---

<!-- RAG_CHUNK id="adrg.10" title="Reasoning router and budget allocator" concepts="routing, impact, uncertainty, coupling, reversibility, branch budget" -->
<a id="adrg-reasoning-router"></a>
# 10. Reasoning Router and Budget Allocator

## 10.1 Decision Complexity

**[PROPOSED OPERATIONALIZATION]** Let a decision node have normalized estimates:

- \(I\): impact on audience meaning or hard compliance;
- \(U\): uncertainty after retrieval;
- \(C\): cross-domain coupling;
- \(R\): irreversibility or cost of a wrong choice;
- \(V\): availability of deterministic validation;
- \(M\): planner capability.

A routing priority may be defined as:

\[
D = w_I I + w_U U + w_C C + w_R R - w_V V.
\]

The graph operator is then selected under model and budget constraints:

```text
low D, strong validator          → direct compile + validate
moderate D                       → least-to-most + one critic
high D, few independent options  → selective ToT
high D, strongly coupled options → GoT subgraph + aggregation
external facts or state needed   → ReAct retrieval/tool action
deterministic computation needed → PAL/PoT-style runtime
ambiguous high-stakes result     → multiple candidates + external adjudication
```

The formula is a routing heuristic, not a psychological model. Its value is testability: the repository can log the features, selected operator, cost, and outcome.

## 10.2 Branch Admission Rule

A candidate branch is admitted only when it satisfies all of the following:

1. it changes at least one declared variation axis;
2. it preserves all hard invariants;
3. it is not dominated by an existing candidate on every evaluation criterion;
4. it is compatible with the target model or has an explicit alternate execution carrier;
5. its expected information gain exceeds its generation and evaluation cost.

## 10.3 Early Pruning

Candidates are pruned before full prompt generation when they:

- violate rights, safety, identity, continuity, or approved claims;
- exceed duration or frame budget;
- require unsupported hard controls;
- duplicate an existing variant’s semantic deltas;
- conflict with retrieved proven concepts without a declared experimental purpose;
- exceed the allowed simultaneous variation count.

## 10.4 Reasoning Budget Ledger

```yaml
reasoning_budget:
  total_units: 100
  allocation:
    intent_and_constraints: 12
    retrieval: 16
    performance_and_action: 20
    camera_and_presentation: 14
    variant_search: 14
    compilation: 12
    verification: 12
  escalation_reserve: 8
  stop_conditions:
    - "all hard controls covered"
    - "no unresolved graph conflicts"
    - "marginal variant gain below threshold"
    - "loss budget satisfied"
```

“Units” may represent tokens, calls, latency, money, or a composite resource score. Longer reasoning is not automatically better; recent work explicitly questions raw token length as a proxy for useful reasoning effort [S015].

## 10.5 Verification Checkpoint

The router must emit:

```text
selected_operator
reason_for_selection
estimated_cost
model_profile
branch_budget
retrieval_budget
validators_required
stop_conditions
```

A plan lacking these fields is not reproducible enough for experiments.

---

<!-- RAG_CHUNK id="adrg.11" title="Variant lattice for intentional design variation" concepts="variant generation, invariants, axes, diversity, selection" -->
<a id="adrg-variant-lattice"></a>
# 11. Variant Lattice for Intentional Design Variation

## 11.1 Problem with Unconstrained Variants

“Give me five versions” often causes models to rewrite surface wording while changing hidden semantics inconsistently. One version changes the camera, another changes the actor’s objective, another adds a cut, and another removes the required product reveal. The variants cannot be compared because too many levers changed.

The repository already requires one-lever A/B tests for causal promotion [S042]. ADRG extends this discipline upstream.

## 11.2 Invariants and Axes

A variant specification has two parts:

```yaml
variant_space:
  invariants:
    - action_identity
    - actor_identity
    - safety_class
    - duration_s
    - product_asset
    - final_story_state
  axes:
    camera_treatment:
      values: ["handheld_close", "low_tracking_medium", "telephoto_observer"]
    performance_intensity:
      values: ["restrained", "moderate", "overt"]
    temporal_shape:
      values: ["steady", "late_acceleration", "impact_hold"]
  incompatibilities:
    - ["handheld_close", "impact_hold"]
  maximum_simultaneous_deltas: 2
```

An **axis** is a typed design dimension. An **invariant** is a protected field or relation. A **delta** is the explicit difference from the parent variant.

## 11.3 Variant Record

```json
{
  "variant_id": "shot07.v_camera_tracking_perf_restrained",
  "parent_id": "shot07.base",
  "deltas": [
    {"axis": "camera_treatment", "from": "handheld_close", "to": "low_tracking_medium"},
    {"axis": "performance_intensity", "from": "moderate", "to": "restrained"}
  ],
  "preserved_invariants": [
    "action_identity",
    "safety_class",
    "duration_s",
    "product_asset"
  ],
  "expected_effect": {
    "action_readability": "+",
    "intimacy": "-",
    "generation_reliability": "+"
  },
  "risk": ["subtle face may be less legible at medium scale"],
  "compile_loss": []
}
```

## 11.4 Model-Scaled Variant Counts

**[PROPOSED defaults for testing]:**

- mini model: one reference treatment plus one orthogonal contrast;
- standard model: three treatments with no more than two simultaneous deltas;
- large model: four to eight candidates before pruning, then two to four finalists;
- empirical A/B promotion: exactly one controlled lever per comparison.

The large-model count is a search budget, not a requirement to render every candidate. Early semantic and capability checks should prune weak branches before expensive video generation.

## 11.5 Diversity Selection

Candidate diversity should be measured on semantic deltas, not lexical distance. Two prompts that use different adjectives but compile to the same camera, action, timing, and performance controls are duplicates. ADRG can select a subset maximizing:

\[
J(S) = \sum_{v \in S} Q(v) + \lambda \sum_{i<j} d_{semantic}(v_i, v_j) - \mu \sum_{v \in S} Risk(v),
\]

subject to all hard invariants. Here, \(Q\) is predicted quality under the rubric, \(d_{semantic}\) is distance across typed axes, and `Risk` includes capability loss and constraint fragility. The weights are project parameters to be calibrated.

## 11.6 Prompt Optimization versus Shot Optimization

Automatic Prompt Engineer and OPRO treat instructions or prompts as candidates scored by an objective [S027, S028]. ADRG applies search at a higher semantic level first. It optimizes the **shot plan and control mapping**, then compiles wording. This prevents the system from finding a locally effective phrase that silently changes the intended scene.

---
<!-- RAG_CHUNK id="adrg.12" title="Graph-aware RAG architecture" concepts="RAG, GraphRAG, hybrid retrieval, query decomposition, provenance" -->
<a id="adrg-graph-rag"></a>
# 12. Graph-Aware RAG for Director Planning

## 12.1 Role of Retrieval

RAG combines model parameters with explicit retrieved memory and can improve access to updateable or domain-specific knowledge while retaining provenance [S022]. In ADRG, retrieval is not used to make a prompt longer. It supplies the planner with the smallest compatible set of concepts, templates, failures, evidence, and model constraints needed to resolve a node.

The retrieval target is a **bundle**, not a single nearest chunk. A request for “a restrained but urgent approach shot” may need:

- locomotion and approach concepts;
- experienced versus displayed affect;
- Laban Time and Flow;
- gaze and interpersonal distance;
- a camera template that makes subtle leakage visible;
- a failure card for overacting or early gaze break;
- the target model’s duration and reference-input capabilities.

## 12.2 Retrieval Object Types

ADRG retains the CPCS knowledge objects and adds planner-specific objects.

| Object type | Purpose |
|---|---|
| `concept_card` | Definition, use conditions, pairings, conflicts, triggers. |
| `evidence_card` | Claim, sources, population/task scope, limitations. |
| `performance_template` | Reusable face/body/gaze/affect/motion fragment. |
| `shot_template` | Camera and edit grammar for a dramatic function. |
| `calibration_profile` | Mapping for a model, rig, performer, lens, or metric. |
| `failure_card` | Detector, likely cause, repair, and evidence. |
| `reasoning_pattern` | A decomposition, branch, selection, or critic strategy. |
| `model_policy` | Planner capability and budget profile. |
| `compiler_rule` | Semantic mapping, ownership, merge, or loss behavior. |
| `variant_axis` | Allowed values, invariants, incompatibilities, metrics. |
| `decision_template` | Question, criteria, candidate shape, and validators. |
| `experiment_record` | Controlled comparison and measured result. |

## 12.3 Query Decomposition

A natural request is normalized into subqueries:

```yaml
query_plan:
  request_text: "Anime fight, but keep the reference choreography exact and make it feel controlled rather than angry."
  subqueries:
    - id: q.intent
      types: [concept_card, performance_template]
      text: "controlled mastery displayed affect"
    - id: q.transfer
      types: [concept_card, compiler_rule]
      text: "preserve action and contact topology under anime style transform"
    - id: q.motion
      types: [concept_card, performance_template, failure_card]
      filters: {layer: action, requires_numeric_truth: true}
      text: "exact choreography contact phase kinematic canonical"
    - id: q.style
      types: [variant_axis, concept_card]
      text: "anime timing key pose hold smear impact frame"
    - id: q.execution
      types: [model_policy, compiler_rule]
      text: "target model supports reference video first frame pose or video-to-video"
```

The planner composes compatible fragments; it does not retrieve one monolithic example and import every detail.

## 12.4 Hybrid Retrieval Pipeline

```text
1. authority and access filtering
2. structured metadata filtering
3. lexical retrieval for exact codes and IDs
4. dense semantic retrieval for user language
5. typed graph expansion
6. provenance and evidence weighting
7. conflict and capability penalty
8. cross-encoder or LLM reranking
9. diversity selection
10. coverage report
```

A retrieval score can extend the CPCS formulation:

\[
R(o|q)=
\alpha R_{lex}+
\beta R_{dense}+
\gamma R_{struct}+
\delta R_{graph}+
\eta R_{prov}+
\kappa R_{model}
-\rho R_{conflict}
-\sigma R_{stale}.
\]

`R_model` rewards compatibility with the current planner and video backend. `R_stale` penalizes model-adapter information beyond the project’s verification window.

## 12.5 Graph Expansion

Graph expansion should be edge-aware and bounded:

```yaml
graph_expansion:
  seed_ids: ["c_style_transform_vector", "c_kinematic_truth"]
  allowed_edges:
    - pairs_with
    - requires
    - mitigates
    - conflicts_with
    - supported_by
  maximum_depth: 2
  maximum_nodes: 24
  stop_on_layers: ["rights", "safety"]
  include_conflicts: true
```

GraphRAG demonstrates the value of graph-derived summaries for global questions over large corpora [S023]. RAPTOR provides hierarchical retrieval across different levels of abstraction [S024], while HippoRAG explores graph-based multi-hop retrieval [S025]. ADRG uses these ideas selectively: local shot questions should retrieve fine-grained cards; architecture or corpus-level questions may use community or hierarchical summaries.

## 12.6 Context Packing

Long contexts do not guarantee uniform use of all information; relevant material can be underused depending on position [S026]. ADRG packs context in the order of authority and immediate task relevance:

1. system and policy constraints;
2. node question and required output schema;
3. hard invariants and target capability profile;
4. top evidence and compatible templates;
5. conflicts and failure cards;
6. optional alternatives;
7. background summaries.

Every retrieved object keeps a stable ID so the decision record can cite it without copying the whole object.

## 12.7 Coverage Contract

The retriever returns:

```json
{
  "query_id": "shot07.plan",
  "coverage": {
    "intent": true,
    "performance": true,
    "action": true,
    "camera": true,
    "target_capabilities": true,
    "verification": false
  },
  "candidates": [],
  "conflicts": [],
  "unresolved": ["no verified target-specific contact metric profile"],
  "source_digests": []
}
```

The planner may proceed with an unresolved soft field, but it may not silently invent a missing hard-control mechanism.

---

<!-- RAG_CHUNK id="adrg.13" title="Natural-language prompting contract" concepts="natural language, director intent, observable behavior, prompt compilation" -->
<a id="adrg-natural-language"></a>
# 13. Natural-Language Prompting Contract

## 13.1 What Natural Language Owns

Natural language is the strongest carrier for:

- director intent;
- audience understanding and feeling;
- character objective, obstacle, tactic, and subtext;
- observable behavior descriptions;
- visual and sonic priorities;
- qualitative relationships between departments;
- concise target-model prompt text.

Natural language should answer:

```text
What happens?
Why does it matter?
What should the audience notice?
What is the visible behavior?
Which event has priority?
What must not happen?
```

It should not be the only authority for dense numerical tracks, exact event arrays, graph dependencies, content hashes, or schema versions.

## 13.2 Director-Language Pattern

```text
[SHOT AND DURATION]
One continuous five-second medium-wide shot.

[SUBJECT AND ACTION]
Astra reads an incoming threat, steps in, pivots, performs one precise staged
near-contact strike, and returns to a controlled guard.

[PERFORMANCE]
The intention is mastery rather than rage. Her face remains restrained; the
body becomes strong and sudden only during execution, then returns to light,
bound control.

[TIMING]
Recognition precedes the step-in. The pivot drives the strike. The near-impact
moment is clear, followed by recovery before the hero pose.

[CAMERA AND PRESENTATION]
Track from a low medium-wide angle, preserving the gauntlet and full action
silhouette. Add one restrained impact accent without implying actual contact.

[NEGATIVES]
No flurry, no extra strike, no early recoil, no identity drift, no product
occlusion, no uncontrolled anger.
```

The labels may be omitted in the final target prompt if the backend performs better with prose. They remain useful in the source and compile report.

## 13.3 Language for Observable Performance

Prefer observable instructions:

```text
weak:  she feels conflicted
better: she maintains eye contact, delays the step, compresses the lips,
        and lets the shoulders retreat slightly before committing
```

Affect words remain useful at the intent layer, but the compiler should map them into visible alternatives rather than assume a single universal expression.

## 13.4 Natural-Language Planner Prompt

A planner prompt should specify a contract, not demand hidden reasoning:

```text
Act as the authoring planner for a CPCS video-control compiler.

Given the request, retrieved objects, hard invariants, and target capability
profile, return a schema-valid DirectorPlan. Decompose the request into the
required departments. Create alternatives only for high-impact uncertain
decisions. Preserve every invariant. Do not invent unsupported model features.

Return concise decision records containing alternatives, criteria, selection,
evidence IDs, assumptions, confidence, and unresolved loss. Do not return a
private chain-of-thought transcript.

The output will be compiled and independently validated. A missing hard control
must be reported as unresolved or unsupported, not silently removed.
```

## 13.5 Prompt Compression

For prompt-only video backends, the compiler ranks clauses by:

1. identity and subject;
2. primary action and event order;
3. hard timing and count constraints;
4. camera and composition;
5. performance qualities;
6. environment and lighting;
7. style and secondary effects;
8. critical negatives.

Low-level samples remain in canonical data or control assets. A prompt string is a lossy projection, as the CPCS architecture already recognizes [S041].

---

<!-- RAG_CHUNK id="adrg.14" title="YAML authoring and reasoning-policy contract" concepts="YAML, authoring, profiles, reasoning policy, inheritance" -->
<a id="adrg-yaml"></a>
# 14. YAML Authoring and Reasoning-Policy Contract

## 14.1 Role

YAML is designed as a human-friendly data serialization language [S029]. In ADRG it owns:

- project and shot authoring;
- reasoning-policy selection;
- model and adapter profile references;
- reusable profile inheritance;
- variation axes and invariants;
- human-reviewed hard constraints;
- import declarations;
- concise department overrides.

It does not own the fully resolved canonical graph after inheritance, imports, aliases, and defaults have been materialized.

## 14.2 Recommended Shape

```yaml
schema: "cpcs-adrg-authoring/1.0"
document_id: "gameLaunch.teaser.shot07"

imports:
  - id: "camera_profile"
    uri: "profile://camera/impact_readability_v1"
    sha256: "<digest>"
  - id: "model_profile"
    uri: "adapter://vendor/video-model@2026-07-23"
    sha256: "<digest>"

extends:
  - "performance://controlled_mastery@2"
  - "style://anime_sakuga_action@3"

reasoning:
  planner_profile: "planner.mini.strict.v1"
  decomposition: "director_fixed_dag_v1"
  branch_policy:
    allowed_axes: [camera_treatment, performance_intensity]
    maximum_branch_width: 2
    maximum_branch_depth: 1
  retrieval:
    top_k: 4
    graph_depth: 2
    include_failures: true
  outputs:
    decision_ledger: true
    raw_chain_of_thought: false

shot:
  duration_s: 5.0
  fps: 24
  intent:
    objective: "demonstrate controlled mastery"
    audience_takeaway: "precision is chosen"
  invariants:
    - "one staged near-contact strike"
    - "gauntlet visible at apex"
    - "recovery before hero pose"
  variation_axes:
    camera_treatment: [low_tracking_medium, telephoto_observer]
    performance_intensity: [restrained, moderate]
```

## 14.3 YAML Safety and Determinism

The compiler should:

- require a YAML 1.2-compatible profile;
- reject duplicate mapping keys;
- use a safe parser and prohibit arbitrary object construction;
- cap alias expansion;
- represent timelines as sequences with timestamps, not implied mapping order;
- treat YAML anchors as serialization conveniences, not semantic inheritance;
- require explicit units in field names or typed objects;
- resolve imports by immutable version or digest;
- materialize all effective values into canonical JSON.

The YAML specification describes mappings as unordered in the representation graph [S029]. Therefore, time and priority must not depend solely on the visual order of mapping keys.

## 14.4 Mini-Model YAML

Mini models should receive shallow YAML with fixed keys and short enum sets. Deep inheritance and cross-file resolution belong to the compiler. A mini model may propose:

```yaml
camera_treatment: low_tracking_medium
performance_intensity: restrained
reason:
  criteria: [action_readability, product_visibility]
  evidence_refs: [c_perceptual_constraints]
confidence: 0.78
```

The model should not rewrite the whole project file to change one decision.

---

<!-- RAG_CHUNK id="adrg.15" title="JSON canonical graph and structured output contract" concepts="JSON, JSON Schema, canonical IR, patches, constrained decoding" -->
<a id="adrg-json"></a>
# 15. JSON Canonical Graph and Structured-Output Contract

## 15.1 Role

JSON is a standardized data-interchange format with objects and ordered arrays [S030]. In ADRG it owns:

- the fully resolved reasoning graph;
- the fully resolved CPCS scene-control graph;
- model capability profiles;
- compile mappings and loss reports;
- exact arrays and timelines;
- JSON Schema validation;
- JSON Pointer addressing;
- JSON Patch revisions;
- hashes and manifests;
- API request payloads.

## 15.2 Canonical Requirements

A canonical JSON document must have:

- explicit schema and document versions;
- unique IDs;
- resolved imports and inheritance;
- explicit timebase and units;
- declared coordinate systems;
- deterministic arrays for ordered data;
- no duplicate object names;
- provenance for every effective control or a documented provenance compression policy;
- no unregistered backend fields outside adapter namespaces;
- validation against a pinned JSON Schema;
- semantic validation beyond structural schema.

## 15.3 JSON Schema

JSON Schema Draft 2020-12 defines a vocabulary for describing and validating JSON instances [S031]. It can enforce required fields, types, ranges, enumerations, conditional alternatives, and reusable definitions. It cannot decide whether a camera choice is artistically appropriate or whether a performance reads as controlled mastery. ADRG therefore separates:

```text
structural validation → JSON Schema
semantic validation   → graph and domain rules
perceptual validation → metrics and human review
empirical validation  → rendered A/B results
```

## 15.4 Constrained Generation

Incremental parsing and constrained decoding can improve validity for formal outputs [S019]. Structured-output benchmarks show that schema compliance, constraint coverage, efficiency, and content quality remain separate dimensions [S021]. Accordingly:

- constrain syntax when the runtime supports it;
- validate every output anyway;
- keep schemas no more complex than necessary;
- retry with targeted errors, not the entire original prompt;
- measure semantic completeness separately from parse success.

A schema-valid empty candidate list is not a successful director plan.

## 15.5 Precise Revision

JSON Pointer identifies values inside a JSON document [S032]. JSON Patch defines ordered `add`, `remove`, `replace`, `move`, `copy`, and `test` operations [S033]. ADRG uses patches for auditable decisions:

```json
[
  {
    "op": "test",
    "path": "/document_id",
    "value": "gameLaunch.teaser.shot07"
  },
  {
    "op": "replace",
    "path": "/decisions/camera_treatment/selected",
    "value": "telephoto_observer"
  },
  {
    "op": "add",
    "path": "/provenance/revisions/-",
    "value": {
      "reason": "director requested less camera participation",
      "review_id": "review.04"
    }
  }
]
```

The `test` operation protects against applying a patch to an unexpected base. Production patches should also include base and result hashes.

---

<!-- RAG_CHUNK id="adrg.16" title="XML director-envelope contract" concepts="XML, ordered mixed content, namespaces, event triggers, XSD" -->
<a id="adrg-xml"></a>
# 16. XML Director-Envelope Contract

## 16.1 Role

XML provides ordered markup and mixed content, and XSD can describe and constrain XML document structures [S034, S035]. In ADRG, XML owns:

- ordered screenplay and director notes;
- dialogue interleaved with semantic events;
- namespaced department annotations;
- trigger-based face, body, camera, VFX, audio, and marketing events;
- approvals and references to canonical JSON;
- transformations into prompts, review documents, or other XML-derived outputs.

XML should not duplicate dense canonical arrays already owned by JSON.

## 16.2 Director Envelope

```xml
<?xml version="1.0" encoding="UTF-8"?>
<adrg:directorPackage
    xmlns:adrg="urn:cpcs:adrg:1.0"
    xmlns:cpcs="urn:cpcs:core:1.1"
    xmlns:perf="urn:cpcs:performance:1.1"
    xmlns:cam="urn:cpcs:camera:1.1"
    xmlns:vfx="urn:cpcs:vfx:1.1"
    id="gameLaunch.teaser.shot07">

  <adrg:intent audienceTakeaway="precision is chosen">
    Controlled mastery, not rage. The action remains exact; presentation may vary.
  </adrg:intent>

  <adrg:beat id="recognition" start="0.00s" end="0.80s">
    <perf:direction actor="astra" display="restrained focus"/>
  </adrg:beat>

  <adrg:beat id="execution" start="0.80s" end="1.82s">
    <cam:directive ref="decision.camera_treatment"/>
    <vfx:trigger event="action.right_cross.near_contact"
                 effect="impact_accent" subordinateTo="constraint.no_contact"/>
  </adrg:beat>

  <cpcs:score href="asset://scores/gameLaunch.teaser.shot07.cpcs.json"
              mediaType="application/cpcs+json"
              sha256="..."/>
</adrg:directorPackage>
```

## 16.3 Namespace Discipline

Namespaces prevent collisions between a facial `event`, a camera `event`, and a marketing `event`. The semantic registry should map each qualified name to the same ontology used by JSON and YAML. Namespaces do not themselves define cinematic meaning; the compiler and schema do.

## 16.4 XML Security

The parser profile should disable external entity expansion unless explicitly required and sandboxed, reject network-dependent DTD resolution, limit document size and nesting, and validate against pinned schemas. Retrieved XML is data, not an instruction that may override system policy.

---
<!-- RAG_CHUNK id="adrg.17" title="Polyglot compiler and semantic ownership" concepts="YAML JSON XML combinations, dual authority, semantic compiler, JSONL" -->
<a id="adrg-polyglot-compiler"></a>
# 17. Polyglot Compiler and Semantic Ownership

## 17.1 One Ontology, Several Carriers

The compiler must treat natural language, YAML, JSON, XML, JSONL, and media as projections of one semantic model. It must not concatenate files and ask a model to guess precedence.

| Carrier | Primary ownership |
|---|---|
| Natural language | intention, audience effect, observable description, target prompt prose |
| YAML | human authoring, profiles, imports, reasoning policy, variants, constraints |
| JSON | canonical resolved graph, exact arrays, schemas, patches, adapters, manifests |
| XML | ordered mixed narrative, dialogue, namespaced event envelopes, approvals |
| JSONL | append-only RAG, decisions, compiler events, metrics, experiments |
| Media/arrays | dense pose, depth, masks, flow, camera, audio, reference video |

This assignment extends the repository’s current format-control map rather than replacing it [S040].

## 17.2 Semantic Ownership Rule

**[PROPOSED]** Every semantic path has one authoritative source at a given build stage:

```yaml
ownership:
  "/intent": "authoring://project.yaml"
  "/ordered_dialogue": "authoring://sequence.xml"
  "/tracks/body": "asset://motion/body_track.cpcs.json"
  "/tracks/camera": "canonical://shot07.cpcs.json"
  "/adapter/request": "compiled://target/request.json"
```

A second source may reference, annotate, or override a path only through a declared merge or patch operation. Inline duplicate values without precedence are errors.

## 17.3 YAML + JSON

Use YAML for intent and configuration; use JSON for exact or machine-generated data.

```yaml
imports:
  - id: "canonical_motion"
    uri: "asset://motion/shot07.body.cpcs.json"
    media_type: "application/cpcs+json"
    sha256: "..."

shot:
  intent:
    objective: "controlled mastery"
  tracks:
    body:
      ref: "canonical_motion#/tracks/body"
      preserve_contacts: true
```

The compiler resolves the JSON Pointer, validates the imported JSON, and inserts it into the canonical score with provenance. YAML does not duplicate thousands of samples.

## 17.4 XML + JSON

Use XML for ordered narrative and event annotations; reference JSON as numerical authority.

```xml
<adrg:directorPackage xmlns:adrg="urn:cpcs:adrg:1.0"
                      xmlns:cpcs="urn:cpcs:core:1.1">
  <adrg:brief>Recognition must precede the pivot.</adrg:brief>
  <cpcs:score href="asset://scores/shot07.cpcs.json"
              mediaType="application/cpcs+json"
              sha256="..."/>
</adrg:directorPackage>
```

Small adapter JSON may be embedded in CDATA when the ownership boundary is explicit, but XML validation alone cannot validate arbitrary JSON content.

## 17.5 YAML + XML

Use YAML for project and reasoning policy; use XML for ordered screenplay and trigger annotations.

```yaml
project:
  id: "gameLaunch"
  reasoning_profile: "planner.standard.v1"
sequence:
  envelope:
    uri: "authoring://teaser_sequence.xml"
    media_type: "application/cpcs-adrg+xml"
    sha256: "..."
```

The YAML compiler loads the XML, validates namespaces and order, maps both documents into the shared abstract syntax, then emits canonical JSON. Neither format is treated as an opaque text blob.

## 17.6 YAML + JSON + XML

A full package may be:

```text
project.yaml
  project defaults, reasoning policy, variants, imports

sequence.xml
  ordered screenplay, dialogue, semantic and department events

shot07.body.cpcs.json
  measured or generated dense body track

shot07.resolved.cpcs.json
  fully resolved canonical scene score

shot07.adrg.json
  reasoning execution and decision graph

run.events.jsonl
  retrieval, compile, validation, render, and review events
```

A manifest binds every file by role, schema, version, and digest.

## 17.7 Direct Multi-Format Prompting

When a user pastes a dual-format block directly into a language-conditioned model, the format acts as organizational rhetoric unless a documented interpreter enforces it. A compact dual prompt may still be useful because it separates concerns and can induce output variation. The compile report should mark this as `text_interpretation_only` unless the system actually parses the formats.

## 17.8 Cross-Format Compile Passes

```text
1. identify media type and parser profile
2. parse safely; reject malformed or duplicate structures
3. validate each source against its authoring schema
4. resolve imports by immutable ID or digest
5. map all sources into the shared semantic registry
6. enforce ownership and authority
7. apply typed inheritance, merge, and patches
8. normalize aliases, units, times, coordinates, and IDs
9. construct reasoning and scene-control graphs
10. validate graph references and dependency acyclicity
11. materialize canonical JSON
12. negotiate target capabilities
13. emit target prompt, parameters, and control assets
14. emit decision, provenance, conflict, and loss records
15. canonicalize, hash, and write the build manifest
```

A file conversion that omits these semantic passes is not the ADRG compiler.

---

<!-- RAG_CHUNK id="adrg.18" title="Worked example across natural language YAML JSON and XML" concepts="worked example, mini model, large model, compilation, decision record" -->
<a id="adrg-worked-example"></a>
# 18. Worked Example: Restrained Recognition and Approach

## 18.1 Director Request

> Six-second continuous shot. Mara walks toward Jon while hiding fear. She recognizes blood on his shirt at the final step, briefly loses control, then recovers. Keep eye contact until the recognition beat. End in a close-up. Produce two meaningful variants, one optimized for a mini planner and one for a larger planner.

## 18.2 Normalized Intent

```yaml
intent:
  objective: "approach while maintaining composure"
  obstacle: "rising fear"
  audience_takeaway: "control fails briefly at recognition"
  action_identity: "walk → recognize → stop → contain reaction"
  duration_s: 6.0
  hard_invariants:
    - "recognition coincides with final foot plant"
    - "no early gaze break"
    - "one continuous shot"
    - "end in close-up"
  allowed_variation_axes:
    - camera_path
    - leakage_intensity
```

## 18.3 Mini-Model Reasoning Policy

The mini planner receives a fixed task sequence:

```text
A. extract beats and invariants
B. retrieve one concept bundle per department
C. choose one value from each allowed enum
D. emit schema-valid decision records
E. compile shallow YAML
F. run deterministic validation
G. repair once on validator feedback
```

It is not asked to invent three full treatments. It proposes a reference plan and one contrast.

### Mini decision record

```json
{
  "decision_id": "dec.camera.mini",
  "question": "How should the camera reveal the brief loss of control?",
  "alternatives": ["late_dolly_in", "continuous_slow_dolly"],
  "selected": "late_dolly_in",
  "criteria": ["recognition_emphasis", "timing_clarity", "generation_reliability"],
  "evidence_refs": ["shot.recognition_dolly", "c_perceptual_constraints"],
  "confidence": 0.77,
  "unresolved": ["exact camera adherence depends on target model"]
}
```

### Mini YAML authoring output

```yaml
schema: "cpcs-adrg-authoring/1.0"
document_id: "filmA.scene12.shot04.mini"
shot:
  duration_s: 6.0
  mode: "single_continuous"
  subject: "Mara approaches Jon, recognizes blood, stops, and contains fear"
  performance:
    face: "restrained until recognition; low brow lowering and trace eye widening after 2.7s"
    gaze: "Jon's eyes until 2.5s; brief drop to shirt; return to eyes"
    body: "direct approach, sustained timing, bound flow; final plant at recognition"
  camera:
    start: "medium tracking"
    event: "late dolly-in beginning at recognition"
    end: "close-up hold"
  constraints:
    - "no early fear display"
    - "no extra step after final plant"
    - "no cut"
```

## 18.4 Large-Model Reasoning Graph

The larger planner may branch on two coupled decisions:

```text
camera treatment
├─ A late dolly-in at recognition
├─ B continuous slow dolly with focus transition
└─ C telephoto observation with no camera participation

performance leakage
├─ 1 facial micro-leak only
├─ 2 face + breath interruption
└─ 3 face + small torso retreat
```

Hard invariants prune combinations that obscure the final foot plant or break eye contact early. The graph scores surviving combinations for emotional clarity, physical feasibility, shot continuity, and target-model reliability. It selects `A2` as the primary treatment and `C3` as the orthogonal variant.

## 18.5 Canonical Decision Graph Excerpt

```json
{
  "nodes": [
    {
      "id": "goal.controlled_approach",
      "type": "goal",
      "plane": "scene_intent_control",
      "title": "Control fails only at recognition"
    },
    {
      "id": "cand.A2",
      "type": "candidate",
      "plane": "reasoning_execution",
      "title": "Late dolly-in plus breath interruption"
    },
    {
      "id": "cand.C3",
      "type": "candidate",
      "plane": "reasoning_execution",
      "title": "Telephoto observer plus small torso retreat"
    },
    {
      "id": "dec.primary",
      "type": "decision",
      "plane": "reasoning_execution",
      "title": "Select primary treatment",
      "selected_candidate": "cand.A2"
    }
  ],
  "edges": [
    {"id": "e1", "type": "proposes", "from": "goal.controlled_approach", "to": "cand.A2"},
    {"id": "e2", "type": "proposes", "from": "goal.controlled_approach", "to": "cand.C3"},
    {"id": "e3", "type": "selected_over", "from": "cand.A2", "to": "cand.C3", "decision_id": "dec.primary"}
  ]
}
```

## 18.6 XML Director Envelope

```xml
<adrg:directorPackage xmlns:adrg="urn:cpcs:adrg:1.0"
                      xmlns:perf="urn:cpcs:performance:1.1"
                      xmlns:cam="urn:cpcs:camera:1.1"
                      xmlns:cpcs="urn:cpcs:core:1.1"
                      id="filmA.scene12.shot04">
  <adrg:beat id="approach" interval="0.00s/2.50s">
    Mara maintains composure and direct eye contact.
    <perf:effort time="sustained" flow="bound" space="direct"/>
  </adrg:beat>
  <adrg:beat id="recognition" interval="2.50s/2.82s">
    The final foot plant and recognition are synchronized.
    <perf:gaze target="jon.shirt.blood" start="2.50s" end="2.76s"/>
    <perf:breath event="soft_inhalation_interrupt" time="2.73s"/>
    <cam:move type="dolly_in" start="2.50s" end="3.50s"/>
  </adrg:beat>
  <adrg:beat id="recovery" interval="2.82s/6.00s">
    She returns gaze to Jon and contains the reaction in close-up.
  </adrg:beat>
  <cpcs:score href="asset://scores/filmA.scene12.shot04.cpcs.json"
              mediaType="application/cpcs+json" sha256="..."/>
</adrg:directorPackage>
```

## 18.7 Compiled Natural-Language Prompt

```text
Single continuous six-second shot. Mara walks directly toward Jon while
maintaining controlled eye contact, her movement sustained and tightly bound.
At 2.5 seconds her final foot plant coincides with noticing blood on his shirt;
her gaze drops briefly, a soft breath interruption and subtle brow tension reveal
fear, then she returns her gaze and contains the reaction. Track in a medium shot,
begin a slow dolly-in at recognition, and settle into a close-up through recovery.
No early fear display, no extra step after the final plant, no cut, no identity
drift, and no exaggerated panic.
```

## 18.8 Compile-Loss Report

For a prompt-only backend, exact foot-contact timing, AU curves, and camera path may be compressed to text or retained for evaluation. For a multimodal backend, the compiler may render recognition and final-state keyframes. For a render-assisted pipeline, the contact, camera, and facial tracks can remain explicit. The report must not claim native precision where only prose is supplied.

---

<!-- RAG_CHUNK id="adrg.19" title="Deterministic compiler and verifier architecture" concepts="authoring compiler verifier, validation checkpoints, schema, graph integrity, loss budget" -->
<a id="adrg-verification"></a>
# 19. Deterministic Compiler and Verifier Architecture

## 19.1 Role Separation

The repository already recommends separate authoring, compiler, and verifier roles [S042]. ADRG makes the interfaces explicit.

### Authoring planner

May retrieve, propose, branch, and select. It cannot declare its own output valid.

### Compiler/resolver

Parses formats, resolves imports and authority, normalizes semantics, constructs canonical graphs, negotiates capabilities, and emits target packages. It should be deterministic for a fixed input set and compiler version.

### Verifier

Checks source validity, graph integrity, semantic consistency, compile loss, target-package completeness, and rendered output metrics. It does not silently repair canonical data without a patch record.

## 19.2 Validation Checkpoints

### Checkpoint A: source parsing

Observable pass conditions:

```text
YAML parses under restricted profile
JSON parses with duplicate names rejected
XML is well formed and namespace-valid
all declared media types match parsers
```

### Checkpoint B: schema validation

```text
all source documents validate
reasoning graph validates
canonical scene score validates
adapter request validates
```

### Checkpoint C: reference integrity

```text
all IDs and JSON Pointers resolve
all imported assets match digests
all graph edges resolve to nodes
all evidence IDs resolve to source records
```

### Checkpoint D: semantic graph validation

```text
depends_on subgraph is acyclic
bounded repair loops have maximum iterations
selected candidates satisfy invariants
hard conflicts are unresolved errors
variant deltas match declared axes
```

### Checkpoint E: temporal and control validation

```text
sample times are monotonic
beats fit within duration
frame counts reconcile with fps and duration
contacts and reactions preserve causal order
camera and action events do not contradict continuity
```

### Checkpoint F: authority and ownership

```text
one authority per semantic path
locks are preserved
rights and safety constraints cannot be weakened
patches target the expected base
```

### Checkpoint G: capability negotiation

```text
every canonical control has a realization status
unsupported hard controls stop the build
loss budget is satisfied
adapter profile is current under project policy
```

### Checkpoint H: target package

```text
prompt and API fields are separated correctly
required assets exist
manifest hashes match
no undeclared backend syntax leaks into canonical data
```

### Checkpoint I: render verification

```text
identity, timing, action count, contact, camera, product visibility,
performance, and continuity metrics are recorded with confidence
```

## 19.3 Constraint Assertions

LM assertions can express computational constraints around model modules [S020]. ADRG uses assertions as first-class validator definitions:

```yaml
assertion:
  id: "assert.variant_preserves_action"
  scope: "candidate"
  condition: "candidate.invariants contains action_identity"
  on_fail: "reject_candidate"

assertion:
  id: "assert.no_unreported_drop"
  scope: "compile_report"
  condition: "every canonical_control has realization_status"
  on_fail: "build_error"
```

## 19.4 Repair Protocol

A repair cycle is bounded:

```text
validator error
→ smallest relevant source slice
→ repair proposal as JSON Patch or source edit
→ apply to expected base
→ rerun failed validator and dependent validators
→ record result
```

A mini model should receive the exact error, relevant schema fragment, and affected object—not the entire corpus. After the permitted retry count, the node becomes `blocked` or escalates.

## 19.5 Compilation Loss Ledger

```json
{
  "control_id": "control.face.mara.au04",
  "target_adapter": "prompt_only.generic.v1",
  "status": "compressed_to_text",
  "retained_information": ["action_unit_semantics", "relative_intensity", "event_order"],
  "lost_information": ["exact_spline", "calibrated_peak", "apex_tolerance"],
  "verification": ["post_generation_au_estimate"],
  "severity": "medium",
  "approved": true
}
```

This ledger is essential when comparing models. A model should not receive credit for “following exact FACS” when the target package supplied only a vague phrase.

---
<!-- RAG_CHUNK id="adrg.20" title="Repository integration design" concepts="concept cards, graph builder, research package, no hand edit, validation" -->
<a id="adrg-repo-integration"></a>
# 20. Repository Integration Design

## 20.1 Integration Principle

The repository declares `lab/graph.json` a derived artifact and requires new research packages to be connected through source aliases, concept cards, the concept index, graph rebuilding, and validation [S036, S038]. ADRG should therefore enter the repository as a new, immutable research package plus lab-level integration records. It should not modify the existing frozen CPCS v1.2 package in place.

## 20.2 Proposed Package Location

```text
research/
  CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0/
    README.md
    paper/
    rag/
    schemas/
    examples/
    references/
    scripts/
    manifests/
```

## 20.3 Proposed Concept Cards

The integration bundle supplies concept cards for:

- ADRG reasoning control plane;
- five graph planes;
- decision ledger instead of raw CoT;
- model-scaled reasoning policy;
- reasoning router;
- selective branch admission;
- variant lattice;
- graph-aware RAG expansion;
- semantic ownership across formats;
- compilation loss ledger;
- schema-constrained specialist agents;
- teacher-to-mini decision-pattern distillation;
- reasoning-mode ablation.

New cards should begin `unexplored` unless repository render or pipeline evidence already exists. Literature support belongs in `source`; it does not substitute for target-repository validation.

## 20.4 Graph Builder Extension

The current builder creates concept, layer, block, pattern, variant, experiment, runbook, run, paper, and evidence nodes [S038]. ADRG recommends adding optional source types:

```text
reasoning_policy
model_profile
decision_template
compiler_rule
variant_axis
failure_card
```

These may initially be represented as `concept` nodes with richer metadata to minimize migration risk. A later schema version can promote them to dedicated node kinds after the retrieval and visualization requirements are stable.

## 20.5 Proposed Edge Additions

The minimum useful additions are:

```text
decomposes_to
depends_on
grounds
requires
mitigates
variant_of
selected_over
compiled_to
approximated_by
validated_by
repaired_by
preserves
```

The builder should allow an edge only when its required metadata is present. For example, `selected_over` should carry a `decision_id`; `compiled_to` should carry a target adapter and realization status.

## 20.6 Concept Index Addition

Add a new indexed part summarizing:

1. why reasoning is a separate control plane;
2. which method is used at which decision type;
3. mini versus large model policies;
4. graph planes and edge vocabulary;
5. language ownership contracts;
6. variant and verification rules;
7. links to the RAG package and schemas.

## 20.7 Validation Sequence

After copying the package into the repository:

```bash
python3 research/CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0/scripts/validate_package.py
python3 lab/scripts/concepts.py validate
python3 lab/scripts/build_graph.py
python3 lab/scripts/validate_repo.py
python3 lab/scripts/sync_repo.py --fix
python3 lab/scripts/validate_repo.py
```

Observable success means every command exits with status 0, the graph diff contains the expected new nodes and edges, and no frozen package was modified.

## 20.8 Migration Strategy

A low-risk staged migration is:

### Stage 1 — documentation and retrieval

Add paper, RAG corpus, sources, concept cards, and aliases. Do not change runtime behavior.

### Stage 2 — schemas and decision records

Add reasoning-graph and policy schemas. Emit decision records beside existing prompt compositions.

### Stage 3 — model routing

Introduce mini/standard/large planner profiles and route one existing workflow through the fixed ADRG graph.

### Stage 4 — variant lattice

Replace untyped “generate variants” calls with invariant-and-axis specifications.

### Stage 5 — compile-loss and render evidence

Connect decisions to target adapters, loss records, and run metrics. Promote only experimentally supported policies.

---

<!-- RAG_CHUNK id="adrg.21" title="Experimental program" concepts="ablation, mini models, large models, formats, metrics, causal testing" -->
<a id="adrg-experiments"></a>
# 21. Experimental Program

## 21.1 Core Research Questions

1. Does a fixed ADRG decomposition improve schema validity and control coverage for mini models relative to one-shot prompting?
2. Does selective branching improve meaningful variant diversity without increasing contradiction rate?
3. Does graph-aware retrieval outperform dense-only retrieval for multi-domain video requests?
4. Do concise decision records preserve plan quality while reducing tokens relative to verbose intermediate reasoning?
5. Does semantic ownership reduce contradictions in YAML+JSON, XML+JSON, and YAML+XML workflows?
6. Does a compile-loss ledger predict where rendered adherence will fail?
7. Which reasoning policies transfer across video-generation backends, and which are model-specific?

## 21.2 Experimental Factors

```yaml
factors:
  planner_model_class: [mini, standard, large]
  reasoning_mode:
    - direct
    - local_cot
    - fixed_least_to_most
    - selective_tot
    - adaptive_director_graph
  retrieval_mode:
    - none
    - dense_only
    - hybrid
    - hybrid_plus_graph
  output_carrier:
    - natural_language
    - yaml
    - json
    - xml
    - yaml_json
    - yaml_xml
    - json_xml
  candidate_policy:
    - one
    - two_orthogonal
    - four_then_prune
  verifier:
    - none
    - intrinsic_critic
    - deterministic
    - deterministic_plus_render_metrics
```

Not every combination must be tested at once. Start with a fractional design that isolates one architectural lever.

## 21.3 Task Set

Use controlled tasks spanning:

- UGC talking-head performance;
- subtle recognition and emotional masking;
- locomotion and stop timing;
- precise dance or fight choreography;
- reference-motion preservation under style transfer;
- product-focused advertising with visibility constraints;
- multi-shot scene continuity;
- prompt-only and multimodal execution tiers.

Each task should have a gold or reviewed control specification so planner quality can be measured before video generation.

## 21.4 Planner Metrics

| Metric | Definition |
|---|---|
| `parse_validity` | Output parses under the required carrier. |
| `schema_validity` | Output passes structural schema. |
| `control_coverage` | Required control fields resolved or explicitly unresolved. |
| `hard_constraint_recall` | Fraction of source hard constraints retained. |
| `contradiction_rate` | Incompatible controls per plan. |
| `evidence_resolution` | Fraction of cited IDs that resolve. |
| `decision_completeness` | Required decision-record fields present. |
| `semantic_duplicate_rate` | Variant pairs with no meaningful typed delta. |
| `token_cost` | Input plus output tokens or normalized inference cost. |
| `repair_count` | Validator-driven attempts before pass/fail. |
| `compile_loss_severity` | Weighted information loss under target adapter. |

## 21.5 Video Metrics

Retain the repository’s realism, skin, motion, and adherence scores [S037, S042], then add task-specific measures:

- action order and count;
- beat timing error;
- contact or near-contact timing;
- foot slip and support violations;
- identity consistency;
- camera and framing adherence;
- facial/gaze event visibility;
- product visibility and occlusion;
- variant diversity under preserved invariants;
- human judgment of intended audience meaning.

## 21.6 Causal Discipline

A rendering result can support a claim only when:

- the compared plans differ on the declared lever;
- model, seed policy, duration, aspect ratio, references, and other inputs are controlled or logged;
- output selection policy is declared;
- the metric and reviewer protocol are fixed before comparison where practical;
- the exact source and compiled artifacts are hashed;
- failed or contrary results are retained.

The repository’s one-lever A/B rule should remain the promotion gate [S042]. Multi-axis variants are useful for creative exploration but weak for causal attribution.

## 21.7 Suggested Initial Experiments

### E-ADRG-001: Mini fixed graph versus one-shot

- same request, retrieval corpus, and target schema;
- compare one-shot JSON generation with fixed five-node decomposition;
- metrics: schema validity, hard-constraint recall, repair count, token cost.

### E-ADRG-002: Decision ledger versus verbose rationale

- same model and candidate set;
- compare compact decision record with unrestricted explanation;
- metrics: selection quality, token cost, evidence resolution, downstream compile success.

### E-ADRG-003: Dense retrieval versus graph bundle

- same query and model;
- dense top-k versus dense plus bounded `pairs_with/conflicts/requires` expansion;
- metrics: coverage, contradictions, irrelevant retrieved objects, final adherence.

### E-ADRG-004: Dual-format semantic ownership

- compare raw concatenated YAML+XML against ownership-declared YAML referencing XML;
- metrics: duplicate authority, parse success, retained constraints, target prompt consistency.

### E-ADRG-005: Selective ToT for camera treatment

- branch only the camera decision;
- compare direct choice with three candidates and rubric selection;
- metrics: selected plan quality, semantic diversity, cost, render adherence.

## 21.8 Promotion Criteria

A reasoning policy may be promoted from `unexplored` only after:

- at least one isolated experiment supports it;
- the result repeats across more than one task or is explicitly scoped;
- costs and failure cases are recorded;
- no unresolved rights or safety issue exists;
- the concept card is updated with evidence IDs and calibrated confidence.

---

<!-- RAG_CHUNK id="adrg.22" title="Security limitations and misuse controls" concepts="prompt injection, RAG security, raw CoT, format security, uncertainty" -->
<a id="adrg-limitations"></a>
# 22. Security, Limitations, and Misuse Controls

## 22.1 Prompt Injection in Retrieved Content

Retrieved documents are data, not authority. The planner must not allow a concept card, paper chunk, XML note, or copied prompt to change system policy, reveal secrets, disable validation, or execute code. Store trust level, access scope, source hash, and allowed use with every retrieval object.

## 22.2 Structured Format Security

- YAML: use safe loaders, reject unsafe tags, duplicate keys, and excessive aliases.
- JSON: reject duplicate names, validate size and depth, avoid `eval`, and pin schemas.
- XML: disable unsafe external entities and network-dependent DTDs; validate namespaces and size.
- JSONL: treat each line as independent untrusted data; do not execute embedded instructions.
- Imported assets: verify media type, digest, access scope, and license.

## 22.3 Model Capability Drift

Planner and video APIs change. A capability profile must include model ID, endpoint or runtime version, verification date, source, and test-suite version. A stale profile should warn or fail under project policy. This paper cannot verify future model behavior with 100% certainty; every adapter claim must be rechecked against current official documentation and local capability tests.

## 22.4 Reasoning Method Generalization

The cited reasoning methods were evaluated on tasks such as arithmetic, symbolic reasoning, search, question answering, or code—not on the entire AI-video directing problem. ADRG’s mapping of those methods to directing is a systems hypothesis. It must be validated in the target repository.

## 22.5 Small-Model Limits

Distillation research shows that smaller models can benefit from teacher rationales [S011, S012], but performance depends on task, data, training, and model family. A small model may still fail on long dependency chains, subtle conflict arbitration, or cross-domain synthesis. The correct response is bounded specialization and escalation, not hidden complexity in a longer prompt.

## 22.6 Self-Critique Limits

Self-refinement can improve outputs [S007], but intrinsic reasoning self-correction is unreliable without external feedback [S008]. Therefore, a critic pass cannot substitute for parsers, schemas, solvers, validators, or render evidence.

## 22.7 Graph Complexity

Graphs can become a new form of prompt bloat. ADRG should retain only durable, queryable, or testable nodes. Low-value scratch nodes should be summarized or discarded. Community summaries, hierarchical retrieval, and bounded expansion can help at corpus scale [S023, S024], but they also add preprocessing and maintenance cost.

## 22.8 Creative Homogenization

Over-constrained retrieval and fixed rubrics can narrow creative range. ADRG protects exploration by separating hard invariants from soft preferences and by reserving branch budget for deliberately orthogonal alternatives. Human directors must be able to override soft scores and introduce a new candidate with documented rationale.

## 22.9 Rights, Identity, and Reference Material

The graph must preserve consent, license, identity, and authorized-use metadata. Reference-video distillation should separate transferable motion or camera grammar from protected identity and distinctive surface details, consistent with the existing CPCS framework [S041].

---

<!-- RAG_CHUNK id="adrg.23" title="Implementation blueprint" concepts="modules, APIs, data flow, services, checkpoints" -->
<a id="adrg-implementation-blueprint"></a>
# 23. Implementation Blueprint

## 23.1 Minimal Service Boundaries

```text
Request Normalizer
  input: user request, assets, requested outputs
  output: normalized DirectorRequest JSON

Knowledge Retriever
  input: structured query plan
  output: evidence bundle + coverage report

Reasoning Router
  input: request features, model profile, budget
  output: operator graph and stop conditions

Planner Workers
  input: one bounded node + evidence + schema
  output: candidate or decision record

Graph Resolver
  input: reasoning nodes and edges
  output: coherent selected treatment + conflicts

CPCS Authoring Compiler
  input: selected treatment
  output: YAML/XML authoring and canonical JSON proposal

Target Adapter
  input: canonical score + capability profile
  output: prompt, API fields, media/control assets, loss ledger

Verifier
  input: all source and target artifacts
  output: validation events and acceptance report

Experiment Logger
  input: planner/run/render results
  output: JSONL records and evidence updates
```

## 23.2 Suggested Repository Data Flow

```text
user request
  ↓
lab concept query + model-profile query
  ↓
ADRG build record (JSON)
  ↓
selected DirectorPlan (JSON)
  ↓
existing profile/block composition
  ↓
CPCS authoring YAML / sequence XML / canonical JSON
  ↓
target adapter and generated prompt
  ↓
render candidate(s)
  ↓
verification JSONL
  ↓
lab run row + experiment record
  ↓
concept/pattern confidence update after review
```

## 23.3 Suggested API Contracts

### Normalize

```json
{
  "request_text": "...",
  "assets": [],
  "target_profile_id": "...",
  "requested_formats": ["yaml", "xml", "json", "natural_language"]
}
```

### Plan node

```json
{
  "node": {},
  "evidence_bundle": [],
  "invariants": [],
  "output_schema_id": "adrg://schema/decision/1.0",
  "budget": {"maximum_output_tokens": 700}
}
```

### Validate

```json
{
  "artifact_uri": "build://shot07/adrg.json",
  "schema_id": "adrg://schema/graph/1.0",
  "semantic_rule_set": "adrg://rules/default/1.0"
}
```

## 23.4 Deterministic Build Identity

A build identity should hash:

- normalized request;
- source documents and imports;
- retrieved object IDs and versions;
- planner model/profile and prompt template;
- schemas and compiler version;
- selected decision graph;
- target adapter profile;
- random seeds where supported.

This does not make stochastic video generation deterministic. It makes the planning and compilation inputs reproducible.

## 23.5 Failure Isolation

Because each node has explicit inputs and outputs, a failed shot can be traced to:

- missing or irrelevant retrieval;
- incorrect decision criteria;
- branch pruning;
- semantic compilation;
- target capability loss;
- stochastic generation;
- verification error.

This is substantially more actionable than revising an entire monolithic prompt after every failure.

---

<!-- RAG_CHUNK id="adrg.24" title="Conclusion and recommendations" concepts="ADRG, GoT, CoT, mini models, polyglot compiler, next steps" -->
<a id="adrg-conclusion"></a>
# 24. Conclusion

The useful question is not “Should video prompting use CoT, ToT, or GoT?” The useful question is “Which reasoning operator should resolve this decision, under this model, budget, evidence, and verification regime?”

For dependency-rich directing, Graph-of-Thoughts is a suitable **orchestration abstraction**. It represents interactions among intent, performance, action, camera, style, capability, and verification more naturally than one linear chain. Within that graph, least-to-most and local CoT decompose bounded problems; ToT explores only high-value alternatives; ReAct and program-aided execution call retrieval, parsers, compilers, and solvers; self-consistency can adjudicate selected ambiguous nodes; and external validators provide the evidence that intrinsic critique cannot guarantee.

For mini models, the strongest production strategy is not wide graph search. It is a fixed narrow graph, small evidence bundles, one specialist responsibility per call, strict structured output, concise decision records, external computation, bounded repair, and escalation. For larger models, branch width and cross-domain aggregation can increase, but authority, schemas, budgets, and independent verification remain mandatory.

Natural language, YAML, JSON, and XML should be treated as a compiler family rather than rival prompting styles. Natural language carries intention and observable description. YAML carries human-authored policy, profiles, and variants. JSON carries the canonical graph, exact controls, patches, and target payloads. XML carries ordered mixed narrative and namespaced events. JSONL carries the evidence and experiment stream. Dual-format prompting is valuable only when ownership is explicit and the compiler prevents contradictory authority.

The proposed ADRG extension gives the repository a way to connect concepts not only by topical relation, but by **design causality**:

```text
user intent
→ retrieved concepts
→ candidate treatments
→ selected decisions
→ canonical controls
→ target compilation
→ measured render results
→ updated evidence
```

That loop is the mechanism for maximizing model output over time. It preserves intention, creates meaningful design variations, uses mini and large models according to their strengths, and turns prompting experiments into graph-grounded engineering knowledge.

---

# Full Reference List

[S001] Wei, J., et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. arXiv:2201.11903.

[S002] Wang, X., et al. (2022). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. arXiv:2203.11171.

[S003] Zhou, D., et al. (2022). *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models*. arXiv:2205.10625.

[S004] Yao, S., et al. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. arXiv:2305.10601.

[S005] Besta, M., et al. (2023). *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*. arXiv:2308.09687.

[S006] Yao, S., et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv:2210.03629.

[S007] Madaan, A., et al. (2023). *Self-Refine: Iterative Refinement with Self-Feedback*. arXiv:2303.17651.

[S008] Huang, J., et al. (2023). *Large Language Models Cannot Self-Correct Reasoning Yet*. arXiv:2310.01798.

[S009] Turpin, M., et al. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. arXiv:2305.04388.

[S010] Lanham, T., et al. (2023). *Measuring Faithfulness in Chain-of-Thought Reasoning*. arXiv:2307.13702.

[S011] Hsieh, C.-Y., et al. (2023). *Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes*. arXiv:2305.02301.

[S012] Li, L. H., et al. (2023). *Symbolic Chain-of-Thought Distillation: Small Models Can Also Think Step-by-Step*. arXiv:2306.14050.

[S013] Xu, S., et al. (2025). *Chain of Draft: Thinking Faster by Writing Less*. arXiv:2502.18600.

[S014] Ubukata, S. (2026). *D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models*. arXiv:2602.21786. [EMERGING]

[S015] Chen, W.-L., et al. (2026). *Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens*. arXiv:2602.13517. [EMERGING]

[S016] Chen, W., et al. (2022). *Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks*. arXiv:2211.12588.

[S017] Gao, L., et al. (2022). *PAL: Program-aided Language Models*. arXiv:2211.10435.

[S018] Khattab, O., et al. (2023). *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines*. arXiv:2310.03714.

[S019] Scholak, T., et al. (2021). *PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models*. arXiv:2109.05093.

[S020] Singhvi, A., et al. (2023). *DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines*. arXiv:2312.13382.

[S021] Geng, S., et al. (2025). *Generating Structured Outputs from Language Models: Benchmark and Studies*. arXiv:2501.10868.

[S022] Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. arXiv:2005.11401.

[S023] Edge, D., et al. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv:2404.16130.

[S024] Sarthi, P., et al. (2024). *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*. arXiv:2401.18059.

[S025] Jimenez Gutierrez, B., et al. (2024). *HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models*. arXiv:2405.14831.

[S026] Liu, N. F., et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts*. arXiv:2307.03172.

[S027] Zhou, Y., et al. (2022). *Large Language Models Are Human-Level Prompt Engineers*. arXiv:2211.01910.

[S028] Yang, C., et al. (2023). *Large Language Models as Optimizers*. arXiv:2309.03409.

[S029] YAML Language Development Team. (2021). *YAML Version 1.2, Revision 1.2.2*.

[S030] Bray, T. (2017). *RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format*.

[S031] Wright, A., Andrews, H., Hutton, B., & Dennis, G. (2022). *JSON Schema Draft 2020-12*.

[S032] Bryan, P., Zyp, K., & Nottingham, M. (2013). *RFC 6901: JavaScript Object Notation (JSON) Pointer*.

[S033] Bryan, P., & Nottingham, M. (2013). *RFC 6902: JavaScript Object Notation (JSON) Patch*.

[S034] Bray, T., Paoli, J., Sperberg-McQueen, C. M., Maler, E., & Yergeau, F. (2008). *Extensible Markup Language (XML) 1.0 (Fifth Edition)*. W3C Recommendation.

[S035] W3C XML Schema Working Group. (2012). *W3C XML Schema Definition Language (XSD) 1.1 Part 1: Structures*.

[S036] Kingsley-Cyber. (2026). *AI Video Movement Prompt System Repository Governance*. `AGENTS.md`.

[S037] Kingsley-Cyber. (2026). *AI Video Movement Prompt System Concept Cards*. `lab/concepts.jsonl`.

[S038] Kingsley-Cyber. (2026). *AI Video Movement Prompt System Graph Builder*. `lab/scripts/build_graph.py`.

[S039] Kingsley-Cyber. (2026). *AI Video Movement Prompt System Control Surface*. `lab/CONTROL_SURFACE.md`.

[S040] Kingsley-Cyber. (2026). *AI Video Movement Prompt System Format-Control Map*. `lab/FORMAT_CONTROL_MAP.md`.

[S041] OpenAI. (2026). *From Action Units to Action Beats: A Directorial Control, Reference-Video Distillation, and Compilation Framework for AI Video Generation*. CPCS research package v1.2.

[S042] Kingsley-Cyber. (2026). *AI Video Movement Prompt Lab Operating Procedure*. `lab/AGENTS.md`.

---

# Document Change Log

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-07-23 | Initial ADRG architecture, RAG model, model-scaled reasoning policies, variant lattice, polyglot compiler contracts, repository integration plan, and validation program. |
