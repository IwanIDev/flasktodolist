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

    return flask.render_template("todos.html", todo=todo.title)
