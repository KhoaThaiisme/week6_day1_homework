from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    user_id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, unique=True)
    email=db.Column(db.String, unique=True)
    password=db.Column(db.String)
    cars=db.relationship('Car', backref='author', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return str(self.user_id)

class Car(db.Model):
    car_id=db.Column(db.Integer, primary_key=True)
    brand=db.Column(db.String(50))
    model=db.Column(db.String(50))
    year=db.Column(db.Integer)
    description=db.Column(db.String(200))
    user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        return f'Car: {self.brand}'

    def commit(self):
        db.session.add(self)
        db.session.commit()