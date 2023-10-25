from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class TenDivisors(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        by_one = Division(10, 1)
        by_one.scale(1.3)
        by_two = Division(10, 2)
        by_two.scale(1.3)
        by_three = Division(10, 3)
        by_three.scale(1.3)
        by_four = Division(10, 4)
        by_four.scale(1.3)
        by_five = Division(10, 5)
        by_five.scale(1.3)
        by_six = Division(10, 6)
        by_six.scale(1.3)
        by_seven = Division(10, 7)
        by_seven.scale(1.3)
        by_eight = Division(10, 8)
        by_eight.scale(1.3)
        by_nine = Division(10, 9)
        by_nine.scale(1.3)
        by_ten = Division(10, 10)
        by_ten.scale(1.3)
        divisions = VGroup(
            VGroup(
                by_one,
                by_two,
                by_three
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                by_four,
                by_five,
                by_six
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                by_seven,
                by_eight,
                by_nine
            ).arrange(RIGHT, buff=0.5),
            by_ten
        )
        divisions.arrange(DOWN, buff=1)
        square1 = SurroundingRectangle(by_one, color=LIGHT_RED_COLOR)
        square2 = SurroundingRectangle(by_two, color=LIGHT_RED_COLOR)
        square3 = SurroundingRectangle(by_five, color=LIGHT_RED_COLOR)
        square4 = SurroundingRectangle(by_ten, color=LIGHT_RED_COLOR)

        self.play(LaggedStart(
            FadeIn(by_one), 
            FadeIn(by_two),
            FadeIn(by_three),
            FadeIn(by_four),
            FadeIn(by_five),
            FadeIn(by_six),
            FadeIn(by_seven),
            FadeIn(by_eight),
            FadeIn(by_nine),
            FadeIn(by_ten),
            lag_ratio=0.3, 
            run_time=1.5
        ))
        self.wait(1)
        self.play(LaggedStart(
            Create(square1),
            Create(square2),
            Create(square3),
            Create(square4),
            lag_ratio=0.3,
            run_time=2.5
        ))
        self.wait(2)
        self.play(
            FadeOut(square1), 
            FadeOut(square2), 
            FadeOut(square3), 
            FadeOut(square4), 
            FadeOut(divisions), 
            run_time=0.5
        )
        self.wait(0.5)