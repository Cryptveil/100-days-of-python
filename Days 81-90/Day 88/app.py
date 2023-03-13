from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class TaskList(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    date_of_creation = db.Column(db.String(250), nullable=False)
    due_date = db.Column(db.String(250), nullable=False)


class CreateNewTask(FlaskForm):
    task = StringField("Type your task here", validators=[DataRequired()])
    due_date = StringField("Due date", validators=[DataRequired()])
    submit = SubmitField("New Task")


@app.route("/")
def home():
    all_tasks = TaskList.query.all()
    return render_template("index.html", tasks=all_tasks)


@app.route("/create", methods=["GET", "POST"])
def make_task():
    form = CreateNewTask()
    if request.method == "POST":
        creation = datetime.now().strftime("%B %d, %Y")
        new_task = TaskList(
                description=request.form.get("description"),
                date_of_creation=creation,
                due_date=request.form.get("date")
                )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("create_task.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
