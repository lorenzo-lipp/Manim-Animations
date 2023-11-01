from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class GraphThree(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Lucro mensal em reais", color=BLACK)
        axes = Axes(
            (0, 7), 
            (0, 9000, 1000), 
            x_length=7, 
            y_length=7, 
            axis_config={"color": BLACK, "include_tip": False},
            y_axis_config={"include_numbers": True},
            x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6]}
        )
        axes.y_axis.set(color=BLACK)
        axes.x_axis.add_labels({
            1: Tex("Janeiro", color=BLACK),
            2: Tex("Fevereiro", color=BLACK),
            3: Tex("Março", color=BLACK),
            4: Tex("Abril", color=BLACK),
            5: Tex("Maio", color=BLACK),
            6: Tex("Junho", color=BLACK)
        }, font_size=24)
        axes.shift(0.5 * RIGHT)
        title.next_to(axes, UP, buff=0.3)
        title.shift(0.5 * RIGHT)
        auxiliary_lines = VGroup(
            Line(axes.coords_to_point(0, 1000, 0), axes.coords_to_point(7, 1000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 2000, 0), axes.coords_to_point(7, 2000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 3000, 0), axes.coords_to_point(7, 3000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 4000, 0), axes.coords_to_point(7, 4000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 5000, 0), axes.coords_to_point(7, 5000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 6000, 0), axes.coords_to_point(7, 6000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 7000, 0), axes.coords_to_point(7, 7000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 8000, 0), axes.coords_to_point(7, 8000, 0), color=BLACK, stroke_width=1),
            Line(axes.coords_to_point(0, 9000, 0), axes.coords_to_point(7, 9000, 0), color=BLACK, stroke_width=1)
        )
        points = VGroup(
            Dot(axes.coords_to_point(1, 5000, 0), color=LIGHT_BLUE_COLOR),
            Dot(axes.coords_to_point(2, 3000, 0), color=LIGHT_BLUE_COLOR),
            Dot(axes.coords_to_point(3, 7000, 0), color=LIGHT_BLUE_COLOR),
            Dot(axes.coords_to_point(4, 8000, 0), color=LIGHT_BLUE_COLOR),
            Dot(axes.coords_to_point(5, 6000, 0), color=LIGHT_BLUE_COLOR),
            Dot(axes.coords_to_point(6, 5000, 0), color=LIGHT_BLUE_COLOR)
        )
        lines = VGroup()

        self.play(
            Write(title),
            Write(axes), 
            run_time=1
        )
        self.play(
            LaggedStart(
                *[Create(point) for point in points],
                lag_ratio=0.2,
                run_time=1
            )
        )

        add_to_back(self, auxiliary_lines)
        self.play(FadeIn(auxiliary_lines), run_time=0.5)

        for i in range(5):
            lines += Line(points[i], points[i + 1], color=LIGHT_BLUE_COLOR)
            self.play(Create(lines[i]), run_time=0.2)

        # Jan to Feb
        self.play(
            points[0].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            points[1].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            lines[0].animate.set(color=LIGHT_RED_COLOR),
            run_time=0.5
        )
        self.wait(1.2)
        self.play(
            points[0].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            points[1].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            lines[0].animate.set(color=LIGHT_BLUE_COLOR),
            run_time=0.5
        )
        # Feb to Apr
        self.play(
            points[1].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            points[2].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            points[3].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            lines[1].animate.set(color=LIGHT_RED_COLOR),
            lines[2].animate.set(color=LIGHT_RED_COLOR),
            run_time=0.5
        )
        self.wait(1.2)
        self.play(
            points[1].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            points[2].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            points[3].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            lines[1].animate.set(color=LIGHT_BLUE_COLOR),
            lines[2].animate.set(color=LIGHT_BLUE_COLOR),
            run_time=0.5
        )
        # Apr to June
        self.play(
            points[3].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            points[4].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            points[5].animate.set(color=LIGHT_RED_COLOR).scale(1.3),
            lines[3].animate.set(color=LIGHT_RED_COLOR),
            lines[4].animate.set(color=LIGHT_RED_COLOR),
            run_time=0.5
        )
        self.wait(1.2)
        self.play(
            points[3].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            points[4].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            points[5].animate.set(color=LIGHT_BLUE_COLOR).scale(1/1.3),
            lines[3].animate.set(color=LIGHT_BLUE_COLOR),
            lines[4].animate.set(color=LIGHT_BLUE_COLOR),
            run_time=0.5
        )

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)