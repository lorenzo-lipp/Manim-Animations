from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class RectangleArea(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        SHIFT_DIST = 1.75
        square = Square(1, fill_opacity=0.8, color=LIGHT_BLUE_COLOR)
        square_base_text = Tex("1m", color=LIGHT_BLUE_COLOR)
        square_base_text.next_to(square, DOWN)
        square_height_text = Tex("1m", color=LIGHT_BLUE_COLOR)
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

        self.play(
            LaggedStart(
                DrawBorderThenFill(square),
                Write(square_base_text),
                Write(square_height_text),
                lag_ratio=0.3
            )
        )
        self.wait(0.5)
        self.play(
            LaggedStart(
                square_gp.animate.shift(SHIFT_DIST * DOWN),
                SpinInFromNothing(rectangle),
                Write(rectangle_base_text),
                Write(rectangle_height_text),
                lag_ratio=0.3
            )
        )
        self.wait(1)
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(
                        square, 
                        Square(1, fill_opacity=0, color=LIGHT_GREEN_COLOR)
                            .move_to(square)
                            .shift(square_pos(3, i)
                        ),
                        run_time=0.7
                    ) for i in range(0, 6)
                ],
                lag_ratio=0.8
            )
        )
        self.wait(1)
        self.play(FadeOut(square_gp))

        formula = Tex("Área = Base x Altura", color=LIGHT_PURPLE_COLOR)
        formula.scale(1.2)
        formula.shift((SHIFT_DIST - 0.5) * DOWN)
        formula_solving = Tex("Área = Base x Altura", color=LIGHT_PURPLE_COLOR)
        formula_solving.scale(1.2)
        formula_solving.shift((SHIFT_DIST + 0.5) * DOWN)
        formula_width = formula_solving[0][6:10]
        formula_height = formula_solving[0][11:]
        formula_result = Tex("Área = $6m^2$", color=LIGHT_PURPLE_COLOR, tex_to_color_map={"$6m^2$": LIGHT_GREEN_COLOR})
        formula_result.scale(1.2)
        formula_result.shift((SHIFT_DIST + 1.5) * DOWN)
        new_rectangle = Rectangle(height=3, width=3, fill_opacity=0.8, color=LIGHT_GREEN_COLOR)
        new_rectangle.shift((SHIFT_DIST + 0.5) * UP)
        new_rectangle_height_text = Tex("3m", color=LIGHT_GREEN_COLOR)
        new_rectangle_height_text.rotate(-90 * DEGREES)
        new_rectangle_height_text.next_to(new_rectangle, RIGHT)
        width_line = VGroup(
            Line(1.5 * LEFT + (SHIFT_DIST - 1) * UP, 1.5 * RIGHT + (SHIFT_DIST - 1) * UP, color=LIGHT_PURPLE_COLOR),
            Line(1.5 * LEFT + (SHIFT_DIST - 0.85) * UP, 1.5 * LEFT + (SHIFT_DIST - 1.15) * UP, color=LIGHT_PURPLE_COLOR),
            Line(1.5 * RIGHT + (SHIFT_DIST - 0.85) * UP, 1.5 * RIGHT + (SHIFT_DIST - 1.15) * UP, color=LIGHT_PURPLE_COLOR),
        )
        height_line = VGroup(
            Line(1.5 * RIGHT + (SHIFT_DIST - 1) * UP, 1.5 * RIGHT + (SHIFT_DIST + 1) * UP, color=LIGHT_PURPLE_COLOR),
            Line(1.35 * RIGHT + (SHIFT_DIST - 1) * UP, 1.65 * RIGHT + (SHIFT_DIST - 1) * UP, color=LIGHT_PURPLE_COLOR),
            Line(1.35 * RIGHT + (SHIFT_DIST + 1) * UP, 1.65 * RIGHT + (SHIFT_DIST + 1) * UP, color=LIGHT_PURPLE_COLOR),
        )

        self.play(Write(formula))
        self.wait(0.5)
        self.play(TransformFromCopy(formula, formula_solving))
        self.play(FadeIn(width_line), run_time=0.7)
        self.play(Indicate(width_line, color=LIGHT_RED_COLOR))
        self.play(
            LaggedStart(
                rectangle_base_text.copy().animate.scale(1.2).move_to(formula_width.get_center()),
                Transform(formula_width, rectangle_base_text.copy().scale(1.2).move_to(formula_width.get_center())),
                lag_ratio=0.3,
                run_time=1
            )
        )
        self.play(FadeOut(width_line), run_time=0.7)
        self.play(FadeIn(height_line), run_time=0.7)
        self.play(Indicate(height_line, color=LIGHT_RED_COLOR))
        self.play(
            LaggedStart(
                rectangle_height_text.copy().animate.rotate(90 * DEGREES).scale(1.2).move_to(formula_height.get_center()),
                Transform(formula_height, rectangle_height_text.copy().rotate(90 * DEGREES).scale(1.2).move_to(formula_height.get_center())),
                lag_ratio=0.3,
                run_time=1
            )
        )
        self.remove(self.mobjects[-1][0])
        self.play(FadeOut(height_line), run_time=0.7)
        self.play(TransformFromCopy(formula_solving, formula_result), run_time=0.7)
        self.wait(1)
        self.play(
            Transform(rectangle, new_rectangle),
            Transform(rectangle_height_text, new_rectangle_height_text),
        )
        self.play(
            Transform(formula_height, Tex("3m", color=LIGHT_GREEN_COLOR).scale(1.2).move_to(formula_height)),
            Transform(formula_result[1][0], SingleStringMathTex("9", color=LIGHT_GREEN_COLOR).scale(1.2).move_to(formula_result[1][0])),
            run_time=0.7
        )
        self.play(
            Indicate(formula_height, color=LIGHT_RED_COLOR),
            Indicate(formula_result[1], color=LIGHT_RED_COLOR)
        )
        self.play(
            LaggedStart(
                *[
                    SpinInFromNothing(
                        Square(1, fill_opacity=0, color=LIGHT_GREEN_COLOR)
                            .move_to(square)
                            .shift(square_pos(3, i)
                        ),
                        run_time=0.7
                    ) for i in range(6, 9)
                ],
                lag_ratio=0.6
            )
        )
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)