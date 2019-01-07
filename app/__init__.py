from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',  MigrateCommand)

from app.models import tables
from app.controllers import default


from app.controllers.functions import shufflebg
app.jinja_env.globals.update(shufflebg=shufflebg)

