
import requests

def buscar_musicas(artista):
    lista = []
    musica = requests.get(f'https://itunes.apple.com/search?term={artista}&media=music&limit=5')
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


musicas = buscar_musicas('brunomars')
exibir_musicas(musicas)



