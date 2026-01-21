from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Média Aritmética", color=LIGHT_ORANGE_COLOR).scale(2)

        self.play(Write(title), run_time=0.7)
        self.remove(*self.mobjects)