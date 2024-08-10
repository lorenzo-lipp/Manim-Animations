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
        Ellipse(1.6, 0.35, color=TEXT_COLOR, stroke_width=4).shift(UP),
        ArcBetweenPoints(UP + 0.8 * LEFT, DOWN + 0.5 * LEFT, angle=0, color=TEXT_COLOR, stroke_width=4),
        ArcBetweenPoints(DOWN + 0.5 * LEFT, DOWN + 0.5 * RIGHT, angle=TAU/8, color=TEXT_COLOR, stroke_width=4),
        ArcBetweenPoints(UP + 0.8 * RIGHT, DOWN + 0.5 * RIGHT, angle=0, color=TEXT_COLOR, stroke_width=4),
    ).scale(2)

def Water(water_level):
    ellipse_width = (water_level * 1.25 + 2) / 2
    ellipse_pos = (water_level * 4 - 2) * UP / 2
    water_angle = -TAU/(10 + water_level * 1.7)

    return Group(
        Ellipse(ellipse_width, 0.2, color=WATER_COLOR, fill_opacity=0.5, stroke_width=0)
            .shift(ellipse_pos),
        ArcPolygonFromArcs(
            ArcBetweenPoints(ellipse_pos + ellipse_width * 0.5 * LEFT, DOWN + 0.5 * LEFT, angle=0, stroke_width=0),
            ArcBetweenPoints(DOWN + 0.5 * LEFT, DOWN + 0.5 * RIGHT, angle=TAU/8, stroke_width=0),
            ArcBetweenPoints(ellipse_pos + ellipse_width * 0.5 * RIGHT, DOWN + 0.5 * RIGHT, angle=0, stroke_width=0),
            ArcBetweenPoints(ellipse_pos + ellipse_width * 0.5 * RIGHT, ellipse_pos + ellipse_width * 0.5 * LEFT, angle=water_angle, stroke_width=0),
            fill_opacity=0.8,
            fill_color=WATER_COLOR,
            stroke_width=0
        )
    ).scale(2)

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