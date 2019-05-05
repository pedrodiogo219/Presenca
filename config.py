
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
#SQLALCHEMY_DATABASE_URI = "postgres://usrpresenca:tstrt12@localhost/presenca"
SQLALCHEMY_DATABASE_URI = "postgres://wnnmfilccvybuc:c33a626592f5570b44abd85c0a6858517a4df7a5a3d37600280d69097c9d8cf7@ec2-54-197-234-117.compute-1.amazonaws.com:5432/d7dbsund4khlfs"
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'ASDASDASDASDASD'
