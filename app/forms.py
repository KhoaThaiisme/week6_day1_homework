from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class CarForm(FlaskForm):
    brand =StringField('brand', validators=[DataRequired()])
    model=StringField('model', validators=[DataRequired()])
    year=StringField('year', validators=[DataRequired()])
    description=StringField('desc')
    submit = SubmitField('Collect')