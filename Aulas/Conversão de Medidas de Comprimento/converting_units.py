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
        self.play(Write(arrows_right[5]), run_time=WRITE_RUN_TIME)

        for i in range(0, 5):
            self.play(
                Unwrite(arrows_right[5 - i]),
                Write(arrows_right[4 - i]),
                run_time=WRITE_RUN_TIME
            )

        self.play(Unwrite(arrows_right[0]), run_time=WRITE_RUN_TIME)
        self.play(Indicate(table[3], scale_factor=1.05, color=LIGHT_ORANGE_COLOR))
        self.play(Indicate(table[5], scale_factor=1.05, color=LIGHT_ORANGE_COLOR))

        arrows_left = UnitsTableLeftArrows(table)
        arrows_right = UnitsTableRightArrows(table)
        arrow_m_cm = UnitsTableLeftArrow(table, 3, 5)
        arrow_cm_m = UnitsTableRightArrow(table, 5, 3)

        for i in range(3, 5):
            self.play(Write(arrows_left[i]),run_time=WRITE_RUN_TIME)

        self.play(
            *[FadeOut(arrows_left[i]) for i in range(3, 5)],
            FadeIn(arrow_m_cm)
        )
        self.wait(1)

        for i in range(0, 2):
            self.play(Write(arrows_right[5 - i]),run_time=WRITE_RUN_TIME)

        self.play(
            *[FadeOut(arrows_right[5 - i]) for i in range(0, 2)],
            FadeIn(arrow_cm_m)
        )
        self.play(
            FadeOut(arrow_m_cm),
            FadeOut(arrow_cm_m)
        )
        self.remove(*self.mobjects)