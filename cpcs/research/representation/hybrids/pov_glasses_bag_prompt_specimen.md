---
id: cpcs.representation.pov_glasses_bag_specimen
kind: fixture_set
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-010, SRC-012]
primary_route: cpcs/research/representation/hybrids/
interfaces:
  - cpcs.representation.prompt_structure_analysis
  - cpcs.canonical.temporal_coupling
  - cpcs.gaps.understanding_register
---

# Prompt Specimen — Smart-Glasses POV Sling-Bag Video (YAML + XML + JSON hybrid)

> **Fixture.** A real agent-produced prompt package for a 20-second vertical,
> first-person smart-glasses UGC video of a compact black sling bag. Captured
> verbatim as a reference artifact for the `representation/` route: it is the
> first known specimen using all four carriers in one document with an
> explicit authority hierarchy (`format_policy primary="yaml+xml"
> precision="json"`). See the breakdown analysis in
> [prompt_structure_analysis.md](../prompt_structure_analysis.md).

## Provenance

| Field | Value |
| --- | --- |
| Captured | 2026-08-09 (user-supplied pasted text) |
| Mode | `single_generation_long_video` (one 20 s pass, seven internal shots) |
| Source footage | none — `text_only` policy |
| Family lineage | descends from the 14.56 s sling-bag YAML + XML pair (same product, same shot beats) |
| Retiming | source clock 14.558912 s proportionally expanded to 20.0 s |
| Analysis | `cpcs.representation.prompt_structure_analysis` |

## Verbatim document

