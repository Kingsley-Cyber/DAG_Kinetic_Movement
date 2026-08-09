---
id: cpcs.runtime.cross_format_compiler_reference
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 Appendix G]
primary_route: cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.runtime.typed_merge_algebra
  - cpcs.runtime.capability_negotiation_protocol
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.mx_compiler
---

# Cross-Format Compiler Reference

> Distilled from CPCS paper Appendix G. Implementation-oriented reference for
> the cross-format CPCS compiler: representation roles, canonical fields,
> style domain registry, compiler pseudocode, and 14-item acceptance checklist.

## Representation roles

| Representation | Normative CPCS role | Unresolved inheritance? | Primary validator | Typical output |
| --- | --- | --- | --- | --- |
| YAML | Human authoring, styles, imports, variants, overrides | Yes | Restricted YAML parser + CPCS authoring schema | canonical JSON |
| JSON | Fully resolved canonical score, schemas, patches, reports | No in canonical score | JSON Schema + semantic validator | target package or evidence |
| XML | Ordered director/narrative envelope, namespaced annotations | Yes, only through explicit CPCS refs | XML parser, namespace checks, XSD | authoring AST or canonical JSON |
| JSONL | RAG, compiler events, metrics, experiments, audits | N/A per line | Line-level JSON Schema + stream rules | searchable evidence stream |
| Binary/media | Dense motion, images, video, audio, render passes | No semantic inheritance | Format-specific validator + manifest | native model or production input |

## Required canonical fields

A canonical CPCS JSON document SHOULD contain: `schema_version`,
`ontology_version`, `document_id`, `document_revision`, `timebase`,
`coordinate_system`, `actors`, `assets`, `beats`, `effective_styles`,
`tracks`, `constraints`, `adapter_extensions`, `provenance`,
`rights_and_approvals`, `content_digest`.

`effective_styles` MUST contain resolved values. Source-level `extends` and
`overrides` MUST NOT remain as unresolved instructions. `provenance` MUST
retain enough information to reconstruct why each effective field exists.

## Style domain registry (10 domains)

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
| `/style/marketing` | product priority, claim density, CTA profile | typed deep merge w/ locked approvals |

## Cross-format package example

A complete package combines:
- `project.yaml` — YAML authoring with imports, extends, targets, variants
- `sequence03.xml` — XML director envelope with namespaced face/camera events
- `shot014.body.json` — JSON body track with contact events and content digest
- Resolved `shot014.cpcs.json` — canonical JSON with provenance pointers
  linking each field back to its source (XML direction, YAML style, JSON body)

## Reference compiler pseudocode

```python
@dataclass(frozen=True)
class CompileResult:
    canonical_score: dict[str, Any]
    target_package: dict[str, Any]
    resolve_report: dict[str, Any]
    compile_report: dict[str, Any]

def compile_cpcs(source_uri, target_profile_uri) -> CompileResult:
    source = parse_by_media_type(source_uri, restricted=True)
    validate_authoring_syntax(source)
    graph = build_dependency_graph(source)
    verify_digests_licenses_and_rights(graph)
    ast = normalize_sources_to_semantic_ast(graph)
    resolved, resolve_report = resolve_typed_inheritance(ast)
    reject_hard_conflicts(resolve_report)
    canonical = normalize_units_time_and_coordinates(resolved)
    validate_json_schema(canonical, schema="cpcs/1.1")
    validate_cross_field_semantics(canonical)
    validate_constraint_feasibility(canonical)
    canonical = attach_field_provenance(canonical, resolve_report)
    canonical_digest = canonicalize_and_hash_json(canonical)
    target_profile = load_and_validate_capability_profile(target_profile_uri)
    plan = negotiate_capabilities(canonical, target_profile)
    reject_unsupported_hard_controls(plan)
    package, compile_report = emit_target_package(canonical, plan)
    verify_package_alignment(package, canonical["timebase"])
    attach_manifest(package, canonical_digest, target_profile)
    return CompileResult(canonical, package, resolve_report, compile_report)
```

Every function has an observable failure mode. No semantic step should be
hidden inside a final prompt string.

## Compile-report schema

