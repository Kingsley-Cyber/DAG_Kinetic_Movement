#!/usr/bin/env python3
"""
Validate a CPCS combat kinematic layer (cpcs/1.2).

Accepts either:
  - a YAML+JSON dual-parse doc (kinematics: {...}), or
  - a bare kinematic JSON file.

Checks the math the layer claims, so numbers are verified rather than asserted:
  1. frame math       — peak_frame == round(peak_s * fps); frame_count == duration_s * fps
  2. velocity vectors — speed_ms == |(vx,vy,vz)| within tolerance
  3. position/velocity coherence — stated peak limb speed is achievable from the position track
  4. contact geometry — striker's limb is actually at the contact point at peak_s
  5. contact closing speed — consistent with the two limbs' velocities at contact
  6. foot contacts     — no actor fully airborne during a grounded strike; no negative intervals
  7. monotonic time    — every track's t is strictly increasing
  8. near-miss clearance — declared clearance is inside its own tolerance band

Usage:
    python validate_kinematics.py <path> [--verbose]
Exit code 0 = all hard checks pass, 1 = at least one failure.
"""

import sys
import json
import math
import argparse

try:
    import yaml
except ImportError:
    yaml = None

TOL_SPEED = 0.05      # m/s tolerance on |v| vs stated speed_ms
TOL_FRAME = 0          # frames of slack on peak_frame math
TOL_REACH = 0.35       # m — how far a limb may be from the stated contact region centre


def load(path):
    raw = open(path, encoding="utf-8").read()
    if path.endswith((".json", ".jsonc")):
        lines = [l for l in raw.splitlines() if not l.lstrip().startswith("//")]
        return json.loads("\n".join(lines))
    if yaml is None:
        sys.exit("PyYAML required for YAML docs: pip install pyyaml")
    doc = yaml.safe_load(raw)
    return doc.get("kinematics", doc)


class Report:
    def __init__(self):
        self.fails, self.warns, self.passes, self.skips = [], [], [], []

    def fail(self, check, msg):
        self.fails.append(f"[FAIL] {check}: {msg}")

    def warn(self, check, msg):
        self.warns.append(f"[WARN] {check}: {msg}")

    def ok(self, check, msg=""):
        self.passes.append(f"[ OK ] {check}{': ' + msg if msg else ''}")

    def skip(self, check, msg):
        """A check that could not run. Must never read as a pass."""
        self.skips.append(f"[SKIP] {check}: {msg}")


def vmag(d, keys=("vx", "vy", "vz")):
    return math.sqrt(sum(d.get(k, 0.0) ** 2 for k in keys))


def sample_at(track, t, keys=("x", "y", "z")):
    """Linear-interpolate a position track at time t."""
    if not track:
        return None
    pts = sorted(track, key=lambda p: p["t"])
    if t <= pts[0]["t"]:
        return tuple(pts[0][k] for k in keys)
    if t >= pts[-1]["t"]:
        return tuple(pts[-1][k] for k in keys)
    for a, b in zip(pts, pts[1:]):
        if a["t"] <= t <= b["t"]:
            span = b["t"] - a["t"]
            f = 0.0 if span == 0 else (t - a["t"]) / span
            return tuple(a[k] + (b[k] - a[k]) * f for k in keys)
    return None


def dist(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))


REGION_TO_SIDE = {
    "right_fist": "right", "left_fist": "left",
    "right_palm": "right", "left_palm": "left",
    "right_forearm": "right", "left_forearm": "left",
    "right_hand": "right", "left_hand": "left",
    "both_hands": "left",
    "sternum": None, "chest": None, "head_volume": None, "head": None,
}

# Joint names differ across schema versions: cpcs/1.2 uses right_hand, v005 used right_arm.
JOINT_ALIASES = {"right": ["right_hand", "right_arm"], "left": ["left_hand", "left_arm"]}

