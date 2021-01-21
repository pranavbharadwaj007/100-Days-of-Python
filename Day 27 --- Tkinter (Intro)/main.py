from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

kilo_result = Label()
kilo_result.grid(column=1, row=1)

kilo_text = Label(text="Km")
kilo_text.grid(column=2, row=1)

def convert():

    kilos = int(miles_entry.get()) * 1.609
    kilo_result.config(text=kilos)


calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()