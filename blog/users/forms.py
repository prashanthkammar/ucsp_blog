from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from blog.models import User


def strip_filter(x): return x.strip() if x else None


class RegistrationForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=30)], filters=[strip_filter])
    email = StringField('Email',
                        validators=[DataRequired(), Email()], filters=[strip_filter])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'Email ID has been taken!') 


class LoginForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(), Email()], filters=[strip_filter])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=30)], filters=[strip_filter])
    email = StringField('Email',
                        validators=[DataRequired(), Email()], filters=[strip_filter])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'Email ID has been taken!')


class RequestResetForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(), Email()], filters=[strip_filter])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register!')


class ResetPasswordForm(Form):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
