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

    form = ProfForm()
    if form.validate_on_submit():
        print(form.data.data)
        print(form.sala.data)
    else:
        print(form.errors)
    return render_template('home/aula.html',
                            form=form)

@app.route("/uberhub", methods=["POST", "GET"])
def sobre():
    return render_template('home/sobre.html')

@app.route("/lista")
def lista():
    dados = tables.Aluno.query.all()
    print(dados)

    return render_template('home/table.html',
                            dados=dados)
