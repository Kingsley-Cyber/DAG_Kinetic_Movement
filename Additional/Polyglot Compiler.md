# Deep Research Prompt — Polyglot Compiler and Data-Language Effect Gap Closure

## Attached research

Use the ADRG package, AI Video Motion Direction KB, MX package, VTTS package, DMR packages, and the current CPCS repository architecture.

## Mission

Research the exact relationship between **semantic meaning** and its serialization into natural language, YAML, JSON, XML, JSONL, or hybrid carriers.

The goal is not to choose one "best prompt format."

The goal is to build an empirical and semantic doctrine for:

```text
one canonical meaning
→ multiple valid representations
→ provider-specific compilation
```

The result must teach a coding agent **when, where, and how to apply each
carrier**. A carrier is never semantic authority merely because a model or
provider accepts it. For every recommendation, identify the boundary:

```text
human authoring
configuration/inheritance
resolved internal interchange
model reasoning context
provider request
ordered multimodal envelope
observation/audit stream
```

Then connect:

```text
canonical meaning_id
→ boundary requirements
→ provider/model capability evidence
→ representation selection rule
→ deterministic serialization/projection
→ validation
→ emitted request
→ compilation-loss record
→ output measurement
→ provider-specific experiment update
```

Label each transformation as lossless, normalization-only, intentionally lossy,
experimental, or invalid. Reasoning or model behavior may influence a Director
decision, but parsing a YAML/XML/NL carrier must not silently create new
canonical meaning.

## 0. Representation boundaries and authority

Before comparing formats, produce a matrix mapping every CPCS boundary to:

- semantic authority;
- permitted carriers;
- required validator/parser;
- ordering requirements;
- provenance requirements;
- loss tolerance;
- consumer;
- fallback;
- prohibited use.

Explicitly resolve where JSONL belongs: it is an append-oriented sequence of
independent JSON records, not another canonical object format. Also distinguish
source authoring YAML from resolved JSON and provider-facing JSON parameters
that may have a completely different schema.

## 1. Semantic equivalence

Define what it means for two representations to have the same meaning.

Create a semantic equivalence model that checks:

- entities;
- values;
- temporal order;
- spatial relations;
- causal relations;
- constraints;
- invariants;
- evidence;
- provenance;
- uncertainty;
- left/right;
- hierarchy.

Show examples where byte-level differences do not matter and examples where tiny structural differences DO matter.

### Application deliverable

Define equivalence levels:

```text
exact_canonical
normalized_equivalent
behaviorally_equivalent_for_capability_scope
lossy_but_accepted
not_equivalent
indeterminate
```

Create a machine-comparable semantic manifest with stable IDs, canonical field
paths, typed values, units/frames, ordered relations, constraints, evidence,
uncertainty, and hierarchy. Define comparison rules for unordered object keys,
ordered arrays/events, numeric normalization, omission vs null vs unknown,
aliases/references, default expansion, and floating-point tolerance. Behavioral
equivalence must name its provider capability scope and may not substitute for
canonical equivalence.

Include equivalence, non-equivalence, and indeterminate examples, and show the
runtime decision caused by each outcome.

## 2. YAML

Research where YAML is useful for:

- human authoring;
- inheritance;
- profiles;
- defaults;
- overrides;
- readable configuration.

Define exact rules for:

- null;
- omission;
- inheritance;
- merge;
- list ordering;
- anchors/aliases if allowed;
- type coercion.

Show authoring examples.

### Application deliverable

Specify a safe, deterministic CPCS YAML authoring subset and resolver. Define
whether aliases/anchors, merge keys, custom tags, duplicate keys, implicit type
resolution, multi-document streams, timestamps, sets, and non-string keys are
allowed. If disallowed, name the validation error. Define precedence across
defaults, profiles, inheritance, and explicit overrides; detect cycles and
conflicts; and record the origin of every resolved value.

Show YAML authoring → resolution trace → canonical JSON, including explicit
null, omitted value, inherited value, overridden value, ordered list, and an
invalid ambiguous scalar. The application conclusion must state where YAML is
allowed and where CPCS must reject it.

## 3. JSON

Research JSON as the resolved canonical form.

Determine:

- schema strategy;
- enums;
- unions;
- discriminators;
- nullable fields;
- arrays vs keyed objects;
- references;
- versioning;
- deterministic serialization;
- hashes;
- exact field paths.

Show how JSON becomes the semantic authority while avoiding over-nesting that harms model use.

### Application deliverable

Separate semantic JSON structure from deterministic byte serialization. Define
schema dialect/version, discriminators, reference scope, canonical field paths,
ordering semantics, number handling, duplicate-key rejection, unknown-field
policy, default materialization, schema migration, and canonicalization/hashing
procedure. Explain which objects use arrays versus keyed maps based on identity,
order, cardinality, and patch behavior—not model preference alone.

Show validation, normalization, hashing, and version migration on the shared
fixture. Provide a deep-nesting pressure case and the rule for introducing a
reference or flattened projection without changing canonical ownership.

