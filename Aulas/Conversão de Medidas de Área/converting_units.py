from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ConvertingUnits(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        WRITE_RUN_TIME = 0.7
        table = UnitsTable()
        arrows_left = UnitsTableLeftArrows(table)
        arrows_right = UnitsTableRightArrows(table)
        
        self.add(table)
        self.play(Write(arrows_left[0]), run_time=WRITE_RUN_TIME)

        for i in range(0, 5):
            self.play(
                Unwrite(arrows_left[i]),
                Write(arrows_left[i + 1]),
                run_time=WRITE_RUN_TIME
            )

        self.play(Unwrite(arrows_left[5]), run_time=WRITE_RUN_TIME)
        self.play(Indicate(table[3], scale_factor=1.05, color=LIGHT_ORANGE_COLOR))
        self.play(Indicate(table[5], scale_factor=1.05, color=LIGHT_ORANGE_COLOR))

        arrows_left = UnitsTableLeftArrows(table)
        arrows_right = UnitsTableRightArrows(table)
        arrow_km_m = UnitsTableLeftArrow(table, 0, 3)
        arrow_km_m[1].rotate(-90 * DEGREES)
        arrow_m_km = UnitsTableRightArrow(table, 3, 0)
        arrow_m_km[1].rotate(-90 * DEGREES)
        arrow_m_cm = UnitsTableLeftArrow(table, 3, 5)
        arrow_m_cm[1].rotate(-90 * DEGREES)
        arrow_m_cm[1].shift(0.1 * UP)
        arrow_cm_m = UnitsTableRightArrow(table, 5, 3)
        arrow_cm_m[1].rotate(-90 * DEGREES)
        arrow_cm_m[1].shift(0.1 * UP)
        arrow_cm_mm = UnitsTableLeftArrow(table, 5, 6)
        arrow_cm_mm[1].rotate(-90 * DEGREES)
        arrow_cm_mm[1].shift(0.1 * DOWN)
        arrow_mm_cm = UnitsTableRightArrow(table, 6, 5)
        arrow_mm_cm[1].rotate(-90 * DEGREES)
        arrow_mm_cm[1].shift(0.1 * DOWN)

        for i in range(3, 5):
            self.play(Write(arrows_left[i]),run_time=WRITE_RUN_TIME)

        self.wait(2)

        text = MathTex("1m^2 = 10.000cm^2", tex_to_color_map={"1m^2":LIGHT_BLUE_COLOR, "10.000cm^2":LIGHT_PURPLE_COLOR}, color=BLACK)
        text.scale(1.8)
        text.shift(4 * DOWN)

        self.play(Write(text))
        self.wait(0.5)
        self.play(
            FadeOut(text), 
            *[FadeOut(arrows_left[i]) for i in range(3, 5)],
        )
        self.wait(1)

        self.play(Write(arrows_right[5]), run_time=WRITE_RUN_TIME)

        for i in range(0, 5):
            self.play(
                Unwrite(arrows_right[5 - i]),
                Write(arrows_right[4 - i]),
                run_time=WRITE_RUN_TIME
            )

        self.play(Unwrite(arrows_right[0]), run_time=WRITE_RUN_TIME)

        arrows_right = UnitsTableRightArrows(table)

        for i in range(0, 2):
            self.play(Write(arrows_right[4 - i]), run_time=WRITE_RUN_TIME)

        self.wait(1)

        text = MathTex("500cm^2 = 0,05m^2", tex_to_color_map={"0,05m^2":LIGHT_BLUE_COLOR, "500cm^2":LIGHT_PURPLE_COLOR}, color=BLACK)
        text.scale(1.8)
        text.shift(4 * DOWN)
        text[2][2:].shift(0.1 * LEFT)

        self.play(Write(text))
        self.wait(2.5)
        self.play(
            FadeOut(text),
            *[FadeOut(arrows_right[4 - i]) for i in range(0, 2)],
        )
        self.wait(1)

        self.play(
            *[Write(arrow) for arrow in [arrow_km_m, arrow_cm_mm, arrow_mm_cm, arrow_m_km, arrow_cm_m, arrow_m_cm]]
        )
        self.wait(5)
        self.play(AnimateToLeft(Group(*self.mobjects)))
        self.remove(*self.mobjects)