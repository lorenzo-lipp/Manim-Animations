from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SmallerPrime(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        animal_1 = ImageMobject("./assets/Asset 2 - Flipped.png")
        animal_1.scale(0.4)
        animal_1.shift(9 * LEFT)
        animal_2 = ImageMobject("./assets/Asset 3.png")
        animal_2.scale(0.4)
        animal_2.shift(9 * RIGHT)
        animal_3 = ImageMobject("./assets/Asset 1.png")
        animal_3.scale(0.4)
        animal_3.shift(9 * RIGHT)
        speech_1 = SpeechBubble(color=TEXT_COLOR, fill_opacity=0.8, fill_color=LIGHT_PURPLE_COLOR)
        speech_1.shift(3 * UP + 7 * LEFT)
        speech_2 = SpeechBubble(color=TEXT_COLOR, fill_opacity=0.8, fill_color=LIGHT_RED_COLOR)
        speech_2.shift(3 * UP + 7 * RIGHT).flip(UP)
        speech_3 = SpeechBubble(color=TEXT_COLOR, fill_opacity=0.8, fill_color=BROWN_COLOR)
        speech_3.shift(3 * UP + 7 * RIGHT).flip(UP)
        text_1 = VGroup(
            Text("E qual é o menor", color=WHITE),
            Text("número primo?", color=WHITE)
        )
        text_1.scale(0.6)
        text_1.arrange(DOWN, buff=0.1)
        text_1.shift(3 * UP + 7 * LEFT)
        text_2 = VGroup(
            Text("O menor primo", color=WHITE),
            Text("é o dois!", color=WHITE),
        )
        text_2.scale(0.6)
        text_2.arrange(DOWN, buff=0.1)
        text_2.shift(3.03 * UP + 7 * RIGHT)
        text_3 = VGroup(
            Text("O número um não", color=WHITE),
            Text("é primo, pois tem", color=WHITE),
            Text("um só divisor.", color=WHITE)
        )
        text_3.scale(0.6)
        text_3.arrange(DOWN, buff=0.1)
        text_3.shift(3.03 * UP + 7 * RIGHT)
        text_3[1].shift(0.03 * DOWN)

        self.play(
            animal_1.animate.shift(7 * RIGHT), 
            speech_1.animate.shift(8 * RIGHT),
            text_1.animate.shift(8 * RIGHT),
            run_time=0.7
        )
        self.wait(1.7)
        self.play(
            animal_1.animate.shift(9 * LEFT), 
            speech_1.animate.shift(9 * LEFT),
            text_1.animate.shift(9 * LEFT),
            animal_2.animate.shift(7 * LEFT), 
            speech_2.animate.shift(8 * LEFT), 
            text_2.animate.shift(8 * LEFT), 
            run_time=0.7
        )
        self.wait(1.9)
        self.play(
            animal_2.animate.shift(9 * LEFT), 
            speech_2.animate.shift(9 * LEFT),
            text_2.animate.shift(9 * LEFT),
            animal_3.animate.shift(7 * LEFT), 
            speech_3.animate.shift(8 * LEFT), 
            text_3.animate.shift(8 * LEFT), 
            run_time=0.7
        )
        self.wait(2.4)
        self.play(
            animal_3.animate.shift(9 * LEFT), 
            speech_3.animate.shift(9 * LEFT),
            text_3.animate.shift(9 * LEFT),
            run_time=0.7
        )
        self.remove(*self.mobjects)
