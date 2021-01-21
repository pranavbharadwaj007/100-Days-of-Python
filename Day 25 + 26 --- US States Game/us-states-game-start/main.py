import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")

data        = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()

guessed_states = []
while len(guessed_states) < len(state_names):

    guess = turtle.textinput(title=f"{len(guessed_states)}/50 states guessed",
                             prompt="What's another state's name?").title()

    if guess in state_names:

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)

        guessed_states.append(guess)

    else:

        remaining_states = [state for state in state_names if state not in guessed_states]
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break

turtle.mainloop()

