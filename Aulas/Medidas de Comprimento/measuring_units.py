from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class MeasuringUnits(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        units = Group(
            VGroup(
                Tex(r"Quilômetro", color=LIGHT_RED_COLOR),
                Tex(r"$\longrightarrow$", color=DARK_GRAY),
                Tex(r"km", color=LIGHT_RED_COLOR)
            ).scale(2).arrange(RIGHT, buff=0.2),
            VGroup(
                Tex(r"Metro", color=LIGHT_BLUE_COLOR),
                Tex(r"$\longrightarrow$", color=DARK_GRAY),
                Tex(r"m", color=LIGHT_BLUE_COLOR)
            ).scale(2).arrange(RIGHT, buff=0.2),
            VGroup(
                Tex(r"Centímetro", color=LIGHT_PURPLE_COLOR),
                Tex(r"$\longrightarrow$", color=DARK_GRAY),
                Tex(r"cm", color=LIGHT_PURPLE_COLOR)
            ).scale(2).arrange(RIGHT, buff=0.2),
            VGroup(
                Tex(r"Milímetro", color=LIGHT_GREEN_COLOR),
                Tex(r"$\longrightarrow$", color=DARK_GRAY),
                Tex(r"mm", color=LIGHT_GREEN_COLOR)
            ).scale(2).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=1.2)

        self.play(
            LaggedStart(
                *[Write(text) for text in units],
                lag_ratio=0.8
            )
        )
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))
        self.remove(*self.mobjects)