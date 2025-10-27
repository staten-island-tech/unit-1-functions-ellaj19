""" import turtle
from turtle import *
t = Turtle()
t.shape('turtle') """

""" def equal(x):
    t.forward(x)
    t.right(240)
    t.forward(x)
    t.right(240)
    t.forward(x)
    t.right(240)
equal(120)



def square(x,y):
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
   
    t.speed(0)  """

""" def spiralstar(x):
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


for i in range(4):
    t.forward(100)
    t.left(90)




size = 25
for i in range(60):
    spiralstar(size)
    t.left(5)
    size += 25

def rectangle():
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
rectangle()

def rectangle(x,y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
rectangle(125,100) """


def casino(q,f,s,t):
    plays = 0
    while q > 0:
        f += 1
        plays += 1
        q = q - 1
        if f == 35:
            f = 0
            q = q + 30
        elif q == 0:
            print(f"martha can play {plays} times until she goes broke")
        s += 1
        plays += 1
        q = q - 1
        if s == 100:
            s = 0
            q = q + 60
        elif q == 0:
            print(f"martha can play {plays} times until she goes broke")
        t += 1
        plays += 1
        q = q - 1
        if t == 10:
            t = 0
            q = q + 9
        elif q == 0:
            print(f"martha can play {plays} times until she goes broke")

casino(48 , 3 , 10 , 4)

