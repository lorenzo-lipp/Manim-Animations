from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SequenceFour(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        pyramids = VGroup(
            VGroup(Pyramid(1), MathTex("1", color=TEXT_COLOR).scale(1.5))
                .arrange(DOWN, buff=0.4),
            VGroup(Pyramid(2), MathTex("3", color=TEXT_COLOR).scale(1.5))
                .arrange(DOWN, buff=0.4),
            VGroup(Pyramid(3), MathTex("6", color=TEXT_COLOR).scale(1.5))
                .arrange(DOWN, buff=0.4),
            VGroup(Pyramid(4), MathTex("10", color=TEXT_COLOR).scale(1.5))
                .arrange(DOWN, buff=0.4)
        ).arrange(DOWN, buff=1.5)

        pyramids.shift(4 * DOWN)

        self.play(FadeIn(pyramids), run_time=0.7)
        self.wait(7)
        self.play(self.camera.frame.animate.shift(11 * DOWN), run_time=3, rate_func=rate_functions.ease_out_quad)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)