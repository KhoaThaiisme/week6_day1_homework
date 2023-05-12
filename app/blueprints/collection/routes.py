from flask import render_template, flash, redirect, url_for

from app.models import Car
from flask_login import current_user, login_required
from . import bp

from app.models import Car, User
from app.forms import CarForm

@bp.route('/car', methods=['GET', 'POST'])
@login_required
def car():
    form=CarForm()
    if form.validate_on_submit():
        c = Car(brand=form.brand.data, model=form.model.data, year=form.year.data, description=form.description.data)
        c.user_id = current_user.user_id
        c.commit()
        flash(f'Car has registered to {c.author}')
        return redirect(url_for('collection.user_page', username=current_user.username))
    return render_template('inventory.j2', form=form)

@bp.route('/username/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    return render_template('user_page.j2', title=username, user=user)