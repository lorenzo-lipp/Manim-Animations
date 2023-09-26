from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FigureOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        fig = VGroup(
            Triangle(stroke_color=BLACK, color=LIGHT_ORANGE_COLOR, fill_opacity=1),
            Triangle(stroke_color=BLACK, color=LIGHT_ORANGE_COLOR, fill_opacity=1)
                .rotate(PI),
            Triangle(stroke_color=BLACK, color=LIGHT_ORANGE_COLOR, fill_opacity=1),
            Triangle(stroke_color=BLACK)
                .rotate(PI),
            Triangle(stroke_color=BLACK)
        )
        fig.arrange(RIGHT, buff=0, aligned_edge=LEFT)
        frac = MathTex(r"\frac{3}{5}", color=BLACK)
        frac.next_to(fig, DOWN, buff=0)
        frac.scale(1.4)
        text = Text("12345", font_size=36)
        text.set_color(BLACK)
        text[0].next_to(fig[0], ORIGIN, buff=0)
        text[0].shift(0.2 * DOWN)
        text[1].next_to(fig[1], ORIGIN, buff=0)
        text[1].shift(0.2 * UP)
        text[2].next_to(fig[2], ORIGIN, buff=0)
        text[2].shift(0.2 * DOWN)
        text[3].next_to(fig[3], ORIGIN, buff=0)
        text[3].shift(0.2 * UP)
        text[4].next_to(fig[4], ORIGIN, buff=0)
        text[4].shift(0.2 * DOWN)
        fig.shift(9 * RIGHT)
        frac[0][0].set_color(LIGHT_ORANGE_COLOR)
        frac[0][0].shift(0.1 * DOWN)
        frac[0][1].scale(2)
        text[3:].shift(0.5 * UP)

        self.play(fig.animate.shift(9 * LEFT), run_time=0.5)
        self.wait(0.5)
        self.play(Write(text[0:3]), run_time=0.7)
        self.play(
            fig.animate.shift(0.5 * UP), 
            text[0:3].animate.shift(0.5 * UP), 
            run_time=0.6
        )
        self.play(Write(frac[0][:2]), run_time=0.7)
        self.play(FadeOut(text[0:3]))
        self.play(Write(text))
        self.play(Write(frac[0][2:]), run_time=0.7)
        self.play(FadeOut(text))
        self.wait(0.3)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)