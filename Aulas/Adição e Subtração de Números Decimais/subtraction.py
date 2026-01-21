from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Subtraction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        TEXT_SCALE = 3
        CARRY_TEXT_SCALE = TEXT_SCALE / 2.5

        subtraction = VGroup(
            MathTex("1010,00", color=BLACK).scale(TEXT_SCALE),
            VGroup(
                MathTex("-", color=BLACK).scale(TEXT_SCALE),
                MathTex("734,39", color=BLACK).scale(TEXT_SCALE)
            ).arrange(RIGHT, buff=0.5),
            MathTex(r"\hline", color=BLACK).scale(1.5).stretch_to_fit_width(6),
            MathTex("275,61", color=BLACK).scale(TEXT_SCALE)
        ).arrange(DOWN)
        subtraction[0].align_to(subtraction[1], RIGHT)
        subtraction[3].align_to(subtraction[1], RIGHT)
        subtraction[1][0].shift(0.15 * UP)
        subtraction[3].shift(0.1 * DOWN)
        carry = VGroup(
            MathTex("10", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(subtraction[0][0][6], UP, buff=0.3),
            MathTex("9", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(subtraction[0][0][5], UP, buff=0.3),
            MathTex("9", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(subtraction[0][0][3], UP, buff=0.3),
            MathTex("0", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(subtraction[0][0][2], UP, buff=0.3),
            MathTex("9", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(subtraction[0][0][1], UP, buff=0.3),
            MathTex("0", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(subtraction[0][0][0], UP, buff=0.3),
            MathTex("10", color=LIGHT_BLUE_COLOR)
                .scale(CARRY_TEXT_SCALE)
                .next_to(subtraction[0][0][2], UP, buff=1),
        )
        cross = VGroup(
            Line(
                subtraction[0][0][-1].get_boundary_point(DL) + 0.15 * (DL), 
                subtraction[0][0][-1].get_boundary_point(UR) + 0.15 * (UR), 
                color=LIGHT_BLUE_COLOR
            ),
        )

        for i in [-2, -4, -5, -6, -7]:
            cross.add(cross[0].copy().move_to(subtraction[0][0][i]))
        
        cross.add(
            Line(
                carry[3].get_boundary_point(DL) + 0.05 * (DL), 
                carry[3].get_boundary_point(UR) + 0.05 * (UR), 
                color=LIGHT_BLUE_COLOR
            )
        )

        self.play(Write(VGroup(subtraction[0][0][:-3], subtraction[1:3])))
        self.wait(3)
        self.play(FadeIn(subtraction[0][0][-3:]), run_time=0.5)
        self.play(Indicate(subtraction[0][0][-3:]), scale_factor=1.2, color=LIGHT_RED_COLOR, run_time=0.7)
        self.play(Write(subtraction[3][0][-3]), run_time=0.7)
        self.wait(0.5)

        for i in range(4):
            self.play(LaggedStart(
                Write(cross[3 - i], run_time=0.5),
                FadeIn(carry[3 - i], run_time=0.5),
                lag_ratio=0.5
            ))

        self.wait(0.5)

        for [i, j] in [[0, -1], [1, -2], [2, -4]]:
            self.play(LaggedStart(
                Circumscribe(Group(carry[i], subtraction[1][1][0][j]), color=LIGHT_RED_COLOR, run_time=1.2),
                Write(subtraction[3][0][j], run_time=0.5),
                lag_ratio=0.75
            ))

        self.wait(0.5)

        for i in [5, 4, -1]:
            self.play(LaggedStart(
                Write(cross[i], run_time=0.5),
                FadeIn(carry[i], run_time=0.5),
                lag_ratio=0.5
            ))

        self.wait(0.5)

        for [i, j] in [[-1, -5], [-3, -6]]:
            self.play(LaggedStart(
                Circumscribe(Group(carry[i], subtraction[1][1][0][j]), color=LIGHT_RED_COLOR, run_time=1.2),
                Write(subtraction[3][0][j], run_time=0.5),
                lag_ratio=0.75
            ))

        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)