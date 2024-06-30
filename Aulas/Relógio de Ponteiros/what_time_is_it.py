from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class WhatTimeIsIt(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        clock = Clock()
        clock.scale(2.5)
        clock.shift(14 * UP)
        time = always_redraw(lambda: 
            VGroup(
                Tex(str(clock.hours).replace("0", "12"), color=LIGHT_RED_COLOR),
                Tex("h ", color=LIGHT_RED_COLOR),
                Tex(str(clock.minutes), color=LIGHT_RED_COLOR),
                Tex("min", color=LIGHT_RED_COLOR)
            ).scale(2)
            .arrange(RIGHT, buff=0.1)
            .next_to(clock, DOWN, buff=1)
        )

        self.add(clock, time)
        self.play(*clock.set_time(1, 0), run_time=0.001)
        self.play(clock.animate.shift(13 * DOWN))
        self.wait(1)
        self.play(Indicate(clock.hours_pointer, color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(2)
        self.play(Indicate(clock.minutes_pointer, color=LIGHT_RED_COLOR, run_time=1.5))
        self.wait(2)

        for i in range(1, 6):
            self.play(*clock.set_time(1, i), run_time=0.5)
            self.wait(0.1)

        self.play(
            *[Indicate(tick, color=LIGHT_RED_COLOR, run_time=1.5) for tick in clock.big_ticks],
            *[Indicate(text, color=LIGHT_RED_COLOR, run_time=1.5) for text in clock.number_texts]
        )
        self.wait(3)
        self.play(*clock.set_time(1, 59), run_time=3)
        self.wait(1)
        self.play(*clock.set_time(2, 0), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(time), run_time=0.7)
        self.play(*clock.set_time(6, 0))

        time_2 = VGroup(
                Tex("6", color=LIGHT_RED_COLOR),
                Tex("h ", color=LIGHT_RED_COLOR),
                Tex("0", color=LIGHT_RED_COLOR),
                Tex("min", color=LIGHT_RED_COLOR)
        ).scale(2)
        time_2.arrange(RIGHT, buff=0.1)
        time_2.next_to(clock, DOWN, buff=1)
        time_3 = VGroup(
                Tex("12", color=LIGHT_RED_COLOR),
                Tex("h ", color=LIGHT_RED_COLOR),
                Tex("55", color=LIGHT_RED_COLOR),
                Tex("min", color=LIGHT_RED_COLOR)
        ).scale(2)
        time_3.arrange(RIGHT, buff=0.1)
        time_3.next_to(clock, DOWN, buff=1)

        self.wait(7)
        self.play(FadeIn(time_2), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(time_2), run_time=0.5)
        self.play(*clock.set_time(0, 55))
        self.wait(4)
        self.play(FadeIn(time_3), run_time=0.7)

        dotted = DashedLine(clock.get_center(), clock.get_top(), color=LIGHT_RED_COLOR)
        dotted.rotate(angle=-27.5 * DEGREES, about_point=clock.get_center())

        self.play(Create(dotted))
        self.wait(2)
        self.play(FadeOut(dotted))
        self.remove(time_3)
        self.add(time)
        self.play(*clock.set_time(1, 55))

        dotted.rotate(angle=-30 * DEGREES, about_point=clock.get_center())

        self.play(Create(dotted))
        self.play(FadeOut(dotted))
        self.play(FadeOut(*self.mobjects), run_time=0.7)
        self.remove(*self.mobjects)