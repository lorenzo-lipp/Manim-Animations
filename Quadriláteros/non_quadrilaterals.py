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
            VGroup(Tex("Não é fechada", color=LIGHT_RED_COLOR), Arrow(start=UP, end=0.5 * DOWN, color=LIGHT_RED_COLOR))
                .arrange(DOWN, buff=0.3)
                .next_to(open_fig, UP, buff=0.3)
        )
        stroke_1 = VGroup(
            Line(UP + 5 * LEFT, UP + 5 * RIGHT, color=LIGHT_BLUE_COLOR),
            Dot(UP + 2 * LEFT, color=LIGHT_BLUE_COLOR),
            Dot(UP + 2 * RIGHT, color=LIGHT_BLUE_COLOR)
        )
        stroke_1.add(Tex("1", color=LIGHT_BLUE_COLOR).next_to(stroke_1[0], UP, 0.2))
        stroke_2 = VGroup(
            Line(9 * UP + 2 * RIGHT, 9 * DOWN + 2 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(UP + 2 * RIGHT, color=LIGHT_RED_COLOR),
            Dot(DOWN + 2 * RIGHT, color=LIGHT_RED_COLOR)
        )
        stroke_2.add(Tex("2", color=LIGHT_RED_COLOR).next_to(stroke_2[0], RIGHT, 0.2))
        stroke_3 = VGroup(
            Line(DOWN + 5 * LEFT, DOWN + 5 * RIGHT, color=LIGHT_PURPLE_COLOR),
            Dot(DOWN + 2 * RIGHT, color=LIGHT_PURPLE_COLOR),
            Dot(DOWN + 2 * LEFT, color=LIGHT_PURPLE_COLOR)
        )
        stroke_3.add(Tex("3", color=LIGHT_PURPLE_COLOR).next_to(stroke_3[0], DOWN, 0.2))
        stroke_4 = VGroup(
            Line(9 * UP + 2 * LEFT, 9 * DOWN + 2 * LEFT, color=LIGHT_ORANGE_COLOR),
            Dot(DOWN + 2 * LEFT, color=LIGHT_ORANGE_COLOR),
            Dot(UP + 2 * LEFT, color=LIGHT_ORANGE_COLOR)
        )
        stroke_4.add(Tex("4", color=LIGHT_ORANGE_COLOR).next_to(stroke_4[0], LEFT, 0.2))

        self.play(AnimateFromLeft(quadrilateral))
        self.wait(0.8)
        self.play(TransformFromCopy(quadrilateral, tridimensional, run_time=0.7))
        self.wait(1)
        self.play(Write(text_1))
        self.wait(1)
        self.play(FadeOut(text_1, run_time=0.7))
        self.play(FadeOut(tridimensional, run_time=0.7))
        self.wait(0.8)
        self.play(TransformFromCopy(quadrilateral, open_fig, run_time=0.7))
        self.play(open_fig[1].animate.rotate(30 * DEGREES, about_point=open_fig[1].get_start()), run_time=0.7)
        self.wait(0.8)
        self.play(Write(text_2))
        self.wait(1)
        self.play(FadeOut(text_2, run_time=0.7))
        self.play(FadeOut(open_fig, run_time=0.7))
        self.wait(0.8)
        self.play(quadrilateral.animate.shift(1.5 * RIGHT).scale(2), run_time=0.7)
        self.play(FadeIn(stroke_1),run_time=0.7)
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_2))
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_3))
        self.wait(0.8)
        self.play(Transform(stroke_1, stroke_4))
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)