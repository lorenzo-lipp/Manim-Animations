from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Mean(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Média Aritmética", color=LIGHT_ORANGE_COLOR).scale(2)
        num_1 = MathTex("7", color=LIGHT_ORANGE_COLOR)
        num_1.scale(1.8)
        num_1.shift(2.7 * DOWN + 2.5 * LEFT)
        num_2 = MathTex("12", color=LIGHT_ORANGE_COLOR)
        num_2.scale(1.8)
        num_2.shift(2.7 * UP + 2.5 * RIGHT)
        num_3 = MathTex("10", color=LIGHT_ORANGE_COLOR)
        num_3.scale(1.8)
        num_3.shift(2.7 * UP + 2.5 * LEFT)
        num_4 = MathTex("11", color=LIGHT_ORANGE_COLOR)
        num_4.scale(1.8)
        num_4.shift(2.7 * DOWN + 2.5 * RIGHT)
        num_5 = MathTex("10", color=LIGHT_ORANGE_COLOR)
        num_5.scale(1.8)

        self.add(title)
        self.wait(1)
        self.play(LaggedStart(
            FadeOut(title),
            SpinInFromNothing(num_3),
            SpinInFromNothing(num_4),
            SpinInFromNothing(num_2),
            SpinInFromNothing(num_1),
            SpinInFromNothing(num_5),
            lag_ratio=0.18
        ))
        self.wait(1)

        result_sum = MathTex(r"{{10}}\,+\,{{12}}\,+\,{{10}}\,+\,{{7}}\,+\,{{11}}\,=\,{{50}}", color=LIGHT_ORANGE_COLOR)
        result_sum[-1].scale(1.8)
        result_mean = MathTex(r"\text{Média } = \frac{50}{5} = 10", color=LIGHT_ORANGE_COLOR)
        result_mean.scale(1.8)
        Group(result_sum, result_mean).arrange(DOWN, buff=1)

        for [i, num] in enumerate([num_3, num_2, num_5, num_1, num_4]):
            self.play(LaggedStart(
                num.animate(run_time=0.7).move_to(result_sum[2 * i]),
                Write(result_sum[2 * i + 1], run_time=0.7),
                lag_ratio=0.3
            ))

        self.wait(0.5)
        self.play(Write(result_sum[-1]))
        self.wait(0.5)
        self.play(Write(result_mean[0][0:7]))
        self.wait(0.5)
        self.play(LaggedStart(
                TransformFromCopy(result_sum[-1], result_mean[0][7:9]),
                Write(result_mean[0][9], run_time=0.7),
                lag_ratio=0.8
        ))
        self.wait(0.5)

        for num in [num_3, num_2, num_5, num_1, num_4]:
            self.play(Indicate(num, color=LIGHT_BLUE_COLOR, scale_factor=1.1, run_time=0.7))

        self.wait(0.5)
        self.play(Write(result_mean[0][10], run_time=0.7))
        self.wait(1)
        self.play(Write(result_mean[0][11:]))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)