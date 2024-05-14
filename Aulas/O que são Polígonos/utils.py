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

def Shape1(**kwargs):
    return VMobject(**kwargs).set_points_as_corners([
        0.2 * LEFT, 
        0.7 * LEFT,
        0.7 * LEFT, 
        0.4 * LEFT + 0.4 * DOWN,
        0.4 * LEFT + 0.4 * DOWN, 
        0.7 * LEFT + 0.8 * DOWN,
        0.7 * LEFT + 0.8 * DOWN, 
        0.2 * LEFT + 0.8 * DOWN,
        0.2 * LEFT + 0.8 * DOWN, 
        1.2 * DOWN,
        1.2 * DOWN, 
        0.2 * RIGHT + 0.8 * DOWN,
        0.2 * RIGHT + 0.8 * DOWN, 
        0.7 * RIGHT + 0.8 * DOWN,
        0.7 * RIGHT + 0.8 * DOWN, 
        0.5 * RIGHT + 0.4 * DOWN,
        0.5 * RIGHT + 0.4 * DOWN, 
        0.7 * RIGHT,
        0.7 * RIGHT, 
        0.2 * RIGHT
    ])

def Shape2(**kwargs):
    return AnnularSector(
        inner_radius=0,
        outer_radius=0.6,
        angle=5*PI/3,
        start_angle=-PI/3,
        **kwargs
    )

def Shape3(**kwargs):
    return RegularPolygon(6, **kwargs).scale(0.7)

def Shape4(**kwargs):
    return VMobject(**kwargs).set_points_as_corners([
        0.2 * LEFT + 0.2 * UP,
        0.2 * LEFT + 0.6 * UP,
        0.2 * RIGHT + 0.6 * UP,
        0.2 * RIGHT + 0.2 * UP,
        0.6 * RIGHT + 0.2 * UP,
        0.6 * RIGHT + 0.2 * DOWN,
        0.2 * RIGHT + 0.2 * DOWN,
        0.2 * RIGHT + 0.6 * DOWN,
        0.2 * LEFT + 0.6 * DOWN,
        0.2 * LEFT + 0.2 * DOWN,
        0.6 * LEFT + 0.2 * DOWN,
        0.6 * LEFT + 0.2 * UP,
        0.2 * LEFT + 0.2 * UP,
    ])

def Shape5(**kwargs):
    return VMobject(**kwargs).set_points_as_corners([
        0.8 * LEFT + 0.4 * DOWN,
        0.3 * RIGHT + 0.4 * DOWN,
        0.8 * RIGHT + 0.4 * UP,
        0.3 * LEFT + 0.4 * UP,
        0.8 * LEFT + 0.4 * DOWN,
    ])

def Shape6(**kwargs):
    return VMobject(**kwargs).set_points_as_corners([
        0.5 * LEFT + 0.4 * UP,
        0.5 * RIGHT + 0.4 * UP,
        0.5 * RIGHT + 0.4 * DOWN,
        0.8 * DOWN,
        0.5 * LEFT + 0.4 * DOWN,
        0.5 * LEFT + 0.4 * UP,
    ])

def Shape7(**kwargs):
    return VGroup(
        DashedLine(0.2 * DOWN + 0.6 * LEFT, 0.2 * DOWN + 0.2 * RIGHT, **kwargs),
        DashedLine(0.2 * DOWN + 0.2 * RIGHT, 0.6 * UP + 0.2 * RIGHT, **kwargs),
        DashedLine(0.2 * DOWN + 0.2 * RIGHT, 0.6 * DOWN + 0.6 * RIGHT, **kwargs),
        VMobject(**kwargs).set_points_as_corners([
            0.2 * UP + 0.6 * RIGHT,
            0.6 * UP + 0.2 * RIGHT,
            0.6 * UP + 0.6 * LEFT,
            0.2 * UP + 0.2 * LEFT,
            0.2 * UP + 0.6 * RIGHT,
        ]),
        VMobject(**kwargs).set_points_as_corners([
            0.2 * UP + 0.6 * RIGHT,
            0.6 * DOWN + 0.6 * RIGHT,
            0.6 * DOWN + 0.2 * LEFT,
            0.2 * UP + 0.2 * LEFT,
            0.2 * UP + 0.6 * RIGHT,
        ]),
        VMobject(**kwargs).set_points_as_corners([
            0.6 * UP + 0.6 * LEFT,
            0.2 * DOWN + 0.6 * LEFT,
            0.6 * DOWN + 0.2 * LEFT,
            0.2 * UP + 0.2 * LEFT,
            0.6 * UP + 0.6 * LEFT,
        ])
    )

