from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class IntroducingUnits(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        table = UnitsTable()
        
        self.play(AnimateFromLeft(table))
        self.play(
            LaggedStart(
                *[Indicate(item, scale_factor=1.05, color=LIGHT_ORANGE_COLOR) for item in table],
                lag_ratio=0.8
            )
        )
        self.wait(0.5)
        self.remove(*self.mobjects)