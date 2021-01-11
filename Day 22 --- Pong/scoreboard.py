from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(x=0, y=230)


        self.p1_score = 0
        self.p2_score = 0
        self.refresh()

    def refresh(self):

        self.clear()

        self.goto(-100, 230)
        self.write(arg=self.p1_score, align=ALIGNMENT, font=FONT)

        self.goto(100, 230)
        self.write(arg=self.p2_score, align=ALIGNMENT, font=FONT)