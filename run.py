from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    if name:
        return f'hello {name}'
    else:
        return "hello man"

