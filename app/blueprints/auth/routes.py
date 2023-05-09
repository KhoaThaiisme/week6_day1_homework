from flask import render_template

from . import bp 

@bp.route('/register')
def register():
    return render_template('register.j2')

@bp.route('/signin')
def signin():
    return render_template('signin.j2')