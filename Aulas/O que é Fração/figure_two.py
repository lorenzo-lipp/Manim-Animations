from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FigureTwo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        fig = VGroup(
            VGroup(
                Rectangle(height=2, width=1, stroke_color=BLACK),
                VGroup(
                    Rectangle(height=1, width=2, stroke_color=BLACK),
                    Rectangle(height=1, width=2, stroke_color=BLACK, color=LIGHT_RED_COLOR, fill_opacity=1),
                ).arrange(DOWN, buff=0),
                Rectangle(height=2, width=1, stroke_color=BLACK, color=LIGHT_RED_COLOR, fill_opacity=1),
            ).arrange(RIGHT, buff=0),
            VGroup(
                Rectangle(height=1, width=2, stroke_color=BLACK, color=LIGHT_RED_COLOR, fill_opacity=1),
                Rectangle(height=1, width=2, stroke_color=BLACK, color=LIGHT_RED_COLOR, fill_opacity=1),
            ).arrange(RIGHT, buff=0),
            VGroup(
                Rectangle(height=2, width=1, stroke_color=BLACK, color=LIGHT_RED_COLOR, fill_opacity=1),
                Rectangle(height=2, width=1, stroke_color=BLACK),
                VGroup(
                    Rectangle(height=1, width=2, stroke_color=BLACK),
                    Rectangle(height=1, width=2, stroke_color=BLACK, color=LIGHT_RED_COLOR, fill_opacity=1),
                ).arrange(DOWN, buff=0)
            ).arrange(RIGHT, buff=0)
        ).arrange(DOWN, buff=0)
        text = Text("123456", font_size=36)
        text.set_color(BLACK)
        frac = MathTex(r"\frac{6}{10}", color=BLACK)
        frac.next_to(fig, RIGHT, buff=0)
        frac.scale(1.4)
        text[0].next_to(fig[0][1][1], ORIGIN, buff=0)
        text[1].next_to(fig[0][2], ORIGIN, buff=0)
        text[2].next_to(fig[1][0], ORIGIN, buff=0)
        text[3].next_to(fig[1][1], ORIGIN, buff=0)
        text[4].next_to(fig[2][0], ORIGIN, buff=0)
        text[5].next_to(fig[2][2][1], ORIGIN, buff=0)
        frac[0][0].set_color(LIGHT_RED_COLOR)
        frac[0][0].shift(0.1 * DOWN)
        frac[0][1].scale(1.5)
        fig.shift(9 * RIGHT)

        self.play(fig.animate.shift(9 * LEFT), run_time=0.5)
        self.wait(0.8)
        self.play(Write(text), run_time=0.7)
        self.play(
            fig.animate.shift(LEFT), 
            text.animate.shift(LEFT), 
            run_time=0.6
        )
        self.play(Write(frac[0][:2]), run_time=0.5)
        self.play(FadeOut(text), run_time=0.7)

        text = Text("12345678910", font_size=36)
        text.set_color(BLACK)
        text[0].next_to(fig[0][0], ORIGIN, buff=0)
        text[1].next_to(fig[0][1][0], ORIGIN, buff=0)
        text[2].next_to(fig[0][1][1], ORIGIN, buff=0)
        text[3].next_to(fig[0][2], ORIGIN, buff=0)
        text[4].next_to(fig[1][0], ORIGIN, buff=0)
        text[5].next_to(fig[1][1], ORIGIN, buff=0)
        text[6].next_to(fig[2][0], ORIGIN, buff=0)
        text[7].next_to(fig[2][1], ORIGIN, buff=0)
        text[8].next_to(fig[2][2][0], ORIGIN, buff=0)
        text[9:].next_to(fig[2][2][1], ORIGIN, buff=0)

        self.play(Write(text))
        self.play(Write(frac[0][2:]), run_time=0.5)
        self.play(FadeOut(text), run_time=0.7)
        self.wait(0.3)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)