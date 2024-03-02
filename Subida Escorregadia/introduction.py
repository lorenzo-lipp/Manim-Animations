from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Hora do", color=LIGHT_RED_COLOR).scale(2.5),
            Tex("Desafio", color=LIGHT_RED_COLOR).scale(2.5)
        ).arrange(DOWN, buff=0.5)
        hedgehog = Hedgehog()
        Group(title, hedgehog).arrange(DOWN, buff=1)

        self.play(Write(title), run_time=0.7)
        self.play(SpinInFromNothing(hedgehog), run_time=0.7)
        self.wait(1)
        self.play(
            FadeOut(title), 
            hedgehog.animate.move_to(ORIGIN),
            run_time=0.7
        )
        self.remove(*self.mobjects)