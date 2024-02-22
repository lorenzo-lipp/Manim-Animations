from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class AlgebraWithLetters(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        operation_1 = LetterOperation("x + 3 = 5", "x = 2")
        operation_2 = LetterOperation("9 - d = 2", "d = 7")
        operation_3 = LetterOperation(r"2\times k = 6", "k = 3")
        Group(
            operation_1, 
            operation_2, 
            operation_3
        ).arrange(DOWN, buff=1)
        
        self.play(SpinInFromNothing(operation_1), run_time=0.7)
        self.play(SpinInFromNothing(operation_2), run_time=0.7)
        self.play(SpinInFromNothing(operation_3), run_time=0.7)
        self.wait(2)
        self.play(operation_1[1][1].animate.set(color=TEXT_COLOR), run_time=0.5)        
        self.wait(2)
        self.play(operation_2[1][1].animate.set(color=TEXT_COLOR), run_time=0.5)
        self.wait(2)
        self.play(operation_3[1][1].animate.set(color=TEXT_COLOR), run_time=0.5)
        self.wait(2)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)