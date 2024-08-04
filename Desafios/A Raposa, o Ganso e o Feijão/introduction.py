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

        self.play(SpinInFromNothing(title, run_time=0.7))
        self.wait(1)
        self.play(AnimateToLeft(title), run_time=0.7)
        self.remove(*self.mobjects)