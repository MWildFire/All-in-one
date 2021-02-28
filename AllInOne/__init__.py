from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update(
        DEBUG=True,
        # Настроки почты
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USERNAME='all.in.one.progect@gmail.com',
        MAIL_PASSWORD='4hw-iDQ-7fY-4C8',
        MAIL_USE_SSL=True
    )
    mail.init_app(app)
    db.init_app(app)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)


    return app
