from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)

def clicked():
    text = input.get()
    label.config(text=text)


# Label
label = Label(text="Tá mé label")
label["text"] = "new_text"
label.config(text="new_text")
label.grid(column=0, row=0)

button = Button(text="my guy", command=clicked)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3, row=2)

new_button = Button()
new_button.grid(column=0, row=2)

window.mainloop()