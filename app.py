
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    dados = requests.json
    return jsonify({'resultado': 'ok'})

app.run()
