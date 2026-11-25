"""
scene2_concept.py - Scene 2: Concept Introduction (synced to audio/scene2.wav)

Audio: audio/scene2.wav (35.413313s) + 0.5s offset = 35.913s total.
"""

from manim import *
import numpy as np

from helpers import (
    COLOR_BG,
    COLOR_EIGEN_1,
    COLOR_MATRIX_A,
    COLOR_HIGHLIGHT,
    COLOR_TEXT,
    COLOR_AXIS,
    CONTENT_X_MIN,
    CONTENT_Y_MAX,
    CONTENT_CENTER,
    create_title_bar,
    center_in_content_zone,
    make_box,
    wait_until,
)


class Scene2Concept(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG
        OFFSET = 0.5
        AUDIO_END = 35.413313 + OFFSET

        self.add_sound("audio/scene2.wav", time_offset=OFFSET)

        # ======================================================================
        # TITLE BAR & BEAT 1 (0.82s audio): Av = lambda v reveal
        # ======================================================================
        title, underline = create_title_bar("The Central Concept: Av = \u03bbv")

        sym_A = MathTex(r"A", font_size=72, color=COLOR_MATRIX_A)
        sym_v_left = MathTex(r"\mathbf{v}", font_size=72, color=COLOR_EIGEN_1)
        sym_eq = MathTex(r"=", font_size=72, color=COLOR_TEXT)
        sym_lambda = MathTex(r"\lambda", font_size=72, color=COLOR_HIGHLIGHT)
        sym_v_right = MathTex(r"\mathbf{v}", font_size=72, color=COLOR_EIGEN_1)

        left_side = VGroup(sym_A, sym_v_left).arrange(RIGHT, buff=0.25)
        right_side = VGroup(sym_lambda, sym_v_right).arrange(RIGHT, buff=0.25)
        equation_group = VGroup(left_side, sym_eq, right_side).arrange(RIGHT, buff=0.75)

        # Braces & labels over A*v and lambda*v (>= 0.5 apart horizontally)
        brace_left = Brace(left_side, UP, buff=0.18, color=COLOR_MATRIX_A)
        left_brace_label = Text("Matrix Mult", font_size=32, color=COLOR_MATRIX_A).next_to(
            brace_left, UP, buff=0.18
        )
        brace_right = Brace(right_side, UP, buff=0.18, color=COLOR_HIGHLIGHT)
        right_brace_label = Text("Scalar Mult", font_size=32, color=COLOR_HIGHLIGHT).next_to(
            brace_right, UP, buff=0.18
        )

        # Definition cards (consistent sans-serif text style)
        card_A = VGroup(
            Text("A", font_size=34, weight=BOLD, color=COLOR_MATRIX_A),
            Text(": Linear transformation matrix (moves space)", font_size=32, color=COLOR_TEXT),
        ).arrange(RIGHT, buff=0.25)

        card_v = VGroup(
            Text("v \u2260 0", font_size=34, weight=BOLD, color=COLOR_EIGEN_1),
            Text(": Eigenvector (non-zero invariant direction)", font_size=32, color=COLOR_TEXT),
        ).arrange(RIGHT, buff=0.25)

        card_lambda = VGroup(
            Text("\u03bb", font_size=34, weight=BOLD, color=COLOR_HIGHLIGHT),
            Text(": Eigenvalue (pure scalar scaling factor)", font_size=32, color=COLOR_TEXT),
        ).arrange(RIGHT, buff=0.25)

        definitions_group = VGroup(card_A, card_v, card_lambda).arrange(
            DOWN, aligned_edge=LEFT, buff=0.4
        )

        top_eq_block = VGroup(
            brace_left, left_brace_label, brace_right, right_brace_label, equation_group
        )
        full_block = VGroup(top_eq_block, definitions_group).arrange(DOWN, buff=0.55)
        center_in_content_zone(full_block)

        wait_until(self, 0.82 + OFFSET)
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            Create(underline),
            run_time=1.0,
        )
        self.play(
            LaggedStart(
                Write(sym_A),
                Write(sym_v_left),
                Write(sym_eq),
                Write(sym_lambda),
                Write(sym_v_right),
                lag_ratio=0.25,
            ),
            run_time=2.0,
        )

        # ======================================================================
        # BEAT 2 (6.76s audio): A definition + Matrix Mult brace
        # ======================================================================
        wait_until(self, 6.76 + OFFSET)
        self.play(
            GrowFromCenter(brace_left),
            FadeIn(left_brace_label, shift=DOWN * 0.1),
            FadeIn(card_A, shift=RIGHT * 0.3),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 3 (12.50s audio): v != 0 definition
        # ======================================================================
        wait_until(self, 12.50 + OFFSET)
        self.play(FadeIn(card_v, shift=RIGHT * 0.3), run_time=1.2)

        # ======================================================================
        # BEAT 4 (17.34s audio): lambda definition + Scalar Mult brace
        # ======================================================================
        wait_until(self, 17.34 + OFFSET)
        self.play(
            GrowFromCenter(brace_right),
            FadeIn(right_brace_label, shift=DOWN * 0.1),
            FadeIn(card_lambda, shift=RIGHT * 0.3),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 5 (25.56s audio): Equation shrinks to left of content zone + diagram
        # ======================================================================
        vis_origin = np.array([-5.6, -1.35, 0.0])
        angle_rad = 20.0 * DEGREES
        line_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0.0])

        span_line = DashedLine(
            start=vis_origin - line_dir * 0.6,
            end=vis_origin + line_dir * 7.2,
            dash_length=0.15,
            color=COLOR_AXIS,
            stroke_width=2.5,
        )
        line_label = Text(
            "Invariant Direction (Span of v)", font_size=32, color="#CBD5E1"
        ).next_to(span_line, DOWN, buff=0.35)

        vec_v = Arrow(
            start=vis_origin,
            end=vis_origin + line_dir * 2.5,
            buff=0,
            color=COLOR_EIGEN_1,
            stroke_width=7,
        )
        lbl_v = MathTex(r"\mathbf{v}", font_size=38, color=COLOR_EIGEN_1).next_to(
            vec_v.get_end(), UP, buff=0.3
        )

        # Target shrunk equation in top-left of Content Zone (x >= -6.1, y <= 2.2)
        eq_target = equation_group.copy().scale(0.62)
        eq_target.move_to(
            np.array([
                CONTENT_X_MIN + 0.4 + eq_target.width / 2.0,
                CONTENT_Y_MAX - 0.4 - eq_target.height / 2.0,
                0.0,
            ])
        )

        wait_until(self, 25.56 + OFFSET)
        self.play(
            FadeOut(definitions_group, shift=DOWN * 0.2),
            FadeOut(brace_left),
            FadeOut(brace_right),
            FadeOut(left_brace_label),
            FadeOut(right_brace_label),
            Transform(equation_group, eq_target),
            run_time=1.0,
        )
        self.play(
            Create(span_line),
            FadeIn(line_label),
            GrowArrow(vec_v),
            FadeIn(lbl_v),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 6 (29.78s audio): Stretch v into Av = lambda v + Geometric Meaning
        # ======================================================================
        vec_Av = Arrow(
            start=vis_origin,
            end=vis_origin + line_dir * 6.0,
            buff=0,
            color=COLOR_MATRIX_A,
            stroke_width=5,
        )
        lbl_Av_tex = MathTex(
            r"A\mathbf{v} = \lambda\mathbf{v}", font_size=36, color=COLOR_MATRIX_A
        ).next_to(vec_Av.get_end(), DOWN, buff=0.3)
        lbl_Av_bg = BackgroundRectangle(lbl_Av_tex, color=COLOR_BG, fill_opacity=0.85, buff=0.08)
        lbl_Av = VGroup(lbl_Av_bg, lbl_Av_tex)

        note_title = Text("Geometric Meaning:", font_size=30, weight=BOLD, color=COLOR_TEXT)
        note_body1 = Text("• Direction is locked in", font_size=30, color=COLOR_EIGEN_1)
        note_body2 = Text("• Pure stretch by factor \u03bb", font_size=30, color=COLOR_HIGHLIGHT)
        note_content = VGroup(note_title, note_body1, note_body2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.18
        )
        note_group = make_box(note_content, color=COLOR_MATRIX_A, pad=0.35, max_width=5.8)
        note_group.move_to(np.array([3.6, -1.7, 0.0]))

        wait_until(self, 29.78 + OFFSET)
        self.play(
            TransformFromCopy(vec_v, vec_Av),
            FadeIn(lbl_Av),
            FadeIn(note_group, shift=LEFT * 0.2),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 7 (32.50s audio): Learning Objective card centered in content zone
        # ======================================================================
        goal_heading = Text(
            "Your Learning Objective", font_size=38, weight=BOLD, color=COLOR_EIGEN_1
        )
        goal_bullet1 = Text(
            "1. Explain what an eigenvector is\n"
            "   geometrically (fixed direction)",
            font_size=32,
            color=COLOR_TEXT,
            line_spacing=0.8,
        )
        goal_bullet2 = Text(
            "2. Find eigenvalues & eigenvectors of a 2\u00d72\n"
            "   matrix algebraically",
            font_size=32,
            color=COLOR_TEXT,
            line_spacing=0.8,
        )
        goal_content = VGroup(goal_heading, goal_bullet1, goal_bullet2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        )
        learning_goal_group = make_box(
            goal_content,
            color=COLOR_EIGEN_1,
            pad=0.5,
            max_width=12.0,
        )
        center_in_content_zone(learning_goal_group)

        wait_until(self, 32.50 + OFFSET)
        self.play(
            FadeOut(span_line),
            FadeOut(line_label),
            FadeOut(vec_v),
            FadeOut(lbl_v),
            FadeOut(vec_Av),
            FadeOut(lbl_Av),
            FadeOut(note_group),
            FadeOut(equation_group),
            FadeIn(learning_goal_group, scale=0.96),
            run_time=1.2,
        )

        wait_until(self, AUDIO_END - 0.8)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
        wait_until(self, AUDIO_END)
