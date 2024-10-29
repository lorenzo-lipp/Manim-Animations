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
LIGHT_GRAY_COLOR = "#d0d0d0"
AQUA_GREEN_COLOR = "#0dc786"
GREEN_COLOR = "#34a853"
DARK_RED_COLOR = "#bf2626"
DARK_BLUE_COLOR = "#3333FF"
SAND_COLOR = "#b3a77d"
BROWN_COLOR = "#b85842"
G_PURPLE = "#b8a9d2"
G_BLUE = "#91d8f7"
G_PINK = "#f38fba"

def AnimateFromLeft(*mobjects, **kwargs):
    return Group(*mobjects).shift(9 * RIGHT).animate(**kwargs).shift(9 * LEFT)

def AnimateToLeft(*mobjects, **kwargs):
    return Group(*mobjects).animate(**kwargs).shift(9 * LEFT)

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

def Board():
    """ 
        Returns a `~.VGroup` with the domino board
    """
    return VGroup(
                VGroup(
                    VGroup(
                    DashedVMobject(RoundedRectangle(0.4, width=3, height=1.5, color=LIGHT_GRAY_COLOR, fill_opacity=0.3), num_dashes=30),
                    DashedLine(0.6 * UP, 0.6 * DOWN, color=LIGHT_GRAY_COLOR)
                    ),
                    VGroup(
                        DashedVMobject(RoundedRectangle(0.4, width=3, height=1.5, color=LIGHT_GRAY_COLOR, fill_opacity=0.3), num_dashes=30),
                        DashedLine(0.6 * UP, 0.6 * DOWN, color=LIGHT_GRAY_COLOR)
                    ),
                ).arrange(RIGHT, 0.3),  
                VGroup(
                    VGroup(
                    DashedVMobject(RoundedRectangle(0.4, width=1.5, height=3, color=LIGHT_GRAY_COLOR, fill_opacity=0.3), num_dashes=30),
                    DashedLine(0.6 * LEFT, 0.6 * RIGHT, color=LIGHT_GRAY_COLOR)
                    ),
                    VGroup(
                        DashedVMobject(RoundedRectangle(0.4, width=1.5, height=3, color=LIGHT_GRAY_COLOR, fill_opacity=0.3), num_dashes=30),
                        DashedLine(0.6 * LEFT, 0.6 * RIGHT, color=LIGHT_GRAY_COLOR)
                    ),
                ).arrange(RIGHT, 3.2),  
                VGroup(
                    VGroup(
                    DashedVMobject(RoundedRectangle(0.4, width=3, height=1.5, color=LIGHT_GRAY_COLOR, fill_opacity=0.3), num_dashes=30),
                    DashedLine(0.6 * UP, 0.6 * DOWN, color=LIGHT_GRAY_COLOR)
                    ),
                    VGroup(
                        DashedVMobject(RoundedRectangle(0.4, width=3, height=1.5, color=LIGHT_GRAY_COLOR, fill_opacity=0.3), num_dashes=30),
                        DashedLine(0.6 * UP, 0.6 * DOWN, color=LIGHT_GRAY_COLOR)
                    ),
                ).arrange(RIGHT, 0.3),            
            ).arrange(DOWN, 0.3)

def TopPieces():
    """ 
        Returns a `~.VGroup` with the top domino pieces
    """
    return VGroup(
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{6}\over{10}", color=BLACK).shift(0.75 * DOWN),
                    VGroup(
                        RegularPolygon(5, radius=0.25, color=LIGHT_PINK, stroke_color=BLACK, fill_opacity=1),
                        RegularPolygon(5, radius=0.25, color=LIGHT_PINK, stroke_color=BLACK, fill_opacity=1)
                            .rotate(36 * DEGREES)
                            .shift(0.32 * UP + 0.21 * RIGHT),
                        RegularPolygon(5, radius=0.25, color=WHITE, stroke_color=BLACK, fill_opacity=1)
                            .rotate(-36 * DEGREES)
                            .shift(0.32 * UP + 0.21 * LEFT),
                        RegularPolygon(5, radius=0.25, color=WHITE, stroke_color=BLACK, fill_opacity=1)
                            .rotate(-36 * DEGREES)
                            .shift(0.4 * RIGHT + 0.14 * DOWN),
                        RegularPolygon(5, radius=0.25, color=WHITE, stroke_color=BLACK, fill_opacity=1)
                            .rotate(-36 * DEGREES)
                            .shift(0.38 * LEFT + 0.12 * DOWN),
                        RegularPolygon(5, radius=0.25, color=LIGHT_PINK, stroke_color=BLACK, fill_opacity=1)
                            .rotate(180 * DEGREES)
                            .shift(0.45 * DOWN),
                    ).shift(0.75 * UP)
                ),
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{2}\over{3}", color=BLACK).shift(0.75 * DOWN),
                    RoundedRectangle(0.1, height=0.2, width=1, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.4 * UP),
                    RoundedRectangle(0.1, height=0.2, width=1, color=LIGHT_RED_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.4 * UP + 0.2 * UP),
                    RoundedRectangle(0.1, height=0.2, width=1, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.4 * UP + 0.4 * UP),
                    RoundedRectangle(0.1, height=0.2, width=1, color=LIGHT_RED_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.4 * UP + 0.6 * UP)
                ),
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{1}\over{4}", color=BLACK).shift(0.75 * DOWN),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=AQUA_GREEN_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * UP + 0.3 * LEFT),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * UP),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=AQUA_GREEN_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * UP + 0.3 * RIGHT),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * LEFT),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=AQUA_GREEN_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * RIGHT),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * DOWN + 0.3 * LEFT),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=AQUA_GREEN_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * DOWN),
                    RoundedRectangle(0.05, width=0.3, height=0.3, color=AQUA_GREEN_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.3 * DOWN + 0.3 * RIGHT),
                ),
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{5}\over{9}", color=BLACK).shift(0.75 * DOWN),
                    RoundedRectangle(0.1, height=1, width=0.2, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP),
                    RoundedRectangle(0.1, height=1, width=0.2, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.2 * RIGHT),
                    RoundedRectangle(0.1, height=1, width=0.2, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.4 * RIGHT),
                    RoundedRectangle(0.1, height=1, width=0.2, color=LIGHT_PURPLE_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.2 * LEFT),
                    RoundedRectangle(0.1, height=1, width=0.2, color=LIGHT_PURPLE_COLOR, stroke_color=BLACK, fill_opacity=1).shift(0.7 * UP + 0.4 * LEFT),
                ),
            ).arrange(RIGHT, 0.5)

