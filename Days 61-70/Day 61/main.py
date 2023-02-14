from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask import Flask, render_template


class Login(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password",
                             validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "1234"
FAKE_ADMIN_EMAIL = "admin@email.com"
FAKE_ADMIN_PASSWORD = "12345678"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = Login()
    if login_form.validate_on_submit():
        if login_form.email.data == FAKE_ADMIN_EMAIL and \
                login_form.password.data == FAKE_ADMIN_PASSWORD:
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
