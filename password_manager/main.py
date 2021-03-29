from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Commands
def clean_entries():
    entry_website.delete(0, "end")
    entry_password.delete(0, "end")


def write_to_file(site, username, pw):
    json_data = {site: {
        "username": username,
        "password": pw
    }}
    try:
        with open("data.json", "r") as data:
            current_data = json.load(data)
    except FileNotFoundError:
        with open("data.json", "w") as new_file:
            json.dump(json_data, new_file, indent=4)
    else:
        current_data.update(json_data)
        with open("data.json", "w") as old_data:
            json.dump(current_data, old_data, indent=4)

    messagebox.showinfo(title="Save", message="Operation Successful!")
    clean_entries()

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for i in range(random.randint(8, 10))]

    password_list += [random.choice(symbols) for i in range(random.randint(2, 4))]

    password_list += [random.choice(numbers) for i in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0,"end")
    entry_password.insert(0,password)
    pyperclip.copy(password)


def save_info_to_file():
    website = entry_website.get().title()
    email_username = entry_email_username.get().title()
    password = entry_password.get().title()

    if len(website) <= 0 or len(email_username) <= 0 or len(password) <= 0:
        messagebox.showerror(title="Error", message="All fields must be filled out")
    else:
        ok_to_proceed = messagebox.askokcancel(title=website,
                                               message=f"Username: {email_username} \n"
                                                       f"Password: {password} \n"
                                                       "Ok to Save?")
        if ok_to_proceed:
            write_to_file(website, email_username, password)


def search():
    website = entry_website.get().title()
    if len(website) <= 0:
        messagebox.showerror(title="Error", message="Website must be filled out")
    else:
        try:
            with open("data.json", "r") as data:
                current_data = json.load(data)

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found")
        else:
            if website in current_data:
                username = current_data[website]["username"]
                password = current_data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {username} \n Password: {password}")
            else:
                messagebox.showerror(title="Error", message="Website not found")


# CANVAS
canvas = Canvas(height=200, width=200)
background_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_img)
canvas.grid(row=0, column=1)

# LABELS
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)

label_password = Label(text="Password")
label_password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, sticky="e")
entry_website.focus()

entry_email_username = Entry(width=35)
entry_email_username.grid(row=2, column=1, columnspan=2, sticky="w")
entry_email_username.insert(0, "test@gmail.com")

entry_password = Entry(width=35)
entry_password.grid(row=3, column=1, sticky="w")

# BUTTON Search
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="w")

# BUTTON GENERATE PASSWORD
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="e")

# BUTTON ADD
add_button = Button(text="ADD", width=30, command=save_info_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