Each control mapping records: `control_id`, `source_path`, `importance`
(hard/soft/hard_target_soft_tolerance), `status` (one of 8 capability
statuses), `outputs` (file paths), `losses` (what was degraded), and
`verification` (metric names for post-hoc checking).

## Capability profile schema

Required fields: `id`, `model_id`, `verified_on`, `accepts`. Each entry in
`accepts` declares `support` (native, model_specific, approximate, none) and
optional `constraints`. Profiles are versioned and dated because hosted
video-analysis APIs can change.

## Direct-prompt templates (3 formats)

For prompt-only or LLM-mediated use (not a replacement for compilation):

- **YAML-oriented**: shot, subject_action, face, body_quality, camera,
  constraints as YAML fields
- **JSON-oriented**: same semantic summary as JSON object with must_not array
- **XML-oriented**: same summary with namespaced elements (face, body, camera,
  avoid)

Relative effectiveness depends on the interpreter and target model.

## 14-item acceptance checklist

1. Can the parser identify the schema and reject duplicate/unsafe constructs?
2. Can every import be resolved to a pinned version and digest?
3. Can the resolver explain every inherited value and lock?
4. Does every inheritable path declare a typed merge policy?
5. Are ordered events represented by arrays or explicit timestamps?
6. Are null, missing, and delete distinguished?
7. Can the canonical JSON validate structurally and semantically?
8. Can the compiler state exactly what each control became?
9. Does the target profile identify unsupported controls before generation?
10. Are prompt text, API parameters, media controls, post events, and
    evaluation targets separated?
11. Do all control passes share one timebase and frame identity?
12. Does every generated variant have a content hash, model/adapter version,
    and measurement identifier?
13. Can a reviewer revise one field through an auditable patch without
    rewriting the entire shot?
14. Are safety and rights gates checked before any generation step?

## Polyglot compiler (SRC-011 EXTEND)

> **Source:** SRC-011 §17 — "Polyglot compiler" +
> `examples/dual_format_patterns.md`.

### Carrier ownership (semantic ownership rule)

One authoritative source per semantic path per stage. When two formats are
combined, each path is owned by exactly one carrier:

| Carrier | Owns |
| --- | --- |
| NL | intent, audience effect, observable behavior |
| YAML | authoring, policy, profiles, imports, variants, invariants |
| JSON | canonical resolved data (numeric authority) |
| XML | ordered narrative, namespaced events, approvals |
| JSONL | append-only evidence stream |
| Media | dense assets (motion, images, video, pose) |

Embedded duplicate authority is rejected (dual_format_patterns.md's invalid
example: `camera.lens_mm: 50` plus `embedded_json` with 85) unless one value
is an explicit typed override. Two formats may not silently own the same
semantic path.

### Valid dual-format patterns

- **YAML + JSON:** YAML owns intent and import policy; JSON owns the dense
  body track (referenced via import + JSON Pointer).
- **XML + JSON:** XML owns narrative order and annotations; JSON owns the
  resolved score (referenced via `cpcs:score` href + digest).
- **YAML + XML:** YAML owns build policy and reasoning profile; XML owns the
  ordered screenplay and triggers.

### Direct multi-format prompting

Pasting structured text directly into a prompt field is
`text_interpretation_only` — prompt rhetoric, not schema enforcement
(equivalent to Mode A in structured_prompting_architecture). It is never
labeled as native control.

### Fifteen cross-format compile passes

1. parse each input under its declared version; 2. reject duplicate
keys/names; 3. validate against pinned schema; 4. resolve imports (pinned +
hashed); 5. resolve YAML/XML references and JSON Pointers; 6. enforce one
authority per semantic path; 7. normalize IDs, units, timebase, coordinates;
8. preserve provenance for every imported value; 9. report conflicts instead
of resolving them by document order; 10. resolve typed inheritance; 11.
apply scoped typed overrides; 12. canonicalize and hash; 13. negotiate
target capabilities; 14. emit target package (prompt/API/media/post); 15.
attach compile-loss report per canonical control. Passes 1–12 extend the
14-pass YAML→JSON reference above with cross-format (YAML+JSON, XML+JSON,
YAML+XML) handling.