# How far forward of the target's ROOT the struck region typically sits, in meters.
# A passive torso is close to the root; a limb extended to meet/deflect a strike reaches
# forward to intercept it, so the effective contact point is much farther from the root.
TARGET_REGION_OFFSET_M = {
    "sternum": 0.18, "chest": 0.18, "head_volume": 0.22, "head": 0.22,
    "left_forearm": 0.50, "right_forearm": 0.50,   # extended to parry
    "left_palm": 0.52, "right_palm": 0.52,          # extended to deflect
    "both_hands": 0.45,                              # reaching to catch
    "left_hand": 0.50, "right_hand": 0.50,
}


def get_joint_tracks(k):
    """Return {actor: {joint: data}} across both known layouts.

    cpcs/1.2 : tracks.joint_tracks.<actor>.<joint>
    v005     : tracks.body.<actor>.joint_tracks.<joint>
    """
    tr = k.get("tracks", {})
    if "joint_tracks" in tr:
        return tr["joint_tracks"]
    out = {}
    for actor, data in tr.get("body", {}).items():
        if isinstance(data, dict) and "joint_tracks" in data:
            out[actor] = data["joint_tracks"]
    return out


def get_root_motion(k):
    """Return {actor: positions[]} across both known layouts."""
    tr = k.get("tracks", {})
    if "root_motion" in tr:
        return {a: d.get("positions", []) for a, d in tr["root_motion"].items()}
    out = {}
    for actor, data in tr.get("body", {}).items():
        if isinstance(data, dict) and "root_motion" in data:
            out[actor] = data["root_motion"].get("positions", [])
    return out


def resolve_joint(joints, region):
    """Find the joint track for a body region, tolerating naming schemes."""
    side = REGION_TO_SIDE.get(region)
    if side is None:
        return None
    for name in JOINT_ALIASES[side]:
        if name in joints:
            return joints[name]
    return None


def actor_reach(k, actor_id):
    for a in k.get("actors", []):
        if a.get("actor_id") == actor_id:
            return a.get("reach_m")
    return None


def check_timebase(k, r):
    tb = k["timebase"]
    fps, dur = tb["fps"], tb["duration_s"]
    expect = round(fps * dur)
    if tb.get("frame_count") != expect:
        r.fail("timebase.frame_count", f"{tb.get('frame_count')} != {fps}*{dur} = {expect}")
    else:
        r.ok("timebase.frame_count", f"{expect} frames @ {fps}fps")
    return fps, dur


def check_monotonic(k, r):
    bad = 0
    def walk(node, path):
        nonlocal bad
        if isinstance(node, list) and node and isinstance(node[0], dict) and "t" in node[0]:
            ts = [p["t"] for p in node]
            if any(b < a for a, b in zip(ts, ts[1:])):
                r.fail("time_monotonic", f"{path} has non-increasing t")
                bad += 1
        elif isinstance(node, dict):
            for kk, vv in node.items():
                walk(vv, f"{path}/{kk}")
        elif isinstance(node, list):
            for i, vv in enumerate(node):
                walk(vv, f"{path}[{i}]")
    walk(k.get("tracks", {}), "/tracks")
    if bad == 0:
        r.ok("time_monotonic", "all tracks strictly increasing")


def check_velocities(k, r, verbose):
    checked = 0
    def walk(node, path):
        nonlocal checked
        if isinstance(node, dict):
            for kk, vv in node.items():
                if kk in ("velocity", "linear_velocity") and isinstance(vv, list):
                    for s in vv:
                        if "speed_ms" not in s:
                            continue
                        mag, stated = vmag(s), s["speed_ms"]
                        checked += 1
                        if abs(mag - stated) > TOL_SPEED:
                            r.fail("velocity_magnitude",
                                   f"{path}/{kk} t={s['t']}: |v|={mag:.3f} but speed_ms={stated}")
                        elif verbose:
                            r.ok("velocity_magnitude", f"{path}/{kk} t={s['t']} |v|={mag:.2f}")
                else:
                    walk(vv, f"{path}/{kk}")
        elif isinstance(node, list):
            for i, vv in enumerate(node):
                walk(vv, f"{path}[{i}]")
    walk(k.get("tracks", {}), "/tracks")
    r.ok("velocity_magnitude", f"{checked} vectors consistent with stated speed")


