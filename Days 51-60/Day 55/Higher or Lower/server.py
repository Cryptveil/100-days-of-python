from flask import Flask
import random

app = Flask(__name__)
GENERATED_NUMBER = random.randint(0, 9)
WELCOME_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH_GIF = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW_GIF = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT_GIF = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"


@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
            f"<img src='{WELCOME_GIF}'>"


@app.route("/<int:guess>")
def checks_guess(guess):
    if guess == GENERATED_NUMBER:
        return "<h1 style='color: green'>You found me!</h1>" \
                f"<img src='{CORRECT_GIF}'>"
    elif guess > GENERATED_NUMBER:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
                f"<img src='{HIGH_GIF}'>"
    elif guess < GENERATED_NUMBER:
        return "<h1 style='color: blue'>Too low, try again!</h1>" \
                f"<img src='{LOW_GIF}'>"


if __name__ == "__main__":
    app.run(debug=True)
