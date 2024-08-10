from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Volume(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        cup = Cup()
        cup_background = cup[0]
        cup_foreground = cup[1:]
        water = Water(0.2)
        water.move_to(cup_foreground, aligned_edge=DOWN)
        measurement_text = VGroup(
            Tex("Capacidade", color=LIGHT_RED_COLOR),
            Tex("(litros ou mililitros)", color=LIGHT_RED_COLOR)
        ).arrange(DOWN, buff=0.5)
        measurement_text[0].scale(2)
        measurement_text.next_to(cup, DOWN, buff=0.9)

        self.play(AnimateFromLeft(cup_background, water, cup_foreground))
        self.wait(0.6)

        for i in range(3, 9):
            self.play(
                Transform(water, Water(i / 10).move_to(cup_foreground, aligned_edge=DOWN)), 
                run_time=0.4, 
                rate_func=linear
            )

        self.wait(1)
        self.play(Write(measurement_text))
        self.wait(3)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)
        