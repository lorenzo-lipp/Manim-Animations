from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class TriangleArea(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        SHIFT_DIST = 1.75
        rectangle = Rectangle(height=2, width=3, fill_opacity=0.6, color=LIGHT_GREEN_COLOR)
        rectangle.shift(SHIFT_DIST * UP)
        rectangle_base_text = Tex("3m", color=LIGHT_GREEN_COLOR)
        rectangle_base_text.next_to(rectangle, DOWN)
        rectangle_height_text = Tex("2m", color=LIGHT_GREEN_COLOR)
        rectangle_height_text.rotate(-90 * DEGREES)
        rectangle_height_text.next_to(rectangle, RIGHT)

        self.play(
            LaggedStart(
                SpinInFromNothing(rectangle),
                Write(rectangle_base_text),
                Write(rectangle_height_text),
                lag_ratio=0.3
            )
        )
        self.wait(1.6)

        formula = Tex("Área = Base x Altura", color=LIGHT_PURPLE_COLOR)
        formula.scale(1.2)
        formula.shift((SHIFT_DIST - 0.5) * DOWN)
        formula_bottom = Tex("2", color=LIGHT_PURPLE_COLOR)
        formula_bottom.scale(1.2)
        formula_bottom.shift((SHIFT_DIST) * DOWN + RIGHT)

        self.play(Write(formula))
        self.wait(0.5)

        rectangle_div = Line(
            [rectangle.get_right()[0], rectangle.get_top()[1], 0],
            [rectangle.get_left()[0], rectangle.get_bottom()[1], 0],
            color=LIGHT_GREEN_COLOR
        )
        formula_line = Line(
            (SHIFT_DIST - 0.5) * DOWN + 0.6 * LEFT,
            (SHIFT_DIST - 0.5) * DOWN + 2.8 * RIGHT,
            color=LIGHT_PURPLE_COLOR
        )

        self.play(Write(rectangle_div, run_time=0.6))
        self.wait(0.5)
        self.play(formula[0][6:].animate.shift(0.5 * UP))
        self.play(Write(formula_line))
        self.play(Write(formula_bottom))
        self.wait(1)
        self.play(FadeOut(Group(rectangle, rectangle_div, rectangle_base_text, rectangle_height_text)))

        triangle = Polygon(
            LEFT * 6 + DOWN * 4,
            RIGHT * 6 + DOWN * 4,
            UP * 4,
            color=LIGHT_ORANGE_COLOR,
            fill_opacity=0.5
        )
        triangle.scale(0.3)
        triangle.shift(2 * UP)
        triangle_base_text = Tex("12m", color=LIGHT_ORANGE_COLOR)
        triangle_base_text.next_to(triangle, DOWN)
        triangle_right_text = Tex("10m", color=LIGHT_ORANGE_COLOR)
        triangle_right_text.next_to(triangle, RIGHT)
        triangle_right_text.shift(0.8 * LEFT + 0.2 * UP)
        triangle_left_text = Tex("10m", color=LIGHT_ORANGE_COLOR)
        triangle_left_text.next_to(triangle, LEFT)
        triangle_left_text.shift(0.8 * RIGHT + 0.2 * UP)
        triangle_div = DashedLine(
            [triangle.get_center()[0], triangle.get_top()[1], 0],
            [triangle.get_center()[0], triangle.get_bottom()[1], 0],
            color=LIGHT_ORANGE_COLOR,
            dash_length=0.1
        )
        triangle_height_text = Tex("8m", color=LIGHT_ORANGE_COLOR)
        triangle_height_text.next_to(triangle_div, RIGHT)
        triangle_height_text.shift(0.1 * LEFT + 0.2 * DOWN)

        self.play(DrawBorderThenFill(triangle))
        self.play(Write(
            VGroup(
                triangle_base_text,
                triangle_right_text,
                triangle_left_text
            )
        ))
        self.play(Write(triangle_div), run_time=0.7)
        self.wait(0.5)
        self.play(Write(triangle_height_text))
        self.wait(1)

        formula_solving = Group(
                formula,
                formula_line,
                formula_bottom
        ).copy()
        
        self.play(formula_solving.animate.shift(2 * DOWN))
        self.play(
            LaggedStart(
                triangle_base_text.copy().animate.scale(1.2).move_to(formula_solving[0][0][6:10].get_center()),
                Transform(formula_solving[0][0][6:10], triangle_base_text.copy().scale(1.2).move_to(formula_solving[0][0][6:10].get_center())),
                lag_ratio=0.3,
                run_time=1
            )
        )
        self.wait(1)
        self.play(
            LaggedStart(
                triangle_height_text.copy().animate.scale(1.2).move_to(formula_solving[0][0][11:].get_center()),
                Transform(formula_solving[0][0][11:], triangle_height_text.copy().scale(1.2).move_to(formula_solving[0][0][11:].get_center())),
                lag_ratio=0.3,
                run_time=1
            )
        )
        self.wait(1)

        formula_result = Tex("Área = $48m^2$", color=LIGHT_PURPLE_COLOR, tex_to_color_map={"$48m^2$": LIGHT_ORANGE_COLOR})
        formula_result.scale(1.2)
        formula_result.shift((SHIFT_DIST + 3) * DOWN)

        self.play(Write(formula_result))
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))
        self.remove(*self.mobjects)