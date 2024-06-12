from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        square = VGroup(
            Square(6, color=WHITE, stroke_color="#9e8a7d", stroke_width=10, fill_opacity=1),
            Line(3 * LEFT + UP, 3 * RIGHT + UP, color="#9e8a7d", stroke_width=10),
            Line(3 * LEFT + DOWN, 3 * RIGHT + DOWN, color="#9e8a7d", stroke_width=10),
            Line(LEFT + 3 * UP, LEFT + 3 * DOWN, color="#9e8a7d", stroke_width=10),
            Line(RIGHT + 3 * UP, RIGHT + 3 * DOWN, color="#9e8a7d", stroke_width=10),
        )
        text_1 = Text("I N Í C I O", color=LIGHT_BLUE_COLOR)
        text_1.next_to(square, DOWN)
        text_2 = Text("F I M", color=LIGHT_ORANGE_COLOR)
        text_2.next_to(square, UP)
        pieces = VGroup(
            VGroup(
                Polygon(
                    [-0.8, -0.7, 0],
                    [0.8, -0.7, 0],
                    [0, 0.7, 0],
                    [-0.8, -0.7, 0],
                    color=LIGHT_GRAY_COLOR,
                    fill_opacity=1
                ),
                Polygon(
                    [-0.8, -0.7, 0],
                    [0.8, -0.7, 0],
                    [0.8 / 3, 0.7 - (0.8 / 3) * 1.75, 0],
                    [0, 0.7 - (0.8 / 3) * 2 * 1.75, 0],
                    [2 * -0.8 / 3, 0.7 - (0.8 / 3) * 2 * 1.75, 0],
                    [-0.8, -0.7, 0],
                    color=LIGHT_BLUE_COLOR,
                    fill_opacity=1
                )
            ).shift(2 * UP + 2 * LEFT),
            VGroup(
                Circle(0.7, color=LIGHT_GRAY_COLOR, fill_opacity=1),
                Sector(0.7, 0, color=LIGHT_GREEN_COLOR, fill_opacity=1, angle=3 * PI / 2),
                Line(0.6 * LEFT, 0.7 * RIGHT, color=LIGHT_GRAY_COLOR),
                Line(0.6 * UP, 0.7 * DOWN, color=LIGHT_GRAY_COLOR),
                Sector(0.6, 0.52, color=LIGHT_YELLOW_COLOR, fill_opacity=1, angle=3 * PI / 2)
            ).shift(2 * UP),
            VGroup(
                Circle(0.4, color=LIGHT_GRAY_COLOR, fill_opacity=1).shift(0.3 * UP + 0.35 * LEFT),
                Circle(0.4, color=LIGHT_RED_COLOR, fill_opacity=1).shift(0.3 * UP + 0.35 * RIGHT),
                Polygon(
                    [0, 0.5, 0],
                    [0, -0.7, 0],
                    [0.65, 0, 0],
                    [0, 0.5, 0],
                    color=LIGHT_RED_COLOR,
                    stroke_width=0,
                    fill_opacity=1
                ),
                Polygon(
                    [0, 0.5, 0],
                    [0, -0.7, 0],
                    [-0.65, 0, 0],
                    [0, 0.5, 0],
                    color=LIGHT_GRAY_COLOR,
                    stroke_width=0,
                    fill_opacity=1
                ),
            ).shift(2 * UP + 2 * RIGHT),
            VGroup(
                Polygon(
                    [-0.7, -0.4, 0],
                    [-0.4, -0.7, 0],
                    [0.7, 0.4, 0],
                    [0.4, 0.7, 0],
                    [-0.7, -0.4, 0],
                    color=LIGHT_GRAY_COLOR,
                    fill_opacity=1
                ),
                Polygon(
                    [-0.55, -0.55, 0],
                    [-0.4, -0.7, 0],
                    [0.7, 0.4, 0],
                    [0.55, 0.55, 0],
                    [-0.55, -0.55, 0],
                    color=BROWN_COLOR,
                    fill_opacity=1
                ),
            ).shift(2 * LEFT),
            VGroup(
                Polygon(
                    [-0.4, 0.7, 0],
                    [0.4, 0.7, 0],
                    [0.81, 0, 0],
                    [0.4, -0.7, 0],
                    [-0.4, -0.7, 0],
                    [-0.81, 0, 0],
                    [-0.4, 0.7, 0],
                    color=LIGHT_GRAY_COLOR,
                    stroke_width=0,
                    fill_opacity=1
                ),
                Polygon(
                    [-0.4, 0.7, 0],
                    [0.4, -0.7, 0],
                    [-0.4, -0.7, 0],
                    [-0.81, 0, 0],
                    [-0.4, 0.7, 0],
                    color=PINK,
                    stroke_width=0,
                    fill_opacity=1
                ),
            ),
            VGroup(
                Square(1.4, color=LIGHT_GRAY_COLOR, fill_opacity=1, stroke_width=0),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.525 * UP + 0.175 * LEFT),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.525 * UP + 0.525 * RIGHT),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.175 * UP + 0.175 * RIGHT),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.175 * UP + 0.525 * LEFT),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.175 * DOWN + 0.175 * LEFT),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.175 * DOWN + 0.525 * RIGHT),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.525 * DOWN + 0.525 * LEFT),
                Square(0.35, color=LIGHT_PINK, fill_opacity=1, stroke_width=0).shift(0.525 * DOWN + 0.175 * RIGHT)
            ).shift(2 * RIGHT),
            VGroup(
                Circle(0.7, color=LIGHT_GRAY_COLOR, fill_opacity=1),
                Sector(0.7, 0, color=LIGHT_GREEN_COLOR, fill_opacity=1, angle=PI),
                Sector(0.52, 0, color=LIGHT_PURPLE_COLOR, fill_opacity=1, angle=PI),
                Line(0.7 * LEFT, 0.7 * RIGHT, color=LIGHT_GRAY_COLOR),
                Line(0.6 * UP, 0.7 * DOWN, color=LIGHT_GRAY_COLOR),
                Line(0.6 * UP, ORIGIN, color=LIGHT_GRAY_COLOR).rotate(PI / 4, about_point=ORIGIN),
                Line(0.6 * UP, ORIGIN, color=LIGHT_GRAY_COLOR).rotate(-PI / 4, about_point=ORIGIN),
                Sector(0.6, 0.52, color=LIGHT_YELLOW_COLOR, fill_opacity=1, angle=PI)
            ).shift(2 * DOWN + 2 * LEFT),
            VGroup(
                Polygon(
                    [0, 0.86, 0],
                    [0.82, 0.27, 0],
                    [0.5, -0.69, 0],
                    [-0.5, -0.69, 0],
                    [-0.82, 0.27, 0],
                    [0, 0.86, 0],
                    color=LIGHT_GRAY_COLOR,
                    stroke_width=0,
                    fill_opacity=1
                ),
                Polygon(
                    [0, 0, 0],
                    [0.82, 0.27, 0],
                    [0.5, -0.69, 0],
                    [-0.5, -0.69, 0],
                    [0, 0, 0],
                    color=AQUA_GREEN_COLOR,
                    stroke_width=0,
                    fill_opacity=1
                )
            ).center().shift(2 * DOWN),
            VGroup(
                Polygon(
                    [-0.7, 0.4, 0],
                    [-0.4, 0.7, 0],
                    [0.7, -0.4, 0],
                    [0.4, -0.7, 0],
                    [-0.7, 0.4, 0],
                    color=LIGHT_GRAY_COLOR,
                    fill_opacity=1
                ),
                Polygon(
                    [-0.7, 0.4, 0],
                    [-0.4, 0.7, 0],
                    [-0.13, 0.43, 0],
                    [-0.28, 0.28, 0],
                    [0.55, -0.55, 0],
                    [0.4, -0.7, 0],
                    [-0.7, 0.4, 0],
                    color=BROWN_COLOR,
                    fill_opacity=1
                ),
            ).shift(2 * DOWN + 2 * RIGHT),
        )

        self.play(AnimateFromLeft(text_1, text_2, square, pieces))
        self.wait(1)
        self.play(pieces[6].animate(run_time=1.5, rate_func=lambda t: smooth(t if t < 0.5 else (1 - t), 10)).scale(1.2).set_color(YELLOW))
        self.play(pieces[3].animate(run_time=1.5, rate_func=lambda t: smooth(t if t < 0.5 else (1 - t), 10)).scale(1.2).set_color(YELLOW))
        self.remove(*self.mobjects)