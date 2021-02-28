from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from flask_login import login_user

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/reg')
def reg():
    return render_template('register.html')

