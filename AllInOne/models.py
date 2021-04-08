from . import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    is_auth = db.Column(db.Boolean())
    messages = db.relationship('messages', backref='user', lazy=True)
    profile = db.relationship('profile', backref='user', lazy=True)
    

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


class Message:

    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    recepient_id = db.Column(db.Integer())
    text =  db.Column(db.String())

    def __init__(self, recepient_id, text):
        self.text = text
        self.recepient_id = recepient_id


class Profile:

    __tablename__ = 'profile'

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    gender = db.Column(db.String(50))
    city = db.Column(db.String(100))
    age = db.Column(db.Integer())

    def __init__(self, gender, city, age):
        self.city = city
        self.gender = gender
        self.age = age
        