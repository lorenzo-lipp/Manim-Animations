from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ConvertingUnits(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        DISABLED_COLOR = GRAY
        SQUARE_SIZE = 2
        units = [
            ["km", "Quilômetro", LIGHT_RED_COLOR], 
            ["ham", "Hectômetro", DISABLED_COLOR], 
            ["dam", "Decâmetro", DISABLED_COLOR], 
            ["m", "Metro", LIGHT_BLUE_COLOR], 
            ["dm", "Decímetro", DISABLED_COLOR], 
            ["cm", "Centímetro", LIGHT_PURPLE_COLOR], 
            ["mm", "Milímetro", LIGHT_GREEN_COLOR]
        ]
        table = VGroup(
            *[VGroup(
                VGroup(
                    Rectangle(unit[2], SQUARE_SIZE/3, SQUARE_SIZE, fill_opacity=0.2),
                    MathTex("0", color=BLACK)
                ),
                VGroup(
                    Rectangle(unit[2], SQUARE_SIZE/3, SQUARE_SIZE, fill_opacity=0.2),
                    MathTex(unit[0], color=unit[2])
                ),
                VGroup(
                    Rectangle(unit[2], SQUARE_SIZE/3, SQUARE_SIZE, fill_opacity=0.2),
                    Tex(unit[1], color=unit[2]).scale(0.7)
                ),
            ).arrange(RIGHT, buff=0) for unit in units]
        ).arrange(DOWN, buff=0)
        table.scale(1.4)

        self.play(AnimateFromRight(table))
        self.wait(1)
        self.play(
            LaggedStart(
                Indicate(table[1], scale_factor=1.05, color=LIGHT_ORANGE_COLOR),
                Indicate(table[2], scale_factor=1.05, color=LIGHT_ORANGE_COLOR),
                Indicate(table[4], scale_factor=1.05, color=LIGHT_ORANGE_COLOR),
                lag_ratio=0.8
            )
        )
        self.wait(0.5)
        self.play(Transform(table[0][0][1], MathTex("1", color=BLACK).scale(1.4).move_to(table[0][0][1])))
        self.play(Indicate(table[0], scale_factor=1.05, color=LIGHT_RED_COLOR))
        self.wait(0.8)
        self.play(
            Circumscribe(Group(table[3][0][1], table[0][0][1]), time_width=1, color=LIGHT_BLUE_COLOR, run_time=4),
            *[
                Indicate(table[i][0][1], scale_factor=1, color=LIGHT_BLUE_COLOR, run_time=4)
                for i in range(4)
            ],
            *[
                FadeOutAndBack(table[i], run_time=4)
                for i in range(4, 7)
            ],
        )

        convertion_text = MathTex(
            "1 km = 1000 m", 
            tex_to_color_map={"1 km": LIGHT_RED_COLOR, "1000 m": LIGHT_BLUE_COLOR}, 
            color=BLACK
        ).scale(1.5).move_to(table, DOWN).shift(DOWN)

        self.play(Write(convertion_text))
        self.wait(1)
        self.play(FadeOut(convertion_text))
        self.play(
            Transform(table[0][0][1], MathTex("0", color=BLACK).scale(1.4).move_to(table[0][0][1])),
            Transform(table[3][0][1], MathTex("1", color=BLACK).scale(1.4).move_to(table[3][0][1]))
        )
        self.play(Indicate(table[3], scale_factor=1.05, color=LIGHT_BLUE_COLOR))
        self.wait(0.5)
        self.play(
            Circumscribe(Group(table[5][0][1], table[3][0][1]), time_width=1, color=LIGHT_PURPLE_COLOR, run_time=4),
            *[
                Indicate(table[i][0][1], scale_factor=1, color=LIGHT_PURPLE_COLOR, run_time=4)
                for i in range(3, 6)
            ],
            *[
                FadeOutAndBack(table[i], run_time=4)
                for i in range(0, 3)
            ],
            FadeOutAndBack(table[6], run_time=4)
        )

        convertion_text = MathTex(
            "1 m = 100 cm", 
            tex_to_color_map={"1 m": LIGHT_BLUE_COLOR, "100 cm": LIGHT_PURPLE_COLOR}, 
            color=BLACK
        ).scale(1.5).move_to(table, DOWN).shift(DOWN)

        self.play(Write(convertion_text))
        self.wait(1)
        self.play(FadeOut(convertion_text))
        self.play(
            Transform(table[3][0][1], MathTex("0", color=BLACK).scale(1.4).move_to(table[3][0][1])),
            Transform(table[5][0][1], MathTex("1", color=BLACK).scale(1.4).move_to(table[5][0][1]))
        )
        self.play(Indicate(table[5], scale_factor=1.05, color=LIGHT_PURPLE_COLOR))
        self.play(
            Circumscribe(Group(table[6][0][1], table[5][0][1]), time_width=1, color=LIGHT_GREEN_COLOR, run_time=4),
            *[
                Indicate(table[i][0][1], scale_factor=1, color=LIGHT_GREEN_COLOR, run_time=4)
                for i in range(5, 7)
            ],
            *[
                FadeOutAndBack(table[i], run_time=4)
                for i in range(0, 5)
            ],
        )
        
        convertion_text = MathTex(
            "1 cm = 10 mm", 
            tex_to_color_map={"1 cm": LIGHT_PURPLE_COLOR, "10 mm": LIGHT_GREEN_COLOR}, 
            color=BLACK
        ).scale(1.5).move_to(table, DOWN).shift(DOWN)

        self.play(Write(convertion_text))
        self.wait(1)
        self.play(FadeOut(convertion_text))
        self.play(
            Transform(table[5][0][1], MathTex("0", color=BLACK).scale(1.4).move_to(table[5][0][1])),
            Transform(table[6][0][1], MathTex("1", color=BLACK).scale(1.4).move_to(table[6][0][1]))
        )
        self.play(
            Indicate(table[6], scale_factor=1.05, color=LIGHT_GREEN_COLOR),
            Transform(table[5][0][1], MathTex("0,", color=BLACK).scale(1.4).move_to(table[5][0][1]))
        )
        self.play(
            Circumscribe(Group(table[6][0][1], table[5][0][1]), time_width=1, color=LIGHT_PURPLE_COLOR, run_time=4),
            *[
                Indicate(table[i][0][1], scale_factor=1, color=LIGHT_PURPLE_COLOR, run_time=4)
                for i in range(5, 7)
            ],
            *[
                FadeOutAndBack(table[i], run_time=4)
                for i in range(0, 5)
            ],
        )
        
        convertion_text = MathTex(
            "1 mm = 0.1 cm", 
            tex_to_color_map={"1 mm": LIGHT_GREEN_COLOR, "0.1 cm": LIGHT_GREEN_COLOR}, 
            color=BLACK
        ).scale(1.5).move_to(table, DOWN).shift(DOWN)

        self.play(Write(convertion_text))
        self.wait(1)
        self.play(FadeOut(convertion_text))
        self.play(AnimateToLeft(Group(*self.mobjects)))
        self.remove(*self.mobjects)