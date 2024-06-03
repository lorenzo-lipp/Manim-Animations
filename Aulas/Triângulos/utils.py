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

def AnimateFromLeft(*mobjects):
    return Group(*mobjects).shift(9 * RIGHT).animate.shift(9 * LEFT)

def AnimateToLeft(*mobjects):
    return Group(*mobjects).animate.shift(9 * LEFT)

def GeogebraLink(title, img, link, scale=0.8):
    text = Tex(r"\textbf{" + title + "}", color=DARK_BLUE_COLOR)
    text.scale(1.2)
    img = ImageMobject("./assets/" + img + ".png")
    img.scale(scale)
    link = Tex(r"\textbf{Link: bit.ly/" + link + "}", color=DARK_BLUE_COLOR)   
    link[0][0:5].set(color=BLACK)
    group = Group(text, img, link)
    group.arrange(DOWN, buff=0.5)
    group.shift(9 * RIGHT)

    return group