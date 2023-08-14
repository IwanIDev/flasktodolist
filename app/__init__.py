import flask
from flask_sqlalchemy import SQLAlchemy
from dataclasses import asdict

app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///database.db'
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()

db.init_app(app)

from app import views
from app import models

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    todos = db.session.query(models.Todo).all()
    return flask.render_template("home.html", todos=todos)
