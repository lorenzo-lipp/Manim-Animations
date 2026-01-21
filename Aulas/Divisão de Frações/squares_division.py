from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SquaresDivision(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        SQUARE_WIDTH = 3

        frac = MathTex(r"\frac{2}{5} \div \frac{3}{2} = \frac{2}{5}\,\times \frac{2}{3} = \frac{4}{15}", 
                       tex_to_color_map={
                           r"\frac{2}{5}\,": LIGHT_BLUE_COLOR,
                           r"\frac{2}{3}": LIGHT_RED_COLOR,
                           r"\frac{4}{15}": LIGHT_PURPLE_COLOR
                        },
                        color=BLACK
                )
        square_1 = VGroup(
            *[
                Rectangle(
                    stroke_color=BLACK, 
                    height=SQUARE_WIDTH/5, 
                    width=SQUARE_WIDTH, 
                    fill_color=LIGHT_BLUE_COLOR, 
                    fill_opacity=0.5 if i < 2 else 0
                ) for i in range(5)
            ]
        ).arrange(DOWN, buff=0)
        square_2 = VGroup(
            *[
                Rectangle(
                    stroke_color=BLACK, 
                    height=SQUARE_WIDTH, 
                    width=SQUARE_WIDTH/3, 
                    fill_color=LIGHT_RED_COLOR, 
                    fill_opacity=0.5 if i < 2 else 0
                ) for i in range(3)
            ]
        ).arrange(RIGHT, buff=0)
        mult = MathTex(r"\times", color=BLACK)

        top_row = VGroup(Square(SQUARE_WIDTH - 0.5, stroke_opacity=0), frac)
        middle_row = VGroup(square_1, mult, square_2).arrange(buff=0.5)
        bottom_row = VGroup(Square(SQUARE_WIDTH, stroke_opacity=0))
        Group(top_row, middle_row, bottom_row).arrange(DOWN, 1)

        self.play(Write(frac[0:5]))
        self.play(TransformFromCopy(frac[1], square_1), run_time=1.2)
        self.play(TransformFromCopy(frac[2], mult), run_time=0.7)
        self.play(TransformFromCopy(frac[3], square_2), run_time=1.2)
        self.wait(0.5)
        self.play(square_2.copy().animate.move_to(bottom_row[0]))
        self.play(square_1.copy().animate.move_to(bottom_row[0]))
        self.wait(1)
        self.play(Transform(
            Rectangle(
                color=LIGHT_PURPLE_COLOR, 
                height=2 * SQUARE_WIDTH/5,
                width=2 * SQUARE_WIDTH/3
            ).align_to(bottom_row, UL), 
            frac[5][0:2]
        ))
        self.wait(0.5)
        self.play(Transform(
            Rectangle(
                color=BLACK, 
                height=SQUARE_WIDTH,
                width=SQUARE_WIDTH,
                fill_opacity=0
            ).align_to(bottom_row, UL), 
            frac[5][2:]
        ))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)