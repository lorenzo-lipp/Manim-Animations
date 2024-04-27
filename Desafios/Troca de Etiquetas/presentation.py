from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        box1 = ImageMobject("./assets/box1.png")
        lid1 = ImageMobject("./assets/lid1.png").shift(0.05 * UP)
        lid2 = ImageMobject("./assets/lid2.png")
        box2 = ImageMobject("./assets/box2.png")
        box3 = ImageMobject("./assets/box3.png")
        Group(
            Group(box1, lid1, lid2),
            box2,
            box3
        ).arrange(DOWN)
        
        self.play(AnimateFromLeft(box1, lid1))
        self.play(AnimateFromLeft(box2))
        self.play(AnimateFromLeft(box3))
        self.wait(4)
        self.play(lid1.animate.shift(0.7 * UP), run_time=0.4, rate_func=linear)
        self.remove(lid1)
        self.add(lid2)
        self.play(lid2.animate.shift(0.3 * UP), run_time=0.3, rate_func=linear)
        self.wait(5)
        self.play(AnimateToLeft(box1, box2, box3, lid2))
        self.remove(*self.mobjects)