from tkinter import *

def convert():
    miles = entry.get()
    km = float(miles) * 1.60934
    km_num_label.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=10, pady=10)

entry = Entry(width=10)
entry.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_num_label = Label(text="0")
km_num_label.grid(row=1, column=1)

km_text_label = Label(text="Km")
km_text_label.grid(row=1, column=2)


#button
button = Button(text="Calculate", command=convert)
button.grid(row=3, column=1)


window.mainloop()

