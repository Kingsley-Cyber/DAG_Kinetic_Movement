# Dual-Format Patterns

## YAML + JSON: authoring plus canonical data

```yaml
imports:
  - id: body_track
    uri: asset://motion/shot04.body.cpcs.json
    media_type: application/cpcs+json
    sha256: "..."
shot:
  intent: "concealed fear during approach"
  tracks:
    body:
      ref: "body_track#/tracks/body"
      preserve_contacts: true
```

Ownership: YAML owns intent and import policy; JSON owns the dense body track.

## XML + JSON: ordered envelope plus numerical authority

```xml
<adrg:directorPackage xmlns:adrg="urn:cpcs:adrg:1.0"
                      xmlns:cpcs="urn:cpcs:core:1.1">
  <adrg:brief>Recognition must coincide with the final plant.</adrg:brief>
  <cpcs:score href="asset://scores/shot04.cpcs.json"
              mediaType="application/cpcs+json" sha256="..."/>
</adrg:directorPackage>
```

Ownership: XML owns narrative order and annotations; JSON owns the resolved score.

## YAML + XML: project policy plus ordered screenplay

```yaml
project:
  id: filmA
  reasoning_profile: planner.standard.modular.v1
sequence:
  envelope:
    uri: authoring://scene12.xml
    media_type: application/cpcs-adrg+xml
    sha256: "..."
```

Ownership: YAML owns build policy; XML owns ordered screenplay and triggers.

## Invalid dual authority

```yaml
camera:
  lens_mm: 50
  embedded_json: '{"camera":{"lens_mm":85}}'
```

This is rejected unless one value is an explicit typed override. Two formats may not silently own the same semantic path.
