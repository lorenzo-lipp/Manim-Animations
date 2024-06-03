from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Triangles(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        triangles = VGroup(
            Triangle(color=LIGHT_GREEN_COLOR, fill_opacity=0.8),
            Polygon(LEFT, DOWN, RIGHT, color=LIGHT_PINK, fill_opacity=0.8),
            Polygon(0.8 * DOWN + LEFT, 0.8 * DOWN + RIGHT, UP + 0.5 * RIGHT, color=LIGHT_BLUE_COLOR, fill_opacity=0.8),
            Polygon(0.8 * DOWN + LEFT, 0.8 * DOWN + 0.5 * RIGHT, UP + RIGHT, color=LIGHT_PURPLE_COLOR, fill_opacity=0.8)
        ).arrange(DOWN, buff=1.2)
        top_edges = VGroup(
            Line(triangles[0].get_all_points()[0], triangles[0].get_all_points()[3], color=BLACK),
            Line(triangles[1].get_all_points()[7], triangles[1].get_all_points()[11], color=BLACK),
            Line(triangles[2].get_all_points()[7], triangles[2].get_all_points()[11], color=BLACK),
            Line(triangles[3].get_all_points()[7], triangles[3].get_all_points()[11], color=BLACK)
        )
        right_edges = VGroup(
            Line(triangles[0].get_all_points()[7], triangles[0].get_all_points()[11], color=BLACK),
            Line(triangles[1].get_all_points()[3], triangles[1].get_all_points()[7], color=BLACK),
            Line(triangles[2].get_all_points()[3], triangles[2].get_all_points()[7], color=BLACK),
            Line(triangles[3].get_all_points()[3], triangles[3].get_all_points()[7], color=BLACK)
        )
        bottom_edges = VGroup(
            Line(triangles[0].get_all_points()[3], triangles[0].get_all_points()[7], color=BLACK),
            Line(triangles[1].get_all_points()[0], triangles[1].get_all_points()[3], color=BLACK),
            Line(triangles[2].get_all_points()[0], triangles[2].get_all_points()[3], color=BLACK),
            Line(triangles[3].get_all_points()[0], triangles[3].get_all_points()[3], color=BLACK)
        )
        angles = VGroup()
        for triangle in triangles:
            angles.add(Line(triangle.get_all_points()[0], triangle.get_all_points()[1], color=BLACK))
            angles.add(Line(triangle.get_all_points()[2], triangle.get_all_points()[3], color=BLACK))
            angles.add(Line(triangle.get_all_points()[4], triangle.get_all_points()[5], color=BLACK))
            angles.add(Line(triangle.get_all_points()[6], triangle.get_all_points()[7], color=BLACK))
            angles.add(Line(triangle.get_all_points()[8], triangle.get_all_points()[9], color=BLACK))
            angles.add(Line(triangle.get_all_points()[10], triangle.get_all_points()[11], color=BLACK))

        self.play(DrawBorderThenFill(triangles))
        self.wait(1)
        self.play(FadeIn(top_edges))
        self.wait(0.3)
        self.play(Transform(top_edges, right_edges))
        self.wait(0.3)
        self.play(Transform(top_edges, bottom_edges))
        self.wait(0.5)
        self.play(FadeOut(top_edges))
        self.wait(0.5)
        self.play(FadeIn(angles))
        self.wait(1.5)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)