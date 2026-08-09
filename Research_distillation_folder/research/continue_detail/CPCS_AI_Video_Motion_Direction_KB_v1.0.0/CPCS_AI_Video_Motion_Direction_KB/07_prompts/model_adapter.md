# Prompt — Capability-Aware Model Adapter

Inputs: validated canonical scene, one dated adapter snapshot, relevant derived weights, and available references.

Return:

```json
{
  "adapter_id": "",
  "request": {},
  "rendered_prompt": "",
  "reference_plan": [],
  "postprocess_plan": [],
  "loss_report": {
    "native": [],
    "reference_conditioned": [],
    "prompt_only": [],
    "postprocess": [],
    "unsupported": [],
    "unknown": [],
    "risks": {}
  },
  "validation": {"errors": [], "warnings": []}
}
```

Never invent an API field. Use only the adapter snapshot. If a field name or capability is unknown, keep it unknown and produce a conceptual request for human/API implementation. Block legacy/expired adapters according to policy.
