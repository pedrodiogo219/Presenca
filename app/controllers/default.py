from app import app, db, lm
from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user

from app.models.forms import PreForm
from app.models.forms import ProfForm
from app.models.forms import ProfLogin

from app.models import tables

from app.controllers.functions import strToDate

@app.route("/index", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    form = PreForm()
    if form.validate_on_submit():
        print(form.cpf.data)
        print(form.prof.data)
    else:
        print(form.errors)
    return render_template('home/index.html',
                            form=form)

@app.route("/prof", methods=["POST", "GET"])
def prof():

    if current_user.is_authenticated:
        form = ProfForm()
        if form.validate_on_submit():
            horario = form.horario.data
            if form.horario.data == "manhã":
                horario = "manha"

            dia = strToDate(form.data.data)

            new_aula = tables.Aula(dia, horario, form.nivel.data, current_user.id)

            db.session.add(new_aula)
            db.session.commit()
            print("commit feito")
            return redirect(url_for("lista"))
        else:
            print(form.errors)
        return render_template('home/aula.html',
                                form=form)
    else:
        return redirect(url_for("login"))

@app.route("/uberhub", methods=["POST", "GET"])
def sobre():
    return render_template('home/sobre.html')

@app.route("/lista")
def lista():
    dados = tables.Aluno.query.all()
    print(dados)

    return render_template('home/table.html',
                            dados=dados)


@lm.user_loader
def load_user(id):
    return tables.Professor.query.filter_by(id=id).first()


@app.route("/login", methods=["POST", "GET"])
def login():
    form = ProfLogin()
    print("aaaaa")
    if form and form.validate_on_submit():
        print("abriu")
        user = tables.Professor.query.filter_by(apelido=form.user.data).first()
        print("procurei")
        if user:
            if user.senha == form.psswd.data:
                login_user(user)
                print("Você logou com sucesso.")
                return redirect(url_for("prof"))
            else:
                print("Sua senha está incorreta.")
        else:
            print("Usuário inválido.")
    return render_template('home/profLogin.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/teste")
def teste():
    dia = strToDate("31/12/2019")

    new_aula = tables.Aula(dia, "tarde", "Intermediario", 1)
    db.session.add(new_aula)
    db.session.commit()


    return "deu certo"