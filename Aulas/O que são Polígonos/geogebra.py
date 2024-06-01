from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Geogebra(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        group1 = GeogebraLink(title="Quebra-cabeça Geométrico", img="quebra-cabeca-geometrico", link="qcm-geometrico", scale=0.8)
        group2 = GeogebraLink(title="Peça Quebrada", img="peca-quebrada", link="qcm-quebrada", scale=0.8)

        self.play(group1.animate.shift(9 * LEFT), run_time=0.7)
        self.wait(2.5)
        self.play(
            group1.animate.shift(9 * LEFT),
            group2.animate.shift(9 * LEFT),
            run_time=0.7
        )
        self.wait(2.5)
        self.play(group2.animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)