def BottomPieces():
    """ 
        Returns a `~.VGroup` with the bottom domino pieces
    """
    last_piece_colors = [LIGHT_GREEN_COLOR, LIGHT_GREEN_COLOR, WHITE, WHITE, LIGHT_GREEN_COLOR, LIGHT_GREEN_COLOR, WHITE, LIGHT_GREEN_COLOR, LIGHT_GREEN_COLOR, WHITE]
    
    return VGroup(
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{3}\over{6}", color=BLACK).shift(0.75 * DOWN),
                    VGroup(
                        Circle(0.5, color=WHITE, stroke_color=BLACK, fill_opacity=1),
                        Sector(0.5, angle=90 * DEGREES, color=AQUA_GREEN_COLOR, stroke_width=DEFAULT_STROKE_WIDTH, stroke_color=BLACK, fill_opacity=1),
                        Line(ORIGIN, 0.5 * LEFT, color=BLACK),
                        Line(ORIGIN, 0.5 * DOWN, color=BLACK)
                    ).shift(0.7 * UP)
                ),
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{2}\over{5}", color=BLACK).shift(0.75 * DOWN),
                    VGroup(
                        RoundedRectangle(0.05, width=0.3, height=0.3, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.3 * UP + 0.3 * LEFT),
                        RoundedRectangle(0.05, width=0.3, height=0.3, color=LIGHT_PINK, stroke_color=BLACK, fill_opacity=1).shift(0.3 * UP + 0.3 * RIGHT),
                        RoundedRectangle(0.05, width=0.3, height=0.3, color=LIGHT_PINK, stroke_color=BLACK, fill_opacity=1),
                        RoundedRectangle(0.05, width=0.3, height=0.3, color=WHITE, stroke_color=BLACK, fill_opacity=1).shift(0.3 * DOWN + 0.3 * LEFT),
                        RoundedRectangle(0.05, width=0.3, height=0.3, color=LIGHT_PINK, stroke_color=BLACK, fill_opacity=1).shift(0.3 * DOWN + 0.3 * RIGHT),
                    ).shift(0.7 * UP)
                ),
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{4}\over{5}", color=BLACK).shift(0.75 * DOWN),
                    VGroup(
                        Circle(0.5, color=WHITE, stroke_color=BLACK, fill_opacity=1),
                        Sector(0.5, angle=90 * DEGREES, color=ORANGE, stroke_width=DEFAULT_STROKE_WIDTH, stroke_color=BLACK, fill_opacity=1),
                        Sector(0.5, angle=90 * DEGREES, start_angle=180 * DEGREES, color=ORANGE, stroke_width=DEFAULT_STROKE_WIDTH, stroke_color=BLACK, fill_opacity=1),
                        Sector(0.5, angle=90 * DEGREES, start_angle=270 * DEGREES, color=ORANGE, stroke_width=DEFAULT_STROKE_WIDTH, stroke_color=BLACK, fill_opacity=1)
                    ).shift(0.7 * UP)
                ),
                VGroup(
                    RoundedRectangle(0.4, width=1.5, height=3, color=BLACK, fill_color="#fefcef", fill_opacity=1),
                    Line(0.6 * LEFT, 0.6 * RIGHT, color="#edebd5"),
                    MathTex(r"{3}\over{5}", color=BLACK).shift(0.75 * DOWN),
                    VGroup(
                        *[
                            RegularPolygon(5, radius=0.17, color=last_piece_colors[i], stroke_color=BLACK, fill_opacity=1)
                                .shift(0.45 * UP)
                                .rotate(i * 36 * DEGREES, about_point=ORIGIN)
                            for i in range(10)
                        ]
                    ).shift(0.7 * UP)
                ),
            ).arrange(RIGHT, 0.5)

def bring_to_forward(scene, *mobjects):
    """ 
        Remove mobjects and add again to the scene
    """
    scene.remove(*mobjects)
    scene.add(*mobjects)