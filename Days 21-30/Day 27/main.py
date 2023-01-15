from tkinter import *

window = Tk()
window.title("Mile to Km Converter")


def convert_miles_to_km():
    result = int(entry.get()) * 1.61
    number_km.configure(text=result)


entry = Entry(width=10)
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

number_km = Label(text="0")
number_km.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
