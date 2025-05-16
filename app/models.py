from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="user", lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date)
    priority = db.Column(db.String(10))  # e.g., "Low", "Medium", "High"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
