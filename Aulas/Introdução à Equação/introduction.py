from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = VGroup(
            Tex("Introdução à", color=LIGHT_PURPLE_COLOR),
            Tex("Equação", color=LIGHT_PURPLE_COLOR)
        )
        title.scale(2.5)
        title.arrange(DOWN, buff=0.2)
        strawberry_tracker = ValueTracker(0)
        strawberry = always_redraw(lambda: 
            Strawberry()
                .scale(0.5)
                .next_to(title, UL, 0.8)
                .shift((1 - strawberry_tracker.get_value()) * 8.7 * RIGHT + 2 * RIGHT)
                .rotate(360 * DEGREES * (1 - strawberry_tracker.get_value()))
        )
        apple_tracker = ValueTracker(0)
        apple = always_redraw(lambda: 
            Apple()
                .scale(0.5)
                .next_to(title, DL, 0.8)
                .shift((1 - apple_tracker.get_value()) * 8.7 * RIGHT + 2 * RIGHT)
                .rotate(360 * DEGREES * (1 - apple_tracker.get_value()))
        )
        lemon_tracker = ValueTracker(0)
        lemon = always_redraw(lambda: 
            Lemon()
                .scale(0.5)
                .next_to(title, UR, 0.8)
                .shift((1 - lemon_tracker.get_value()) * 8.5 * RIGHT - 1.8 * RIGHT)
                .rotate(360 * DEGREES * (1 - lemon_tracker.get_value()))
        )
        grapes_tracker = ValueTracker(0)
        grapes = always_redraw(lambda: 
            Grapes()
                .scale(0.5)
                .next_to(title, DR, 0.8)
                .shift((1 - grapes_tracker.get_value()) * 8.5 * RIGHT - 1.8 * RIGHT)
                .rotate(360 * DEGREES * (1 - grapes_tracker.get_value()))
        )

        self.add(strawberry)
        self.play(
            FadeIn(title, run_time=0.7),
            strawberry_tracker.animate(run_time=1.2).set_value(1)
        ) 
        self.add(apple, lemon, grapes)  
        self.play(
            apple_tracker.animate(run_time=1.2).set_value(1),
            lemon_tracker.animate(run_time=1.2).set_value(1),
            grapes_tracker.animate(run_time=1.6).set_value(1)
        )
        self.wait(1)
        self.play(ShrinkToCenter(Group(*self.mobjects)), run_time=0.7)
        self.remove(*self.mobjects)