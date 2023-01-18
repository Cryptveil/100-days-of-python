import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

data = pd.read_csv("data/french_words.csv")
word_dict = pd.DataFrame.to_dict(data, orient="records")
new_word = random.choice(word_dict)
french_word = new_word["French"]


def next_card():
    new_word = random.choice(word_dict)
    french_word = new_word["French"]
    canvas.itemconfig(word, text=french_word)


window = tk.Tk()
window.title("Flash Card Program")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

correct_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="French", font=FONT_LANGUAGE)
word = canvas.create_text(400, 263, text=french_word,
                          font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

correct_button = tk.Button(image=correct_image, highlightthickness=0,
                           command=next_card)
correct_button.grid(column=1, row=1)

wrong_button = tk.Button(image=wrong_image, highlightthickness=0,
                         command=next_card)
wrong_button.grid(column=0, row=1)

window.mainloop()
