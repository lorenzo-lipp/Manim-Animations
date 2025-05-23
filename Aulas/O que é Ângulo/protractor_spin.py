from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class ProtractorSpin(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        protractor = Protractor()
        protractor.scale(1.5)

        self.play(SpinInFromNothing(protractor))
        self.wait(2)
        self.play(FadeOut(protractor), run_time=0.5)        
        self.remove(*self.mobjects)