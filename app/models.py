from app import db
from dataclasses import dataclass


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    def todict(self):
        return {
            'id': self.id,
            'title': self.title
        }
