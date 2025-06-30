from flask import Flask, request, jsonify
from flask_cors import CORS
from database import verificar_usuario

app = Flask(_name_)
CORS(app)  # Permite o frontend acessar a API

@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    if verificar_usuario(dados['usuario'], dados['senha']):
        return jsonify({"mensagem": "Login bem-sucedido!"})
    else:
        return jsonify({"mensagem": "Usuário ou senha incorretos."}), 401

if _name_ == '_main_':
    app.run(debug=True)