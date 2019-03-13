from flask_wtf import FlaskForm
from wtforms import IntegerField ,DateField, StringField, PasswordField, BooleanField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional

class PreForm(FlaskForm):
    email = StringField("email", validators=[Length(min=6, max=35), Optional()])
    id_uri = StringField("id_uri", validators=[Optional()])
    prof = SelectField('prof', choices=[])
    preSubmit = SubmitField("preSubmit")

class ProfForm(FlaskForm):
    data = StringField("data", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=10, max=10, message="Data invalida")])
    horario = SelectField("horario", choices=[("manha", "manha"),("tarde", "tarde")]) # manha, tarde
    nivel = SelectField("nivel", choices=[("Iniciante","Iniciante"),("Iniciado","Iniciado"),("Intermediario","Intermediario"),("Avancado I","Avancado I"),("Avancado II","Avancado II")]) #Iniciante, Iniciado, Intermediario, Avancado I, Avancado II
    sala = SelectField('sala', choices=[])
    ciclo = SelectField('ciclo', choices=[], coerce=int)
    profSubmit = SubmitField("profSubmit")

class ProfLogin(FlaskForm):
    user = StringField("user", validators=[DataRequired(message="Campo Obrigatório!")])
    psswd = PasswordField("psswd", validators=[DataRequired(message="Campo Obrigatório!")])
    profLogSubmit = SubmitField("profLogSubmit")

class ConsultaAulas(FlaskForm):
    email = StringField("email", validators=[Length(min=6, max=35), Optional()])
    id_uri = StringField("id_uri", validators=[Optional()])
    consultaSubmit = SubmitField("consultaSubmit")

class CadForm(FlaskForm):
    cpf = StringField("cpf", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=14, max=14, message="CPF invalido")])
    email = StringField("email", validators=[Length(min=6, max=35), DataRequired(message="Campo Obrigatório!")])
    name = StringField("name", validators=[DataRequired(message="Campo Obrigatório!")])
    tel = StringField("tel", validators=[DataRequired(message="Campo Obrigatório!"), Length(min=8, max=14, message="Telefone inválido")])
    horario = SelectField("horario", choices=[("manha", "manha"),("tarde", "tarde")])
    ID_URI = StringField("id_uri", validators=[DataRequired(message="Campo Obrigatório!")])
    usrProf = StringField("usrProf", validators=[DataRequired(message="Campo Obrigatório!")])
    psswdProf = PasswordField("psswd", validators=[DataRequired(message="Campo Obrigatório!")])
    cadSubmit = SubmitField("cadSubmit")
