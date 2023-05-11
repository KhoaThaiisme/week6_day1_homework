from flask import render_template, flash, redirect, url_for

from app.models import Car
from flask_login import current_user
from . import bp

from app.models import Car
from app.forms import CarForm

@bp.route('/car', methods=['GET', 'POST'])
def car():
    form=CarForm()
    if form.validate_on_submit():
        c = Car(brand=form.brand.data, model=form.model.data, year=form.year.data)
        c.user_id = current_user.user_id
        c.commit()
        print(f'{c.author= }{c.author.cars[0]}')
    return render_template('inventory.j2', form=form)