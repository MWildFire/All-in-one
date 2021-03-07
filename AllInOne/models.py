from . import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    is_auth = db.Column(db.Boolean())

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

