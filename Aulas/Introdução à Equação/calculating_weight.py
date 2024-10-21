from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class CalculatingWeight(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        lemon = Lemon()
        lemon.scale(0.45)
        apple = Apple()
        apple.scale(0.45)
        equation = Group(
            apple,
            Tex("=", color=LIGHT_RED_COLOR).scale(2),
            lemon,
            Tex("+", color=LIGHT_RED_COLOR).scale(2),
            lemon.copy()
        ).arrange(RIGHT, buff=0.5)
        grams_1 = Tex("100g", color=LIGHT_ORANGE_COLOR)
        grams_1.scale(2)
        grams_1.move_to(equation[2])
        grams_2 = Tex("100g", color=LIGHT_ORANGE_COLOR)
        grams_2.scale(2)
        grams_2.move_to(equation[4])
        result = Group(
            apple.copy(),
            Tex("=", color=LIGHT_RED_COLOR).scale(2),
            Tex("200g", color=LIGHT_ORANGE_COLOR).scale(2)
        ).arrange(RIGHT, buff=0.5)

        self.play(FadeIn(equation))
        self.wait(2.5)
        self.play(
            equation[2].animate.set_opacity(0),
            FadeIn(grams_1),
            equation[4].animate.set_opacity(0),
            FadeIn(grams_2),
        )
        self.wait(2.5)
        self.play(
            FadeOut(equation[2:]),
            FadeOut(grams_1),
            FadeOut(grams_2),
            FadeIn(result[2:]),
            Transform(equation[0], result[0]),
            Transform(equation[1], result[1])
        )
        self.wait(1.5)
        self.play(FadeOut(Group(*self.mobjects)))
        self.remove(*self.mobjects)