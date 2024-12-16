from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Challenge(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        expression_1 = MathTex(
            "2 . m = 28", 
            tex_to_color_map={"m": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR}, 
            color=TEXT_COLOR
        )
        expression_1.scale(2)
        expression_1_copy = expression_1.copy()
        expression_2 = MathTex(
            r"2 . m \div 2 = 28 \div 2", 
            tex_to_color_map={"m": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR, r"\div 2": LIGHT_GREEN_COLOR}, 
            color=TEXT_COLOR
        )
        expression_2.scale(2)
        expression_2.shift(0.8 * DOWN)
        expression_3 = MathTex(
            r"2 . m \div 2 = 14", 
            tex_to_color_map={"m": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR, r"\div 2": LIGHT_GREEN_COLOR}, 
            color=TEXT_COLOR
        )
        expression_3.scale(2)
        expression_3.shift(0.8 * DOWN)
        expression_4 = MathTex(
            r"m = 14", 
            tex_to_color_map={"m": LIGHT_RED_COLOR, "=": LIGHT_BLUE_COLOR}, 
            color=TEXT_COLOR
        )
        expression_4.scale(2)
        expression_4.shift(0.8 * DOWN)
        # line_1 = Line(
        #     expression_2[1][1].get_corner(DL) + 0.1 * (LEFT + DOWN), 
        #     expression_2[1][1].get_corner(UR) + 0.1 * (UP + RIGHT), 
        #     color=LIGHT_RED_COLOR
        # )
        # line_2 = Line(
        #     expression_2[2][1].get_corner(DL) + 0.1 * (LEFT + DOWN), 
        #     expression_2[2][1].get_corner(UR) + 0.1 * (UP + RIGHT), 
        #     color=LIGHT_RED_COLOR
        # )

        self.play(FadeIn(expression_1))
        self.wait(4)
        self.play(
            expression_1.animate.shift(0.8 * UP),
            Transform(expression_1_copy, expression_2)
        )
        self.wait(1)
        self.play(Transform(expression_1_copy, expression_3))
        self.wait(1)
        self.play(Transform(expression_1_copy, expression_4))
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))
        self.remove(*self.mobjects)