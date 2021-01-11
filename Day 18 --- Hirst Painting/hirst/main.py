#import colorgram
#
#extract = colorgram.extract('hirst.jpg', 10)
#
#colours = []
#for i in range(len(extract)):
#    r = extract[i].rgb.r
#    g = extract[i].rgb.g
#    b = extract[i].rgb.b
#    colours.append((r, g, b))
#
#print(colours)

from turtle import Turtle, Screen
import random

colours = [(231, 205, 85), (228, 148, 89), (120, 167, 186), (216, 222, 227), (162, 11, 19), (31, 111, 160), (234, 81, 45)]

tim = Turtle()
tim.speed(0)
screen = Screen()
screen.colormode(255)


def hirst(d, space):

    tim.up()
    tim.backward(300)
    tim.right(90)
    tim.forward(300)
    tim.left(90)
    tim.down()
    tim.hideturtle()

    for y in range(10):

        for x in range(10):

            tim.pendown()
            tim.dot(d, random.choice(colours))

            tim.penup()
            tim.forward(space)

        tim.penup()
        tim.left(90)
        tim.forward(space)
        tim.right(90)
        tim.backward(space*10)


hirst(20, 50)


screen.exitonclick()