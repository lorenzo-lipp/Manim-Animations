from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class GraphTwo(Scene):
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
        table.shift(3.3 * UP)
        graph = Group(circle, legend)
        legend.shift(3 * RIGHT)
        graph.shift(3.4 * DOWN)
        title = Tex("Frutas favoritas", color=BLACK)
        title.next_to(circle, UP, buff=0.5)
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
                .shift(3.4 * DOWN)
        )
        strawberry_angle = ValueTracker(0)
        strawberry_max_angle = 2 * PI / 3
        strawberry_sector = always_redraw(lambda: 
            AnnularSector(0, 2, strawberry_angle.get_value(), 6*PI/4, stroke_width=0, color=LIGHT_RED_COLOR, fill_opacity=1)
                .shift(3.4 * DOWN)
        )
        orange_angle = ValueTracker(0)
        orange_max_angle = PI / 3
        orange_sector = always_redraw(lambda:
            AnnularSector(0, 2, orange_angle.get_value(), 13*PI/6, stroke_width=0, color=LIGHT_ORANGE_COLOR, fill_opacity=1)
                .shift(3.4 * DOWN)
        )

        self.add(table)
        self.play(
            FadeIn(graph), 
            FadeIn(title),
            run_time=0.5
        )
        self.play(FadeIn(auxiliary_lines), run_time=0.5)
        self.wait(0.5)
        
        banana_cells = Group(
            table.get_highlighted_cell((2, 1), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((2, 2), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((6, 1), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((6, 2), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((7, 1), color=LIGHT_YELLOW_COLOR),
            table.get_highlighted_cell((7, 2), color=LIGHT_YELLOW_COLOR)
        )
        add_to_back(self, banana_cells, banana_sector)

        self.play(FadeIn(banana_cells), run_time=0.5)
        self.play(banana_angle.animate.set_value(banana_max_angle), run_time=2)
        self.play(FadeOut(banana_cells), run_time=0.5)

        banana_sector.clear_updaters()
        strawberry_cells = Group(
            table.get_highlighted_cell((3, 1), color=LIGHT_RED_COLOR),
            table.get_highlighted_cell((3, 2), color=LIGHT_RED_COLOR),
            table.get_highlighted_cell((5, 1), color=LIGHT_RED_COLOR),
            table.get_highlighted_cell((5, 2), color=LIGHT_RED_COLOR)
        )
        add_to_back(self, strawberry_cells, strawberry_sector)


        self.play(FadeIn(strawberry_cells), run_time=0.5)
        self.play(strawberry_angle.animate.set_value(strawberry_max_angle), run_time=1.5)
        self.play(FadeOut(strawberry_cells), run_time=0.5) 

        strawberry_sector.clear_updaters()
        orange_cells = Group(
            table.get_highlighted_cell((4, 1), color=LIGHT_ORANGE_COLOR),
            table.get_highlighted_cell((4, 2), color=LIGHT_ORANGE_COLOR)
        )
        add_to_back(self, orange_cells, orange_sector)

        self.play(FadeIn(orange_cells), run_time=0.5)
        self.play(orange_angle.animate.set_value(orange_max_angle), run_time=1)
        self.play(
            FadeOut(auxiliary_lines[1]),
            FadeOut(auxiliary_lines[2]),
            FadeOut(auxiliary_lines[4]),
            FadeOut(orange_cells), 
            run_time=0.7
        )

        orange_sector.clear_updaters()      

        self.wait(1.3)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)