from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User, Member

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')

class NewMemberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    profession = StringField('Profession', validators=[DataRequired()])
    level = IntegerField('Level', validators=[InputRequired()])
    party = StringField('Party')
    alignment = StringField('Alignment', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Add Member')

    def validate_name(self, name):
        member = db.session.scalar(sa.select(Member).where(
            Member.name == name.data))
        if member is not None:
            raise ValidationError('Please use a different name.')

    def validate_level(self, level):
        if level.data < 0 or level.data > 20:
            raise ValidationError('Please enter a level between 0 and 20')

    def validate_alignment(self, alignment):
        if len(alignment.data) != 2:
            raise ValidationError('Please enter the alignment as two letters.')
