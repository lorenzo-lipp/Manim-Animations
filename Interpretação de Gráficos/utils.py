from manim import *

BACKGROUND_COLOR = "#faf4e1"
TEXT_COLOR = "#434343"
LIGHT_RED_COLOR = "#f55e61"
LIGHT_GREEN_COLOR = "#5fcb50"
LIGHT_BLUE_COLOR = "#408ef5"
LIGHT_ORANGE_COLOR = "#e3883d"
LIGHT_PURPLE_COLOR = "#a346eb"
LIGHT_YELLOW_COLOR = "#f9e24c"
AQUA_GREEN_COLOR = "#0dc786"
GREEN_COLOR = "#34a853"
DARK_RED_COLOR = "#bf2626"
DARK_BLUE_COLOR = "#3333FF"
SAND_COLOR = "#b3a77d"
BROWN_COLOR = "#b85842"

class NoGradientBarChart(BarChart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _update_colors(self):
        for i in range(len(self.bar_colors)):
            self.bars[i].set(color=self.bar_colors[i])

def add_to_back(self, *mobjects):
    all_mobjects = [*self.mobjects]

    self.remove(*self.mobjects)
    self.add(*mobjects, *all_mobjects)
