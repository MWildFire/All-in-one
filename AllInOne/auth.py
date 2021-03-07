from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User
from flask_login import login_user

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
    return redirect('/')


@auth.route('/reg', methods=['GET'])
def reg():
    return render_template('register.html')


@auth.route('/reg', methods=['POST'])
def reg_handler():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    repeat_password = request.form.get("repeat_password")
    new_user = User(email=email,
                    username=username,
                    password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/login')
