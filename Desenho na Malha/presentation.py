from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        vertical_lines = VGroup()
        for i in range(22):
            vertical_lines.add(Line(1.4 * UP, 1.4 * DOWN, color=LIGHT_GREY))
        vertical_lines.arrange(RIGHT, buff=0.4)
        horizontal_lines = VGroup()
        for i in range(8):
            horizontal_lines.add(Line(4.2 * LEFT, 4.2 * RIGHT, color=LIGHT_GREY))
        horizontal_lines.arrange(DOWN, buff=0.4)
        lines = VGroup(
            Line(DOWN + 3.8 * LEFT, 0.2 * UP + 3.8 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.2 * UP + 3.8 * LEFT, 0.2 * UP + 2.6 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.2 * UP + 2.6 * LEFT, DOWN + 2.6 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(DOWN + 2.6 * LEFT, DOWN + 2.2 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(DOWN + 2.2 * LEFT, 0.2 * DOWN + 2.2 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.2 * DOWN + 2.2 * LEFT, 0.2 * DOWN + 1.4 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.2 * DOWN + 1.4 * LEFT, DOWN + 1.4 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(DOWN + 1.4 * LEFT, DOWN + LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(DOWN + LEFT, 0.6 * DOWN + LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.6 * DOWN + LEFT, 0.6 * DOWN + 0.6 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.6 * DOWN + 0.6 * LEFT, DOWN + 0.6 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(DOWN + 0.6 * LEFT, DOWN + 0.2 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(DOWN + 0.2 * LEFT, 0.2 * UP + 0.2 * LEFT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.2 * UP + 0.2 * LEFT, 0.2 * UP + 1 * RIGHT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(0.2 * UP + 1 * RIGHT, DOWN + 1 * RIGHT, color=LIGHT_RED_COLOR, stroke_width=6),
            Line(DOWN + 1 * RIGHT, DOWN + 1.4 * RIGHT, color=LIGHT_RED_COLOR, stroke_width=6)
        )
        dots = VGroup(
            Dot(DOWN + 1.8 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(0.2 * UP + 2.2 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(0.2 * DOWN + 2.6 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(0.2 * UP + 3.4 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(DOWN + 3.8 * RIGHT, color=LIGHT_RED_COLOR),
        )

        self.play(FadeIn(vertical_lines, horizontal_lines))
        for line in lines:
            self.play(Create(line), run_time=0.4)
        self.play(FadeIn(dots))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)