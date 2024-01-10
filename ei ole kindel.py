# markus laanemäe
# 28.11.2023
# ülesanne 5

import turtle
import random

w = turtle.Screen()
w.setup(600,600)

def viisnurk():
    a = random.randint(50,100)
    x = random.randint(-300,300-a)
    y = random.randint(-300+(a//2),300-(a//2))
    pitsu = turtle.Turtle()
    pitsu.hideturtle()
    pitsu.speed("fastest")
    pitsu.penup()
    pitsu.goto(x,y)
    pitsu.pendown()
    pitsu.left(random.randint(0,360))
    for i in range(5):
        pitsu.fd(a)
        pitsu.rt(144)

def kolmnurk():
    a = random.randint(50,100)
    x = random.randint(-300,300-a)
    y = random.randint(-300+(a//2),300-(a//2))
    pitsu = turtle.Turtle()
    pitsu.hideturtle()
    pitsu.speed("fastest")
    pitsu.penup()
    pitsu.goto(x,y)
    pitsu.pendown()
    pitsu.left(random.randint(0,360))
    pitsu.pencolor("red")
    for i in range(5):
        pitsu.fd(a)
        pitsu.rt(120)

def suvaline():
    suv = random.randint(1,2)
    if suv == 1:
        viisnurk()
    else:
        kolmnurk()


def kuvamenyy():
    loop = 1
    while loop==1:
        valikujund = w.numinput("Kujundi valik","1. vali viisnurk \n2. vali kolmnurk \n3. vali suvaline \n4. EXIT ")
        if valikujund >= 4:
            exit()
        valiKogus = int(w.numinput("Kujundite arv","vali kujundite arv"))
        for i in range(valiKogus):
            if valikujund == 1:
                viisnurk()
            elif valikujund == 2:
                kolmnurk()
            elif valikujund == 3:
                suvaline()
            else:
                print("EXIT")
                



kuvamenyy()

turtle.exitonclick()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
    
   