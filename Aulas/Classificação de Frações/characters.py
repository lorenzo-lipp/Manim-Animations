from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Characters(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        pietro = Pietro()
        julia = Julia()
        augusto = Augusto()
        Group(pietro, julia, augusto).arrange(RIGHT, buff=0.3)

        self.play(LaggedStart(
            GrowFromCenter(pietro, rate_func=rate_functions.ease_out_bounce, run_time=1.3),
            GrowFromCenter(julia, rate_func=rate_functions.ease_out_bounce, run_time=1.3),
            GrowFromCenter(augusto, rate_func=rate_functions.ease_out_bounce, run_time=1.3),
            lag_ratio=0.35
        ))
        self.wait(1)
        self.play(
            FadeOut(pietro),
            FadeOut(augusto)
        )
        self.remove(*self.mobjects)