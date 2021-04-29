from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db, mail
from flask_mail import Mail, Message


main = Blueprint('main', __name__)


@main.route('/')
def start():
    return render_template('start.html')


@main.route('/change_password', methods=['GET'])
def change_pass():
    return render_template('change_pass.html')


@main.route('/change_password', methods=['POST'])
def change_pass_hanlder():
    return 'Здесь будет обработка смены пароля у пользователя'


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


@main.route('/profile')
def profile():
    return render_template("profile.html")


@main.route('/chats')
def chats():
    return render_template("chats.html")

# https://www.youtube.com/embed/vNSDPfeMcB0
# https://youtu.be/vNSDPfeMcB0
@main.route('/yt_watch', methods=['GET', 'POST'])
def yt_watch():
    if request.method == 'GET':
        return render_template('yt_form.html')
    else:
        link = 'https://www.youtube.com/embed/' + request.form.get('link').split('/')[-1]
        return render_template('yt_watch.html', link=link)


@main.route('/chat')
def chat():
    return render_template("chat.html")


