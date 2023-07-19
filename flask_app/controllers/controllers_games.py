from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import models_user, models_game

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
    return render_template('games.html')

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