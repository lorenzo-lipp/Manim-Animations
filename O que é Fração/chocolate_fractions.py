from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ChocolateFractions(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("1 de um total de 12 pedaços", color=LIGHT_RED_COLOR)
        title.scale(1.3)
        frac = MathTex(r"\frac{1}{12}", color=LIGHT_RED_COLOR)
        frac.scale(1.8)
        chocolate_row = VGroup(
            ChocolateSquare(),
            ChocolateSquare(),
            ChocolateSquare(),
        )
        chocolate_row.arrange(RIGHT, buff=0)
        chocolate_bar = VGroup(
            chocolate_row.copy(),
            chocolate_row.copy(),
            chocolate_row.copy(),
            chocolate_row.copy(),
        )
        chocolate_bar.arrange(DOWN, buff=0)
        Group(title, chocolate_bar, frac).arrange(DOWN, buff=0.5)
        chocolate_bar.shift(9 * RIGHT)

        self.play(chocolate_bar.animate.shift(9 * LEFT))
        self.play(
            LaggedStart(
                Write(title.shift(0.3 * UP)), 
                chocolate_bar[0][0].animate.shift((LEFT + UP) / 2),
                lag_ratio=0.2,
                run_time=1.8
            )
        )
        self.play(Write(frac), run_time=0.7)
        self.play(
            chocolate_bar[2][2].animate.shift(RIGHT * 1.5),
            chocolate_bar[0][0].animate.shift((RIGHT + DOWN) / 2),
            run_time=0.8
        )
        self.wait(0.5)
        self.play(chocolate_bar[2][2].animate.shift(LEFT * 1.5), run_time=0.5)
        self.play(Group(*self.mobjects).animate.scale(0), run_time=0.7)
        self.remove(*self.mobjects)