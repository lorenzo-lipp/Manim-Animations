from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class DivisionByThree(Scene):
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
            ImageMobject("./assets/crianca-1.png"),
            ImageMobject("./assets/crianca-2.png"),
            ImageMobject("./assets/crianca-3.png")
        )
        kids.scale(0.6)
        kids.arrange(DOWN, buff=0.7)
        Group(kids, bananas).arrange(RIGHT, buff=2)
        division = Division(6, 3)
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
        self.play(
            LaggedStart(
                Transform(bananas[5], banana.copy().scale(0.8).next_to(kids[0], buff=1)),
                Transform(bananas[4], banana.copy().scale(0.8).next_to(kids[0], buff=2)),
                Transform(bananas[3], banana.copy().scale(0.8).next_to(kids[1], buff=1)),
                Transform(bananas[2], banana.copy().scale(0.8).next_to(kids[1], buff=2)),
                Transform(bananas[1], banana.copy().scale(0.8).next_to(kids[2], buff=1)),
                Transform(bananas[0], banana.copy().scale(0.8).next_to(kids[2], buff=2)),
                run_time=2.5,
                lag_ratio=0.5
            )
        )
        self.wait(0.8)
        self.play(FadeOut(*self.mobjects), run_time=0.5)