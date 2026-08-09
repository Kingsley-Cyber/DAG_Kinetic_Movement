# Pro Deep Research Prompt — Director Motion Reasoning Evidence Delta

Act as a principal research engineer, computational movement scientist, ontology engineer, multimodal behavior researcher, and technical standards analyst.

## Mission

Produce a source-grounded **evidence delta** for the repository `Kingsley-Cyber/ai-video-movement-prompt-system`. Do not restate topics already adequately covered by its CPCS v1.2 and CPCS-MX v1.0 packages. Focus on gaps that can be integrated into the existing canonical score, Video Observation Graph, concept corpus, and validation control plane.

## Mandatory repository context

Before researching, inspect:

- `AGENTS.md`
- `README.md`
- `lab/AGENTS.md`
- `lab/CONCEPT_INDEX.md`
- `lab/CONTROL_SURFACE.md`
- `lab/FORMAT_CONTROL_MAP.md`
- `lab/UNIVERSAL_MOTION_SKELETON.md`
- `lab/concepts.jsonl`
- both CPCS research-package READMEs, source indexes, schemas, and implementation roadmaps.

Build a requirement-to-existing-owner matrix. Do not research or write a replacement for a concept that already has a sufficient owner.

## Research questions

### A. Bartenieff connectivity

1. What are the recognized Patterns of Total Body Connectivity, their canonical names, aliases, and conceptual boundaries?
2. Which claims come from Bartenieff/Hackney practice, and which computational features are later proxies?
3. Which pose/mocap features could defensibly approximate initiation, propagation, contralateral coordination, phase lag, support, and center-of-mass effects?
4. What cannot be inferred from 2D video alone?

### B. Behavior Markup Language

1. What is BML's verified specification/status and SAIBA role?
2. Which modalities and synchronization mechanisms are core versus extension-specific?
3. What are the exact meanings of `start`, `ready`, `stroke-start`, `stroke`, `stroke-end`, `relax`, and `end` in the verified profile?
4. How can CPCS XML align with BML without falsely claiming full conformance?
5. How should speech, gaze, gesture, posture, face, head, blink, breath, and external event triggers map to the canonical score?

### C. Temporal phase models

Compare primary/foundational sources for:

- FACS onset/apex/offset;
- gesture preparation/stroke/holds/retraction;
- gait stance/swing and functional subdivisions;
- BML behavior phases/sync points;
- animation anticipation/action/follow-through/settle;
- biomechanics and motor-control segmentation;
- action recognition and text-to-motion temporal segmentation.

Determine whether a single authoritative universal seven-phase movement model exists. A negative result is acceptable and must be explicit. Then propose a project-specific normalized profile only if justified, with domain mappings, optional phases, merge/split rules, interruption semantics, and uncertainty.

### D. Affect interoperability

Research W3C EmotionML and dimensional affect literature. Define how CPCS VAD/control trajectories, confidence, modality, observer, and time traces can map without claiming that observed behavior proves internal emotion.

### E. Graph/provenance interoperability

Assess PROV-O, SHACL, and temporal-ontology alignment for:

- source/observation/claim/transformation/validation provenance;
- temporal intervals and relations;
- confidence and alternative interpretations;
- graph constraint validation.

Keep the JSON canonical model independent of RDF; propose optional mappings.

### F. Serialization and LLM behavior

Review controlled empirical evidence comparing Markdown/plain text, YAML, XML, JSON, and structured-output constraints. Separate:

- input template effects;
- output parseability;
- constrained decoding;
- reasoning performance;
- model/task/size dependence;
- token overhead;
- provider-native structured output;
- anecdotal guidance.

Do not conclude that one format universally improves model intelligence. Propose a local benchmark with fixed semantics, repeated trials, parseability, semantic accuracy, token count, latency, and reasoning/adherence metrics.

### G. Cross-format semantic equivalence

Specify a deterministic canonical-to-Markdown/YAML/XML/JSON/JSONL architecture. Identify what each format can preserve exactly, what requires convention, and what is necessarily lossy. Define semantic-hash and round-trip tests.

### H. Closed-loop verification

Define measurable authored-vs-generated comparison metrics for action order, phase timing, contact timing/distance, root/joint paths, support/foot slip, camera, edits, identity drift, affect/display cues, product visibility, and style invariants. State observability limits and calibration requirements.

## Source policy

Prioritize, in order:

1. standards/specifications and foundational publications;
2. peer-reviewed primary research;
3. official institutions/professional organizations;
4. university material;
5. reputable technical documentation;
6. secondary summaries only when primary sources are unavailable.

For every material claim record:

- source ID;
- author/institution;
- title/year;
- DOI or stable locator;
- source type;
- primary/secondary;
- peer-review or standards status;
- access date;
- exact concepts supported;
- reliability/limitations;
- rights/licensing note;
- direct evidence versus synthesis.

Do not use search snippets as final evidence. Do not fabricate page numbers or quotations. Mark inaccessible details unverified. Limit quotation and paraphrase proprietary manuals.

## Required outputs

Create one research bundle with:

```text
README.md
EVIDENCE_DELTA.md
SOURCE_CATALOG.csv
SOURCE_ANNOTATIONS.jsonl
CLAIM_SOURCE_MATRIX.csv
BARTENIEFF_CONNECTIVITY.md
BML_ALIGNMENT.md
TEMPORAL_MODEL_COMPARISON.md
NORMALIZED_PHASE_PROFILE_PROPOSAL.md
EMOTIONML_ALIGNMENT.md
GRAPH_STANDARDS_ALIGNMENT.md
FORMAT_EMPIRICAL_REVIEW.md
SEMANTIC_EQUIVALENCE_SPEC.md
CLOSED_LOOP_VERIFICATION_SPEC.md
INTEGRATION_RECOMMENDATIONS.md
UNVERIFIED_AND_CONFLICTING_CLAIMS.md
```

Every file must distinguish:

- `established_standard`
- `research_derived_parameterization`
- `project_specific_synthesis`
- `empirical_repository_finding`
- `unverified`

## Acceptance criteria

- Explicit verdict on universal seven-phase claim.
- Explicit distinction between BML seven sync points and any project phase model.
- Six Bartenieff patterns covered with source/caveat/proxy mappings.
- BML and EmotionML conformance claims bounded accurately.
- Contradictory format-effect findings represented, not averaged away.
- Every recommendation points to an existing repository owner or a justified minimal new artifact.
- No new parallel canonical ontology is proposed.
- No real-world harm optimization or protected-trait inference.
- Source and claim counts reported by evidence class.
