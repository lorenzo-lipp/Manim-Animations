from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Probabilidade", color=LIGHT_PURPLE_COLOR)
        title.scale(2)
        title.shift(UP)
        dice = Dice()
        dice.rotate(35 * DEGREES, about_point=ORIGIN, axis=UP)
        dice.rotate(30 * DEGREES, about_point=ORIGIN, axis=RIGHT)
        dice.scale(0.8)
        roulette = Roulette()
        Group(title, Group(roulette, dice)).arrange(DOWN, buff=0.5)
        dice.shift(0.1 * DOWN + 1.4 * LEFT)
        roulette.shift(1.4 * RIGHT)

        self.play(Write(title))
        self.play(AnimateFromRight(dice), AnimateFromLeft(roulette))
        self.wait(1)

        self.play(Group(*self.mobjects).animate.scale(0).fade(1))
        self.remove(*self.mobjects)