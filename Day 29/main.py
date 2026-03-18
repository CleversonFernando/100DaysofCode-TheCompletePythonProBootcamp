import json
import random
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generating_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if website == "" or password == "" or username == "":
        messagebox.showwarning(title="Error", message="Please fill all fields")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        except JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No details for the website exists.")
        return

    except JSONDecodeError:
        messagebox.showwarning(title="Error", message="No details for the website exists.")
        return

    try:
        data = data[website]
        messagebox.showinfo(title=f"{website}",
                            message=f"Email: {data['email']}\n Password: {data['password']}")

    except KeyError:
        messagebox.showwarning(title="Error", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Configure image
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Label 1
website_label = Label(text="Website:", font=("Times New Roman", 10))
website_label.grid(row=1, column=0, sticky=W)

# Label 2
username_label = Label(text="Email/Username:", font=("Times New Roman", 10))
username_label.grid(row=2, column=0, sticky=W)

# Label 3
password_label = Label(text="password:", font=("Times New Roman", 10))
password_label.grid(row=3, column=0, sticky=W)

# Entry 1
website_entry = Entry(width=21, font=("Times New Roman", 10))
website_entry.grid(row=1, column=1, sticky=EW)
website_entry.focus()

# Entry 2
username_entry = Entry(font=("Times New Roman", 10))
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
username_entry.insert(0, "cleverson.email.com")

# Entry 3
password_entry = Entry(width=21, font=("Times New Roman", 10))
password_entry.grid(row=3, column=1, sticky=EW)

# Button 1
generate_password = Button(text="Generate Password", font=("Times New Roman", 10), command=generating_password)
generate_password.grid(row=3, column=2, sticky=EW)

# Button 2
add = Button(text="Add", font=("Times New Roman", 10), command=save)
add.grid(row=4, column=1, columnspan=2, sticky=EW)

# Button 3
find_password = Button(text="Search", font=("Times New Roman", 10), command=find_password)
find_password.grid(row=1, column=2, sticky=EW)

window.mainloop()
