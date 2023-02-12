from flask import Flask, render_template
import requests

app = Flask(__name__)
POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route("/")
def home():
    response = requests.get(POSTS_URL).json()
    return render_template("index.html",
                           posts=response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
