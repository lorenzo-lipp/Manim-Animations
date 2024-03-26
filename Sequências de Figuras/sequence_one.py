from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SequenceOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        animals = [Sloth, Crab]
        sequence = Group(*[animals[i % 2]() for i in range(6)])
        sequence.arrange(DOWN, buff=0.6)
        missing = sequence[4]
        sequence.remove(missing)
        question_mark = MathTex("?", color=TEXT_COLOR)
        question_mark.scale(3)
        question_mark.move_to(missing)

        self.play(FadeIn(sequence, question_mark))
        self.wait(3)
        self.play(FadeOut(question_mark), run_time=0.3)
        self.play(FadeIn(missing), run_time=0.6)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)