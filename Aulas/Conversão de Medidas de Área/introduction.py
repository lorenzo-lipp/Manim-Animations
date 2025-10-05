from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Convertendo Medidas", color=LIGHT_BLUE_COLOR)
                .scale(1.8),
            Tex("de Área", color=LIGHT_BLUE_COLOR)
                .scale(1.8)
        )
        title.arrange(DOWN, buff=0.3)
        title.shift(1.2 * UP)
        square_gp = Group(
            Square(2, color=LIGHT_BLUE_COLOR, fill_opacity=0.3),
            MathTex("1cm^2", color=LIGHT_BLUE_COLOR)
        ).shift(1.2 * DOWN)
        

        self.play(Write(title), run_time=1.2)
        self.play(AnimateFromRight(square_gp))
        self.wait(0.5)
        self.play(Transform(square_gp[1], MathTex("100mm^2", color=LIGHT_BLUE_COLOR).shift(1.2 * DOWN)))
        self.wait(1)
        self.play(AnimateToLeft(Group(*self.mobjects)), run_time=0.7)
        self.remove(*self.mobjects)