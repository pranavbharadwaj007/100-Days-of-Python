from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK            = "#e2979c"
RED             = "#e7305b"
GREEN           = "#9bdeac"
YELLOW          = "#f7f5dd"
FONT_NAME       = "Courier"
WORK_MIN        = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN  = 20
reps            = 0
timer           = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    global reps
    reps = 0

    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="0:00")

    title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global reps
    reps += 1

    work_sec        = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec  = LONG_BREAK_MIN * 60

    if reps % 8 == 0:

        countdown(long_break_sec, "Break", RED)

    elif reps % 2 == 0:

        countdown(short_break_sec, "Break", PINK)

    else:

        countdown(work_sec, "WORK", GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count, phrase, color):

    mins    = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    title.config(text=phrase, fg=color)
    canvas.itemconfig(timer_text, text=f"{mins}:{seconds}")

    if count > 0:

        global timer
        timer = window.after(1000, countdown, count-1, phrase, color)

    else:

        start_timer()

        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=600, height=433)
window.maxsize(width=600, height=433)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background)
timer_text = canvas.create_text(100, 132, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title       = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

start       = Button(text="Start", bg=PINK, font=(FONT_NAME, 16, "bold"), command=start_timer)
start.grid(column=0, row=2)

reset       = Button(text="Reset", bg=PINK, font=(FONT_NAME, 16, "bold"), command=reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()