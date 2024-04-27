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
SAND_COLOR = "#b3a77d"
BROWN_COLOR = "#b85842"

def SpeechBubble(**kwargs):
    gp = VGroup(
        RoundedRectangle(width=4.5, height=2.5),
        Polygram([
            [-4.5/3, -2.5 + 0.55, 0], 
            [-4.5/2.8, -2.5 + 1.25, 0], 
            [-4.5/2.8 + 1, -2.5 + 1.25, 0]
        ])
    )

    return Union(*gp, **kwargs)

def Division(numerator, denominator):
    result = numerator // denominator
    integerPart = int(result * denominator)
    remainder = numerator - integerPart
    
    gp = VGroup(
        VGroup(
            MathTex(str(numerator), color=LIGHT_PURPLE_COLOR),
            VGroup(
                Line((0, 0, 0), (0, 0.6, 0), color=LIGHT_PURPLE_COLOR),
                Line((0, 0, 0), (0.6, 0, 0), color=LIGHT_PURPLE_COLOR),
                MathTex(str(denominator), color=LIGHT_PURPLE_COLOR).shift(0.3 * UP + 0.32 * RIGHT)
            ) 
        ).arrange(RIGHT),
        VGroup(
            MathTex("-", color=SAND_COLOR),
            MathTex(r"\frac{" + str(integerPart) + "}{" + str(remainder) + "}", color=SAND_COLOR),
            MathTex(str(result), color=SAND_COLOR)
        ).arrange(RIGHT)
    )

    gp[1].shift(0.5 * LEFT + 0.9 * DOWN)
    gp[1][0].shift(0.3 * UP)
    gp[1][1][0][1].scale(2).shift(0.03 * UP)
    gp[1][2].shift(0.3 * UP + 0.22 * RIGHT)

    return gp

def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
        
    return True