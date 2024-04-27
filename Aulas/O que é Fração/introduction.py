from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Frações", color=LIGHT_RED_COLOR)
        title.scale(2.5)
        fractions = VGroup(
            MathTex(r"\frac{1}{2}", color=LIGHT_RED_COLOR)
                .shift(2 * LEFT + 3.5 * UP),
            MathTex(r"\frac{3}{4}", color=LIGHT_RED_COLOR)
                .shift(2 * RIGHT + 3.5 * UP),
            MathTex(r"\frac{1}{8}", color=LIGHT_RED_COLOR)
                .shift(2 * LEFT + 3.5 * DOWN),
            MathTex(r"\frac{7}{12}", color=LIGHT_RED_COLOR)
                .shift(2 * RIGHT + 3.5 * DOWN),
            MathTex(r"\frac{36}{84}", color=LIGHT_RED_COLOR)
                .shift(1.5 * DOWN),
            MathTex(r"\frac{4}{7}", color=LIGHT_RED_COLOR)
                .shift(1.5 * UP)
        )
        
        self.play(Write(title), run_time=0.8)
        self.play(
            LaggedStart(
                *[SpinInFromNothing(frac) for frac in fractions], 
                lag_ratio=0.2
            )
        )
        self.wait(0.5)
        self.play(
            Unwrite(fractions, reverse=True),
            Unwrite(title, reverse=True),
            run_time=1.6
        )