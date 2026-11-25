"""
scene0_title.py - Scene 0: Silent Title Card (4.0 seconds)
"""

from manim import *

from helpers import (
    COLOR_BG,
    COLOR_MATRIX_A,
    COLOR_TEXT,
    center_in_content_zone,
    wait_until,
)


class Scene0Title(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        title = Text(
            "Eigenvalues & Eigenvectors",
            font_size=54,
            weight=BOLD,
            color=COLOR_TEXT,
        )
        subtitle = Text(
            "M3 Internal Assessment",
            font_size=38,
            color=COLOR_MATRIX_A,
        )
        student_info = Text(
            "Sagar Mangla, E25B070652",
            font_size=34,
            color="#94A3B8",
        )

        title_group = VGroup(title, subtitle, student_info).arrange(DOWN, buff=0.5)
        center_in_content_zone(title_group)

        self.play(FadeIn(title_group, shift=UP * 0.25), run_time=1.0)
        wait_until(self, 3.2)
        self.play(FadeOut(title_group, shift=DOWN * 0.25), run_time=0.8)
        wait_until(self, 4.0)
