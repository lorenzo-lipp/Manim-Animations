from manim import *

BACKGROUND_COLOR = "#faf4e1"
TEXT_COLOR = "#434343"
LIGHT_RED_COLOR = "#f55e61"
LIGHT_BLUE_COLOR = "#408ef5"
LIGHT_ORANGE_COLOR = "#e3883d"
LIGHT_PURPLE_COLOR = "#a346eb"
AQUA_GREEN_COLOR = "#0dc786"

def running_start(t):
    return rate_functions.running_start(t, -0.3)

def FibonacciSquare(size, color):
    rect = Square(size / 5, color=color)
    text = Tex(f"{size}", color=color)
    text.scale(3 * min(1, size / 12))
    text.move_to(rect)

    return Group(rect, text)