from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Scizor(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        scizor = Group(
            ImageMobject("./assets/tesoura-baixo.png"),
            ImageMobject("./assets/tesoura-cima.png")
        )
        middle_point = Dot(0.55 * (RIGHT + UP))
        left_point = Dot(1.05 * RIGHT + 1.5 * UP, fill_opacity=0.001)
        right_point = Dot(1.48 * RIGHT + 1.25 * UP, fill_opacity=0.001)
        angle_middle = Dot(0.8 * (RIGHT + UP), fill_opacity=0.001)
        angle = always_redraw(lambda: 
            ArcPolygon(
                angle_middle.get_center(),
                right_point.get_center(),
                left_point.get_center(),
                fill_opacity=0.5,
                stroke_opacity=0.5,
                color=LIGHT_RED_COLOR,
                arc_config=[
                    {'angle': 0, 'color': LIGHT_RED_COLOR, 'stroke_opacity': 0.5},
                    {'color': LIGHT_RED_COLOR, 'stroke_opacity': 0.5},
                    {'angle': 0, 'color': LIGHT_RED_COLOR, 'stroke_opacity': 0.5}
                ]
            )
        )

        self.play(AnimateFromLeft(scizor), run_time=0.7)
        self.wait(1.5)   
        self.play(FadeIn(angle))  
        self.wait(1)
        self.play(
            scizor[1].animate.rotate(40 * DEGREES, about_point=middle_point.get_center()),
            left_point.animate.rotate(40 * DEGREES, about_point=middle_point.get_center()),
            angle_middle.animate.shift(0.08 * DOWN + 0.1 * LEFT),
            run_time=2
        )   
        self.wait(1)
        self.play(
            scizor[1].animate.rotate(-40 * DEGREES, about_point=middle_point.get_center()),
            left_point.animate.rotate(-40 * DEGREES, about_point=middle_point.get_center()),
            angle_middle.animate.shift(0.08 * UP + 0.1 * RIGHT),
            run_time=1.5
        )
        self.play(FadeOut(angle))
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)