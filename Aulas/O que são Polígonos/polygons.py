from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Polygons(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        shapes = VGroup(
            VGroup(
                Shape1(color=DARK_GRAY, stroke_width=8),
                Shape2(color=LIGHT_BLUE_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape3(color=LIGHT_PURPLE_COLOR, fill_opacity=0.6, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
            VGroup(
                Shape4(color=LIGHT_GREEN_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape9(color=DARK_GRAY, fill_opacity=0.5, stroke_width=5),
                Shape6(color=LIGHT_YELLOW_COLOR, fill_opacity=0.5, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
            VGroup(
                Shape7(color=AQUA_BLUE_COLOR, fill_opacity=0.5, stroke_width=5, joint_type=LineJointType.ROUND),
                Shape8(color=LIGHT_PINK, fill_opacity=0.6, stroke_width=5),
                Shape5(color=LIGHT_RED_COLOR, fill_opacity=0.6, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
            VGroup(
                Shape10(color=DARK_GRAY, stroke_width=8),
                Shape13(color=LIGHT_PURPLE_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape12(color=BROWN_COLOR, fill_opacity=0.6, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
            VGroup(
                Shape11(color=AQUA_GREEN_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape14(color=LIGHT_ORANGE_COLOR, fill_opacity=0.6, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
        ).arrange(DOWN, buff=0.8)
        shapes.shift(0.8 * DOWN)
        text_1 = Tex("Plana", color=TEXT_COLOR)
        text_1.scale(2)
        text_1.next_to(shapes, UP, 0.8)
        text_2 = Tex("Fechada", color=TEXT_COLOR)
        text_2.scale(2)
        text_2.next_to(shapes, UP, 0.8)
        text_3 = VGroup(
            Tex("Formada por", color=TEXT_COLOR),
            Tex("segmentos de reta", color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.2)
        text_3.scale(1.5)
        text_3.next_to(shapes, UP, 0.6)
        text_4 = VGroup(
            Tex("Os lados não", color=TEXT_COLOR),
            Tex("podem se cruzar", color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.2)
        text_4.scale(1.5)
        text_4.next_to(shapes, UP, 0.6)
        polygons = VGroup(
            VGroup(
                Shape3(color=LIGHT_PURPLE_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape4(color=LIGHT_GREEN_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape6(color=LIGHT_YELLOW_COLOR, fill_opacity=0.5, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
            VGroup(
                Shape5(color=LIGHT_RED_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape12(color=BROWN_COLOR, fill_opacity=0.6, stroke_width=5),
                Shape11(color=AQUA_GREEN_COLOR, fill_opacity=0.6, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
            VGroup(
                Shape14(color=LIGHT_ORANGE_COLOR, fill_opacity=0.6, stroke_width=5)
            ).scale(1.5).arrange(RIGHT, buff=0.8),
        ).arrange(DOWN, buff=0.8)

        self.play(AnimateFromLeft(shapes))
        self.wait(1)
        self.play(Write(text_1))
        self.wait(1)
        self.play(Indicate(shapes[1][1], color=LIGHT_RED_COLOR, run_time=2))
        self.wait(0.3)
        self.play(Indicate(shapes[2][0], color=LIGHT_RED_COLOR, run_time=2))
        self.wait(0.7)
        self.play(AlmostFadeOut(shapes[1][1], shapes[2][0]), run_time=0.7)
        self.wait(0.5)
        self.play(Transform(text_1, text_2))
        self.wait(1)
        self.play(Indicate(shapes[0][0], color=LIGHT_RED_COLOR, run_time=2))
        self.wait(0.3)
        self.play(Indicate(shapes[3][0], color=LIGHT_RED_COLOR, run_time=2))
        self.wait(0.7)
        self.play(AlmostFadeOut(shapes[0][0], shapes[3][0]), run_time=0.7)
        self.wait(0.5)
        self.play(Transform(text_1, text_3))
        self.wait(1)
        self.play(Indicate(shapes[0][1], color=LIGHT_RED_COLOR, run_time=2))
        self.wait(0.3)
        self.play(Indicate(shapes[3][1], color=LIGHT_RED_COLOR, run_time=2))
        self.wait(0.7)
        self.play(AlmostFadeOut(shapes[0][1], shapes[3][1]), run_time=0.7)
        self.wait(0.5)
        self.play(Transform(text_1, text_4))
        self.wait(1)
        self.play(Indicate(shapes[2][1], color=LIGHT_RED_COLOR, run_time=2))
        self.wait(0.7)
        self.play(AlmostFadeOut(shapes[2][1]), FadeOut(text_1), run_time=0.7)
        self.wait(1)
        self.play(
            FadeOut(shapes[0][0], run_time=0.6),
            FadeOut(shapes[0][1], run_time=0.6),
            Transform(shapes[0][2], polygons[0][0]),
            Transform(shapes[1][0], polygons[0][1]),
            FadeOut(shapes[1][1], run_time=0.6),
            Transform(shapes[1][2], polygons[0][2]),
            FadeOut(shapes[2][0], run_time=0.6),
            FadeOut(shapes[2][1], run_time=0.6),
            Transform(shapes[2][2], polygons[1][0]),
            FadeOut(shapes[3][0], run_time=0.6),
            FadeOut(shapes[3][1], run_time=0.6),
            Transform(shapes[3][2], polygons[1][1]),
            Transform(shapes[4][0], polygons[1][2]),
            Transform(shapes[4][1], polygons[2][0]),
        )
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)