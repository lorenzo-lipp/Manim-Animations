from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class PresentationOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        small_stickers = Group(
            Group(Sticker(0.8, "./assets/010.png"), Sticker(0.8, "./assets/011.png"))
                .arrange(RIGHT, buff=0.3),
            Group(Sticker(0.8, "./assets/012.png"), Sticker(0.8, "./assets/013.png"), Sticker(0.8, "./assets/014.png"))
                .arrange(RIGHT, buff=0.3),
            Group(Sticker(0.8, "./assets/019.png"), Sticker(0.8, "./assets/021.png"))
                .arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, buff=0.2)
        medium_stickers = Group(
            Group(Sticker(1, "./assets/022.png"), Sticker(1, "./assets/023.png"))
                .arrange(RIGHT, buff=0.3),
            Group(Sticker(1, "./assets/031.png"), Sticker(1, "./assets/032.png"))
                .arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, buff=0.2)
        Group(small_stickers, medium_stickers).arrange(DOWN, buff=2.5)
        arrow = Arrow(small_stickers.get_bottom() + 0.1 * DOWN, medium_stickers.get_top() + 0.1 * UP, color=LIGHT_RED_COLOR)

        self.play(AnimateFromLeft(small_stickers))
        self.wait(1)
        self.play(AnimateFromLeft(medium_stickers))
        self.wait(1)
        self.play(Write(arrow))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)