from app import db
from sqlalchemy import CheckConstraint

class Aluno(db.Model):
    __tablename__ = "aluno"

    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf      = db.Column(db.String(11), nullable=False, unique=True)
    email    = db.Column(db.String(50), nullable=False, unique=True)
    nome     = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(11))
    horario  = db.Column(db.String(5), CheckConstraint('horario="manha" or horario="tarde"'), nullable=False)
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


class Aula(db.Model):
    __tablename__ = "aula"

    id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dia = db.Column(db.Date)
    horario  = db.Column(db.String(5), CheckConstraint('horario="manha" or horario="tarde"'), nullable=False)
    nivel = db.Column(db.String(15), nullable=False)
    id_prof = db.Column(db.Integer, db.ForeignKey('professor.id'))

    fk_professor =  db.relationship('Professor', foreign_keys=id_prof)


class Presenca(db.Model):
    __tablename__ = "presenca"

    id_aula = db.Column(db.Integer, db.ForeignKey('aula.id'), primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), primary_key=True)

    fk_aula = db.relationship('Aula', foreign_keys=id_aula)
    fk_aluno = db.relationship('Aluno', foreign_keys=id_aluno)
   

"""
insert into aluno(cpf, email, nome, telefone, horario, ID_URI) values('12629753603', 'pedro@pedro.com', 'pedrin', '32323223', 'manha', '12345');
insert into aluno(cpf, email, nome, telefone, horario, ID_URI) values('12629753604', 'kkk@pedro.com', 'kkk', '32323223', 'manha', '12346');
insert into aluno(cpf, email, nome, telefone, horario, ID_URI) values('12345678901', 'hehe@hehe.com', 'hehe', '31133113', 'manha', '54321');

"""