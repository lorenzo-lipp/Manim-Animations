from manim import *

BACKGROUND_COLOR = "#faf4e1"
TEXT_COLOR = "#434343"
LIGHT_RED_COLOR = "#f55e61"
LIGHT_GREEN_COLOR = "#5fcb50"
LIGHT_BLUE_COLOR = "#408ef5"
LIGHT_ORANGE_COLOR = "#e3883d"
LIGHT_PURPLE_COLOR = "#a346eb"
AQUA_GREEN_COLOR = "#0dc786"
GREEN_COLOR = "#34a853"
DARK_RED_COLOR = "#bf2626"
DARK_BLUE_COLOR = "#3333FF"

def Pizza():
    return VGroup(
        Circle(1.3, color="#f7a139", fill_opacity=1),
        Circle(1.1, color="#e63838", fill_opacity=1),
        Circle(1, color="#ffd52c", fill_opacity=1),
        Pepperonni().shift(0.25 * UP),
        Pepperonni().shift(0.16 * DOWN + 0.25 * RIGHT),
        Pepperonni().shift(0.16 * DOWN + 0.25 * LEFT),
        Pepperonni().shift(0.55 * UP + 0.55 * RIGHT),
        Pepperonni().shift(0.55 * DOWN + 0.55 * RIGHT),
        Pepperonni().shift(0.55 * UP + 0.55 * LEFT),
        Pepperonni().shift(0.55 * DOWN + 0.55 * LEFT),
        Pepperonni().shift(0.75 * UP),
        Pepperonni().shift(0.75 * RIGHT),
        Pepperonni().shift(0.75 * DOWN),
        Pepperonni().shift(0.75 * LEFT),
    )
        
def Pepperonni():
    return VGroup(
        Circle(0.18, color="#d73d3d", fill_opacity=1),
        Circle(0.02, color="#f05454", fill_opacity=1).shift(0.07 * (UP + LEFT)),
        Circle(0.02, color="#f05454", fill_opacity=1).shift(0.07 * (UP + RIGHT)),
        Circle(0.03, color="#f05454", fill_opacity=1).shift(0.07 * (DOWN))
    )

def ChocolateSquare():
    return VGroup(
                Square(1, color="#a26953", fill_opacity=1, stroke_color="#814c3c"),
                Line((UP + RIGHT) / 2, (DOWN + LEFT) / 2, color="#814c3c"),
                Line((UP + LEFT) / 2, (DOWN + RIGHT) / 2, color="#814c3c"),
                Square(0.5, color="#814c3c", fill_opacity=1),
            )