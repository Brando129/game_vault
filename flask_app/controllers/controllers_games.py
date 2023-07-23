from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import models_user, models_game
from pprint import pprint
import requests

# GET Routes
# Route for rendering the "consoles" page.
@app.route('/consoles')
def render_consoles_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('consoles.html')

# Route for rendering the "games" page.
@app.route('/games')
def render_games_page():
    if 'user_id' not in session:
        return redirect('/logout')
    """ Get request to Video Games Database Api for all games"""
    rawg_key = "90fdbb86a3864e1ca9ba0dfdd948a58f"
    url = f"https://rawg-video-games-database.p.rapidapi.com/games?key={rawg_key}"
    headers = {
        "X-RapidAPI-Key": "7b12899369msh6c9c430681eef3ep1f7973jsn1dcd54b8a95f",
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    json = response.json()
    results = json['results']
    pprint(results)
    info = {
        "previous_page": json['previous'],
        "next_page": json['next']
    }
    print("*"*50)
    print(info)
    print("*"*50)

    games = []

    for result in results:
        game = {
            "id": result['id'],
            "name": result['name'],
            "short_screenshots": result['short_screenshots'][0]['image'],
            "released": result['released'],
            "platforms": result['platforms'][0]['platform']['name'],
            "rating": result['rating'],
            "genres": result['genres'][0]['name']
        }
        games.append(game)

    return render_template('games.html', games=games, info=info)

# Route for rendering the "peripherals" page.
@app.route('/peripherals')
def render_peripherals_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('peripherals.html')

# Route for rendering the "print media" page.
@app.route('/print/media')
def render_print_media_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('print_media.html')

# Route for rendering the "collection summary" page.
@app.route('/collection_summary')
def render_collection_summary_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('collection_summary.html')

# POST ROUTES
# Route for searching for a game.
@app.post('/get_game')
def get_game():
    if 'user_id' not in session:
        return redirect('/')
    pass