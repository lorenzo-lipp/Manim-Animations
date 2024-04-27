from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Geogebra(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        group1 = GeogebraLink(title="Palitos e Quadrados I", img="palitos-e-quadrados-i", link="qcm-quadrados1", scale=1)
        group2 = GeogebraLink(title="Palitos e Quadrados II", img="palitos-e-quadrados-i", link="qcm-quadrados2", scale=1)
        group3 = GeogebraLink(title="Oito Retângulos", img="oito-retangulos", link="qcm-retangulos")
        group4 = GeogebraLink(title="Palitos Coloridos", img="palitos-coloridos", link="qcm-coloridos")

        self.play(group1.animate.shift(9 * LEFT), run_time=0.7)
        self.wait(2)
        self.play(
            group1.animate.shift(9 * LEFT),
            group2.animate.shift(9 * LEFT),
            run_time=0.7
        )
        self.wait(2)
        self.play(
            group2.animate.shift(9 * LEFT),
            group3.animate.shift(9 * LEFT),
            run_time=0.7
        )
        self.wait(2)
        self.play(
            group3.animate.shift(9 * LEFT),
            group4.animate.shift(9 * LEFT),
            run_time=0.7
        )
        self.wait(2)
        self.play(group4.animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)