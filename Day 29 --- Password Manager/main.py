from tkinter import *
from tkinter import messagebox
import random, pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    lets = [random.choice(letters) for i in range(random.randint(8, 10))]
    nums = [random.choice(numbers) for j in range(random.randint(2, 4))]
    syms = [random.choice(symbols) for k in range(random.randint(2, 4))]

    password_list = lets + nums + syms
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():

    website_data = website_entry.get()
    user_data = user_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(user_data) == 0 or len(password_data) == 0:

        messagebox.showinfo(title="Error", message="Do not leave any fields empty!")
        return

    is_ok = messagebox.askyesno(title="Warning!", message=f"Are you sure you want to save this data? \n Website: {website_data} \n Email/Username: {user_data} \n Password: {password_data}")

    if is_ok:

        with open("entries.txt", "a") as file:

            file.write(f"{website_data} | {user_data} | {password_data}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=55, pady=55)

canvas = Canvas(width=200, height=200)
bg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)


# Labels
website_text    = Label(text="Website:")
user_text       = Label(text="Email/Username:")
password_text   = Label(text="Password:")

website_text.grid(row=1, column=0)
user_text.grid(row=2, column=0)
password_text.grid(row=3, column=0)


# Entries
website_entry   = Entry(width=50)
user_entry      = Entry(width=50)
password_entry  = Entry(width=32)

website_entry.grid(row=1, column=1, columnspan=2)
user_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

website_entry.focus()
user_entry.insert(END, "csbroman10@gmail.com")


# Buttons
password_button = Button(text="Generate Password", command=generate_password)
add_button      = Button(width=43, text="Add", command=save_entry)

password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()