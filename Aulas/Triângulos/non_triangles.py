from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class NonTriangles(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        triangle = Triangle(color=LIGHT_GREEN_COLOR, fill_opacity=0.8)
        tridimensional = VGroup(
            Triangle(color=LIGHT_GREEN_COLOR, fill_opacity=0.8)
                .shift(0.2 * RIGHT),
            Polygon(
                triangle.points[0], 
                triangle.points[0] + 0.2 * RIGHT,
                triangle.points[3] + 0.2 * RIGHT,
                triangle.points[3] + 0.1 * LEFT + 0.15 * DOWN,
                color=LIGHT_GREEN_COLOR,
                fill_opacity=0.6
            ),
            Polygon(
                triangle.points[7] + 0.2 * RIGHT,
                triangle.points[3] + 0.2 * RIGHT, 
                triangle.points[3] + 0.1 * LEFT + 0.15 * DOWN,
                triangle.points[7] + 0.15 * DOWN,
                color=LIGHT_GREEN_COLOR,
                fill_opacity=0.6,
                joint_type=LineJointType.ROUND
            ),
        )
        tridimensional.shift(1.5 * RIGHT)
        open_fig = VGroup(
            Line(triangle.points[0], triangle.points[3], color=LIGHT_GREEN_COLOR),
            Line(triangle.points[3], triangle.points[7], color=LIGHT_GREEN_COLOR),
            Line(triangle.points[7], triangle.points[11], color=LIGHT_GREEN_COLOR)
        ).shift(1.5 * RIGHT)
        triangle.shift(1.5 * LEFT)
        text_1 = VGroup(
            VGroup(Tex("É plana", color=LIGHT_GREEN_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_GREEN_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(triangle, UP, buff=0.3),
            VGroup(Tex("Não é plana", color=LIGHT_RED_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_RED_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(tridimensional, UP, buff=0.3)
        )
        text_2 = VGroup(
            VGroup(Tex("É fechada", color=LIGHT_GREEN_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_GREEN_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(triangle, UP, buff=0.3),
            VGroup(Tex("É aberta", color=LIGHT_RED_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_RED_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(open_fig, UP, buff=0.3)
        )

        self.play(AnimateFromLeft(triangle))
        self.wait(0.5)
        self.play(TransformFromCopy(triangle, tridimensional, run_time=0.7))
        self.wait(0.5)
        self.play(Write(text_1), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(text_1, tridimensional, run_time=0.5))
        self.wait(0.4)
        self.play(TransformFromCopy(triangle, open_fig, run_time=0.7))
        self.play(open_fig[2].animate.rotate(10 * DEGREES, about_point=open_fig[2].get_end()), run_time=0.6)
        self.wait(0.5)
        self.play(Write(text_2), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(text_2, open_fig, run_time=0.5))
        self.wait(0.5)
        self.play(triangle.animate.shift(1.5 * RIGHT).scale(2), run_time=0.7)

        stroke_1 = VGroup(
            Line(triangle.points[0], triangle.points[3], color=LIGHT_BLUE_COLOR),
            Dot(triangle.points[0], color=LIGHT_BLUE_COLOR),
            Dot(triangle.points[3], color=LIGHT_BLUE_COLOR)
        )
        stroke_2 = VGroup(
            Line(triangle.points[3], triangle.points[7], color=LIGHT_RED_COLOR),
            Dot(triangle.points[3], color=LIGHT_RED_COLOR),
            Dot(triangle.points[7], color=LIGHT_RED_COLOR)
        )
        stroke_3 = VGroup(
            Line(triangle.points[7], triangle.points[11], color=LIGHT_PURPLE_COLOR),
            Dot(triangle.points[7], color=LIGHT_PURPLE_COLOR),
            Dot(triangle.points[11], color=LIGHT_PURPLE_COLOR)
        )

        self.play(FadeIn(stroke_1),run_time=0.7)
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_2), run_time=0.7)
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_3), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)