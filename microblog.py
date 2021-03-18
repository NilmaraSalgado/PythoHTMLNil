from app import app

#app = Flask("microblog") #programa que fica ligado na internet e recebe microrequesições e vai ter rotas  (liga url com funçao do pyton)

#quero linkar essa função com uma rota (docom 2 urls)
#toda vez que a pessoa entrar no ocean.com e encontrar / vai retornar a função
#vou fazer com esse decorator em cima da função 
#@app.route("/")
#def index ():
 #   return "Hello World"
#rodar o servidor que vai fazer esse link
#app.run()

#agora vamos distribuir em outros arquivos para organizar o trabalho

#seguimos os passos
#pegamos o link do github e colamos no gitpod.io
#pip install flask (instalar)
#File new -> microblog.py -> salvar -> executar: python3 microblog.py

#salvar no git -> git add . -> git commit -m "Hello World" -> git push
# Agora, em uma outra fase:
# criar pasta app
#criar os arquivos nessa pasta -> __init__.py e routes.py
#precisamos instalar o pip install python-dotenv

#criou arquivo fora da pasta app .. arquivo .flaskenv
#testando a execução - > flask run

#Na 2a parte da aula vamos apreder sobre templates
# vamos fazer um arquivo html e vamos pedir para o flask mandar esse arquivo html para as pessoas.
# No arquivo routes 
