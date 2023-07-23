from flask_app import app
from flask import render_template, redirect, session

# GET Routes
# Route for rendering the "consoles" page.
@app.route('/consoles')
def render_consoles_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('consoles.html')