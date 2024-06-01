from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Relógio de", color=LIGHT_BLUE_COLOR),
            Tex("Ponteiros", color=LIGHT_BLUE_COLOR)
        ).arrange(DOWN, buff=0.1)
        title.scale(2.2)

        self.play(Write(title), run_time=0.7)
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)