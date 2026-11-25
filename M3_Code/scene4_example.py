"""
scene4_example.py - Scene 4: Worked Example (synced to audio/scene4.wav in audio order)

Audio: audio/scene4.wav (90.837313s) + 0.5s offset = 91.337s total.
"""

from manim import *
import numpy as np

from helpers import (
    COLOR_BG,
    COLOR_EIGEN_1,
    COLOR_EIGEN_2,
    COLOR_MATRIX_A,
    COLOR_HIGHLIGHT,
    COLOR_TEXT,
    CONTENT_Y_MAX,
    create_title_bar,
    center_in_content_zone,
    make_box,
    wait_until,
)


class Scene4Example(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG
        OFFSET = 0.5
        AUDIO_END = 90.837313 + OFFSET

        self.add_sound("audio/scene4.wav", time_offset=OFFSET)

        # ======================================================================
        # TITLE BAR & BEAT 1 (0.66s audio): Step 1, Av = lambda v -> (A - lambda I)v = 0
        # ======================================================================
        title, underline = create_title_bar("Worked Example: Algebraic Solution")

        step1_badge = Text(
            "Step 1: Characteristic Equation", font_size=32, color=COLOR_MATRIX_A
        ).move_to(np.array([0.0, CONTENT_Y_MAX - 0.45, 0.0]))

        # Rolling slots centered vertically in the content zone below step1_badge
        SLOT_TOP = np.array([0.0, 0.95, 0.0])
        SLOT_MID = np.array([0.0, -0.35, 0.0])
        SLOT_BOT = np.array([0.0, -1.80, 0.0])

        l1 = MathTex(r"A\mathbf{v} = \lambda\mathbf{v}", font_size=46, color=COLOR_TEXT).move_to(SLOT_TOP)
        l2 = MathTex(r"(A - \lambda I)\mathbf{v} = \mathbf{0}", font_size=46, color=COLOR_TEXT).move_to(SLOT_MID)

        wait_until(self, 0.66 + OFFSET)
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            Create(underline),
            FadeIn(step1_badge),
            run_time=1.0,
        )
        self.play(Write(l1), run_time=1.0)
        self.play(
            l1.animate.set_opacity(0.5),
            Write(l2),
            run_time=1.2,
        )

        # ======================================================================
        # BEAT 2 (11.04s audio): Nonzero v exists only if det(A - lambda I) = 0
        # ======================================================================
        l3 = VGroup(
            Text("Nonzero ", font_size=34, color=COLOR_TEXT),
            MathTex(r"\mathbf{v}", font_size=44, color=COLOR_EIGEN_1),
            Text(" exists only if ", font_size=34, color=COLOR_TEXT),
            MathTex(r"\det(A - \lambda I) = 0", font_size=44, color=COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.14).move_to(SLOT_BOT)

        wait_until(self, 11.04 + OFFSET)
        self.play(
            l2.animate.set_opacity(0.5),
            FadeIn(l3, shift=UP * 0.1),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 3 (18.64s audio): det([[2-lambda, 1], [1, 2-lambda]]) = 0
        # ======================================================================
        l4 = MathTex(
            r"\det \begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix} = 0",
            font_size=44,
            color=COLOR_TEXT,
        ).move_to(SLOT_BOT)

        wait_until(self, 18.64 + OFFSET)
        self.play(
            FadeOut(l1, shift=UP * 0.3),
            l2.animate.move_to(SLOT_TOP).set_opacity(0.5),
            l3.animate.move_to(SLOT_MID).set_opacity(0.5),
            Write(l4),
            run_time=1.5,
        )

        # ======================================================================
        # BEAT 4 (29.24s audio): (2 - lambda)^2 - (1)(1) = 0
        # ======================================================================
        l5 = MathTex(r"(2 - \lambda)^2 - (1)(1) = 0", font_size=46, color=COLOR_TEXT).move_to(SLOT_BOT)

        wait_until(self, 29.24 + OFFSET)
        self.play(
            FadeOut(l2, shift=UP * 0.3),
            l3.animate.move_to(SLOT_TOP).set_opacity(0.5),
            l4.animate.move_to(SLOT_MID).set_opacity(0.5),
            Write(l5),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 5 (33.78s audio): 4 - 4*lambda + lambda^2 - 1 = 0
        # ======================================================================
        l5b = MathTex(r"4 - 4\lambda + \lambda^2 - 1 = 0", font_size=46, color=COLOR_TEXT).move_to(SLOT_BOT)

        wait_until(self, 33.78 + OFFSET)
        self.play(
            FadeOut(l3, shift=UP * 0.3),
            l4.animate.move_to(SLOT_TOP).set_opacity(0.5),
            l5.animate.move_to(SLOT_MID).set_opacity(0.5),
            Write(l5b),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 6 (38.80s audio): lambda^2 - 4*lambda + 3 = 0
        # ======================================================================
        l6 = MathTex(r"\lambda^2 - 4\lambda + 3 = 0", font_size=46, color=COLOR_TEXT).move_to(SLOT_BOT)

        wait_until(self, 38.80 + OFFSET)
        self.play(
            FadeOut(l4, shift=UP * 0.3),
            l5.animate.move_to(SLOT_TOP).set_opacity(0.5),
            l5b.animate.move_to(SLOT_MID).set_opacity(0.5),
            Write(l6),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 7 (43.24s audio): Factorise -> (lambda - 1)(lambda - 3) = 0
        # ======================================================================
        l7 = MathTex(r"(\lambda - 1)(\lambda - 3) = 0", font_size=46, color=COLOR_EIGEN_1).move_to(SLOT_BOT)

        wait_until(self, 43.24 + OFFSET)
        self.play(
            FadeOut(l5, shift=UP * 0.3),
            l5b.animate.move_to(SLOT_TOP).set_opacity(0.5),
            l6.animate.move_to(SLOT_MID).set_opacity(0.5),
            Write(l7),
            run_time=1.5,
        )

        # ======================================================================
        # BEAT 8 (56.42s audio): Boxed eigenvalues lambda_1 = 1, lambda_2 = 3
        # ======================================================================
        l8 = make_box(
            MathTex(r"\lambda_1 = 1, \quad \lambda_2 = 3", font_size=48, color=COLOR_EIGEN_1),
            color=COLOR_EIGEN_1,
            pad=0.35,
            max_width=8.0,
        )
        l8.move_to(SLOT_BOT + DOWN * 0.1)

        wait_until(self, 56.42 + OFFSET)
        self.play(
            FadeOut(l5b, shift=UP * 0.3),
            l6.animate.move_to(SLOT_TOP).set_opacity(0.5),
            l7.animate.move_to(SLOT_MID).set_opacity(0.5),
            FadeIn(l8, scale=0.96),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 9 (60.30s audio): Step 2 — Eigenvector for lambda_2 = 3
        # ======================================================================
        ev_banner = make_box(
            MathTex(r"\text{Eigenvalues Found: } \lambda_2 = 3, \quad \lambda_1 = 1", font_size=38, color=COLOR_TEXT),
            color=COLOR_MATRIX_A,
            pad=0.32,
            max_width=10.5,
        )

        step2_title = Text(
            "Step 2: Eigenvector for \u03bb\u2082 = 3",
            font_size=34,
            weight=BOLD,
            color=COLOR_EIGEN_1,
        )
        eq_eig1_b = MathTex(
            r"(A - 3I)\mathbf{v} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}",
            font_size=42,
            color=COLOR_TEXT,
        )
        eq_eig1_c = MathTex(
            r"\text{Row 1: } -v_1 + v_2 = 0 \implies v_2 = v_1",
            font_size=42,
            color=COLOR_EIGEN_1,
        )
        eig1_card = make_box(
            MathTex(
                r"\text{Choose } v_1 = 1 \implies \mathbf{v}_{\lambda=3} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}",
                font_size=40,
                color=COLOR_EIGEN_1,
            ),
            color=COLOR_EIGEN_1,
            pad=0.35,
            max_width=9.0,
        )

        part2_group = VGroup(ev_banner, step2_title, eq_eig1_b, eq_eig1_c, eig1_card).arrange(DOWN, buff=0.32)
        center_in_content_zone(part2_group)

        wait_until(self, 60.30 + OFFSET)
        self.play(
            FadeOut(l6),
            FadeOut(l7),
            FadeOut(l8),
            FadeOut(step1_badge),
            FadeIn(ev_banner),
            FadeIn(step2_title),
            Write(eq_eig1_b),
            run_time=1.5,
        )

        # ======================================================================
        # BEAT 10 (66.68s audio): Row 1: -v_1 + v_2 = 0 => v_2 = v_1
        # ======================================================================
        wait_until(self, 66.68 + OFFSET)
        self.play(
            eq_eig1_b.animate.set_opacity(0.5),
            Write(eq_eig1_c),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 11 (71.52s audio): Choose v_1 = 1 => (1, 1)
        # ======================================================================
        wait_until(self, 71.52 + OFFSET)
        self.play(
            eq_eig1_c.animate.set_opacity(0.5),
            FadeIn(eig1_card, scale=0.95),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 12 (75.56s audio): Step 3 — Eigenvector for lambda_1 = 1
        # ======================================================================
        step3_title = Text(
            "Step 3: Eigenvector for \u03bb\u2081 = 1",
            font_size=34,
            weight=BOLD,
            color=COLOR_EIGEN_2,
        )
        eq_eig2_b = MathTex(
            r"(A - I)\mathbf{v} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}",
            font_size=42,
            color=COLOR_TEXT,
        )
        eq_eig2_c = MathTex(
            r"\text{Row 1: } v_1 + v_2 = 0 \implies v_2 = -v_1",
            font_size=42,
            color=COLOR_EIGEN_2,
        )
        eig2_card = make_box(
            MathTex(
                r"\text{Choose } v_1 = 1 \implies \mathbf{v}_{\lambda=1} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}",
                font_size=40,
                color=COLOR_EIGEN_2,
            ),
            color=COLOR_EIGEN_2,
            pad=0.35,
            max_width=9.0,
        )

        part3_sub = VGroup(step3_title, eq_eig2_b, eq_eig2_c, eig2_card).arrange(DOWN, buff=0.32)
        part3_sub.next_to(ev_banner, DOWN, buff=0.32)

        wait_until(self, 75.56 + OFFSET)
        self.play(
            FadeOut(step2_title),
            FadeOut(eq_eig1_b),
            FadeOut(eq_eig1_c),
            FadeOut(eig1_card),
            FadeIn(step3_title),
            Write(eq_eig2_b),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 13 (79.40s audio): Row 1: v_1 + v_2 = 0 => v_2 = -v_1
        # ======================================================================
        wait_until(self, 79.40 + OFFSET)
        self.play(
            eq_eig2_b.animate.set_opacity(0.5),
            Write(eq_eig2_c),
            run_time=1.4,
        )

        # ======================================================================
        # BEAT 14 (85.28s audio): Choose v_1 = 1 => (1, -1)
        # ======================================================================
        wait_until(self, 85.28 + OFFSET)
        self.play(
            eq_eig2_c.animate.set_opacity(0.5),
            FadeIn(eig2_card, scale=0.95),
            run_time=1.4,
        )

        wait_until(self, AUDIO_END - 0.8)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
        wait_until(self, AUDIO_END)
