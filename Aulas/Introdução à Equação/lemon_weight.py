from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class LemonWeight(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        eletronic_balance = EletronicBalance()
        eletronic_balance.scale(1.5)
        eletronic_balance.shift(0.5 * DOWN)
        lemon = Lemon()
        lemon.scale(0.65)
        lemon.shift(10 * UP + 0.5 * LEFT)

        self.play(shift_from_left(eletronic_balance))
        self.wait(1)
        self.play(
            lemon.animate.shift(8.75 * DOWN), 
            rate_func=rate_functions.ease_out_circ, 
            run_time=0.7
        )
        self.play(
            eletronic_balance.set_weight(100), 
            run_time=2
        )
        self.wait(2)
        self.play(shift_to_left(eletronic_balance, lemon))
        self.remove(*self.mobjects)