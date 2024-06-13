from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        pieces = VGroup(
            TopPieces(),
            Board(),
            BottomPieces()
        ).arrange(DOWN, 0.8)

        self.play(FadeIn(pieces))
        self.play(pieces[2][0].animate.move_to(pieces[1][1][0]))
        self.wait(1)
        self.remove(*self.mobjects)