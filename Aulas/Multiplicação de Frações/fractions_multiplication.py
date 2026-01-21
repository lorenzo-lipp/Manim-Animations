from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FractionsMultiplication(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        frac = MathTex(r"\frac{3}{4} \times \frac{2}{4} = \frac{6}{16}", color=BLACK)
        frac.scale(2)

        self.play(Write(frac[0][0:8]))
        self.wait(1)
        self.play(Indicate(frac[0][0], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac[0][3], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac[0][4], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Write(frac[0][8:10]))
        self.wait(2)
        self.play(Indicate(frac[0][2], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac[0][3], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac[0][6], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.wait(0.5)
        self.play(Write(frac[0][10:]))
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)