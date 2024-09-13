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

class GeogebraLink(Group):
    """ A :class:`Group` with a title, an image and a link arranged vertically. """
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

class EletronicBalance(Group):  
    """ A :class:`Group` of :class:`MObjects <.MObject>` that emmulates an eletronic balance. """
    def __init__(self):
        self.top_border = RoundedRectangle(
            corner_radius=0.15, 
            color=DARK_BLUE, 
            height=0.25, 
            width=4, 
            fill_opacity=1, 
            stroke_width=1
        )
        self.bowl = ArcBetweenPoints(
            1.8 * LEFT, 
            1.8 * RIGHT, 
            radius=1.8,
            color=LIGHT_BLUE_COLOR,
            fill_opacity=1
        )
        self.bowl.stretch_to_fit_height(1.1)
        self.bowl.shift(0.22 * UP)
        self.bottom_border = RoundedRectangle(
            0.08, 
            color=DARK_BLUE, 
            height=0.2, 
            width=2, 
            fill_opacity=1, 
            stroke_width=1
        )
        self.bottom_border.shift(1.15 * DOWN)
        self.bottom_square = Polygon(
            1.4 * LEFT,
            1.7 * LEFT + 1.3 * DOWN,
            1.5 * LEFT + 1.3 * DOWN,
            1.4 * LEFT + 1.1 * DOWN,
            1.4 * RIGHT + 1.1 * DOWN,
            1.5 * RIGHT + 1.3 * DOWN,
            1.7 * RIGHT + 1.3 * DOWN,
            1.4 * RIGHT,
            color=LIGHT_BLUE_COLOR,
            fill_opacity=1, 
            stroke_width=1
        )
        self.bottom_square.shift(1.25 * DOWN)
        self.display = Polygon(
            0.6 * LEFT,
            0.7 * LEFT + 0.6 * DOWN,
            0.7 * RIGHT + 0.6 * DOWN,
            0.6 * RIGHT,
            color=DARK_BLUE,
            fill_color=WHITE,
            fill_opacity=1, 
            stroke_width=15
        )
        self.display.shift(1.5 * DOWN)
        self.weight = ValueTracker(0)
        self.display_text = Text("0 g", color=BLACK, font_size=18)
        self.display_text.move_to(self.display)

        super().__init__(
            self.top_border,
            self.bowl,
            self.bottom_border,
            self.bottom_square,
            self.display,
            self.display_text
        )
    
    def set_weight(self, weight):
        """ Returns an :class:`~.AnimationGroup` that changes weight display. """
        return AnimationGroup(
            self.weight.animate.set_value(weight),
            UpdateFromFunc(self.display_text, lambda m: m.become(
                Text(
                    f"{int(self.weight.get_value())} g", 
                    color=BLACK, 
                    font_size=26
                ).move_to(self.display)
            ))
        )

