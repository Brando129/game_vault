from flask_app import app
from flask import render_template, redirect, session

# Get Routes
# Route for rendering the "Features" page.
@app.get('/features')
def render_features_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('features.html')