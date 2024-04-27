from manim import *
from utils import *

config.frame_size = 1080, 1920 
config.frame_width = 9
config.frame_height = 16

class Presentation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        background = Square(6, color="#C0C0C0", fill_opacity=1, stroke_width=0)
        grid = VGroup(
            VGroup(
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE)
            ).arrange(RIGHT, buff=0.25),
            VGroup(
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE)
            ).arrange(RIGHT, buff=0.25),
            VGroup(
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE)
            ).arrange(RIGHT, buff=0.25),
            VGroup(
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE),
                Piece(color="#A0A0A0", fill_color=WHITE)
            ).arrange(RIGHT, buff=0.25)            
        ).arrange(DOWN, buff=0.25)
        purple_fixed = FixedPiece(color="#9966FF")
        green_fixed = FixedPiece(color="#5FE672")
        blue_fixed = FixedPiece(color="#6699FF")
        red_fixed = FixedPiece(color="#FF3366")
        bottom_pieces = VGroup(
            VGroup(Piece(color="#5FE672"), Piece(color="#5FE672"), Piece(color="#FF3366"), Piece(color="#FF3366"))
                .arrange(RIGHT, buff=0.3),
            VGroup(Piece(color="#FF3366"), Piece(color="#6699FF"), Piece(color="#6699FF"), Piece(color="#6699FF"))
                .arrange(RIGHT, buff=0.3),
            VGroup(Piece(color="#9966FF"), Piece(color="#9966FF"), Piece(color="#9966FF"), Piece(color="#9966FF"))
                .arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.3)
        Group(Group(background, grid), bottom_pieces).arrange(DOWN, buff=0.8)
        purple_fixed.move_to(grid[0][3])
        green_fixed.move_to(grid[0][1])
        blue_fixed.move_to(grid[3][0])
        red_fixed.move_to(grid[2][2])

        self.add(background, grid, red_fixed, purple_fixed, green_fixed, blue_fixed, bottom_pieces)
        self.wait(1)
        self.play(
            grid[0][0].animate.set(fill_color="#AEF2B8"),
            grid[0][2].animate.set(fill_color="#AEF2B8"),
            grid[1][1].animate.set(fill_color="#AEF2B8"),
            run_time=0.7
        )
        self.wait(1)
        self.play(bottom_pieces[0][0].animate.move_to(grid[1][1]))
        self.wait(0.3)
        self.play(
            grid[2][1].animate.set(fill_color="#AEF2B8"),
            run_time=0.7
        )
        self.wait(1)
        self.play(bottom_pieces[0][1].animate.move_to(grid[0][2]))    
        self.wait(0.3)    
        self.play(
            grid[0][0].animate.set(fill_color=WHITE),
            grid[0][2].animate.set(fill_color=WHITE),
            grid[1][1].animate.set(fill_color=WHITE),
            grid[2][1].animate.set(fill_color=WHITE),
            run_time=0.7
        )
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.remove(*self.mobjects)