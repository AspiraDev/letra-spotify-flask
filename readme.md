## Letra de músicas do spotify com python e flask

Programa feito em python e flask que ao adicionar o link de uma playlist spotify, retorna uma interface web com todas as músicas da playlist. Ao clica em algúma música, retorna a letra desta música.

## Instalação das dependência

```sh
cd letra-spotify-flask
pip install Flask
pip install spotipy
```

## Configuração
Adiciona seu ID e sua KEY spotify e vagalume no arquivo `app.py` 
Spotify: https://developer.spotify.com/dashboard/applications
Vagalume: https://auth.vagalume.com.br/settings/api/

```
CLIENTE_ID='SEU ID SPOTIFY'
KEY_SPOTIFY='SUA KEY SPOTIFY'
KEY_VAGALUME='SUA KEY VAGALUME'
```

## Iniciando o programa

```sh
set FLASK_APP=hello
flask run
```
Acesse no seu navegador: http://127.0.0.1:5000/

