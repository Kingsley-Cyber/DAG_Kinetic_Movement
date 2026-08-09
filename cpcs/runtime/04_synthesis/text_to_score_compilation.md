---
id: cpcs.runtime.text_compilation
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §24]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.constraint_compilation
  - cpcs.found.evidence_two_axis_model
---

# Text-to-CPCS-MX Compilation

> **Source:** SRC-005 §24 — "Text-to-CPCS-MX compilation"

## Principle

Natural language remains the most accessible directorial interface. The
problem is not that prose is useless; it is that prose under-specifies time,
geometry, authority, and conflict resolution. A text-to-CPCS-MX compiler
should preserve the expressive advantages of language while refusing to
fabricate precision that the director did not provide.

## Compilation stages

```text
source request
→ discourse and shot segmentation
→ entity and role resolution
→ action/event graph induction
→ temporal relation extraction
→ performance-quality extraction
→ camera/VFX/marketing extraction
→ ambiguity and feasibility analysis
→ schema population
→ constraint synthesis
→ model-specific compilation
```

Each stage emits provenance and confidence. An LLM may propose action labels
or timing intervals; a deterministic validator checks schema, units,
references, and contradictions.

## Separate intent from implementation

A compiler first recovers intent and events, then proposes implementation
candidates:

```yaml
intent:
  objective: cross without detection
  obstacle: uncertain sound behind her
  subtext: fear is actively suppressed

events:
  - quiet_locomotion
  - auditory_trigger
  - freeze
  - gaze_lead
  - controlled_turn

implementation_candidates:
  quiet_locomotion:
    root_speed_mps: [0.55, 0.75]
    laban:
      weight: light
      time: sustained
      space: direct
      flow: bound
    contacts:
      footfall_impulse_scale: low
  freeze:
    duration_s: null
    status: requires_director_or_style_default
```

The missing freeze duration is not invented as a fact. The compiler can offer
candidates based on a style profile, but the selected value is labeled
`authored_by_compiler` or `defaulted`.

## Lexicon without rigidity

A reusable lexicon maps language to candidate modules. The lexicon is
probabilistic and context-sensitive. "Heavy" may refer to body mass, perceived
Weight, impact sound, animation timing, or emotional tone. The compiler asks
which domain is intended when ambiguity affects execution; in batch mode, it
preserves alternatives.

## Temporal language

Natural-language temporal relations compile into a partial-order graph:

```text
before · after · during · overlaps · starts_with ·
ends_with · meets · contains · immediately_after
```

A scheduler assigns times subject to duration ranges, locks, and target shot
length. If the graph is inconsistent, the compiler returns the minimal
conflict set instead of choosing silently.

## Numeric grounding

Numbers in prompts require units and scope. "Move two meters" is root
displacement in declared world coordinates. "Turn 90 degrees" — root yaw or
named joint rotation? "Hold for six frames" — at which frame rate and retime
policy? "30% stronger" — which observable? The compiler normalizes quantities
to SI internally while retaining the author's expression. It does not
translate "30% stronger" into a real-world torque without an explicit
virtual-dynamics model.

## Director-facing questions and defaults

For interactive authoring, ambiguity is resolved through targeted questions.
For autonomous batch generation, the compiler uses named, versioned defaults:

```yaml
default_resolution:
  profile: cinematic_human_v2
  freeze_duration_s: 0.45
  gaze_lead_s: 0.12
  contact_mode: staged_near_contact
  uncertainty_policy: preserve_alternatives
```

An agent can reproduce the score only if it knows the default profile.

## Output contract

The LLM returns a candidate document with: schema version, source text spans
supporting each field, evidence class, confidence, unresolved terms,
alternatives, requested external assets, safety scope, and no undeclared
fields. The candidate is validated, normalized, and resolved by deterministic
code. This division uses the LLM for semantic interpretation and ordinary
software for contract enforcement.

## Reverse compilation to text

The resolved score can be summarized into a model-specific prompt, but the
compiler must distinguish **lossless controls** from **textual fallbacks**.
The exact curves remain in pose, trajectory, or rig controls. The prose is a
semantic reinforcement, not the sole carrier of timing.

## Text-to-CPCS-MX agent contract (SRC-008 EXTEND)

The frozen package defines a concrete text-to-structure agent prompt
(`prompt.cpcs-mx.text-to-structure.v1`) with 13 required reasoning products:

1. intent, objective, tactic, and subtext
2. ordered action graph
3. phases and temporal relations
4. subjects, targets, contacts, and support states
5. root and key-joint requirements (explicitly stated or necessary for locked contacts)
6. Laban Body–Effort–Shape–Space descriptors with intervals
7. FACS-like facial events, gaze, head, blink, and breath
8. mannerism and character-profile references
9. style and superhuman transformations as typed dimensions
10. camera, edit, VFX, audio, and marketing controls
11. hard, soft, and perceptual constraints
12. verification metrics and acceptance gates
13. assumptions, defaults, alternatives, and unresolved ambiguities

### Agent quality gate

Before returning, verify: all actions have actors; all contacts have sites and
time/phase anchors; all numbers have units; temporal relations do not
contradict; style fields do not overwrite anatomy; hard constraints are testable;
unsupported target controls are listed.

### Evidence labeling

Each extracted or proposed value must be labeled as one of: `measured`,
`detected`, `inferred`, `interpreted`, `authored`, `defaulted`, `derived`.

See also: `cpcs.runtime.agent_prompts` for the full 4-prompt contract set.
