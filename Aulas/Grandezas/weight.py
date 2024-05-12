from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Weight(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        balance = Balance()
        balance.scale(1.5)
        balance.shift(DOWN)
        tomato = Tomato()
        tomato.scale(0.65)
        tomato.shift(10 * UP)
        measurement_text = VGroup(
            Tex("Massa", color=LIGHT_RED_COLOR),
            Tex("(kilogramas ou gramas)", color=LIGHT_RED_COLOR)
        ).arrange(DOWN, buff=0.5)
        measurement_text[0].scale(2)
        measurement_text.next_to(balance, DOWN, buff=0.9)

        self.play(AnimateFromLeft(balance))
        self.wait(1)
        self.play(tomato.animate.shift(6.8 * DOWN))
        self.wait(0.2)
        self.play(
            balance[0:2].animate.shift(0.2 * DOWN),
            tomato.animate.shift(0.2 * DOWN),
            Rotate(balance[-2], -72 * PI / 180, about_point=balance[-1].get_center())
        )
        self.wait(1)
        self.play(Write(measurement_text))
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)