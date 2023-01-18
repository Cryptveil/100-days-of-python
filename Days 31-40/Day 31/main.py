import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

data = pd.read_csv("data/french_words.csv")
french_dict = pd.DataFrame.to_dict(data, orient="records")
new_word = {}


def next_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(french_dict)
    french_word = new_word["French"]
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    flip_timer = window.after(3000, card_translation)


def card_translation():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=new_word["English"])


window = tk.Tk()
window.title("Flash Card Program")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, card_translation)

correct_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="", font=FONT_LANGUAGE)
word = canvas.create_text(400, 263, text="",
                          font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

correct_button = tk.Button(image=correct_image, highlightthickness=0,
                           command=next_card)
correct_button.grid(column=1, row=1)

wrong_button = tk.Button(image=wrong_image, highlightthickness=0,
                         command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
