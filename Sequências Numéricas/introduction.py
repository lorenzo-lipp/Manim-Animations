from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Sequências"), 
            Tex("Numéricas")
        )
        title.arrange(DOWN)

        inner_box = Square(2.7, stroke_color=WHITE)
        outer_box = Square(3.7, color=RED, fill_opacity=1, stroke_color=WHITE)

        number_group_1 = ImageMobject("./assets/NumberGroup1.png")
        number_group_1.next_to(outer_box, LEFT)
        number_group_1.shift(7 * UP + 1.7 * RIGHT)
        number_group_1.scale(0.4)

        number_group_2 = ImageMobject("./assets/NumberGroup2.png")
        number_group_2.next_to(outer_box, RIGHT)
        number_group_2.shift(7 * UP + 2.1 * LEFT)
        number_group_2.scale(0.4)

        rectangle_group_1 = Rectangle(color=RED, height=0.05, width=2, fill_opacity=1)
        rectangle_group_1.next_to(outer_box, LEFT)
        rectangle_group_1.shift(0.6 * UP + 0.2 * RIGHT)

        rectangle_group_2 = Rectangle(color=RED, height=0.05, width=2.5, fill_opacity=1)
        rectangle_group_2.next_to(outer_box, RIGHT)
        rectangle_group_2.shift(0.6 * DOWN + 0.2 * LEFT)
        

        self.play(
            FadeIn(rectangle_group_1),
            FadeIn(rectangle_group_2),
            FadeIn(outer_box),
            FadeIn(inner_box),
            FadeIn(title)
        )
        self.play(
            number_group_1.animate.shift(6 * DOWN), 
            rate_func=rate_functions.rush_from
        )
        self.wait(0.8)
        self.play(
            number_group_2.animate.shift(7.2 * DOWN), 
            rate_func=rate_functions.rush_from, 
            run_time=1.2
        )
        self.wait(1.5)
        self.play(*[
            mobject.animate(rate_func=running_start, run_time=1.3).shift(LEFT * 15) 
            for mobject in self.mobjects
        ])
        self.remove(*self.mobjects)