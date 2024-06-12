from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        left_girl = ImageMobject("./assets/001.png")
        right_girl = ImageMobject("./assets/002.png")
        candies = Group(
            ImageMobject("./assets/007.png"),
            ImageMobject("./assets/006.png"),
            ImageMobject("./assets/008.png"),
            ImageMobject("./assets/009.png"),
            ImageMobject("./assets/010.png"),
            ImageMobject("./assets/011.png"),
        )
        candies.arrange(RIGHT, buff=0.3)
        Group(
            Group(left_girl, right_girl).arrange(RIGHT, buff=3),
            Group(candies[0:3], candies[3:]).arrange(DOWN, buff=0)
        ).arrange(DOWN, buff=1)

        self.play(FadeIn(left_girl, right_girl))
        self.play(AnimateFromLeft(candies), run_time=0.7)
        self.wait(2)
        self.play(candies[5].animate.shift(4 * UP + 4.5 * LEFT))
        self.play(candies[0].animate.shift(2 * UP + 3.5 * RIGHT))
        self.play(candies[1].animate.shift(1.5 * UP + 2.5 * RIGHT))
        self.play(candies[2].animate.shift(2 * UP + 1.5 * RIGHT))
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)