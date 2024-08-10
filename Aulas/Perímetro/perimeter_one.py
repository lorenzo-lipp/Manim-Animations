from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class PerimeterOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        poly = Polygon(
            [6.6, 1.32, 0],
            [8.535, 8.05, 0],
            [-0.136, 5.634, 0],
            [6.6, 1.32, 0],
            color=LIGHT_BLUE_COLOR,
            fill_opacity=0.5
        )
        poly.center()
        poly.scale(0.8)
        sizes = VGroup(
            Text("9", color=LIGHT_BLUE_COLOR)
                .shift(2.2 * UP + 0.1 * LEFT),
            Text("7", color=LIGHT_BLUE_COLOR)
                .shift(3.1 * RIGHT + 0.3 * DOWN),
            Text("8", color=LIGHT_BLUE_COLOR)
                .shift(0.9 * LEFT + 1.4 * DOWN)
        )
        sum_text = Tex("9 + 7 + 8 = 24", color=LIGHT_BLUE_COLOR)
        sum_text.scale(2)
        sum_text.next_to(poly, direction=DOWN, buff=2)
        

        self.play(DrawBorderThenFill(poly))
        self.play(*[Write(size) for size in sizes])
        self.wait(1)
        self.play(TransformFromCopy(sizes[0][0], sum_text[0][0]))
        self.wait(0.3)
        self.play(TransformFromCopy(sizes[1][0], sum_text[0][2]))
        self.wait(0.3)
        self.play(TransformFromCopy(sizes[2][0], sum_text[0][4]))
        self.wait(1)
        self.play(
            Write(sum_text[0][1].set_color(LIGHT_RED_COLOR)),
            Write(sum_text[0][3].set_color(LIGHT_RED_COLOR)),
            run_time=0.7
        )
        self.wait(0.5)
        self.play(
            Write(sum_text[0][5:].set_color(LIGHT_RED_COLOR)),
            run_time=0.7
        )
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)