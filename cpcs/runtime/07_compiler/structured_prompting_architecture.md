---
id: cpcs.runtime.structured_prompting_architecture
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §19]
primary_route: cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.constraint_compilation
  - cpcs.runtime.text_compilation
---

# Structured Prompting Architecture

> Distilled from CPCS paper §19 (~1,900 lines). This is the most detailed section
> of the paper and defines how CPCS compiles directorial intent into actual video
> model inputs. It is the architectural backbone of the entire framework.

## Core distinction: Serialization ≠ Control

YAML, JSON, XML are data-serialization languages. They describe how information
is written and exchanged. They do not, by themselves, define the cinematic meaning
of `AU04`, `bound_flow`, `impact_frame`, or `hero_product_reveal`. Five levels of
"structured understanding" must be distinguished:

1. **Software understands an API protocol** — service receives bytes, parses fields, checks types
2. **A text encoder tokenizes a prompt** — characters become token IDs (no formal semantics guaranteed)
3. **A multimodal model consumes tensors** — text tokens + image latents + audio features → numerical arrays
4. **A model may have learned conventions** — if training data exposed it to tagged descriptions
5. **A compiler can create actual control** — maps validated field to native parameter, with verification

CPCS defines control as: for source field \(x\), target adapter \(A\), generated artifact \(Y\):
\[A(x) \rightarrow \{z_1, z_2, \ldots, z_k\}\]
where each \(z_j\) is a supported prompt clause, API parameter, control asset, latent condition,
simulation target, compositor operation, or evaluation constraint. The system must record whether
the mapping was exact, approximate, baked into a reference, reduced to prose, or unsupported.

## Four modes of structured direction

| Mode | Description | Reliability |
| --- | --- | --- |
| A | Structured text pasted directly into prompt field | Prompt rhetoric, not schema enforcement. Appropriate for rapid exploration. Label `text_interpretation_only`. |
| B | LLM-mediated interpretation — LLM reads structured source, produces target prompt | Non-deterministic. Must require structured output against schema, compare with input, generate loss report. |
| C | Deterministic compiler and workflow engine — parses, resolves, validates, negotiates, emits | Can guarantee field mapping, temporal ordering, lock preservation, unsupported control warnings. |
| D | Native structured conditioning — model natively accepts first/last frames, pose, depth, masks, camera paths | Strongest control. Field-specific: model may accept duration but not AU curves. |

Mode C is deterministic for the **translation process**, not the generated video.
A stochastic video model may still produce different pixels across runs.

## Three-Representation Architecture + Evidence Stream

```text
Authoring Source Layer (ASL)
  YAML, XML, screenplay text, storyboard references, measured JSON tracks
                         │
                         ▼
Canonical Intermediate Representation (CIR)
  fully resolved, typed, unit-normalized CPCS JSON
  No unresolved extends/overrides. Provenance for every effective field.
                         │
                         ▼
Target Execution Package (TEP)
  model request JSON + prompt text + media/control assets + post/VFX/edit plan
                         │
Verification Evidence Records (VER)
  JSONL compliance, metrics, contradictions, human review
```

### Representation roles

| Representation | Role | Unresolved inheritance? | Validator |
| --- | --- | --- | --- |
| YAML | Human authoring, styles, imports, variants, overrides | Yes | Restricted YAML parser + CPCS schema |
| JSON | Fully resolved canonical score, schemas, patches, reports | No in canonical | JSON Schema + semantic validator |
| XML | Ordered director/narrative envelope, namespaced annotations | Only through explicit CPCS refs | XML parser + namespace checks + XSD |
| JSONL | RAG, compiler events, metrics, experiments, audits | N/A per line | Line-level JSON Schema |
| Binary/media | Dense motion, images, video, audio, render passes | No semantic inheritance | Format-specific + manifest |

## Six typed control contracts

Each domain has distinct schemas, compilation targets, and verification:

