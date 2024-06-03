from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Length(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        camp = VGroup(
            Rectangle(LIGHT_GREEN_COLOR, 9, 6, fill_opacity=1),
            Rectangle(WHITE, 8, 5, stroke_width=8),
            Rectangle(WHITE, 1, 2, stroke_width=8)
                .shift(3.5 * UP),
            Rectangle(WHITE, 0.4, 1, stroke_width=8)
                .shift(3.8 * UP),
            Rectangle(WHITE, 1, 2, stroke_width=8)
                .shift(3.5 * DOWN),
            Rectangle(WHITE, 0.4, 1, stroke_width=8)
                .shift(3.8 * DOWN),
            ArcBetweenPoints(3 * UP + 0.6 * LEFT, 3 * UP + 0.6 * RIGHT, color=WHITE, stroke_width=8),
            ArcBetweenPoints(3 * DOWN + 0.6 * RIGHT, 3 * DOWN + 0.6 * LEFT, color=WHITE, stroke_width=8),
            ArcBetweenPoints(3.6 * UP + 2.5 * LEFT, 4 * UP + 2.1 * LEFT, color=WHITE, stroke_width=8),
            ArcBetweenPoints(4 * UP + 2.1 * RIGHT, 3.6 * UP + 2.5 * RIGHT, color=WHITE, stroke_width=8),
            ArcBetweenPoints(4 * DOWN + 2.1 * LEFT, 3.6 * DOWN + 2.5 * LEFT, color=WHITE, stroke_width=8),
            ArcBetweenPoints(3.6 * DOWN + 2.5 * RIGHT, 4 * DOWN + 2.1 * RIGHT, color=WHITE, stroke_width=8),
            Circle(1, color=WHITE, stroke_width=8),
            Line(2.5 * LEFT, 2.5 * RIGHT, color=WHITE, stroke_width=8),
            Dot(color=WHITE),
            Dot(3.3 * UP, color=WHITE),
            Dot(3.3 * DOWN, color=WHITE)
        )
        height = DoubleArrow(
            [camp.get_right()[0] + 0.5, camp.get_top()[1] + 0.3, 0], 
            [camp.get_right()[0] + 0.5, camp.get_bottom()[1] - 0.3, 0],
            color=LIGHT_GREEN_COLOR
        )
        width = DoubleArrow(
            [camp.get_left()[0] - 0.3, camp.get_bottom()[1] - 0.5, 0], 
            [camp.get_right()[0] + 0.3, camp.get_bottom()[1] - 0.5, 0],
            color=LIGHT_GREEN_COLOR
        )
        measurement_text = VGroup(
            Tex("Comprimento", color=LIGHT_RED_COLOR),
            Tex("(metros ou centímetros)", color=LIGHT_RED_COLOR)
        ).arrange(DOWN, buff=0.5)
        measurement_text[0].scale(2)
        measurement_text.next_to(camp, DOWN, buff=0.9)

        self.play(AnimateFromLeft(camp))
        self.wait(1)
        self.play(FadeIn(height), run_time=0.8)
        self.wait(1.7)
        self.play(Write(measurement_text))
        self.wait(1.3)
        self.play(
            Transform(measurement_text[0], Tex("Largura", color=LIGHT_RED_COLOR).scale(2).move_to(measurement_text[0])),
            Transform(height, width)
        )
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)
        