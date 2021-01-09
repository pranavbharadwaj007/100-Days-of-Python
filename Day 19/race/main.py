from turtle import Turtle, Screen, textinput
import random

screen = Screen()
screen.setup(width=500, height=400)

bet = textinput(title="Make your bet!", prompt="Which colour will win the race?")

colours = ["red", "blue", "yellow", "green", "purple", "pink"]

turtles = []
for i in range(len(colours)):

    t = Turtle(shape="turtle")
    t.color(colours[i])

    t.penup()
    t.goto(x=-230, y=-100 + (40*i))

    turtles.append(t)

if bet:
    race_is_on = True

while race_is_on:

    for turtle in turtles:

        if turtle.xcor() > 230:

            is_race_on = False
            winner = turtle.pencolor()

            if bet == winner:

                print(f"You won! {winner} has won the race!")

            else:

                print(f"You lost... {winner} won the race...")

            break

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()