| Domain | Key fields | Compilation target |
| --- | --- | --- |
| FACS | AU intensities, onset/apex/offset, asymmetry | Face rig, landmarks, expression reference, text |
| Laban | Weight, Time, Space, Flow, Shape | Style conditioning, retiming, motion retrieval |
| Combat/Action | Action atoms, phases, contacts, causal graph | Motion graph, choreography, pose constraints |
| Director/Editorial | Shot scale, camera move, cut timing, reveals | Camera path, EDL, first/last frames, prompt |
| VFX/Anime | Effect events, masks, particles, smear policy | Compositor graph, masks, prompt, post |
| Marketing | Product visibility, CTA, proof order, hook timing | Shot ordering, visibility constraints, variants |

## Eleven style domains (not one adjective string)

Each has independent inheritance and typed merge policy:

| Domain path | Representative fields | Default merge |
| --- | --- | --- |
| `/style/visual` | medium, palette, contrast, texture, era | typed deep merge |
| `/style/performance` | acting scale, gesture amplitude, externalization | typed deep merge |
| `/style/affect_display` | suppression, leakage, recovery | replace per field |
| `/style/motion` | realism, smoothness, microvariation | replace or explicit delta |
| `/style/laban` | Weight, Time, Space, Flow, Shape | replace per dimension |
| `/style/cinematography` | camera grammar, lens family, framing | typed deep merge |
| `/style/editorial` | pace, cut bias, holds, time warp | keyed/timeline merge |
| `/style/vfx` | effect language, shake, trails, smear policy | keyed-event merge |
| `/style/audio` | dynamics, breath, impacts, ambience | typed deep merge |
| `/style/marketing` | product priority, claim density, CTA profile | typed deep merge with locked approvals |

## Scope cascade

7 levels: studio defaults → project → sequence → scene → shot → beat → event/frame.

6 authority classes (highest to lowest):
1. **Safety** — never overridden
2. **Asset identity** — locked references, rig integrity
3. **Continuity** — cross-shot consistency
4. **Director hard** — explicit director overrides
5. **Department** — FACS, Laban, camera, VFX, audio, marketing
6. **Adapter** — model-specific constraints

## 14-pass YAML-to-JSON compilation

1. Parse YAML (restricted parser — no arbitrary tags, no merge keys)
2. Reject unsafe constructs (arbitrary Python objects, cyclic references)
3. Validate against authoring schema
4. Resolve imports (URI → content, SHA-256 verification)
5. Resolve aliases (YAML anchors are serialization devices, not inheritance)
6. Expand `extends` (typed merge per path, per style domain registry)
7. Apply overrides (scoped, typed, provenance-tracked)
8. Normalize units, timebase, coordinate systems
9. Resolve cross-document references
10. Materialize defaults (from profile, studio, schema)
11. Validate semantics (cross-field, constraint feasibility, reference resolution)
12. Emit canonical JSON
13. Canonicalize and hash (deterministic serialization for content addressing)
14. Emit reports (resolve report, compile report, conflict report)

## 8 verification checkpoints

1. Source parse and schema validation
2. Import resolution and digest verification
3. Inheritance resolution (every inherited value traceable)
4. Unit and timebase normalization
5. Cross-field semantic validation
6. Constraint feasibility check
7. Capability negotiation (unsupported controls reported before generation)
8. Post-compilation package alignment (timebase, frame identity, content hash)

## What structured languages still cannot guarantee

1. Semantic understanding by the model (Mode A/B only)
2. Physical plausibility (requires motion/physics solvers)
3. Aesthetic quality (requires human review or learned evaluator)
4. Identity preservation (requires dedicated verification)
5. Temporal coherence across shots (requires editorial assembly)
6. Cultural appropriateness (requires human review)
7. Legal compliance (requires rights review)
8. Deterministic video output (model is stochastic)

## RAG design for compiler knowledge

The compiler should retrieve: concept cards, movement atoms, performance templates,
shot templates, calibration profiles, source provenance, failure cases. Retrieval
constrained by: body part, action, affect, Laban qualities, contact structure,
camera grammar, duration, evidence level, licensing.
