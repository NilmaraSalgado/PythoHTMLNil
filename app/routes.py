# ficaram nossas rotas que dependem do app

from app import app

@app.route('/')
def index():
    return "Hello World"