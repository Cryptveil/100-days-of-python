import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_text = tk.Label(
                text="Score: 0",
                bg=THEME_COLOR,
                fg="white"
                )
        self.score_text.grid(column=1, row=0)
        correct_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(
                image=correct_image,
                highlightthickness=0,
                )
        self.true_button.grid(column=0, row=2)
        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(
                image=false_image,
                highlightthickness=0,
                )
        self.false_button.grid(column=1, row=2)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
                150,
                125,
                width=280,
                text="Placeholder text",
                fill=THEME_COLOR,
                font=("Arial", 20, "italic")
                )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
