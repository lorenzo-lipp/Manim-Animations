from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FiveDivision(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        by_one = Division(5, 1)
        by_one.scale(1.4)
        by_two = Division(5, 2)
        by_two.scale(1.4)
        by_three = Division(5, 3)
        by_three.scale(1.4)
        by_four = Division(5, 4)
        by_four.scale(1.4)
        by_five = Division(5, 5)
        by_five.scale(1.4)
        divisions = VGroup(
            VGroup(
                by_one,
                by_two
            ).arrange(RIGHT, buff=1),
            VGroup(
                by_three,
                by_four,
            ).arrange(RIGHT, buff=1),
            by_five
        )
        divisions.arrange(DOWN, buff=1)

        self.play(LaggedStart(
            FadeIn(by_one), 
            FadeIn(by_two),
            FadeIn(by_three),
            FadeIn(by_four),
            FadeIn(by_five),
            lag_ratio=0.3, 
            run_time=1.5
        ))
        self.wait(1)
        self.play(LaggedStart(
            Circumscribe(by_one, color=LIGHT_RED_COLOR),
            Circumscribe(by_five, color=LIGHT_RED_COLOR),
            lag_ratio=0.5,
            run_time=2
        ))
        self.play(FadeOut(divisions), run_time=0.5)
        self.wait(0.5)