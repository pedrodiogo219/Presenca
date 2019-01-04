from flask_wtf import FlaskForm
from wtforms import IntegerField ,DateField, StringField, PasswordField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired


class PreForm(FlaskForm):
    username = StringField("cpf", validators=[DataRequired()])
    name = StringField('prof', validators=[DataRequired()])
    cadSubmit = SubmitField("preSubmit")

class ProfForm(FlaskForm):
    username = StringField("data", validators=[DataRequired()])
    password = PasswordField("sala", validators=[DataRequired()])
    logSubmit = SubmitField("profSubmit")
