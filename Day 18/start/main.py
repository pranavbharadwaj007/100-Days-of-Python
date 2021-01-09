from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.speed(10)
tim.pensize(10)

screen = Screen()
screen.colormode(255)

def square(l):

    for i in range(4):

        tim.forward(l)
        tim.right(90)


colours = ["red", "blue", "green", "yellow", "medium aquamarine", "aquamarine", "dark red", "olive drab", "rosy brown", "deep pink", "khaki", "dark orange", "dark khaki"]

def dashed(l):

    line = (l / 10) / 2

    for _ in range(10):

        tim.pendown()
        tim.forward(line)
        tim.penup()
        tim.forward(line)


def shapes(l):

    for x in range(3, 11):

        angle = 360 / x
        tim.color(random.choice(colours))

        for y in range(x):

            tim.forward(l)
            tim.right(angle)


def rand_walk(n, l):

    for i in range(n):
        angle = 90 * round(random.randint(0, 360)/90)
        tim.right(angle)

        tim.color(random_colour())

        tim.forward(l)


def random_colour():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


def spirograph(n, l):

    tim.pensize(1)
    tim.speed(0)


    for i in range(n):

        tim.color(random_colour())

        tim.circle(l)

        tim.right(360/n)


def hirst():

    pass


#square(100)
#dashed(200)
#shapes(100)
#rand_walk(200, 30)
#spirograph(200, 100)


screen.exitonclick()