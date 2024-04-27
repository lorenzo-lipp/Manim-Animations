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

def Crab():
    return ImageMobject("./assets/003.png")

def Alligator():
    return ImageMobject("./assets/001.png")

def Sloth():
    return ImageMobject("./assets/002.png")

def Toucan():
    return ImageMobject("./assets/004.png")

def Feather():
    return ImageMobject("./assets/005.png")

def Pyramid(size):
    return VGroup(*[
        VGroup(*[
            Circle(0.5, color=LIGHT_GREEN_COLOR, fill_opacity=1) 
            for j in range(i + 1)
        ]).arrange(RIGHT, buff=0.2) 
        for i in range(size)
    ]).arrange(DOWN, buff=0.2)