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

        bring_to_forward(self, pieces[0][0])

        self.play(pieces[0][0].animate.move_to(pieces[1][2][0]))
        self.play(pieces[0][0].animate.rotate(90 * DEGREES), run_time=0.7)
        self.wait(1)

        ellipse = Ellipse(width=1.65, height=3.4, color=LIGHT_RED_COLOR, fill_opacity=0.2)
        ellipse.shift(2.375 * LEFT + 1.65 * DOWN)

        self.play(DrawBorderThenFill(ellipse), run_time=0.7)
        self.wait(1)
        self.play(FadeOut(ellipse), run_time=0.7)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)