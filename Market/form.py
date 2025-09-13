from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField 
from wtforms.validators import Length, DataRequired,Email, EqualTo, ValidationError  
from Market.models import User
class register(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("User name already exists so try another name")
    def validate_email(self, email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email: 
            raise ValidationError("That email has been signed up so try another one or just login in")
    username = StringField(label="User Name",validators = [Length( min=2, max=30),DataRequired()])
    email = StringField(label="Email Address",validators=[Email(),DataRequired()])
    password1 = PasswordField(label="Password",validators=[Length(min=8),DataRequired()])
    password2 = PasswordField(label="Confirm Password",validators=[EqualTo('password1'),DataRequired()])
    submit= SubmitField(label="Create Account")
class Login_form(FlaskForm):
    username=StringField(label="User Name", validators=[DataRequired()])
    password=PasswordField(label="Password",validators=[DataRequired()])
    submit=SubmitField(label="Sign in")
class purchaseitemform(FlaskForm):
    submit=SubmitField(label="Purchase item")
class sellitemform(FlaskForm):
    submit=SubmitField(label="sell item")
# class dashboard