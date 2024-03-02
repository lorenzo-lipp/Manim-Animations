from manim import *

BACKGROUND_COLOR = "#faf4e1"
TEXT_COLOR = "#434343"
LIGHT_RED_COLOR = "#f55e61"
LIGHT_GREEN_COLOR = "#5fcb50"
LIGHT_BLUE_COLOR = "#408ef5"
LIGHT_ORANGE_COLOR = "#e3883d"
LIGHT_PURPLE_COLOR = "#a346eb"
LIGHT_YELLOW_COLOR = "#f9e24c"
LIGHT_SAND_COLOR = "#f8e087"
AQUA_GREEN_COLOR = "#0dc786"
GREEN_COLOR = "#34a853"
DARK_RED_COLOR = "#bf2626"
DARK_BLUE_COLOR = "#3333FF"
SAND_COLOR = "#b3a77d"
BROWN_COLOR = "#b85842"
G_PURPLE = "#b8a9d2"
G_BLUE = "#91d8f7"
G_PINK = "#f38fba"

def AnimateFromLeft(*mobjects):
    return Group(*mobjects).shift(9 * RIGHT).animate.shift(9 * LEFT)

def AnimateToLeft(*mobjects):
    return Group(*mobjects).animate.shift(9 * LEFT)

def RotatePiece(self, piece, center):
    for i in range(10):
        self.play(Rotate(piece, 7.2 * DEGREES, about_point=center), run_time=0.07, rate_func=linear)