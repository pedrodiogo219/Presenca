from flask import Flask
from flask_script import Manager


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ASJDIDASDASDADS'
#app.config.from_object('config')

manager = Manager(app)

from app.controllers import default

from app.controllers.functions import shufflebg
app.jinja_env.globals.update(shufflebg=shufflebg)
