from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import app, db, lm, conn, session

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
            return redirect(url_for("lista"))
        else:
            print(form.errors)

        aulas = tables.Aula.query.filter_by(id_prof=current_user.id)
        return render_template('home/aula.html', form=form, aulas=aulas)
    else:
        return redirect(url_for("login"))

@app.route("/uberhub", methods=["POST", "GET"])
def sobre():
    return render_template('home/sobre.html')

@app.route("/lista/")
@app.route("/lista/<id_aula>")
def lista(id_aula=None):
    if current_user.is_authenticated:

        if id_aula == None:
            id_aula = tables.Aula.query.filter_by(id_prof=current_user.id).order_by(tables.Aula.id.desc()).first().id


        aula = tables.Aula.query.filter_by(id=id_aula).first()
        alunos = session.query(tables.Aluno).join(tables.Presenca).filter_by(id_aula=id_aula).all()

        print(aula)
        print(alunos)
        print("printei")

        return render_template('home/table.html',
                                alunos=alunos, aula=aula)
    else:
        return redirect(url_for('login'))



@app.route("/abriraula/<id_aula>")
def abriraula(id_aula=None):
    # if id_aula==None:

    s = tables.Aula.__table__.update().where(tables.Aula.id==id_aula).values(ativa=1)
    conn.execute(s)
    return redirect(url_for('lista', id_aula=id_aula))


@app.route("/fecharaula/<id_aula>")
def fecharaula(id_aula=None):
    # if id_aula==None:

    s = tables.Aula.__table__.update().where(tables.Aula.id==id_aula).values(ativa=0)
    conn.execute(s)
    return redirect(url_for('lista', id_aula=id_aula))



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
    query = session.query(tables.Presenca, tables.Aluno, tables.Aula).join(tables.Aluno).join(tables.Aula).all()
    print(query)
    #print(conn.execute(query))
    return "deu certo"