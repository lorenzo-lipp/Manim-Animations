from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SubSameBase(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        frac = MathTex(
            r"\frac{3}{5} - \frac{2}{5} = \frac{?}{?}", 
            color=BLACK,
            tex_to_color_map={r"\frac{3}{5}": LIGHT_BLUE_COLOR, r"\frac{2}{5}": LIGHT_PURPLE_COLOR}
        )
        frac.scale(2.5)
        unknown_numerator = MatchingMathTex("1", frac[3][1], color=LIGHT_GREEN_COLOR)
        unknown_denominator = MatchingMathTex("5", frac[3][3], color=LIGHT_GREEN_COLOR)

        self.play(Write(frac), run_time=0.7)
        self.wait(1)
        self.play(
            Indicate(frac[0][2], color=LIGHT_RED_COLOR, scale_factor=1.2),
            Indicate(frac[2][2], color=LIGHT_RED_COLOR, scale_factor=1.2),
            run_time=1.5
        )
        self.wait(1)
        self.play(Transform(frac[3][3], unknown_denominator))
        self.play(
            LaggedStart(
                Indicate(frac[0][0], color=LIGHT_RED_COLOR, scale_factor=1.2),
                Indicate(frac[1][0], color=LIGHT_RED_COLOR, scale_factor=1.2),
                Indicate(frac[2][0], color=LIGHT_RED_COLOR, scale_factor=1.2),
                lag_ratio=0.5
            )
        )
        self.play(Transform(frac[3][1], unknown_numerator))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)