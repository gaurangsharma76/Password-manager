from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    email_entered = email_input.get()
    password_entered = password_input.get()
    website_entered = website_input.get()
    if (email_entered == "") or (password_entered == "") or (website_entered == ""):
        messagebox.showwarning(title="Missing fields", message="Please enter all fields")
    else:
        with open("data.txt", "a") as password_file:
            password_file.write(
                f"website:{website_entered}| EmailID/Username:{email_entered}| password:{password_entered}\n")
        password_input.delete(0, END)
        website_input.delete(0, END)
        email_input.delete(0, END)
        messagebox.showinfo(title="Success", message="Details saved successfully")
        website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=17)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=gen_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, width=35, command=add_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
