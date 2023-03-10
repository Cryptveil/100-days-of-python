import time
import tkinter as tk

# Read words from file
def get_words():
    with open('words.txt') as f:
        words = f.read().split()
    return words

# Update the WPM counter
def update_wpm():
    global start_time
    # Calculate time taken and words per minute
    end_time = time.time()
    time_taken = end_time - start_time
    wpm = len(entry.get()) / 5 / (time_taken / 60)

    # Display the WPM counter
    wpm_label.config(text=f"WPM: {round(wpm)}")

    # Schedule the next update
    root.after(100, update_wpm)

# Start the test
def start_test():
    global start_time
    # Hide start button and show text entry
    start_button.pack_forget()
    entry.pack()

    # Enable text entry and set focus
    entry.config(state=tk.NORMAL)
    entry.delete(0, tk.END)
    entry.focus()

    # Start the timer and the WPM counter update loop
    start_time = time.time()
    update_wpm()

# Calculate WPM and accuracy
def end_test():
    global start_time
    # Disable text entry
    entry.config(state=tk.DISABLED)

    # Stop the WPM counter update loop
    wpm_label.after_cancel(update_wpm)

    # Calculate time taken and words per minute
    end_time = time.time()
    time_taken = end_time - start_time
    wpm = len(entry.get()) / 5 / (time_taken / 60)

    # Calculate accuracy
    words_typed = entry.get().split()
    correct_words = [word for word in words_typed if word in words]
    accuracy = len(correct_words) / len(words_typed)

    # Display results
    result_label.config(text=f"WPM: {round(wpm)}\nAccuracy: {round(accuracy*100)}%")
    result_label.pack()

# Create the main window
root = tk.Tk()
root.title("Typing Test")

# Create the widgets
words = get_words()
text_label = tk.Label(root, text=" ".join(words), font=("Arial", 12))
start_button = tk.Button(root, text="Start", font=("Arial", 12), command=start_test)
entry = tk.Entry(root, font=("Arial", 12), state=tk.DISABLED)
wpm_label = tk.Label(root, text="WPM: 0", font=("Arial", 12))
result_label = tk.Label(root, font=("Arial", 12))

# Pack the widgets
text_label.pack()
start_button.pack()
entry.pack()
wpm_label.pack()
result_label.pack()

# Start the event loop
root.mainloop()
