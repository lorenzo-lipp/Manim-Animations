from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class PerimeterTwo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        poly = Polygon(
            [5.088, 2.24, 0],
            [7.79, 3.54, 0],
            [7.86, 10.54, 0],
            [-0.74, 3.69, 0],
            [5.088, 2.24, 0],
            color=LIGHT_PINK,
            fill_opacity=0.5
        )
        poly.center()
        poly.scale(0.8)
        poly.shift(UP)
        sizes = VGroup(
            Text("11", color=LIGHT_PINK)
                .shift(2 * UP + 0.5 * LEFT),
            Text("7", color=LIGHT_PINK)
                .shift(3.8 * RIGHT + 0.9 * UP),
            Text("3", color=LIGHT_PINK)
                .shift(2.7 * RIGHT + 2.2 * DOWN),
            Text("6", color=LIGHT_PINK)
                .shift(0.9 * LEFT + 2.2 * DOWN)
        )
        sum_text = Tex("11 + 7 + 3 + 6 = 27", color=LIGHT_PINK)
        sum_text.scale(1.7)
        sum_text.next_to(poly, direction=DOWN, buff=1.7)
        

        self.play(DrawBorderThenFill(poly))
        self.play(*[Write(size) for size in sizes])
        self.wait(1)
        self.play(LaggedStart(
            TransformFromCopy(sizes[0][0:], sum_text[0][0:2]),
            TransformFromCopy(sizes[1][0], sum_text[0][3]),
            TransformFromCopy(sizes[2][0], sum_text[0][5]),
            TransformFromCopy(sizes[3][0], sum_text[0][7]),
            lag_ratio=0.5
        ))
        self.wait(0.3)
        self.play(
            Write(sum_text[0][2].set_color(LIGHT_BLUE_COLOR)),
            Write(sum_text[0][4].set_color(LIGHT_BLUE_COLOR)),
            Write(sum_text[0][6].set_color(LIGHT_BLUE_COLOR)),
            run_time=0.7
        )
        self.wait(0.5)
        self.play(
            Write(sum_text[0][8:].set_color(LIGHT_BLUE_COLOR)),
            run_time=0.7
        )
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)