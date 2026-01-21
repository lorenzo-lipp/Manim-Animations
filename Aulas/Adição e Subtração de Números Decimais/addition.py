from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Addition(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        TEXT_SCALE = 3
        CARRY_TEXT_SCALE = TEXT_SCALE / 2
        
        addition = VGroup(
            MathTex("312,25", color=BLACK).scale(TEXT_SCALE),
            VGroup(
                MathTex("+", color=BLACK).scale(TEXT_SCALE),
                MathTex("195,90", color=BLACK).scale(TEXT_SCALE)
            ).arrange(RIGHT, buff=0.5),
            MathTex(r"\hline", color=BLACK).scale(1.5).stretch_to_fit_width(6),
            MathTex("508,15", color=BLACK).scale(TEXT_SCALE)
        ).arrange(DOWN)
        addition[0].align_to(addition[1], RIGHT)
        addition[3].align_to(addition[1], RIGHT)
        addition[1][0].shift(0.15 * UP)
        addition[3].shift(0.1 * DOWN)
        carry = VGroup(
            MathTex("1", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(addition[0][0][2], UP, buff=0.3),
            MathTex("1", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(addition[0][0][0], UP, buff=0.3),
            MathTex("11", color=BLACK)
                .scale(CARRY_TEXT_SCALE)
                .next_to(addition[3][0][-1], LEFT, buff=0.3),
            MathTex("10", color=BLACK)
                .scale(CARRY_TEXT_SCALE)
                .next_to(addition[3][0][-4], LEFT, buff=0.3),
        )

        self.play(Write(VGroup(addition[0], addition[1][0], addition[1][1][0][:-1], addition[2])))
        self.wait(3)
        self.play(FadeIn(addition[1][1][0][-1]), run_time=0.5)
        self.play(Indicate(addition[1][1][0][-1]), scale_factor=1.2, color=LIGHT_RED_COLOR, run_time=0.7)
        self.wait(0.5)
        self.play(LaggedStart(
                Circumscribe(Group(addition[0][0][-1], addition[1][1][0][-1]), color=LIGHT_RED_COLOR, run_time=1.2),
                Write(addition[3][0][-1], run_time=0.5),
                lag_ratio=0.75
        ))
        self.play(LaggedStart(
                Circumscribe(Group(addition[0][0][-2], addition[1][1][0][-2]), color=LIGHT_RED_COLOR, run_time=1.2),
                Write(carry[2], run_time=0.5),
                lag_ratio=0.75
        ))
        self.play(
            Transform(carry[2][0][1], addition[3][0][-2]),
            Transform(carry[2][0][0], carry[0])
        )
        self.play(Write(addition[3][0][-3]), run_time=0.5)
        self.play(LaggedStart(
            Circumscribe(Group(carry[0],addition[0][0][-4], addition[1][1][0][-4]), color=LIGHT_RED_COLOR, run_time=1.2),
            Write(addition[3][0][-4], run_time=0.5),
            lag_ratio=0.75
        ))
        self.play(LaggedStart(
            Circumscribe(Group(addition[0][0][-5], addition[1][1][0][-5]), color=LIGHT_RED_COLOR, run_time=1.2),
            Write(carry[3], run_time=0.5),
            lag_ratio=0.75
        ))
        self.play(
            Transform(carry[3][0][1], addition[3][0][-5]),
            Transform(carry[3][0][0], carry[1])
        )
        self.play(LaggedStart(
            Circumscribe(Group(carry[1],addition[0][0][-6], addition[1][1][0][-6]), color=LIGHT_RED_COLOR, run_time=1.2),
            Write(addition[3][0][-6], run_time=0.5),
            lag_ratio=0.75
        ))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)