from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Polígonos", color=LIGHT_PINK)
        title.scale(3)

        self.play(SpinInFromNothing(title))
        self.wait(1.5)
        self.play(Transform(title, title.copy().shift(6 * LEFT).set_opacity(0)))
        self.remove(*self.mobjects)