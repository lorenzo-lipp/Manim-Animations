from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Tex("Quadriláteros", color=LIGHT_BLUE_COLOR)
        title.scale(2.2)
        square_colors = [LIGHT_BLUE_COLOR, LIGHT_GREEN_COLOR, LIGHT_ORANGE_COLOR, LIGHT_PURPLE_COLOR]
        squares = VGroup(
            *[
                VGroup(*[
                    Square(1, color=square_colors[(j + i) % 4], stroke_width=0, fill_opacity=1) 
                    for i in range(int(config.frame_width))
                ]).arrange(RIGHT, buff=0)
                for j in range(int(config.frame_height))
            ]  
        ).arrange(DOWN, buff=0)
        
        for i in range(7):
            for j in range(2):
                squares[7 + j][i + 1].set(color=BACKGROUND_COLOR)

        self.play(AnimateFromLeft(squares), rate_func=rate_functions.ease_out_bounce, run_time=1.2)
        self.play(GrowFromCenter(title), run_time=0.7)
        self.wait(1.5)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)