class PlatesBalance(Group):  
    """ A :class:`Group` of :class:`MObjects <.MObject>` that emmulates a plates balance. """
    def __init__(self):
        self.angle = 0
        self.moving_top_part = RoundedRectangle(
            corner_radius=0.05, 
            color=LIGHT_BLUE_COLOR, 
            height=0.13, 
            width=3.6, 
            fill_opacity=1, 
            stroke_width=1
        )
        self.column = RoundedRectangle(
            corner_radius=0.05, 
            color=LIGHT_BLUE_COLOR, 
            height=3.4, 
            width=0.13, 
            fill_opacity=1, 
            stroke_width=1
        ).shift(1.7 * DOWN)
        self.center_point = Dot(color=ORANGE_COLOR, radius=0.18)
        self.bottom_part = Group(
            RoundedRectangle(
                corner_radius=0.05, 
                color=DARK_BLUE, 
                height=0.16, 
                width=1, 
                fill_opacity=1, 
                stroke_width=1
            ).shift(3.4 * DOWN),
            RoundedRectangle(
                0.05, 
                color=LIGHT_BLUE_COLOR, 
                height=0.16, 
                width=1.5, 
                fill_opacity=1, 
                stroke_width=1
            ).shift(3.56 * DOWN)
        )
        self.left_plate = Group(
            Line(
                start=1.6 * LEFT, 
                end=1.9 * LEFT + 1.5 * DOWN, 
                color=ORANGE, 
                stroke_width=8
            ),
            Line(
                start=1.6 * LEFT, 
                end=1.3 * LEFT + 1.5 * DOWN, 
                color=ORANGE, 
                stroke_width=8
            ),
            ArcBetweenPoints(
                start=2.1 * LEFT + 1.5 * DOWN, 
                end=1.1 * LEFT + 1.5 * DOWN, 
                color=LIGHT_BLUE_COLOR,
                fill_opacity=1
            ).scale(1.5)
                .stretch_to_fit_height(0.55)
                .shift(0.16 * DOWN)
        )
        self.left_plate.move_to(
            self.moving_top_part.get_boundary_point(DL) + 0.1 * RIGHT, 
            aligned_edge=UP
        )
        self.right_plate = Group(
            Line(
                start=1.6 * RIGHT, 
                end=1.9 * RIGHT + 1.5 * DOWN, 
                color=ORANGE, 
                stroke_width=8
            ),
            Line(
                start=1.6 * RIGHT, 
                end=1.3 * RIGHT + 1.5 * DOWN, 
                color=ORANGE, 
                stroke_width=8
            ),
            ArcBetweenPoints( 
                start=1.1 * RIGHT + 1.5 * DOWN, 
                end=2.1 * RIGHT + 1.5 * DOWN,
                color=LIGHT_BLUE_COLOR,
                fill_opacity=1
            ).scale(1.5)
                .stretch_to_fit_height(0.55)
                .shift(0.16 * DOWN)
        )
        self.right_plate.move_to(
            self.moving_top_part.get_boundary_point(DR) + 0.1 * LEFT,
            aligned_edge=UP
        )

        super().__init__(
            self.left_plate,
            self.right_plate,
            self.moving_top_part,
            self.column,
            self.center_point,
            self.bottom_part,
        )
        self.center()

    def set_weight(self, left_weight, right_weight):
        """ Returns an :class:`~.AnimationGroup` that changes plates position based on weights. """
        bigger_weight = right_weight if right_weight > left_weight else left_weight
        signal = -1 if bigger_weight == right_weight else 1
        total_weight = left_weight + right_weight
        total_weight = total_weight if total_weight > 0 else 1
        new_angle = signal * (bigger_weight/total_weight) * 40 * DEGREES

        new_position = self.moving_top_part.copy().rotate(
            angle=new_angle - self.angle,
            about_point=self.center_point.get_center()
        )
        animations = AnimationGroup(
            self.left_plate.animate.move_to(
                new_position.get_boundary_point(DL) + 0.1 * RIGHT, 
                aligned_edge=UP
            ),
            self.right_plate.animate.move_to(
                new_position.get_boundary_point(DR) + 0.1 * LEFT,
                aligned_edge=UP
            ),
            self.moving_top_part.animate.rotate(
                angle=new_angle - self.angle,
                about_point=self.center_point.get_center()
            ),
            self.center_point.animate.rotate(angle=0),
            rate_func=linear
        )

        self.angle = new_angle

        return animations

class Lemon(ImageMobject):
    """ An :class:`ImageMObject` of a lemon. """
    
    def __init__(self, scale=0.5):
        super().__init__("./assets/limão.png")
        self.scale(scale)

class Apple(ImageMobject):
    """ An :class:`ImageMObject` of a apple. """
    
    def __init__(self, scale=0.5):
        super().__init__("./assets/maçã.png")
        self.scale(scale)

class Strawberry(ImageMobject):
    """ An :class:`ImageMObject` of a strawberry. """
    
    def __init__(self, scale=0.5):
        super().__init__("./assets/morango.png")
        self.scale(scale)

class Pear(ImageMobject):
    """ An :class:`ImageMObject` of a pear. """
    
    def __init__(self, scale=0.5):
        super().__init__("./assets/pêra.png")
        self.scale(scale)

class Grapes(ImageMobject):
    """ An :class:`ImageMObject` of grapes. """
    
    def __init__(self, scale=0.5):
        super().__init__("./assets/uva.png")
        self.scale(scale)