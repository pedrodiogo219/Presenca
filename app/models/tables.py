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
    sala     = db.Column(db.String(30), db.ForeignKey('sala.nome'))
    ciclo    = db.Column(db.Integer, db.ForeignKey('ciclo.id'))

    fk_professor = db.relationship('Professor', foreign_keys=id_prof)
    dk_sala      = db.relationship('Sala', foreign_keys=sala)
    fk_ciclo     = db.relationship('Ciclo', foreign_keys=ciclo)

    def __init__(self, d, h, n, i, s, c):
        self.dia     = d
        self.horario = h
        self.nivel   = n
        self.id_prof = i
        self.sala    = s
        self.ciclo   = c


class Instituicao(db.Model):
    __tablename__ = "instituicao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    endereco = db.Column(db.String(100), nullable=False)


class Sala(db.Model):
    __tablename__ = "sala"

    nome           = db.Column(db.String(30), primary_key=True)
    capacidade     = db.Column(db.Integer, nullable=False)
    id_instituicao = db.Column(db.Integer, db.ForeignKey('instituicao.id'))

    fk_instituicao = db.relationship('Instituicao', foreign_keys=id_instituicao)


class Ciclo(db.Model):
    __tablename__ = "ciclo"

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome        = db.Column(db.String(50), nullable=False)
    data_inicio = db.Column(db.Date)
    data_fim    = db.Column(db.Date)


class Participantes(db.Model):
    __tablename__ = "participantes"

    id_ciclo       = db.Column(db.Integer, db.ForeignKey('ciclo.id'), primary_key=True)
    id_instituicao = db.Column(db.Integer, db.ForeignKey('instituicao.id'), primary_key=True)

    fk_ciclo       = db.relationship('Ciclo', foreign_keys=id_ciclo)
    fk_instituicao = db.relationship('Instituicao', foreign_keys=id_instituicao)

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
