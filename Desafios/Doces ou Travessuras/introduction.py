from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Hora do", color=LIGHT_RED_COLOR).scale(2.5),
            Tex("Desafio", color=LIGHT_RED_COLOR).scale(2.5)
        ).arrange(DOWN, buff=0.5)
        title.shift(UP)
        percent = ValueTracker(0)
        pumpkin_head = always_redraw(lambda: 
            ImageMobject("./assets/003.png")
                .next_to(title, DOWN, 1)
                .shift((1 - percent.get_value()) * 6 * RIGHT)
                .rotate(360 * DEGREES * (1 - percent.get_value()))
        )

        self.add(pumpkin_head)
        self.play(
            SpinInFromNothing(title, run_time=0.7),
            percent.animate(run_time=1.4).set_value(1)
        )
        self.wait(1)
        self.play(AnimateToLeft(title), run_time=0.7)
        self.remove(*self.mobjects)