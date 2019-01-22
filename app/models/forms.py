from flask_wtf import FlaskForm
from wtforms import IntegerField ,DateField, StringField, PasswordField, BooleanField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class PreForm(FlaskForm):
    cpf = StringField("cpf", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=14, max=14, message="CPF invalido")])
    prof = StringField('prof', validators=[DataRequired()])
    preSubmit = SubmitField("preSubmit")

class ProfForm(FlaskForm):
    data = StringField("data", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=10, max=10, message="Data invalida")])
    horario = StringField("horario", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=5, max=5, message="Horário inválido!")]) # manha, tarde
    nivel = StringField("nivel", validators=[DataRequired(message="Campo Obrigatório!")]) #Iniciante, Iniciado, Intermediario, Avancado I, Avancado II
    #sala = StringField("sala", validators=[DataRequired(message="Campo Obrigatório!")])
    profSubmit = SubmitField("profSubmit")

class ProfLogin(FlaskForm):
    user = StringField("user", validators=[DataRequired(message="Campo Obrigatório!")])
    psswd = PasswordField("psswd", validators=[DataRequired(message="Campo Obrigatório!")])
    profLogSubmit = SubmitField("profLogSubmit")

class ConsultaAulas(FlaskForm):
    cpf = StringField("cpf", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=14, max=14, message="CPF invalido")])
    consultaSubmit = SubmitField("consultaSubmit")