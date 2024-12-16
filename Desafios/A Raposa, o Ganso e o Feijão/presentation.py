from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        background = Background()
        farmer = Farmer()
        farmer.shift(LEFT + 0.5 * DOWN)
        fox = Fox()
        fox.shift(3.8 * LEFT + 0.5 * DOWN)
        goose = Goose()
        goose.shift(2.5 * LEFT + 1.5 * DOWN)
        beans = Beans()
        beans.shift(1 * LEFT + 2.3 * DOWN)

        self.play(FadeIn(Group(background, farmer, fox, goose, beans)))
        self.wait(1)
        self.play(fox.animate.shift(1.8 * RIGHT + 0.5 * UP))
        self.wait(0.5)

        for i in range(15):
            farmer.change_state()
            farmer.shift(0.1 * RIGHT + 0.05 * UP)
            fox.shift(0.1 * RIGHT + 0.05 * UP)
            self.wait(0.15)
    
        self.play(goose.animate.shift(0.5 * RIGHT + 0.2 * DOWN))

        beans.change_state()
        goose.change_state()

        self.wait(1)
        self.play(FadeOut(farmer, fox, goose, beans))

        farmer.shift(1 * LEFT + 0.5 * DOWN)
        fox.shift(3.3 * LEFT + 1.5 * DOWN)
        goose.shift(0.5 * LEFT + 0.2 * UP)
        goose.change_state()
        beans.change_state()

        self.play(FadeIn(farmer, fox, goose, beans))
        self.wait(1)
        self.play(beans.animate.shift(0.6 * LEFT + 2.4 * UP))
        self.wait(0.5)

        for i in range(15):
            farmer.change_state()
            farmer.shift(0.1 * RIGHT + 0.05 * UP)
            beans.shift(0.1 * RIGHT + 0.05 * UP)
            self.wait(0.15)
    
        self.play(fox.animate.shift(0.5 * RIGHT + 0.2 * DOWN))
        self.remove(goose)

        fox.change_state()

        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)