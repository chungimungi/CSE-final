while True:
    print("****Choose the pattern****")
    print("1.DNA Structures")
    print("2.Spirograph")    
    print("3.Lissajous Curves")
    print("4. Exit")
    choice=int(input("Enter your choice:"))


    if choice==1:
        print("1. 3D structure")
        print("2. 2D structure")
        chi=int(input("Enter which structure you want to see: "))
        if chi==1:
            import pygame as pg
            import numpy as np
            from math import sin, cos

            WIDTH = 800
            HEIGHT = 1000

            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)
            GREEN = (0, 255, 0)
            YELLOW = (255, 255, 0)
            RED = (255, 0, 0)
            BLUE = (0, 191, 255)

            pg.init()

            clock = pg.time.Clock()
            screen = pg.display.set_mode((WIDTH, HEIGHT))


            class proj:
                def __init__(self, width, height):
                    self.width = width
                    self.height = height
                    self.screen = pg.display.set_mode((width, height))
                    self.background = BLACK
                    self.surfaces = {}

                def addsurf(self, name, surface):
                    self.surfaces[name] = surface

                def drcirc(self):
                    for surface in self.surfaces.values():
                        for node in surface.nodes:
                            pg.draw.circle(self.screen, WHITE, (WIDTH / 2 + int(node[0]), int(node[2])), 5)

                def rZ(self, theta):
                    for surface in self.surfaces.values():
                        center = surface.findCentre()

                        c = np.cos(theta)
                        s = np.sin(theta)

                        matrix = np.array([[c, -s, 0, 0],
                                           [s, c, 0, 0],
                                           [0, 0, 1, 0],
                                           [0, 0, 0, 1]])

                        surface.rotate(center, matrix)


            class obj:
                def __init__(self):
                    self.nodes = np.zeros((0, 4))

                def addnod(self, node_array):
                    ones_column = np.ones((len(node_array), 1))
                    ones_added = np.hstack((node_array, ones_column))
                    self.nodes = np.vstack((self.nodes, ones_added))

                def findCentre(self):
                    mean = self.nodes.mean(axis=0)
                    return mean

                def rotate(self, center, matrix):
                    for i, node in enumerate(self.nodes):
                        self.nodes[i] = center + np.matmul(matrix, node - center)

                    for m in range(0, 100, 4):
                        drlin(m, m + 1, self.nodes, GREEN, RED)

                    for m in range(2, 100, 4):
                        drlin(m, m + 1, self.nodes, YELLOW, BLUE)


            def drlin(i, j, k, color1, color2):
                a = k[i]
                b = k[j]
                c = (a[0] + b[0]) / 2
                pg.draw.line(screen, color1, (WIDTH / 2 + a[0], a[2]), (WIDTH / 2 + c, b[2] - 6), 3)
                pg.draw.line(screen, color2, (WIDTH / 2 + c, a[2] + 6), (WIDTH / 2 + b[0], b[2]), 3)


            helix = []

            for t in range(100):
                x = round(60 * cos(3 * t), 0)
                y = round(60 * sin(3 * t), 0)
                z = 12 * t
                helix.append((x, y, z))

            spin = 0

            running = True
            while running:

                clock.tick(60)

                pv = proj(WIDTH, HEIGHT)

                dna = obj()
                dna_nodes = [i for i in helix]
                dna.addnod(np.array(dna_nodes))

                pv.addsurf('DNA', dna)
                pv.rZ(spin)
                pv.drcirc()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False

                pg.display.update()
                spin += 0.02
            pg.quit()
                

        elif chi==2:
 
            import math 
            def printUpperHalf(str): 

                    first=0
                    second=0
                    pos = 0
                    for i in range(1,5): 

                                
                            first = str[pos] 
                            second = str[pos+1] 
                            pos += 2
                                
                            for j in range ( 4 - i, 0,-1): 
                                    print(" ",end="") 
                            print(first,end="") 
                            for j in range (1, i): 
                                    print("--",end="") 
                            print(second) 
                        
            def printLowerHalf(str): 

                    first=0
                    second=0
                    pos = 0
                    for i in range(1,5): 

                            first = str[pos] 
                            second = str[pos+1] 
                            pos += 2
                                
                            for j in range(1,i): 
                                    print(" ",end="") 
                            print(first,end="") 
                            for j in range (4 - i, 0,-1): 
                                    print("--",end="") 
                            print(second) 


                 
            def printDNA( str, n): 

                    for i in range(0,n): 

                            x = i % 6
                            if (x % 2 == 0): 
                                    printUpperHalf(str[x]) 
                            else:
                                printLowerHalf(str[x]) 

            n = 8
            DNA = [ "ATTAATTA", "TAGCTAGC", "CGCGATAT", 
                        "TAATATGC", "ATCGTACG", "CGTAGCAT" ]
            printDNA(DNA, n)

    elif choice==2:
        print("1. Rosetta Orbit")
        print("2. Basic Spirograph using a square")
        chis=int(input("Enter which one you would like to see:"))
        

        if chis==1:
            import turtle as tt
            tt.bgcolor('black')
            tt.pensize(2)
            tt.speed(100)

            for i in range(6):
                for color in ('red','blue','red','blue','red','blue','red'):
                    tt.color(color)
                    tt.circle(100)
                    tt.left(10)
                    tt.right(20)
                tt.hideturtle()

        elif chis==2:
            from turtle import *
            from random import randint
            speed(0)
            bgcolor('black')
            x=1
            while x<400:
                r=randint(0,255)
                g=randint(0,255)
                b=randint(0,255)

                colormode(255)
                pencolor(r,g,b)

                fd(50+x)
                rt(90.911)
                x=x+1
            exitonclick()

    elif choice==3:
        import turtle
        from math import cos,sin
        from time import sleep

        window = turtle.Screen()
        window.bgcolor("#000000")

        myPen = turtle.Turtle()
        myPen.hideturtle()
        myPen.speed(0)
        myPen.pensize(3)
        myPen.color("#FFFF00")

        myPen.penup()

        A = 100
        B = 100
        a = 3 
        b = 4
        delta = 3.14/2
        t=0

        for i in range(0,1000):
            t+=0.01
            #Apply Lissajous Parametric Equations
            x = A * sin(a*t + delta) 
            y = B * sin(b*t) 

            myPen.goto(x,y)
            myPen.pendown()
            myPen.getscreen().update() 

        sleep(0.5)

  
    elif choice==4:
        break