## 4. XML

Research where XML actually adds value:

- ordered event streams;
- namespaced vocabularies;
- mixed content;
- explicit nesting;
- multimodal synchronization;
- BML-like envelopes.

Do not recommend XML merely because it is structured.

Define namespace and ordering semantics.

### Application deliverable

Define the exact XML use case and prove why JSON plus an ordered array is
insufficient or less appropriate at that boundary. Specify namespaces, schema
validation, element versus attribute rules, mixed-content policy, ID/reference
integrity, event ordering, timebase, whitespace, canonicalization, parser
security, and unknown-extension behavior. External entity expansion and
untrusted document features must be explicitly addressed.

Show canonical JSON → XML projection → canonical JSON comparison for an ordered
multimodal event envelope. Include namespace collision, reordered event, missing
required timebase, and unknown-extension fixtures. If no current consumer gains
from XML, conclude `not_implementable_now` instead of inventing one.

## 5. Natural language

Research how canonical controls should become concise prose.

Determine how to preserve:

- causal order;
- temporal order;
- spatial relationships;
- motion quality;
- subject priority;
- constraints;
- continuity.

Research the failure modes of prose:

- ambiguity;
- pronoun reference;
- omitted dependencies;
- long enumerations;
- conflicting adjectives;
- overloaded style labels.

### Application deliverable

Define natural-language projection as controlled lexicalization from canonical
fields. Specify subject naming, reference resolution, explicit left/right,
temporal connectives, causal connectives, constraint wording, negation,
priority, sentence ordering, compression, and prohibited ambiguous pronouns.
Every emitted clause must link to the canonical control IDs/paths it realizes.

Show canonical meaning → clause plan → prose → semantic re-extraction →
equivalence/loss report. Include two actors with the same pronoun class, nested
timing, unsupported control expressed semantically, and a constraint that cannot
be safely shortened. Reverse extraction from prose may audit preservation but
must not replace the canonical source.

## 6. Hybrid formats

Research:

```text
YAML + JSON
XML + JSON
YAML + NL
JSON + NL
XML + NL
```

Determine when a hybrid is semantically useful versus redundant.

### Application deliverable

For every hybrid, identify the authority-bearing part, supplementary part,
join key, duplication policy, contradiction resolver, parser boundary, provider
consumer, and measured advantage. The same fact must not appear in two parts
without a deterministic precedence/equivalence rule.

Provide one useful hybrid where structured controls and prose have distinct
provider roles, one redundant hybrid rejected for token/contradiction cost, and
one contradictory hybrid that fails validation. A hybrid recommendation must be
provider/version-specific unless it is purely an internal authoring construct.

## 7. Format effect experiments

Design controlled experiments with identical canonical meaning.

Factor:

```text
model
task
carrier
length
nesting
number of constraints
number of actors
temporal complexity
causal complexity
```

Measure:

- adherence;
- omission;
- contradiction;
- schema validity;
- temporal correctness;
- causal correctness;
- left/right correctness;
- token count;
- latency;
- output variance;
- repair count.

Do not conflate formatting with model capability.

### Application deliverable

Define a pre-registered, paired experiment in which every carrier variant is
generated from the same canonical `meaning_id`. Control semantic content,
examples, instruction wording, length bands, sampling settings, seed where
available, model/provider/version, and media inputs. Factor length and nesting
separately from syntax so "format" is not a proxy for token count or complexity.

Specify null hypothesis, randomization, repeats, scoring rubric, automated and
blinded-human evaluation, confidence intervals/effect sizes, multiple-comparison
policy, stopping rule, malformed-input robustness tests, negative-result
retention, evidence date, and reprobe trigger. Report per-field preservation and
failure class, not only a global preference score.

End with an executable selection rule: which measured result changes a
provider's preferred carrier, which merely records uncertainty, and which
invalidates a claimed advantage.

## 8. Format tax

Research current evidence on formatting overhead and whether structured-output requirements can impose a "format tax."

Determine whether reasoning should happen before formatting:

```text
reason
→ resolve
→ validate
→ serialize
```

rather than forcing the model to reason directly in a syntax-constrained carrier.

### Application deliverable

Operationally decompose "format tax" into token overhead, parse/validation
failures, repair calls, latency, output truncation, omission/contradiction,
reasoning-task accuracy, and provider adherence. Compare at equal semantics and,
where possible, both equal token budget and natural full length.

Test at least `reason → resolve → validate → serialize` against direct
syntax-constrained generation, while ensuring hidden reasoning is not required
as an artifact. Define which stages are deterministic code, model calls, or
provider-native structured-output features. The conclusion must remain scoped
to the tested model/task/version.

## 9. Compiler architecture

Produce a compiler model:

```text
CanonicalScore
   ↓
RepresentationPlan
   ├── NL
   ├── YAML
   ├── JSON
   ├── XML
   └── Hybrid
   ↓
ProviderCapabilityNegotiation
   ↓
ProviderRequest
```

