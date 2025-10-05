from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ParallelogramArea(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        SHIFT_DIST = 1.75
        rectangle = Rectangle(height=2, width=3, fill_opacity=0.5, color=LIGHT_GREEN_COLOR)
        rectangle.shift(SHIFT_DIST * UP)
        rectangle_base_text = Tex("3m", color=LIGHT_GREEN_COLOR)
        rectangle_base_text.next_to(rectangle, DOWN)
        rectangle_height_text = Tex("2m", color=LIGHT_GREEN_COLOR)
        rectangle_height_text.rotate(90 * DEGREES)
        rectangle_height_text.next_to(rectangle, RIGHT)
        rectangle_points = rectangle.get_points_defining_boundary()
        parallelogram = Polygram(
            [
                rectangle_points[0] + 0.5 * RIGHT,
                rectangle_points[2] + 0.5 * RIGHT,
                rectangle_points[4] + 0.5 * LEFT,
                rectangle_points[6] + 0.5 * LEFT,
            ],
            fill_opacity=0.5,
            color=LIGHT_GREEN_COLOR
        )
        parallelogram_lateral_text = Tex("2,06m", color=LIGHT_GREEN_COLOR)
        parallelogram_lateral_text.rotate(65 * DEGREES)
        parallelogram_lateral_text.next_to(rectangle, RIGHT)
        parallelogram_lateral_text.shift(0.2 * LEFT)
        parallelogram_base_text = Tex("3m", color=LIGHT_GREEN_COLOR)
        parallelogram_base_text.next_to(rectangle, DOWN)
        parallelogram_base_text.shift(0.5 * LEFT)
        parallelogram_div = DashedLine(
            [parallelogram.get_center()[0] + 1, parallelogram.get_top()[1], 0],
            [parallelogram.get_center()[0] + 1, parallelogram.get_bottom()[1], 0],
            color=LIGHT_GREEN_COLOR,
            dash_length=0.1
        )
        parallelogram_div_text = Tex("2m", color=LIGHT_GREEN_COLOR)
        parallelogram_div_text.next_to(parallelogram_div, LEFT)

        self.play(
            LaggedStart(
                SpinInFromNothing(parallelogram),
                Write(parallelogram_base_text),
                Write(parallelogram_lateral_text),
                lag_ratio=0.3
            )
        )
        self.wait(1)
        self.play(Write(parallelogram_div, run_time=0.7))
        self.play(Write(parallelogram_div_text, run_time=0.8))
        self.wait(2)

        formula = Tex("Área = Base x Altura", color=LIGHT_PURPLE_COLOR)
        formula.scale(1.2)
        formula.shift((SHIFT_DIST - 0.5) * DOWN)
        formula_bottom = Tex("2", color=LIGHT_PURPLE_COLOR)
        formula_bottom.scale(1.2)
        formula_bottom.shift((SHIFT_DIST) * DOWN + RIGHT)

        formula_solving = Tex("Área = Base x Altura", color=LIGHT_PURPLE_COLOR)
        formula_solving.scale(1.2)
        formula_solving.shift((SHIFT_DIST + 0.5) * DOWN)
        formula_width = formula_solving[0][6:10]
        formula_height = formula_solving[0][11:]

        formula_result = Tex("Área = $6m^2$", color=LIGHT_PURPLE_COLOR, tex_to_color_map={"$6m^2$": LIGHT_GREEN_COLOR})
        formula_result.scale(1.2)
        formula_result.shift((SHIFT_DIST + 1.5) * DOWN)

        width_line = VGroup(
            Line(2 * LEFT + (SHIFT_DIST - 1) * UP, 1 * RIGHT + (SHIFT_DIST - 1) * UP, color=LIGHT_PURPLE_COLOR),
            Line(2 * LEFT + (SHIFT_DIST - 0.85) * UP, 2 * LEFT + (SHIFT_DIST - 1.15) * UP, color=LIGHT_PURPLE_COLOR),
            Line(1 * RIGHT + (SHIFT_DIST - 0.85) * UP, 1 * RIGHT + (SHIFT_DIST - 1.15) * UP, color=LIGHT_PURPLE_COLOR),
        )
        height_line = VGroup(
            Line(1 * RIGHT + (SHIFT_DIST - 1) * UP, 1 * RIGHT + (SHIFT_DIST + 1) * UP, color=LIGHT_PURPLE_COLOR),
            Line(0.85 * RIGHT + (SHIFT_DIST - 1) * UP, 1.15 * RIGHT + (SHIFT_DIST - 1) * UP, color=LIGHT_PURPLE_COLOR),
            Line(0.85 * RIGHT + (SHIFT_DIST + 1) * UP, 1.15 * RIGHT + (SHIFT_DIST + 1) * UP, color=LIGHT_PURPLE_COLOR),
        )

        self.play(Write(formula))
        self.play(TransformFromCopy(formula, formula_solving), run_time=0.7)
        self.play(FadeIn(width_line), run_time=0.7)
        self.play(Indicate(width_line, color=LIGHT_RED_COLOR), run_time=0.7)
        self.play(
            LaggedStart(
                parallelogram_base_text.copy().animate.scale(1.2).move_to(formula_width.get_center()),
                Transform(formula_width, parallelogram_base_text.copy().scale(1.2).move_to(formula_width.get_center())),
                lag_ratio=0.3,
                run_time=0.7
            )
        )
        self.play(FadeOut(width_line), run_time=0.7)
        self.play(FadeIn(height_line), run_time=0.7)
        self.play(Indicate(height_line, color=LIGHT_RED_COLOR), run_time=0.7)
        self.play(
            LaggedStart(
                parallelogram_div_text.copy().animate.scale(1.2).move_to(formula_height.get_center()),
                Transform(formula_height, parallelogram_div_text.copy().scale(1.2).move_to(formula_height.get_center())),
                lag_ratio=0.3,
                run_time=0.7
            )
        )
        self.remove(self.mobjects[-1][0])
        self.play(FadeOut(height_line), run_time=0.7)
        self.play(TransformFromCopy(formula_solving, formula_result), run_time=0.7)

        new_rectangle = Polygram(
            [
                rectangle_points[0] + 0.5 * LEFT,
                rectangle_points[2] + 0.5 * RIGHT,
                rectangle_points[4] + 0.5 * LEFT,
                rectangle_points[6] + 0.5 * LEFT,
            ],
            fill_opacity=0.5, 
            color=LIGHT_GREEN_COLOR
        )
        right_triangle = Polygram(
            [
                rectangle_points[0] + 0.5 * LEFT,
                rectangle_points[0] + 0.5 * RIGHT,
                rectangle_points[6] + 0.5 * LEFT,
            ],
            fill_opacity=0.5, 
            color=LIGHT_GREEN_COLOR
        )
        right_triangle.round_corners(0.005)

        self.remove(parallelogram)
        self.add(new_rectangle, right_triangle)
        self.play(FadeOut(parallelogram_lateral_text))
        self.wait(0.5)
        self.play(right_triangle.animate.shift(3 * LEFT))
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
        self.remove(*self.mobjects)