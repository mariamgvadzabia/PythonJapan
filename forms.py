from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, length, equal_to, Email


class RegisterFrom(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[length(min=8, max=40)])
    repeat_password = PasswordField("Repeat Password", validators=[equal_to("password")])
    birthday = DateField("Birthday", validators=[DataRequired()])
    submit = SubmitField("Register")

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('souvenirs', 'Souvenirs'),
        ('tickets', 'Museum Tickets'),
        ('food', 'Traditional Snacks'),
        ('place', 'Visit:Fukuoka (NEW)'),
        ('place', 'Visit:Nagoya (NEW)'),
        ('Neon skyscrapers rising above quiet, historic shrines.', 'TOKYO')


    ])
    img = FileField( validators=[DataRequired(), FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Add Product")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

class AskForm(FlaskForm):
    question = StringField("Ask AI", validators=[DataRequired(),
    length(max=200, message="Maximum 200 characters allowed."
    )])
    submit = SubmitField("Send")