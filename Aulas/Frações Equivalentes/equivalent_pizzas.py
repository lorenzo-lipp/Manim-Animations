from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class EquivalentPizzas(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        one_half = VGroup(
            Pizza(),
            AnnularSector(1.4, 0, PI, 3 * PI/2, color=BACKGROUND_COLOR),
            DashedVMobject(Arc(1.3, 3 * PI/2, PI, color=DARK_RED_COLOR)),
            DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR), 10),
            VGroup(
                MathTex(r"\frac{1}{2}", color=BLACK),
                Tex("pizza", color=BLACK)
            ).arrange(RIGHT).shift(2 * DOWN)
        )
        three_out_of_six = VGroup(
            Pizza(),
            AnnularSector(1.4, 0, PI, 3 * PI/2, color=BACKGROUND_COLOR),
            DashedVMobject(Arc(1.3, 3 * PI/2, PI, color=DARK_RED_COLOR)),
            DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR), 10),
            DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR), 10)
                .rotate(PI / 3, about_point=ORIGIN),
            DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR), 10)
                .rotate(2 * PI / 3, about_point=ORIGIN),
            VGroup(
                MathTex(r"\frac{3}{6}", color=BLACK),
                Tex("pizza", color=BLACK)
            ).arrange(RIGHT).shift(2 * DOWN)
        )
        VGroup(one_half, three_out_of_six).arrange(RIGHT, buff=1)
        fractions = VGroup(
            MathTex(r"\frac{1}{2}", color=BLACK),
            MathTex("=", color=BLACK),
            MathTex(r"\frac{3}{6}", color=BLACK)
        )
        fractions.scale(2)
        fractions.arrange(RIGHT, buff=1)
        fractions.shift(2 * DOWN)

        self.play(LaggedStart(
            SpinInFromNothing(one_half),
            SpinInFromNothing(three_out_of_six),
            lag_ratio=0.5
        ))
        self.wait(2)
        self.play(Group(*self.mobjects).animate.shift(2 * UP), run_time=0.7)
        self.play(Write(fractions), run_time=0.5)
        self.wait(1.7)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)