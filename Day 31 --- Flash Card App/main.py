# -------------------------- IMPORTS -------------------------- #
from tkinter import *
import pandas
import random
# -------------------------- CONSTANTS -------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# -------------------------- WORD HANDLING -------------------------- #
data_dict = {}
try:

    data = pandas.read_csv("./data/to_learn.csv")

except:

    original = pandas.read_csv("./data/french_words.csv")
    data_dict = original.to_dict(orient="records")

else:

    data_dict = data.to_dict(orient="records")

def next_card():

    global current_card, flip_timer
    current_card = random.choice(data_dict)
    window.after_cancel(flip_timer)

    canvas.itemconfig(bg, image=background1)
    canvas.itemconfig(title, text="French", fill="black")
    french_word = current_card["French"].title()
    canvas.itemconfig(word, text=french_word, fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():

    global current_card
    canvas.itemconfig(bg, image=background2)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():

    global current_card
    data_dict.remove(current_card)

    learned = pandas.DataFrame(data_dict)
    learned.to_csv("./data/to_learn.csv", index=False)

    next_card()


# -------------------------- UI SETUP -------------------------- #
window = Tk()
window.title("Flashy!")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas      = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background1  = PhotoImage(file="./images/card_front.png")
background2  = PhotoImage(file="./images/card_back.png")

bg = canvas.create_image(401, 263, image=background1)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

grade_button = Button(text="Grade!", bg=BACKGROUND_COLOR, font=("Arial", 25, "italic"))
grade_button.grid(row=2, column=0, columnspan=2)

next_card()

window.mainloop()
