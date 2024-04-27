from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Geogebra(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        group1 = GeogebraLink(title="Palitos e Triângulos I", img="palitos-e-triangulos-i", link="qcm-triangulos1", scale=1)
        group2 = GeogebraLink(title="Palitos e Triângulos II", img="palitos-e-triangulos-ii", link="qcm-triangulos2", scale=1)
        group3 = GeogebraLink(title="Copiando Formas", img="copiando-formas", link="qcm-formas")

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
        self.play(group3.animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)