from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class DivisionByOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        banana = ImageMobject("./assets/banana.png")
        bananas = Group(
            banana.copy()
                .shift(0.9 * RIGHT + 0.1 * UP)
                .rotate(45 * DEGREES),
            banana.copy()
                .shift(0.6 * RIGHT + 0.15 * DOWN)
                .rotate(20 * DEGREES),
            banana.copy()
                .shift(0.2 * RIGHT + 0.25 * DOWN),
            banana.copy()
                .shift(0.2 * LEFT + 0.25 * DOWN)
                .rotate(-25 * DEGREES),
            banana.copy()
                .shift(0.6 * LEFT + 0.05 * DOWN)
                .rotate(-45 * DEGREES),
            banana.copy()
                .shift(0.85 * LEFT + 0.25 * UP)
                .rotate(-70 * DEGREES)
        )
        bananas.scale(0.8)
        kids = Group(
            ImageMobject("./assets/crianca-1.png")
        )
        kids.scale(0.6)
        kids.arrange(DOWN, buff=0.7)
        Group(kids, bananas).arrange(RIGHT, buff=2)
        division = Division(6, 1)
        division.scale(1.8)
        division.next_to(bananas, UP, buff=2)
        division.shift(0.5 * RIGHT)

        self.play(
            FadeIn(bananas), 
            FadeIn(kids),
            FadeIn(division),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(bananas.animate.shift(1.5 * LEFT), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(*self.mobjects), run_time=0.5)