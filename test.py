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

t.speed(5)

def square():
    for i in range(4): 
     t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)