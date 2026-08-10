# Shot Decomposition Rules

## Objective

Decomposition converts one underdetermined, overloaded generation problem into several bounded problems with explicit state handoffs. It is not merely shorter prompting. Every split must preserve identity, state, geography, event causality, audio, and edit intent across the boundary.

## Mandatory split conditions

Split the clip—or use source/control media—when a hard requirement depends on any of the following and no continuous control signal is available:

- complete opaque occlusion with a production-critical hidden trajectory;
- two or more similar actors crossing, grappling, or swapping depth lanes;
- precise contact plus a complex camera move or full-frame effect;
- more dependent events than the provider/task has empirically qualified;
- irreversible object/material transition followed by a cut or long absence;
- graphic/anime deformation requiring a guaranteed recovery frame;
- deterministic product geometry, logo, handoff, or state change;
- frame-accurate dialogue, impact, or music synchronization;
- a provider prompt budget that cannot retain all hard controls;
- one failed interval inside an otherwise accepted artifact when an edit-capable workflow can preserve the rest.

## Preferred cut points

Use boundaries where state is fully observable and low-velocity:

- before complete occlusion begins;
- after a landing, settle, recoil, or recovery;
- before actors cross the action axis;
- after a prop release and before a new acquire;
- before a full-frame flash/splash/smoke wipe;
- at a neutral establishing view before a reverse angle;
- on a musical beat only when the visual handoff state is also explicit.

Avoid cuts in the middle of ambiguous contact, during untracked possession transfer, or while identity is fully hidden unless the next shot starts from a strong keyframe/reference.

## Handoff contract

Every shot boundary records:

```text
outgoing frame/artifact hash
incoming reference/keyframe hash
entity IDs and actor count
identity and costume signatures
object inventory and possession
world layout and screen/depth lanes
pose, velocity, support, and recovery state
material/effect state
camera pose/lens/motion state
ordered unfinished dependencies
terminal state of the outgoing shot
initial state of the incoming shot
allowed edit discontinuities
forbidden world-state discontinuities
verification assertions across the seam
```

## Decomposition patterns

### Hidden-state bridge

```text
shot 1: entry trajectory remains visible → cut before total cover
shot 2: effect plate or short opaque transition
shot 3: authored reappearance keyframe → continuation and recovery
```

### Interaction plate plus effects

```text
generate or film clean choreography with readable silhouettes
→ verify contact/near-contact, roles, and state
→ add splash/smoke/flash/shake in V2V or compositing
→ reverify identity, count, effect origin, and seams
```

### Multi-actor role preservation

```text
establish distinct actors and lanes
→ isolate one primary exchange per shot
→ use neutral re-establishing shot before screen-side reversal
→ maintain role and object ledgers across every cut
```

## Assembly verification

The assembled sequence must be verified as one artifact. Passing each clip separately is insufficient: identity, object state, screen direction, audio phase, camera continuity, and material state can fail only at the seam.
