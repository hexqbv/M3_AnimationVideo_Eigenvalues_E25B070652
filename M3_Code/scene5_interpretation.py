"""
scene5_interpretation.py - Scene 5: Interpretation (synced to audio/scene5.wav)

Audio: audio/scene5.wav (47.296s) + 0.5s offset = 47.796s total.
"""

from manim import *
import numpy as np

from helpers import (
    COLOR_BG,
    COLOR_EIGEN_1,
    COLOR_EIGEN_2,
    COLOR_MATRIX_A,
    COLOR_TEXT,
    CONTENT_CENTER,
    create_title_bar,
    create_labeled_plane,
    make_box,
    wait_until,
)


class Scene5Interpretation(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG
        OFFSET = 0.5
        AUDIO_END = 47.296 + OFFSET

        self.add_sound("audio/scene5.wav", time_offset=OFFSET)

        # ======================================================================
        # TITLE BAR & BEAT 1 (1.04s audio): Coordinate plane in Content Zone
        # ======================================================================
        title, underline = create_title_bar("Interpretation: Verification & Area Scaling")

        plane = create_labeled_plane(
            x_range=(-4, 4, 1),
            y_range=(-3, 3, 1),
            x_length=5.8,
            y_length=4.0,
            font_size=32,
        ).move_to(np.array([-2.9, CONTENT_CENTER[1], 0.0]))

        wait_until(self, 1.04 + OFFSET)
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            Create(underline),
            Create(plane, lag_ratio=0.04),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 2A (3.94s audio): Verification 1 — heading INSIDE box with 0.2 padding
        # ======================================================================
        origin = plane.c2p(0, 0)
        vec_e1 = Arrow(origin, plane.c2p(3.0, 3.0), buff=0, color=COLOR_EIGEN_1, stroke_width=6)
        lbl_vec_e1_tex = MathTex(r"A\mathbf{v}_1", font_size=32, color=COLOR_EIGEN_1).next_to(
            plane.c2p(3.0, 3.0), LEFT, buff=0.3
        )
        lbl_vec_e1 = VGroup(
            BackgroundRectangle(lbl_vec_e1_tex, color=COLOR_BG, fill_opacity=0.8, buff=0.06),
            lbl_vec_e1_tex,
        )

        card_v1_title = Text("Verification 1 (\u03bb\u2082 = 3):", font_size=30, weight=BOLD, color=COLOR_EIGEN_1)
        card_v1_top = MathTex(r"\text{Top: } 2(1) + 1(1) = 3", font_size=30, color=COLOR_TEXT)
        card_v1_bot = MathTex(r"\text{Bot: } 1(1) + 2(1) = 3", font_size=30, color=COLOR_TEXT)
        card_v1_res = MathTex(
            r"\begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ 1 \end{pmatrix} \ \checkmark",
            font_size=30,
            color=COLOR_EIGEN_1,
        )
        card_v1_content = VGroup(card_v1_title, card_v1_top, card_v1_bot, card_v1_res).arrange(
            DOWN, aligned_edge=LEFT, buff=0.10
        )
        card_v1 = make_box(card_v1_content, color=COLOR_EIGEN_1, pad=0.32, max_width=6.0)
        card_v1_bg = card_v1.box

        card_v2_title = Text("Verification 2 (\u03bb\u2081 = 1):", font_size=30, weight=BOLD, color=COLOR_EIGEN_2)
        card_v2_math1 = MathTex(
            r"\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}",
            font_size=30,
            color=COLOR_TEXT,
        )
        card_v2_math2 = MathTex(
            r"= 1 \begin{pmatrix} 1 \\ -1 \end{pmatrix} \ \checkmark",
            font_size=30,
            color=COLOR_EIGEN_2,
        )
        card_v2_content = VGroup(card_v2_title, card_v2_math1, card_v2_math2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.10
        )
        card_v2 = make_box(card_v2_content, color=COLOR_EIGEN_2, pad=0.32, max_width=6.0)

        right_cards = VGroup(card_v1, card_v2).arrange(DOWN, buff=0.22).move_to(
            np.array([3.55, CONTENT_CENTER[1], 0.0])
        )

        wait_until(self, 3.94 + OFFSET)
        self.play(
            GrowArrow(vec_e1),
            FadeIn(lbl_vec_e1),
            FadeIn(card_v1_bg),
            FadeIn(card_v1_title),
            Write(card_v1_top),
            run_time=1.6,
        )

        # ======================================================================
        # BEAT 2B (10.28s audio): Verification 1 — bottom row = 3
        # ======================================================================
        wait_until(self, 10.28 + OFFSET)
        self.play(Write(card_v1_bot), run_time=1.2)

        # ======================================================================
        # BEAT 2C (13.74s audio): Verification 1 — result = 3*(1, 1)
        # ======================================================================
        wait_until(self, 13.74 + OFFSET)
        self.play(
            Write(card_v1_res),
            Flash(plane.c2p(3.0, 3.0), color=COLOR_EIGEN_1, flash_radius=0.4),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 3 (18.06s audio): Verification 2 — A(1, -1) = 1*(1, -1)
        # ======================================================================
        vec_e2 = Arrow(origin, plane.c2p(1.2, -1.2), buff=0, color=COLOR_EIGEN_2, stroke_width=6)
        lbl_vec_e2_tex = MathTex(r"A\mathbf{v}_2", font_size=32, color=COLOR_EIGEN_2).next_to(
            plane.c2p(1.2, -1.2), RIGHT, buff=0.3
        )
        lbl_vec_e2 = VGroup(
            BackgroundRectangle(lbl_vec_e2_tex, color=COLOR_BG, fill_opacity=0.8, buff=0.06),
            lbl_vec_e2_tex,
        )

        wait_until(self, 18.06 + OFFSET)
        self.play(
            GrowArrow(vec_e2),
            FadeIn(lbl_vec_e2),
            FadeIn(card_v2, shift=LEFT * 0.3),
            Flash(plane.c2p(1.2, -1.2), color=COLOR_EIGEN_2, flash_radius=0.4),
            run_time=1.8,
        )

        # ======================================================================
        # BEAT 4 (28.62s audio): Show grey Unit Square (area = 1)
        # ======================================================================
        unit_poly_grey = Polygon(
            plane.c2p(0, 0),
            plane.c2p(1, 0),
            plane.c2p(1, 1),
            plane.c2p(0, 1),
            fill_color="#94A3B8",
            fill_opacity=0.35,
            stroke_color="#CBD5E1",
            stroke_width=3,
        )
        unit_poly_anim = unit_poly_grey.copy().set_fill(COLOR_MATRIX_A, opacity=0.35).set_stroke(COLOR_MATRIX_A, width=3)

        area1_txt = Text("area = 1", font_size=32, color="#CBD5E1").next_to(
            unit_poly_grey, DOWN, buff=0.3
        )
        area1_lbl = VGroup(
            BackgroundRectangle(area1_txt, color=COLOR_BG, fill_opacity=0.8, buff=0.06),
            area1_txt,
        )

        wait_until(self, 28.62 + OFFSET)
        self.play(
            FadeOut(vec_e1),
            FadeOut(lbl_vec_e1),
            FadeOut(card_v1),
            FadeOut(vec_e2),
            FadeOut(lbl_vec_e2),
            FadeOut(card_v2),
            DrawBorderThenFill(unit_poly_grey),
            FadeIn(area1_lbl),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 5 (30.12s audio): Keep grey unit square visible under parallelogram
        # ======================================================================
        sheared_poly = Polygon(
            plane.c2p(0, 0),
            plane.c2p(2, 1),
            plane.c2p(3, 3),
            plane.c2p(1, 2),
            fill_color=COLOR_MATRIX_A,
            fill_opacity=0.35,
            stroke_color=COLOR_MATRIX_A,
            stroke_width=3,
        )
        self.add(unit_poly_anim)

        wait_until(self, 30.12 + OFFSET)
        self.play(
            Transform(unit_poly_anim, sheared_poly),
            run_time=2.0,
        )

        # ======================================================================
        # BEAT 6 (33.00s audio): Show "area = 3" beside parallelogram & det(A) card
        # ======================================================================
        area3_txt = Text("area = 3", font_size=32, weight=BOLD, color=COLOR_MATRIX_A).next_to(
            sheared_poly, UP, buff=0.3
        )
        area3_lbl = VGroup(
            BackgroundRectangle(area3_txt, color=COLOR_BG, fill_opacity=0.8, buff=0.06),
            area3_txt,
        )

        area_card_t1 = Text("Area Scaling Law:", font_size=32, weight=BOLD, color=COLOR_TEXT)
        area_card_t2 = MathTex(r"\text{Area Scale} = \det(A)", font_size=32, color=COLOR_MATRIX_A)
        area_card_t3 = MathTex(r"= (2)(2) - (1)(1) = 3", font_size=32, color=COLOR_TEXT)
        area_card_t4 = MathTex(
            r"= \lambda_1 \cdot \lambda_2 = 1 \cdot 3 = 3 \ \checkmark",
            font_size=32,
            color=COLOR_EIGEN_1,
        )
        area_card_content = VGroup(area_card_t1, area_card_t2, area_card_t3, area_card_t4).arrange(
            DOWN, aligned_edge=LEFT, buff=0.18
        )
        area_card = make_box(area_card_content, color=COLOR_MATRIX_A, pad=0.35, max_width=6.0).move_to(
            np.array([3.55, CONTENT_CENTER[1] + 0.4, 0.0])
        )
        area_card_bg = area_card.box

        wait_until(self, 33.00 + OFFSET)
        self.play(
            FadeIn(area3_lbl),
            FadeIn(area_card_bg),
            FadeIn(area_card_t1),
            Write(area_card_t2),
            Write(area_card_t3),
            run_time=1.0,
        )

        wait_until(self, 34.00 + OFFSET)
        self.play(Write(area_card_t4), run_time=1.2)

        # ======================================================================
        # BEAT 7 (43.32s audio): Highlight "Area x3"
        # ======================================================================
        area_badge = Text("Area \u00d73", font_size=36, weight=BOLD, color=COLOR_EIGEN_1).next_to(
            area_card, DOWN, buff=0.4
        )
        wait_until(self, 43.32 + OFFSET)
        self.play(
            FadeIn(area_badge, scale=1.15),
            Indicate(area3_lbl, color=COLOR_EIGEN_1, scale_factor=1.18),
            run_time=1.2,
        )

        wait_until(self, AUDIO_END - 0.8)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
        wait_until(self, AUDIO_END)