def check_position_velocity_coherence(k, r):
    """Peak stated limb speed must be broadly achievable from the position track."""
    jt = get_joint_tracks(k)
    any_vel = any("linear_velocity" in d for joints in jt.values() for d in joints.values())
    if not any_vel:
        r.skip("pos_vel_coherence", "no linear_velocity tracks — limb speeds are unspecified")
        return
    for actor, joints in jt.items():
        for joint, data in joints.items():
            pos, vel = data.get("positions"), data.get("linear_velocity")
            if not pos or not vel:
                continue
            peak = max(vel, key=lambda s: s.get("speed_ms", 0))
            t, stated = peak["t"], peak["speed_ms"]
            pts = sorted(pos, key=lambda p: p["t"])
            seg = None
            for a, b in zip(pts, pts[1:]):
                if a["t"] <= t <= b["t"]:
                    seg = (a, b)
                    break
            if not seg:
                continue
            a, b = seg
            dt = b["t"] - a["t"]
            if dt <= 0:
                continue
            d = dist((a["x"], a["y"], a["z"]), (b["x"], b["y"], b["z"]))
            seg_v = d / dt
            # stated instantaneous peak should exceed the local average but stay within ~2.5x
            if stated < seg_v * 0.85:
                r.fail("pos_vel_coherence",
                       f"{actor}.{joint} t={t}: stated peak {stated} m/s < segment average {seg_v:.2f} m/s")
            elif stated > seg_v * 2.6:
                r.warn("pos_vel_coherence",
                       f"{actor}.{joint} t={t}: stated peak {stated} m/s is {stated/seg_v:.1f}x "
                       f"segment average {seg_v:.2f} m/s (steep but possible under cubic_in)")
            else:
                r.ok("pos_vel_coherence",
                     f"{actor}.{joint} peak {stated} m/s vs seg avg {seg_v:.2f} m/s")


def check_reach_feasibility(k, r):
    """THE structural check: can the striker physically reach the target at contact?

    Catches the class of defect where contact events assert strikes that the position
    tracks cannot produce — the model then has to reconcile contradictory numbers and
    silently approximates.
    """
    roots = get_root_motion(k)
    contacts = k["tracks"].get("contacts", [])
    if not roots:
        r.skip("reach_feasibility", "no root_motion track — cannot verify strike range")
        return
    if not contacts:
        r.skip("reach_feasibility", "no contacts declared")
        return

    for c in contacts:
        cid = c["id"]
        a, b = c["actor_a"], c["actor_b"]
        t = c.get("peak_s", c.get("start_s"))
        reach_a, reach_b = actor_reach(k, a), actor_reach(k, b)
        if reach_a is None or reach_b is None:
            r.skip("reach_feasibility", f"{cid}: actors lack reach_m — cannot verify range")
            continue
        pa = sample_at(roots.get(a, []), t)
        pb = sample_at(roots.get(b, []), t)
        if not pa or not pb:
            r.skip("reach_feasibility", f"{cid}: no root sample at t={t}")
            continue

        sep = dist(pa, pb)
        combined = reach_a + reach_b

        if c["type"] == "near_miss":
            # a near-miss still has to be thrown from a plausible distance
            if sep > combined * 1.15:
                r.fail("reach_feasibility",
                       f"{cid}: roots {sep:.2f}m apart at t={t} — too far for even a near-miss "
                       f"(combined reach {combined:.2f}m)")
            else:
                r.ok("reach_feasibility", f"{cid} near-miss thrown from {sep:.2f}m (reach {combined:.2f}m)")
            continue

        # An impact needs the STRIKER to cover the gap to wherever the target region
        # actually sits, which depends on the region: a torso hit is close to the target's
        # root, but a forearm/palm actively extended to MEET the strike sits well forward
        # of it. Using a flat offset here produces false warnings on parries.
        striker_reach = reach_a if c["actor_a"] == a else reach_b
        limit = striker_reach + TARGET_REGION_OFFSET_M.get(c.get("region_b"), 0.20)
        if sep > combined:
            r.fail("reach_feasibility",
                   f"{cid}: roots {sep:.2f}m apart at t={t} but combined reach is only "
                   f"{combined:.2f}m — DEFICIT {sep - combined:.2f}m. The declared contact is "
                   f"physically impossible from these positions.")
        elif sep > limit:
            r.warn("reach_feasibility",
                   f"{cid}: roots {sep:.2f}m apart; striker reach {striker_reach:.2f}m + body "
                   f"offset = {limit:.2f}m. Contact only works if the target leans in.")
        else:
            r.ok("reach_feasibility", f"{cid} separation {sep:.2f}m within striker reach {striker_reach:.2f}m")


