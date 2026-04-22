
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
import webbrowser

load_dotenv()
chave = os.getenv('OPENROUTER_API_KEY')
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=chave
)


def buscar_musicas(musica):
    lista = []
    musica = requests.get(f'https://itunes.apple.com/search?term={musica}&media=music&limit=5')
    dicionario = (musica.json())
    musicas = (dicionario['results'])
    for musica in musicas:
        music = (f'{musica['trackName']}')
        lista.append(music)
    return lista


def exibir_musicas(musicas):
    i = 0
    for musica in musicas:
        i += 1
        print(f'Musica {i}: {musica}')


def interpretar_humor(humor):
    resposta = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
            {"role": "user", "content": f'O usuário está se sentindo assim: {humor}. Me retorne apenas o nome de um artista musical e uma música que combina com esse sentimento no formato Artista - Música, sem explicação, só o nome.'}
        ]
    )
    artista = resposta.choices[0].message.content
    return artista


def pedir_humor():
    humor = input('Como você está se sentindo?: ')
    return humor

def abrir_musica(nome_musica):
    musica = f'https://www.youtube.com/results?search_query={nome_musica}'
    webbrowser.open(musica)



humor = pedir_humor()
musica = interpretar_humor(humor)
nome_musica = abrir_musica(musica)

