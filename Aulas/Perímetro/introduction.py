from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            VGroup(
                Rectangle(LIGHT_GREEN_COLOR, 4, 5.5, fill_opacity=1),
                Rectangle(LIGHT_PURPLE_COLOR, 0.3, 5.5, fill_opacity=1),
                Rectangle(LIGHT_ORANGE_COLOR, 0.3, 5.5, fill_opacity=1),
                Rectangle(LIGHT_BLUE_COLOR, 0.3, 5.5, fill_opacity=1)
            ).arrange(DOWN, buff=0),
            Tex("Perímetro", color=WHITE)
                .scale(2.2)
        )

        self.play(AnimateFromLeft(title))
        self.wait(2)
        self.play(AnimateToLeft(title).fade(0.2))
        self.remove(*self.mobjects)