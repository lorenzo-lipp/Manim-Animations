from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SixDivision(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        by_one = Division(6, 1)
        by_one.scale(1.4)
        by_two = Division(6, 2)
        by_two.scale(1.4)
        by_three = Division(6, 3)
        by_three.scale(1.4)
        by_four = Division(6, 4)
        by_four.scale(1.4)
        by_five = Division(6, 5)
        by_five.scale(1.4)
        by_six = Division(6, 6)
        by_six.scale(1.4)
        divisions = VGroup(
            VGroup(
                by_one,
                by_two
            ).arrange(RIGHT, buff=1),
            VGroup(
                by_three,
                by_four
            ).arrange(RIGHT, buff=1),
            VGroup(
                by_five,
                by_six
            ).arrange(RIGHT, buff=1)
        )
        divisions.arrange(DOWN, buff=1)

        self.play(LaggedStart(
            FadeIn(by_one), 
            FadeIn(by_two),
            FadeIn(by_three),
            FadeIn(by_four),
            FadeIn(by_five),
            FadeIn(by_six),
            lag_ratio=0.3, 
            run_time=1.5
        ))
        self.wait(1)
        self.play(LaggedStart(
            Circumscribe(by_one, color=LIGHT_RED_COLOR),
            Circumscribe(by_two, color=LIGHT_RED_COLOR),
            Circumscribe(by_three, color=LIGHT_RED_COLOR),
            Circumscribe(by_six, color=LIGHT_RED_COLOR),
            lag_ratio=0.3,
            run_time=2.5
        ))
        self.play(FadeOut(divisions), run_time=0.5)
        self.wait(0.5)