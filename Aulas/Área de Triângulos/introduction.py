from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Área de Triângulos", color=LIGHT_BLUE_COLOR).scale(2)
        triangles = VGroup(*[
            Triangle(color=LIGHT_GREEN_COLOR, fill_opacity=1)
                .scale(0.4)
                .move_to(title[0][7])
                .shift(i * 0.9 * RIGHT + 0.1 * RIGHT + 0.08 * DOWN)
            for i in range(5)
        ])

        self.play(Write(title), run_time=0.7)
        self.wait(0.5)
        self.play(
            LaggedStart(
                Transform(title[0][7:9], triangles[0]),
                Transform(title[0][9:12], triangles[1]),
                Transform(title[0][12:14], triangles[2]),
                Transform(title[0][14:16], triangles[3]),
                Transform(title[0][16:18], triangles[4]),
                lag_ratio=0.3
            )
        )
        self.wait(0.5)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)