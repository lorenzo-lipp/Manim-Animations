from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ThreeEqualsThree(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        expression = MathTex("3 = 3", color=LIGHT_BLUE_COLOR, tex_to_color_map={
            "3": ORANGE_COLOR
        })
        expression.scale(3)

        self.play(Write(expression))
        self.wait(1)
        self.play(Circumscribe(expression[0], color=LIGHT_RED_COLOR))
        self.play(Circumscribe(expression[2], color=LIGHT_RED_COLOR))
        self.remove(*self.mobjects)