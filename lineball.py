from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl diametric.py ShowDia
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class ShowLin(Scene):
    def construct(self):

        axes = Axes()

        intro_words = Text("Can we have a line without any points")
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


        line1 = Line()
        line1.put_start_and_end_on(axes.c2p(10,0),axes.c2p(-10,0))
        line1.set_stroke(BLUE_B)




        new_left_circle = Circle(radius=0.5)
        new_left_circle.move_to(axes.c2p(-1,0))
        new_left_circle.set_stroke(BLUE_D)

        new_right_circle = Circle(radius=0.5)
        new_right_circle.move_to(axes.c2p(1,0))
        new_right_circle.set_stroke(BLUE_D)

        new_center_circle = Circle(radius=0.5)
        new_center_circle.move_to(axes.c2p(0,0))
        new_center_circle.set_stroke(BLUE_D)



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



        star1_circle = Circle(radius=0.5)
        star1_circle.move_to(axes.c2p(2,0))
        star1_circle.set_stroke(BLUE_D)
        
        star2_circle = Circle(radius=0.5)
        star2_circle.move_to(axes.c2p(3,0))
        star2_circle.set_stroke(BLUE_D)
        
        star3_circle = Circle(radius=0.5)
        star3_circle.move_to(axes.c2p(4,0))
        star3_circle.set_stroke(BLUE_D)

        star4_circle = Circle(radius=0.5)
        star4_circle.move_to(axes.c2p(5,0))
        star4_circle.set_stroke(BLUE_D)

        star5_circle = Circle(radius=0.5)
        star5_circle.move_to(axes.c2p(6,0))
        star5_circle.set_stroke(BLUE_D)

        star6_circle = Circle(radius=0.5)
        star6_circle.move_to(axes.c2p(7,0))
        star6_circle.set_stroke(BLUE_D)


        
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

        self.wait(0.75)

        self.play(Write(star1_circle))
        
        self.wait(0.75)

        self.play(Write(star2_circle))
        introball = Group(star1_circle,star2_circle,center_circle,left_circle,right_circle)
        
        radius1 = 0.5
        num_circles = 1997
        circles = []
        for i in range(num_circles):
            circle = Circle(radius=radius1)
            circle.set_stroke(BLUE_D)
            if i == 0:
                circle.move_to(ORIGIN)
            else:
                prev_circle = circles[i-1]
                circle.next_to(prev_circle, RIGHT, buff=0)
            circles.append(circle)
        circle_group = VGroup(*circles)
        circle_group.move_to(ORIGIN)

        #line = Line(start=LEFT*8, end=RIGHT*8, color=BLUE_D)
        #line.move_to(ORIGIN)

        self.play(FadeIn(circle_group))
        self.play(FadeOut(introball))
        self.wait(2)
        self.play(circle_group.animate.scale(0.0109),run_time=4)
        #elf.play(Transform(circle_group,line))
        



      




        