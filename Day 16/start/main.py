from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.color("red")

def fractal(n, l):
    if n == 0:
        return

    timmy.forward(l)

    timmy.left(45)
    fractal(n - 1, l / 2)
    timmy.right(90)
    fractal(n - 1, l / 2)
    timmy.left(45)

    timmy.back(l)


timmy.back(200)
fractal(10, 300)

screen.exitonclick()

