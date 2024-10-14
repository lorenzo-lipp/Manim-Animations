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
        wrong = MathTex(r"\neq", color=LIGHT_RED_COLOR)
        wrong.scale(2)

        self.play(FadeIn(left_girl, right_girl), run_time=0.7)
        self.play(AnimateFromLeft(candies), run_time=0.7)
        self.wait(0.7)
        self.play(candies[5].animate.shift(3.5 * UP + 4.5 * LEFT), run_time=0.7)
        self.play(candies[0].animate.shift(2 * UP + 3.5 * RIGHT), run_time=0.7)
        self.play(candies[1].animate.shift(1.5 * UP + 2.5 * RIGHT), run_time=0.7)
        self.play(candies[2].animate.shift(2 * UP + 1.5 * RIGHT), run_time=0.7)
        self.play(candies[4].animate.shift(4 * UP + 3.5 * LEFT), run_time=0.7)
        self.play(candies[3].animate.shift(4 * UP + 0.5 * RIGHT), run_time=0.7)
        self.wait(0.7)
        self.play(FadeIn(wrong), run_time=0.7)
        self.play(Indicate(wrong, scale_factor=1.5, color=LIGHT_RED_COLOR))
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)