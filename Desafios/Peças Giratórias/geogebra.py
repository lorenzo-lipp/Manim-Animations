from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Geogebra(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        text1 = Tex(r"\textbf{Peças Giratórias I}", color=DARK_BLUE_COLOR)
        text1.scale(1.2)
        img1 = ImageMobject("./assets/pecas-giratorias-i.png")
        img1.scale(1.5)
        link1 = Tex(r"\textbf{Link: bit.ly/qcm-pecas1}", color=DARK_BLUE_COLOR)
        text2 = Tex(r"\textbf{Peças Giratórias II}", color=DARK_BLUE_COLOR)
        text2.scale(1.2)
        img2 = ImageMobject("./assets/pecas-giratorias-ii.png")
        img2.scale(1.4)
        link2 = Tex(r"\textbf{Link: bit.ly/qcm-pecas2}", color=DARK_BLUE_COLOR)
        group1 = Group(text1, img1, link1)
        group1.arrange(DOWN, buff=0.5)
        group1.shift(9 * RIGHT)
        group2 = Group(text2, img2, link2)
        group2.arrange(DOWN, buff=0.5)
        group2.shift(9 * RIGHT)

        self.play(group1.animate.shift(9 * LEFT), run_time=0.7)
        self.wait(2)
        self.play(
            group1.animate.shift(9 * LEFT),
            group2.animate.shift(9 * LEFT),
            run_time=0.7
        )
        self.wait(2)
        self.play(group2.animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)