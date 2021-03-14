from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, mail
from .models import User
from flask_login import login_user
from string import punctuation
from flask_mail import Message

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_handler():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or password != user.password:
        return redirect('/login')

    user.is_auth = True
    login_user(user)
    return redirect('/')


@auth.route('/reg', methods=['GET'])
def reg():
    return render_template('register.html')


@auth.route('/reg', methods=['POST'])
def reg_handler():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    repeat_password = request.form.get("repeat-password")
    if password == repeat_password:
        if set('@').isdisjoint(set(password)):
            return 'Пароль не содержит специальных симоволов'
        else:
            new_user = User(email=email,
                            username=username,
                            password=password)
            db.session.add(new_user)
            db.session.commit()
            response = send(email)
            return render_template('email_confirmation.html', response=response)
    else:
        return 'Пароли не свопадают'


def send(email):
    try:
        msg = Message("Send Mail Test", sender=("ALL IN ONE", 'all.in.one.progect@gmail.com'),
                      recipients=[email])
        msg.body = "Подтверждение регистрации"
        mail.send(msg)
        return 'На ваш email было отправлено письмо с подтверждением'
    except Exception as e:
        return f'Не удалось отпрваить письмо с подтверждением на ваш email. Ошибка: {str(e)}'
