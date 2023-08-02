from flask import Flask, render_template

from flask_socketio import SocketIO, send

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*") # isso aqui é o tunel de comunicação entre os pcs

# funcionalidade de enviar mensagem

@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# Criar nossa primeira página = primeira rota

@app.route("/")
def homepage():
    return render_template("index.html")

# Rodar o app
socketio.run(app, host="192.168.0.84")

# websocket -> tunel