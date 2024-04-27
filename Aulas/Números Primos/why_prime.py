from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class WhyPrime(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        numbers = VGroup(
            Tex("2 é primo", color=LIGHT_RED_COLOR),
            Tex("3 é primo", color=LIGHT_RED_COLOR),
            Tex("4 = 2 x 2", color=LIGHT_BLUE_COLOR),
            Tex("5 é primo", color=LIGHT_RED_COLOR),
            Tex("6 = 2 x 3", color=LIGHT_BLUE_COLOR),
            Tex("7 é primo", color=LIGHT_RED_COLOR),
            Tex("8 = 2 x 2 x 2", color=LIGHT_BLUE_COLOR),
            Tex("9 = 3 x 3", color=LIGHT_BLUE_COLOR),
            Tex("10 = 2 x 5", color=LIGHT_BLUE_COLOR),
            Tex("11 é primo", color=LIGHT_RED_COLOR)
        )
        numbers.scale(1.5)
        numbers.arrange(DOWN, buff=0.7)

        self.play(Write(numbers), run_time=3)
        self.wait(2)
        self.play(Unwrite(numbers, reverse=False))