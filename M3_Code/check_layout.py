"""
check_layout.py - Automated layout & overlap checker for all Manim scenes.

Hooks `helpers.wait_until` so that at every beat boundary it checks:
1. Every non-title mobject's bounding box stays inside the Content Zone:
   x in [-6.5, 6.5], y in [-3.5, 2.6].
   (Title mobjects marked `is_title=True` are checked against x in [-6.5, 6.5], y in [3.0, 3.9].)
2. No two visible Text / MathTex / Tex mobjects have overlapping bounding boxes.

Usage:
    python3 check_layout.py
"""

import importlib
import sys
from manim import *

import helpers
from helpers import (
    CONTENT_X_MIN,
    CONTENT_X_MAX,
    CONTENT_Y_MIN,
    CONTENT_Y_MAX,
    TITLE_Y_MAX,
    UNDERLINE_Y,
)

TOL = 0.02  # Small floating-point tolerance


def is_text_or_math(mob):
    return isinstance(mob, (Text, MathTex, Tex))


def collect_leaf_text_mobs(mobjects):
    """Collect visible leaf Text/MathTex/Tex mobjects (ignoring NumberPlane axis ticks)."""
    leaves = []

    def walk(m, in_plane=False):
        if isinstance(m, NumberPlane):
            in_plane = True
        if in_plane:
            return
        if isinstance(m, BackgroundRectangle):
            return
        if is_text_or_math(m):
            if m.width > 1e-4 and m.height > 1e-4:
                leaves.append(m)
            return
        for sub in getattr(m, "submobjects", []):
            walk(sub, in_plane=in_plane)

    for m in mobjects:
        walk(m, in_plane=False)
    return leaves


def mob_label(mob):
    if hasattr(mob, "text") and mob.text:
        return f"Text({mob.text[:35]!r})"
    if hasattr(mob, "tex_string") and mob.tex_string:
        return f"MathTex({mob.tex_string[:35]!r})"
    return mob.__class__.__name__


def boxes_overlap(a, b, pad=0.0):
    ax0, ax1 = a.get_left()[0], a.get_right()[0]
    ay0, ay1 = a.get_bottom()[1], a.get_top()[1]
    bx0, bx1 = b.get_left()[0], b.get_right()[0]
    by0, by1 = b.get_bottom()[1], b.get_top()[1]
    return (ax0 < bx1 - pad) and (ax1 > bx0 + pad) and (ay0 < by1 - pad) and (ay1 > by0 + pad)


