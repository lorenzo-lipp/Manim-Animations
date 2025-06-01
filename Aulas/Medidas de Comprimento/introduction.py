from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("O que são Medidas", color="#a346eb")
                .scale(2),
            Tex("de Comprimento?", color="#a346eb")
                .scale(2)
        )
        title.arrange(DOWN, buff=0.3)
        ruler = Ruler()
        ruler.scale(2)
        ruler.shift(2 * DOWN)
        measuring_tape = MeasuringTape()
        measuring_tape.scale(2)
        measuring_tape.shift(2 * UP)

        self.play(LaggedStart(
            Write(title),
            SpinInFromNothing(ruler),
            AnimateFromRight(measuring_tape),
            lag_ratio=0.3
        ))
        self.wait(0.5)
        self.play(measuring_tape.moving_part.animate.shift(4.6 * LEFT))
        self.wait(0.5)
        self.play(AnimateToLeft(Group(*self.mobjects)), run_time=0.7)
        self.remove(*self.mobjects)