from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        animals_1 = Group(
            ImageMobject("./assets/Asset 1.png")
                .scale(0.4),
            ImageMobject("./assets/Asset 2.png")
                .scale(0.4)
        )
        animals_1.arrange(RIGHT, buff=1)
        text = VGroup(
            Tex("Números", color="#a346eb")
                .scale(3),
            Tex("Primos", color="#a346eb")
                .scale(3)
        )
        text.arrange(DOWN, buff=0.7)
        animals_2 = Group(
            ImageMobject("./assets/Asset 3.png")
                .scale(0.4),
            ImageMobject("./assets/Asset 4.png")
                .scale(0.4)
        )
        animals_2.arrange(RIGHT, buff=1)
        Group(animals_1, text, animals_2).arrange(DOWN, buff=1)

        self.play(
            Transform(animals_1[0].copy().scale(0), animals_1[0]),
            Transform(animals_1[1].copy().scale(0), animals_1[1]),
            Transform(animals_2[0].copy().scale(0), animals_2[0]),
            Transform(animals_2[1].copy().scale(0), animals_2[1]),
            Write(text)
        )
        self.wait(1)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.7)