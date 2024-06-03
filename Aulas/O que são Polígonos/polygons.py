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

        self.play(AnimateFromLeft(shapes), run_time=0.7)
        self.wait(3.2)
        self.play(Indicate(shapes[1][1], color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(0.3)
        self.play(Indicate(shapes[2][0], color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(0.3)
        self.play(AlmostFadeOut(shapes[1][1], shapes[2][0]), run_time=0.7)
        self.wait(2.4)
        self.play(Indicate(shapes[0][0], color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(0.3)
        self.play(Indicate(shapes[3][0], color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(0.3)
        self.play(AlmostFadeOut(shapes[0][0], shapes[3][0]), run_time=0.7)
        self.wait(2.4)
        self.play(Indicate(shapes[0][1], color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(0.3)
        self.play(Indicate(shapes[3][1], color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(0.3)
        self.play(AlmostFadeOut(shapes[0][1], shapes[3][1]), run_time=0.7)
        self.wait(2.4)
        self.play(Indicate(shapes[2][1], color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(0.3)
        self.play(AlmostFadeOut(shapes[2][1]), run_time=0.7)
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
        self.wait(4)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)