from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ChangingEquals(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        expression_1 = MathTex("3 = 3", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "3": ORANGE_COLOR
        }).scale(3)
        expression_2 = MathTex("3 + 4 = 2 + 5", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "3": ORANGE_COLOR,
            "4": LIGHT_RED_COLOR,
            "2": LIGHT_GREEN_COLOR,
            "5": LIGHT_PURPLE_COLOR
        }).scale(3)
        expression_3 = MathTex("7 = 7", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "7": LIGHT_GREEN_COLOR
        }).scale(3)
        expression_4 = MathTex("7 - 1 = 7 - 1", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "7": LIGHT_GREEN_COLOR,
            "1": LIGHT_RED_COLOR
        }).scale(3)
        expression_5 = MathTex("6 = 6", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "6": LIGHT_PURPLE_COLOR
        }).scale(3)
        expression_6 = MathTex("6 . 2 = 6 . 2", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "6": LIGHT_PURPLE_COLOR,
            "2": LIGHT_RED_COLOR
        }).scale(3)
        expression_7 = MathTex("12 = 12", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "12": LIGHT_PURPLE_COLOR
        }).scale(3)

        self.add(expression_1)
        self.wait(1)
        self.play(Transform(expression_1, expression_2), run_time=0.7)
        self.wait(1.5)
        self.play(Transform(expression_1, expression_3), run_time=0.7)
        self.wait(1.5)
        self.play(Transform(expression_1, expression_4), run_time=0.7)
        self.wait(1.5)
        self.play(Transform(expression_1, expression_5), run_time=0.7)
        self.wait(1.5)
        self.play(Transform(expression_1, expression_6), run_time=0.7)
        self.wait(1.5)
        self.play(Transform(expression_1, expression_7), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(Group(*self.mobjects)))
        #self.play(Circumscribe(expression_1[0], color=LIGHT_RED_COLOR))
        #self.play(Circumscribe(expression_1[2], color=LIGHT_RED_COLOR))
        self.remove(*self.mobjects)