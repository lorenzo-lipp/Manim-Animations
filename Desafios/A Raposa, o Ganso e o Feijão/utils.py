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

def Background():
    return ImageMobject("./assets/001.png").scale(0.55)

class StateImg(Group):
    def __init__(self, *images, **kwargs):
        super().__init__(**kwargs)
        self.images = images
        self.state = 0
        self.add(self.images[0])

    def change_state(self):
        self.state = (self.state + 1) % 2

        if self.state == 1:
            self.images[1].move_to(self.images[0])
            self.remove(self.images[0])
            self.add(self.images[1])
        else:
            self.images[0].move_to(self.images[1])
            self.remove(self.images[1])
            self.add(self.images[0])

class Fox(StateImg):
    def __init__(self, **kwargs):
        super().__init__(
            ImageMobject("./assets/002.png").scale(0.8), 
            ImageMobject("./assets/003.png").scale(0.025), 
            **kwargs
        )
    
class Goose(StateImg):
    def __init__(self, **kwargs):
        super().__init__(
            ImageMobject("./assets/005.png").scale(1.2), 
            ImageMobject("./assets/006.png").scale(0.3), 
            **kwargs
        )
    
class Beans(StateImg):
    def __init__(self, **kwargs):
        super().__init__(
            ImageMobject("./assets/004.png").scale(0.6), 
            ImageMobject("./assets/008.png").scale(0.15), 
            **kwargs
        )
    
class Farmer(StateImg):
    def __init__(self, **kwargs):
        super().__init__(
            ImageMobject("./assets/009.png").shift(0.5 * RIGHT).scale(0.6),
            ImageMobject("./assets/010.png").shift(0.5 * RIGHT).scale(0.6),
            **kwargs
        )
        self.add_to_back(ImageMobject("./assets/007.png").scale(0.6))