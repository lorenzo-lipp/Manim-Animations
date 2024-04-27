from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class HowManyPrimes(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        text_1 = VGroup(
            Text("Existem infinitos", color=TEXT_COLOR),
            Text("números primos!", color=TEXT_COLOR)
        )
        text_1[0][7:].set(color=LIGHT_PURPLE_COLOR)
        text_1.scale(1.4)
        text_1.arrange(DOWN, buff=0.5)

        self.play(Write(text_1), run_time=0.7)
        self.wait(1)
        self.play(text_1.animate.scale(0), run_time=0.7)
        self.remove(*self.mobjects)