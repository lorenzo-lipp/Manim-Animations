from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class UnknownValue(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        expression_1 = MathTex(
            "a - 5 = 18", 
            tex_to_color_map={"a": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR}, 
            color=TEXT_COLOR
        )
        expression_1.scale(2)
        expression_1_copy = expression_1.copy()
        expression_2 = MathTex(
            "a - 5 + 5 = 18 + 5", 
            tex_to_color_map={"a": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR, "+ 5": LIGHT_GREEN_COLOR}, 
            color=TEXT_COLOR
        )
        expression_2.scale(2)
        expression_2.shift(0.8 * DOWN)
        expression_3 = MathTex(
            "a = 18 + 5", 
            tex_to_color_map={"a": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR, "+ 5": LIGHT_GREEN_COLOR}, 
            color=TEXT_COLOR
        )
        expression_3.scale(2)
        expression_3.shift(0.8 * DOWN)
        expression_4 = MathTex(
            "a = 23", 
            tex_to_color_map={"a": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR}, 
            color=TEXT_COLOR
        )
        expression_4.scale(2)
        expression_4.shift(0.8 * DOWN)
        line_1 = Line(
            expression_2[1][1].get_corner(DL) + 0.1 * (LEFT + DOWN), 
            expression_2[1][1].get_corner(UR) + 0.1 * (UP + RIGHT), 
            color=LIGHT_RED_COLOR
        )
        line_2 = Line(
            expression_2[2][1].get_corner(DL) + 0.1 * (LEFT + DOWN), 
            expression_2[2][1].get_corner(UR) + 0.1 * (UP + RIGHT), 
            color=LIGHT_RED_COLOR
        )

        self.play(Write(expression_1))
        self.wait(1)
        self.play(Indicate(expression_1[0], color=LIGHT_ORANGE_COLOR, scale_factor=1.5))
        self.wait(1)
        self.play(
            expression_1.animate.shift(0.8 * UP),
            Transform(expression_1_copy, expression_2)
        )
        self.wait(1)
        self.play(
            Create(line_1),
            Create(line_2)
        )
        self.wait(0.5)
        self.play(
            Transform(expression_1_copy, expression_3),
            FadeOut(Group(line_1, line_2), rate_func=rush_from)
        )
        self.wait(1.5)
        self.play(Transform(expression_1_copy, expression_4))
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))
        self.remove(*self.mobjects)