# Minimum Sufficient Representation

## Evidence-backed answer

There is no representation that can **guarantee** a stochastic generative model will never invent information. The minimum sufficient CPCS representation is instead the smallest target that removes avoidable ambiguity, exposes unsupported obligations, selects the right conditioning carrier, and makes every critical failure observable.

For a visually ambiguous transition, that target must contain at least:

### 1. Persistent entity identity

```text
stable entity_id
entity type
actor/object count
identity/costume/body/voice signature
role
existence separate from visibility
allowed and forbidden identity/state changes
```

### 2. State ledger

```text
initial state
state at each critical beat/shot boundary
irreversible deltas
object inventory and possession
material/environment state
terminal state
invariants that remain true through occlusion and cuts
```

### 3. Ordered event graph

```text
initiator
target
action
onset
apex
consequence
reaction delay
recovery
before / only_after / while / causes / prevents / terminates edges
```

### 4. Spatial state transition

```text
explicit coordinate frame
world position versus screen projection
screen and depth lanes
camera pose/motion/lens state
entry trajectory
expected target/reappearance region
axis, eyeline, and crossing rules
```

### 5. Visibility and hidden-state contract

```text
occluder and subject IDs
start/end of partial or complete occlusion
subject remains existing while invisible
hidden motion path or control reference
visibility bridge when available
required reappearance state and region
actor/object count lock
```

### 6. Interaction, support, and material contract

```text
contact type or near-contact cheat
contact target region and interval
minimum separation / penetration tolerance
support foot or surface
momentum/reaction/recovery obligations
material impact origin, displacement, topology, and effect lifetime
```

### 7. Graphic, edit, and deformation contract

```text
cut versus flash versus smear versus occlusion
whether world time advances
whether world state may change
allowed stylized deformation interval
required anatomy/style recovery frame
```

### 8. Audio anchors

```text
sound/speech/music event ID
visual cause or off-screen classification
speaker/voice identity
target onset and permitted offset
```

### 9. Provider realization and loss

```text
exact provider/model/version/interface
supported carrier for each hard control
prompt/reference/control asset projection
rewrite/enhancement setting
unsupported/evaluation-only controls
character/token budget and overflow decision
```

### 10. Verification assertions

```text
failure/metric ID
artifact and interval
observable lane
method/evaluator/version/configuration
threshold policy
known blind spots
human-review requirement
critical versus advisory severity
```

## When prompt-only generation remains reasonable

Prompt-only is reasonable when the scene has a small number of visually distinct persistent entities; primary events are simple and mostly visible; spatial relations do not require an exact hidden path; contact and physical consequences are perceptual rather than geometric; the camera is simple; the terminal state is easy to state; and failures can be tolerated or cheaply regenerated.

## When to escalate to references

Use reference images/storyboards when identity, product geometry, wardrobe, layout, first/last pose, style, or reappearance state must be visually anchored but the time-varying path remains flexible.

## When to escalate to control media

Use masks, pose, points, depth, trajectories, camera paths, beat/audio tracks, or source/control video when a hard requirement is time-varying and not continuously observable from text: hidden motion, precise path, multi-actor assignment, contact geometry, camera motion, lip sync, or material/effect origin.

## When to split the shot

Split when dependency depth, action density, actor similarity/crossings, complete occlusion, contact, camera motion, effects, and audio anchors combine beyond the measured provider/task envelope; when the prompt budget cannot retain all hard controls; or when a clean state handoff is cheaper than asking the model to infer an invisible transition.

## When to use postproduction

Use deterministic postproduction for exact splash/smoke/flash/shake/audio timing, logos/text, precise object count and product geometry, clean occlusion used to hide a safe edit, or material effects whose topology and causal origin must be exact.

## When to declare unsupported

Declare unsupported when no available provider or controlled workflow can carry and verify the hard requirement at an acceptable success rate and cost. The correct system output is an explicit limitation and alternative production plan, not an overconfident prompt.


## Decision summary

Prompt-only generation should be abandoned as soon as a production-critical requirement depends on information that is invisible, geometric, time-varying, tightly synchronized, or not carried by the selected provider interface. References anchor appearance and boundaries; control media carries paths and geometry; shot decomposition converts hidden transitions into observable handoff states; postproduction guarantees deterministic effects and synchronization; unsupported status is correct when no qualified workflow clears the gate.
