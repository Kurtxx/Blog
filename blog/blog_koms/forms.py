# blog_koms/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class AddCommentForm(FlaskForm):
    body = StringField("Body", validators=[DataRequired()])
    submit = SubmitField("Post")
