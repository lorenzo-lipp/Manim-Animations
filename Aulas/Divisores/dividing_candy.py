from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class DividingCandy(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        candy = ImageMobject("./assets/doces.png")
        candy.scale(0.6)
        text = Tex("10 doces", color=TEXT_COLOR)
        text.scale(2)
        text[0][2:].set(color=LIGHT_PURPLE_COLOR)
        group = Group(text, candy)
        group.arrange(DOWN, buff=1)

        self.play(SpinInFromNothing(group), run_time=0.7)
        self.wait(1)
        self.play(group.animate.shift(9 * LEFT), run_time=0.7)