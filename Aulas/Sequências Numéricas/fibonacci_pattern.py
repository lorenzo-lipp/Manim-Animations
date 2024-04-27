from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FibonacciPattern(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Group(
            Tex("Observe a sequência", color=LIGHT_RED_COLOR),
            Tex("abaixo:", color=LIGHT_RED_COLOR)
        )
        title.arrange(DOWN)
        title.scale(1.8)
        title.shift(3.5 * UP)
        colors = [
            LIGHT_BLUE_COLOR, 
            LIGHT_RED_COLOR, 
            LIGHT_ORANGE_COLOR, 
            AQUA_GREEN_COLOR, 
            LIGHT_PURPLE_COLOR, 
            LIGHT_BLUE_COLOR
        ]
        sequence = [0, 1, 1, 2, 3, 5, 8]
        pattern_text = Tex("0, 1, 1, 2, 3, 5, 8, 13, ...", color=TEXT_COLOR).scale(1.5)
        previous_arc = None
        previous_arc_text = None
        previous_arc_box = None

        self.add(title)
        self.play(FadeIn(Group(pattern_text)), run_time=0.8)
        self.wait(1)

        for i in range(6):
            start = -2.1 + i * 0.85
            end = -3.25 + i * 0.85

            arc_text = Tex(f"{sequence[i]}+{sequence[i+1]}", color=colors[i])
            arc_text.scale(0.8)

            if i % 2 == 0:
                y1 = 0.5
                y2 = 0.5
                direction = UP
            else:
                y1 = -0.6
                y2 = -0.39
                direction = DOWN

            arc = ArcBetweenPoints([start, y1, 0], [end, y1, 0], color=colors[i])
            arc.flip(UP)

            if i % 2 == 1:
                arc.flip(RIGHT)

            arc.add_tip(tip_shape=ArrowTriangleFilledTip)
            arc_text.next_to(arc, direction)
            arc_box = Line(np.array([end - 0.455, y2, 0]), np.array([start - 0.555, y2, 0]), color=colors[i])

            if previous_arc is None:
                self.play(FadeIn(Group(arc_text, arc, arc_box)), run_time=0.25)
            else:
                self.play(
                    Transform(previous_arc_text.copy().set_opacity(0), arc_text), 
                    Transform(previous_arc.copy().set_opacity(0), arc),
                    Transform(previous_arc_box.copy().set_opacity(0), arc_box),
                    rate_func=rate_functions.rush_from,
                    run_time=0.4
                )

            previous_arc_text = arc_text
            previous_arc = arc
            previous_arc_box = arc_box
            self.wait(0.7)
        
        text = Tex("Fibonacci", color=TEXT_COLOR)
        text.shift(DOWN * 3.5)
        text.scale(2)

        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))