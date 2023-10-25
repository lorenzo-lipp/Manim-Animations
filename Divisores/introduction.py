from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
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
        text = Tex("Divisores", color=AQUA_GREEN_COLOR)
        text.scale(3)
        Group(text, bananas).arrange(DOWN, buff=0.8)
        bananas.shift(0.3 * LEFT)

        self.play(Write(text))
        self.play(FadeIn(bananas[0]), run_time=0.5)
        self.play(Transform(bananas[0].copy(), bananas[1].copy()), run_time=0.3)
        self.play(Transform(bananas[1].copy(), bananas[2].copy()), run_time=0.3)
        self.play(Transform(bananas[2].copy(), bananas[3].copy()), run_time=0.3)
        self.play(Transform(bananas[3].copy(), bananas[4].copy()), run_time=0.3)
        self.play(Transform(bananas[4].copy(), bananas[5].copy()), run_time=0.3)
        self.play(Group(*self.mobjects).animate.scale(0))
