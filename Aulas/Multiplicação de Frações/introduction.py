from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Multiplicação", color=LIGHT_BLUE_COLOR).scale(2),
            Tex("de Frações", color=LIGHT_PURPLE_COLOR).scale(2),
        ).arrange(DOWN, buff=0.4)
        fraction_1 = MathTex(r"\frac{2}{5}", color=LIGHT_BLUE_COLOR)
        fraction_1.scale(1.8)
        fraction_1.shift(2.7 * DOWN + 2.5 * LEFT)
        fraction_2 = MathTex(r"\frac{3}{4}", color=LIGHT_BLUE_COLOR)
        fraction_2.scale(1.8)
        fraction_2.shift(2.7 * UP + 2.5 * RIGHT)
        fraction_3 = MathTex(r"\frac{6}{9}", color=LIGHT_PURPLE_COLOR)
        fraction_3.scale(1.8)
        fraction_3.shift(2.7 * UP + 2.5 * LEFT)
        fraction_4 = MathTex(r"\frac{1}{2}", color=LIGHT_PURPLE_COLOR)
        fraction_4.scale(1.8)
        fraction_4.shift(2.7 * DOWN + 2.5 * RIGHT)

        self.play(Write(title), run_time=0.7)
        self.play(LaggedStart(
            SpinInFromNothing(fraction_3),
            SpinInFromNothing(fraction_4),
            SpinInFromNothing(fraction_2),
            SpinInFromNothing(fraction_1),
            lag_ratio=0.18
        ))
        self.wait(0.5)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)