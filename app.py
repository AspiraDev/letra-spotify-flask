from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

#SPOTIFY - https://developer.spotify.com/dashboard/applications
CLIENTE_ID = '29170be8b354453443544175e3a6fb1'
KEY_SPOTIFY = '202c03485438443776ccf1a31c8'

#VAGALUME - https://auth.vagalume.com.br/settings/api/
KEY_VAGALUME = '85SD5F1SD41F8D181313451'


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def inicio():
    playlist()
    return render_template('index.html', len = contador, album = albuns, artista = artistas, musica = musicas, imagem = imagens)


def playlist():

    global track_name, albuns, artistas, musicas, imagens, playlist_link, contador

    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENTE_ID, client_secret=KEY_SPOTIFY)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    try:
        playlist_link = request.form.get('name')
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]
        
        track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
        musicas = []
        artistas = []
        imagens = []
        albuns = []
        for track in sp.playlist_tracks(playlist_URI)["items"]:
            album = track["track"]["album"]["name"]
            track_name = track["track"]["name"]
            artist_name = track["track"]["artists"][0]["name"]
            imagem = track["track"]["album"]["images"][0]["url"]

            
            musicas.append(track_name)
            artistas.append(artist_name)
            imagens.append(imagem)
            albuns.append(album)

        contador = len(albuns)
    except:
        contador = 0
        artistas = 'none'
        imagens = 'none'
        albuns = 'none'
        musicas = 'none'



@app.route('/letra/<count>')
def letra(count):
    print(count)


    album = albuns[int(count)]
    artista = artistas[int(count)]
    musica = musicas[int(count)]
    imagem = imagens[int(count)]

    data = requests.get(f"https://api.vagalume.com.br/search.php?art={artista}&mus={musica}&apikey={KEY_VAGALUME}")
    letra = data.json()

    letra = letra['mus'][0]['text']
    letra = letra.replace('\n', '<br>')

    return render_template('letra.html',letra = letra, count = contador, album = album, artista = artista, musica = musica, imagem = imagem)

