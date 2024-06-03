from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Quadrilateral(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        quadrilaterals = VGroup(
            Rectangle(LIGHT_GREEN_COLOR, 1, 2, fill_opacity=0.8),
            Polygon(LEFT, DOWN, RIGHT, UP, color=LIGHT_PINK, fill_opacity=0.8),
            Polygon(0.8 * DOWN + LEFT, 0.8 * DOWN + RIGHT, UP + 0.5 * RIGHT, UP + 0.5 * LEFT, color=LIGHT_BLUE_COLOR, fill_opacity=0.8),
            Polygon(0.8 * DOWN + LEFT, 0.8 * DOWN + 0.5 * RIGHT, UP + RIGHT, UP + 0.5 * LEFT, color=LIGHT_PURPLE_COLOR, fill_opacity=0.8)
        ).arrange(DOWN, buff=1.2)
        top_edges = VGroup(
            Line(quadrilaterals[0].get_all_points()[0], quadrilaterals[0].get_all_points()[3], color=BLACK),
            Line(quadrilaterals[1].get_all_points()[11], quadrilaterals[1].get_all_points()[15], color=BLACK),
            Line(quadrilaterals[2].get_all_points()[7], quadrilaterals[2].get_all_points()[11], color=BLACK),
            Line(quadrilaterals[3].get_all_points()[7], quadrilaterals[3].get_all_points()[11], color=BLACK)
        )
        right_edges = VGroup(
            Line(quadrilaterals[0].get_all_points()[11], quadrilaterals[0].get_all_points()[15], color=BLACK),
            Line(quadrilaterals[1].get_all_points()[7], quadrilaterals[1].get_all_points()[11], color=BLACK),
            Line(quadrilaterals[2].get_all_points()[3], quadrilaterals[2].get_all_points()[7], color=BLACK),
            Line(quadrilaterals[3].get_all_points()[3], quadrilaterals[3].get_all_points()[7], color=BLACK)
        )
        bottom_edges = VGroup(
            Line(quadrilaterals[0].get_all_points()[7], quadrilaterals[0].get_all_points()[11], color=BLACK),
            Line(quadrilaterals[1].get_all_points()[3], quadrilaterals[1].get_all_points()[7], color=BLACK),
            Line(quadrilaterals[2].get_all_points()[0], quadrilaterals[2].get_all_points()[3], color=BLACK),
            Line(quadrilaterals[3].get_all_points()[0], quadrilaterals[3].get_all_points()[3], color=BLACK)
        )
        left_edges = VGroup(
            Line(quadrilaterals[0].get_all_points()[3], quadrilaterals[0].get_all_points()[7], color=BLACK),
            Line(quadrilaterals[1].get_all_points()[0], quadrilaterals[1].get_all_points()[3], color=BLACK),
            Line(quadrilaterals[2].get_all_points()[11], quadrilaterals[2].get_all_points()[15], color=BLACK),
            Line(quadrilaterals[3].get_all_points()[11], quadrilaterals[3].get_all_points()[15], color=BLACK)
        )
        angles = VGroup()
        for quadrilateral in quadrilaterals:
            angles.add(Line(quadrilateral.get_all_points()[0], quadrilateral.get_all_points()[1], color=BLACK))
            angles.add(Line(quadrilateral.get_all_points()[14], quadrilateral.get_all_points()[15], color=BLACK))
            angles.add(Line(quadrilateral.get_all_points()[2], quadrilateral.get_all_points()[3], color=BLACK))
            angles.add(Line(quadrilateral.get_all_points()[4], quadrilateral.get_all_points()[5], color=BLACK))
            angles.add(Line(quadrilateral.get_all_points()[6], quadrilateral.get_all_points()[7], color=BLACK))
            angles.add(Line(quadrilateral.get_all_points()[8], quadrilateral.get_all_points()[9], color=BLACK))
            angles.add(Line(quadrilateral.get_all_points()[10], quadrilateral.get_all_points()[11], color=BLACK))
            angles.add(Line(quadrilateral.get_all_points()[12], quadrilateral.get_all_points()[13], color=BLACK))

        self.play(DrawBorderThenFill(quadrilaterals))
        self.wait(1)
        self.play(FadeIn(top_edges))
        self.wait(0.3)
        self.play(Transform(top_edges, right_edges))
        self.wait(0.3)
        self.play(Transform(top_edges, bottom_edges))
        self.wait(0.3)
        self.play(Transform(top_edges, left_edges))
        self.wait(0.3)
        self.play(FadeOut(top_edges))
        self.wait(0.5)
        self.play(FadeIn(angles))
        self.wait(1.4)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)