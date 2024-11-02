from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ThirdPizza(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        pietro = Pietro()
        pietro.shift(1.5 * UP)
        pizza = Pizza()
        pizza_2 = Pizza()
        Group(pizza, pizza_2).arrange(RIGHT, buff=0.5)
        pizza.shift(1.6 * DOWN)
        pizza_2.shift(1.6 * DOWN)
        ur_slice_2 = VGroupIntersection(
            pizza_2, 
            SurroundingRectangle(pizza_2, fill_opacity=1)
                .move_to(pizza_2.get_center(), aligned_edge=DL)
        )    
        ul_slice_2 = VGroupIntersection(
            pizza_2, 
            SurroundingRectangle(pizza_2, fill_opacity=1)
                .move_to(pizza_2.get_center(), aligned_edge=DR)
        )
        pizza_group = Group(ur_slice_2, ul_slice_2)


        self.play(LaggedStart(
            GrowFromCenter(pietro),
            GrowFromCenter(pizza),
            GrowFromCenter(pizza_group),
            lag_ratio=0.2
        ))
        self.wait(0.1)
        self.remove(pizza, pizza_group)

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
        ur_slice_2 = VGroupIntersection(
            pizza_2, 
            SurroundingRectangle(pizza_2, fill_opacity=1)
                .move_to(pizza_2.get_center(), aligned_edge=DL)
        )    
        ul_slice_2 = VGroupIntersection(
            pizza_2, 
            SurroundingRectangle(pizza_2, fill_opacity=1)
                .move_to(pizza_2.get_center(), aligned_edge=DR)
        )  

        self.play(
            ur_slice.animate.shift(0.05 * UR),
            ul_slice.animate.shift(0.05 * UL),
            dr_slice.animate.shift(0.05 * DR),
            dl_slice.animate.shift(0.05 * DL),
            ur_slice_2.animate.shift(0.05 * UR),
            ul_slice_2.animate.shift(0.05 * UL),
        )
        self.wait(1)

        fraction = MathTex(r"\frac{6}{4}", color=TEXT_COLOR)
        fraction.scale(2)
        fraction.shift(2.8 * DOWN)
        classification = Tex(
            "Fração Imprópria", 
            color=TEXT_COLOR,
            tex_to_color_map={"Imprópria": LIGHT_PURPLE_COLOR}
        )
        classification.scale(1.8)
        classification.shift(2.8 * DOWN + 0.8 * RIGHT)

        self.play(
            pietro.animate.shift(1.5 * UP),
            ur_slice.animate.shift(1.5 * UP),
            ul_slice.animate.shift(1.5 * UP),
            dr_slice.animate.shift(1.5 * UP),
            dl_slice.animate.shift(1.5 * UP),
            ur_slice_2.animate.shift(1.5 * UP),
            ul_slice_2.animate.shift(1.5 * UP),
            Write(fraction)
        )
        self.wait(1)
        self.play(Indicate(fraction[0][0], color=LIGHT_ORANGE_COLOR))
        self.wait(0.5)
        self.play(Indicate(fraction[0][2], color=LIGHT_ORANGE_COLOR))
        self.wait(1)
        self.play(
            LaggedStart(
                fraction.animate.shift(3.5 * LEFT),
                Write(classification),
                lag_ratio=0.5
            )
        )
        self.wait(1)
        self.play(Circumscribe(classification[1], color=LIGHT_PURPLE_COLOR))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)