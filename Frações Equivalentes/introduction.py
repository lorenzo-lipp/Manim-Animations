from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Frações", color=LIGHT_RED_COLOR).scale(2.5),
            Tex("Equivalentes", color=LIGHT_RED_COLOR).scale(2.5)
        ).arrange(DOWN)
        pizza = Pizza()
        cracker = SmallCracker()
        cracker.scale(1.2)
        Group(
            title, 
            Group(pizza, cracker).arrange(RIGHT, buff=1)
        ).arrange(DOWN, buff=1)

        self.play(Write(title), run_time=0.7)
        self.play(LaggedStart(
            SpinInFromNothing(pizza),
            SpinInFromNothing(cracker),
            lag_ratio=0.5
        ))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)