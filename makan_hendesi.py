from formula import  mohit_dayere_mokhtasat
import random
from cha import *
class av(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"
        chagh = chaghCreature()
        chagh.scale(0.7)
        chagh.to_edge(DR)
        chagh.set_color(BLUE_B)
        chagh.set_stroke(width=0.5)
        chagh.set_fill(opacity=0.8)
        self.play(FadeIn(chagh))
        
        soal1=Text("مکان هندسی مرکز همه دایره‌هایی با شعاع ثابت r،",font="B Nazanin")
        soal1.set_color(BLACK)
        soal1.scale(0.8)
        soal1.to_edge(UP)
        soal2=Text("که بر دایره C(O,r) در صفحه این دایره مماس خارجی اند را بدست آورید.",font="B Nazanin")
        soal2.set_color(BLACK)
        soal2.scale(0.8)
        soal2.next_to(soal1,DOWN)

        self.play(Write(soal1,reverse=True),ApplyMethod(chagh.change,"frown" ,soal1))
        
        self.play(Write(soal2,reverse=True),ApplyMethod(chagh.look_at,soal2))
        self.play(ApplyMethod(chagh.change,"think"))
        self.wait(1)
        #creating the circle with stroke tiny
        def dayere_markaz_dar(radius,color,stroke_width=1):

            circle = Circle(radius=radius,color=color,stroke_width=stroke_width)
            dot = Dot(color=RED_E,radius=0.05)
            gorup = VGroup(circle,dot)
            
            return gorup

        circle = dayere_markaz_dar(radius=1,color=GREEN_E,stroke_width=5.5)
        circle.set_color(GREEN)
        o = Text("O")
        o.scale(0.5)
        o.set_color(BLACK)
        o.next_to(circle[1],LEFT*0.6)
        #creat a yellow line from [0,0,0] to [1,0,0] 
        line = Line(start=ORIGIN,end=RIGHT*1,stroke_width=2,color=YELLOW)
        brace = Brace(line,UP)
        
        brace.scale(0.8)   
        brace.next_to(line,UP*0.5)

        brace.set_color(BLACK)
        text = Text("   شعاع = r   ",font="B Nazanin")
        text.scale(0.25)
        text.set_color(BLACK)
        text.next_to(brace,UP*0.3)
        
        
        self.play(Create(line),Write(brace),Write(text,reverse=True),Create(circle),Write(o),ApplyMethod(chagh.change,"plain" ,circle))
        self.wait(2)
        self.play(FadeOut(soal1),FadeOut(soal2))
        list_dayere=[]
        color_list = [RED,BLUE,YELLOW,PURPLE,ORANGE,GREEN,PINK,TEAL]
        for i in range(1,50,6):
            list_mokhtasat = mohit_dayere_mokhtasat(i)
            v=random.choice([1,-1])
            for j in range(len(list_mokhtasat)):
                #creating the circle with random color
                dayere = dayere_markaz_dar(1,color = random.choice(color_list))
                dayere.move_to(list_mokhtasat[j]*2*v)
                list_dayere.append(dayere)
                self.play(Create(dayere),ApplyMethod(chagh.change,"smile" ,dayere),run_time= 1/(i*i*0.2))
        self.wait(2)             
        circle2 = dayere_markaz_dar (radius=2,color=RED,stroke_width=5.5)
        vg= VGroup()
        for x in list_dayere:
            vg.add(x)
            
        self.play(FadeOut(vg),
                FadeOut(circle),
                FadeOut(brace),
                FadeOut(text),
                FadeOut(line),
                FadeIn(circle2),ApplyMethod(chagh.change,"smile" ,circle),run_time=2)
        self.wait(2)
        #creat a yellow line from [0,0,0] to [1,0,0] 
        line = Line(start=ORIGIN,end=RIGHT*2,stroke_width=2,color=YELLOW)
        brace = Brace(line,UP)
        brace.set_color(BLACK)
        text = Text("   شعاع = ۲r   ",font="B Nazanin")
        text.scale(0.4)
        text.set_color(BLACK)
        text.next_to(brace,UP)
        self.play(Create(line),Write(brace),Write(text,reverse=True))
        self.wait(1)
        javab = Text("دایره‌ای به مرکز O و شعاع ۲r مکان هندسی مورد نظر ما می‌باشد.",font="B Nazanin")
        javab.scale(0.7)
        javab.set_color(BLACK)
        javab.to_edge(DOWN)
        javab.shift(LEFT*1.3)
        self.play(Write(javab,reverse=True ),ApplyMethod(chagh.change,"plain" ,javab))
        self.wait(2)

