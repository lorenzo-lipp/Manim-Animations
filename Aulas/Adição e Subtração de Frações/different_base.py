from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class DifferentBase(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        frac = MathTex(
            r"\frac{3}{4} + \frac{1}{10} = \frac{?}{?}", 
            color=BLACK,
            tex_to_color_map={r"\frac{3}{4}": LIGHT_BLUE_COLOR, r"\frac{1}{10}": LIGHT_PURPLE_COLOR}
        )
        frac.scale(2.5)

        self.play(Write(frac), run_time=0.7)
        self.wait(1)
        self.play(
            LaggedStart(
                Indicate(frac[0][2], color=LIGHT_RED_COLOR, scale_factor=1.2),
                Indicate(frac[2][2:4], color=LIGHT_RED_COLOR, scale_factor=1.2),
                run_time=1.5,
                lag_ratio=0.5
            )
        )
        self.wait(1)
        self.play(Group(*self.mobjects).animate.shift(2 * UP))

        mcm = VGroup(
            MathTex(r"4,\,10\,\,|\,\,2", color=BLACK).scale(1.5),
            MathTex(r"2,\,\,5\,\,|\,\,2", color=BLACK).scale(1.5),
            MathTex(r"1,\,\,5\,\,|\,\,5", color=BLACK).scale(1.5),
            MathTex(r"1,\,\,1\,\,|\,\,a", color=BLACK, tex_to_color_map={"a": BACKGROUND_COLOR}).scale(1.5),
        )
        mcm.arrange(DOWN, buff=0.2)
        mcm.shift(2 * DOWN + 1.5 * LEFT)
        mcm_result = MathTex(r"2.2.5=20", color=BLACK)
        mcm_result.scale(1.5)
        mcm_result.shift(2 * DOWN + 2 * RIGHT)

        for line in mcm: self.play(Write(line))
        self.play(TransformFromCopy(mcm[0][0][-1], mcm_result[0][0]))
        self.play(TransformFromCopy(mcm[1][0][-1], mcm_result[0][2]))
        self.play(TransformFromCopy(mcm[2][0][-1], mcm_result[0][4]))
        self.play(*[Write(mcm_result[0][i]) for i in range(1, len(mcm_result[0])) if i not in [0, 2, 4]])
        self.wait(1)
        self.play(
            LaggedStart(
                FadeOut(mcm, mcm_result),
                frac.animate.shift(2 * DOWN), 
                lag_ratio=0.5
            )
        )

        mult_first = Tex(r"x5", color=LIGHT_RED_COLOR, stroke_width=1)
        mult_first.move_to(frac[0][0], UR)
        mult_first.shift(0.5 * RIGHT + 0.2 * UP)
        mult_first.scale(0.8)
        div_first = Tex(r"x5", color=LIGHT_RED_COLOR, stroke_width=1)
        div_first.move_to(frac[0][2], UR)
        div_first.shift(0.5 * RIGHT + 0.2 * UP)
        div_first.scale(0.8)
        mult_second = Tex(r"x2", color=LIGHT_RED_COLOR, stroke_width=1)
        mult_second.move_to(frac[2][0], UR)
        mult_second.shift(0.5 * RIGHT + 0.2 * UP)
        mult_second.scale(0.8)
        div_second = Tex(r"x2", color=LIGHT_RED_COLOR, stroke_width=1)
        div_second.move_to(frac[2][3], UR)
        div_second.shift(0.5 * RIGHT + 0.2 * UP)
        div_second.scale(0.8)

        self.play(FadeIn(Group(mult_first, div_first), run_time=0.5))
        self.play(
            Indicate(mult_first, color=LIGHT_RED_COLOR, scale_factor=1.2),
            Indicate(div_first, color=LIGHT_RED_COLOR, scale_factor=1.2),
        )
        self.play(
            FadeOut(Group(mult_first, div_first), run_time=0.6),
            Transform(frac[0][0], MatchingMathTex(r"15", frac[0][0], color=LIGHT_BLUE_COLOR)),
            Transform(frac[0][2], MatchingMathTex(r"20", frac[0][2], color=LIGHT_BLUE_COLOR))
        )
        self.wait(1)
        self.play(FadeIn(Group(mult_second, div_second), run_time=0.5))
        self.play(
            Indicate(mult_second, color=LIGHT_RED_COLOR, scale_factor=1.2),
            Indicate(div_second, color=LIGHT_RED_COLOR, scale_factor=1.2),
        )
        self.play(
            FadeOut(Group(mult_second, div_second), run_time=0.6),
            Transform(frac[2][0], MatchingMathTex(r"2", frac[2][0], color=LIGHT_PURPLE_COLOR)),
            Transform(frac[2][2:4], MatchingMathTex(r"20", frac[2][2:4], color=LIGHT_PURPLE_COLOR))
        )
        self.wait(1)
        self.play(Transform(frac[3][3], MatchingMathTex("20", frac[3][3], color=LIGHT_GREEN_COLOR)))
        self.wait(1)
        self.play(Transform(frac[3][1], MatchingMathTex("17", frac[3][1], color=LIGHT_GREEN_COLOR)))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)