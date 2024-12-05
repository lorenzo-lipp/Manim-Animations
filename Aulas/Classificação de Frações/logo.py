from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Logo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        svg_symbol = SVGMobject(file_name="../assets/logo-simbolo.svg", stroke_color=TEXT_COLOR, height=5, fill_opacity=0.9)
        svg_symbol.shift(3 * UP)
        svg_text_1 = SVGMobject(file_name="../assets/logo-texto1.svg", height=1.1, fill_opacity=0.9)
        svg_text_1.shift(0.5 * DOWN)
        svg_text_2 = SVGMobject(file_name="../assets/logo-texto2.svg", height=1, fill_opacity=0.9)
        svg_text_2.shift(1.5 * DOWN)
        svg_text_3 = SVGMobject(file_name="../assets/logo-texto3.svg", height=0.7, fill_opacity=0.9)
        svg_text_3.shift(2.5 * DOWN)

        self.play(
            FadeIn(svg_symbol),
            FadeIn(svg_text_1),
            FadeIn(svg_text_2),
            FadeIn(svg_text_3), 
        )
        self.wait(1)
        self.play(
            FadeOut(svg_symbol), 
            FadeOut(svg_text_1), 
            FadeOut(svg_text_2), 
            FadeOut(svg_text_3), 
            run_time=0.7
        )