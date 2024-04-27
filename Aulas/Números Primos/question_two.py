from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class QuestionTwo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        animal = ImageMobject("./assets/Asset 1.png")
        animal.scale(0.4)
        animal.shift(9 * LEFT)
        speech = SpeechBubble(color=TEXT_COLOR, fill_opacity=0.8, fill_color=BROWN_COLOR)
        speech.shift(3 * UP + 8 * LEFT)
        text = VGroup(
            Text("O número seis", color=WHITE),
            Text("é primo?", color=WHITE)
        )
        text.scale(0.6)
        text.arrange(DOWN, buff=0.1)
        text.shift(3 * UP + 8 * LEFT)

        self.play(
            animal.animate.shift(7 * RIGHT), 
            speech.animate.shift(9 * RIGHT), 
            text.animate.shift(9 * RIGHT), 
            run_time=0.7
        )
        self.wait(2)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.7)
        self.remove(*self.mobjects)