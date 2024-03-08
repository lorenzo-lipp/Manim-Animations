from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class GraphTwo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        chart = BarChart(
            [3, 1, 2],
            y_range=[0, 3, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLACK, "include_ticks": False},
            bar_colors=[LIGHT_YELLOW_COLOR, LIGHT_ORANGE_COLOR, LIGHT_RED_COLOR],
            bar_fill_opacity=1,
            bar_names=["Banana", "Laranja", "Morango"]
        )
        chart.x_axis.set(color=BLACK)
        chart.y_axis.set(color=BACKGROUND_COLOR)
        chart[2][0][1].set(color=BLACK)
        x_label = Tex("Frutas favoritas", color=BLACK)
        x_label.scale(0.7)
        x_label.next_to(chart, DOWN)
        x_label.shift(0.2 * RIGHT)
        y_label = Tex("Quantidade de pessoas", color=BLACK)
        y_label.scale(0.7)
        y_label.rotate(PI/2)
        y_label.next_to(chart, LEFT)
        y_label.shift(0.2 * UP)
        Group(chart, x_label, y_label).shift(2 * UP)
        lines = VGroup(
            Line(chart.coords_to_point(0, 1, 0), chart.coords_to_point(3, 1, 0), color=LIGHT_GRAY, stroke_width=3),
            Line(chart.coords_to_point(0, 2, 0), chart.coords_to_point(3, 2, 0), color=LIGHT_GRAY, stroke_width=3),
            Line(chart.coords_to_point(0, 3, 0), chart.coords_to_point(3, 3, 0), color=LIGHT_GRAY, stroke_width=3)
        )
        circle = Circle(2, color=BLACK)
        legend = VGroup(
            VGroup(
                Square(0.3, fill_opacity=1, color=LIGHT_YELLOW_COLOR), 
                Tex("Banana", color=BLACK).scale(0.5)
            ).arrange(RIGHT),
            VGroup(
                Square(0.3, fill_opacity=1, color=LIGHT_ORANGE_COLOR), 
                Tex("Laranja", color=BLACK).scale(0.5)
            ).arrange(RIGHT),
            VGroup(
                Square(0.3, fill_opacity=1, color=LIGHT_RED_COLOR), 
                Tex("Morango", color=BLACK).scale(0.5)
            ).arrange(RIGHT)
        ).arrange(DOWN, aligned_edge=LEFT)
        graph = Group(circle, legend)
        legend.shift(3.5 * RIGHT)
        graph.shift(3.8 * DOWN + LEFT)
        basic_line = Line(circle.get_center(), circle.get_top(), color=BLACK)
        auxiliary_lines = VGroup(
            basic_line.copy(),
            basic_line.copy().rotate(PI / 3, about_point=basic_line.get_bottom()),
            basic_line.copy().rotate(2 * PI / 3, about_point=basic_line.get_bottom()),
            basic_line.copy().rotate(PI, about_point=basic_line.get_bottom()),
            basic_line.copy().rotate(4 * PI / 3, about_point=basic_line.get_bottom()),
            basic_line.copy().rotate(5 * PI / 3, about_point=basic_line.get_bottom())
        )
        banana_angle = ValueTracker(0)
        banana_max_angle = PI
        banana_sector = always_redraw(lambda: 
            AnnularSector(0, 2, banana_angle.get_value(), PI/2, stroke_width=0, color=LIGHT_YELLOW_COLOR, fill_opacity=1)
                .shift(3.8 * DOWN + LEFT)
        )
        strawberry_angle = ValueTracker(0)
        strawberry_max_angle = 2 * PI / 3
        strawberry_sector = always_redraw(lambda: 
            AnnularSector(0, 2, strawberry_angle.get_value(), 6*PI/4, stroke_width=0, color=LIGHT_RED_COLOR, fill_opacity=1)
                .shift(3.8 * DOWN + LEFT)
        )
        orange_angle = ValueTracker(0)
        orange_max_angle = PI / 3
        orange_sector = always_redraw(lambda:
            AnnularSector(0, 2, orange_angle.get_value(), 13*PI/6, stroke_width=0, color=LIGHT_ORANGE_COLOR, fill_opacity=1)
                .shift(3.8 * DOWN + LEFT)
        )

        self.add(lines, chart, x_label, y_label)
        self.play(
            FadeIn(graph), 
            run_time=0.7
        )
        self.wait(1.5)
        self.play(FadeIn(auxiliary_lines), run_time=0.7)
        self.wait(1.5)
        add_to_back(self, banana_sector)
        self.wait(1)
        self.play(banana_angle.animate.set_value(banana_max_angle), run_time=2)
        banana_sector.clear_updaters()
        self.wait(1)
        add_to_back(self, strawberry_sector)
        self.play(strawberry_angle.animate.set_value(strawberry_max_angle), run_time=1.5)
        strawberry_sector.clear_updaters()
        self.wait(1)
        add_to_back(self, orange_sector)
        self.play(orange_angle.animate.set_value(orange_max_angle), run_time=1)
        self.wait(1)
        orange_sector.clear_updaters()
        self.play(
            FadeOut(auxiliary_lines[1]),
            FadeOut(auxiliary_lines[2]),
            FadeOut(auxiliary_lines[4]),
            run_time=0.7
        )
        self.wait(0.7)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)