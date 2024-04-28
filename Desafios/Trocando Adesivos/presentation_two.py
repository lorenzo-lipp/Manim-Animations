from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class PresentationTwo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        medium_stickers = Group(
            Group(Sticker(1, "./assets/022.png"), Sticker(1, "./assets/023.png"))
                .arrange(RIGHT, buff=0.3),
            Group(Sticker(1, "./assets/031.png"), Sticker(1, "./assets/032.png"), Sticker(1, "./assets/028.png"))
                .arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, buff=0.2)
        big_stickers = Group(Sticker(1.4, "./assets/025.png"), Sticker(1.4, "./assets/026.png"))
        big_stickers.arrange(RIGHT, buff=0.3)
        Group(medium_stickers, big_stickers).arrange(DOWN, buff=2.5)
        arrow = Arrow(medium_stickers.get_bottom() + 0.1 * DOWN, big_stickers.get_top() + 0.1 * UP, color=LIGHT_RED_COLOR)
        natalia = Group(
            ImageMobject("./assets/001.png"),
            Tex("21 adesivos pequenos", color=TEXT_COLOR),
            Tex("13 adesivos médios", color=TEXT_COLOR),
            Tex("3 adesivos grandes", color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.4)
        arrow_2 = Arrow(start=natalia.get_bottom(), end=natalia.get_bottom() + 1.5 * DOWN, color=LIGHT_RED_COLOR)
        text = Tex("? adesivos grandes", color=TEXT_COLOR)
        text.next_to(arrow_2, DOWN, 0.1)

        self.play(AnimateFromLeft(medium_stickers), run_time=0.7)
        self.wait(1)
        self.play(AnimateFromLeft(big_stickers), run_time=0.7)
        self.wait(1)
        self.play(Write(arrow))
        self.wait(1)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)
        self.play(AnimateFromLeft(natalia))
        self.wait(2)
        self.play(Write(arrow_2), run_time=0.7)
        self.play(Write(text), run_time=0.7)
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)