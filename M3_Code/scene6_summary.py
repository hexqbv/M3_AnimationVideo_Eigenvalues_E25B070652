"""
scene6_summary.py - Scene 6: Summary & Credits (synced to audio/scene6.wav + 8s silent hold)

Audio: audio/scene6.wav (26.432s) + 0.5s offset = 26.932s audio end.
Plus 8.0s extra silent hold on closing credits = 34.932s total.
"""

from manim import *

from helpers import (
    COLOR_BG,
    COLOR_EIGEN_1,
    COLOR_EIGEN_2,
    COLOR_MATRIX_A,
    COLOR_TEXT,
    CONTENT_HEIGHT,
    create_title_bar,
    center_in_content_zone,
    make_box,
    wait_until,
)


class Scene6Summary(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG
        OFFSET = 0.5
        AUDIO_END = 26.432 + OFFSET
        SCENE_END = AUDIO_END + 8.0

        self.add_sound("audio/scene6.wav", time_offset=OFFSET)

        # ======================================================================
        # TITLE BAR & TAKEAWAYS (centered vertically in Content Zone)
        # ======================================================================
        title, underline = create_title_bar("Summary: Core Takeaways")

        def make_card(card_title, body, stroke_color):
            t_num = Text(card_title, font_size=28, weight=BOLD, color=stroke_color)
            t_txt = Text(body, font_size=24, color=COLOR_TEXT, line_spacing=0.8)
            content = VGroup(t_num, t_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            return make_box(
                content,
                color=stroke_color,
                pad=0.35,
                fixed_width=11.6,
                align_content="left",
            )

        card1 = make_card(
            "1. Geometric Invariance:",
            "Eigenvectors keep their direction under A\n(pure stretch, zero rotation).",
            COLOR_MATRIX_A,
        )
        card2 = make_card(
            "2. Finding Eigenvalues (\u03bb):",
            "\u03bb is the stretch factor, calculated by setting det(A - \u03bbI) = 0.",
            COLOR_EIGEN_1,
        )
        card3 = make_card(
            "3. Finding Eigenvectors (v):",
            "For each \u03bb, eigenvectors are non-zero solutions to (A - \u03bbI)v = 0.",
            COLOR_EIGEN_2,
        )
        det_note = Text(
            "det(A) = \u03bb\u2081 \u00b7 \u03bb\u2082   (Area scaling factor)",
            font_size=26,
            color=COLOR_EIGEN_1,
        )

        stack = VGroup(card1, card2, card3).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        det_note.next_to(stack, DOWN, buff=0.40)
        summary_stack = VGroup(stack, det_note)
        center_in_content_zone(summary_stack)

        # Takeaway 1 (0.37s - 7.10s audio, strictly before 7.50s)
        wait_until(self, 0.37 + OFFSET)
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            Create(underline),
            FadeIn(card1, shift=UP * 0.2),
            run_time=1.2,
        )

        # Takeaway 2 (7.50s audio)
        wait_until(self, 7.50 + OFFSET)
        self.play(FadeIn(card2, shift=UP * 0.2), run_time=1.0)

        # Takeaway 3 (14.83s audio)
        wait_until(self, 14.83 + OFFSET)
        self.play(FadeIn(card3, shift=UP * 0.2), run_time=1.0)

        # Takeaway 4 (20.27s audio)
        wait_until(self, 20.27 + OFFSET)
        self.play(FadeIn(det_note, shift=UP * 0.15), run_time=1.0)

        # ======================================================================
        # CLOSING CREDITS (25.61s audio -> 26.11s scene, then 8s silent hold)
        # ======================================================================
        cred_title = Text("Eigenvalues & Eigenvectors", font_size=34, weight=BOLD, color=COLOR_TEXT)
        cred_author = Text("Produced by: Sagar Mangla, E25B070652", font_size=30, color=COLOR_MATRIX_A)

        ref_heading = Text("Academic References & Resources:", font_size=30, weight=BOLD, color=COLOR_EIGEN_1)
        ref_text1 = Text("• Gilbert Strang, Introduction to Linear Algebra (5th Edition)", font_size=30, color=COLOR_TEXT)
        ref_text2 = Text("• 3Blue1Brown, Essence of Linear Algebra (inspiration only)", font_size=30, color=COLOR_TEXT)

        tool_music = Text("Built with Manim Community Edition   |   Music: none", font_size=30, color="#94A3B8")

        disc_title = Text("Academic AI Disclosure:", font_size=32, weight=BOLD, color="#94A3B8")
        disc_body = Text(
            "Antigravity (Gemini) was used to help draft the storyboard\n"
            "and write/debug Manim code. All mathematics was verified\n"
            "by me. Narration recorded by me.",
            font_size=32,
            color=COLOR_TEXT,
            line_spacing=0.8,
        )
        disc_content = VGroup(disc_title, disc_body).arrange(
            DOWN, aligned_edge=LEFT, buff=0.10
        )
        disclosure_card = make_box(disc_content, color="#475569", pad=0.35, max_width=11.8)

        credits_group = VGroup(
            cred_title,
            cred_author,
            ref_heading,
            ref_text1,
            ref_text2,
            tool_music,
            disclosure_card,
        ).arrange(DOWN, buff=0.18)
        center_in_content_zone(credits_group)

        wait_until(self, 25.61 + OFFSET)
        self.play(
            FadeOut(title),
            FadeOut(underline),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(det_note),
            run_time=0.8,
        )
        self.play(FadeIn(credits_group, scale=0.97), run_time=1.2)

        # Hold credits silently for 8 extra seconds after audio ends
        wait_until(self, SCENE_END - 1.0)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.0)
        wait_until(self, SCENE_END)
