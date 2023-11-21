from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class EquivalentFractions(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        fractions = VGroup(
            MathTex(r"\frac{1}{2}", color=TEXT_COLOR),
            MathTex("=", color=TEXT_COLOR),
            MathTex(r"\frac{3}{6}", color=TEXT_COLOR)
        ).scale(2).arrange(RIGHT, buff=1)

        self.play(Write(fractions), run_time=0.5)
        self.wait(1)
        self.play(fractions.animate.scale(0), run_time=0.5)
        self.remove(*self.mobjects)