from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"
EMAIL = ""
PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
MSG = "Subject: Contact info\n\n"


@app.route("/")
def home():
    response = requests.get(POSTS_URL).json()
    return render_template("index.html",
                           posts=response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":  
        with smtplib.SMTP(SMTP_SERVER, port=PORT) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg=f"{MSG}Name: {request.form['name']}\n \
                        Email: {request.form['email']}\n \
                        Phone number: {request.form['phone']}\n \
                        Message: {request.form['message']}"
                                )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:blog_id>")
def post(blog_id):
    response = requests.get(POSTS_URL).json()[blog_id-1]
    return render_template("post.html", post=response)


if __name__ == "__main__":
    app.run(debug=True)
