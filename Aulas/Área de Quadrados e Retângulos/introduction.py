from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Área de Quadrados", color=LIGHT_GREEN_COLOR).scale(1.7),
            Tex("e Retângulos", color=LIGHT_GREEN_COLOR).scale(1.7),
        ).arrange(DOWN, buff=0.4)
        squares = VGroup(*[
            Square(0.35, color=LIGHT_GREEN_COLOR, fill_opacity=1)
                .move_to(title[0][0][7])
                .shift((i - 7) * 0.5 * RIGHT)
            for i in range(7, len(title[0][0]))
        ])
        rectangles = VGroup(*[
            Rectangle(LIGHT_GREEN_COLOR, 0.25, 0.35, fill_opacity=1)
            .move_to(title[1][0][1])
                .shift((i - 1) * 0.5 * RIGHT)
            for i in range(1, len(title[1][0]))
        ])

        self.play(Write(title), run_time=0.7)
        self.wait(0.5)
        self.play(
            LaggedStart(
                *[Transform(title[0][0][i], squares[i - 7]) for i in range(7, len(title[0][0]))],
                *[Transform(title[1][0][i], rectangles[i - 1]) for i in range(1, len(title[1][0]))],
                lag_ratio=0.1
            )
        )
        self.wait(0.5)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)