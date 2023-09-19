from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class MultiplyPattern(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Group(
            Tex("Observe a sequência", color=LIGHT_RED_COLOR),
            Tex("abaixo:", color=LIGHT_RED_COLOR)
        )
        title.arrange(DOWN)
        title.scale(1.8)
        title.shift(3.5 * UP)
        pattern_text = Tex("1, 3, 9, 27, 81, 243, ...", color=TEXT_COLOR).scale(1.5)
        previous_arc = None
        previous_arc_text = None
        
        self.add(title)
        self.play(FadeIn(pattern_text), run_time=0.8)
        self.wait(1)

        for i in range(5):
            start = -2.6 + i * 0.85
            end = start - 0.8

            if i > 2:
                start += 0.4
                end += 0.3
            
            if i > 3:
                start += 0.6
                end += 0.3

            if i % 2 == 0:
                y = 0.5
                direction = UP
            else:
                y = -0.6
                direction = DOWN

            arc = ArcBetweenPoints([start, y, 0], [end, y, 0], color=LIGHT_BLUE_COLOR)
            arc.flip(UP)
            
            if i % 2 == 1:
                arc.flip(RIGHT)

            arc.add_tip(tip_shape=ArrowTriangleFilledTip)
            arc_text = Tex("x3", color=LIGHT_BLUE_COLOR)
            arc_text.scale(0.8)
            arc_text.next_to(arc, direction)

            if previous_arc is None:
                self.play(FadeIn(Group(arc_text, arc)), run_time=0.25)
            else:
                self.play(
                    Transform(previous_arc_text.copy().set_opacity(0), arc_text), 
                    Transform(previous_arc.copy().set_opacity(0), arc),
                    rate_func=rate_functions.rush_from,
                    run_time=0.4
                )

            previous_arc_text = arc_text
            previous_arc = arc
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects[1:])))
        self.remove(*self.mobjects)