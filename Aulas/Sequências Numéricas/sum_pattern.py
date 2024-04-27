from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class SumPattern(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Group(
            Tex("Observe a sequência", color=LIGHT_RED_COLOR),
            Tex("abaixo:", color=LIGHT_RED_COLOR)
        )
        title.arrange(DOWN)
        title.scale(1.8)
        title.shift(3.5 * UP)
        pattern_text = Tex("1, 2, 3, 4, 5, 6, 7, 8, ...", color=TEXT_COLOR)
        pattern_text.scale(1.5)
        previous_arc = None
        previous_arc_text = None

        self.play(
            FadeIn(title), 
            FadeIn(pattern_text), 
            run_time=0.5
        )
        self.wait(0.3)
        self.play(Circumscribe(pattern_text[0][0], color=LIGHT_RED_COLOR, run_time=2.5))

        for i in range(7):
            start = -2.7 + i * 0.85
            end = start - 0.8

            if i % 2 == 0:
                y = 0.5
                direction = UP
            else:
                y = -0.5
                direction = DOWN

            arc = ArcBetweenPoints([start, y, 0], [end, y, 0], color=LIGHT_RED_COLOR)
            arc.flip(UP)

            if i % 2 == 1: 
                arc.flip(RIGHT)

            arc.add_tip(tip_shape=ArrowTriangleFilledTip)
            arc_text = Tex("+1", color=LIGHT_RED_COLOR)
            arc_text.scale(0.8)
            arc_text.next_to(arc, direction)

            if previous_arc is None:
                self.play(FadeIn(Group(arc_text, arc)), run_time=0.2)
            else:
                self.play(
                    Transform(previous_arc_text.copy().set_opacity(0), arc_text), 
                    Transform(previous_arc.copy().set_opacity(0), arc),
                    rate_func=rate_functions.rush_from,
                    run_time=0.3
                )

            previous_arc_text = arc_text
            previous_arc = arc
            self.wait(0.5)

        self.wait(0.5)
        self.play(FadeOut(Group(*self.mobjects[1:]), run_time=0.5))
        self.remove(*self.mobjects)