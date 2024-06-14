from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class NonQuadrilaterals(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        quadrilateral = Rectangle(LIGHT_GREEN_COLOR, 1, 2, fill_opacity=0.8)
        quadrilateral.shift(1.5 * LEFT)
        tridimensional = VGroup(
            Rectangle(LIGHT_GREEN_COLOR, 1, 2, fill_opacity=0.8)
                .shift(0.2 * (RIGHT + DOWN)),
            Polygon(
                0.5 * UP + RIGHT, 
                0.3 * UP + 1.2 * RIGHT,
                0.3 * UP + 0.8 * LEFT,
                0.5 * UP + LEFT,
                color=LIGHT_GREEN_COLOR,
                fill_opacity=0.6
            ),
            Polygon(
                0.3 * UP + 0.8 * LEFT,
                0.5 * UP + LEFT,
                0.5 * DOWN + LEFT,
                0.7 * DOWN + 0.8 * LEFT,
                color=LIGHT_GREEN_COLOR,
                fill_opacity=0.6
            )
        )
        tridimensional.shift(1.5 * RIGHT)
        text_1 = VGroup(
            VGroup(Tex("É plana", color=LIGHT_GREEN_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_GREEN_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(quadrilateral, UP, buff=0.3),
            VGroup(Tex("Não é plana", color=LIGHT_RED_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_RED_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(tridimensional, UP, buff=0.3)
        )
        open_fig = VGroup(
            Line(0.5 * UP + LEFT, 0.5 * UP + RIGHT, color=LIGHT_GREEN_COLOR),
            Line(0.5 * UP + RIGHT, 0.5 * DOWN + RIGHT, color=LIGHT_GREEN_COLOR),
            Line(0.5 * DOWN + LEFT, 0.5 * DOWN + RIGHT, color=LIGHT_GREEN_COLOR),
            Line(0.5 * UP + LEFT, 0.5 * DOWN + LEFT, color=LIGHT_GREEN_COLOR),
        ).shift(1.5 * RIGHT)
        text_2 = VGroup(
            VGroup(Tex("É fechada", color=LIGHT_GREEN_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_GREEN_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(quadrilateral, UP, buff=0.3),
            VGroup(Tex("É aberta", color=LIGHT_RED_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_RED_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(open_fig, UP, buff=0.3)
        )
        stroke_1 = VGroup(
            Line(UP + 2 * LEFT, UP + 2 * RIGHT, color=LIGHT_BLUE_COLOR),
            Dot(UP + 2 * LEFT, color=LIGHT_BLUE_COLOR),
            Dot(UP + 2 * RIGHT, color=LIGHT_BLUE_COLOR)
        )
        stroke_2 = VGroup(
            Line(UP + 2 * RIGHT, DOWN + 2 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(UP + 2 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(DOWN + 2 * RIGHT, color=LIGHT_RED_COLOR)
        )
        stroke_3 = VGroup(
            Line(DOWN + 2 * RIGHT, DOWN + 2 * LEFT, color=LIGHT_PURPLE_COLOR),
            Dot(DOWN + 2 * RIGHT, color=LIGHT_PURPLE_COLOR),
            Dot(DOWN + 2 * LEFT, color=LIGHT_PURPLE_COLOR)
        )
        stroke_4 = VGroup(
            Line(DOWN + 2 * LEFT, UP + 2 * LEFT, color=LIGHT_ORANGE_COLOR),
            Dot(DOWN + 2 * LEFT, color=LIGHT_ORANGE_COLOR),
            Dot(UP + 2 * LEFT, color=LIGHT_ORANGE_COLOR)
        )

        self.play(AnimateFromLeft(quadrilateral))
        self.wait(0.5)
        self.play(TransformFromCopy(quadrilateral, tridimensional, run_time=0.7))
        self.wait(0.7)
        self.play(Write(text_1), run_time=1)
        self.wait(1.3)
        self.play(FadeOut(text_1, tridimensional, run_time=0.4))
        self.wait(0.4)
        self.play(TransformFromCopy(quadrilateral, open_fig, run_time=0.7))
        self.play(open_fig[1].animate.rotate(30 * DEGREES, about_point=open_fig[1].get_start()), run_time=0.6)
        self.wait(0.5)
        self.play(Write(text_2), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(text_2, open_fig, run_time=0.5))
        self.wait(0.5)
        self.play(quadrilateral.animate.shift(1.5 * RIGHT).scale(2), run_time=0.7)
        self.play(FadeIn(stroke_1),run_time=0.7)
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_2), run_time=0.7)
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_3), run_time=0.7)
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_4), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)