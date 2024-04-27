from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Sequências", color=LIGHT_PURPLE_COLOR),
            Tex("de Figuras", color=LIGHT_PURPLE_COLOR)
        ).arrange(DOWN, buff=0.1)
        title.scale(2.2)
        fig1 = Alligator()
        fig2 = Sloth()
        fig3 = Crab()
        fig4 = Toucan()
        Group(
            Group(fig1, fig2).arrange(RIGHT, buff=2),
            title,
            Group(fig3, fig4).arrange(RIGHT, buff=2)
        ).arrange(DOWN, buff=0.5)

        self.play(Write(title), run_time=0.7)
        self.play(
            LaggedStart(
                SpinInFromNothing(fig1),
                SpinInFromNothing(fig2),
                SpinInFromNothing(fig3),
                SpinInFromNothing(fig4),
                lag_ratio=0.15
            )
        )
        self.wait(0.6)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.5)
        self.remove(*self.mobjects)