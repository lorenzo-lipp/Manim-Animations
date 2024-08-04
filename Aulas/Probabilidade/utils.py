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

def AnimateFromRight(*mobjects):
    return Group(*mobjects).shift(9 * LEFT).animate.shift(9 * RIGHT)

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

class Roulette(Group):
    def __init__(self, **kwargs):
        self.roulette_base = [
            Polygon(
                [-0.35, -0.95, 0],
                [0.35, -0.95, 0],
                [0.7, -1.45, 0],
                [-0.7, -1.45, 0],
                [-0.35, -0.95, 0],
                color="#9e9e9e",
                fill_opacity=1
            ),
            Polygon(
                [0.8, -1.45, 0],
                [0.8, -1.55, 0],
                [-0.8, -1.55, 0],
                [-0.8, -1.45, 0],
                color=GRAY_D,
                fill_opacity=1
            )
        ]
        self.roulette_background = Circle(radius=1.1, color="#c8c8c8", fill_opacity=1)
        self.roulette_sectors = [
            Sector(color=LIGHT_BLUE_COLOR, angle=PI / 4, start_angle=PI / 2, fill_opacity=1),
            Sector(color=LIGHT_RED_COLOR, angle=PI / 4, start_angle=PI / 2 + PI / 4, fill_opacity=1),
            Sector(color=LIGHT_PURPLE_COLOR, angle=PI / 4, start_angle=PI, fill_opacity=1),
            Sector(color=LIGHT_GREEN_COLOR, angle=PI / 4, start_angle=PI + PI / 4, fill_opacity=1),
            Sector(color=LIGHT_BLUE_COLOR, angle=PI / 4, start_angle=PI + PI / 2, fill_opacity=1),
            Sector(color=LIGHT_RED_COLOR, angle=PI / 4, start_angle=PI + 3 * PI / 4, fill_opacity=1),
            Sector(color=LIGHT_GREEN_COLOR, angle=PI / 4, start_angle=2 * PI, fill_opacity=1),
            Sector(color=LIGHT_RED_COLOR, angle=PI / 4, start_angle=2 * PI + PI / 4, fill_opacity=1)
        ]
        self.roulette_spin = [
            Polygon(
                [-0.1, 0.1, 0],
                [0.1, 0.1, 0],
                [0, 0.3, 0],
                [-0.1, 0.1, 0],
                color="#c75a06",
                stroke_color=WHITE, 
                stroke_width=2,
                fill_opacity=1
            ),
            Circle(radius=0.2, color="#FF9933", fill_opacity=1, stroke_color=WHITE, stroke_width=2),
            Circle(radius=0.1, color="#c75a06", fill_opacity=0.6)
        ]
        self.roulette_angle = 0

        super().__init__(
            *self.roulette_base,
            self.roulette_background,
            *self.roulette_sectors,
            *self.roulette_spin,
            **kwargs
        )

    def spin(self, angle, **kwargs):
        self.roulette_angle = (self.roulette_angle + angle) % (2 * PI)
        return [Rotate(sector, about_point=self.roulette_background.get_center(), angle=angle, **kwargs) for sector in self.roulette_sectors]
    
    def flash_selected(self):
        return self.get_selected().animate(rate_func=lambda t: smooth(0.8 * t if t < 0.5 else 0.8 * (1 - t), 10)).set_color(WHITE)
    
    def get_selected(self):
        return self.roulette_sectors[7 - int(self.roulette_angle / (PI / 4))]
    
class Dice(VGroup):
    def __init__(self, side_length = 2, **kwargs):
        self.side_length = side_length
        faces = []

        for vect in RIGHT, DOWN, IN, OUT, LEFT, UP:
            square = Square(side_length=self.side_length, fill_color=LIGHT_RED_COLOR, fill_opacity=1)
            circles = self.get_circles(vect)
            face = VGroup(square, *circles)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            faces.append(face)
        
        super().__init__(*faces, **kwargs)

    def get_circles(self, vect):
        circle_size = 0.1 * self.side_length

        if np.array_equal(vect, IN):
            return [Circle(circle_size, WHITE, fill_opacity=1)]
        elif np.array_equal(vect, OUT):
            return [
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UR),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * RIGHT),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DR),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UL),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * LEFT),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DL)
            ]
        elif np.array_equal(vect, UP):
            return [
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UR),
                Circle(circle_size, WHITE, fill_opacity=1),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DL)
            ]
        elif np.array_equal(vect, DOWN):
            return [
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UR),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DR),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UL),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DL)
            ]
        elif np.array_equal(vect, RIGHT):
            return [
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UR),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DR),
                Circle(circle_size, WHITE, fill_opacity=1),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UL),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DL)
            ]
        elif np.array_equal(vect, LEFT):
            return [
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * UR),
                Circle(circle_size, WHITE, fill_opacity=1).shift(0.3 * self.side_length * DL)
            ]