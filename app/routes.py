# ficaram nossas rotas que dependem do app

from app import app
#ler de html e manda o arquivo pra frente
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
   # return "Hello World"
    return render_template("index.html", username="nil")
