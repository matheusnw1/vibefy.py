
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
        art = (f'{musica['artworkUrl100']}')
        preview = (f'{musica['previewUrl']}')
        lista.append((music, art, preview))
    return lista


def exibir_musicas(musicas):
    i = 0
    for musica in musicas:
        i += 1
        print(f'Musica {i}: {musica}')


def interpretar_humor(humor, gostos):
    resposta = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {"role": "user", "content": f'O usuário está se sentindo assim: {humor} e ele gosta dessas músicas: {gostos}. Me retorne apenas o nome de um artista musical e uma música com base no humor e gosto dessa pessoa no formato Artista - Música, sem explicação, só o nome.'}
        ]
    )
    artista = resposta.choices[0].message.content
    return artista.strip('.')


def pedir_humor():
    humor = input('Como você está se sentindo?: ')
    return humor

def abrir_musica(nome_musica):
    musica = f'https://www.youtube.com/results?search_query={nome_musica}'
    webbrowser.open(musica)

def pedir_musicas():
    gostos = []
    i = 0
    while i < 3:
        musicas = input('Digite até 3 músicas que você gosta: ')
        if musicas == '':
            break
        i+= 1
        gostos.append(musicas)
    return gostos

if __name__ == '__main__':
    humor = pedir_humor()
    gostos = pedir_musicas()
    musica = interpretar_humor(humor, gostos)
    nome_musica = abrir_musica(musica)  
    resultados = buscar_musicas(musica)
    nome, capa, preview = resultados[0]
    print(nome, capa, preview)
    