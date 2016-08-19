from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_TRACK_MODIFICATIONS=True
))
db = SQLAlchemy(app)


class MyModel(db.Model):
    """Just a sample model."""
    __tablename__ = 'my_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
