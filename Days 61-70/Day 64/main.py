from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap5(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500))
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False, unique=True)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(1000), nullable=False, unique=True)

    def __repr__(self):
        return f"<Movie {self.title}>"


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movie_list=all_movies)


@app.route("/edit/<movie_id>")
def edit(movie_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
