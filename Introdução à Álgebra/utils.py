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

def MathOperation(path, expression_text):
    image = ImageMobject(path)
    expression = Tex(expression_text, color=BLACK)
    expression.scale(1.8)
    group = Group(image, expression)
    group.arrange(RIGHT, buff=0.25)

    return group

def MonsterSum(path, times, result_text):
    image = ImageMobject(path)
    plus = Tex("+", color=BLACK)
    result = Tex(result_text, color=BLACK)
    result.scale(1.8)
    group = Group()

    for i in range(times - 1):
        group.add(image.copy())
        group.add(plus.copy())

    group.add(image.copy())
    group.add(result)
    group.arrange(RIGHT, buff=0.25)

    return group

def LetterOperation(expression, expression_result):
    inner_group = Group(
        Tex(expression, color=TEXT_COLOR).scale(1.8),
        Tex(expression_result, color=TEXT_COLOR).scale(1.8),
    ).arrange(DOWN, buff=0.8)
    box = DashedVMobject(
        SurroundingRectangle(inner_group, color=AQUA_BLUE_COLOR, buff=0.5),
        num_dashes=25,
        dashed_ratio=0.7
    )
    outer_group = Group(
        box,
        inner_group
    )

    return outer_group