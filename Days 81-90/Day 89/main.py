import tkinter as tk
import time


def on_keypress(event):
    global text, last_type_time
    text = textbox.get("1.0", tk.END)
    last_type_time = time.time()


def check_text():
    global text, last_type_time
    if last_type_time and time.time() - last_type_time > 5:
        textbox.delete("1.0", tk.END)
    root.after(check_interval, check_text)


root = tk.Tk()
root.title("Text Entry App")
root.geometry("400x300")

textbox = tk.Text(root, font=("Arial", 14))
textbox.pack(fill=tk.BOTH, expand=True)

text = ""
last_type_time = None
check_interval = 5000  # 5 seconds

textbox.bind("<Key>", on_keypress)
root.after(check_interval, check_text)

root.mainloop()
