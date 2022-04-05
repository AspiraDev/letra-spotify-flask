import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="spotify"
)

cursor = db.cursor()

client_credentials_manager = SpotifyClientCredentials(client_id='29170be8ba2948c695f1d9675e3a6fb1', client_secret='202c0a4de3404299938c776ccf1a31c8')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_URI = "6cFlbPOhqAsnPzcUjWCjS3"
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
musicas = []
artistas = []
for track in sp.playlist_tracks(playlist_URI)["items"]:
    album = track["track"]["album"]["name"]
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    imagem = track["track"]["album"]["images"][0]["url"]
    print(imagem)

    
    
    
    
    
    
    
    
    
    
    #musicas.append(f'{track_name} - {artist_name}')
    #comandoSQL = "INSERT INTO usuarios(cidade, idade, nome) VALUES (%s,%s, %s)"
    #dados = (track_name, artist_name, album)
    #cursor.execute(comandoSQL, dados)
    #db.commit()

    #cursor.execute("SELECT artista FROM musicas")

    #valores = cursor.fetchall()

    #print(valores)
