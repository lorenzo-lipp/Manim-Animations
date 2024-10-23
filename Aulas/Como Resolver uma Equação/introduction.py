from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Como Resolver", color=LIGHT_GREEN_COLOR).scale(2),
            VGroup(
                Tex("uma", color=LIGHT_GREEN_COLOR).scale(2),
                Tex("Equação", color=LIGHT_BLUE_COLOR).scale(2),
            ).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, buff=0.4)
        equals = MathTex("=", color=LIGHT_BLUE_COLOR)
        equals.scale(4)
        equals.move_to(title[1][1])

        self.play(SpinInFromNothing(title))
        self.wait(1)
        self.play(Transform(title[1][1], equals))
        self.wait(0.5)
        self.play(shift_to_left(*self.mobjects))
        self.remove(*self.mobjects)