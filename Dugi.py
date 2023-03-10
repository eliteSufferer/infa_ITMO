from turtle import *
from math import sqrt
# pensize(3)
# lt (90)
# color('blue', 'aqua')
# begin_fill()
# for i in range(4):
#     circle(50, 180)
#     rt(180)
# rt(180)
# circle(200, 180)
# end_fill()

dist = sqrt(128)*10


def draw_grass():
    color('lightgreen')
    for i in range(4):
        begin_fill()
        fd(dist)
        lt(135)
        fd(80)
        lt(90)
        fd(80)
        lt(135)
        end_fill()
        fd(dist)


def draw_flower():
    lt(180)
    fd(dist*3)
    rt(90)
    penup()
    fd(30)
    pendown()
    fd(100)
    rt(90)
    circle(50)
    rt(90)
    color("black", "yellow")
    for i in range(5):
        begin_fill()
        circle(35, 252)
        rt(180)
        end_fill()
    color("black", "white")
    lt(90)
    begin_fill()
    circle(50)
    end_fill()


draw_grass()
draw_flower()

penup()
fd(700)
