from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class GrapesWeight(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        apple = Apple()
        apple.scale(0.65)
        apple.shift(10 * UP + 3 * RIGHT)
        lemon = Lemon()
        lemon.scale(0.55)
        lemon.shift(10 * UP + 3 * RIGHT)
        plates_balance = PlatesBalance()
        plates_balance.scale(1.8)
        plates_balance.shift(DOWN)
        grapes = Grapes()
        grapes.scale(0.65)
        grapes.shift(10 * UP + 3 * LEFT)
        question_tracker = ValueTracker(0)
        question_mark = always_redraw(lambda: 
            Tex("?", color=ORANGE_COLOR)
                .scale(6)
                .shift(question_tracker.get_value() * 6 * RIGHT)
                .rotate(360 * DEGREES * (1 - question_tracker.get_value()))
        )

        self.play(FadeIn(plates_balance))
        self.remove(plates_balance)
        self.add(grapes, lemon, apple, plates_balance)
        self.play(
            apple.animate.shift(9.9 * DOWN), 
            grapes.animate.shift(9.8 * DOWN), 
            rate_func=rate_functions.ease_out_circ, 
            run_time=0.7
        )
        self.wait(0.5)
        self.play(
            plates_balance.set_weights(300, 200),
            grapes.animate.shift(1.4 * DOWN + 0.18 * RIGHT),
            apple.animate.shift(1.3 * UP + 0.18 * LEFT)
        )
        self.wait(2)
        self.play(
            lemon.move_to(apple).animate.shift(LEFT),
            apple.animate.shift(0.5 * RIGHT)
        )
        self.play(
            plates_balance.set_weights(0, 0),
            grapes.animate.shift(1.4 * UP + 0.18 * LEFT),
            apple.animate.shift(1.3 * DOWN + 0.18 * RIGHT),
            lemon.animate.shift(1.3 * DOWN + 0.18 * RIGHT),
            run_time=1.3
        )
        self.wait(1)
        self.play(
            FadeOut(*self.mobjects),
            FadeIn(question_mark)
        )
        self.wait(1)
        self.play(question_tracker.animate.set_value(1))
        self.remove(*self.mobjects)