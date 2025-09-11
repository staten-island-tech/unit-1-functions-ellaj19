import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

""" def equal(x):
    t.forward(x)
    t.right(240)
    t.forward(x)
    t.right(240)
    t.forward(x)
    t.right(240)
equal(120) """


""" def square(x,y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
square(125,100)


for i in range(240):
    square(125,100)
    t.left(5) 
   
    t.speed(0) """

def spiralstar(x):
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
spiralstar(20)

size = 25
for i in range(60):
    spiralstar(size)
    t.left(5)
    size += 25