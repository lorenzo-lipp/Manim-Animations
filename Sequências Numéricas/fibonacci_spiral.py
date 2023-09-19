from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FibonacciSpiral(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        colors = [
            LIGHT_BLUE_COLOR, 
            LIGHT_RED_COLOR, 
            LIGHT_ORANGE_COLOR, 
            AQUA_GREEN_COLOR, 
            LIGHT_PURPLE_COLOR
        ]
        sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        directions = [DOWN, RIGHT, UP, LEFT]
        corners = [UR, UL, DL, DR]
        angles = [PI, 3 * PI / 2, 2 * PI, PI / 2]
        animations = []
        squares = Group(
            FibonacciSquare(sequence[0], colors[2]),
            FibonacciSquare(sequence[1], colors[3]),
            FibonacciSquare(sequence[2], colors[1]),
            FibonacciSquare(sequence[3], colors[0]),
            FibonacciSquare(sequence[4], colors[4]),
            FibonacciSquare(sequence[5], colors[3]),
            FibonacciSquare(sequence[6], colors[2]),
            FibonacciSquare(sequence[7], colors[1]),
            FibonacciSquare(sequence[8], colors[0])
        )
        squares.shift(1.5 * RIGHT + 2.5 * UP)

        for i in range(8):
            squares[i + 1].next_to(squares[i], directions[(i + 1) % 4], 0, directions[i % 4])

        for square in squares:
            animations.append(Create(square[0]))
            animations.append(Write(square[1]))

        self.play(LaggedStart(*animations, lag_ratio=0.2))

        for i in range(9):
            if i != 0: 
                self.remove(dot)

            arc_angle = ValueTracker(0.0)
            arc = always_redraw(
                lambda: Arc(
                    radius=sequence[i] / 5, 
                    arc_center=squares[i].get_corner(corners[i % 4]), 
                    color=TEXT_COLOR, 
                    start_angle=angles[i % 4], 
                    angle=arc_angle.get_value()
                )
            )
            dot = always_redraw(
                lambda: Dot(radius=0.05, color=TEXT_COLOR)
                    .move_to(arc.get_end())
            )

            self.add(arc, dot)
            self.play(
                arc_angle.animate.set_value(PI / 2), 
                rate_func=linear, 
                run_time=max(0.3, sequence[i] / 34)
            )
            arc.clear_updaters()
        
        self.wait(0.5)
        self.play(*[FadeOut(mobject) for mobject in self.mobjects[:19]], FadeOut(dot))
        self.wait(1.5)
        self.play(FadeOut(Group(*self.mobjects)))