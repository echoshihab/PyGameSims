from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

csv = pd.read_csv("data/french_words.csv")
main_list = csv.to_dict(orient='records')
current_card = {}


def get_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(main_list)
    random_french = current_card["French"]
    canvas.itemconfig(foreground, image=foreground_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_french, fill="black")
    flip_timer= window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(foreground, image=background_img)
    random_english = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_english, fill="white")


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# CANVAS



canvas = Canvas(width=800, height=526)
foreground_img = PhotoImage(file="images/card_front.png")
background_img = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
foreground = canvas.create_image(400, 263, image=foreground_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=get_next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=get_next_card)
known_button.grid(row=1, column=1)

canvas.grid(row=0, column=0)

get_next_card()

window.mainloop()
