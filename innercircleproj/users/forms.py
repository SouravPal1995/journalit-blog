
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from innercircleproj.models import User
from flask_login import current_user

class Registration(FlaskForm):
    name = StringField("Name : ", validators = [DataRequired()])
    email = StringField("Email : ", validators = [DataRequired(), Email()])
    password = PasswordField("Password : ", validators = [DataRequired(), EqualTo('password_conf', message="Password did not match")])
    password_conf = PasswordField("Re-enter Password : ", validators = [DataRequired()])
    submit = SubmitField("Register")
    
    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            return ValidationError("Email is already registered")
        
    def validate_name(self, field):
        if User.query.filter_by(email = field.data).first():
            return ValidationError("User name is taken")

class Login(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField('Login')
    
class UpdateUser(FlaskForm):
    name = StringField("Enter name: ")
    email = StringField("Enter email")
    profile_pic = FileField("Choose profile pic", validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField("Submit")
    
    def validate_name(self, name):
        if name.data!=current_user.name:
            if User.query.filter_by(name = name.data).first():
                raise ValidationError("Name is already registered")
            
    def validate_email(self, email):
        if email.data!=current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("Email is already registered")
    
    
    
    
    



        