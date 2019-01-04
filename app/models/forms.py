from flask_wtf import FlaskForm
from wtforms import IntegerField ,DateField, StringField, PasswordField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired


class PreForm(FlaskForm):
    cpf = StringField("cpf", validators=[DataRequired()])
    prof = StringField('prof', validators=[DataRequired()])
    preSubmit = SubmitField("preSubmit")

class ProfForm(FlaskForm):
    data = StringField("data", validators=[DataRequired()])
    sala = StringField("sala", validators=[DataRequired()])
    profSubmit = SubmitField("profSubmit")
