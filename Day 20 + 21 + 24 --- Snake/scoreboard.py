from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self, high_score):

        super().__init__()
        self.p1_score = None
        self.color("white")
        self.ht()
        self.up()
        self.goto(x=0, y=270)

        self.score = 0
        self.high_score = int(high_score)
        self.update_scoreboard()

    def increase_score(self):

        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):

        self.clear()
        self.goto(x=-100, y=270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=270)
        self.write(arg=f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):

        if self.score > self.high_score:

            self.high_score = self.score

            with open("highscore.txt", "w") as file:

                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)