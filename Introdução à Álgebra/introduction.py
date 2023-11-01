from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Introdução à", color=LIGHT_BLUE_COLOR),
            Tex("Álgebra", color=LIGHT_BLUE_COLOR)
        ).arrange(DOWN, buff=0.1)
        title.scale(2.2)
        monster1 = ImageMobject("./assets/Asset 1.png")
        monster2 = ImageMobject("./assets/Asset 2.png")
        monster3 = ImageMobject("./assets/Asset 3.png")
        monster4 = ImageMobject("./assets/Asset 4.png")
        Group(
            Group(monster1, monster2).arrange(RIGHT, buff=2),
            title,
            Group(monster3, monster4).arrange(RIGHT, buff=2)
        ).arrange(DOWN, buff=0.5)

        self.play(Write(title), run_time=0.7)
        self.play(
            LaggedStart(
                SpinInFromNothing(monster1),
                SpinInFromNothing(monster2),
                SpinInFromNothing(monster3),
                SpinInFromNothing(monster4),
                lag_ratio=0.15
            )
        )
        self.wait(0.6)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)