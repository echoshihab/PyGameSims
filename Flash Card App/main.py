from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

csv = pd.read_csv("data/french_words.csv")
main_list = csv.to_dict(orient='records')

def get_next_card():
    random_french = random.choice(main_list)['French']
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=random_french)

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# CANVAS



canvas = Canvas(width=800, height=526)
foreground_img = PhotoImage(file="images/card_front.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=foreground_img)
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
