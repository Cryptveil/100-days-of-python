from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED,
                           font=(FONT_NAME, 35, "bold"),
                           highlightthickness=0, bg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK,
                           font=(FONT_NAME, 35, "bold"),
                           highlightthickness=0, bg=YELLOW)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=PINK,
                           font=(FONT_NAME, 35, "bold"),
                           highlightthickness=0, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Background and tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label
title_label = Label(text="Timer", fg=GREEN,
                             font=(FONT_NAME, 35, "bold"),
                             highlightthickness=0, bg=YELLOW)
title_label.grid(column=1, row=0)

# Start button
button = Button(text="Start", command=start_timer)
button.grid(column=0, row=2)

# Reset button
button = Button(text="Reset")
button.grid(column=2, row=2)

# Checkmark label
label = Label(text="✔", fg=GREEN, font=(FONT_NAME, 25, "bold"), highlightthickness=0, bg=YELLOW)
label.grid(column=1, row=3)


window.mainloop()

