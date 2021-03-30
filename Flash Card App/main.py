from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# CANVAS

canvas = Canvas(width=800, height=526)
foreground_img = PhotoImage(file="images/card_front.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=foreground_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image= PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

# timer_text = canvas.create_text(116, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=0, column=0)


#image


window.mainloop()
