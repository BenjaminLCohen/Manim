from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl diametric.py ShowDia
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class ShowDia(Scene):
    def construct(self):

        axes = Axes()

        intro_words = Text("What does it mean for three balls to be diametric?")
        intro_words.to_edge(UP)

        intro_quest = Text("all 3 balls are co-linear or they are tangent on opicite sides.")
        intro_quest.to_edge(UP)

        intro_questTwo = Text("can we define tangent by only using part?")
        intro_questTwo.to_edge(UP)

        intro_questThree= Text("well lets try")
        intro_questThree.to_edge(UP)
    
        left_circle = Circle(radius=1.0)
        left_circle.move_to(axes.c2p(-3,0))
        left_circle.set_stroke(BLUE_D)

        right_circle = Circle(radius=1.0)
        right_circle.move_to(axes.c2p(3,0))
        right_circle.set_stroke(BLUE_D)

        center_circle = Circle(radius=2.0)
        center_circle.move_to(axes.c2p(0,0))
        center_circle.set_stroke(GREEN_D)



        new_left_circle = Circle(radius=0.5)
        new_left_circle.move_to(axes.c2p(-1.5,0))
        new_left_circle.set_stroke(BLUE_D)

        new_right_circle = Circle(radius=0.5)
        new_right_circle.move_to(axes.c2p(1.5,0))
        new_right_circle.set_stroke(BLUE_D)

        new_center_circle = Circle(radius=1.0)
        new_center_circle.move_to(axes.c2p(0,0))
        new_center_circle.set_stroke(GREEN_D)



        new1_left_circle = Circle(radius=0.25)
        new1_left_circle.move_to(axes.c2p(-3,.75))
        new1_left_circle.set_stroke(BLUE_D)

        new1_right_circle = Circle(radius=0.25)
        new1_right_circle.move_to(axes.c2p(-3,-.75))
        new1_right_circle.set_stroke(BLUE_D)

        new1_center_circle = Circle(radius=0.5)
        new1_center_circle.move_to(axes.c2p(-3,0))
        new1_center_circle.set_stroke(GREEN_D)

        new2_center_circle = Circle(radius=0.50664)
        new2_center_circle.move_to(axes.c2p(-3.100,0))
        new2_center_circle.set_stroke(GREEN_D)



        star1_circle = Circle(radius=2.5)
        star1_circle.move_to(axes.c2p(3.5,0))
        star1_circle.set_stroke(RED_D)
        

        star2_circle = Circle(radius=2.5)
        star2_circle.move_to(axes.c2p(-3.5,0))
        star2_circle.set_stroke(RED_D)
        

        star3_circle = Circle(radius=500)
        star3_circle.move_to(axes.c2p(501,0))
        star3_circle.set_stroke(RED_D)
        

        star4_circle = Circle(radius=500)
        star4_circle.move_to(axes.c2p(-501,0))
        star4_circle.set_stroke(RED_D)
        

        star5_circle = Circle(radius=1.5)
        star5_circle.move_to(axes.c2p(-3,-2))
        star5_circle.set_stroke(RED_D)

        star6_circle = Circle(radius=1.5)
        star6_circle.move_to(axes.c2p(-3,2))
        star6_circle.set_stroke(RED_D)

        star7_circle = Circle(radius=1.5)
        star7_circle.move_to(axes.c2p(-2.8348,-1.989))
        star7_circle.set_stroke(RED_D)

        star8_circle = Circle(radius=1.5)
        star8_circle.move_to(axes.c2p(-2.8348,1.989))
        star8_circle.set_stroke(RED_D)
        
        radhold = 0.1

        star9_circle = Circle(radius=100.000-radhold)
        star9_circle.move_to(axes.c2p(10.183331436,-99.62498299))
        star9_circle.set_stroke(RED_D)

        star10_circle = Circle(radius=100.000-radhold)
        star10_circle.move_to(axes.c2p(10.183331436,99.62498299))
        star10_circle.set_stroke(RED_D)

        star11_circle = Circle(radius=100.000)
        star11_circle.move_to(axes.c2p(-3,-100.5))
        star11_circle.set_stroke(RED_D)

        star12_circle = Circle(radius=100.000)
        star12_circle.move_to(axes.c2p(-3,100.5))
        star12_circle.set_stroke(RED_D)
 


        #start animation
        self.play(Write(intro_words))
        self.wait(0.5)
        self.play(Write(center_circle))
        self.wait(0.25)
        self.play(FadeIn(left_circle),
                  FadeIn(right_circle))
        self.wait(0.75)

        self.play(
        Transform(center_circle, new_center_circle),
        Transform(left_circle, new_left_circle),
        Transform(right_circle, new_right_circle))

        self.play(FadeOut(intro_words))

        self.wait(0.75)       
        self.play(FadeIn(star1_circle),
                  FadeIn(star2_circle))
        
        self.wait(1)

        self.play(
        Transform(star1_circle, star3_circle),
        Transform(star2_circle, star4_circle),run_time=5)

        self.wait(1)

        self.play(FadeOut(star1_circle),
                  FadeOut(star2_circle),run_time=1)

        self.play(
        Transform(center_circle, new1_center_circle),
        Transform(left_circle, new1_left_circle),
        Transform(right_circle, new1_right_circle),run_time=1)
        self.play(FadeIn(star5_circle),
                  FadeIn(star6_circle))
        
        self.wait(1)

        self.play(
        Transform(center_circle, new2_center_circle),
        Transform(star5_circle, star7_circle),
        Transform(star6_circle, star8_circle))

        self.play(
        Transform(star5_circle, star9_circle),
        Transform(star6_circle, star10_circle),run_time=4)

        self.wait(1)


        self.play(
        Transform(center_circle, new1_center_circle),
        Transform(star5_circle, star11_circle),
        Transform(star6_circle, star12_circle))








        
    




        



