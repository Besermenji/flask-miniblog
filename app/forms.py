from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    open_id = StringField('open_id', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class UserEditForm(FlaskForm):
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=160)])
    nickname = StringField('nickname', validators=[DataRequired()])
