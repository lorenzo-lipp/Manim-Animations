from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class MultiplyingFractions(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        fractions = VGroup(
            MathTex(r"\frac{2}{3}", color=TEXT_COLOR).scale(2),
            MathTex(r"\frac{4}{6}", color=TEXT_COLOR).scale(2)
        ).arrange(RIGHT, buff=3)
        arrow_up = ArcBetweenPoints(
            fractions[0].get_top() + 0.2 * UP + 0.1 * RIGHT, 
            fractions[1].get_top() + 0.2 * UP + 0.1 * LEFT, 
            angle=-TAU / 4, 
            color=LIGHT_BLUE_COLOR
        ).add_tip()
        arrow_down = ArcBetweenPoints(
            fractions[0].get_bottom() + 0.2 * DOWN + 0.1 * RIGHT, 
            fractions[1].get_bottom() + 0.2 * DOWN + 0.1 * LEFT, 
            color=LIGHT_BLUE_COLOR
        ).add_tip()
        text_up = Tex(r"Multiplicado por 2", color=LIGHT_BLUE_COLOR)
        text_up.next_to(arrow_up, UP)
        text_down = Tex(r"Multiplicado por 2", color=LIGHT_BLUE_COLOR)
        text_down.next_to(arrow_down, DOWN)
        equal = MathTex("=", color=LIGHT_BLUE_COLOR)
        equal.scale(2)

        self.play(Write(fractions), run_time=0.5)
        self.play(
            Write(arrow_up),
            Write(text_up, run_time=0.7)
        )
        self.wait(0.5)
        self.play(
            Write(arrow_down),
            Write(text_down, run_time=0.7)
        )
        self.wait(1)
        self.play(Write(equal), run_time=0.5)
        self.wait(0.5)
        self.play(
            FadeOut(arrow_up),
            FadeOut(text_up),
            FadeOut(arrow_down),
            FadeOut(text_down),
            run_time=0.7
        )
        self.wait(0.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)