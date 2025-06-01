from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("O que é", color="#a346eb")
                .scale(3),
            Tex("Ângulo?", color="#a346eb")
                .scale(3)
        )
        title.arrange(DOWN, buff=0.4)

        self.play(Write(title), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        angle_color = BLACK
        fixed_left_point = 2 * LEFT + 2 * DOWN
        fixed_right_point = 2 * RIGHT + 2 * DOWN
        movable_right_point = Point(fixed_right_point)
        movable_right_point.rotate(0.1 * DEGREES, about_point=fixed_left_point)
        bottom_line = Line(fixed_left_point, fixed_right_point, color=angle_color)
        movable_line = always_redraw(lambda: Line(fixed_left_point, movable_right_point, color=angle_color))
        lines_angle = always_redraw(lambda: 
            Angle.from_three_points(
                fixed_right_point, 
                fixed_left_point, 
                movable_right_point, 
                color=angle_color
            )
        )

        self.play(FadeIn(bottom_line))
        self.add(movable_line, lines_angle)
        for i in range(0, 60, 10):
            self.play(
                movable_right_point.animate(rate_func=linear)
                    .rotate(9.99 * DEGREES, about_point=fixed_left_point), 
                run_time=0.5
            )
            self.wait(0.015)
        self.wait(0.5)
        self.remove(movable_right_point)
        self.play(FadeOut(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)