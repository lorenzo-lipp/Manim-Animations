from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Geogebra(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        group1 = GeogebraLink(title="Perímetro", img="perimetro", link="qcm-perimetro", scale=1)

        self.play(group1.animate.shift(9 * LEFT), run_time=0.7)
        self.wait(4)
        self.play(group1.animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)