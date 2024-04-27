from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class EquivalentCrackers(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        big_gray_cracker = GrayCracker().scale(1.5)
        big_cracker = BigCracker([0, 1, 1]).scale(1.5)
        gray_cracker = GrayCracker().scale(1.5)
        cracker = SmallCracker([0, 1, 1, 1, 0, 1]).scale(1.5)
        Group(
            Group(big_gray_cracker, big_cracker),
            Group(gray_cracker, cracker)
        ).arrange(DOWN, buff=2).shift(0.5 * UP)
        big_cracker_fraction = MathTex(r"\frac{2}{3}", color=TEXT_COLOR)
        big_cracker_fraction.next_to(big_cracker, DOWN)
        cracker_fraction = MathTex(r"\frac{4}{6}", color=TEXT_COLOR)
        cracker_fraction.next_to(cracker, DOWN)
        
        self.play(
            AnimateFromLeft(big_gray_cracker),
            AnimateFromLeft(big_cracker),
            AnimateFromLeft(gray_cracker),
            AnimateFromLeft(cracker),
            run_time=0.7
        )
        self.wait(0.5)
        self.play(
            Write(big_cracker_fraction),
            Write(cracker_fraction),
            run_time=0.7
        )
        self.wait(1.2)
        self.play(
            Transform(
                cracker[1][0],
                cracker[1][1].copy().set_opacity(1)
            ))
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)