from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class ShowInt(Scene):
    def construct(self):

        tarski= ImageMobject("/Users/BennyCohen/manim/gunk/TarskiPhoto.jpeg")
        tarski.scale(1.2)
        tarski.to_edge(RIGHT, buff=1)

        self.play(FadeIn(tarski))
        self.wait(1.0)
        self.play(tarski.animate.shift(LEFT*4))