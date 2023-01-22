import tkinter as tk
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.window.mainloop()
