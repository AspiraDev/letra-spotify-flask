## Letra de músicas do spotify com python e flask

Programa feito em python e flask que ao adicionar o link de uma playlist spotify, retorna uma interface web com todas as músicas da playlist. Ao clica em algúma música, retorna a letra desta música.

## Instalação das dependência

```sh
cd letra-spotify-flask
pip install Flask
pip install spotipy
```

## Configuração
Adiciona seu ID e sua KEY spotify no arquivo `app.py` 
https://developer.spotify.com/dashboard/applications

Adiciona sus KEY vagalume no arquivo `app.py` 
https://auth.vagalume.com.br/settings/api/

## Iniciando o programa

```sh
set FLASK_APP=hello
flask run
```
Acesse no seu navegador: http://127.0.0.1:5000/

