from flask import render_template, flash, redirect, url_for
from flask_login import login_user
from app.models import User

from . import bp 
from app.forms import RegisterForm, SigninForm

@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data,email=form.username.data,password=form.password.data)
            u.password = u.hash_password(form.password.data)
            u.commit()
            flash(f'{form.username.data} has been registered', 'success')
            return redirect(url_for("main.home"))
        if user:
            flash(f'{form.username.data} already taken, try again')
        else:
            flash(f'{form.email.data} already taken, try again')
    return render_template('register.j2', form=form)

    # if form.validate_on_submit():
    #     username = form.username.data
    #     user = User.query.filter_by(username=username).first()
    #     email = User.query.filter_by(email=form.email.data).first()
    #     if not email and not user:
    #         u = User(username=username, email=form.email.data,password=form.password.data)
    #         u.commit()
    #         flash(f'{username} registered')
    #         return redirect(url_for("main.home"))
    #     if user:
    #         flash(f'{username} already taken, try again!')
    #     elif email:
    #         flash(f'{form.email.data} has already taken, try again!')

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form=SigninForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash(f'{form.username.data} signed in!', 'success')
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash(f'{form.username.data} doesn\'t exist, or password is incorrect, please try again')
    return render_template('signin.j2', form=form)