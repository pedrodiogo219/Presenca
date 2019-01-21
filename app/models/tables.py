from app import db
import sqlalchemy as sa
from sqlalchemy import CheckConstraint

class Aluno(db.Model):
    __tablename__ = "aluno"

    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf      = db.Column(db.String(11), nullable=False, unique=True)
    email    = db.Column(db.String(50), nullable=False, unique=True)
    nome     = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(11))
    horario  = db.Column(db.String(5), CheckConstraint('horario IN ("manha", "tarde")'), nullable=False)
    ID_URI   = db.Column(db.String(5), unique=True)


class Professor(db.Model):
    __tablename__ = "professor"

    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf      = db.Column(db.String(11), nullable=False, unique=True)
    apelido  = db.Column(db.String(15), nullable=False, unique=True)
    email    = db.Column(db.String(50), nullable=False, unique=True)
    nome     = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(11))
    ID_URI   = db.Column(db.String(5), unique=True)
    senha    = db.Column(db.String(30), nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Aula(db.Model):
    __tablename__ = "aula"

    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dia      = db.Column(db.Date)
    horario  = db.Column(db.String(5), CheckConstraint('horario="manha" or horario="tarde"'), nullable=False)
    nivel    = db.Column(db.String(15), nullable=False)
    ativa    = db.Column(db.Boolean, default=False, server_default=sa.sql.expression.false(), nullable=False)
    id_prof  = db.Column(db.Integer, db.ForeignKey('professor.id'))


    fk_professor =  db.relationship('Professor', foreign_keys=id_prof)

    def __init__(self, d, h, n, i):
        self.dia     = d
        self.horario = h
        self.nivel   = n
        self.id_prof = i


class Presenca(db.Model):
    __tablename__ = "presenca"

    id_aula  = db.Column(db.Integer, db.ForeignKey('aula.id'), primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), primary_key=True)

    fk_aula  = db.relationship('Aula', foreign_keys=id_aula)
    fk_aluno = db.relationship('Aluno', foreign_keys=id_aluno)



    def __init__(self, idAu, idAl):
        self.id_aula=idAu
        self.id_aluno=idAl
   

"""
insert into aluno(cpf, email, nome, telefone, horario, ID_URI) values('12629753603', 'pedro@pedro.com', 'pedrin', '32323223', 'manha', '12345');
insert into aluno(cpf, email, nome, telefone, horario, ID_URI) values('12629753604', 'kkk@pedro.com', 'kkk', '32323223', 'manha', '12346');
insert into aluno(cpf, email, nome, telefone, horario, ID_URI) values('12345678901', 'hehe@hehe.com', 'hehe', '31133113', 'manha', '54321');

"""
