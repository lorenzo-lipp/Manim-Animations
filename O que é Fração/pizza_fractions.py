from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class PizzaFractions(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        pizzas = VGroup(
            Pizza(),
            VGroup(
                Pizza(),
                AnnularSector(1.4, 0, PI, 1.5 * PI, color=BACKGROUND_COLOR),
                DashedVMobject(Arc(1.3, 1.5 * PI, PI, color=DARK_RED_COLOR)),
                DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR), 10)
            ),
            VGroup(
                Pizza(),
                AnnularSector(1.4, 0, PI / 2, 0, color=BACKGROUND_COLOR),
                DashedVMobject(Arc(1.3, 0, PI / 2, color=DARK_RED_COLOR), 7),
                DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR), 10),
                DashedVMobject(Line(1.3 * RIGHT, 1.3 * LEFT, color=DARK_RED_COLOR), 10)
            ),
            VGroup(
                Pizza(),
                AnnularSector(1.4, 0, PI, 11/6 * PI, color=BACKGROUND_COLOR),
                DashedVMobject(Arc(1.3, 11/6 * PI, PI, color=DARK_RED_COLOR)),
                DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR), 10),
                DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR)
                    .rotate(2 * PI / 6), 10),
                DashedVMobject(Line(1.3 * UP, 1.3 * DOWN, color=DARK_RED_COLOR)
                    .rotate(4 * PI / 6), 10)
            ),
            VGroup(
                Pizza(),
                AnnularSector(1.4, 0, 6 * PI / 7, 17/14 * PI, color=BACKGROUND_COLOR),
                DashedVMobject(Arc(1.3, 17/14 * PI, 6 * PI / 7, color=DARK_RED_COLOR)),
                DashedVMobject(Line(ORIGIN, 1.3 * DOWN, color=DARK_RED_COLOR), 5),
                DashedVMobject(Line(ORIGIN, 1.3 * DOWN, color=DARK_RED_COLOR), 5)
                    .rotate(2 * PI / 7, about_point=ORIGIN),
                DashedVMobject(Line(ORIGIN, 1.3 * DOWN, color=DARK_RED_COLOR), 5)
                    .rotate(4 * PI / 7, about_point=ORIGIN),
                DashedVMobject(Line(ORIGIN, 1.3 * DOWN, color=DARK_RED_COLOR), 5)
                    .rotate(6 * PI / 7, about_point=ORIGIN),
                DashedVMobject(Line(ORIGIN, 1.3 * DOWN, color=DARK_RED_COLOR), 5)
                    .rotate(8 * PI / 7, about_point=ORIGIN),
                DashedVMobject(Line(ORIGIN, 1.3 * DOWN, color=DARK_RED_COLOR), 5)
                    .rotate(10 * PI / 7, about_point=ORIGIN),
                DashedVMobject(Line(ORIGIN, 1.3 * DOWN, color=DARK_RED_COLOR), 5)
                    .rotate(12 * PI / 7, about_point=ORIGIN),
            )
        )
        pizzas.scale(0.9)
        pizzas.arrange(DOWN)

        self.play(
            LaggedStart(
                *[SpinInFromNothing(pizza) for pizza in pizzas], 
                lag_ratio=0.2,
                run_time=1.8
            )
        )
        self.play(pizzas.animate.shift(LEFT), run_time=0.5)

        arrows = []

        for i in range(5):
            arrows.append(Arrow(pizzas[i].get_right(), pizzas[i].get_right() + 1.5 * RIGHT, color=LIGHT_PURPLE_COLOR))

        text1 = MathTex("1", color=BLACK)
        text1.next_to(arrows[0], RIGHT)
        text2 = MathTex(r"\frac{1}{2}", color=BLACK)
        text2.next_to(arrows[1], RIGHT)
        text3 = MathTex(r"\frac{3}{4}", color=BLACK)
        text3.next_to(arrows[2], RIGHT)
        text4 = MathTex(r"\frac{3}{6}", color=BLACK)
        text4.next_to(arrows[3], RIGHT)
        text5 = MathTex(r"\frac{4}{7}", color=BLACK)
        text5.next_to(arrows[4], RIGHT)
        texts = [text1, text2, text3, text4, text5]

        for i in range(5):
            self.play(
                DrawBorderThenFill(arrows[i]), 
                Write(texts[i]), 
                run_time=0.7
            )

        self.wait(1)
        self.play(
            *[pizza.animate.scale(0) for pizza in pizzas if pizza != pizzas[2]],
            *[FadeOut(arrow) for arrow in arrows if arrow != arrows[2]],
            *[FadeOut(text) for text in texts if text != texts[2]],
            run_time=0.8
        )
        self.play(
            Group(pizzas[2], arrows[2]).animate.rotate(-PI / 2).shift(0.2 * RIGHT + UP),
            texts[2].animate.shift(2 * LEFT + 2 * DOWN),
            run_time=0.8
        )

        arrow_num = Arrow(text3[0][0].get_left(), text3[0][0].get_left() + LEFT, color=LIGHT_RED_COLOR)
        arrow_den = Arrow(text3[0][2].get_right(), text3[0][2].get_right() + RIGHT, color=GREEN_COLOR)
        text_num = Tex("Numerador", color=LIGHT_RED_COLOR)
        text_num.next_to(arrow_num, LEFT)
        text_den = Tex("Denominador", color=GREEN_COLOR)
        text_den.next_to(arrow_den, RIGHT)

        self.play(
            DrawBorderThenFill(arrow_num), 
            Write(text_num), 
            text3[0][0].animate.set_color(LIGHT_RED_COLOR)
        )
        self.play(
            DrawBorderThenFill(arrow_den), 
            Write(text_den), 
            text3[0][2].animate.set_color(GREEN_COLOR)
        )
        self.wait(1)
        self.play(Group(*self.mobjects).animate.shift(9 * LEFT), run_time=0.5)
        self.remove(*self.mobjects)