from tkinter import *
from tkinter import messagebox
import random
import pyperclip



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Commands
def clean_entries():
    entry_website.delete(0, "end")
    entry_password.delete(0, "end")


def write_to_file(site, username, pw):
    with open("data.txt", "a") as data:
        data.write(f'{site} | {username} | {pw} \n')
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
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()

    if len(website) <= 0 or len(email_username) <= 0 or len(password) <= 0:
        messagebox.showerror(title="Error", message="All fields must be filled out")
    else:
        ok_to_proceed = messagebox.askokcancel(title=website,
                                               message=f"Username: {email_username} \n"
                                                       f"Password: {password} \n"
                                                       "Ok to Save?")
        if ok_to_proceed:
            write_to_file(website, email_username, password)



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
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email_username = Entry(width=35)
entry_email_username.grid(row=2, column=1, columnspan=2)
entry_email_username.insert(0, "test@gmail.com")

entry_password = Entry(width=25)
entry_password.grid(row=3, column=1, sticky="e")

# BUTTON GENERATE PASSWORD
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

# BUTTON ADD
add_button = Button(text="ADD", width=30, command=save_info_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
