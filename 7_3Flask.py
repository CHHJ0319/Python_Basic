#Flask모듈
"https://flask.palletsprojects.com/en/2.0.x/"
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Flask</h1>"