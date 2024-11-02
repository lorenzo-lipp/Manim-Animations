from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class FirstPizza(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        pietro = Pietro()
        julia = Julia()
        augusto = Augusto()
        Group(pietro, julia, augusto).arrange(RIGHT, buff=0.3)
        pizza_tracker = ValueTracker(0)
        pizza = always_redraw(lambda:
            Pizza()
                .shift(1.6 * DOWN + 9 * (1 - pizza_tracker.get_value()) * RIGHT)
                .rotate(360 * DEGREES * (1 - pizza_tracker.get_value()))
        )

        self.add(julia, pizza)
        self.play(LaggedStart(
            julia.animate.shift(1.5 * UP),
            pizza_tracker.animate(run_time=1.2).set_value(1),
            lag_ratio=0.3
        ))
        self.wait(1)
        self.remove(pizza)

        ur_slice = VGroupIntersection(
            pizza, 
            SurroundingRectangle(pizza, fill_opacity=1)
                .move_to(pizza.get_center(), aligned_edge=DL)
        )    
        ul_slice = VGroupIntersection(
            pizza, 
            SurroundingRectangle(pizza, fill_opacity=1)
                .move_to(pizza.get_center(), aligned_edge=DR)
        )    
        dr_slice = VGroupIntersection(
            pizza, 
            SurroundingRectangle(pizza, fill_opacity=1)
                .move_to(pizza.get_center(), aligned_edge=UL)
        )    
        dl_slice = VGroupIntersection(
            pizza, 
            SurroundingRectangle(pizza, fill_opacity=1)
                .move_to(pizza.get_center(), aligned_edge=UR)
        )    

        self.add(ur_slice, ul_slice, dr_slice, dl_slice)
        self.play(
            ur_slice.animate.shift(0.05 * UR),
            ul_slice.animate.shift(0.05 * UL),
            dr_slice.animate.shift(0.05 * DR),
            dl_slice.animate.shift(0.05 * DL)
        )
        self.wait(0.5)
        self.play(
            dr_slice.animate.shift(9 * RIGHT),
            dl_slice.animate.shift(9 * RIGHT)
        )

        fraction = MathTex(r"\frac{2}{4}", color=TEXT_COLOR)
        fraction.scale(2)
        fraction.shift(2.4 * DOWN)
        classification = Tex(
            "Fração Própria", 
            color=TEXT_COLOR,
            tex_to_color_map={"Própria": LIGHT_PURPLE_COLOR}
        )
        classification.scale(1.8)
        classification.shift(2.4 * DOWN + 0.8 * RIGHT)

        self.play(
            julia.animate.shift(0.75 * UP),
            ur_slice.animate.shift(0.75 * UP),
            ul_slice.animate.shift(0.75 * UP),
            Write(fraction)
        )
        self.wait(1)
        self.play(Indicate(fraction[0][0], color=LIGHT_ORANGE_COLOR))
        self.wait(0.5)
        self.play(Indicate(fraction[0][2], color=LIGHT_ORANGE_COLOR))
        self.wait(1)
        self.play(
            LaggedStart(
                fraction.animate.shift(2.9 * LEFT),
                Write(classification),
                lag_ratio=0.5
            )
        )
        self.wait(1)
        self.play(Circumscribe(classification[1], color=LIGHT_PURPLE_COLOR))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)