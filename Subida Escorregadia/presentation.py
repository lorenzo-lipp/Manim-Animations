from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        hedgehog = Hedgehog()
        hedgehog2 = ReflectedHedgehog()
        hedgehog2.scale(0.5)
        hedgehog2.rotate(-19*DEGREES)
        background = Background().shift(14 * RIGHT)
        points = Group(
            Point((-3.5, 3.7, 0.0)),
            Point((-2.5, 3.7, 0.0)),
            Point((-2.1, 4.3, 0.0)),
            Point((-1.7, 5, 0.0)),
            Point((-1.3, 5.4, 0.0)),
            Point((-0.9, 5.7, 0.0)),
            Point((-0.7, 5.4, 0.0)),
            Point((-0.4, 4.9, 0.0)),
            Point((-0.25, 4.2, 0.0)),
            Point((-0.1, 3.5, 0.0)),
            Point((0.2, 0.7, 0.0)),
            Point((2.6, -3, 0.0)),
            Point((1.7, -1.61, 0.0)),
            Point((2, -2.08, 0.0)),
            Point((1.1, -0.68, 0.0)),
            Point((1.43, -1.19, 0.0)),
        )
        ant1 = Ant().move_to((3.5, -3.6, 0.0))
        ant2 = Ant().move_to((3.8, -3.3, 0.0))
        arrow = Line((2.6-1.5, -3, 0.0), (-0.74-1.5, 2.14, 0.0), color=LIGHT_ORANGE_COLOR)
        arrow.add_tip(tip_shape=ArrowTriangleFilledTip)
        arrow.add_tip(tip_shape=ArrowTriangleFilledTip, at_start=True)
        size = Tex("95cm", color=LIGHT_ORANGE_COLOR)
        size.scale(2)
        size.next_to(arrow, LEFT, buff=-1.3)
        question = VGroup(
            Tex("Quantas vezes ele", color=LIGHT_PURPLE_COLOR),
            Tex("escorregou até", color=LIGHT_PURPLE_COLOR),
            Tex("sair do buraco?", color=LIGHT_PURPLE_COLOR),
        )
        question.scale(2)
        question.arrange(DOWN)

        self.add(background, hedgehog)
        self.play(hedgehog.animate.scale(0.5).move_to(points[0]))
        self.wait(0.5)
        self.play(background.animate.shift(13 * LEFT), run_time=1.4)
        self.wait(0.5)
        self.play(
            FadeIn(arrow),
            FadeIn(size), 
            run_time=1
        )
        self.wait(0.5)
        self.add(ant1)
        self.play(Flash(ant1, color=LIGHT_ORANGE_COLOR), run_time=0.5)
        self.wait(0.2)
        self.add(ant2)
        self.play(Flash(ant2, color=LIGHT_ORANGE_COLOR), run_time=0.5)
        self.wait(0.5)
        self.play(hedgehog.animate.move_to(points[1]), run_time=0.2, rate_func=linear)
        self.wait(0.15)
        self.play(hedgehog.animate.move_to(points[2]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[3]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[4]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[5]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[6]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[7]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[8]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[9]), run_time=0.1, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[10]), run_time=0.25, rate_func=linear)
        self.play(hedgehog.animate.move_to(points[11]), run_time=0.6, rate_func=linear)
        self.wait(1)
        self.remove(ant2)
        self.play(Flash(ant2, color=LIGHT_ORANGE_COLOR), run_time=0.5)
        self.remove(ant1)
        self.play(Flash(ant1, color=LIGHT_ORANGE_COLOR), run_time=0.5)
        self.wait(0.2)
        self.remove(hedgehog)
        self.add(hedgehog2.move_to(hedgehog))
        self.wait(1.5)
        self.play(hedgehog2.animate.move_to(points[12]), run_time=0.6, rate_func=linear)
        self.wait(1)
        self.play(hedgehog2.animate.move_to(points[13]), run_time=0.3, rate_func=linear)
        self.wait(0.8)
        self.play(hedgehog2.animate.move_to(points[14]), run_time=0.6, rate_func=linear)
        self.wait(1)
        self.play(hedgehog2.animate.move_to(points[15]), run_time=0.3, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(Group(*self.mobjects), run_time=0.7))
        self.play(Write(question), run_time=0.7)
        self.wait(1)
        self.play(FadeOut(question))
        self.remove(*self.mobjects)