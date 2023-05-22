import random
from random import randint
from shutil import move
import turtle
#import colormode
t = turtle.Turtle()
t.speed(0)

def pen(color):
    t.color(color)

pen('red')

def koor():
    t.pu()
    x=random.randint(-165,165)
    y=random.randint(-165,165)
    t.goto(x,y)
    t.pd()

def sky(colour):
     wn = turtle.Screen()
     wn.bgcolor(colour)

sky('yellow')

turtle.colormode(255)
def firework(size):
    for num in range(20):
         t.fd(size)
         t.rt(190)
while True:
    t.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
    for i in range(5):
        firework(random.randint(40,200))
        koor()
    t.clear()