from flask_app import app
from flask import render_template, redirect, session

# Get Route
# Route for rendering the "About" page.
@app.get('/about')
def render_about_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('about.html')