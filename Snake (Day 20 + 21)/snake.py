from turtle import Turtle

MOVE_DIST   = 20

UP          = 90
DOWN        = 270
LEFT        = 180
RIGHT       = 0

class Snake:

    def __init__(self, length=3):

        self.length = length

        self.segments = []
        self.create_snake()

        self.head = self.segments[0]

    def create_snake(self):

        for i in range(self.length):

            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(x=-20 * i, y=0)
            self.segments.append(seg)

    def create_segment(self):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        self.segments.append(seg)
        self.length += 1

    def move(self):

        for num in range(self.length - 1, 0, -1):

            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()

            self.segments[num].goto(x=new_x, y=new_y)

        # Move head alone
        self.head.forward(MOVE_DIST)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
