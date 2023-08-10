from app import db


class Todo(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
