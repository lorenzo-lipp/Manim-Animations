from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class MeasuringAngleSquare(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        protractor = Protractor()
        protractor.scale(1.5)
        protractor.shift(8 * RIGHT)
        square = Square(4, color=LIGHT_RED_COLOR, fill_opacity=0.4)

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
        right_angle = Square(0.4, color=angle_color)
        right_angle.move_to(fixed_left_point, aligned_edge=DL)

        self.play(AnimateFromLeft(square))
        self.wait(1)        
        self.play(protractor.animate.move_to(2 * LEFT + 0.87 * DOWN))
        self.play(FadeIn(bottom_line))
        self.add(movable_line, lines_angle)
        for i in range(0, 90, 10):
            self.play(
                movable_right_point.animate(rate_func=linear)
                    .rotate(9.99 * DEGREES, about_point=fixed_left_point), 
                Indicate(
                    protractor.inner_text[i // 10], 
                    color=LIGHT_RED_COLOR, 
                    scale_factor=1.8
                ),
                run_time=0.3
            )
            self.wait(0.015)
        self.play(
            FadeOut(lines_angle),
            FadeIn(right_angle),
            run_time=0.6
        )
        self.play(
            Indicate(
                protractor.ninety_degrees_text, 
                color=LIGHT_RED_COLOR, 
                scale_factor=1.5
            ),
            run_time=1
        )
        self.wait(1)
        self.play(Group(*self.mobjects).animate.shift(14 * LEFT))
        self.remove(*self.mobjects)