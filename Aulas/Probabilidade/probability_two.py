from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ProbabilityTwo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        dice = Dice(side_length=3)
        dice.rotate(35 * DEGREES, about_point=ORIGIN, axis=UP)
        dice.rotate(30 * DEGREES, about_point=ORIGIN, axis=RIGHT)
        dice_2 = Dice(side_length=2)
        dice_2.rotate(90 * DEGREES, about_point=ORIGIN, axis=UP)
        dice_2.shift(DOWN + 3 * LEFT)
        dice_3 = Dice(side_length=2)
        dice_3.rotate(-90 * DEGREES, about_point=ORIGIN, axis=RIGHT)
        dice_3[5].fade(1)
        dice_3.shift(DOWN)
        dice_4 = Dice(side_length=2)
        dice_4.shift(DOWN + 3 * RIGHT)
        dice_5 = Dice(side_length=2)
        dice_5.rotate(-90 * DEGREES, about_point=ORIGIN, axis=UP)
        dice_5.shift(5 * DOWN + 1.5 * LEFT)
        dice_5[4].fade(1)
        dice_6 = Dice(side_length=2)
        dice_6.shift(5 * DOWN + 1.5 * RIGHT)
        text_1 = Text("Pares:", color=TEXT_COLOR)
        text_1.shift(0.8 * UP)
        text_2 = Text("Maiores que 4:", color=TEXT_COLOR)
        text_2.shift(3.2 * DOWN)
    
        self.play(AnimateFromLeft(dice))
        self.wait(1)
        self.play(dice.animate.shift(4 * UP))
        self.play(Write(text_1), run_time=0.8)
        self.play(Transform(dice.copy(), dice_2))
        self.play(Transform(dice.copy(), dice_3))
        self.play(Transform(dice.copy(), dice_4))
        self.wait(1)
        self.play(Write(text_2), run_time=0.8)
        self.play(Transform(dice.copy(), dice_5))
        self.play(Transform(dice.copy(), dice_6))
        self.remove(*self.mobjects)