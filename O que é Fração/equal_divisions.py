from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class EqualDivisions(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Dividida em partes iguais", color=BLACK)
        title.scale(1.5)
        title.shift(4 * UP)
        title[0][10:].set_color("#a346eb")
        rect = Rectangle(color=LIGHT_RED_COLOR, height=3, width=4, fill_opacity=0.3)
        rect_vdiv = Line(rect.get_top(), rect.get_bottom(), color=LIGHT_RED_COLOR)
        rect_hdiv = Line(rect.get_left(), rect.get_right(), color=LIGHT_RED_COLOR)
        circ = Circle(1.5, color=LIGHT_GREEN_COLOR, fill_opacity=0.3)
        circ_div = Line(circ.get_top(), circ.get_bottom(), color=LIGHT_GREEN_COLOR)
        rect_divisions = VGroup(
            rect_vdiv.copy().shift(RIGHT),
            rect_vdiv.copy(),
            rect_vdiv.copy().shift(LEFT),
            rect_hdiv.copy().shift(1/2 * UP),
            rect_hdiv.copy().shift(- 1/2 * UP)
        )
        circ_divisions = VGroup(*[circ_div.copy().rotate(i * 45 * DEGREES) for i in range(8)])
        circ_n_rect = VGroup(
            VGroup(rect, rect_divisions), 
            VGroup(circ, circ_divisions)
        )
        circ_n_rect.arrange(DOWN, buff=1)

        self.play(
            Create(rect),
            Create(circ),
            run_time=1.5
        )
        self.play(Create(rect_divisions))
        self.play(Create(circ_divisions), run_time=1.8)
        self.play(circ_n_rect.animate.shift(DOWN), run_time=0.2)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)
        self.play(
            circ_n_rect.animate.shift(9 * LEFT), 
            title.animate.shift(9 * LEFT),
            run_time=0.8
        )
        self.remove(circ_n_rect, title)