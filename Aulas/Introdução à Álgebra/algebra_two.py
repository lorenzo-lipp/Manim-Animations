from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class AlgebraTwo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        operation_1 = MonsterSum("./assets/Asset 4.png", 3, "= 15")
        operation_2 = Tex(r"\textbf{5} + \textbf{5} + \textbf{5} = 15", color=BLACK)
        operation_2[0][0:6:2].set(color=AQUA_BLUE_COLOR)
        operation_2.scale(1.8)
        conclusion_1 = MathOperation("./assets/Asset 4.png", "= 5")
        conclusion_1.scale(0.8)
        Group(
            operation_1,
            operation_2,
            conclusion_1
        ).arrange(DOWN, buff=0.7)
        

        self.play(operation_1.shift(9 * RIGHT).animate.shift(9 * LEFT), run_time=0.5)
        self.wait(2)
        self.play(Transform(operation_1[5].copy(), operation_2), run_time=0.7)
        self.wait(0.5)
        self.play(SpinInFromNothing(conclusion_1), run_time=0.7)
        self.wait(0.8)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)