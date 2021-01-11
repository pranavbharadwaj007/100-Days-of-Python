from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.p1_score = None
        self.color("white")
        self.ht()
        self.goto(x=0, y=270)

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):

        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):

        self.clear()
        phrase = f"Score: {self.score}"
        self.write(arg=phrase, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)