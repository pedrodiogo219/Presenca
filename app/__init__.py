from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from config import SQLALCHEMY_DATABASE_URI

from sqlalchemy.pool import SingletonThreadPool


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',  MigrateCommand)

lm = LoginManager()
lm.init_app(app)

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, poolclass=SingletonThreadPool)
conn = engine.connect()
session = sessionmaker(bind=engine)()

from app.models import tables
from app.controllers import default


from app.controllers.functions import shufflebg, dateToStr, shufflename
app.jinja_env.globals.update(shufflebg=shufflebg)
app.jinja_env.globals.update(dateToStr=dateToStr)
app.jinja_env.globals.update(shufflename=shufflename)
