from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class ShowTan(Scene):
    def construct(self):

        axes = Axes()

        intro_words = Text("What does it mean for two balls to be tangent?")
        intro_words.to_edge(UP)

        intro_quest = Text("This is Tangent?")
        intro_quest.to_edge(UP)

        intro_questTwo = Text("can we define tangent by only using part?")
        intro_questTwo.to_edge(UP)

        intro_questThree= Text("well lets try")
        intro_questThree.to_edge(UP)
    
        left_circle = Circle(radius=2.0)
        left_circle.set_stroke(BLUE_D)

        right_circle = Circle(radius=2.0)
        right_circle.move_to(axes.c2p(2,0))
        right_circle.set_stroke(BLUE_D)

        star1_circle = Circle(radius=3)
        star1_circle.move_to(axes.c2p(2,0))
        star1_circle.set_stroke(RED_D)
        star1_circle = DashedVMobject(star1_circle,num_dashes=50)

        star2_circle = Circle(radius=2.0)
        star2_circle.move_to(axes.c2p(1,0))
        star2_circle.set_stroke(RED_D)
        star2_circle = DashedVMobject(star2_circle,num_dashes=50)

        star3_circle = Circle(radius=1.5)
        star3_circle.move_to(axes.c2p(.5,0))
        star3_circle.set_stroke(RED_A)
        star3_circle = DashedVMobject(star3_circle,num_dashes=50)

        star4_circle = Circle(radius=2.5)
        star4_circle.move_to(axes.c2p(1.5,0))
        star4_circle.set_stroke(RED_B)
        star4_circle = DashedVMobject(star4_circle,num_dashes=50)

        star5_circle = Circle(radius=3.5)
        star5_circle.move_to(axes.c2p(2.5,0))
        star5_circle.set_stroke(RED_C)
        star5_circle = DashedVMobject(star5_circle,num_dashes=50)


        #start animation
        self.play(Write(intro_words))
        self.wait(0.5)
        self.play(Write(left_circle))
        self.wait(0.75)
        self.play(left_circle.animate.move_to(axes.c2p(-2, 0)))
        self.wait(0.75)

        self.play(FadeOut(intro_words))
        self.play(Write(right_circle))
        self.play(Write(intro_quest))
        self.wait(0.5)
        self.play(FadeOut(intro_quest))

        self.play(Write(intro_questTwo))
        self.wait(0.5)
        self.play(FadeOut(intro_questTwo))

        self.play(Write(intro_questThree))

        self.play(ScaleInPlace(right_circle,0.5),
                  ScaleInPlace(left_circle,0.5))
        self.play(right_circle.animate.move_to(axes.c2p(0,0)))

        self.wait(2.0)
        self.play(Write(star1_circle),
                  Write(star2_circle))
        
        self.play(FadeOut(intro_questThree))

        self.wait(1.0)

        self.play(right_circle.animate.move_to(axes.c2p(.25, 0)))

        self.wait(2.0)
        self.play(star1_circle.animate.move_to(axes.c2p(2.15, 0.3)),
                  star2_circle.animate.move_to(axes.c2p(1, -0.4)))
        
        self.wait(2.0)

        self.play(star1_circle.animate.move_to(axes.c2p(2, 0)),
                  star2_circle.animate.move_to(axes.c2p(1, 0)),
                  right_circle.animate.move_to(axes.c2p(0, 0)))
        
        self.wait(2.0)

        self.play(Write(star3_circle),
                  Write(star4_circle),
                  Write(star5_circle))



        
      



       