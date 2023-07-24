from flask_app import app
from flask import render_template, redirect, request, session
from pprint import pprint
import requests

# Route for rendering the "games" page.
# Helper function for changing the "games" page
def make_request(url):
    headers = {
        "X-RapidAPI-Key": "7b12899369msh6c9c430681eef3ep1f7973jsn1dcd54b8a95f",
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.route('/games')
def render_games_page():
    if 'user_id' not in session:
        return redirect('/logout')

    # API key
    rawg_key = "90fdbb86a3864e1ca9ba0dfdd948a58f"

    # Default games page url.
    if not 'url' in session:
        session['url'] = f"https://rawg-video-games-database.p.rapidapi.com/games?key={rawg_key}"

    json = make_request(session['url'])
    results = json['results']

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
            "short_screenshots": result['short_screenshots'][0]['image'],
            "released": result['released'],
            "platforms": result['platforms'][0]['platform']['name'],
            "rating": result['rating'],
            "genres": result['genres'][0]['name']
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
@app.post('/get_game')
def get_game():
    if 'user_id' not in session:
        return redirect('/')
    game = request.form['name']
    print("*"*25)
    print(game)
    print("*"*25)
    rawg_key = "90fdbb86a3864e1ca9ba0dfdd948a58f"
    url = f"https://rawg-video-games-database.p.rapidapi.com/games?game={game},key={rawg_key}"
    pass