```xml
<cpcs id="sling_bag_meta_glasses_pov_20s" mode="single_generation_long_video">
  <format_policy primary="yaml+xml" precision="json" />
  <input_policy media="none" source="text_only" />
  <pov_policy camera="head_mounted_smart_glasses" subject_face="mirror_reveal_only" glasses_in_pitch="false" />

  <order>
    <shot ref="s01_pov_hook" />
    <cut ref="cut_01" type="hard" />
    <shot ref="s02_pov_design" />
    <cut ref="cut_02" type="hard" />
    <shot ref="s03_pov_zipper_setup" />
    <cut ref="cut_03" type="hard" />
    <shot ref="s04_pov_zipper_operation" />
    <cut ref="cut_04" type="hard" continuity_state="closure_released" />
    <shot ref="s05_pov_manual_opening" />
    <cut ref="cut_05" type="hard_match" />
    <shot ref="s06_pov_capacity_loaded" />
    <cut ref="cut_06" type="hard" />
    <shot ref="s07_pov_wear_mirror_endorse" />
  </order>

  <control lang="yaml"><![CDATA[
project:
  goal: create one complete 20-second vertical UGC demonstration of a compact black sling bag, filmed entirely first-person from the wearer's smart glasses
  narrative: a guy wearing camera glasses shows off a bag hands-free - looks at it, works the zipper, opens it, sees what fits, slings it on, checks the mirror
  output: vertical 9:16, 30 fps, continuous first-person POV, casual synced voiceover, exact seven-shot order
  text_only_policy: generate every subject, location, object, action, and transition from this package; no media reference is available
  timing_policy: the original 14.558912-second rhythm is proportionally expanded to 20 seconds so speech and hand actions breathe
  realism_intent: ordinary real smart-glasses footage, NOT cinematic, no film look, no color grade, no bokeh; casual, unrehearsed, hands-free
  pov_logic: the camera is the wearer's eyes - it moves only with his head, hands always enter from the bottom of frame, and his face is NEVER seen except as a mirror reflection at the end
  causal_law: the zipper and the panel are TWO SEPARATE SYSTEMS - the slider controls the closure seam; the hands control the front panel; unzipping releases the closure but never self-opens the bag
  hand_law:
    count: there are EXACTLY TWO hands in this entire video, both belonging to the wearer; a third hand never exists
    labels: refer only to the LEFT hand and the RIGHT hand; never invent a new named hand when a hand changes its job - it is still the same left or right hand
    left_hand_job: the steady hand - it holds the bag still (rear shell, then top handle) for the whole demonstration and never lets go until the bag is open
    right_hand_job: the working hand - it does everything active (pulls the zipper, then opens the panel); only ONE hand ever moves the bag at a time
    identity: bare hands, no watch, no rings, no bracelets; consistent skin tone, knuckles, and size on both hands across every cut
    reentry: if a hand leaves the bottom of frame it must return as the SAME hand in the same state; hands never pop into the middle of frame

continuity:
  wearer_reflection_only:
    note: the wearer is invisible for s01-s06 (we are inside his POV); he appears ONLY as a mirror reflection in s07
    identity: real-looking man, early-30s, seen only in the mirror; keep consistent
    face: natural asymmetry, one eyebrow slightly higher, a little tired around the eyes, light stubble; friendly, not polished
    skin_have: fine visible pores on cheeks and nose, subtly uneven skin tone, faint fine lines, slight under-eye puffiness, light T-zone oil sheen, faint natural redness by the nose - unfiltered real skin in the reflection
    skin_avoid: smooth ai skin, waxy skin, poreless, airbrushed, uniform skin tone, plastic skin, beauty smoothing, model-like symmetry, glamour lighting
    glasses_note: black Ray-Ban-style smart glasses are visible on his face in the mirror reflection; expected, never spoken about
  hands:
    present: exactly two - the wearer's LEFT and RIGHT hands, entering from the lower frame
    look: bare hands, no watch or rings; real skin, visible knuckles, five distinct fingers each, consistent scale and tone across all cuts
    rule: only one hand moves the bag at a time; the other keeps a firm hold; never a third hand, never fused or duplicated fingers
  location: bright ordinary bag shop, dark shelving and counter; a wall/full-length mirror near the counter for the final shot; real retail clutter fine; no location changes
  product: same compact black fabric sling bag every shot; orange zipper pulls; gray interior lining; stable seams, strap, silhouette, scale, compartment geometry
  capture:
    device_look: POV footage from Ray-Ban-style camera glasses; ultra-wide fixed lens, ~1080p-3K, 30 fps (30 not 24)
    fisheye: mild barrel/fisheye distortion; straight lines bow slightly near edges; center stays sharp-ish
    vantage: eye-level of a standing adult, looking slightly DOWN at his own hands and the counter; hands and bag in the lower two-thirds
    head_locked_motion: frame moves ONLY with head motion - tilts down to the hands, pans on a turn, small natural head bobs and gaze micro-shifts; NOT a handheld sway, NOT a gimbal, NO orbit
    tone: flat auto-exposure with lifted shadows; cool/neutral white balance; available shop light only; visible auto-exposure/white-balance shifts on turns
    stabilization: electronic stabilization, mostly steady but slightly swimmy at the edges; mild motion blur and rolling shutter on quick head turns
    quality: slightly soft, faint over-sharpening, minor compression artifacts; deep focus, no bokeh, no zoom, no rack focus
  captions: none baked in - leave the words for the edit

performance:
  baseline: casual telling-a-friend energy as voiceover while he looks and works; low-key, relaxed, a little amused he likes this bag this much; NOT presenting to a lens
  looseness: unrehearsed - one quick glance off and back, one small natural restart or breath; do not stage clean marks
  gaze_as_camera: what he looks at is what the frame shows; he glances between bag and shop and the frame follows
  hands_first: hands-free, so both hands work the bag naturally from the bottom of frame; hands are the main on-screen actor for s01-s06
  body: continuous subtle head motion and breathing micro-bob; the frame never freezes
  voice_arc: warm on the hook, mildly focused on the zipper, a small satisfied lift on the capacity reveal, relaxed and genuine on the close
  mirror_moment: only in s07 does he look up into the mirror; reflection shows a relaxed genuine smile (cheeks AND mouth) and a thumbs-up - the single face beat
  speech: one continuous conversational male voiceover, casual and slightly imperfect, ~185 wpm; contractions, not ad-copy

object_mechanics:
  part_graph:
    rear_shell: stable body of bag
    front_panel: attached to rear_shell by one bottom hinge and two side gussets
    zipper_slider: constrained to zipper track; cannot detach or jump
    zipper_teeth: interlocked or separated only according to slider passage
    side_gussets: folded when panel aligned; expanded when panel rotates open
    cavity: hidden behind aligned panel; progressively visible as panel rotates down
  hand_assignment:
    left_hand: STEADY hand - holds the bag still the entire time (rear shell in s03-s04, top handle in s05); never releases until the bag is fully open; does not move the bag
    right_hand: WORKING hand - the only hand that acts on the bag; it pulls the zipper, then WITHOUT losing contact slides along the bag to the front lip and opens the panel
    invariant: at every instant one hand holds and one hand works; two hands total, never three
  zipper_control:
    track:
      closed_stop: left
      open_stop: right
      invariant: only the track already passed by the slider adopts the target closure state
    unzip:
      execute_in_this_video: true
      pre: {slider: closed_stop, teeth: fully_interlocked, panel: aligned_and_secured, cavity: hidden}
      motion:
        slider: left_to_right
        right_hand: keeps its grasp on the orange pull and drags the slider once, left to right
        left_hand: stays put, stabilizing the rear shell
        left_of_slider: teeth_separated
        right_of_slider: teeth_interlocked
        seam_gap: grows_left_to_right
      post: {slider: open_stop, teeth: fully_separated, closure: released, panel: still_aligned, cavity: still_hidden}
    open_panel:
      execute_in_this_video: true
      pre: closure_released
      contact_preserving_transfer:
        - right_hand keeps touching the bag the whole time (no reaching through empty air)
        - right_hand slides from the orange pull up onto the front lip and closes into a grasp
        - left_hand slides from the rear shell to grip the top handle, still holding the bag steady
        - at no point are both hands off the bag, and at no point is a hand empty in mid-air
      motion:
        front_panel: the right hand rotates it down and outward around the bottom hinge
        side_gussets: expand_with_panel
        rear_shell: held stable by the left hand
        cavity: progressively_revealed
      post: {panel: folded_down, gussets: expanded, cavity: fully_visible, closure: open}
    close_panel:
      execute_in_this_video: false
      pre: closure_open
      motion: {front_panel: rotates_up_around_bottom_hinge, side_gussets: compress_inward, zipper_halves: align}
      post: {panel: aligned, zipper_halves: seated, cavity: hidden, closure: released}
    zip:
      execute_in_this_video: false
      pre: {slider: open_stop, panel: aligned, zipper_halves: seated}
      motion:
        slider: right_to_left
        right_hand: keeps its grasp on the pull
        left_hand: stabilizes the rear shell
        right_of_slider: teeth_interlocked
        left_of_slider: teeth_separated
        seam_gap: shrinks_right_to_left
      post: {slider: closed_stop, teeth: fully_interlocked, panel: secured, closure: shut}

shots:
  s01_pov_hook:
    purpose: hook with genuine enthusiasm, first-person, looking down at the bag in his hands
    visual: POV looking slightly down at the closed bag held in both his own hands over the dark counter; ultra-wide, mild edge fisheye; shop softly visible around it
    camera: head-locked POV; small natural head bob; one tiny gaze shift; deep focus
    spatial: bag centered in the lower-middle; his two hands (left and right) enter from the bottom edge - exactly two hands
    action: both hands cradle the bag; he turns it a little to look at it; a small breath before he talks
    dialogue: "Okay, you gotta see this bag."
    audio: close voice as if from the wearer, quiet shop room tone, a small breath before the line

  s02_pov_design:
    purpose: show the clean shape and that it holds more than it looks
    visual: POV looking down as he sets the closed bag upright on the counter; fabric, seams, panel outline, strap, orange pulls readable; edges bow slightly
    camera: head-locked POV with a slight lean-in; no orbit, deep focus
    spatial: bag centered; his two hands enter from lower edges; front stays toward camera
    action: the two hands lightly steady and trace the outside shape without squashing it; small head tilt
    dialogue: "Honestly it holds way more than you'd think, looks clean too."
    audio: same voice, shop room tone

  s03_pov_zipper_setup:
    purpose: establish the closed zipper, the two hand roles, and the direction before movement
    visual: POV closer look down at the top zipper track and orange pull as he tilts his head down; both hands visible on the bag
    camera: head-locked POV, fairly steady; zipper track horizontal across frame; slight AE shift on lean-in
    spatial: closed-stop screen left; open-stop screen right; cavity hidden
    action: the RIGHT hand forms a secure thumb-and-index grasp on the orange pull; the LEFT hand holds the rear shell steady; exactly two hands, gaze settles on the zipper
    dialogue: "And the zipper -"
    audio: same voice and room tone; slight trailing-off delivery

  s04_pov_zipper_operation:
    purpose: one mechanically legible left-to-right UNZIP; closure releases but the panel does NOT open
    visual: POV close look down at the slider, teeth, seam, and his two hands (right on the pull, left holding the bag)
    camera: head-locked POV close on the hands; no orbit, no rack focus, no cutaway during slider travel
    state: shut_to_released
    phase_a_unzip: the RIGHT hand keeps its grip on the orange pull and drags the slider once, left to right; teeth separate ONLY behind the slider; the opening seam grows along the slider path; the LEFT hand stays put holding the rear shell; the front panel does not move; only two hands are ever visible
    phase_b_reach_stop: the slider reaches the right open-stop; closure is fully released; the panel remains aligned and the cavity stays hidden; the right hand is still on the pull
    dialogue: "yeah, it's so smooth."
    audio: same voice, soft real zipper sound, shop ambience

  s05_pov_manual_opening:
    purpose: the missing causal step - a contact-preserving hand move OPENS the released panel, using the same two hands
    visual: POV wide enough to show both his hands, the front panel, bottom hinge, gussets, gray cavity
    camera: head-locked three-quarter downward POV; slight swimmy edge motion; no camera move competing with the hands
    state: released_to_open_empty
    phase_a_transfer: the RIGHT hand does NOT fly off into empty air - it stays in contact with the bag and slides from the orange pull up onto the front lip, closing into a grasp; the LEFT hand slides a short way from the rear shell to grip the top handle, still holding the bag steady; both hands stay on the bag, still only two hands, no third hand appears during the handoff
    phase_b_rotate: the RIGHT hand pulls the front panel down and outward around the bottom hinge; the gussets expand; the gray cavity appears progressively; the LEFT hand keeps the rear shell stable
    phase_c_hold: hold the fully open state with the same two hands; the front panel stays folded down; the cavity and internal pockets remain visible
    dialogue: "it fits your phone, wallet, and basically"
    audio: same voice and room tone; no exaggerated fabric sound

  s06_pov_capacity_loaded:
    purpose: show useful capacity without a hard insertion animation
    visual: exact same open downward POV angle, crop, both hands, contact points, gray lining, pockets, silhouette as the end of s05; a black phone already in the upper pocket and one slim light item already below
    camera: hard match cut, no framing, scale, exposure, head-angle, or hand-position change
    spatial: only the contents change across the cut; every bag part and both hands stay fixed; still exactly two hands
    action: hold the loaded open state; a tiny satisfied downward "see?" head nudge; do not insert, remove, regrip, add a hand, or reshape anything
    dialogue: "all your essentials."
    audio: same uninterrupted voice and shop ambience

  s07_pov_wear_mirror_endorse:
    purpose: sling it on hands-free and close on a genuine endorsement seen in the shop mirror
    visual: POV as his two hands lift the bag and guide the strap up over his own head (strap briefly grazes the top of frame), then the frame tilts down to the bag settling at his chest; he turns and steps to the shop mirror, and for the first time we see HIM in the reflection wearing the bag crossbody over the white T-shirt (black smart glasses visible on his face - expected, unmentioned)
    camera: head-locked POV throughout; strap briefly occludes the top of frame; walking gives natural head-bob and motion blur; the mirror reflection is framed by the bowed wide lens
    spatial: strap stays continuous over shoulder and chest; bag stays attached at the torso; in the mirror the crossbody strap and bag read clearly; in the reflection he has two hands and two arms, correct anatomy
    action: the two hands guide the strap over his head; he looks down and adjusts the bag at his chest; turns and steps to the mirror; looks up at his reflection; small check-himself turn; easy thumbs-up with one hand; finish on a relaxed genuine smile (cheeks and mouth) as his shoulders settle
    dialogue: "And even on long days, it honestly stays super comfy."
    audio: same voice and shop ambience; finish clean, no music

render_rules:
  transitions: execute only the six declared hard cuts; preserve object state across cut_04 and exact open geometry AND both hand positions across cut_05
  camera: smart-glasses POV grammar only - head-locked motion, ultra-wide with mild fisheye, hands from the bottom of frame; NO handheld selfie sway, NO third-person/selfie shot, NO dolly/crane/drone/gimbal/orbit/cinematic macro/bokeh/color grade
  pov_integrity: the wearer is never seen except in the s07 mirror reflection; no shoulder-cam arm, no floating third-person view
  object_causality: slider direction determines whether passed teeth separate or interlock; unzipping RELEASES the closure but does not open the panel; the panel moves ONLY after the right hand grips the front lip; cavity visibility is an effect of panel rotation plus gusset expansion
  hand_integrity: EXACTLY two hands (one left, one right) exist for the whole video; only one hand moves the bag at a time while the other holds; hands keep five distinct fingers, stable identity, consistent scale, and physically continuous, contact-preserving paths from the bottom of frame; a hand that leaves frame returns as the same hand; never a third hand, extra arm, fused finger, or duplicated hand
  audio: one casual voice as the wearer, one acoustic environment, natural room tone, small breaths, no music, no designed effects
  performance_lock: keep the delivery unrehearsed and low-key; do NOT clean it up into a spokesperson read
  long_video_lock: generate one complete 20-second POV video with seven internal shots; never return separate clips

forbid:
  - a third hand, an extra arm, or more than two hands in any frame
  - a second hand appearing while both of the two hands are already accounted for
  - a hand duplicating, splitting, or spawning during the pull-to-lip handoff
  - a hand floating empty in mid-air, teleporting, or jumping to the front lip without a continuous contact-preserving path
  - both hands leaving the bag at the same moment during the open
  - fused fingers, extra fingers, missing fingers, or a hand changing size or skin tone between cuts
  - the left and right hand swapping identity or the working/holding roles flipping mid-action
  - teeth changing ahead of the slider
  - panel opening before closure release
  - panel moving without the right hand gripping the front lip
  - zipper pull moving without the right hand attached
  - cavity appearing before panel separation
  - the whole seam popping open at once instead of growing behind the slider
  - bag morphing or rubber deformation, changing hinge, or disappearing gussets
  - visible item insertion or content changing before cut_05
  - any third-person, selfie, or over-the-shoulder shot of the wearer outside the s07 mirror reflection
  - a handheld phone visible in frame or a selfie-arm holding a device
  - handheld sway or gimbal glide instead of head-locked motion; camera orbiting the bag
  - hands or arms entering from the top or sides instead of the bottom of frame
  - smooth ai skin, waxy skin, poreless, airbrushed, uniform skin tone, plastic skin, beauty smoothing, model-like symmetry, glamour lighting (applies to the mirror reflection)
  - cinematic look, color grade, shallow depth of field, bokeh, 24fps film cadence, studio lighting, polished commercial acting, scripted ad-read delivery
  - frozen static frame, robotic stillness
  - new scenes, reordered beats, extra actions, product drift, wardrobe drift, background music, or a different ending
]]></control>

  <precision id="timeline_and_state_json" lang="json"><![CDATA[
{
  "timebase": {"unit": "seconds", "duration": 20.0, "fps": 30, "frame_count": 600, "aspect_ratio": "9:16", "camera": "head_mounted_pov"},
  "retiming": {"source_duration": 14.558912, "target_duration": 20.0, "method": "proportional_source_clock_expansion", "boundary_rounding_seconds": 0.1},
  "hand_model": {
    "count": 2,
    "left_hand": "steady - holds the bag (rear shell then top handle), never moves the bag",
    "right_hand": "working - pulls the zipper, then contact-slides to the front lip and opens the panel",
    "invariant": "one hand holds while one hand works at every instant; a third hand never appears",
    "identity": "bare hands, no watch, no rings, consistent tone/knuckles/size across all cuts"
  },
  "shots": [
    {"id": "s01_pov_hook", "seconds": [0.0, 2.4], "frames": [0, 72]},
    {"id": "s02_pov_design", "seconds": [2.4, 6.7], "frames": [72, 201]},
    {"id": "s03_pov_zipper_setup", "seconds": [6.7, 7.8], "frames": [201, 234]},
    {"id": "s04_pov_zipper_operation", "seconds": [7.8, 10.2], "frames": [234, 306]},
    {"id": "s05_pov_manual_opening", "seconds": [10.2, 13.0], "frames": [306, 390]},
    {"id": "s06_pov_capacity_loaded", "seconds": [13.0, 14.1], "frames": [390, 423]},
    {"id": "s07_pov_wear_mirror_endorse", "seconds": [14.1, 20.0], "frames": [423, 600]}
  ],
  "cuts": [
    {"id": "cut_01", "at_seconds": 2.4, "at_frame": 72, "type": "hard"},
    {"id": "cut_02", "at_seconds": 6.7, "at_frame": 201, "type": "hard"},
    {"id": "cut_03", "at_seconds": 7.8, "at_frame": 234, "type": "hard"},
    {"id": "cut_04", "at_seconds": 10.2, "at_frame": 306, "type": "hard", "preserve_state": "closure_released"},
    {"id": "cut_05", "at_seconds": 13.0, "at_frame": 390, "type": "hard_match", "changed_field": "content_state_only", "preserve_hands": true},
    {"id": "cut_06", "at_seconds": 14.1, "at_frame": 423, "type": "hard"}
  ],
  "speech": [
    {"shot": "s01_pov_hook", "start": 0.240, "end": 2.186, "words": 6, "wpm": 185, "text": "Okay, you gotta see this bag."},
    {"shot": "s02_pov_design", "start": 2.550, "end": 5.793, "words": 10, "wpm": 185, "text": "Honestly it holds way more than you'd think, looks clean too."},
    {"shot": "s03_pov_zipper_setup", "start": 6.800, "end": 7.773, "words": 3, "wpm": 185, "text": "And the zipper -"},
    {"shot": "s04_pov_zipper_operation", "start": 8.000, "end": 9.297, "words": 4, "wpm": 185, "text": "yeah, it's so smooth."},
    {"shot": "s05_pov_manual_opening", "start": 10.300, "end": 12.570, "words": 7, "wpm": 185, "text": "it fits your phone, wallet, and basically"},
    {"shot": "s06_pov_capacity_loaded", "start": 13.050, "end": 14.023, "words": 3, "wpm": 185, "text": "all your essentials."},
    {"shot": "s07_pov_wear_mirror_endorse", "start": 14.300, "end": 17.543, "words": 10, "wpm": 185, "text": "And even on long days, it honestly stays super comfy."}
  ],
  "object_events": [
    {"id": "zipper_contact", "seconds": [7.8, 8.0], "frames": [234, 240], "pre": "closure_shut", "post": "right_hand_grasp_on_pull_left_hand_on_rear_shell"},
    {"id": "unzip", "seconds": [8.0, 9.7], "frames": [240, 291], "direction": "screen_left_to_right", "moving_hand": "right", "holding_hand": "left", "pre": {"teeth": "fully_interlocked", "panel": "aligned_and_secured", "cavity": "hidden"}, "post": {"teeth": "fully_separated", "closure": "released", "panel": "still_aligned", "cavity": "still_hidden"}, "panel_motion": "none"},
    {"id": "reach_open_stop_hold", "seconds": [9.7, 10.2], "frames": [291, 306], "state": "closure_released_panel_aligned_right_hand_on_pull"},
    {"id": "contact_transfer", "seconds": [10.2, 10.65], "frames": [306, 319], "type": "contact_preserving", "right_hand": "slides from pull to front lip, never leaves the bag", "left_hand": "slides from rear shell to top handle, keeps holding", "hands_total": 2, "empty_hand_in_air": false},
    {"id": "panel_open", "seconds": [10.65, 12.25], "frames": [319, 367], "pivot": "bottom_hinge", "moving_hand": "right", "holding_hand": "left", "pre": "closure_released_panel_aligned", "post": "open_empty", "effects": ["gussets_expand", "cavity_progressively_revealed"]},
    {"id": "open_hold", "seconds": [12.25, 13.0], "frames": [367, 390], "state": "open_empty_panel_folded_down_cavity_visible_two_hands_holding"},
    {"id": "content_match_cut", "at_seconds": 13.0, "at_frame": 390, "pre": "open_empty", "post": "open_loaded", "preserve": ["bag_geometry", "panel_angle", "left_hand_position", "right_hand_position", "camera", "head_angle", "lighting"]}
  ],
  "wear_events": [
    {"seconds": [14.1, 15.1], "action": "two_hands_lift_bag_and_guide_strap_up_over_own_head_strap_grazes_top_of_frame"},
    {"seconds": [15.1, 16.0], "action": "look_down_settle_and_adjust_bag_at_chest"},
    {"seconds": [16.0, 17.0], "action": "turn_and_step_toward_shop_mirror_natural_head_bob"},
    {"seconds": [17.0, 18.2], "action": "look_up_into_mirror_first_reflection_of_wearer_in_bag_crossbody_correct_two_arm_anatomy"},
    {"seconds": [18.2, 18.8], "action": "small_check_himself_turn_in_mirror"},
    {"seconds": [18.8, 19.2], "action": "one_hand_thumbs_up_at_mirror_reflection"},
    {"seconds": [19.2, 20.0], "action": "hold_relaxed_genuine_smile_in_reflection"}
  ],
  "verification": {
    "shot_order_exact": ["s01_pov_hook", "s02_pov_design", "s03_pov_zipper_setup", "s04_pov_zipper_operation", "s05_pov_manual_opening", "s06_pov_capacity_loaded", "s07_pov_wear_mirror_endorse"],
    "exactly_two_hands_all_frames": true,
    "only_one_hand_moves_bag_at_a_time": true,
    "contact_preserving_transfer_no_empty_hand": true,
    "no_third_hand_during_handoff": true,
    "hand_identity_stable_across_cuts": true,
    "camera_is_head_locked_pov": true,
    "wearer_face_only_in_mirror": true,
    "hands_enter_from_bottom_of_frame": true,
    "no_third_person_or_selfie_shot": true,
    "slider_direction_determines_teeth_state": true,
    "teeth_state_changes_only_behind_slider": true,
    "unzip_releases_closure_only": true,
    "panel_opens_only_after_right_hand_grips_lip": true,
    "cavity_visibility_follows_panel_rotation": true,
    "cut_05_changes_contents_only": true,
    "identity_drift_allowed": false,
    "product_drift_allowed": false,
    "separate_clip_output_allowed": false
  }
}
]]></control>

  <execution>
    Generate one complete 20-second vertical video from text only, filmed entirely as first-person point-of-view footage from the wearer's camera glasses. Read YAML as the primary directing layer, execute the XML shot and hard-cut order, and use JSON as the exact clock and state authority. There are EXACTLY TWO hands in the whole video - the wearer's left and right hands - and a third hand never appears: the LEFT hand is the steady hand that always holds the bag, the RIGHT hand is the only hand that acts on it. When the demonstration moves from zipping to opening, the same right hand stays in contact with the bag and slides from the zipper pull up to the front lip - it never flies off into empty air, because an empty reaching hand is what makes the model hallucinate an extra hand. The camera IS the wearer's eyes: it moves only with his head, both hands enter from the bottom of frame, the image is ultra-wide with mild fisheye, and his face is never seen until his reflection appears in the shop mirror. Enforce the causal law as two separate systems: the slider moving left-to-right separates ONLY the teeth it has already passed and RELEASES the closure without opening the bag; then the right hand's grip on the front lip rotates the released panel down around its bottom hinge so the gussets expand and the cavity is progressively revealed. The reverse operations (close_panel, zip) are defined for state consistency but are NOT performed. Keep hand identity, product, shop, voice, and object topology stable across all cuts, and keep the delivery casual and unrehearsed.
  </execution>
</cpcs>
```

## Verification

`test_specimen_verbatim_fidelity`,
`test_specimen_references_analysis_card`,
`test_specimen_matches_source_lineage_duration_retiming`.
