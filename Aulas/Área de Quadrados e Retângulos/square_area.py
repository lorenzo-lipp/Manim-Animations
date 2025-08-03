from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SquareArea(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        SHIFT_DIST = 1.75
        square = Square(1, fill_opacity=0.8, color=LIGHT_BLUE_COLOR)
        square_base_text = Tex("1cm", color=LIGHT_BLUE_COLOR)
        square_base_text.next_to(square, DOWN)
        square_height_text = Tex("1cm", color=LIGHT_BLUE_COLOR)
        square_height_text.rotate(-90 * DEGREES)
        square_height_text.next_to(square, RIGHT)
        square_gp = Group(square, square_base_text, square_height_text)
        rectangle = Rectangle(height=2, width=3, fill_opacity=0.8, color=LIGHT_GREEN_COLOR)
        rectangle.shift(SHIFT_DIST * UP)
        rectangle_base_text = Tex("3m", color=LIGHT_GREEN_COLOR)
        rectangle_base_text.next_to(rectangle, DOWN)
        rectangle_height_text = Tex("2m", color=LIGHT_GREEN_COLOR)
        rectangle_height_text.rotate(-90 * DEGREES)
        rectangle_height_text.next_to(rectangle, RIGHT)
        new_rectangle = Rectangle(height=3, width=3, fill_opacity=0.8, color=LIGHT_RED_COLOR)
        new_rectangle.shift((SHIFT_DIST + 0.5) * UP)
        new_rectangle_height_text = Tex("3cm", color=LIGHT_RED_COLOR)
        new_rectangle_height_text.rotate(-90 * DEGREES)
        new_rectangle_height_text.next_to(new_rectangle, RIGHT)
        new_rectangle_base_text = Tex("3cm", color=LIGHT_RED_COLOR)
        new_rectangle_base_text.next_to(new_rectangle, DOWN)

        self.add(rectangle, rectangle_base_text, rectangle_height_text)
        self.play(
            Transform(rectangle, new_rectangle),
            Transform(rectangle_height_text, new_rectangle_height_text),
            Transform(rectangle_base_text, new_rectangle_base_text),
        )
        self.wait(1)

        formula = Tex("Área = Base x Altura", color=LIGHT_PURPLE_COLOR)
        formula.scale(1.2)
        formula.shift((SHIFT_DIST - 0.5) * DOWN)
        new_formula = Tex("Área = Lado x Lado", color=LIGHT_PURPLE_COLOR)
        new_formula.scale(1.2)
        new_formula.shift((SHIFT_DIST - 0.5) * DOWN)
        formula_solving = Tex("Área = 3cm x 3cm", color=LIGHT_PURPLE_COLOR, tex_to_color_map={"3cm": LIGHT_RED_COLOR})
        formula_solving.scale(1.2)
        formula_solving.shift((SHIFT_DIST + 0.5) * DOWN)
        formula_result = Tex("Área = $9cm^2$", color=LIGHT_PURPLE_COLOR, tex_to_color_map={"$9cm^2$": LIGHT_RED_COLOR})
        formula_result.scale(1.2)
        formula_result.shift((SHIFT_DIST + 1.5) * DOWN)

        self.play(Write(formula))
        self.wait(1)
        self.play(Transform(formula[0][6:], new_formula[0][6:]))
        self.wait(0.5)

        formula_copy = formula.copy()
        width_line = VGroup(
            Line(1.5 * LEFT + (SHIFT_DIST - 1) * UP, 1.5 * RIGHT + (SHIFT_DIST - 1) * UP, color=LIGHT_PURPLE_COLOR),
            Line(1.5 * LEFT + (SHIFT_DIST - 0.85) * UP, 1.5 * LEFT + (SHIFT_DIST - 1.15) * UP, color=LIGHT_PURPLE_COLOR),
            Line(1.5 * RIGHT + (SHIFT_DIST - 0.85) * UP, 1.5 * RIGHT + (SHIFT_DIST - 1.15) * UP, color=LIGHT_PURPLE_COLOR),
        )

        self.play(FadeIn(width_line), run_time=0.7)
        self.play(Indicate(width_line, color=LIGHT_BLUE_COLOR))
        self.play(FadeOut(width_line), run_time=0.7)
        self.play(Transform(formula_copy, formula_solving))
        self.wait(1)
        self.play(TransformFromCopy(formula_copy, formula_result))
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)