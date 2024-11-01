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

class Pizza(VGroup):
    """ A `VGroup` of `MObjects` that looks like a pizza """

    def __init__(self):
        super().__init__(
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
        
class Pepperonni(VGroup):
    """ A `VGroup` of `Circles` that looks like a pepperonni """

    def __init__(self):
        super().__init__(
            Circle(0.18, color="#d73d3d", fill_opacity=1),
            Circle(0.02, color="#f05454", fill_opacity=1).shift(0.07 * (UP + LEFT)),
            Circle(0.02, color="#f05454", fill_opacity=1).shift(0.07 * (UP + RIGHT)),
            Circle(0.03, color="#f05454", fill_opacity=1).shift(0.07 * (DOWN))
        )


class GeogebraLink(Group):
    """ A `Group` with a title, an image and a link arranged vertically """
    def __init__(self, title, img, link, text_scale=1.2, img_scale=0.8):
        text = Tex(r"\textbf{" + title + "}", color=DARK_BLUE_COLOR)
        text.scale(text_scale)
        img = ImageMobject("./assets/" + img + ".png")
        img.scale(img_scale)
        link = Tex(r"\textbf{Link: bit.ly/" + link + "}", color=DARK_BLUE_COLOR)   
        link[0][0:5].set(color=BLACK)

        super().__init__(text, img, link)
        self.arrange(DOWN, buff=0.5)
        self.shift(9 * RIGHT)

def shift_to_left(*mobjects, dist=9):
    """ Returns an `AnimationGroup` that shifts mobjects to left """

    return AnimationGroup(*[
        mobject.animate.shift(dist * LEFT) 
        for mobject in mobjects
    ])

def shift_from_left(*mobjects, dist=9):
    """ Shifts mobjects to right and returns an `AnimationGroup` that shifts mobjects back to the initial position """

    return AnimationGroup(*[
        mobject.shift(dist * RIGHT).animate.shift(dist * LEFT) 
        for mobject in mobjects
    ])