from flask_app import app
from flask import render_template, redirect, session
from flask_app.models import models_game
from playsound import playsound

# Get Routes
# Route for rendering the "Collection Summary" page.
@app.get('/collection_summary')
def render_collection_summary():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'user_id': session['user_id']
    }
    collected_games = models_game.Game.get_users_collected_games(data)
    return render_template('collection_summary.html', collected_games=collected_games)

# Route for deleting a game in the user's collection.
@app.get('/destroy_game/collection/<int:id>')
def destroy_collected_game(id):
    # print("Destroying collected game")
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id,
        'user_id': session['user_id']
    }
    models_game.Game.destroy_game(data)
    playsound('flask_app/static/audio/videogame_death.mp3', block=False)
    # print("Game destroyed")
    return redirect('/collection_summary')