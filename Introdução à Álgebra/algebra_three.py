from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class AlgebraThree(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        operation_1 = MathOperation("./assets/Asset 3.png", "* 6 = 24")
        operation_2 = Tex(r"\textbf{a} * 6 = 24", color=BLACK)
        operation_2[0][0].set(color=ORANGE_COLOR)
        operation_2.scale(1.8)
        operation_3 = Tex(r"\textbf{4} * 6 = 24", color=BLACK)
        operation_3[0][0].set(color=ORANGE_COLOR)
        operation_3.scale(1.8)
        conclusion_1 = MathOperation("./assets/Asset 3.png", "= 4")
        conclusion_2 = Tex(r"\textbf{a} = 4", color=BLACK)
        conclusion_2[0][0].set(color=ORANGE_COLOR)
        conclusion_1.scale(0.8)
        conclusion_2.scale(1.8)
        Group(
            operation_1,
            operation_2,
            operation_3,
            Group(conclusion_1, conclusion_2).arrange(RIGHT, buff=0.5)
        ).arrange(DOWN, buff=0.7)
        

        self.play(operation_1.shift(9 * RIGHT).animate.shift(9 * LEFT), run_time=0.5)
        self.wait(1)
        self.play(Transform(operation_1[1].copy(), operation_2))
        self.wait(1)
        self.play(Transform(operation_2.copy(), operation_3))
        self.wait(1)
        self.play(
            SpinInFromNothing(conclusion_1),
            SpinInFromNothing(conclusion_2)
        )
        self.wait(2)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)