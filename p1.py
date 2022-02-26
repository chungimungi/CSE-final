while True:
    print("****OPTION LIST****")
    print("1.Archimede's Spiral")
    print("2.DNA Structures")
    print("3.Spirograph")    
    print("4.Lissajous Curves")
    print("5. Exit")
    choice=int(input("Enter your choice:"))


    if choice==1:
        import turtle
        import random

        fred=turtle.Turtle()
        fred.speed(0)

        colours = ["red","green","blue","yellow","orange","gold","purple","cyan","brown"]

        length = 500
        angle = 91
        circle_size= 10

        for side in range(length):
            print(side)
            colour = random.choice(colours)
            fred.pencolor(colour)
            fred.fillcolor(colour)
            fred.penup
            fred.forward(side)
            fred.pendown()
            fred.left(angle)
            fred.begin_fill()
            fred.circle(circle_size)
            fred.end_fill()

        turtle.exitonclick()

    elif choice==2:
        print("1. 3D structure")
        print("2. 2D structure")
        chi=int(input("Enter which structure you want to see: "))
        if chi==1:

            from math import cos, sin, pi

            print("The nitrogen bases present in the DNA are:")
            print("Adenine")
            print("Cytosine")
            print("Guanine")
            print("Thymine")
            print("They tend to form hydrogen bonds between Adenine and Thymine and Cytosine and Guanine")

            length = 50
            width = 30
            thickness = 10
            rotation = 0.15
            strands = [0, 2 * pi / 3]
            strand_char = "~"

            radius = width / 2
            for line in range(length):
                output = [" "] * (width + thickness + 2)
                total_rotation = -line * rotation
                sorted_strands = sorted(strands, key=lambda s: cos(total_rotation + s))
                for strand_offset in sorted_strands:
                    pos = int(radius * sin(total_rotation + strand_offset) + radius)
                    output[pos: pos + thickness + 2] = " " + strand_char * thickness + " "
                print("".join(output))

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

    elif choice==3:
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

    elif choice==4:
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

  
    elif choice==5:
        break

