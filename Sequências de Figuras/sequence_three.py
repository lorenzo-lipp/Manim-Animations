from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SequenceThree(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        animals = [Toucan, Feather,Alligator]
        sequence = Group(*[animals[i % 3]().scale(0.65) for i in range(15)])
        sequence.arrange(DOWN, buff=0.25)
        sequence.shift(5 * DOWN)
        nums = Group(*[
            MathTex(str(i + 1), color=LIGHT_RED_COLOR)
                .scale(2)
                .next_to(sequence[i], LEFT, buff=0.4) 
            for i in range(15)
        ])
        missing1 = sequence[8]
        missing2 = sequence[12]
        missing3 = sequence[14]
        sequence.remove(missing1)
        sequence.remove(missing2)
        sequence.remove(missing3)
        question_mark = MathTex("?", color=TEXT_COLOR)
        question_mark.scale(3)
        question_mark.move_to(missing1)

        self.play(FadeIn(sequence, question_mark))
        self.wait(3)
        self.play(FadeOut(question_mark), run_time=0.3)
        self.play(FadeIn(missing1), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(nums))

        question_mark.move_to(missing2)

        self.add(question_mark)
        self.play(self.camera.frame.animate.shift(7 * DOWN), run_time=2.5, rate_func=rate_functions.ease_out_quad)
        self.wait(1)
        self.play(FadeOut(question_mark), run_time=0.3)
        self.play(FadeIn(missing2), run_time=0.6)
        self.wait(2)

        question_mark.move_to(missing3)

        self.add(question_mark)
        self.play(self.camera.frame.animate.shift(2.5 * DOWN), run_time=1.5, rate_func=rate_functions.ease_out_quad)
        self.wait(1)
        self.play(FadeOut(question_mark), run_time=0.3)
        self.play(FadeIn(missing3), run_time=0.6)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)