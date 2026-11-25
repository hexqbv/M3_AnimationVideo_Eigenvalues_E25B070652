"""
scene3_intuition.py - Scene 3: Visual Intuition (synced to audio/scene3.wav)

Audio: audio/scene3.wav (67.434688s) + 0.5s offset = 67.935s total.
Colors: Teal for (1,1) / y=x, Purple for (1,-1) / y=-x, Orange for test vector w=(2,0).
"""

from manim import *
import numpy as np

from helpers import (
    COLOR_BG,
    COLOR_ORANGE,
    COLOR_TEAL,
    COLOR_PURPLE,
    COLOR_MATRIX_A,
    COLOR_TEXT,
    CONTENT_CENTER,
    create_title_bar,
    create_labeled_plane,
    create_matrix_display,
    clip_segment_to_box,
    build_clipped_warped_grid,
    center_in_content_zone,
    make_box,
    wait_until,
)


def make_badged_label(mob, anchor_point, direction, buff=0.3):
    """Wraps a label in a dark BackgroundRectangle(opacity=0.8) and places it beside an object."""
    mob.next_to(anchor_point, direction, buff=buff)
    bg = BackgroundRectangle(mob, color=COLOR_BG, fill_opacity=0.8, buff=0.08)
    return VGroup(bg, mob)


