from datetime import timedelta

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, abort
)
from flask_login import login_user, logout_user, login_required

from app.database import db
from app.domain import is_safe_url
from app.domain.auth.repositories.user_repository import UserRepository


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                user_repo = UserRepository()
                user_repo.register_user(username, password)
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username: str = request.form.get('username', type=str)
        password: str = request.form.get('password', type=str)
        remember_me: bool = request.form.get('remember_me', type=bool)

        error = None

        user_repo = UserRepository()
        user = user_repo.login_user(username, password)

        if user is None:
            error = 'Incorrect credentials.'

        if error is None:

            login_user(user, remember=remember_me, duration=timedelta(days=1))

            next = request.args.get('next')

            if not is_safe_url(next):
                return abort(400)

            return redirect(next or url_for('blog.index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
