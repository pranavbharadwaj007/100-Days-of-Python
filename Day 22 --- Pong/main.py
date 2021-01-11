from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


p1 = Paddle(-350, 0)
p2 = Paddle(350, 0)


ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(key="w", fun=p1.go_up)
screen.onkeypress(key="s", fun=p1.go_down)

screen.onkeypress(key="Up", fun=p2.go_up)
screen.onkeypress(key="Down", fun=p2.go_down)


game_is_on = True
while game_is_on:

    ball.refresh()
    scoreboard.refresh()

    # Detect wall collision
    if ball.ycor() > 290 or ball.ycor() < -280:

        ball.y_bounce()

    # Detect collision with paddles
    if (ball.distance(p1) < 50 and ball.xcor() < -340) or (ball.distance(p2) < 50 and ball.xcor() > 340):

        ball.x_bounce()
        ball.speed += 1

    elif ball.xcor() < -340:

        scoreboard.p2_score += 1
        ball.reset()
        time.sleep(3)

    elif ball.xcor() > 340:

        scoreboard.p1_score += 1
        ball.reset()

    screen.update()
    time.sleep(0.03)


screen.exitonclick()