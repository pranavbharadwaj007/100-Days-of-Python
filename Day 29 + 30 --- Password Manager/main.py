from tkinter import *
from tkinter import messagebox
import random, pyperclip, json
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():

    try:

        data = json.load(open("entries.json", "r"))

    except FileNotFoundError:

        messagebox.showinfo(title="Error!", message="Entry not found in data!")

    else:

        website = website_entry.get()
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title="Account Found!", message=f"Email: {email} \n Password: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    lets = [random.choice(letters) for _ in range(random.randint(8, 10))]
    nums = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    syms = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = lets + nums + syms
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():

    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:

        messagebox.showinfo(title="Error", message="Do not leave any fields empty!")
        return

    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }

    try:

        with open("entries.json", "r") as file:

            data = json.load(file)
            data.update(new_data)

        with open("entries.json", "w") as file:

            json.dump(data, file, indent=4)

    except FileNotFoundError:

        with open("entries.json", "w") as file:

            json.dump(new_data, file, indent=4)

    finally:

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
website_entry   = Entry(width=32)
user_entry      = Entry(width=50)
password_entry  = Entry(width=32)

website_entry.grid(row=1, column=1)
user_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

website_entry.focus()
user_entry.insert(END, "csbroman10@gmail.com")


# Buttons
search_button   = Button(width=14, text="Search", command=search)
password_button = Button(width=14, text="Generate", command=generate_password)
add_button      = Button(width=43, text="Add", command=save_entry)

search_button.grid(row=1, column=2)
password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()