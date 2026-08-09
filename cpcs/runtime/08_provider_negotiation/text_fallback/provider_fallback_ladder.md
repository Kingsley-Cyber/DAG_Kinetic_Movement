---
id: cpcs.provider.provider_fallback_ladder
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§36]
primary_route: cpcs/runtime/08_provider_negotiation/text_fallback/
secondary_routes:
  - cpcs/runtime/07_compiler/loss_ledger/
interfaces: []
---

# Provider Fallback Ladder

Unsupported abstract concepts must not simply disappear. The compiler attempts
a controlled fallback ladder:

```text
canonical semantic control
  → provider-native exact control
  → provider-native semantic equivalent     (if unavailable)
  → observable behavioral realization       (if unavailable)
  → reference/control representation         (if inadequate)
  → unsupported                              (if unavailable)
```

Each fallback creates a loss record (see capability classes loss taxonomy).

## FACS fallback

```text
FACS AU target → provider has no AU control
  → visible facial action description → provider prompt → verification
```

The provider prompt is **not** allowed to claim `"the actor feels happy"` when
the canonical target was only a facial action.

## Bartenieff fallback

```text
Cross-Lateral → provider lacks Bartenieff vocabulary
  → contralateral body-action realization → provider projection → video verification
```

## Verification

`test_unsupported_provider_control_emits_loss`.
