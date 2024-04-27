from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        big_triangle = Triangle(color=LIGHT_PURPLE_COLOR)
        big_triangle.scale(2)
        big_triangle.shift(2 * DOWN)
        small_triangles = VGroup(
            Triangle(color=LIGHT_GREEN_COLOR, fill_opacity=1)
                .shift(3 * UP + 1.5 * LEFT)
                .rotate(-15 * DEGREES),
            Triangle(color=LIGHT_ORANGE_COLOR, fill_opacity=1)
                .shift(3 * UP + 1.5 * RIGHT)
                .rotate(-65 * DEGREES),
            Triangle(color=LIGHT_BLUE_COLOR, fill_opacity=1)
                .shift(UP + 1.5 * LEFT)
                .rotate(15 * DEGREES),
            Triangle(color=LIGHT_RED_COLOR, fill_opacity=1)
                .shift(UP + 1.5 * RIGHT)
                .rotate(65 * DEGREES)
        )

        self.play(AnimateFromLeft(big_triangle))
        self.play(LaggedStart(
            *[SpinInFromNothing(triangle, run_time=0.7) for triangle in small_triangles],
            lag_ratio=0.6
        ))
        self.wait(1)
        self.remove(big_triangle)
        self.add(big_triangle)
        self.play(small_triangles[2].animate
                    .rotate(-15 * DEGREES)
                    .next_to(big_triangle, direction=ORIGIN, aligned_edge=DR, buff=0)  
        )
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)