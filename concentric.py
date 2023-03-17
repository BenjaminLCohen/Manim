from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl diametric.py ShowDia
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class ConCir(Scene):
    def construct(self):
        n = 30  # Replace this with the desired number of circles
        min_radius = 1
        max_radius = 5

        # Calculate the step size for the radius
        radius_step = (max_radius - min_radius) / (n - 1)

        # Create the concentric circles
        circles = [Circle(radius=min_radius + i * radius_step) for i in range(n)]

        # Create the diametric circles on both sides
        diametric_circles_right = [
            Circle(radius=(radius_step / 2)).next_to(circles[i], direction=RIGHT, buff=0)
            for i in range(n - 1)
        ]
        diametric_circles_left = [
            Circle(radius=(radius_step / 2)).next_to(circles[i], direction=LEFT, buff=0)
            for i in range(n - 1)
        ]

        # Animate the concentric circles and diametric circles
        self.play(
            *[
                FadeIn(circle)
                for circle in circles + diametric_circles_right + diametric_circles_left
            ]
        )

        # Wait for a moment before ending the scene
        self.wait()