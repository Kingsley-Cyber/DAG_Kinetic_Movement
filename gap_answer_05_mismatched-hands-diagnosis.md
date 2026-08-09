# Why AI Video Adds Extra Or Mismatched Hands

Researched: 2026-08-09

## Short Diagnosis

The likely root cause is identity ambiguity. The prompt describes two physical hands, but it gives them three changing role labels: `zipper_hand`, `anchor_hand`, and `lip hand`. Across shot or beat changes, the model may treat those labels as separate visual agents instead of two persistent hands whose jobs change over time.

The fix is to keep the identity labels stable:

- Use `left hand` and `right hand` only.
- Describe changing actions on the same named hand.
- Keep contact continuous during transfers.
- Avoid reintroducing a hand from offscreen without restating that it is the same hand.

## Why This Particular Prompt Is Fragile

### 1. Role renaming creates extra actors

When one prompt says `zipper_hand`, another says `anchor_hand`, and a later beat says `lip hand`, the visual model has to infer whether those are job labels or separate entities. In a scene with no face, body, or wider context anchoring identity, hands become the main characters. Any identity ambiguity lands directly on the hands.

Better:

> The right hand grips the zipper pull. The left hand braces the bag. The right hand, same hand, slides from the zipper pull to the front lip and grips it.

Worse:

> The zipper hand releases the pull. The anchor hand holds the bag. The lip hand grasps the front lip.

### 2. Empty-hand transfer invites hallucination

The action "release pull -> reach -> grasp lip" creates a moment where one hand holds nothing. During that open-air reach, the model can lose track of which hand is moving, especially if another hand is already visible and stationary.

Better:

> The right hand keeps light contact with the bag, sliding along the fabric from the zipper pull to the front lip, then gripping the lip.

### 3. Hard cuts re-sample identity

Hard cuts ask the model to regenerate the scene state. If the hands are the main subject, each cut is another chance for hand count, pose, side, or appearance to drift.

OpenAI's Sora prompting guidance says motion is often the hardest part to control and recommends simple, clear subject action with timing broken into beats. It also notes that when important details are left open, Sora will infer them. Source: [Sora 2 Prompting Guide](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide).

### 4. Hands exiting and re-entering frame reset continuity

If a hand leaves through the bottom of frame and later returns, the model may not preserve its identity unless the prompt explicitly says it is the same physical hand.

Better:

> The right hand dips partly below the bottom edge, then returns as the same right hand, still bare and unadorned.

### 5. POV forearms have a competing visual prior

A POV shot with forearms visible should contain the wearer's two hands. But many training examples of bags, zippers, and manipulation are third-person shots where another hand can enter from the center or side. If the prompt is ambiguous, the model may satisfy both interpretations.

### 6. Hand-object contact is technically hard

Research on hand-object interaction repeatedly identifies contact, occlusion, temporal synchronization, and physically plausible grasping as hard problems. DiffH2O notes that plausible hand-object interaction must satisfy geometry, semantics, and timing at once. JointHOI notes that small contact errors can create obvious artifacts such as floating and interpenetration. Sources: [DiffH2O](https://arxiv.org/html/2403.17827v1), [JointHOI](https://arxiv.org/abs/2607.01768).

## Research Support

- Hands are a known weak point in generative models. HanDiffuser lists irregular hand poses, shapes, finger counts, and physically implausible finger orientations as common artifacts. Source: [HanDiffuser](https://arxiv.org/abs/2403.01693).
- Two-hand interaction data is difficult because of self-occlusion, self-similarity, and complex articulation. Source: [HandDiffuse](https://arxiv.org/html/2312.04867v2).
- Video identity consistency is harder than image identity consistency because motion and identity features interact. Source: [Video Storyboarding](https://arxiv.org/html/2412.07750v1).
- Reference-image and character-conditioning workflows exist specifically because text alone is often not enough to preserve appearance over time. Sources: [OpenAI Sora Video Generation](https://developers.openai.com/api/docs/guides/video-generation), [Veo Reference Images](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/use-reference-images-to-guide-video-generation).

## Bottom Line

This is not just "AI is bad at hands." It is a stacked failure:

- Ambiguous role labels.
- A contact break.
- Hard cuts.
- Hand exits and re-entries.
- POV framing.
- A high-degree-of-freedom object-contact task.

The highest leverage fix is to reduce the model's identity burden: two stable hand labels, one continuous contact path, fewer action changes per clip, and start/end or reference frames when available.
