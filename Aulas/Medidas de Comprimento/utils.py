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

class LogoLink(Group):
    """ A :class:`Group` with a svg image and a link arranged vertically. """
    def __init__(self, img_scale=1):
        img = SVGMobject(file_name="../assets/logo-simbolo.svg", stroke_color=TEXT_COLOR, height=5, fill_opacity=0.9)
        img.scale(img_scale)
        link = Tex(r"\textbf{Link: bit.ly/portal-qcm}", color=DARK_BLUE_COLOR)   
        link[0][0:5].set(color=BLACK)

        super().__init__(img, link)
        self.arrange(DOWN, buff=0.5)
        self.shift(9 * RIGHT)

def AnimateFromLeft(*mobjects):
    return Group(*mobjects).shift(9 * RIGHT).animate.shift(9 * LEFT)

def AnimateFromRight(*mobjects):
    return Group(*mobjects).shift(9 * LEFT).animate.shift(9 * RIGHT)

def AnimateToLeft(*mobjects):
    return Group(*mobjects).animate.shift(9 * LEFT)

class Ruler(Group):
    """ A :class:`Group` of mobjects that looks like a ruler. """
    def __init__(self, **kwargs):
        self.ruler_box = Rectangle(DARK_GRAY, 0.5, 3.3, fill_opacity=0.1)
        self.lines_x = -1.5
        self.lines_y = 0.25
        self.lines = [
            Line([self.lines_x + i / 25, self.lines_y - 0.2, 0], [self.lines_x + i / 25, self.lines_y, 0], color=BLACK, stroke_width=2)
            if i % 5 == 0 else
            Line([self.lines_x + i / 25, self.lines_y - 0.1, 0], [self.lines_x + i / 25, self.lines_y, 0], color=BLACK, stroke_width=2)
            for i in range(0, 76, 1)
        ]
        self.texts = [
            MathTex(str(i), color=BLACK)
                .scale(0.25)
                .move_to([self.lines_x + i / 5, self.lines_y - 0.3, 0])
            for i in range(0, 16, 1)
        ]

        self.ruler_components = [
            self.ruler_box,
            *self.lines,
            *self.texts
        ]

        super().__init__(
            *self.ruler_components,
            **kwargs
        )

class MeasuringTape(Group):
    """ A :class:`Group` of mobjects that looks like a measuring tape. """
    def __init__(self, **kwargs):
        self.box = RoundedRectangle(0.1, color=BLACK, height=0.6, width=0.9, fill_opacity=1)
        self.ruler_box = Rectangle(DARK_GRAY, 0.4, 3.3, fill_opacity=0.1)
        self.box.move_to(self.ruler_box, LEFT)

        self.yellow_box = RoundedRectangle(0.05, color="#ffcc00", height=0.4, width=0.5, fill_opacity=1)
        self.black_box = RoundedRectangle(0.025, color=BLACK, height=0.25, width=0.2, fill_opacity=1)
        self.metal_detail = RoundedRectangle(0.015, color=BLACK, fill_color=LIGHT_GRAY, height=0.45, width=0.07, fill_opacity=1, stroke_width=DEFAULT_STROKE_WIDTH / 2)
        self.yellow_box.move_to(self.box, RIGHT)
        self.yellow_box.shift(0.02 * LEFT)
        self.black_box.move_to(self.yellow_box, RIGHT)
        self.black_box.shift(0.02 * LEFT)
        self.metal_detail.move_to(self.ruler_box, RIGHT)
        self.metal_detail.shift(0.015 * RIGHT)
        self.moving_part = Group(
            self.box,
            self.yellow_box,
            self.black_box
        )
        self.moving_part.shift(2.3 * RIGHT)

        self.lines_x = -1.5
        self.lines_y = 0.2
        self.lines = [
            Line([self.lines_x + i / 25, self.lines_y - 0.2, 0], [self.lines_x + i / 25, self.lines_y, 0], color=BLACK, stroke_width=2)
            if i % 5 == 0 else
            Line([self.lines_x + i / 25, self.lines_y - 0.1, 0], [self.lines_x + i / 25, self.lines_y, 0], color=BLACK, stroke_width=2)
            for i in range(0, 76, 1)
        ]
        self.texts = [
            MathTex(str(i), color=BLACK)
                .scale(0.25)
                .move_to([self.lines_x + (15 - i) / 5, self.lines_y - 0.3, 0])
            for i in range(0, 16, 1)
        ]

        self.invisible_box = always_redraw(lambda: 
            Polygon(
                [self.ruler_box.get_left()[0], self.moving_part.get_top()[1], 0],
                [self.ruler_box.get_left()[0], self.moving_part.get_bottom()[1], 0],
                [self.moving_part.get_left()[0], self.moving_part.get_bottom()[1], 0],
                [self.moving_part.get_left()[0], self.moving_part.get_top()[1], 0],
                color=BACKGROUND_COLOR, 
                fill_opacity=1
            )
        )

        self.ruler_components = [
            self.ruler_box,
            *self.lines,
            *self.texts,
            self.metal_detail,
            self.invisible_box,
            self.moving_part,
        ]

        super().__init__(
            *self.ruler_components,
            **kwargs
        )

class FadeOutAndBack(FadeOut):
    def __init__(self, *mobjects: Mobject, **kwargs) -> None:
        super().__init__(*mobjects, rate_func=rate_functions.there_and_back, **kwargs)
        self.remover = False