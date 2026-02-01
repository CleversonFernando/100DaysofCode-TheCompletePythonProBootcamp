from tkinter import *


def convert():
    conversion_value = 1.60934
    miles = float(entry.get())
    km = miles * conversion_value
    output.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

# LABELS
# First label
first_label = Label(text="is equal to", font=("Arial", 20))
first_label.grid(column=0, row=1)

# Second label
second_label = Label(text="Miles", font=("Arial", 20))
second_label.grid(column=2, row=0)
second_label.config(padx=20, pady=20)

# Third label
third_label = Label(text="Km", font=("Arial", 20))
third_label.grid(column=2, row=1)
third_label.config(padx=20, pady=20)

# ENTRY
entry = Entry(width=10)
entry.grid(column=1, row=0)

# OUTPUT
output = Label(text="0", font=("Arial", 20))
output.grid(column=1, row=1)

# BUTTON
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()