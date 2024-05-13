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

class Clock(Group):
    def __init__(self, **kwargs):
        self.hours = 0
        self.minutes = 0
        self.text_alignments = [Dot(1.1 * UP).rotate(-angle * PI / 180, about_point=ORIGIN) for angle in range(0, 360, 30)]
        self.clock_background = Circle(1.5, color=WHITE, fill_opacity=1, stroke_color=DARK_GRAY, stroke_width=15)
        self.small_ticks = [Line(1.4 * UP, 1.3 * UP, color=GRAY_D).rotate(angle * PI / 180, about_point=ORIGIN) for angle in range(0, 360, 6) if angle % 5 != 0]
        self.big_ticks = [Line(1.4 * UP, 1.25 * UP, color=DARK_GRAY).rotate(angle * PI / 180, about_point=ORIGIN) for angle in range(0, 360, 30)]
        self.number_texts = [Tex(num, color=DARK_GRAY).scale(0.4).move_to(self.text_alignments[i]) for [i, num] in enumerate(["12", *[str(num) for num in range(1, 12, 1)]])]
        self.minutes_pointer = RoundedRectangle(width=0.04, height=1, color=GRAY_C, corner_radius=0.02, fill_opacity=1).shift(0.4 * UP)
        self.hours_pointer = RoundedRectangle(width=0.04, height=0.7, color=DARK_GRAY, corner_radius=0.02, fill_opacity=1).shift(0.25 * UP)
        self.center_dot = Dot(ORIGIN, radius=0.025, stroke_color=BLACK, stroke_width=0.01)

        super().__init__(
            self.clock_background, 
            *self.small_ticks,
            *self.big_ticks,
            *self.number_texts,
            self.minutes_pointer,
            self.hours_pointer,
            self.center_dot,
            **kwargs
        )

    def set_time(self, hours, minutes):
        time_diff = (self.hours - hours % 12) * 60 + self.minutes - minutes
        self.hours = hours
        self.minutes = minutes

        return (
            Rotate(self.minutes_pointer, 2 * PI * time_diff / 60, about_point=self.get_center()),
            Rotate(self.hours_pointer, 2 * PI * time_diff / 720, about_point=self.get_center())
        )