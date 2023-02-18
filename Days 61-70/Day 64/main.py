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


class Movie(db.Model):  # type: ignore
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


class MovieForm(FlaskForm):
    rating = StringField("Your Rating", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movie_list=all_movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    form = MovieForm()
    if request.method == "POST":
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add")
def add():
    return render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)
