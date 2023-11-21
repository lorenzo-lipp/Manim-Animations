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

def SmallCrackerPiece():
    WIDTH = 2.5/3
    HEIGHT = 1

    return VGroup(
        DashedVMobject(
            Rectangle(
                width=WIDTH, 
                height=HEIGHT, 
                color="#f5c36e", 
                stroke_width=10
            ), 
            num_dashes=50, 
            dashed_ratio=0.7
        ),
        Rectangle(
            width=WIDTH, 
            height=HEIGHT, 
            color=LIGHT_SAND_COLOR, 
            stroke_opacity=0, 
            fill_opacity=1
        ),
        CrackerHole().shift(0.3 * UP + 0.2 * RIGHT),
        CrackerHole().shift(0.2 * RIGHT),
        CrackerHole().shift(0.3 * DOWN + 0.2 * RIGHT),
        CrackerHole().shift(0.3 * UP + 0.2 * LEFT),
        CrackerHole().shift(0.2 * LEFT),
        CrackerHole().shift(0.3 * DOWN + 0.2 * LEFT),
    )

def BigCrackerPiece():
    WIDTH = 2.5/3 + 0.035
    HEIGHT = 2 + 0.035

    return VGroup(
        DashedVMobject(
            Rectangle(
                width=WIDTH, 
                height=HEIGHT, 
                color="#f5c36e", 
                stroke_width=10
            ), 
            num_dashes=100, 
            dashed_ratio=0.7
        ),
        Rectangle(
            width=WIDTH, 
            height=HEIGHT, 
            color=LIGHT_SAND_COLOR, 
            stroke_opacity=0, 
            fill_opacity=1
        ),
        CrackerHole().shift(0.8 * UP + 0.2 * RIGHT),
        CrackerHole().shift(0.5 * UP + 0.2 * RIGHT),
        CrackerHole().shift(0.2 * UP + 0.2 * RIGHT),
        CrackerHole().shift(0.2 * DOWN + 0.2 * RIGHT),
        CrackerHole().shift(0.5 * DOWN + 0.2 * RIGHT),
        CrackerHole().shift(0.8 * DOWN + 0.2 * RIGHT),
        CrackerHole().shift(0.8 * UP + 0.2 * LEFT),
        CrackerHole().shift(0.5 * UP + 0.2 * LEFT),
        CrackerHole().shift(0.2 * UP + 0.2 * LEFT),
        CrackerHole().shift(0.2 * DOWN + 0.2 * LEFT),
        CrackerHole().shift(0.5 * DOWN + 0.2 * LEFT),
        CrackerHole().shift(0.8 * DOWN + 0.2 * LEFT),
    )

def CrackerHole():
    return VGroup(
        Circle(
            radius=0.07, 
            color="#f5c36e", 
            fill_opacity=1,
            stroke_opacity=0
        ),
        Circle(
            radius=0.01, 
            color=LIGHT_ORANGE_COLOR, 
            stroke_opacity=0.7
        )
    )

def SmallCracker(opacity_arr=[1, 1, 1, 1, 1, 1]):
    return VGroup(
        VGroup(
            SmallCrackerPiece().set_opacity(opacity_arr[0]),
            SmallCrackerPiece().set_opacity(opacity_arr[1]),
            SmallCrackerPiece().set_opacity(opacity_arr[2]),
        ).arrange(RIGHT, buff=0.035),
        VGroup(
            SmallCrackerPiece().set_opacity(opacity_arr[3]),
            SmallCrackerPiece().set_opacity(opacity_arr[4]),
            SmallCrackerPiece().set_opacity(opacity_arr[5]),
        ).arrange(RIGHT, buff=0.035)
    ).arrange(DOWN, buff=0.035)

def BigCracker(opacity_arr=[1, 1, 1]):
    return VGroup(
        BigCrackerPiece().set_opacity(opacity_arr[0]),
        BigCrackerPiece().set_opacity(opacity_arr[1]),
        BigCrackerPiece().set_opacity(opacity_arr[2]),
    ).arrange(RIGHT, buff=0.035)

def GrayCracker():
    return SmallCracker().set(color=LIGHT_GRAY)

def AnimateFromLeft(*mobjects):
    return Group(*mobjects).shift(9 * RIGHT).animate.shift(9 * LEFT)

def AnimateToLeft(*mobjects):
    return Group(*mobjects).animate.shift(9 * LEFT)