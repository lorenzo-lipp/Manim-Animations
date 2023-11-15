from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class MultiplyingTwoSteps(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        fractions = VGroup(
            MathTex(r"\frac{4}{8}", color=TEXT_COLOR).scale(2),
            MathTex(r"\frac{1}{2}", color=TEXT_COLOR).scale(2),
            MathTex(r"\frac{5}{10}", color=TEXT_COLOR).scale(2)
        ).arrange(RIGHT, buff=2)
        arrow_up_1 = ArcBetweenPoints(
            fractions[0].get_top() + 0.2 * UP + 0.1 * RIGHT, 
            fractions[1].get_top() + 0.2 * UP + 0.1 * LEFT, 
            angle=-TAU / 4, 
            color=LIGHT_BLUE_COLOR
        ).add_tip()
        arrow_down_1 = ArcBetweenPoints(
            fractions[0].get_bottom() + 0.2 * DOWN + 0.1 * RIGHT, 
            fractions[1].get_bottom() + 0.2 * DOWN + 0.1 * LEFT, 
            color=LIGHT_BLUE_COLOR
        ).add_tip()
        text_up_1 = Tex(r"Dividido por 4", color=LIGHT_BLUE_COLOR)
        text_up_1.scale(0.7)
        text_up_1.next_to(arrow_up_1, UP)
        text_down_1 = Tex(r"Dividido por 4", color=LIGHT_BLUE_COLOR)
        text_down_1.scale(0.7)
        text_down_1.next_to(arrow_down_1, DOWN)
        equal_1 = MathTex(r"=", color=LIGHT_BLUE_COLOR)
        equal_1.shift(1.5 * LEFT)
        equal_1.scale(2)
        arrow_up_2 = ArcBetweenPoints(
            fractions[1].get_top() + 0.2 * UP + 0.1 * RIGHT, 
            fractions[2].get_top() + 0.2 * UP, 
            angle=-TAU / 4, 
            color=LIGHT_BLUE_COLOR
        ).add_tip()
        arrow_down_2 = ArcBetweenPoints(
            fractions[1].get_bottom() + 0.2 * DOWN + 0.1 * RIGHT, 
            fractions[2].get_bottom() + 0.2 * DOWN, 
            color=LIGHT_BLUE_COLOR
        ).add_tip()
        text_up_2 = Tex(r"Multiplicado por 5", color=LIGHT_BLUE_COLOR)
        text_up_2.scale(0.7)
        text_up_2.next_to(arrow_up_2, UP, buff=0.2)
        text_down_2 = Tex(r"Multiplicado por 5", color=LIGHT_BLUE_COLOR)
        text_down_2.scale(0.7)
        text_down_2.next_to(arrow_down_2, DOWN, buff=0.2)
        equal_2 = MathTex(r"=", color=LIGHT_BLUE_COLOR)
        equal_2.shift(1.1 * RIGHT)
        equal_2.scale(2)

        self.play(Write(fractions), run_time=0.5)
        self.play(
            Write(arrow_up_1),
            Write(text_up_1, run_time=0.7)
        )
        self.wait(0.5)
        self.play(
            Write(arrow_down_1),
            Write(text_down_1, run_time=0.7)
        )
        self.wait(1)
        self.play(Write(equal_1), run_time=0.5)
        self.wait(0.5)
        self.play(
            FadeOut(arrow_up_1), 
            FadeOut(arrow_down_1), 
            FadeOut(text_up_1), 
            FadeOut(text_down_1), 
            run_time=0.7
        )
        self.play(
            Write(arrow_up_2),
            Write(text_up_2, run_time=0.7)
        )
        self.wait(0.5)
        self.play(
            Write(arrow_down_2),
            Write(text_down_2, run_time=0.7)
        )
        self.wait(1)
        self.play(Write(equal_2), run_time=0.5)
        self.wait(0.5)
        self.play(
            FadeOut(arrow_up_2), 
            FadeOut(arrow_down_2), 
            FadeOut(text_up_2), 
            FadeOut(text_down_2), 
            run_time=0.7
        )
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)