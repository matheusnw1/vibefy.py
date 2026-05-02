
from flask import Flask, render_template, jsonify, request
from vibefy import interpretar_humor, buscar_musicas

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    dados = request.json
    humor = dados['humor']
    gostos = dados['gostos']
    musica = interpretar_humor(humor, gostos)
    print("IA retornou:", musica)
    resultado = buscar_musicas(musica)
    print("iTunes retornou:", resultado)
    nome, capa, preview = resultado[0]
    return jsonify({'nome': nome, 'capa': capa, 'preview': preview})

app.run()
