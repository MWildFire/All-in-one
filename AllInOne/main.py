from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db, mail
from flask_mail import Mail, Message


main = Blueprint('main', __name__)


@main.route('/')
def start():
    return render_template('start.html')


@main.route('/base')
def base():
    return render_template("base.html")


@main.route('/send_mail')
def send():
    try:
        msg = Message("Send Mail Test", sender=("ALL IN ONE", 'all.in.one.progect@gmail.com'), recipients=["pda1205@yandex.ru", "mvstrike17@gmail.com"])
        msg.body = "Привет, мы тестирум автоматескую отправку сообщений"
        mail.send(msg)
        return 'Сообщение отправлено'
    except Exception as e:
        return str(e)
