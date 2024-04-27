from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Symbols(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        operation = MathTex("? + 3 = 9", color=BLACK)
        operation.scale(3)
        
        self.play(Write(operation), run_time=0.7)
        self.wait(0.5)
        self.play(Transform(operation, MathTex(r"\star + 3 = 9", color=BLACK).scale(3)), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(operation, MathTex(r"a + 3 = 9", color=BLACK).scale(3)), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(operation, MathTex(r"b + 3 = 9", color=BLACK).scale(3)), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(operation, MathTex(r"c + 3 = 9", color=BLACK).scale(3)), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(operation, MathTex(r"x + 3 = 9", color=BLACK).scale(3)), run_time=0.5)
        self.wait(1.5)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)