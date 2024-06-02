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

def Cup():
    return Group(
        ArcPolygonFromArcs(
            ArcBetweenPoints(UP + 0.7 * RIGHT, UP + 0.8 * LEFT, angle=TAU/6, color=TEXT_COLOR, stroke_width=4),
            ArcBetweenPoints(UP + 0.8 * LEFT, DOWN + 0.5 * LEFT, angle=0, color=TEXT_COLOR, stroke_width=4),
            ArcBetweenPoints(DOWN + 0.5 * LEFT, DOWN + 0.5 * RIGHT, angle=TAU/12, color=TEXT_COLOR, stroke_width=4),
            ArcBetweenPoints(UP + 0.7 * RIGHT, DOWN + 0.5 * RIGHT, angle=0, color=TEXT_COLOR, stroke_width=4),
            fill_opacity=0.1,
            fill_color=GRAY
        ),
        ArcPolygonFromArcs(
            ArcBetweenPoints(UP + 0.8 * LEFT, DOWN + 0.5 * LEFT, angle=0, color=TEXT_COLOR, stroke_width=4),
            ArcBetweenPoints(DOWN + 0.5 * LEFT, DOWN + 0.5 * RIGHT, angle=TAU/12, color=TEXT_COLOR, stroke_width=4),
            ArcBetweenPoints(UP + 0.7 * RIGHT, DOWN + 0.5 * RIGHT, angle=0, color=TEXT_COLOR, stroke_width=4),
            ArcBetweenPoints(UP + 0.7 * RIGHT, UP + 0.8 * LEFT, angle=-TAU/6, color=TEXT_COLOR, stroke_width=4),
            fill_opacity=0.1,
            fill_color=GRAY
        ),
        ArcBetweenPoints(UP + 0.8 * LEFT, UP + 0.7 * RIGHT, angle=TAU/6, color=TEXT_COLOR, stroke_width=4),
    ).scale(2)

def Droplet():
    return ArcPolygonFromArcs(
        ArcBetweenPoints(0.7 * UP, 0.4 * LEFT, angle=0, color=LIGHT_BLUE_COLOR, stroke_width=4),
        ArcBetweenPoints(0.4 * LEFT, 0.4 * RIGHT, angle=TAU/2, color=LIGHT_BLUE_COLOR, stroke_width=4),
        ArcBetweenPoints(0.7 * UP, 0.4 * RIGHT, angle=0, color=LIGHT_BLUE_COLOR, stroke_width=4),
        fill_opacity=1,
        fill_color="#64a1ef",
        color=LIGHT_BLUE_COLOR
    )

def Water(water_level):
    return ArcPolygonFromArcs(
        ArcBetweenPoints((water_level * 4 - 2) * UP + (water_level * 0.6 + 1) * LEFT, 2 * DOWN +  LEFT, angle=0, stroke_width=0),
        ArcBetweenPoints(2 * DOWN + LEFT, 2 * DOWN + RIGHT, angle=TAU/12, stroke_width=0),
        ArcBetweenPoints((water_level * 4 - 2) * UP + (water_level * 0.4 + 1) * RIGHT, 2 * DOWN + RIGHT, angle=0, stroke_width=0),
        ArcBetweenPoints((water_level * 4 - 2) * UP + (water_level * 0.4 + 1) * RIGHT, (water_level * 4 - 2) * UP + (water_level * 0.6 + 1) * LEFT, angle=-TAU/8, stroke_width=0),
        fill_opacity=0.8,
        fill_color="#64a1ef",
        stroke_width=0
    )

def Balance():
    balance = Group(
        Rectangle(DARK_BLUE, 0.1, 4, fill_opacity=1, stroke_width=1),
        Rectangle(LIGHT_BLUE_COLOR, 0.2, 3.6, fill_opacity=1, stroke_width=0),
        Rectangle(DARK_BLUE, 0.5, 0.2, fill_opacity=1, stroke_width=0),
        Rectangle(LIGHT_BLUE_COLOR, 1.4, 3, fill_opacity=0, stroke_width=0),
        Rectangle(LIGHT_BLUE_COLOR, 1.5, 3, fill_opacity=1),
        Rectangle(DARK_BLUE, 0.2, 3.3, fill_opacity=1),
    ).arrange(DOWN, buff=0)
    tick_mark = Line(ORIGIN + 0.15 * UP, ORIGIN, color=DARK_BLUE)
    pointer = Line(0.5 * DOWN, 0.935 * DOWN, color=LIGHT_RED_COLOR, stroke_width=5)

    balance.add(
        ArcBetweenPoints(
            balance[4].get_center() + 0.75 * UP + 1.5 * RIGHT, 
            balance[4].get_center() + 0.75 * UP + 1.5 * LEFT, 
            radius=1.5,
            color=LIGHT_BLUE_COLOR,
            fill_opacity=1
        ),
        Circle(
            color=BACKGROUND_COLOR, 
            radius=0.7, 
            fill_opacity=1,
            stroke_color=DARK_BLUE,
            stroke_width=10
        ).shift(0.5 * DOWN),
        *[tick_mark.copy().rotate(angle * PI / 180, about_point=0.5 * DOWN) for angle in range(0, 360, 36)],
        pointer,
        Dot(0.5 * DOWN, color=DARK_BLUE, radius=0.05),
    )
    return balance

def Tomato():
    return ImageMobject("./assets/tomato.png")