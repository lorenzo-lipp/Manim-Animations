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
        square1 = SurroundingRectangle(by_one, color=LIGHT_RED_COLOR)
        square2 = SurroundingRectangle(by_five, color=LIGHT_RED_COLOR)

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
            Create(square1),
            Create(square2),
            lag_ratio=0.3,
            run_time=1.5
        ))
        self.wait(2)
        self.play(
            FadeOut(square1), 
            FadeOut(square2), 
            FadeOut(divisions), 
            run_time=0.5
        )
        self.wait(0.5)