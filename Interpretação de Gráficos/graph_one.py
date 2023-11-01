from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class GraphOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        table = Table(
            [
                ["Pablo", "Banana"],
                ["Gabriela", "Morango"],
                ["Bianca", "Laranja"],
                ["Murilo", "Morango"],
                ["Heitor", "Banana"],
                ["Isabela", "Banana"],
            ],
            col_labels=[Text("Nome"), Text("Fruta Favorita")],
            include_outer_lines=True
        )
        table.get_vertical_lines().set(color=BLACK)
        table.get_horizontal_lines().set(color=BLACK)
        table.get_entries().set(color=BLACK)
        table.scale(0.5)
        chart = BarChart(
            [0, 0, 0],
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
        Group(table, chart).arrange(DOWN, buff=2)
        x_label = Tex("Frutas favoritas", color=BLACK)
        x_label.scale(0.7)
        x_label.next_to(chart, DOWN)
        x_label.shift(0.2 * RIGHT)
        y_label = Tex("Quantidade de pessoas", color=BLACK)
        y_label.scale(0.7)
        y_label.rotate(PI/2)
        y_label.next_to(chart, LEFT)
        y_label.shift(0.2 * UP)
        table.shift(9 * RIGHT)
        lines = VGroup(
            Line(chart.coords_to_point(0, 1, 0), chart.coords_to_point(3, 1, 0), color=BLACK, stroke_width=1),
            Line(chart.coords_to_point(0, 2, 0), chart.coords_to_point(3, 2, 0), color=BLACK, stroke_width=1),
            Line(chart.coords_to_point(0, 3, 0), chart.coords_to_point(3, 3, 0), color=BLACK, stroke_width=1)
        )

        self.play(table.animate.shift(9 * LEFT), run_time=0.7)
        self.wait(1)
        self.play(
            FadeIn(lines),
            FadeIn(chart), 
            FadeIn(x_label), 
            FadeIn(y_label), 
            run_time=0.4
        )
        self.wait(1)

        banana_cells = Group(
            table.get_highlighted_cell((2, 1), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((2, 2), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((6, 1), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((6, 2), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((7, 1), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((7, 2), color=LIGHT_YELLOW_COLOR)
        )
        add_to_back(self, banana_cells)

        self.play(FadeIn(banana_cells), run_time=0.5)
        self.play(chart.animate.change_bar_values([3, 0, 0]), run_time=1.3)
        self.play(FadeOut(banana_cells), run_time=0.5)

        orange_cells = Group(
            table.get_highlighted_cell((4, 1), color=LIGHT_ORANGE_COLOR),
            table.get_highlighted_cell((4, 2), color=LIGHT_ORANGE_COLOR)
        )
        add_to_back(self, orange_cells)

        self.play(FadeIn(orange_cells), run_time=0.5)
        self.play(chart.animate.change_bar_values([3, 1, 0]), run_time=0.7)
        self.play(FadeOut(orange_cells), run_time=0.5)

        strawberry_cells = Group(
            table.get_highlighted_cell((3, 1), color=LIGHT_RED_COLOR),
            table.get_highlighted_cell((3, 2), color=LIGHT_RED_COLOR),
            table.get_highlighted_cell((5, 1), color=LIGHT_RED_COLOR),
            table.get_highlighted_cell((5, 2), color=LIGHT_RED_COLOR)
        )
        add_to_back(self, strawberry_cells)

        self.play(FadeIn(strawberry_cells), run_time=0.5)
        self.play(chart.animate.change_bar_values([3, 1, 2]), run_time=1)
        self.play(FadeOut(strawberry_cells), run_time=0.5)

        self.wait(2)

        self.play(
            FadeOut(lines),
            FadeOut(chart), 
            FadeOut(x_label), 
            FadeOut(y_label), 
            run_time=0.4
        )
        self.remove(*self.mobjects)