from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def start():
    return render_template('index.html')