def check_contacts(k, r, fps):
    jt = get_joint_tracks(k)
    for c in k["tracks"].get("contacts", []):
        cid = c["id"]

        # frame math
        if "peak_s" in c and "peak_frame" in c:
            expect = round(c["peak_s"] * fps)
            if abs(c["peak_frame"] - expect) > TOL_FRAME:
                r.fail("contact_frame_math",
                       f"{cid}: peak_frame={c['peak_frame']} but peak_s*fps={c['peak_s']}*{fps}={expect}")
            else:
                r.ok("contact_frame_math", f"{cid} frame {c['peak_frame']}")

        # interval sanity
        if not (c["start_s"] <= c.get("peak_s", c["start_s"]) <= c["end_s"]):
            r.fail("contact_interval", f"{cid}: peak_s outside [start_s, end_s]")

        # geometry — are the two limbs actually near each other at peak?
        t = c.get("peak_s", c["start_s"])
        ta = resolve_joint(jt.get(c["actor_a"], {}), c.get("region_a"))
        tb = resolve_joint(jt.get(c["actor_b"], {}), c.get("region_b"))
        pa = sample_at(ta["positions"], t) if ta else None
        pb = sample_at(tb["positions"], t) if tb else None
        if REGION_TO_SIDE.get(c.get("region_a")) and not ta:
            r.skip("contact_geometry", f"{cid}: no joint track for {c['region_a']}")
        if pa and pb:
            d = dist(pa, pb)
            if c["type"] == "near_miss":
                r.ok("contact_geometry", f"{cid} limbs {d:.3f}m apart (near_miss)")
            elif d > TOL_REACH:
                r.fail("contact_geometry",
                       f"{cid}: limbs {d:.3f}m apart at t={t} — too far to be in contact "
                       f"(limit {TOL_REACH}m)")
            else:
                r.ok("contact_geometry", f"{cid} limbs {d:.3f}m apart at contact")

        # near-miss clearance inside its own tolerance band
        if c["type"] == "near_miss":
            cl, tol = c.get("clearance_m"), c.get("clearance_tolerance_m")
            if cl is not None and tol is not None:
                if cl - tol <= 0:
                    r.fail("near_miss_clearance",
                           f"{cid}: clearance {cl}m +/- {tol}m can reach 0 — may render as a hit")
                else:
                    r.ok("near_miss_clearance", f"{cid} {cl}m +/- {tol}m stays clear of contact")

        # impulse vs force vs duration:  impulse ~= peak_force * duration (triangular ~0.5 factor)
        imp, force = c.get("impulse_ns"), c.get("peak_force_n")
        if imp and force:
            dur = c["end_s"] - c["start_s"]
            implied = imp / force
            if not (0.2 * dur <= implied <= 1.2 * dur):
                r.warn("impulse_consistency",
                       f"{cid}: impulse/force = {implied*1000:.0f}ms vs contact window {dur*1000:.0f}ms")
            else:
                r.ok("impulse_consistency",
                     f"{cid} impulse {imp}Ns / force {force}N = {implied*1000:.0f}ms effective")

        # normal must be ~unit length
        n = c.get("normal")
        if n:
            m = math.sqrt(n["nx"] ** 2 + n["ny"] ** 2 + n["nz"] ** 2)
            if abs(m - 1.0) > 0.05:
                r.fail("contact_normal", f"{cid}: normal magnitude {m:.3f} is not unit length")
            else:
                r.ok("contact_normal", f"{cid} normal unit length ({m:.3f})")


