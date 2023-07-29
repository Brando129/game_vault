from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import models_game
# from pprint import pprint
import requests
import os

# API Key
header = os.environ.get('KEY')

# Helper function for changing the "games" page
def make_request(url):
    headers = {
        "X-RapidAPI-Key": "7b12899369msh6c9c430681eef3ep1f7973jsn1dcd54b8a95f",
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Route for rendering the "games" page.
@app.get('/games')
def render_games_page():
    if 'user_id' not in session:
        return redirect('/logout')

    # Default games page url.
    if not 'url' in session:
        session['url'] = f"https://rawg-video-games-database.p.rapidapi.com/games?key={header}"

    json = make_request(session['url'])
    results = json['results']
    # pprint(results)

    # Data dictionary that is getting a page's url from the API.
    info = {
        "previous_page": json['previous'],
        "next_page": json['next']
    }

    # Empty games list
    games = []

    """For loop that creates a game object and appends that
    game object to the games list."""

    for result in results:
        game = {
            "id": result['id'],
            "name": result['name'],
            "background_image": result['background_image'],
            "short_screenshots": result['short_screenshots'][0]['image'],
            "playtime": result['playtime'],
            "ratings_count": result['ratings_count'],
            "released": result['released'],
            "platforms": result['platforms'][0]['platform']['name'],
            "rating": result['rating'],
            # "esrb_rating": result['esrb_rating']['name'],
            "genres": result['genres'][0]['name'],
            # "description": result['description_raw']
        }
        games.append(game)

    return render_template('games.html', games=games, info=info)


# Route for rendering the Show game details page.
@app.get('/show_game/details')
def show_game_details():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('show_game_details.html')


# POST ROUTES
# Route for changing the "Games" page.
@app.post('/url/set')
def set_url():
    if 'user_id' not in session:
        return redirect('/logout')
    session['url'] = request.form['url']
    return redirect('/games')

# Route for searching for a game.
@app.post('/search_game/details')
def search_game_details():
    if 'user_id' not in session:
        return redirect('/')

    id = request.form['name']
    # API requires the id.
    url = f"https://api.rawg.io/api/games/{id}?key={header}"
    response = requests.get(url)

    session['game_id'] = response.json()['id']
    session['image'] = response.json()['background_image']
    session['name'] = response.json()['name']
    session['developer'] = response.json()['developers'][0]['name']
    session['release_date'] = response.json()['released']
    session['play_time'] = response.json()['playtime']
    session['genre'] = response.json()['genres'][0]['name']
    session['rating'] = response.json()['esrb_rating']['name']
    session['achievements_count'] = response.json()['achievements_count']
    session['platforms'] = response.json()['platforms'][0]['platform']['name']
    session['description'] = response.json()['description_raw']

    # return response.json()
    return redirect('/show_game/details')

# Route for clicking game details.
@app.post('/click_game/details/')
def click_game_details():
    if 'user_id' not in session:
        return redirect('/')

    id = request.form['game_id']
    url = f"https://api.rawg.io/api/games/{id}?key={header}"
    response = requests.get(url)

    session['game_id'] = response.json()['id']
    session['image'] = response.json()['background_image']
    session['name'] = response.json()['name']
    session['developer'] = response.json()['developers'][0]['name']
    session['release_date'] = response.json()['released']
    session['play_time'] = response.json()['playtime']
    session['genre'] = response.json()['genres'][0]['name']
    session['rating'] = response.json()['esrb_rating']['name']
    session['achievements_count'] = response.json()['achievements_count']
    session['platforms'] = response.json()['platforms'][0]['platform']['name']
    session['description'] = response.json()['description_raw']

    return redirect('/show_game/details')

# Route for creating/saving a new game to a user's collection.
@app.post('/save/game')
def create_game():
    if 'user_id' not in session:
        return redirect('/logout')

    id = request.form['id']
    url = f"https://api.rawg.io/api/games/{id}?key={header}"
    response = requests.get(url)

    game = {
        "id": response.json()['id'],
        "name": response.json()['name'],
        "background_image": response.json()['background_image'],
        "playtime": response.json()['playtime'],
        "released": response.json()['released'],
        "rating": response.json()['rating'],
        "esrb_rating": response.json()['esrb_rating']['name'],
        "genre": response.json()['genres'][0]['name'],
        "platform": response.json()['platforms'][0]['platform']['name'],
        "description": response.json()['description_raw'],
        "user_id": session['user_id']
    }

    models_game.Game.save_game(game)
    return redirect('/games')