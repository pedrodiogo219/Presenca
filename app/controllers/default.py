from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app import app, db, lm, conn, session, engine
from sqlalchemy.sql import select, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

from app.models.forms import PreForm, ProfForm, ProfLogin, ConsultaAulas, CadForm
from app.models import tables

from datetime import date
from app.controllers.functions import strToDate, trataCpf, dateToStr

@app.route("/index", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def index():

    form = PreForm()
    form.prof.choices = [(p.apelido, p.apelido) for p in tables.Professor.query.all()]

    if request.method == "POST" and form.validate_on_submit():
        if form.id_uri.data:
            id_uri = form.id_uri.data
            query = select([tables.Aluno.id]).where(tables.Aluno.ID_URI == id_uri)
        elif form.email.data:
            email = form.email.data
            query = select([tables.Aluno.id]).where(tables.Aluno.email == email)
        else:
            flash('formulario vazio')
            return redirect(url_for('index'))

        conn = engine.connect()
        res = conn.execute(query).fetchone()

        if res:
            id_aluno = res['id']

            query = select([tables.Aula.id]).where(
                and_( tables.Aula.id_prof == tables.Professor.id,
                      and_( tables.Aula.ativa == 1,
                            and_( tables.Professor.apelido == form.prof.data,
                                  tables.Aula.dia == date.today() ))))
            result = conn.execute(query).fetchone()


            if result:
                id_aula = result['id']
                new_presenca = tables.Presenca(id_aula, id_aluno)
                db.session.add(new_presenca)
                try:
                    db.session.commit()
                except exc.IntegrityError:
                    db.session.rollback()
                    flash("Voce ja tem presenca nessa aula")
            else:
                flash("O professor nao tem nenhuma aula aberta pro dia de hoje")

        else:
            flash("Dado nao cadastrado")

    else:
        if form.errors:
            flash(form.errors)
    return render_template('home/index.html',
                            form=form)

@app.route("/prof", methods=["POST", "GET"])
def prof():

    if current_user.is_authenticated:
        form = ProfForm()
        form.sala.choices = [(s.nome, s.nome) for s in tables.Sala.query.all()]
        form.ciclo.choices = [(s.id, s.nome) for s in tables.Ciclo.query.all()]
        if form.validate_on_submit():
            horario = form.horario.data
            if form.horario.data == "manhã":
                horario = "manha"

            dia = strToDate(form.data.data)

            new_aula = tables.Aula(dia, horario, form.nivel.data, current_user.id, form.sala.data, form.ciclo.data)

            db.session.add(new_aula)
            db.session.commit()
            return redirect(url_for("minhasAulas"))
        else:
            if form.errors:
                flash(form.errors)

        aulas = tables.Aula.query.filter_by(id_prof=current_user.id)
        return render_template('home/aula.html', form=form, aulas=aulas)
    else:
        return redirect(url_for("login"))

@app.route("/minhasAulas")
def minhasAulas():
    aulas = tables.Aula.query.filter_by(id_prof=current_user.id).order_by(tables.Aula.ciclo.desc(), tables.Aula.dia, tables.Aula.horario)
    ciclos = tables.Ciclo.query.all()
    for c in ciclos:
        print(c.nome)
    return render_template('home/minhasaulas.html', aulas=aulas, ciclos=ciclos)


@app.route("/uberhub")
def sobre():
    return render_template('home/sobre.html')

@app.route("/lista/")
@app.route("/lista/<id_aula>")
def lista(id_aula=None):
    if current_user.is_authenticated:

        if id_aula == None:
            id_aula = tables.Aula.query.filter_by(id_prof=current_user.id).order_by(tables.Aula.id.desc()).first().id


        aula = tables.Aula.query.filter_by(id=id_aula).first()
        session = sessionmaker(bind=engine)()
        alunos = session.query(tables.Aluno).join(tables.Presenca).filter_by(id_aula=id_aula).all()

        return render_template('home/table.html',
                                alunos=alunos, aula=aula)
    else:
        return redirect(url_for('login'))



@app.route("/abriraula/<id_aula>")
def abriraula(id_aula=None):
    #if id_aula==None:

    s = tables.Aula.__table__.update().where(tables.Aula.id==id_aula).values(ativa=1)
    conn = engine.connect()
    conn.execute(s)
    return redirect(url_for('lista', id_aula=id_aula))


@app.route("/fecharaula/<id_aula>")
def fecharaula(id_aula=None):
    # if id_aula==None:

    s = tables.Aula.__table__.update().where(tables.Aula.id==id_aula).values(ativa=0)
    conn = engine.connect()
    conn.execute(s)
    return redirect(url_for('lista', id_aula=id_aula))



@lm.user_loader
def load_user(id):
    return tables.Professor.query.filter_by(id=id).first()


@app.route("/login", methods=["POST", "GET"])
def login():
    form = ProfLogin()
    if request.method == "POST" and form.validate_on_submit():
        user = tables.Professor.query.filter_by(apelido=form.user.data).first()
        if user:
            if user.senha == form.psswd.data:
                login_user(user)
                flash("Você logou com sucesso.")
                return redirect(url_for("prof"))
            else:
                flash("Sua senha está incorreta.")
        else:
            flash("Usuário inválido.")
    return render_template('home/profLogin.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

"""
@app.route("/teste")
def teste():
    query = session.query(tables.Presenca, tables.Aluno, tables.Aula).join(tables.Aluno).join(tables.Aula).all()
    print(query)
    #print(conn.execute(query))
    return "deu certo"
"""


@app.route("/consulta", methods=["POST", "GET"])
def consulta():
    form = ConsultaAulas()
    if request.method == "POST" and form.validate_on_submit():
        if form.id_uri.data:
            id_uri = form.id_uri.data
            query = select([tables.Aula.dia, tables.Aula.nivel, tables.Professor.apelido]).where(
                and_( tables.Aula.id == tables.Presenca.id_aula,
                    and_(tables.Presenca.id_aluno==tables.Aluno.id,
                        and_(tables.Aluno.ID_URI == id_uri,
                            and_(tables.Aula.id_prof == tables.Professor.id,
                                 tables.Aula.ativa == 0
                            )
                        )
                    )
                )
            )
        if form.email.data:
            email = form.email.data
            query = select([tables.Aula.dia, tables.Aula.nivel, tables.Professor.apelido]).where(
                and_( tables.Aula.id == tables.Presenca.id_aula,
                    and_(tables.Presenca.id_aluno==tables.Aluno.id,
                        and_(tables.Aluno.email == email,
                            and_(tables.Aula.id_prof == tables.Professor.id,
                                 tables.Aula.ativa == 0
                            )
                        )
                    )
                )
            )
        conn = engine.connect()
        result = conn.execute(query)
        return render_template('home/mostraAulas.html', aulas=result)
    else:
        return render_template('home/consultaAulas.html', form=form)

@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    form = CadForm()
    if form.validate_on_submit():
        cpf = ""
        for letra in form.cpf.data:
            if '9' >= letra >= '0':
                cpf+=letra
        tel = ""
        for letra in form.tel.data:
            if '9' >= letra >= '0':
                tel+=letra

        if request.method == "POST" and form.validate_on_submit():
            user = tables.Professor.query.filter_by(apelido=form.usrProf.data).first()
            if user:
                if user.senha == form.psswdProf.data:
                    new_aluno = tables.Aluno(cpf, form.email.data, form.name.data, tel, form.horario.data, form.ID_URI.data)

                    db.session.add(new_aluno)
                    db.session.commit()
                    flash("Você foi cadastrado com sucesso, marque sua presença.")
                    return redirect(url_for("index"))
                else:
                    flash("Senha incorreta.")
            else:
                flash("Usuário inválido.")
    else:
        if form.errors:
            flash(form.errors)

    return render_template('home/cadastro.html', form=form)

@app.route("/material")
def material():

    return render_template('home/material.html')
