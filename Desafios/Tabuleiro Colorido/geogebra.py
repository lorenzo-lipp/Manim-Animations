from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Geogebra(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        group1 = GeogebraLink(title="Tabuleiro Colorido I", img="tabuleiro-colorido-i", link="qcm-tabuleiro1", scale=0.8)
        group2 = GeogebraLink(title="Tabuleiro Colorido II", img="tabuleiro-colorido-ii", link="qcm-tabuleiro2", scale=0.8)

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