class Scene3Intuition(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG
        OFFSET = 0.5
        AUDIO_END = 67.434688 + OFFSET

        self.add_sound("audio/scene3.wav", time_offset=OFFSET)

        # ======================================================================
        # TITLE BAR & BEAT 1 (1.23s audio): Plane fills right 65% of content area
        # Content width = 13.0 -> right 65% ~ 8.45 wide (x in [-2.0, 6.45])
        # Left text column stays at x <= -2.6 (at least 0.5 away from plane's left edge)
        # ======================================================================
        title, underline = create_title_bar("Visual Intuition: Geometric Action of A")

        plane = create_labeled_plane(
            x_range=(-4, 5, 1),
            y_range=(-3, 3, 1),
            x_length=7.2,
            y_length=4.2,
            font_size=30,
        )
        plane.move_to(np.array([1.8, CONTENT_CENTER[1], 0.0]))

        matrix_badge = create_matrix_display(
            [[2, 1], [1, 2]], name="A", color=COLOR_MATRIX_A, font_size=32
        )
        badge_bg = BackgroundRectangle(
            matrix_badge, color=COLOR_BG, fill_opacity=0.85, buff=0.15
        )
        matrix_group = VGroup(badge_bg, matrix_badge)
        matrix_group.move_to(np.array([-4.4, 1.55, 0.0]))

        origin = plane.c2p(0, 0)
        unit_square = Polygon(
            origin,
            plane.c2p(1, 0),
            plane.c2p(1, 1),
            plane.c2p(0, 1),
            fill_color=COLOR_ORANGE,
            fill_opacity=0.25,
            stroke_color=COLOR_ORANGE,
            stroke_width=3,
        )

        wait_until(self, 1.23 + OFFSET)
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            Create(underline),
            Create(plane, lag_ratio=0.04),
            FadeIn(matrix_group, shift=RIGHT * 0.25),
            DrawBorderThenFill(unit_square),
            run_time=2.0,
        )

        # ======================================================================
        # BEAT 2 (4.59s audio): Teal vector (1, 1) drawn on line y = x
        # ======================================================================
        p_min, p_max = plane.c2p(-4, -3), plane.c2p(5, 3)
        px0, px1, py0, py1 = p_min[0], p_max[0], p_min[1], p_max[1]

        c_yx = clip_segment_to_box(plane.c2p(-10, -10), plane.c2p(10, 10), px0, px1, py0, py1)
        line_y_eq_x = DashedLine(c_yx[0], c_yx[1], dash_length=0.15, color=COLOR_TEAL, stroke_width=3.5)

        label_y_eq_x = make_badged_label(
            MathTex(r"\text{Line } y = x", font_size=30, color=COLOR_TEAL),
            plane.c2p(-2.0, -2.0),
            LEFT,
            buff=0.3,
        )
        vec_e1 = Arrow(origin, plane.c2p(1.0, 1.0), buff=0, color=COLOR_TEAL, stroke_width=6)
        lbl_e1 = make_badged_label(
            MathTex(r"\mathbf{v}_1 = (1, 1)", font_size=30, color=COLOR_TEAL),
            plane.c2p(1.0, 1.0),
            UP,
            buff=0.3,
        )

        wait_until(self, 4.59 + OFFSET)
        self.play(
            Create(line_y_eq_x),
            FadeIn(label_y_eq_x),
            GrowArrow(vec_e1),
            FadeIn(lbl_e1),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 3 (8.83s audio): ApplyMatrix deforms unit square + clipped warped grid
        # ======================================================================
        transform_matrix = [[2.0, 1.0], [1.0, 2.0]]
        warped_grid = build_clipped_warped_grid(plane, transform_matrix)

        wait_until(self, 8.83 + OFFSET)
        self.play(
            FadeOut(plane),
            FadeIn(warped_grid),
            ApplyMatrix(transform_matrix, unit_square, about_point=origin),
            run_time=2.0,
            rate_func=smooth,
        )

        # ======================================================================
        # BEAT 4 (13.99s audio): Teal vector stretches to (3, 3)
        # ======================================================================
        vec_e1_stretched = Arrow(origin, plane.c2p(3.0, 3.0), buff=0, color=COLOR_TEAL, stroke_width=6)

        wait_until(self, 13.99 + OFFSET)
        self.play(
            Transform(vec_e1, vec_e1_stretched),
            FadeOut(lbl_e1),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 5 (18.53s audio): Label "stretched by 3" (lambda = 3)
        # ======================================================================
        tag_stretch_3 = Text("stretched by 3 (\u03bb = 3)", font_size=32, weight=BOLD, color=COLOR_TEAL)
        tag_bg_3 = BackgroundRectangle(tag_stretch_3, color=COLOR_BG, fill_opacity=0.8, buff=0.12)
        callout_3 = VGroup(tag_bg_3, tag_stretch_3).next_to(matrix_group, DOWN, buff=0.5).align_to(matrix_group, LEFT)

        wait_until(self, 18.53 + OFFSET)
        self.play(
            FadeIn(callout_3),
            Flash(plane.c2p(3.0, 3.0), color=COLOR_TEAL, flash_radius=0.4),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 6 (22.23s audio): Purple vector (1, -1) drawn on line y = -x
        # ======================================================================
        c_ynx = clip_segment_to_box(plane.c2p(-10, 10), plane.c2p(10, -10), px0, px1, py0, py1)
        line_y_eq_neg_x = DashedLine(c_ynx[0], c_ynx[1], dash_length=0.15, color=COLOR_PURPLE, stroke_width=3.5)
        label_y_eq_neg_x = make_badged_label(
            MathTex(r"\text{Line } y = -x", font_size=32, color=COLOR_PURPLE),
            plane.c2p(-2.5, 2.5),
            RIGHT,
            buff=0.35,
        )
        vec_e2 = Arrow(origin, plane.c2p(1.0, -1.0), buff=0, color=COLOR_PURPLE, stroke_width=6)
        lbl_e2 = make_badged_label(
            MathTex(r"\mathbf{v}_2 = (1, -1)", font_size=32, color=COLOR_PURPLE),
            plane.c2p(1.0, -1.0),
            LEFT,
            buff=0.35,
        )

        wait_until(self, 22.23 + OFFSET)
        self.play(
            FadeOut(unit_square),
            Create(line_y_eq_neg_x),
            FadeIn(label_y_eq_neg_x),
            GrowArrow(vec_e2),
            FadeIn(lbl_e2),
            run_time=1.5,
        )

        # ======================================================================
        # BEAT 7 (24.85s audio): Purple vector maps to (1, -1) unchanged
        # ======================================================================
        wait_until(self, 24.85 + OFFSET)
        self.play(
            Indicate(vec_e2, color=COLOR_PURPLE, scale_factor=1.12),
            run_time=1.5,
        )

        # ======================================================================
        # BEAT 8 (29.53s audio): Label "stretched by 1" (lambda = 1)
        # ======================================================================
        tag_stretch_1 = Text("stretched by 1 (\u03bb = 1)", font_size=32, weight=BOLD, color=COLOR_PURPLE)
        tag_bg_1 = BackgroundRectangle(tag_stretch_1, color=COLOR_BG, fill_opacity=0.8, buff=0.12)
        callout_1 = VGroup(tag_bg_1, tag_stretch_1).next_to(callout_3, DOWN, buff=0.4).align_to(callout_3, LEFT)

        wait_until(self, 29.53 + OFFSET)
        self.play(
            FadeOut(lbl_e2),
            FadeIn(callout_1),
            Flash(plane.c2p(1.0, -1.0), color=COLOR_PURPLE, flash_radius=0.35),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 9 (34.75s audio): Orthogonal natural axes
        # ======================================================================
        ortho_banner = Text("Orthogonal Axes", font_size=32, weight=BOLD, color=COLOR_TEXT)
        ortho_bg = BackgroundRectangle(ortho_banner, color=COLOR_BG, fill_opacity=0.85, buff=0.12)
        ortho_group = VGroup(ortho_bg, ortho_banner).next_to(callout_1, DOWN, buff=0.4).align_to(callout_1, LEFT)

        wait_until(self, 34.75 + OFFSET)
        self.play(
            FadeIn(ortho_group, shift=DOWN * 0.1),
            Indicate(line_y_eq_x, color=COLOR_TEAL),
            Indicate(line_y_eq_neg_x, color=COLOR_PURPLE),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 10 (44.99s audio): Reset plane to untransformed NumberPlane + w = (2, 0)
        # ======================================================================
        plane_reset = create_labeled_plane(
            x_range=(-4, 5, 1),
            y_range=(-3, 3, 1),
            x_length=7.2,
            y_length=4.2,
            font_size=30,
        ).move_to(plane.get_center())

        vec_w = Arrow(origin, plane_reset.c2p(2.0, 0.0), buff=0, color=COLOR_ORANGE, stroke_width=6)
        lbl_w = make_badged_label(
            MathTex(r"\mathbf{w} = (2, 0)", font_size=30, color=COLOR_ORANGE),
            plane_reset.c2p(2.0, 0.0),
            DOWN,
            buff=0.35,
        )
        decomp_tex = MathTex(
            r"(2, 0) = 1(1, 1) + 1(1, -1)", font_size=32, color=COLOR_ORANGE
        )
        decomp_bg = BackgroundRectangle(decomp_tex, color=COLOR_BG, fill_opacity=0.85, buff=0.12)
        decomp_card = VGroup(decomp_bg, decomp_tex).next_to(matrix_group, DOWN, buff=0.5).align_to(matrix_group, LEFT)

        wait_until(self, 44.99 + OFFSET)
        self.play(
            ReplacementTransform(warped_grid, plane_reset),
            FadeOut(callout_3),
            FadeOut(callout_1),
            FadeOut(ortho_group),
            FadeOut(vec_e1),
            FadeOut(vec_e2),
            GrowArrow(vec_w),
            FadeIn(lbl_w),
            FadeIn(decomp_card),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 11 (53.99s audio): Scale each eigenvector component
        # ======================================================================
        vec_c1 = Arrow(origin, plane_reset.c2p(3.0, 3.0), buff=0, color=COLOR_TEAL, stroke_width=5)
        vec_c2 = Arrow(origin, plane_reset.c2p(1.0, -1.0), buff=0, color=COLOR_PURPLE, stroke_width=5)

        wait_until(self, 53.99 + OFFSET)
        self.play(
            GrowArrow(vec_c1),
            GrowArrow(vec_c2),
            run_time=1.5,
        )

        # ======================================================================
        # BEAT 12 (57.37s audio): Sum (3, 3) + (1, -1) = (4, 2)
        # Place "Aw = (4, 2)" to the right of the arrowhead, not on it!
        # ======================================================================
        vec_Aw = Arrow(origin, plane_reset.c2p(4.0, 2.0), buff=0, color=COLOR_ORANGE, stroke_width=6)
        lbl_Aw = make_badged_label(
            MathTex(r"A\mathbf{w} = (4, 2)", font_size=30, color=COLOR_ORANGE),
            plane_reset.c2p(4.0, 2.0),
            RIGHT,
            buff=0.25,
        )
        sum_tex = MathTex(
            r"(3, 3) + (1, -1) = (4, 2)\ \checkmark", font_size=32, color=COLOR_ORANGE
        )
        sum_bg = BackgroundRectangle(sum_tex, color=COLOR_BG, fill_opacity=0.85, buff=0.12)
        sum_card = VGroup(sum_bg, sum_tex).next_to(decomp_card, DOWN, buff=0.4).align_to(decomp_card, LEFT)

        wait_until(self, 57.37 + OFFSET)
        self.play(
            Transform(vec_w, vec_Aw),
            Transform(lbl_w, lbl_Aw),
            FadeIn(sum_card),
            run_time=1.6,
        )

        # ======================================================================
        # BEAT 13 (63.39s audio): Geometric Insight card centered in content zone
        # ======================================================================
        sum_title = Text("Geometric Insight", font_size=36, weight=BOLD, color=COLOR_TEXT)
        sum_point1 = Text(
            "• Eigenvectors define the natural coordinate system for A.",
            font_size=28,
            color=COLOR_TEXT,
        )
        sum_point2 = Text(
            "• Line y = x (teal) is stretched by factor 3 (λ₁ = 3)",
            font_size=28,
            color=COLOR_TEAL,
        )
        sum_point3 = Text(
            "• Line y = -x (purple) is stretched by factor 1 (λ₂ = 1, unchanged)",
            font_size=28,
            color=COLOR_PURPLE,
        )
        sum_content = VGroup(sum_title, sum_point1, sum_point2, sum_point3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.25
        )
        summary_group = make_box(sum_content, color=COLOR_MATRIX_A, pad=0.35, max_width=11.6)
        center_in_content_zone(summary_group)

        wait_until(self, 63.39 + OFFSET)
        self.play(
            FadeOut(plane_reset),
            FadeOut(line_y_eq_x),
            FadeOut(label_y_eq_x),
            FadeOut(line_y_eq_neg_x),
            FadeOut(label_y_eq_neg_x),
            FadeOut(vec_w),
            FadeOut(lbl_w),
            FadeOut(vec_c1),
            FadeOut(vec_c2),
            FadeOut(decomp_card),
            FadeOut(sum_card),
            FadeOut(matrix_group),
            FadeIn(summary_group, scale=0.96),
            run_time=1.2,
        )

        wait_until(self, AUDIO_END - 0.8)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
        wait_until(self, AUDIO_END)
