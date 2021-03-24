from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7405b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def count_down(count):
    seconds_left = f'0{count % 60}' if count % 60 > 59 or \
                                       count % 60 == 0 or \
                                       count % 60 < 10 else count % 60
    canvas.itemconfig(timer_text, text=f"{count // 60}:{seconds_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0:
            current_text = label_checkmark.cget("text")
            current_text += "✔"
            label_checkmark.config(text=current_text)


def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        label_timer.config(text="Focus on Work")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long Break!", fg=RED)
    else:
        count_down(short_break_sec)
        label_timer.config(text="Short Break!", fg=YELLOW)


def reset():

    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_checkmark.config(text="")
    reps = 0


window = Tk()
window.title("Pomodoro App")
window.config(padx=10, pady=10, bg=RED)

# CANVAS
canvas = Canvas(width=244, height=274)
background_img = PhotoImage(file="tomoto.png")
canvas.create_image(122, 137, image=background_img)
timer_text = canvas.create_text(116, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# LABEL TIMER
label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30), bg=RED)
label_timer.grid(row=0, column=1)

# LABEL CHECKMARK
label_checkmark = Label(text="", fg=GREEN, font=(FONT_NAME, 30), bg=RED)
label_checkmark.grid(row=3, column=1)

# BUTTON RESET
button = Button(text="start", command=start)
button.grid(row=2, column=0)

# BUTTON RESET
button = Button(text="reset", command=reset)
button.grid(row=2, column=2)

window.mainloop()
