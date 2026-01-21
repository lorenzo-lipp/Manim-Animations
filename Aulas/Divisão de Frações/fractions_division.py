from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FractionsDivision(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        frac_1 = MathTex(r"\frac{2}{5} \div \frac{3}{2}", color=BLACK)
        frac_1.scale(2)
        frac_2 = MathTex(r"\frac{2}{5} \times \frac{2}{3} = \frac{4}{15}", color=BLACK)
        frac_2.scale(2)

        Group(frac_1, frac_2).arrange(DOWN, buff=1)

        self.play(Write(frac_1))
        self.wait(1.5)
        self.play(TransformFromCopy(frac_1[0][0:3], frac_2[0][0:3]))
        self.wait(2.5)
        self.play(TransformFromCopy(frac_1[0][3], frac_2[0][3]))
        self.wait(1)
        self.play(TransformFromCopy(frac_1[0][4], frac_2[0][6]))
        self.play(TransformFromCopy(frac_1[0][5], frac_2[0][5]))
        self.play(TransformFromCopy(frac_1[0][6], frac_2[0][4]))
        self.wait(0.5)
        self.play(Indicate(frac_2[0][0], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac_2[0][3], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac_2[0][4], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.wait(0.5)
        self.play(Write(frac_2[0][7:10]))
        self.wait(0.5)
        self.play(Indicate(frac_2[0][2], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac_2[0][3], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Indicate(frac_2[0][6], color=LIGHT_RED_COLOR, scale_factor=1.2))
        self.play(Write(frac_2[0][10:]))
        self.wait(2.5)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)