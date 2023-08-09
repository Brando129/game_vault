from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_user, models_game
from playsound import playsound
# Bcrypt import
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) # We are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument.

# Get Routes
# Route for rendering the "Registration and login" page.
@app.route('/')
def index():
    return render_template('registration_and_login.html')

# Route for checking if a user is in session.
@app.route('/homepage')
def check_session():
    # print('Checking if user id is in session route...')
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    # print("User in session route was successful...")
    facts = models_game.Game.random_game_facts()
    user_data = {
        'user_id': session['user_id']
    }
    collected_games = models_game.Game.get_users_collected_games(user_data)
    if 'collection_count' not in session:
        session['collection_count'] = len(collected_games)
    return render_template('homepage.html', user=models_user.User.get_user_by_id(data), facts=facts, collected_games=collected_games)

# Route for logging a user out
@app.route('/logout')
def logout():
    print("Logging user out route...")
    session.clear()
    playsound('flask_app/static/audio/ouch.mp3', block=False)
    return redirect('/')

# Post Routes
# Route for creating/registering a user
@app.route('/register', methods=['POST'])
def register():
    # print("Registering a new user route...")
    if not models_user.User.validate_user(request.form):
        # We redirect to the template with the form.
        return redirect('/')
    # Create data object for hashing a user's password.
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']), # Function for generating the hash.
        "confirm_password": request.form['confirm_password']
    }
    """We save the data to the database and are returned a user's id. We put
    this user id into session because when we go back to the dashboard we want
    to check if the user is in session and if they are not we redirect them.
    This is how we keep our applications safe."""
    id = models_user.User.save_user(data)
    session['user_id'] = id
    # print("Register new user route was successful...")
    playsound('flask_app/static/audio/big_impact.mp3', block=False)
    return redirect('/homepage')

# Route for logging a user in.
@app.route('/login', methods=['POST'])
def login():
    # print("Logging in a user route...")
    user = models_user.User.get_user_by_email(request.form)
    if not user:
        flash("Invalid email or password.", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid email or password.", "login")
        return redirect('/')
    session['user_id'] = user.id
    data = {
        'user_id': session['user_id']
    }
    playsound('flask_app/static/audio/big_impact.mp3', block=False)
    # print("Log in route was successful...")
    return redirect('/homepage')
