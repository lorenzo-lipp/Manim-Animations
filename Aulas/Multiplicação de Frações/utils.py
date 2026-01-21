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

class FadeOutAndBack(FadeOut):
    def __init__(self, *mobjects: Mobject, **kwargs) -> None:
        super().__init__(*mobjects, rate_func=rate_functions.there_and_back, **kwargs)
        self.remover = False

class MatchingMathTex(SingleStringMathTex):
    def __init__(self, text, mobj: Mobject, text_scale=2.5, **kwargs):
        super().__init__(text, **kwargs)
        self.scale(text_scale)
        self.move_to(mobj)

def time_convert(editor_code_time):
    int_part = int(editor_code_time)
    float_part = editor_code_time - int_part
    return int_part + (float_part * 100 / 60)