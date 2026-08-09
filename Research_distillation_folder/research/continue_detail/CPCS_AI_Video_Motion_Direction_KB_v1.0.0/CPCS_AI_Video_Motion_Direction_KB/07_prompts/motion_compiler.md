# Prompt — Canonical Motion Compiler

Compile one selected intent realization into CPCS layers. Output only a JSON object conforming to `canonical_scene.schema.json` plus a separate compiler report.

Order:

1. actors/objects/environment;
2. narrative beats and affect tracks;
3. body organization, connectivity, and BESS;
4. motion primitives and seven-phase CPCS timelines, permitting omitted phases;
5. kinematic/contact/interaction records;
6. force profile separated by measurement status;
7. rhythm, camera, and style with locked invariants;
8. constraints and target adapters.

Hard rules:

- interaction/contact causality before camera/style;
- no unsupported measurement presented as measured;
- no automatic emotion/deception conclusion from FACS;
- no style transform may alter a locked predicate/contact;
- all times within scene duration;
- every CPCS-created numeric preset labeled `CPCS_CONVENTION`.