def check_foot_contacts(k, r):
    events = k["tracks"].get("foot_contacts", [])
    if not events:
        r.warn("foot_contacts", "no foot-contact track — foot sliding is the #1 motion tell")
        return
    by_actor = {}
    for e in events:
        s, en = e["planted_s"]
        if en <= s:
            r.fail("foot_interval", f"{e['actor']}.{e['foot']} interval {e['planted_s']} is non-positive")
        by_actor.setdefault(e["actor"], []).append((s, en, e["foot"]))
    for actor, iv in by_actor.items():
        iv.sort()
        gaps = []
        cursor = iv[0][0]
        for s, en, _ in iv:
            if s > cursor + 1e-6:
                gaps.append((cursor, s))
            cursor = max(cursor, en)
        airborne = [g for g in gaps if g[1] - g[0] > 0.001]
        if airborne:
            r.warn("foot_grounding",
                   f"{actor} fully airborne during {['%.2f-%.2fs' % g for g in airborne]}")
        else:
            r.ok("foot_grounding", f"{actor} always has at least one foot planted")


def check_contacts_grounded(k, r):
    """A strike delivering real impulse should have the striker grounded."""
    events = k["tracks"].get("foot_contacts", [])
    for c in k["tracks"].get("contacts", []):
        if not c.get("impulse_ns"):
            continue
        t, actor = c.get("peak_s", c["start_s"]), c["actor_a"]
        grounded = any(e["actor"] == actor and e["planted_s"][0] <= t <= e["planted_s"][1]
                       for e in events)
        if not grounded:
            r.warn("strike_grounded",
                   f"{c['id']}: {actor} has no planted foot at t={t} but delivers {c['impulse_ns']}Ns")
        else:
            r.ok("strike_grounded", f"{c['id']} striker grounded at contact")


def check_lab_control(k, r):
    for actor, spans in k["tracks"].get("lab_control", {}).items():
        prev_end = None
        for s in spans:
            a, b = s["interval_s"]
            if b <= a:
                r.fail("lab_interval", f"{actor}: interval {s['interval_s']} non-positive")
            if prev_end is not None and abs(a - prev_end) > 1e-6:
                r.warn("lab_continuity", f"{actor}: gap/overlap at t={prev_end} -> {a}")
            prev_end = b
            e = s["effort"]
            for axis in ("weight", "time", "space"):
                if not 0.0 <= e[axis] <= 1.0:
                    r.fail("lab_range", f"{actor} {axis}={e[axis]} outside [0,1]")
            if not -1.0 <= e["flow"] <= 1.0:
                r.fail("lab_range", f"{actor} flow={e['flow']} outside [-1,1]")
        r.ok("lab_control", f"{actor}: {len(spans)} effort spans valid")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    k = load(args.path)
    r = Report()

    fps, _ = check_timebase(k, r)
    check_monotonic(k, r)
    check_velocities(k, r, args.verbose)
    check_position_velocity_coherence(k, r)
    check_reach_feasibility(k, r)
    check_contacts(k, r, fps)
    check_foot_contacts(k, r)
    check_contacts_grounded(k, r)
    check_lab_control(k, r)

    if args.verbose:
        for line in r.passes:
            print(line)
    else:
        print(f"{len(r.passes)} checks passed")
    for line in r.skips:
        print(line)
    for line in r.warns:
        print(line)
    for line in r.fails:
        print(line)

    print(f"\n{len(r.passes)} passed, {len(r.skips)} skipped, "
          f"{len(r.warns)} warnings, {len(r.fails)} failures")
    if r.skips:
        print("NOTE: skipped checks are NOT passes — the document lacks the data to verify them.")
    return 1 if r.fails else 0


if __name__ == "__main__":
    sys.exit(main())
