from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ComparingWeight(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        lemon = Lemon()
        lemon.scale(0.65)
        lemon.shift(10 * UP + 3 * RIGHT)
        lemon_copy = lemon.copy()
        plates_balance = PlatesBalance()
        plates_balance.scale(1.8)
        plates_balance.shift(DOWN)
        apple = Apple()
        apple.scale(0.55)
        apple.shift(10 * UP + 3 * LEFT)

        self.play(FadeIn(plates_balance))
        self.remove(plates_balance)
        self.add(apple, lemon, lemon_copy, plates_balance)
        self.play(
            lemon.animate.shift(9.9 * DOWN), 
            apple.animate.shift(9.8 * DOWN), 
            rate_func=rate_functions.ease_out_circ, 
            run_time=0.7
        )
        self.wait(0.5)
        self.play(
            plates_balance.set_weights(200, 100),
            apple.animate.shift(1.3 * DOWN + 0.18 * RIGHT),
            lemon.animate.shift(1.3 * UP + 0.18 * LEFT)
        )
        self.wait(2)
        self.play(
            lemon_copy.move_to(lemon).animate.shift(0.5 * RIGHT),
            lemon.animate.shift(LEFT)
        )
        self.play(
            plates_balance.set_weights(0, 0),
            apple.animate.shift(1.3 * UP + 0.18 * LEFT),
            lemon_copy.animate.shift(1.3 * DOWN + 0.18 * RIGHT),
            lemon.animate.shift(1.3 * DOWN + 0.18 * RIGHT)
        )
        self.wait(1)
        self.play(shift_to_left(*self.mobjects, dist=10))
        self.remove(*self.mobjects)