def Shape8(**kwargs):
    return VMobject(**kwargs).set_points_as_corners([
        0.5 * LEFT + 0.5 * UP,
        0.5 * RIGHT + 0.5 * UP,
        0.5 * LEFT + 0.5 * DOWN,
        0.5 * RIGHT + 0.5 * DOWN,
        0.5 * LEFT + 0.5 * UP,
    ])

def Shape9(stroke_width=5, **kwargs):
    return VGroup(
        VGroup(
            VGroup(
                ArcBetweenPoints(0.6 * RIGHT, 0.6 * LEFT, angle=PI, stroke_width=stroke_width, **kwargs)
                        .stretch_to_fit_height(0.25)
                        .stretch_to_fit_width(1.2),
                ArcBetweenPoints(0.6 * LEFT, 0.6 * RIGHT, angle=PI, stroke_width=stroke_width, **kwargs)
                        .stretch_to_fit_height(0.25)
                        .stretch_to_fit_width(1.2),
            ).arrange(DOWN, buff=0),
            VGroup(
                DashedVMobject(
                    ArcBetweenPoints(0.6 * RIGHT, 0.6 * LEFT, angle=PI, stroke_width=stroke_width, **kwargs)
                        .stretch_to_fit_height(0.25)
                        .stretch_to_fit_width(1.2)
                ),
                ArcBetweenPoints(0.6 * LEFT, 0.6 * RIGHT, angle=PI, stroke_width=stroke_width, **kwargs)
                        .stretch_to_fit_height(0.25)
                        .stretch_to_fit_width(1.2),
            ).arrange(DOWN, buff=0)
        ).arrange(DOWN, buff=0),
        Difference(
            Rectangle(height=0.5, width=1.2),
            ArcBetweenPoints(0.6 * LEFT, 0.6 * RIGHT, angle=PI, stroke_width=stroke_width, **kwargs)
                .stretch_to_fit_height(0.25)
                .stretch_to_fit_width(1.2)
                .move_to(0.125 * UP),
            stroke_width=0,
            **kwargs
        ),
        Line(0.6 * LEFT + 0.25 * UP, 0.6 * LEFT + 0.25 * DOWN, stroke_width=stroke_width, **kwargs),
        Line(0.6 * RIGHT + 0.25 * UP, 0.6 * RIGHT + 0.25 * DOWN, stroke_width=stroke_width, **kwargs)
    )

def Shape10(**kwargs):
    return VMobject(**kwargs).set_points_as_corners([
        0.2 * LEFT + 0.6 * DOWN,
        0.2 * LEFT,
        0.5 * LEFT,
        0.6 * UP,
        0.5 * RIGHT,
        0.2 * RIGHT,
        0.2 * RIGHT + 0.6 * DOWN
    ])

def Shape11(**kwargs):
    return Rectangle(height=0.6, width=1.2, **kwargs)

def Shape12(**kwargs):
    return Star(**kwargs).scale(0.66)

def Shape13(**kwargs):
    return RoundedRectangle(-0.25, height=1, width=1.6, **kwargs)

def Shape14(**kwargs):
    return VMobject(**kwargs).set_points_as_corners([
        0.6 * LEFT + 0.6 * DOWN,
        0.6 * LEFT + 0.6 * UP,
        0.6 * RIGHT + 0.6 * DOWN,
        0.6 * LEFT + 0.6 * DOWN,
    ])

def AlmostFadeOut(*mobjects):
    return Transform(Group(*mobjects), Group(*mobjects).copy().fade(0.8))