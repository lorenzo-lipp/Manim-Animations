from manim import *

BACKGROUND_COLOR = "#faf4e1"
TEXT_COLOR = "#434343"
LIGHT_RED_COLOR = "#f55e61"
LIGHT_GREEN_COLOR = "#5fcb50"
LIGHT_BLUE_COLOR = "#408ef5"
LIGHT_ORANGE_COLOR = "#e3883d"
LIGHT_PURPLE_COLOR = "#a346eb"
LIGHT_YELLOW_COLOR = "#f9e24c"
AQUA_BLUE_COLOR = "#16b0b5"
AQUA_GREEN_COLOR = "#0dc786"
GREEN_COLOR = "#34a853"
ORANGE_COLOR = "#fc5922"
DARK_RED_COLOR = "#bf2626"
DARK_BLUE_COLOR = "#3333FF"
DARK_PURPLE_COLOR = "#5157b9"
SAND_COLOR = "#b3a77d"
BROWN_COLOR = "#b85842"
WATER_COLOR = "#64a1ef"

class GeogebraLink(Group):
    """ A :class:`Group` with a title, an image and a link arranged vertically. """
    def __init__(self, title, img, link, text_scale=1.2, img_scale=0.8):
        text = Tex(r"\textbf{" + title + "}", color=DARK_BLUE_COLOR)
        text.scale(text_scale)
        img = ImageMobject("./assets/" + img + ".png")
        img.scale(img_scale)
        link = Tex(r"\textbf{Link: bit.ly/" + link + "}", color=DARK_BLUE_COLOR)   
        link[0][0:5].set(color=BLACK)

        super().__init__(text, img, link)
        self.arrange(DOWN, buff=0.5)
        self.shift(9 * RIGHT)

def AnimateFromLeft(*mobjects):
    return Group(*mobjects).shift(9 * RIGHT).animate.shift(9 * LEFT)

def AnimateFromRight(*mobjects):
    return Group(*mobjects).shift(9 * LEFT).animate.shift(9 * RIGHT)

def AnimateToLeft(*mobjects):
    return Group(*mobjects).animate.shift(9 * LEFT)

class Protractor(Group):
    """ A :class:`Group` of mobjects that looks like a protractor. """
    def __init__(self, **kwargs):
        protractor_bkg = "#F5F5F5"

        self.outer_lines = [
            Line(
                [(-1.85 if i % 5 != 0 else -1.75 if i % 10 != 0 else -1.65), 0, 0], 
                [-1.99, 0, 0], 
                color=BLACK, 
                stroke_width=(1 if i % 5 != 0 else 2)
            ).rotate(-i * DEGREES, about_point=ORIGIN)
            for i in range(0, 181, 1)
        ]
        self.inner_lines = [
            Line([-1, 0, 0], [-1.25, 0, 0], color=BLACK, stroke_width=2).rotate(-i * DEGREES, about_point=ORIGIN)
            if i == 90 else
            Line([-1, 0, 0], [-1.15, 0, 0], color=BLACK, stroke_width=2).rotate(-i * DEGREES, about_point=ORIGIN)
            for i in range(0, 181, 10)
        ]
        self.outer_text = [
            MathTex(str(i), color=(BLACK if i != 90 else protractor_bkg))
                .scale(0.25)
                .move_to(
                    Point(1.52 * LEFT)
                        .rotate(-i * DEGREES, about_point=ORIGIN)
                )
            for i in range(0, 181, 10)
        ]
        self.inner_text = [
           MathTex(str(i), color=(BLACK if i != 90 else protractor_bkg))
                .scale(0.2)
                .move_to(
                    Point(1.27 * RIGHT)
                        .rotate(i * DEGREES, about_point=ORIGIN)
                )
            for i in range(0, 181, 10) 
        ]
        self.ninety_degrees_text = MathTex("90", color=BLACK).scale(0.4).move_to(1.45 * UP)

        self.protractor_components = [
            AnnularSector(angle=TAU/2, color=protractor_bkg, stroke_color=BLACK, stroke_width=2),
            Rectangle(height=0.5, width=4, color=protractor_bkg, stroke_color=BLACK, stroke_width=2, fill_opacity=1)
                .shift(0.25 * DOWN),
            Line([1, 0, 0], [1.99, 0, 0], color=protractor_bkg, stroke_width=4),
            Line([-1, 0, 0], [-1.99, 0, 0], color=protractor_bkg, stroke_width=4),
            *self.outer_lines,
            *self.inner_lines,
            *self.outer_text,
            self.ninety_degrees_text,
            *self.inner_text,
            Line([0, 0, 0], [0, -0.15, 0], color=BLACK, stroke_width=2),
        ]

        super().__init__(
            *self.protractor_components,
            **kwargs
        )