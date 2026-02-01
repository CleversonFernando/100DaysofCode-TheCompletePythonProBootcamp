from tkinter import *



def button_clicked():
    my_label["text"] = input_field.get()

#window
window = Tk()
window.title("My first GUI")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

#label
my_label = Label(text="My first label", font=("Arial", 25))
my_label.grid(column=0, row=0)
my_label["text"] = "My first label"
my_label.config(padx=20, pady=20)

#button
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=20, pady=20)

#entry
input_field = Entry(width=40)
input_field.grid(column=4, row=3)

#new button
button2 = Button(text="New button", command=button_clicked)
button2.grid(column=3, row=0)

window.mainloop()
