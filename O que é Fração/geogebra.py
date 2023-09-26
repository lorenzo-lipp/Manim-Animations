from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Geogebra(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        text1 = Tex(r"\textbf{Labirinto}", color=DARK_BLUE_COLOR)
        text1.scale(1.2)
        img1 = ImageMobject("./assets/labirinto.png")
        img1.scale(1.5)
        link1 = Tex(r"\textbf{Link: bit.ly/qcm-labirinto}", color=DARK_BLUE_COLOR)
        text2 = Tex(r"\textbf{Dominó das Frações}", color=DARK_BLUE_COLOR)
        text2.scale(1.2)
        img2 = ImageMobject("./assets/dominó.png")
        img2.scale(1.5)
        link2 = Tex(r"\textbf{Link: bit.ly/qcm-domino}", color=DARK_BLUE_COLOR)
        group1 = Group(text1, img1, link1)
        group1.arrange(DOWN, buff=0.5)
        group1.shift(9 * RIGHT)
        group2 = Group(text2, img2, link2)
        group2.arrange(DOWN, buff=0.5)
        group2.shift(9 * RIGHT)

        self.play(group1.animate.shift(9 * LEFT), run_time=0.7)
        self.wait(2.45)
        self.play(
            group1.animate.shift(9 * LEFT),
            group2.animate.shift(9 * LEFT),
            run_time=0.7
        )
        self.wait(2.45)
        self.play(group2.animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)