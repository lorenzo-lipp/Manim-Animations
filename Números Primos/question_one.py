from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class QuestionOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        animal_1 = ImageMobject("./assets/Asset 2 - Flipped.png")
        animal_1.scale(0.4)
        animal_1.shift(9 * LEFT)
        animal_2 = ImageMobject("./assets/Asset 3.png")
        animal_2.scale(0.4)
        animal_2.shift(9 * RIGHT)
        animal_3 = ImageMobject("./assets/Asset 4.png")
        animal_3.scale(0.4)
        animal_3.shift(9 * RIGHT)
        speech_1 = SpeechBubble(color=TEXT_COLOR, fill_opacity=0.8, fill_color=LIGHT_PURPLE_COLOR)
        speech_1.shift(3 * UP + 8 * LEFT)
        speech_2 = SpeechBubble(color=TEXT_COLOR, fill_opacity=0.8, fill_color=LIGHT_RED_COLOR)
        speech_2.shift(3 * UP + 8 * RIGHT)
        speech_2.flip(UP)
        speech_3 = speech_2.copy()
        speech_3.set(fill_color=GREEN_COLOR)
        text_1 = VGroup(
            Text("O que são", color=WHITE),
            Text("números primos?", color=WHITE)
        )
        text_1.scale(0.6)
        text_1.arrange(DOWN, buff=0.1)
        text_1.shift(3 * UP + 8 * LEFT)
        text_2 = VGroup(
            Text("São números que", color=WHITE),
            Text("têm somente dois", color=WHITE),
            Text("divisores,", color=WHITE)
        )
        text_2.scale(0.6)
        text_2.arrange(DOWN, buff=0.1)
        text_2.shift(3.03 * UP + 8 * RIGHT)
        text_2[2].shift(0.1 * DOWN)
        text_3 = VGroup(
            Text("1 e ele", color=WHITE),
            Text("mesmo.", color=WHITE)
        )
        text_3.scale(0.6)
        text_3.arrange(DOWN, buff=0.3)
        text_3.shift(3.03 * UP + LEFT)
        text_4 = VGroup(
            Text("O número cinco", color=WHITE),
            Text("é primo?", color=WHITE)
        )
        text_4.scale(0.6)
        text_4.arrange(DOWN, buff=0.2)
        text_4.shift(3 * UP + 8 * RIGHT)

        self.play(
            animal_1.animate.shift(7 * RIGHT), 
            speech_1.animate.shift(9 * RIGHT),
            text_1.animate.shift(9 * RIGHT),
            run_time=0.7
        )
        self.wait(1.5)
        self.play(
            animal_1.animate.shift(9 * LEFT), 
            speech_1.animate.shift(9 * LEFT), 
            text_1.animate.shift(9 * LEFT), 
            animal_2.animate.shift(7 * LEFT), 
            speech_2.animate.shift(9 * LEFT), 
            text_2.animate.shift(9 * LEFT), 
            run_time=0.7
        )
        self.wait(1)
        self.play(
            FadeOut(text_2),
            FadeIn(text_3), 
            run_time=0.5
        )
        self.wait(1)
        self.play(
            animal_2.animate.shift(9 * LEFT), 
            speech_2.animate.shift(9 * LEFT), 
            text_3.animate.shift(9 * LEFT), 
            animal_3.animate.shift(7 * LEFT), 
            speech_3.animate.shift(9 * LEFT), 
            text_4.animate.shift(9 * LEFT), 
            run_time=0.7
        )
        self.wait(1.5)
        self.play(
            animal_3.animate.shift(9 * LEFT), 
            speech_3.animate.shift(8 * LEFT), 
            text_4.animate.shift(8 * LEFT), 
            run_time=0.7
        )
        self.remove(*self.mobjects)