Define compilation-loss accounting.

### Application deliverable

Define a deterministic `RepresentationPlan` selection algorithm. Inputs must
include canonical control inventory, boundary, provider/version capability
snapshot, supported request fields, carrier constraints, experiment evidence,
required/optional control priority, token/length limits, and fallback policy.
Outputs must include chosen carrier(s), transformation sequence, validators,
emitted field/clauses, and exactly-once loss dispositions.

Show these branches:

```text
native structured field available
semantic prose approximation only
hybrid has measured advantage
required control unsupported → fail closed
optional control unsupported → omit with loss
capability stale/unknown → reprobe or conservative fallback
```

Separate canonical compiler passes, carrier serializers, provider adapters, and
experiment registry. Do not let adapter code own research semantics.

## 10. Round-trip test

Create:

```text
canonical JSON
→ YAML
→ JSON
```

and:

```text
canonical JSON
→ XML
→ JSON
```

and:

```text
canonical JSON
→ NL
→ semantic extraction
→ comparison
```

Define exactly which fields must survive and which are expected to be lossy.

### Application deliverable

Compare normalized semantic manifests rather than byte equality. For every
field/edge, declare `must_survive`, `may_normalize`, `may_drop_for_scope`, or
`not_representable`; no field may be silently lost. Define order, numeric,
reference, null/omission, uncertainty, provenance, and extension comparison.

Include positive, normalization-only, intentional-loss, contradiction,
malformed, and unknown-extension fixtures. For NL, use semantic re-extraction
only as an evaluator with confidence and human-review fallback. Give exact pass,
fail, and indeterminate criteria plus stable failure codes.

## 11. Schema sketches

Provide schemas for:

```text
representation_plan
format_variant
semantic_equivalence_report
compilation_loss
provider_carrier_capability
```

### Application deliverable

For each schema define identity, version, authority, required/optional/nullable,
enum extension, references, ordering, cross-field invariants, provenance,
evidence date, expiry, and lifecycle. Supply JSON Schema sketches, canonical
instances, authoring examples where applicable, invalid fixtures, and the
runtime consumer/decision for every non-reserved field.

Also add:

```text
meaning_manifest
carrier_variant
round_trip_report
format_experiment_run
format_experiment_result
```

Do not add a schema only to mirror another artifact; explain why each has a
distinct owner and lifecycle.

## Shared application fixture

Use one stable meaning throughout all carrier examples and experiments:

```text
Actor A strikes a drinking glass with the right forearm during a bounded time
window. The glass falls and breaks; shards persist. Actor B reacts after a
constrained latency. The camera reframes to Actor B and then reveals the shards.
Identity, screen direction, event order, causal links, and persistent state must
be preserved. At least one canonical control lacks a native provider field.
```

Assign stable IDs and exact origin labels. Create one canonical JSON source,
then derive YAML, XML when justified, NL, JSONL audit records, and at least one
hybrid. Do not hand-author semantically divergent examples. Use the same
`meaning_id` in equivalence reports, token counts, provider requests, loss
records, and evaluator results.

## Required "how to apply" output

Include these packet-specific sections in addition to the master protocol:

1. `REPRESENTATION_BOUNDARY_MATRIX` — boundary, authority, carrier, validator,
   consumer, loss tolerance, fallback, prohibited use.
2. `FORMAT_SELECTION_DECISION_TABLE` — provider capability/evidence + semantic
   requirements → RepresentationPlan.
3. `FIELD_LEVEL_EQUIVALENCE_MANIFEST` — preservation status for every shared
   fixture field and relation.
4. `END_TO_END_COMPILER_TRACE` — canonical meaning through emitted provider
   request, loss ledger, observation, and repair.
5. `MINIMAL_POLYGLOT_VERTICAL_SLICE` — JSON authority + one YAML authoring path +
   one NL provider path + round-trip/loss validators; XML only if a real first
   consumer is established.
6. `FORMAT_EXPERIMENT_PROTOCOL` — paired fixtures, controls, metrics, decision
   thresholds, and versioned conclusions.
7. `DEFERRED_SCOPE_AND_FALSIFICATION` — unproven carriers/features and evidence
   that would justify or reject them.

## Final requirement

Produce a clear conclusion on:

> What should CPCS believe about data languages, and what should remain an empirical provider-specific question?

End with `CPCS_CLOSURE_MATRIX` and `PROPOSED_AGENT_BUILD_PACKET`.


## Research execution rules

Use the attached frozen package as the primary corpus, but independently verify important claims with primary sources. Do not silently "fix" the package. Explicitly distinguish package-derived claims, external-source findings, proposed CPCS representations, and experimental hypotheses.

The objective is not a literature review. The objective is to close implementation-relevant semantic gaps with enough precision that a coding agent can extend the existing CPCS tree without inventing a competing authority.

You MUST apply the output contract in `00_MASTER_DEEP_RESEARCH_PROTOCOL.md`.
