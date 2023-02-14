from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, render_template


class Login(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")


app = Flask(__name__)
app.secret_key = "1234"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    login_form = Login()
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
