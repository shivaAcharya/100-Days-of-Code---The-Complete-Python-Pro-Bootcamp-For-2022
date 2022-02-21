from tkinter import *

# Create a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=70, pady=70)

# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def button_click():
    miles = float(entry.get())
    kms = round(miles * 1.609, 2)
    result_label.config(text=kms)


# Button
button = Button(text="Calculate", command=button_click)
button.grid(row=2, column=1)

window.mainloop()
