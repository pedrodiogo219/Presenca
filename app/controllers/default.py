from app import app
from flask import render_template

from app.models.forms import PreForm
from app.models.forms import ProfForm
from app.models.forms import ProfLogin

from app.models import tables

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
    dados = tables.Aluno.query.all()
    print(dados)

    form = ProfForm()
    if form.validate_on_submit():
        print(form.data.data)
        print(form.sala.data)
    else:
        print(form.errors)
    return render_template('home/aula.html',
                            form=form,
                            dados=dados)

@app.route("/uberhub", methods=["POST", "GET"])
def sobre():
    return render_template('home/sobre.html')
