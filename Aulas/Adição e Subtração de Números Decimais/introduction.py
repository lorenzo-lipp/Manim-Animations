from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Adição e Subtração", color=LIGHT_PURPLE_COLOR).scale(1.8),
            Tex("de Números Decimais", color=LIGHT_PURPLE_COLOR).scale(1.8),
        ).arrange(DOWN, buff=0.4)
        plus_sign = MathTex("+", color=LIGHT_BLUE_COLOR)
        plus_sign.scale(2.5)
        plus_sign.shift(1.8 * DOWN + 1.8 * LEFT)
        minus_sign = MathTex("-", color=LIGHT_BLUE_COLOR)
        minus_sign.scale(2.5)
        minus_sign.shift(1.8 * DOWN + 1.8 * RIGHT)

        self.play(Write(title), run_time=0.7)
        self.wait(0.3)
        self.play(title.animate.shift(UP), run_time=0.7)
        self.play(LaggedStart(
            SpinInFromNothing(plus_sign),
            SpinInFromNothing(minus_sign),
            lag_ratio=0.5,
            run_time=1.2
        ))
        self.wait(0.3)
        self.play(LaggedStart(
            Indicate(plus_sign, color=LIGHT_RED_COLOR, run_time=0.9),
            Indicate(minus_sign, color=LIGHT_RED_COLOR, run_time=0.9),
            lag_ratio=0.5,
        ))
        self.wait(0.3)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)