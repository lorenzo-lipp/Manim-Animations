from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        inner_pentagon = RegularPolygon(5, fill_opacity=1, color=G_PURPLE)
        inner_pentagon.scale(2)
        inner_pentagon.move_to(ORIGIN + 0.1 * DOWN)
        inner_points = inner_pentagon.get_vertex_groups()[0]
        inner_circles = VGroup(
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((inner_points[0] + inner_points[1] + 0.55 * DOWN + 0.5 * RIGHT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((inner_points[1] + inner_points[2] + 0.25 * UP + 0.8 * RIGHT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((inner_points[2] + inner_points[3] + 0.8 * UP) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((inner_points[3] + inner_points[4] + 0.25 * UP + 0.8 * LEFT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((inner_points[4] + inner_points[0] + 0.55 * DOWN + 0.5 * LEFT) / 2)
        )
        inner_numbers = always_redraw(lambda: VGroup(
            Tex("4", color=BLACK)
                .move_to(inner_circles[0]),
            Tex("5", color=BLACK)
                .move_to(inner_circles[1]),
            Tex("8", color=BLACK)
                .move_to(inner_circles[2]),
            Tex("7", color=BLACK)
                .move_to(inner_circles[3]),
            Tex("2", color=BLACK)
                .move_to(inner_circles[4])
        ))
        middle_pentagon = RegularPolygon(5, fill_opacity=1, color=G_BLUE)
        middle_pentagon.scale(3)
        middle_pentagon.move_to(ORIGIN + 0.05 * DOWN)
        middle_points = middle_pentagon.get_vertex_groups()[0]
        middle_circles = VGroup(
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((middle_points[0] + middle_points[1] + 0.55 * DOWN + 0.5 * RIGHT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((middle_points[1] + middle_points[2] + 0.25 * UP + 0.8 * RIGHT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((middle_points[2] + middle_points[3] + 0.8 * UP) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((middle_points[3] + middle_points[4] + 0.25 * UP + 0.8 * LEFT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((middle_points[4] + middle_points[0] + 0.55 * DOWN + 0.5 * LEFT) / 2)
        )
        middle_numbers = always_redraw(lambda: VGroup(
            Tex("10", color=BLACK)
                .move_to(middle_circles[0]),
            Tex("8", color=BLACK)
                .move_to(middle_circles[1]),
            Tex("10", color=BLACK)
                .move_to(middle_circles[2]),
            Tex("6", color=BLACK)
                .move_to(middle_circles[3]),
            Tex("11", color=BLACK)
                .move_to(middle_circles[4])
        ))
        outer_pentagon = RegularPolygon(5, fill_opacity=1, color=G_PINK)
        outer_pentagon.scale(4)
        outer_pentagon.move_to(ORIGIN)
        outer_points = outer_pentagon.get_vertex_groups()[0]
        outer_circles = VGroup(
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((outer_points[0] + outer_points[1] + 0.55 * DOWN + 0.5 * RIGHT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((outer_points[1] + outer_points[2] + 0.25 * UP + 0.8 * RIGHT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((outer_points[2] + outer_points[3] + 0.8 * UP) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((outer_points[3] + outer_points[4] + 0.25 * UP + 0.8 * LEFT) / 2),
            Circle(0.3, color=WHITE, fill_opacity=1)
                .move_to((outer_points[4] + outer_points[0] + 0.55 * DOWN + 0.5 * LEFT) / 2)
        )
        outer_numbers = always_redraw(lambda: VGroup(
            Tex("18", color=BLACK)
                .move_to(outer_circles[0]),
            Tex("20", color=BLACK)
                .move_to(outer_circles[1]),
            Tex("14", color=BLACK)
                .move_to(outer_circles[2]),
            Tex("12", color=BLACK)
                .move_to(outer_circles[3]),
            Tex("15", color=BLACK)
                .move_to(outer_circles[4])
        ))
        outer_piece = VGroup(outer_pentagon, outer_circles, outer_numbers)
        middle_piece = VGroup(middle_pentagon, middle_circles, middle_numbers)
        inner_piece = VGroup(inner_pentagon, inner_circles, inner_numbers)
        ellipse = Ellipse(2, 1, color=LIGHT_RED_COLOR)
        ellipse.surround(Group(outer_numbers[3], inner_numbers[3])).rotate(-22 * DEGREES)

        self.play(AnimateFromLeft(outer_piece, middle_piece, inner_piece), run_time=0.7)
        self.wait(2)
        RotatePiece(self, inner_piece, center_of_mass(inner_points))
        self.wait(2)
        RotatePiece(self, middle_piece, center_of_mass(middle_points))
        self.play(Write(ellipse), run_time=0.7)
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)