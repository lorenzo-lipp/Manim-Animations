from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class GraphOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

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
        text = VGroup(
            Tex("Três pessoas preferem banana", color=BLACK),
            Tex("Uma pessoa prefere laranja", color=BLACK),
            Tex("Duas pessoas preferem morango", color=BLACK)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        text.shift(2.8 * DOWN)

        self.play(
            FadeIn(lines),
            FadeIn(chart), 
            FadeIn(x_label), 
            FadeIn(y_label), 
            run_time=0.4
        )
        self.play(chart.animate.change_bar_values([3, 0, 0]), run_time=1.4, rate_func=linear)
        self.wait(0.5)
        self.play(chart.animate.change_bar_values([3, 1, 0]), run_time=0.6, rate_func=linear)
        self.wait(0.5)
        self.play(chart.animate.change_bar_values([3, 1, 2]), run_time=1, rate_func=linear)
        self.wait(1.3)
        self.play(
            lines[2].animate.set(color=LIGHT_RED_COLOR), 
            chart.y_axis.numbers[2].animate.set(color=LIGHT_RED_COLOR).scale(1.5),
            run_time=0.7
        )
        self.play(Write(text[0]), run_time=0.7)
        self.wait(1.2)
        self.play(
            lines[2].animate.set(color=LIGHT_GRAY), 
            chart.y_axis.numbers[2].animate.set(color=BLACK).scale(2/3),
            lines[0].animate.set(color=LIGHT_RED_COLOR),
            chart.y_axis.numbers[0].animate.set(color=LIGHT_RED_COLOR).scale(1.5),
            run_time=0.7
        )
        self.play(Write(text[1]), run_time=0.7)
        self.wait(1.2)
        self.play(
            lines[0].animate.set(color=LIGHT_GRAY), 
            chart.y_axis.numbers[0].animate.set(color=BLACK).scale(2/3),
            lines[1].animate.set(color=LIGHT_RED_COLOR),
            chart.y_axis.numbers[1].animate.set(color=LIGHT_RED_COLOR).scale(1.5),
            run_time=0.7
        )
        self.play(Write(text[2]), run_time=0.7)
        self.wait(1.2)
        self.play(
            lines[1].animate.set(color=LIGHT_GRAY), 
            chart.y_axis.numbers[1].animate.set(color=BLACK).scale(2/3),
            run_time=0.7
        )
        self.play(
            FadeOut(text),
            run_time=0.7
        )
        self.wait(1)
        self.remove(*self.mobjects)