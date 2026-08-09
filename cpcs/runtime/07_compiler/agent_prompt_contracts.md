---
id: cpcs.runtime.agent_prompts
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-008 §prompts/]
primary_route: cpcs/runtime/07_compiler/
secondary_routes:
  - cpcs/runtime/04_synthesis/
interfaces:
  - cpcs.runtime.text_compilation
  - cpcs.verification.measurement_record_form
  - cpcs.style.anime_sakuga
  - cpcs.body.superhuman_transform
---

# CPCS-MX Agent Prompt Contracts

> Distilled from the frozen package's `prompts/` directory: text-to-CPCS-MX,
> verifier, style-transfer, and XML request envelope.

The package defines three logically separate agent roles with distinct prompt
contracts. **Do not let one model silently perform all three roles while hiding
assumptions.**

## 1. Text-to-CPCS-MX Semantic Authoring Agent

| Field | Value |
| --- | --- |
| prompt_id | `prompt.cpcs-mx.text-to-structure.v1` |
| output_contract | CPCS-MX authoring YAML or candidate JSON |
| safety_scope | virtual animation and professionally staged screen action |

### Role

Translate directorial or movement language into a candidate CPCS-MX authoring
document. The agent is a **semantic compiler, not the final numerical solver**.
Preserve ambiguity rather than inventing exact values.

### Required reasoning products (13)

1. intent, objective, tactic, and subtext when present
2. ordered action graph
3. phases and temporal relations
4. subjects, targets, contacts, and support states
5. root and key-joint requirements (explicitly stated or necessary for locked contacts)
6. Laban Body–Effort–Shape–Space descriptors with intervals
7. FACS-like facial events, gaze, head, blink, and breath
8. mannerism and character-profile references
9. style and superhuman transformations as typed dimensions
10. camera, edit, VFX, audio, and marketing controls when relevant
11. hard, soft, and perceptual constraints
12. verification metrics and acceptance gates
13. assumptions, defaults, alternatives, and unresolved ambiguities

### Non-negotiable distinctions

- JSON, YAML, XML are not executable motion by themselves.
- Qualitative Laban terms are not universal physical constants.
- FACS AUs are not proof of emotion, deception, or intent.
- Stylized hyperextension is never applied to a human anatomical or rig-safe joint
  limit; use a declared virtual deformation layer.
- Combat defaults to `staged_near_contact` unless authorized virtual collision is
  explicitly required.
- Unspecified timing uses ranges or `null` plus `requires_resolution`.

### Quality gate

Before returning: all actions have actors; all contacts have sites and time/phase
anchors; all numbers have units; temporal relations do not contradict; style fields
do not overwrite anatomy; hard constraints are testable; unsupported controls are
listed.

## 2. CPCS-MX Verification Agent

| Field | Value |
| --- | --- |
| prompt_id | `prompt.cpcs-mx.verifier.v1` |
| output_contract | verification report JSON |

### Role

Compare generated or executed motion/video with a resolved CPCS-MX score. **Do not
alter targets or thresholds.** Localize failures by layer.

### Procedure (10 steps)

1. Validate all input schemas and hashes
2. Align source and output clocks without silently time-warping locked events
3. Match entities and joints using stable mappings
4. Measure action order and phase boundaries
5. Measure root, joint, contact, support, and camera errors
6. Evaluate joint limits, penetration, foot slip, and recovery
7. Evaluate Laban proxy, face, gaze, blink, breath only where visibility permits
8. Evaluate style invariants separately from style intensity
9. Report every hard-constraint violation
10. Classify each field as `pass`, `fail`, `unobservable`, `unsupported`, or
    `inconclusive`

### Output layers (8)

semantic · temporal · kinematic · contact · dynamic · performance · style ·
presentation

### Prohibitions

- Do not raise thresholds after seeing the candidate
- Do not call a missing observation a pass
- Do not infer force from visual impact alone
- Do not infer internal emotion from FACS
- Do not replace a locked score value with the generated output

## 3. CPCS-MX Cross-Style Transformation Agent

| Field | Value |
| --- | --- |
| prompt_id | `prompt.cpcs-mx.style-transform.v1` |
| output_contract | typed style-transform JSON plus loss report |

### Role

Transform a resolved motion score from one style to another while preserving
declared invariants. Operate on **typed domains**, not one global style scalar.

### Required transformation domains (6)

1. **temporal** — anticipation, execution, holds, recovery, overlap
2. **spatial** — root path, arcs, reach, silhouette, perspective
3. **dynamic** — virtual gravity, impulse, damping, recovery
4. **deformation** — mesh, squash/stretch, smear geometry, rig policy
5. **performance** — Laban phrasing, mannerism retention, FACS amplitude/timing
6. **presentation** — camera, edit, VFX, audio emphasis

### Invariants (never changed without explicit unlock)

action order · participant identity · critical contacts · safety classification ·
rights replacements · recovery completion

### Rule

A request such as "30% more superhuman" must be decomposed into named dimensions.
Do not directly enlarge anatomical joint limits; use a nonhuman rig or a separate
stylized deformation layer.

## 4. XML Agent Request Envelope

`cpcs_mx_agent_request.xml` — a strongly delimited semantic envelope for directing
an LLM compiler. XML wraps the agent request; it is not used for dense motion. The
envelope separates role instructions, context, and output contract into
delimited sections.
