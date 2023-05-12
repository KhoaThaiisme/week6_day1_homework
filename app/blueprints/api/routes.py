from flask import request, jsonify

from . import bp
from app.models import Car, User

# Receive all cars
@bp.get('/post')
def api_cars():
    result = []
    cars = Car.query.all()
    for car in cars:
        result.append(
            {
            'id': car.id,
            'brand': car.brand,
            'model': car.model,
            'year': car.year,
            'description': car.description,
            'author': car.user_id
            }
        )
    return jsonify(result), 200

# Receive Cars from single user
@bp.get('/post/<username>')
def user_cars(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify([{
            'id': car.id,
            'brand': car.brand,
            'model': car.model,
            'year': car.year,
            'description': car.description
        }for car in user.cars]), 200
    return jsonify([{'message':'Invalid Username'}]), 404

# Send single car to the api database
@bp.get('/post/<id>')
def get_car(id):
    try:
        car = Car.query.get(id)
        return jsonify([{
            'id': car.id,
            'brand': car.brand,
            'model': car.models,
            'year': car.year,
            'description': car.description,
            'author': car.user_id

        }])
    except:
        return jsonify([{'message':'Invalid Post Id'}]), 404                                                                                                                                                      