from flask_app import app
from flask import render_template, redirect, session
from flask_app.models import models_user

# Get Routes
# Route for rendering the "Collection Summary" page.
@app.get('/collection_summary')
def render_collection_summary():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'user_id': session['user_id']
    }
    collected_games = models_user.User.get_users_collected_games(data)
    return render_template('collection_summary.html', collected_games=collected_games)