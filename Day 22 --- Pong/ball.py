import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):

        super().__init__()
        self.speed = 5
        self.shape("circle")
        self.color("white")
        self.width(20)
        self.penup()

        self.reset()

    def reset(self):

        self.speed = 5
        angle = random.randrange(30, 150)
        side = random.choice([1, -1])

        self.goto(0, 0)
        self.setheading(90 + (angle * side))

    def x_bounce(self):

        self.setheading(180 - self.heading())

    def y_bounce(self):

        self.setheading(3 - self.heading())

    def refresh(self):

        self.forward(self.speed)