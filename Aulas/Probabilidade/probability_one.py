from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ProbabilityOne(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        roulette = Roulette()
        roulette.scale(2)
        frac_text = MathTex("{3}\over{8}", color=TEXT_COLOR)
        frac_text.scale(3)
        frac_text[0][0].set_color(LIGHT_RED_COLOR)
        Group(roulette, frac_text).arrange(DOWN, buff=0.5)

        self.play(AnimateFromLeft(roulette))
        self.wait(1)
        self.play(*roulette.spin(angle=4.1 * PI, run_time=3, rate_func=rate_functions.ease_out_quad))
        self.wait(0.3)
        self.play(roulette.flash_selected(), run_time=0.7)
        self.play(roulette.flash_selected(), run_time=0.7)
        self.wait(1)

        texts = [Text(str(num), color=WHITE) for num in range(1, 9)]
        texts[0].move_to(roulette.roulette_sectors[1].get_center() + (0.2 * LEFT + 0.05 * DOWN))
        texts[1].move_to(roulette.roulette_sectors[7].get_center() + (0.07 * LEFT + 0.2 * UP))
        texts[2].move_to(roulette.roulette_sectors[5].get_center() + (0.2 * RIGHT + 0.05 * UP))

        self.play(*[Write(text) for text in texts[0:3]])
        self.wait(0.7)
        self.play(FadeOut(*texts[0:3]), Write(frac_text[0][0]))

        texts[0].move_to(roulette.roulette_sectors[7].get_center() + (0.07 * LEFT + 0.2 * UP))
        texts[1].move_to(roulette.roulette_sectors[6].get_center())
        texts[2].move_to(roulette.roulette_sectors[5].get_center() + (0.2 * RIGHT + 0.05 * UP))
        texts[3].move_to(roulette.roulette_sectors[4].get_center())
        texts[4].move_to(roulette.roulette_sectors[3].get_center() + (0.07 * RIGHT + 0.1 * DOWN))
        texts[5].move_to(roulette.roulette_sectors[2].get_center())
        texts[6].move_to(roulette.roulette_sectors[1].get_center() + (0.2 * LEFT + 0.05 * DOWN))
        texts[7].move_to(roulette.roulette_sectors[0].get_center() + (0.03 * UP))

        self.play(*[Write(text) for text in texts])
        self.wait(1.8)
        self.play(FadeOut(*texts), Write(frac_text[0][1:]))
        self.wait(2)
        self.play(*roulette.spin(angle=5.25 * PI, run_time=3, rate_func=rate_functions.ease_out_quad))
        self.play(Transform(frac_text[0][0], MathTex("{1}\over{8}", color=LIGHT_PURPLE_COLOR).scale(3).move_to(frac_text)[0][0]))
        self.wait(0.3)
        self.play(roulette.flash_selected(), run_time=0.7)
        self.play(roulette.flash_selected(), run_time=0.7)
        self.wait(2)
        self.play(AnimateToLeft(*self.mobjects))
        self.remove(*self.mobjects)