from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class IntroducingUnits(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        DISABLED_COLOR = GRAY
        SQUARE_SIZE = 2
        units = [
            ["km", "Quilômetro", LIGHT_RED_COLOR], 
            ["ham", "Hectômetro", DISABLED_COLOR], 
            ["dam", "Decâmetro", DISABLED_COLOR], 
            ["m", "Metro", LIGHT_BLUE_COLOR], 
            ["dm", "Decímetro", DISABLED_COLOR], 
            ["cm", "Centímetro", LIGHT_PURPLE_COLOR], 
            ["mm", "Milímetro", LIGHT_GREEN_COLOR]
        ]
        table = VGroup(
            *[VGroup(
                VGroup(
                    Rectangle(unit[2], SQUARE_SIZE/3, SQUARE_SIZE, fill_opacity=0.2),
                    MathTex(unit[0], color=unit[2])
                ),
                VGroup(
                    Rectangle(unit[2], SQUARE_SIZE/3, SQUARE_SIZE, fill_opacity=0.2),
                    Tex(unit[1], color=unit[2]).scale(0.7)
                ),
            ).arrange(RIGHT, buff=0) for unit in units]
        ).arrange(DOWN, buff=0)
        table.scale(1.4)
        
        self.play(AnimateFromRight(table))
        self.play(
            LaggedStart(
                *[Indicate(item, scale_factor=1.05, color=LIGHT_ORANGE_COLOR) for item in table],
                lag_ratio=0.8
            )
        )
        self.wait(0.5)
        self.remove(*self.mobjects)