def check_scene_state(scene_name, beat_idx, t, mobjects):
    issues = []

    FRAME_MARGIN = 0.5
    FRAME_X_MIN = -config.frame_width / 2.0 + FRAME_MARGIN
    FRAME_X_MAX = config.frame_width / 2.0 - FRAME_MARGIN
    FRAME_Y_MIN = -config.frame_height / 2.0 + FRAME_MARGIN
    FRAME_Y_MAX = config.frame_height / 2.0 - FRAME_MARGIN

    for mob in mobjects:
        if mob.width < 1e-4 and mob.height < 1e-4:
            continue
        x0, x1 = mob.get_left()[0], mob.get_right()[0]
        y0, y1 = mob.get_bottom()[1], mob.get_top()[1]

        if getattr(mob, "is_title", False):
            if x0 < CONTENT_X_MIN - TOL or x1 > CONTENT_X_MAX + TOL or y0 < UNDERLINE_Y - TOL or y1 > TITLE_Y_MAX + TOL:
                issues.append(
                    f"[{scene_name} | beat {beat_idx} @ {t:.2f}s] TITLE OUT OF BOUNDS: {mob_label(mob)} "
                    f"x=[{x0:.2f},{x1:.2f}] y=[{y0:.2f},{y1:.2f}]"
                )
        else:
            if x0 < CONTENT_X_MIN - TOL or x1 > CONTENT_X_MAX + TOL or y0 < CONTENT_Y_MIN - TOL or y1 > CONTENT_Y_MAX + TOL:
                issues.append(
                    f"[{scene_name} | beat {beat_idx} @ {t:.2f}s] OUT OF CONTENT ZONE: {mob_label(mob)} "
                    f"x=[{x0:.2f},{x1:.2f}] y=[{y0:.2f},{y1:.2f}] "
                    f"(allowed x=[{CONTENT_X_MIN},{CONTENT_X_MAX}] y=[{CONTENT_Y_MIN},{CONTENT_Y_MAX}])"
                )
            # Frame margin check: nothing may come within 0.5 units of any frame edge except title
            if x0 < FRAME_X_MIN - TOL or x1 > FRAME_X_MAX + TOL or y0 < FRAME_Y_MIN - TOL or y1 > FRAME_Y_MAX + TOL:
                issues.append(
                    f"[{scene_name} | beat {beat_idx} @ {t:.2f}s] FRAME MARGIN VIOLATION: {mob_label(mob)} "
                    f"x=[{x0:.2f},{x1:.2f}] y=[{y0:.2f},{y1:.2f}] (within 0.5 of frame edge)"
                )

    text_mobs = collect_leaf_text_mobs(mobjects)
    for i in range(len(text_mobs)):
        for j in range(i + 1, len(text_mobs)):
            a, b = text_mobs[i], text_mobs[j]
            if boxes_overlap(a, b, pad=0.02):
                issues.append(
                    f"[{scene_name} | beat {beat_idx} @ {t:.2f}s] TEXT/MATH OVERLAP: "
                    f"{mob_label(a)} vs {mob_label(b)}"
                )

    # Text-in-box check: for every box, text must be inside with at least 0.3 padding
    boxes = []
    def find_boxes(m):
        if isinstance(m, BackgroundRectangle):
            return
        if getattr(m, "is_box", False) or isinstance(m, (SurroundingRectangle, RoundedRectangle)):
            boxes.append(m)
        for sub in getattr(m, "submobjects", []):
            find_boxes(sub)
    for m in mobjects:
        find_boxes(m)

    for box in boxes:
        bl, br = box.get_left()[0], box.get_right()[0]
        bb, bt = box.get_bottom()[1], box.get_top()[1]
        if hasattr(box, "content") and box.content is not None:
            c = box.content
            cl, cr = c.get_left()[0], c.get_right()[0]
            cb, ct = c.get_bottom()[1], c.get_top()[1]
            pad_l, pad_r, pad_b, pad_t = cl - bl, br - cr, cb - bb, bt - ct
            min_pad = min(pad_l, pad_r, pad_b, pad_t)
            if min_pad < 0.3 - TOL:
                issues.append(
                    f"[{scene_name} | beat {beat_idx} @ {t:.2f}s] TEXT-IN-BOX VIOLATION: {mob_label(c)} "
                    f"padding={min_pad:.3f} < 0.300 (L={pad_l:.2f}, R={pad_r:.2f}, B={pad_b:.2f}, T={pad_t:.2f})"
                )
        else:
            enclosed_texts = [
                tm for tm in text_mobs
                if tm.get_left()[0] >= bl - TOL and tm.get_right()[0] <= br + TOL
                and tm.get_bottom()[1] >= bb - TOL and tm.get_top()[1] <= bt + TOL
            ]
            if enclosed_texts:
                cl = min(tm.get_left()[0] for tm in enclosed_texts)
                cr = max(tm.get_right()[0] for tm in enclosed_texts)
                cb = min(tm.get_bottom()[1] for tm in enclosed_texts)
                ct = max(tm.get_top()[1] for tm in enclosed_texts)
                pad_l, pad_r, pad_b, pad_t = cl - bl, br - cr, cb - bb, bt - ct
                min_pad = min(pad_l, pad_r, pad_b, pad_t)
                if min_pad < 0.3 - TOL:
                    issues.append(
                        f"[{scene_name} | beat {beat_idx} @ {t:.2f}s] TEXT-IN-BOX VIOLATION: box at "
                        f"x=[{bl:.2f},{br:.2f}] y=[{bb:.2f},{bt:.2f}] padding={min_pad:.3f} < 0.300"
                    )
    return issues


def run_check_on_scene(module_name, class_name):
    all_issues = []
    beat_counter = [0]

    def hooked_wait_until(scene, t):
        beat_counter[0] += 1
        all_issues.extend(check_scene_state(class_name, beat_counter[0], t, scene.mobjects))

    helpers.wait_until = hooked_wait_until

    mod = importlib.import_module(module_name)
    importlib.reload(mod)
    scene_cls = getattr(mod, class_name)

    config.dry_run = True
    config.write_to_movie = False
    scene = scene_cls()
    scene.render()
    return all_issues


SCENES = [
    ("scene0_title", "Scene0Title"),
    ("scene1_hook", "Scene1Hook"),
    ("scene2_concept", "Scene2Concept"),
    ("scene3_intuition", "Scene3Intuition"),
    ("scene4_example", "Scene4Example"),
    ("scene5_interpretation", "Scene5Interpretation"),
    ("scene6_summary", "Scene6Summary"),
]

if __name__ == "__main__":
    total_issues = []
    for mod_name, cls_name in SCENES:
        print(f"Checking {cls_name}...")
        issues = run_check_on_scene(mod_name, cls_name)
        for iss in issues:
            print("  FAIL:", iss)
        total_issues.extend(issues)

    print(f"\nTotal layout issues: {len(total_issues)}")
    sys.exit(1 if total_issues else 0)
