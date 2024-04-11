from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Triângulos", color=BACKGROUND_COLOR)
        title.scale(3)
        colors = ["#f06292", "#d23368", "#9c254d", "#f06262", "#d23333", "#9c2525"]
        triangle_size = Triangle().width
        triangles = VGroup(
            *[
                VGroup(*[
                    Triangle(color=colors[(2 * j + i) % 6], stroke_width=0, fill_opacity=1).rotate((i % 2) * 180 * DEGREES)
                    for i in range(int(config.frame_width + 3))
                ]).arrange(RIGHT, buff=-triangle_size/2)
                for j in range(int(config.frame_height))
            ]  
        ).arrange(DOWN, buff=0)

        self.play(FadeIn(triangles))
        self.play(Write(title), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)