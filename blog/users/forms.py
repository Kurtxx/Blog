# users/FORMS.PY

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from blog.models import User

#####################################
########## Klasa Logowania ##########
#####################################

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Zaloguj się!')

#######################################
########## Klasa Rejestracji ##########
#######################################

class RegistratonForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Zarejestruj się!')

##########################################
## Sprawdza czy email nie jest w bazie! ##
##########################################

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Pod tym mailem użytkownik został już zarejestrowany!')

#####################################################################
######### Sprawdza czy nazwa użytkownika nie jest w bazie! ##########
#####################################################################

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nazwa użytkownika została już użyta!')

#####################################################################
############### Dodaje/Zmienia Zdjęcie profilowe ####################
############### Zmienia Maila i nazwe Użytkownika ###################
#####################################################################

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Zmień zdjęcie profilowe', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Aktualizuj!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Pod tym mailem użytkownik został już zarejestrowany!')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nazwa użytkownika została już użyta!')
