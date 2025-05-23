from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class MeasuringAngleTriangle(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        protractor = Protractor()
        protractor.scale(1.5)
        protractor.shift(8 * RIGHT)
        triangle = Triangle(color=LIGHT_GREEN_COLOR, fill_opacity=0.4)
        triangle.scale(3)

        angle_color = BLACK
        fixed_left_point = 2.59 * LEFT + 2 * DOWN
        fixed_right_point = 2.59 * RIGHT + 2 * DOWN
        movable_left_point = Point(fixed_left_point, color=angle_color)
        movable_left_point.rotate(-0.01 * DEGREES, about_point=fixed_right_point)
        bottom_line = Line(fixed_left_point, fixed_right_point, color=angle_color)
        movable_line = always_redraw(lambda: Line(fixed_right_point, movable_left_point, color=angle_color))
        lines_angle = always_redraw(lambda: 
            Angle.from_three_points(
                movable_left_point, 
                fixed_right_point, 
                fixed_left_point, 
                color=angle_color
            )
        )

        self.play(AnimateFromLeft(triangle))
        self.wait(1)        
        self.play(protractor.animate.move_to(2.59 * RIGHT + 0.87 * DOWN))
        self.play(FadeIn(bottom_line))
        self.add(movable_line, lines_angle)
        for i in range(0, 60, 10):
            self.play(
                movable_left_point.animate(rate_func=linear)
                    .rotate(-10 * DEGREES, about_point=fixed_right_point), 
                Indicate(
                    protractor.outer_text[i // 10], 
                    color=LIGHT_RED_COLOR, 
                    scale_factor=1.8
                ),
                run_time=0.3
            )
            self.wait(0.015)
        self.play(
            Indicate(
                protractor.outer_text[6], 
                color=LIGHT_RED_COLOR, 
                scale_factor=1.8
            ),
            run_time=1
        )
        self.wait(1)
        self.play(Group(*self.mobjects).animate.shift(14 * LEFT))
        self.remove(*self.mobjects)