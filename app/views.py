import flask

from app import app
from app import db
from app.models import Todo


@app.route("/submit", methods=["POST"])
def submit():
    todo = Todo()
    todoname = flask.request.form["todo"]
    todo.title = todoname
    db.session.add(todo)
    db.session.commit()

    return flask.render_template("todos.html", todoName=todo.title, todoId=todo.id)


@app.route("/delete/<int:todoid>", methods=["DELETE"])
def delete_todo(todoid):
    todo = Todo.query.get(todoid)
    db.session.delete(todo)
    db.session.commit()

    return ""
