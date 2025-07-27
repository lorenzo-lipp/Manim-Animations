from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SquareArea(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        square = Square(1, fill_opacity=0.8, color=LIGHT_BLUE_COLOR)
        square_base_text = Tex("1cm", color=LIGHT_BLUE_COLOR)
        square_base_text.next_to(square, DOWN)
        square_height_text = Tex("1cm", color=LIGHT_BLUE_COLOR)
        square_height_text.rotate(-90 * DEGREES)
        square_height_text.next_to(square, RIGHT)
        square_gp = Group(square, square_base_text, square_height_text)
        big_square = Square(3, fill_opacity=0.8, color=LIGHT_PURPLE_COLOR)
        big_square.shift(2 * UP)
        big_square_base_text = Tex("3cm", color=LIGHT_PURPLE_COLOR)
        big_square_base_text.next_to(big_square, DOWN)
        big_square_height_text = Tex("3cm", color=LIGHT_PURPLE_COLOR)
        big_square_height_text.rotate(-90 * DEGREES)
        big_square_height_text.next_to(big_square, RIGHT)

        self.play(DrawBorderThenFill(square), run_time=0.7)
        self.wait(0.5)
        self.play(
            LaggedStart(
                Write(square_base_text),
                Write(square_height_text),
                lag_ratio=0.3
            )
        )
        self.wait(0.5)
        self.play(
            LaggedStart(
                square_gp.animate.shift(2 * DOWN),
                DrawBorderThenFill(big_square),
                Write(big_square_base_text),
                Write(big_square_height_text),
                lag_ratio=0.3
            )
        )
        self.wait(1)
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(
                        square, 
                        Square(1, fill_opacity=0, color=LIGHT_PURPLE_COLOR)
                            .move_to(square)
                            .shift(square_pos(3, i)
                        )
                    ) for i in range(0, 9)
                ],
                lag_ratio=0.8
            )
        )
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)