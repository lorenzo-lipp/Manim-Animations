from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class TenPrimes(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        text = Tex("Dez primeiros primos", color=LIGHT_RED_COLOR)
        text.scale(1.5)
        primes = VGroup(*[Tex(str(prime), color=LIGHT_BLUE_COLOR) for prime in range(2, 30) if is_prime(prime)])
        primes.scale(1.5)
        first_five = VGroup(*primes[0:5])
        first_five.arrange(RIGHT, buff=0.8)
        next_five = VGroup(*primes[5:])
        next_five.arrange(RIGHT, buff=0.5)
        Group(
            text,
            first_five, 
            next_five
        ).arrange(DOWN, buff=0.8)

        self.play(Write(text), run_time=0.7)

        for prime in primes:
            self.play(DrawBorderThenFill(prime), run_time=0.3, rate_func=linear)

        self.wait(2)
        self.play(Group(*self.mobjects).animate.scale(0), run_time=0.7)