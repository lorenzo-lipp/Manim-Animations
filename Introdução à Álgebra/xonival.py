from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Xonival(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        label = Text("Xonival", color=DARK_PURPLE_COLOR)
        label.scale(1.5)
        operation_1 = MathOperation("./assets/Asset 2.png", "+ 5 = 15")
        operation_2 = MathOperation("./assets/x.png", "+ 5 = 15")
        operation_3 = MathOperation("./assets/ten.png", "+ 5 = 15")
        conclusion_1 = MathOperation("./assets/Asset 2.png", "= 10")
        conclusion_2 = MathOperation("./assets/x.png", "= 10")
        conclusion_1.scale(0.8)
        conclusion_2.scale(0.8)
        Group(
            label,
            operation_1,
            operation_2,
            operation_3,
            Group(conclusion_1, conclusion_2).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, buff=0.7)
        

        self.play(
            label.shift(9 * LEFT).animate.shift(9 * RIGHT), 
            operation_1.shift(9 * LEFT).animate.shift(9 * RIGHT)
        )
        self.wait(1)
        self.play(Transform(operation_1.copy(), operation_2))
        self.wait(1)
        self.play(Transform(operation_2.copy(), operation_3))
        self.wait(1)
        self.play(
            SpinInFromNothing(conclusion_1),
            SpinInFromNothing(conclusion_2)
        )
        self.wait(1.5)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)