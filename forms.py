from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SignUpForm(FlaskForm):
    type = SelectField(choices=[('student', 'STUDENT'), ('tutor', 'TUTOR')])
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    gender = SelectField(choices=[('unkwon', ''), ('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')])
    submit = SubmitField('Next')

class CompleteSignUpForm(FlaskForm):#don't know if it is really neccesary using 3 forms
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)])
    password_con = PasswordField('Confirm', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Next')

class TutorSignUpForm(FlaskForm):#don't know if it is really neccesary using 3 forms
    degree = SelectField(choices=[('diploma', 'DIPLOMA'), ('bacheloer', 'BACHELOR'), ('master', 'MASTER')])
    submit = SubmitField('Next')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField('Login')

