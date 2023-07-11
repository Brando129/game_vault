from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import models_user, models_game

# GET Routes
# Route to take the user to the add game page.
@app.route('/add_game')
def new_game():
    print("Add new game route...")
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    print("Add new game route successful...")
    return render_template('add_game.html', user=models_user.User.get_user_by_id(data))

# Route to take the user back to the home page.
@app.route('/your_collection')
def back_to_collection():
    print("Back to the collection route...")
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    print("Back to the collection route successful...")
    return render_template('homepage.html', user=models_user.User.get_user_by_id(data))

# Route to take the user to the edit game page.
@app.route('/edit_game')
def edit_game():
    print("Edit game route...")
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    print("Edit game route successful...")
    return render_template('edit_game.html', user=models_user.User.get_user_by_id(data))