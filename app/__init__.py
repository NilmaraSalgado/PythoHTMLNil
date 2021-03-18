from flask import Flask

app = Flask(__name__)

#faz importação de todas as rotas
from app import routes