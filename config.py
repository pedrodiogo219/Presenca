
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
#SQLALCHEMY_DATABASE_URI = "postgres://zevzrrqiikbhhc:2371d50a04cf84207eac2807f125f5dd8ef3588c709fed686760c44dbf8f676c@ec2-23-21-129-125.compute-1.amazonaws.com:5432/df00kqhp7setue"
#SQLALCHEMY_DATABASE_URI = "postgres://pediogo:tstrt12@localhost/pediogo"
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'ASDASDASDASDASD'
