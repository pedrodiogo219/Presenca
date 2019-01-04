from flask_wtf import FlaskForm
from wtforms import IntegerField ,DateField, StringField, PasswordField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired, Length


class PreForm(FlaskForm):
    cpf = StringField("cpf", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=14, max=14, message="CPF invalido")])
    prof = StringField('prof', validators=[DataRequired()])
    preSubmit = SubmitField("preSubmit")

class ProfForm(FlaskForm):
    data = StringField("data", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=10, max=10, message="Data invalida")])
    sala = StringField("sala", validators=[DataRequired(message="Campo Obrigatório!")])
    profSubmit = SubmitField("profSubmit")
