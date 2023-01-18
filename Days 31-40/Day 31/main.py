import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flash Card Program")
window.config(padx=50, pady=50)

correct_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

correct_button = tk.Button(image=correct_image, highlightthickness=0)
correct_button.grid(column=1, row=1)

wrong_button = tk.Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
