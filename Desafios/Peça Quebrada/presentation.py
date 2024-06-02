from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        triangle = Triangle(color=LIGHT_BLUE_COLOR, fill_opacity=1)
        rect_1 = Rectangle(height=triangle.height, width=triangle.width, color=LIGHT_BLUE_COLOR, fill_opacity=1)
        rect_2 = Rectangle(height=triangle.height, width=triangle.width, color=LIGHT_BLUE_COLOR, fill_opacity=1)
        parallelogram = VGroup(
            Triangle(color=LIGHT_BLUE_COLOR, fill_opacity=1),
            Triangle(color=LIGHT_BLUE_COLOR, fill_opacity=1)
                .rotate(180 * DEGREES)
                .shift(triangle.width * 0.5 * RIGHT)
        ).center()
        piece = Polygon(
            [0, 0, 0],
            [triangle.width * 2, 0, 0],
            [triangle.width * 2, triangle.height, 0],
            [triangle.width * 1.5, triangle.height * 2, 0],
            [triangle.width * 0.5, triangle.height * 2, 0],
            [0, triangle.height, 0],
            color=BLACK
        ).center()
        piece.shift(2 * DOWN)
        group = Group(
            Group(triangle, parallelogram)
                .arrange(RIGHT, buff=0.75),
            Group(rect_1, rect_2)
                .arrange(RIGHT, buff=0.75)
        ).arrange(DOWN, buff=0.75)
        group.shift(2.5 * UP + 0.45 * RIGHT)
        group[1].shift(0.45 * LEFT)

        self.play(AnimateFromLeft(piece))
        self.play(LaggedStart(
            SpinInFromNothing(triangle, run_time=0.7),
            SpinInFromNothing(parallelogram, run_time=0.7),
            SpinInFromNothing(rect_1, run_time=0.7),
            SpinInFromNothing(rect_2, run_time=0.7), 
            lag_ratio=0.6
        ))
        self.remove(piece)
        self.add(piece)
        self.play(rect_2.animate.next_to(piece, direction=ORIGIN, aligned_edge=UP, buff=0))
        self.wait(0.5)
        self.play(rect_2.animate.next_to(piece, direction=ORIGIN, aligned_edge=DR, buff=0))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)