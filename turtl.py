import turtle
from time import *

pen = turtle
pen.color('red')

def bgcolor(param):
    pass


bgcolor('black')

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    pen.end_fill()

font = ("Montserrat", 16, "bold")


def draw_text():
    pen.pu()
    pen.setpos(-50, 90)
    pen.down()
    pen.color('white')
    pen.write("Я тебя люблю", font=font)
    pen.up()
    pen.setpos(-70, 70)
    pen.down()
    time.sleep(3)


draw_heart()
draw_text()
pen.ht()


def done():
    pass


done()


