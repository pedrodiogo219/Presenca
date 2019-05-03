
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
#SQLALCHEMY_DATABASE_URI = "postgres://usrpresenca:tstrt12@localhost/presenca"
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'ASDASDASDASDASD'
