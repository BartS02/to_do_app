from flask import Flask, Blueprint, render_template, request, redirect, url_for
from .models import Todo
from . import db

my_view = Blueprint("my_view", __name__)
@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    print(todo_list)
    message = request.args.get('message', None)
    return render_template("index.html", todo_list = todo_list, message = message)

#!This allows a user to do a post request and defines the finctions such as new tasks,catogories etc
@my_view.route("/add", methods=["POST"])
def add():
    try: 
        task = request.form.get("task")
        categories = request.form.get("categories")
        new_todo = Todo(task=task,categories=categories)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("my_view.home"))
    except:
        message = "There was an error adding your task. Please try again"
        return redirect(url_for("my_view.home", message=message))
#!This allows users to update such tasks by marking them as complete
@my_view.route("/update/<todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("my_view.home"))

#!This allows the tasks to be deleted
@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home"))