from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class AddSameBase(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        frac = MathTex(
            r"\frac{1}{2} + \frac{6}{2} = \frac{?}{?}", 
            color=BLACK,
            tex_to_color_map={r"\frac{1}{2}": LIGHT_BLUE_COLOR, r"\frac{6}{2}": LIGHT_PURPLE_COLOR}
        )
        frac.scale(2.5)
        unknown_numerator = SingleStringMathTex("7", color=LIGHT_GREEN_COLOR)
        unknown_numerator.scale(2.5)
        unknown_numerator.move_to(frac[3][1])
        unknown_denominator = SingleStringMathTex("2", color=LIGHT_GREEN_COLOR)
        unknown_denominator.scale(2.5)
        unknown_denominator.move_to(frac[3][3])

        self.play(Write(frac), run_time=0.7)
        self.wait(1)
        self.play(
            Indicate(frac[0][2], color=LIGHT_RED_COLOR, scale_factor=1.2),
            Indicate(frac[2][2], color=LIGHT_RED_COLOR, scale_factor=1.2),
            run_time=1.5
        )
        self.wait(1)
        self.play(Transform(frac[3][3], unknown_denominator))
        self.wait(1)
        self.play(Transform(frac[3][1], unknown_numerator))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)