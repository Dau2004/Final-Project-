from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField, TextAreaField
from wtforms.validators import DataRequired

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Login')

class ScheduleCollectionForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    collection_date = DateField('Collection Date', validators=[DataRequired()])
    collection_time = TimeField('Collection Time', validators=[DataRequired()])
    submit = SubmitField('Schedule Collection')

class TrackRecyclingForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    materials = TextAreaField('Recycled Materials', validators=[DataRequired()])
    submit = SubmitField('Track Recycling')
