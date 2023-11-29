from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        text = VGroup(
            Tex("Interpretação", color=LIGHT_BLUE_COLOR),
            Tex("de Gráficos", color=LIGHT_BLUE_COLOR)
        ).arrange(DOWN)
        text.scale(2.2)
        axes = Axes(
            (0, 5), 
            (0, 4), 
            x_length=5, 
            y_length=4, 
            axis_config={"color": BLACK, "tip_shape": StealthTip, "include_ticks": False}
        )
        points = VGroup(
            Dot(axes.coords_to_point(0.5, 1, 0), color=LIGHT_RED_COLOR),
            Dot(axes.coords_to_point(1.5, 1.5, 0), color=LIGHT_RED_COLOR),
            Dot(axes.coords_to_point(2.5, 0.5, 0), color=LIGHT_RED_COLOR),
            Dot(axes.coords_to_point(3.5, 2.5, 0), color=LIGHT_RED_COLOR),
            Dot(axes.coords_to_point(4.5, 0.5, 0), color=LIGHT_RED_COLOR)
        )
        bar_values = [0, 0, 0, 0, 0, 0, 0]
        chart = NoGradientBarChart(
            [*bar_values],
            y_range=[0, 0.7, 0.1],
            x_length=5,
            y_length=4,
            axis_config={"color": BLACK, "tip_shape": StealthTip, "include_ticks": False, "include_tip": True},
            bar_colors=[LIGHT_RED_COLOR, LIGHT_ORANGE_COLOR, LIGHT_YELLOW_COLOR, GREEN_COLOR, LIGHT_BLUE_COLOR, LIGHT_PURPLE_COLOR],
            bar_fill_opacity=1,
        )
        chart[2][0][2].set(color=BLACK)
        Group(text, Group(axes, points), chart).arrange(DOWN, buff=1)

        self.play(Write(text), run_time=0.7)
        self.play(Write(axes), run_time=0.4)
        self.play(
            LaggedStart(
                *[Create(point) for point in points],
                lag_ratio=0.2,
                run_time=1
            )
        )

        for i in range(4):
            self.play(Create(Line(points[i], points[i + 1], color=LIGHT_RED_COLOR)), run_time=0.2)

        self.play(Write(chart), run_time=0.4)
        self.play(chart.animate.change_bar_values([0.1, 0.2, 0.3, 0.4, 0.5, 0.6]), run_time=1)
        self.wait(0.5)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)