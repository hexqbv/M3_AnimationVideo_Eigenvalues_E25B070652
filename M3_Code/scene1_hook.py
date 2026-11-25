"""
scene1_hook.py - Scene 1: Hook & Geometric Context (synced to audio/scene1.wav)

Audio: audio/scene1.wav (29.504s) + 0.5s offset = 30.004s total.
Colors: Orange for (1,0), Teal for (1,1), Purple for (1,-1).
"""

from manim import *
import numpy as np

from helpers import (
    COLOR_BG,
    COLOR_REGULAR,
    COLOR_ORANGE,
    COLOR_TEAL,
    COLOR_PURPLE,
    COLOR_MATRIX_A,
    COLOR_HIGHLIGHT,
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


class Scene1Hook(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG
        OFFSET = 0.5
        AUDIO_END = 29.504 + OFFSET

        self.add_sound("audio/scene1.wav", time_offset=OFFSET)

        # ======================================================================
        # TITLE BAR & PLANE + MATRIX BADGE (Beat 1: 0.40s audio)
        # ======================================================================
        title, underline = create_title_bar("Matrices Transform Space")

        plane = create_labeled_plane(
            x_range=(-4, 4, 1),
            y_range=(-3, 3, 1),
            x_length=6.4,
            y_length=4.0,
            font_size=32,
        )
        plane.move_to(np.array([1.8, CONTENT_CENTER[1], 0.0]))

        matrix_badge = create_matrix_display(
            [[2, 1], [1, 2]],
            name="A",
            color=COLOR_MATRIX_A,
            font_size=32,
        )
        badge_bg = BackgroundRectangle(
            matrix_badge, color=COLOR_BG, fill_opacity=0.85, buff=0.15
        )
        matrix_display_group = VGroup(badge_bg, matrix_badge)
        matrix_display_group.move_to(np.array([-4.5, 1.4, 0.0]))

        wait_until(self, 0.40 + OFFSET)
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            Create(underline),
            Create(plane, lag_ratio=0.05),
            FadeIn(matrix_display_group, shift=RIGHT * 0.25),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 2 (4.48s audio): Reference span lines & vectors
        # ======================================================================
        coords_orange = np.array([1.0, 0.0, 0.0])
        coords_reg2 = np.array([-1.0, 1.5, 0.0])
        coords_teal = np.array([1.0, 1.0, 0.0])
        coords_purple = np.array([1.0, -1.0, 0.0])

        origin = plane.c2p(0, 0)
        p_min, p_max = plane.c2p(-4, -3), plane.c2p(4, 3)
        px0, px1, py0, py1 = p_min[0], p_max[0], p_min[1], p_max[1]

        def make_span_line(coords, color):
            unit_dir = coords[:2] / np.linalg.norm(coords[:2])
            p_a = plane.c2p(-unit_dir[0] * 10, -unit_dir[1] * 10)
            p_b = plane.c2p(unit_dir[0] * 10, unit_dir[1] * 10)
            clipped = clip_segment_to_box(p_a, p_b, px0, px1, py0, py1)
            return DashedLine(
                start=clipped[0],
                end=clipped[1],
                dash_length=0.12,
                color=color,
                stroke_opacity=0.45,
                stroke_width=2.5,
            )

        ref_lines = VGroup(
            make_span_line(coords_orange, COLOR_ORANGE),
            make_span_line(coords_reg2, COLOR_REGULAR),
            make_span_line(coords_teal, COLOR_TEAL),
            make_span_line(coords_purple, COLOR_PURPLE),
        )

        vec_orange = Arrow(origin, plane.c2p(*coords_orange[:2]), buff=0, color=COLOR_ORANGE, stroke_width=6)
        vec_reg2 = Arrow(origin, plane.c2p(*coords_reg2[:2]), buff=0, color=COLOR_REGULAR, stroke_width=6)
        vec_teal = Arrow(origin, plane.c2p(*coords_teal[:2]), buff=0, color=COLOR_TEAL, stroke_width=6)
        vec_purple = Arrow(origin, plane.c2p(*coords_purple[:2]), buff=0, color=COLOR_PURPLE, stroke_width=6)

        lbl_orange = MathTex(r"\mathbf{v}_1", font_size=32, color=COLOR_ORANGE).next_to(vec_orange.get_end(), DOWN, buff=0.3)
        lbl_reg2 = MathTex(r"\mathbf{v}_2", font_size=32, color=COLOR_REGULAR).next_to(vec_reg2.get_end(), LEFT, buff=0.3)
        lbl_teal = MathTex(r"\mathbf{v}_3", font_size=32, color=COLOR_TEAL).next_to(vec_teal.get_end(), UP, buff=0.3)
        lbl_purple = MathTex(r"\mathbf{v}_4", font_size=32, color=COLOR_PURPLE).next_to(vec_purple.get_end(), RIGHT, buff=0.3)

        wait_until(self, 4.48 + OFFSET)
        self.play(Create(ref_lines), run_time=1.0)
        self.play(
            LaggedStart(
                AnimationGroup(GrowArrow(vec_orange), FadeIn(lbl_orange)),
                AnimationGroup(GrowArrow(vec_reg2), FadeIn(lbl_reg2)),
                AnimationGroup(GrowArrow(vec_teal), FadeIn(lbl_teal)),
                AnimationGroup(GrowArrow(vec_purple), FadeIn(lbl_purple)),
                lag_ratio=0.2,
            ),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 3 (8.80s audio): Apply A (clipped warped grid + transformed vectors)
        # ======================================================================
        matrix_2x2 = np.array([[2.0, 1.0], [1.0, 2.0]])
        warped_grid = build_clipped_warped_grid(plane, matrix_2x2)

        coords_orange_after = matrix_2x2 @ coords_orange[:2]  # (2, 1)
        coords_reg2_after = matrix_2x2 @ coords_reg2[:2]      # (-0.5, 2.0)
        coords_teal_after = matrix_2x2 @ coords_teal[:2]      # (3, 3)
        coords_purple_after = matrix_2x2 @ coords_purple[:2]  # (1, -1)

        target_vec_orange = Arrow(origin, plane.c2p(*coords_orange_after), buff=0, color=COLOR_ORANGE, stroke_width=6)
        target_vec_reg2 = Arrow(origin, plane.c2p(*coords_reg2_after), buff=0, color=COLOR_REGULAR, stroke_width=6)
        target_vec_teal = Arrow(origin, plane.c2p(*coords_teal_after), buff=0, color=COLOR_TEAL, stroke_width=6)
        target_vec_purple = Arrow(origin, plane.c2p(*coords_purple_after), buff=0, color=COLOR_PURPLE, stroke_width=6)

        lbl_orange_after = MathTex(r"A\mathbf{v}_1", font_size=32, color=COLOR_ORANGE).next_to(target_vec_orange.get_end(), RIGHT, buff=0.3)
        lbl_reg2_after = MathTex(r"A\mathbf{v}_2", font_size=32, color=COLOR_REGULAR).next_to(target_vec_reg2.get_end(), LEFT, buff=0.3)
        lbl_teal_after = MathTex(r"A\mathbf{v}_3 = 3\mathbf{v}_3", font_size=32, color=COLOR_TEAL).next_to(target_vec_teal.get_end(), RIGHT, buff=0.3)
        lbl_purple_after = MathTex(r"A\mathbf{v}_4 = 1\mathbf{v}_4", font_size=32, color=COLOR_PURPLE).next_to(target_vec_purple.get_end(), RIGHT, buff=0.3)

        wait_until(self, 8.80 + OFFSET)
        self.play(
            FadeOut(plane),
            FadeIn(warped_grid),
            Transform(vec_orange, target_vec_orange),
            Transform(vec_reg2, target_vec_reg2),
            Transform(vec_teal, target_vec_teal),
            Transform(vec_purple, target_vec_purple),
            Transform(lbl_orange, lbl_orange_after),
            Transform(lbl_reg2, lbl_reg2_after),
            Transform(lbl_teal, lbl_teal_after),
            Transform(lbl_purple, lbl_purple_after),
            run_time=2.0,
            rate_func=smooth,
        )

        # ======================================================================
        # BEAT 4 (11.08s audio): Orange arrow changed direction
        # ======================================================================
        angle_rot = np.arctan2(coords_orange_after[1], coords_orange_after[0])
        p_arc_start = origin + RIGHT * 1.4
        p_arc_end = origin + np.array([np.cos(angle_rot), np.sin(angle_rot), 0.0]) * 1.4
        curved_arrow1 = CurvedArrow(
            p_arc_start, p_arc_end, angle=PI / 6, color=COLOR_HIGHLIGHT, stroke_width=3.5
        )
        rot_label1 = Text("Direction changed!", font_size=32, color=COLOR_HIGHLIGHT).next_to(
            matrix_display_group, DOWN, buff=0.5
        ).align_to(matrix_display_group, LEFT)

        wait_until(self, 11.08 + OFFSET)
        self.play(
            Create(curved_arrow1),
            FadeIn(rot_label1),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 5 (13.82s audio): Focus on teal arrow
        # ======================================================================
        wait_until(self, 13.82 + OFFSET)
        self.play(
            Indicate(vec_teal, color=COLOR_TEAL, scale_factor=1.08),
            run_time=1.0,
        )

        # ======================================================================
        # BEAT 6 (15.54s audio): Teal stays on line, scales x3
        # ======================================================================
        stay_label1 = Text("Stays on line! (\u00d73)", font_size=32, color=COLOR_TEAL).next_to(
            rot_label1, DOWN, buff=0.45
        ).align_to(rot_label1, LEFT)
        stay_label2 = Text("Stays on line! (\u00d71)", font_size=32, color=COLOR_PURPLE).next_to(
            stay_label1, DOWN, buff=0.35
        ).align_to(stay_label1, LEFT)

        wait_until(self, 15.54 + OFFSET)
        self.play(
            FadeIn(stay_label1),
            FadeIn(stay_label2),
            Flash(vec_teal.get_end(), color=COLOR_TEAL, flash_radius=0.4),
            Flash(vec_purple.get_end(), color=COLOR_PURPLE, flash_radius=0.4),
            run_time=1.5,
        )

        # ======================================================================
        # BEAT 7 (21.82s audio): Eigenvectors hook card (centered in content zone)
        # ======================================================================
        hook_question = Text(
            "Which vectors only get stretched?",
            font_size=42,
            weight=BOLD,
            color=COLOR_TEXT,
        )
        hook_sub = Text(
            "These special directions are Eigenvectors.",
            font_size=32,
            color=COLOR_TEAL,
        )
        card_content = VGroup(hook_question, hook_sub).arrange(DOWN, buff=0.35)
        question_card = make_box(card_content, color=COLOR_MATRIX_A, pad=0.4, max_width=11.6)
        center_in_content_zone(question_card)

        wait_until(self, 21.82 + OFFSET)
        self.play(
            FadeOut(warped_grid),
            FadeOut(ref_lines),
            FadeOut(vec_orange),
            FadeOut(vec_reg2),
            FadeOut(vec_teal),
            FadeOut(vec_purple),
            FadeOut(lbl_orange),
            FadeOut(lbl_reg2),
            FadeOut(lbl_teal),
            FadeOut(lbl_purple),
            FadeOut(curved_arrow1),
            FadeOut(rot_label1),
            FadeOut(stay_label1),
            FadeOut(stay_label2),
            FadeOut(matrix_display_group),
            FadeIn(question_card, scale=0.95),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 8 (fadeout to AUDIO_END)
        # ======================================================================
        wait_until(self, AUDIO_END - 1.0)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.0)
        wait_until(self, AUDIO_END)
