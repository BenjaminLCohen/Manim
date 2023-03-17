from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl diametric.py ShowDia
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class Grid(Scene):
    def construct(self):
        # Create a 3x3 grid of circles
        circles = self.create_circle_grid()

        # Display the grid of circles
        self.play(*[FadeIn(circle) for circle in circles])

        # Wait for a moment
        self.wait()

        # Transform the circles into squares
        squares = self.create_square_grid()
        self.play(*[Transform(circle, square) for circle, square in zip(circles, squares)], run_time=1)

        # Wait for a moment
        self.wait()

    def create_circle_grid(self):
        circle_grid = []
        for i in range(3):
            for j in range(3):
                circle = Circle(radius=0.25)
                circle.shift(UP * i + RIGHT * j - UP - RIGHT)
                circle_grid.append(circle)
        return circle_grid

    def create_square_grid(self):
        square_grid = []
        for i in range(3):
            for j in range(3):
                square = Square(side_length=2 * 0.25)
                square.shift(UP * i + RIGHT * j - UP - RIGHT)
                square_grid.append(square)
        return square_grid